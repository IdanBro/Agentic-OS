#!/usr/bin/env python3
"""Zero-model sanity checker for the Agentic OS Claude Code plugin."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "hooks" / "hooks.json",
    ROOT / "scripts" / "session-start.sh",
    ROOT / "agents" / "project-manager.md",
    ROOT / "agents" / "implementer.md",
    ROOT / "agents" / "reviewer.md",
    ROOT / "agents" / "debugger.md",
    ROOT / "skills" / "pm-mode" / "SKILL.md",
    ROOT / "skills" / "methodology-os" / "SKILL.md",
    ROOT / "skills" / "methodology-planning" / "SKILL.md",
    ROOT / "skills" / "methodology-handoff" / "SKILL.md",
    ROOT / "skills" / "methodology-retrospective" / "SKILL.md",
    ROOT / "core" / "PRINCIPLES.md",
    ROOT / "core" / "QUALITY_GATES.md",
    ROOT / "core" / "ESCALATION_POLICY.md",
    ROOT / "templates" / "TASK_PACKET.md",
    ROOT / "templates" / "WORK_REPORT.md",
]


def fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return 1


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.exists()]
    if missing:
        for path in missing:
            print(f"MISSING: {path}", file=sys.stderr)
        return 1

    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "agentic-os":
        return fail("plugin manifest name must be agentic-os")

    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    matches = [p for p in marketplace.get("plugins", []) if p.get("name") == "agentic-os"]
    if len(matches) != 1 or matches[0].get("source") != "./":
        return fail("marketplace must expose exactly one root agentic-os plugin")

    hook = json.loads((ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))
    if "SessionStart" not in hook:
        return fail("SessionStart routing hook is required")

    start = (ROOT / "skills" / "pm-mode" / "SKILL.md").read_text(encoding="utf-8")
    if "${CLAUDE_PLUGIN_ROOT}" not in start:
        return fail("pm-mode must use CLAUDE_PLUGIN_ROOT")
    remote_loader_markers = ["gh api", "METHODOLOGY_OS_REPO=", "GITHUB_TOKEN", "GH_TOKEN"]
    if any(marker in start for marker in remote_loader_markers):
        return fail("pm-mode must not perform runtime GitHub control-plane fetching")

    agent_expectations = {
        "implementer.md": ["Agent", "AskUserQuestion"],
        "reviewer.md": ["Edit", "Write", "NotebookEdit", "Agent"],
        "debugger.md": ["Edit", "Write", "NotebookEdit", "Agent"],
    }
    for filename, denied in agent_expectations.items():
        text = (ROOT / "agents" / filename).read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)[1]
        for tool in denied:
            if tool not in frontmatter:
                return fail(f"{filename}: missing denied tool {tool}")

    principles = (ROOT / "core" / "PRINCIPLES.md").read_text(encoding="utf-8")
    if "Main Is Human-Gated" not in principles:
        return fail("main human-gate invariant missing")
    if "Global Learning Requires Human Promotion" not in principles:
        return fail("global-learning human-promotion invariant missing")
    if "The PM Orchestrates Standard/Full Work" not in principles:
        return fail("PM delegation invariant missing")

    scenario = ROOT / "evals" / "scenarios" / "E-015-full-build-requires-delegation.json"
    if not scenario.is_file():
        return fail("delegation regression scenario E-015 is missing")

    print("Plugin runtime sanity: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
