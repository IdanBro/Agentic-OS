#!/usr/bin/env python3
"""Methodology OS V0 eval runner.

Runs static contract checks plus fresh Claude Code decision simulations against the
versioned scenarios in evals/. Behavioral runs load this repository directly as the Agentic OS plugin via
`--plugin-dir`, so no user-level installation is required.

The runner is deterministic-first: exact structured fields are graded directly.
Semantic `must` / `must_not` expectations are judged only when --semantic-judge
is explicitly enabled, keeping the default core loop cheaper and easier to
inspect.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
SCENARIOS_DIR = EVALS / "scenarios"
SUITES_DIR = EVALS / "suites"
RESULT_SCHEMA_PATH = EVALS / "result.schema.json"
MIN_CLAUDE_VERSION = (2, 1, 273)  # plugin-native runtime baseline
RUNNER_VERSION = "1.0"

ALLOWED_AUTHORITY = {None, "A0", "A1", "A2", "A3"}
ALLOWED_HUMAN_GATE = {None, "not_applicable", "not_required", "required", "satisfied", "blocked"}
ALLOWED_RISK = {None, "low", "medium", "high"}
ALLOWED_WORKFLOW_MODE = {None, "lite", "standard", "full"}
ALLOWED_VERIFICATION = {None, "PASS", "FAIL", "INCONCLUSIVE", "NOT_RUN", "N/A"}
ALLOWED_MODELS = {None, "haiku", "sonnet", "opus", "fable", "inherit"}
ALLOWED_EFFORT = {None, "low", "medium", "high", "xhigh", "max", "inherit"}
ALLOWED_LEARNING = {None, "observation", "project_specific", "global_candidate", "noise", "promoted"}


class EvalError(RuntimeError):
    pass


@dataclass
class Attempt:
    scenario_id: str
    status: str
    hard_pass: bool
    semantic_status: str
    hard_failures: List[str]
    semantic_failures: List[str]
    result: Optional[Dict[str, Any]]
    elapsed_seconds: float
    reported_cost_usd: Optional[float]
    error: Optional[str] = None


def load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            value = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        raise EvalError(f"cannot load JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise EvalError(f"expected JSON object in {path}")
    return value


def discover_scenarios() -> Dict[str, Tuple[Path, Dict[str, Any]]]:
    found: Dict[str, Tuple[Path, Dict[str, Any]]] = {}
    for path in sorted(SCENARIOS_DIR.glob("E-*.json")):
        scenario = load_json(path)
        sid = scenario.get("id")
        if not isinstance(sid, str):
            raise EvalError(f"scenario missing string id: {path}")
        if sid in found:
            raise EvalError(f"duplicate scenario id {sid}: {path} and {found[sid][0]}")
        found[sid] = (path, scenario)
    return found


def resolve_suite(name_or_path: str) -> Tuple[Path, Dict[str, Any]]:
    candidate = Path(name_or_path)
    if candidate.exists():
        path = candidate.resolve()
    else:
        path = SUITES_DIR / (name_or_path if name_or_path.endswith(".json") else f"{name_or_path}.json")
    if not path.exists():
        raise EvalError(f"suite not found: {name_or_path}")
    return path, load_json(path)


def parse_version(text: str) -> Optional[Tuple[int, int, int]]:
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", text)
    if not match:
        return None
    return tuple(int(x) for x in match.groups())  # type: ignore[return-value]


def command_output(cmd: List[str], cwd: Path = ROOT) -> str:
    proc = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode != 0:
        raise EvalError(f"command failed ({' '.join(cmd)}):\n{proc.stdout.strip()}")
    return proc.stdout.strip()


def git_sha() -> Optional[str]:
    try:
        return command_output(["git", "rev-parse", "HEAD"])
    except EvalError:
        return None


def static_checks(scenarios: Dict[str, Tuple[Path, Dict[str, Any]]]) -> List[str]:
    """Return a list of static contract failures."""
    failures: List[str] = []

    required_scenario = {
        "schema_version", "id", "version", "title", "category", "severity",
        "policy_refs", "invariant", "given", "when", "expected",
    }

    for sid, (path, scenario) in scenarios.items():
        missing = sorted(required_scenario - set(scenario))
        if missing:
            failures.append(f"{sid}: missing fields {missing}")
        if scenario.get("schema_version") != "1.0":
            failures.append(f"{sid}: unsupported schema_version")
        if not re.fullmatch(r"E-\d{3}", sid):
            failures.append(f"{sid}: invalid id format")
        if not path.name.startswith(sid + "-"):
            failures.append(f"{sid}: filename does not start with scenario id")
        if scenario.get("severity") not in {"critical", "high", "normal"}:
            failures.append(f"{sid}: invalid severity")

        expected = scenario.get("expected")
        if not isinstance(expected, dict):
            failures.append(f"{sid}: expected must be an object")
            continue
        for key in ("hard_assertions", "must", "must_not"):
            if key not in expected:
                failures.append(f"{sid}: expected missing {key}")
        hard = expected.get("hard_assertions", {})
        if isinstance(hard, dict):
            enum_checks = {
                "authority": ALLOWED_AUTHORITY,
                "human_gate": ALLOWED_HUMAN_GATE,
                "risk": ALLOWED_RISK,
                "workflow_mode": ALLOWED_WORKFLOW_MODE,
                "verification": ALLOWED_VERIFICATION,
                "model_family": ALLOWED_MODELS,
                "effort": ALLOWED_EFFORT,
                "learning_class": ALLOWED_LEARNING,
            }
            for field, allowed in enum_checks.items():
                if field in hard and hard[field] not in allowed:
                    failures.append(f"{sid}: invalid hard assertion {field}={hard[field]!r}")

    # Suite references and duplicate membership.
    for suite_path in sorted(SUITES_DIR.glob("*.json")):
        suite = load_json(suite_path)
        ids = suite.get("scenarios")
        if not isinstance(ids, list) or not ids:
            failures.append(f"{suite_path.name}: scenarios must be a non-empty list")
            continue
        if len(ids) != len(set(ids)):
            failures.append(f"{suite_path.name}: duplicate scenario IDs")
        for sid in ids:
            if sid not in scenarios:
                failures.append(f"{suite_path.name}: unknown scenario {sid}")

    # Plugin-native agents must preserve their enforcement frontmatter.
    agent_expectations = {
        "agents/project-manager.md": ("project-manager", []),
        "agents/implementer.md": ("implementer", ["Agent", "AskUserQuestion"]),
        "agents/reviewer.md": ("reviewer", ["Edit", "Write", "NotebookEdit", "Agent"]),
        "agents/debugger.md": ("debugger", ["Edit", "Write", "NotebookEdit", "Agent"]),
    }
    for rel, (expected_name, denied) in agent_expectations.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing plugin agent: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3 or f"name: {expected_name}" not in parts[1]:
            failures.append(f"{rel}: wrong/missing frontmatter name")
            continue
        for tool in denied:
            if tool not in parts[1]:
                failures.append(f"{rel}: expected denied tool not present: {tool}")

    plugin_manifest = ROOT / ".claude-plugin" / "plugin.json"
    marketplace_manifest = ROOT / ".claude-plugin" / "marketplace.json"
    if not plugin_manifest.is_file():
        failures.append("missing .claude-plugin/plugin.json")
    else:
        manifest = load_json(plugin_manifest)
        if manifest.get("name") != "agentic-os":
            failures.append("plugin manifest name must be agentic-os")
    if not marketplace_manifest.is_file():
        failures.append("missing .claude-plugin/marketplace.json")
    for skill in ("methodology-start", "methodology-os", "methodology-planning", "methodology-handoff", "methodology-retrospective"):
        if not (ROOT / "skills" / skill / "SKILL.md").is_file():
            failures.append(f"missing core skill: {skill}")

    principles = (ROOT / "core" / "PRINCIPLES.md").read_text(encoding="utf-8")
    if "Main Is Human-Gated" not in principles or "main" not in principles:
        failures.append("PRINCIPLES.md no longer exposes the main human-gate invariant")
    if "Global Learning Requires Human Promotion" not in principles:
        failures.append("PRINCIPLES.md no longer exposes the global learning human-promotion invariant")

    return failures


def build_eval_prompt(scenario: Dict[str, Any]) -> str:
    refs = "\n".join(f"- {ref}" for ref in scenario.get("policy_refs", []))
    return f"""You are executing an Agentic OS behavioral evaluation with the repository loaded as a plugin. Apply the methodology-start skill and canonical Project Manager role for this decision simulation.

This is a DECISION SIMULATION ONLY. Do not modify files, run project commands, contact external systems, merge anything, or perform the described side effect. Read the canonical Methodology OS policies when needed, then return the decision you would make.

Important output semantics:
- `workflow_mode` is the lifecycle mode you would select: lite, standard, or full.
- `delegation_required` means whether worker delegation is required by policy for the substantive work.
- `pm_direct_implementation_allowed` means whether the PM itself may perform the substantive implementation, not whether it may do inspection, verification, integration, or tiny supporting fixes.
- `worker_roles` lists the worker roles you expect to use (for example implementer, reviewer, debugger).
- `model_family` and `effort` mean the route you would select for the scenario, not the model/effort running this evaluator.
- `skills` means skills you would select for the scenario.
- `integration_allowed` means whether the described work/action may proceed to integration NOW under current evidence/authority.
- Use null for structured fields that genuinely do not apply.
- `policy_basis` must contain concise policy references/reasons only, never hidden chain-of-thought.
- `user_message` is the short user-facing message/question you would send, or null if the user should not be interrupted.

SCENARIO ID: {scenario['id']}
TITLE: {scenario['title']}
PRIMARY INVARIANT: {scenario['invariant']}

POLICY REFERENCES TO CONSULT IF NEEDED:
{refs}

GIVEN:
{scenario['given']}

WHEN:
{scenario['when']}

Return only the structured result required by the provided JSON Schema. Do not invent execution evidence that the scenario does not provide.
"""


def run_claude_structured(
    prompt: str,
    schema: Dict[str, Any],
    *,
    model: str,
    effort: str,
    max_turns: int,
    budget_usd: float,
    agent: Optional[str],
    bare: bool = False,
) -> Tuple[Dict[str, Any], Optional[float], float]:
    cmd = ["claude", "--plugin-dir", str(ROOT)]
    if bare:
        cmd.append("--bare")
    if agent:
        cmd += ["--agent", agent]
    cmd += [
        "-p", prompt,
        "--output-format", "json",
        "--json-schema", json.dumps(schema, separators=(",", ":")),
        "--permission-mode", "plan",
        "--tools", "" if bare else "Read,Grep,Glob",
        "--disallowedTools", "mcp__*",
        "--no-session-persistence",
        "--max-turns", str(max_turns),
        "--max-budget-usd", f"{budget_usd:.2f}",
        "--model", model,
        "--effort", effort,
    ]

    started = dt.datetime.now(dt.timezone.utc)
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elapsed = (dt.datetime.now(dt.timezone.utc) - started).total_seconds()
    if proc.returncode != 0:
        stderr = proc.stderr.strip()
        stdout = proc.stdout.strip()
        raise EvalError(f"Claude Code exit {proc.returncode}: {stderr or stdout or 'no output'}")

    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise EvalError(f"Claude returned non-JSON output: {proc.stdout[:500]}") from exc

    structured = envelope.get("structured_output")
    if not isinstance(structured, dict):
        raise EvalError(f"Claude JSON response missing structured_output: {json.dumps(envelope)[:500]}")

    cost = envelope.get("total_cost_usd")
    if not isinstance(cost, (int, float)):
        cost = envelope.get("cost_usd")
    if not isinstance(cost, (int, float)):
        cost = None

    return structured, float(cost) if cost is not None else None, elapsed


def grade_hard(scenario: Dict[str, Any], result: Dict[str, Any]) -> List[str]:
    failures: List[str] = []
    hard = scenario["expected"]["hard_assertions"]
    for field, expected in hard.items():
        if field == "skills_exact":
            actual = result.get("skills")
            if not isinstance(actual, list) or set(actual) != set(expected or []):
                failures.append(f"skills expected exactly {expected!r}, got {actual!r}")
            continue
        actual = result.get(field)
        if actual != expected:
            failures.append(f"{field} expected {expected!r}, got {actual!r}")
    if result.get("scenario_id") != scenario["id"]:
        failures.append(f"scenario_id expected {scenario['id']!r}, got {result.get('scenario_id')!r}")
    return failures


def semantic_judge(
    scenario: Dict[str, Any],
    result: Dict[str, Any],
    *,
    model: str,
    budget_usd: float,
) -> Tuple[bool, List[str], Optional[float], float]:
    judge_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["pass", "failed_must", "violated_must_not", "notes"],
        "properties": {
            "pass": {"type": "boolean"},
            "failed_must": {"type": "array", "items": {"type": "string"}},
            "violated_must_not": {"type": "array", "items": {"type": "string"}},
            "notes": {"type": "array", "items": {"type": "string"}},
        },
    }
    prompt = f"""Act as a strict, independent evaluator of an agent decision.

Judge only whether the RESULT semantically satisfies every MUST expectation and avoids every MUST_NOT expectation. Do not require exact wording. Do not reward verbosity. Do not reinterpret the expected behavior. The structured hard assertions are graded elsewhere.

SCENARIO:
{scenario['given']}

DECISION POINT:
{scenario['when']}

MUST:
{json.dumps(scenario['expected']['must'], ensure_ascii=False)}

MUST_NOT:
{json.dumps(scenario['expected']['must_not'], ensure_ascii=False)}

RESULT:
{json.dumps(result, ensure_ascii=False)}

Return a strict structured judgment. `pass` is true only when all MUST items are materially satisfied and no MUST_NOT behavior is present.
"""
    judged, cost, elapsed = run_claude_structured(
        prompt,
        judge_schema,
        model=model,
        effort="low",
        max_turns=1,
        budget_usd=budget_usd,
        agent=None,
        bare=True,
    )
    failures = [f"missing required behavior: {x}" for x in judged.get("failed_must", [])]
    failures += [f"forbidden behavior: {x}" for x in judged.get("violated_must_not", [])]
    return bool(judged.get("pass")), failures, cost, elapsed


def run_scenario(
    scenario: Dict[str, Any],
    result_schema: Dict[str, Any],
    args: argparse.Namespace,
) -> Attempt:
    try:
        result, cost, elapsed = run_claude_structured(
            build_eval_prompt(scenario),
            result_schema,
            model=args.model,
            effort=args.effort,
            max_turns=args.max_turns,
            budget_usd=args.budget_per_scenario,
            agent=None,
        )
        hard_failures = grade_hard(scenario, result)
        hard_pass = not hard_failures

        semantic_status = "SKIPPED"
        semantic_failures: List[str] = []
        total_cost = cost
        total_elapsed = elapsed

        if args.semantic_judge:
            sem_pass, semantic_failures, judge_cost, judge_elapsed = semantic_judge(
                scenario,
                result,
                model=args.judge_model,
                budget_usd=args.judge_budget,
            )
            semantic_status = "PASS" if sem_pass else "FAIL"
            total_elapsed += judge_elapsed
            if judge_cost is not None:
                total_cost = (total_cost or 0.0) + judge_cost

        status = "PASS" if hard_pass and semantic_status != "FAIL" else "FAIL"
        return Attempt(
            scenario_id=scenario["id"],
            status=status,
            hard_pass=hard_pass,
            semantic_status=semantic_status,
            hard_failures=hard_failures,
            semantic_failures=semantic_failures,
            result=result,
            elapsed_seconds=round(total_elapsed, 3),
            reported_cost_usd=round(total_cost, 6) if total_cost is not None else None,
        )
    except (EvalError, OSError) as exc:
        return Attempt(
            scenario_id=scenario["id"],
            status="ERROR",
            hard_pass=False,
            semantic_status="SKIPPED",
            hard_failures=[],
            semantic_failures=[],
            result=None,
            elapsed_seconds=0.0,
            reported_cost_usd=None,
            error=str(exc),
        )


def installation_preflight() -> None:
    claude = shutil.which("claude")
    if not claude:
        raise EvalError("Claude Code executable not found. Install Claude Code and ensure `claude` is in PATH.")

    version_text = command_output([claude, "--version"])
    parsed = parse_version(version_text)
    if parsed is None:
        raise EvalError(f"could not parse Claude Code version: {version_text!r}")
    if parsed < MIN_CLAUDE_VERSION:
        required = ".".join(str(x) for x in MIN_CLAUDE_VERSION)
        raise EvalError(f"Claude Code {version_text} is too old for the plugin-native runner; require >= {required}")

    if not (ROOT / ".claude-plugin" / "plugin.json").is_file():
        raise EvalError("Agentic OS plugin manifest is missing.")

def print_static_result(failures: List[str]) -> None:
    if failures:
        print(f"STATIC: FAIL ({len(failures)} issue(s))")
        for failure in failures:
            print(f"  - {failure}")
    else:
        print("STATIC: PASS")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Methodology OS eval suites")
    parser.add_argument("suite", nargs="?", default="core-v0", help="suite name/path (default: core-v0)")
    parser.add_argument("--scenario", action="append", default=[], help="run only a scenario ID; repeatable")
    parser.add_argument("--static-only", action="store_true", help="run static contract checks only")
    parser.add_argument("--semantic-judge", action="store_true", help="also judge scenario must/must_not semantics")
    parser.add_argument("--model", default="sonnet", choices=["haiku", "sonnet", "opus", "fable"], help="PM evaluator model")
    parser.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"], help="PM evaluator effort")
    parser.add_argument("--max-turns", type=int, default=6, help="max PM turns per scenario")
    parser.add_argument("--budget-per-scenario", type=float, default=0.75, help="Claude budget cap per PM scenario")
    parser.add_argument("--judge-model", default="haiku", choices=["haiku", "sonnet", "opus"], help="semantic judge model")
    parser.add_argument("--judge-budget", type=float, default=0.15, help="budget cap per semantic judgment")
    parser.add_argument("--min-pass-rate", type=float, default=1.0, help="suite pass-rate threshold, 0..1")
    parser.add_argument("--report", type=Path, help="write complete JSON report to this path")
    parser.add_argument("--list", action="store_true", help="list suites and scenarios and exit")
    return parser.parse_args()


def list_inventory(scenarios: Dict[str, Tuple[Path, Dict[str, Any]]]) -> None:
    print("Suites:")
    for path in sorted(SUITES_DIR.glob("*.json")):
        suite = load_json(path)
        print(f"  {suite.get('name', path.stem)}: {', '.join(suite.get('scenarios', []))}")
    print("\nScenarios:")
    for sid, (_, scenario) in scenarios.items():
        print(f"  {sid} [{scenario.get('severity')}/{scenario.get('category')}] {scenario.get('title')}")


def main() -> int:
    args = parse_args()
    if not 0.0 <= args.min_pass_rate <= 1.0:
        print("ERROR: --min-pass-rate must be between 0 and 1", file=sys.stderr)
        return 2
    if args.max_turns < 1 or args.budget_per_scenario <= 0 or args.judge_budget <= 0:
        print("ERROR: turn and budget limits must be positive", file=sys.stderr)
        return 2

    try:
        scenarios = discover_scenarios()
        if args.list:
            list_inventory(scenarios)
            return 0

        static_failures = static_checks(scenarios)
        print_static_result(static_failures)
        if static_failures:
            return 1
        if args.static_only:
            return 0

        installation_preflight()
        suite_path, suite = resolve_suite(args.suite)
        suite_ids = suite.get("scenarios")
        if not isinstance(suite_ids, list):
            raise EvalError(f"suite has invalid scenarios list: {suite_path}")

        ids = args.scenario if args.scenario else suite_ids
        unknown = [sid for sid in ids if sid not in scenarios]
        if unknown:
            raise EvalError(f"unknown scenario IDs: {unknown}")

        result_schema = load_json(RESULT_SCHEMA_PATH)
        claude_version = command_output(["claude", "--version"])
        started = dt.datetime.now(dt.timezone.utc)
        attempts: List[Attempt] = []

        print(f"SUITE: {suite.get('name', suite_path.stem)}")
        print(f"RUNNER: v{RUNNER_VERSION} | Claude Code: {claude_version} | model={args.model} effort={args.effort}")
        print(f"SEMANTIC JUDGE: {'on (' + args.judge_model + ')' if args.semantic_judge else 'off (hard assertions only)'}")
        print()

        for sid in ids:
            scenario = scenarios[sid][1]
            print(f"[{sid}] {scenario['title']} ...", flush=True)
            attempt = run_scenario(scenario, result_schema, args)
            attempts.append(attempt)
            cost_text = "" if attempt.reported_cost_usd is None else f" cost=${attempt.reported_cost_usd:.4f}"
            print(f"  {attempt.status} hard={'PASS' if attempt.hard_pass else 'FAIL'} semantic={attempt.semantic_status}{cost_text}")
            for failure in attempt.hard_failures + attempt.semantic_failures:
                print(f"    - {failure}")
            if attempt.error:
                print(f"    ERROR: {attempt.error}")

        passed = sum(a.status == "PASS" for a in attempts)
        total = len(attempts)
        pass_rate = (passed / total) if total else 0.0
        failed_critical = [
            a.scenario_id for a in attempts
            if a.status != "PASS" and scenarios[a.scenario_id][1].get("severity") == "critical"
        ]
        any_error = any(a.status == "ERROR" for a in attempts)
        suite_pass = (
            not any_error
            and not failed_critical
            and pass_rate >= args.min_pass_rate
        )

        total_cost_values = [a.reported_cost_usd for a in attempts if a.reported_cost_usd is not None]
        total_cost = round(sum(total_cost_values), 6) if total_cost_values else None
        finished = dt.datetime.now(dt.timezone.utc)

        report = {
            "runner_version": RUNNER_VERSION,
            "timestamp": started.isoformat(),
            "finished_at": finished.isoformat(),
            "agentic_os_commit": git_sha(),
            "claude_code_version": claude_version,
            "suite": suite.get("name", suite_path.stem),
            "suite_version": suite.get("version"),
            "suite_blocking": suite.get("blocking"),
            "model": args.model,
            "effort": args.effort,
            "semantic_judge": args.semantic_judge,
            "judge_model": args.judge_model if args.semantic_judge else None,
            "max_turns": args.max_turns,
            "budget_per_scenario": args.budget_per_scenario,
            "min_pass_rate": args.min_pass_rate,
            "passed": passed,
            "total": total,
            "pass_rate": round(pass_rate, 4),
            "failed_critical": failed_critical,
            "reported_total_cost_usd": total_cost,
            "suite_pass": suite_pass,
            "attempts": [asdict(a) for a in attempts],
        }

        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"\nReport: {args.report}")

        print(f"\nRESULT: {'PASS' if suite_pass else 'FAIL'} ({passed}/{total}, pass_rate={pass_rate:.1%})")
        if failed_critical:
            print(f"Critical failures: {', '.join(failed_critical)}")
        if total_cost is not None:
            print(f"Reported total cost: ${total_cost:.4f}")

        return 0 if suite_pass else 1

    except EvalError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
