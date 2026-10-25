#!/usr/bin/env python3
"""Small zero-model runtime sanity checker.

This checker complements `run_evals.py --static-only` with a deliberately tiny
surface that can be executed independently when debugging installation/CI.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "runtime" / "CLAUDE.md",
    ROOT / "runtime" / "agents" / "methodology-project-manager.md",
    ROOT / "runtime" / "agents" / "methodology-implementer.md",
    ROOT / "runtime" / "agents" / "methodology-reviewer.md",
    ROOT / "runtime" / "agents" / "methodology-debugger.md",
    ROOT / "skills" / "methodology-start" / "SKILL.md",
    ROOT / "skills" / "methodology-os" / "SKILL.md",
    ROOT / "skills" / "methodology-planning" / "SKILL.md",
    ROOT / "skills" / "methodology-handoff" / "SKILL.md",
    ROOT / "skills" / "methodology-retrospective" / "SKILL.md",
]


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.exists()]
    if missing:
        for path in missing:
            print(f"MISSING: {path}", file=sys.stderr)
        return 1

    kernel = (ROOT / "runtime" / "CLAUDE.md").read_text(encoding="utf-8")
    if "Never merge/promote to `main` without explicit approval" not in kernel:
        print("MISSING: runtime main human-gate rule", file=sys.stderr)
        return 1
    if "global OS learning as a proposal" not in kernel:
        print("MISSING: runtime global-learning promotion rule", file=sys.stderr)
        return 1

    print("Runtime sanity: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
