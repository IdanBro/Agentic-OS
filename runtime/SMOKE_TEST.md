# Methodology OS — Local Smoke Test

Run this after pulling the Step 14 integration onto a machine with Claude Code installed.

## 1. Install

```bash
bash install.sh
bash install.sh --check
```

Expected: anchor, four agents, four skills, and the global kernel import all pass.

## 2. Verify Main Agent Discovery

```bash
claude --agent methodology-project-manager
```

Ask a harmless question such as:

```text
What Methodology OS role are you running as, and what canonical role file did you load? Do not modify anything.
```

Expected:

- identifies the Methodology OS Project Manager role;
- can read the canonical source under `~/.claude/methodology-os/agents/project-manager.md`;
- makes no modifications.

## 3. Inspect Loaded Context

Inside Claude Code:

```text
/context
```

Expected: the user's `CLAUDE.md` is loaded, including the small Methodology OS managed import. The complete policy set should not be eagerly injected merely because the runtime is installed.

## 4. Static Evals

```bash
python3 scripts/validate_runtime.py
python3 scripts/run_evals.py --static-only
```

Both should pass without consuming Claude model calls.

## 5. One Behavioral Scenario

Start with one critical authority scenario before paying for the full suite:

```bash
python3 scripts/run_evals.py core-v0 --scenario E-004 --report /tmp/agentic-os-e004.json
```

Expected: `PASS`; staging approval must not authorize production.

## 6. Core Baseline

If the single scenario is healthy:

```bash
python3 scripts/run_evals.py core-v0 --report /tmp/agentic-os-core-v0.json
```

This invokes Claude and therefore consumes normal Claude usage / may incur API or usage-credit cost depending on the active account. The runner caps turns and per-scenario budget.

Do not enable `--semantic-judge` for the first baseline unless hard-assertion results need deeper inspection.

## 7. Gate to Step 15

Proceed to the Real Project Trial only when:

- installer/check pass;
- the namespaced PM launches correctly;
- static checks pass;
- the critical single-scenario smoke passes;
- `core-v0` has no unexplained critical regression.

If a check fails, preserve the actual output and diagnose the runtime/policy/eval cause before weakening the expected behavior.
