# Agentic OS / Methodology OS

A reusable operating system for running complex Claude Code work with high autonomy, professional-quality output, independent verification, durable state, controlled context, and explicit human authority over consequential decisions.

The repository is the **source of truth**. Claude Code receives a thin global runtime through symlinks and a small `CLAUDE.md` kernel; detailed policies are loaded only when relevant.

## Design Priorities

1. Professional-quality output.
2. Efficient token and context usage.
3. High autonomy for routine execution.
4. Human control over high-impact decisions.
5. Evidence-based completion and independent verification.

The governing rule is:

> Use the lightest workflow that still protects the required quality bar.

## Status

- ✅ Step 1 — Requirements & Philosophy
- ✅ Step 2 — Constitution / Core Principles
- ✅ Step 3 — Project Lifecycle / Orchestration
- ✅ Step 4 — Agent Architecture
- ✅ Step 5 — Model & Effort Routing
- ✅ Step 6 — Context Architecture
- ✅ Step 7 — Project State
- ✅ Step 8 — Delegation Protocol
- ✅ Step 9 — Verification System
- ✅ Step 10 — Skills Architecture
- ✅ Step 11 — Escalation & Autonomy
- ✅ Step 12 — Learning System
- ✅ Step 13 — Evals
- ✅ Step 14 — Claude Code Integration (repository/runtime implementation)
- ➡️ Step 15 — Real Project Trial

Step 14's repository-side implementation is complete. A real local Claude Code smoke/eval run is still required after pulling `dev` onto the target machine; Step 15 begins once that runtime check passes.

## Architecture

```text
User
 ↓
Methodology Project Manager
 ├── Implementer   — bounded change + self-verification
 ├── Reviewer      — independent, read-only review
 └── Debugger      — diagnosis-first, read-only investigation

PM
 ↓
independent verification
 ↓
quality / authority gates
 ↓
working branch → PR → dev
 ↓
explicit user approval
 ↓
main
```

V0 deliberately keeps orchestration shallow: workers do not recursively manage other workers. Complexity is added only when evidence shows a real benefit.

## Lifecycle

Three execution depths are available:

- **Lite** — small, low-risk, well-understood work.
- **Standard** — normal multi-step or medium-risk work.
- **Full** — large, high-risk, ambiguous, long-running, or coordination-heavy work.

Canonical lifecycle:

```text
INTAKE → TRIAGE → [INVESTIGATE] → PLAN → [HUMAN GATE] → PREPARE
                                                        ↓
                                                   EXECUTE
                                                        ↓
                                                     VERIFY
                                                        ↓
                                                    [REVIEW]
                                                        ↓
                                                    INTEGRATE
                                                        ↓
                                                  SYSTEM CHECK
                                                        ↓
                                                    COMPLETE
```

Verification failure routes through diagnosis/replanning rather than blind retry.

## Core Runtime Rules

### Delegation

PM→worker work is bounded by `templates/TASK_PACKET.md`; execution workers return `templates/WORK_REPORT.md`.

Worker execution states:

```text
PASS | PARTIAL | BLOCKED | FAILED
```

Worker `PASS` is only a claim eligible for PM verification — never project truth by itself.

### Verification

`core/QUALITY_GATES.md` is canonical.

| Risk | PM verification | Independent Reviewer |
| --- | --- | --- |
| Low | required for delegated work | normally no |
| Medium | required | required |
| High | deep | required, deep |

Verification states:

```text
PASS | FAIL | INCONCLUSIVE | NOT_RUN | N/A
```

Human approval never converts missing/failed technical evidence into `PASS`.

### Authority

`core/ESCALATION_POLICY.md` separates authority from technical risk:

```text
A0 — AUTONOMOUS
A1 — AUTONOMOUS + RECORD
A2 — HUMAN GATE
A3 — BLOCKED
```

Approval envelopes are bounded by action, target, scope, conditions, limits, and freshness. Approval is not transitive.

A clear current request can itself satisfy the gate for that exact action; duplicate confirmation is discouraged.

`main` remains specifically human-gated.

### Context

`core/CONTEXT_POLICY.md` treats context as a working set, not an archive.

Keep durable truth in project artifacts; keep high-volume logs/searches local to workers; return compact evidence to the PM. Prefer references to copied history.

### Routing

`core/ROUTING.md` routes model capability separately from effort.

```text
Haiku  → tiny/mechanical
Sonnet → normal bounded execution
Opus   → complex reasoning / difficult debugging / high-risk review
Fable  → hardest long-horizon, highly ambiguous work
```

Missing context, bad decomposition, or environment failures are fixed directly. Insufficient reasoning depth normally raises effort before model family; genuine capability gaps raise model capability.

### Skills

Skills are optional capability modules and are loaded on demand. Generic workers preload none in V0.

Global Methodology OS skills:

- `methodology-os`
- `methodology-planning`
- `methodology-handoff`
- `methodology-retrospective`

Skill availability never expands authority.

### Learning

Global learning is governed by `core/LEARNING_POLICY.md`:

```text
OBSERVATION
   ↓
CANDIDATE
   ↓
NEEDS_EVIDENCE / VALIDATING
   ↓
READY_FOR_PROMOTION
   ↓
HUMAN PROMOTION GATE
   ↓
IMPLEMENT + EVAL + VERIFY
   ↓
PROMOTED
```

Project-specific learning stays local. A global candidate is never active policy until explicitly promoted and integrated through normal quality gates.

## Project State

Canonical durable artifacts:

| Artifact | Purpose |
| --- | --- |
| `PROJECT_BRIEF.md` | stable outcome, scope, constraints, success criteria |
| `PLAN.md` | intended path, tasks, dependencies, acceptance |
| `STATE.md` | current operational truth |
| `DECISIONS.md` | durable material decisions and bounded approvals |
| `HANDOFF.md` | compressed ownership transfer |
| `LEARNING_CANDIDATE.md` | durable global-learning candidate when warranted |

`STATE.md` is the sole hot operational snapshot. The other artifacts should not become parallel status trackers.

## Claude Code Installation

The repository remains canonical. The installer creates only a thin global runtime under `~/.claude`.

From the repository root:

```bash
bash install.sh
bash install.sh --check
```

Installed layout:

```text
~/.claude/
├── methodology-os -> <this checkout>
├── CLAUDE.md
│    └── managed import → runtime/CLAUDE.md
├── agents/
│    ├── methodology-project-manager.md
│    ├── methodology-implementer.md
│    ├── methodology-reviewer.md
│    └── methodology-debugger.md
└── skills/
     ├── methodology-os
     ├── methodology-planning
     ├── methodology-handoff
     └── methodology-retrospective
```

Global agent names are intentionally namespaced to avoid collisions with project-specific agents. Runtime adapters load the canonical role contracts from this repository instead of duplicating them.

The installer:

- is idempotent in installed state;
- preserves existing user `CLAUDE.md` content;
- manages only a clearly marked import block;
- backs up regular `CLAUDE.md` before editing;
- refuses to overwrite conflicting agent/skill paths unless `--force` is explicit;
- removes only paths it owns during `--uninstall`.

Full Methodology OS session:

```bash
claude --agent methodology-project-manager
```

Lightweight use from a normal Claude Code session:

```text
/methodology-os
```

Detailed runtime documentation: `runtime/README.md`.

## Evals

The V0 eval framework protects behavioral invariants rather than raw coding intelligence.

Static validation requires no Claude model calls:

```bash
python3 scripts/run_evals.py --static-only
```

Blocking core behavioral suite:

```bash
python3 scripts/run_evals.py core-v0
```

Optional deeper semantic evaluation:

```bash
python3 scripts/run_evals.py core-v0 --semantic-judge
```

Targeted suites include `routing-v0` and `learning-v0`; `full-v0` runs all current scenarios.

Behavioral runs use structured JSON, read-only tools, plan permission mode, fresh non-persistent sessions, turn caps, and budget caps. Critical authority/verification/self-modification failures block regardless of aggregate score.

GitHub Actions runs syntax, static-contract, and isolated installer lifecycle checks without consuming Claude tokens.

See `evals/README.md` for the complete eval contract.

## Git Operating Model

```text
dev
 └── task / feature / fix branch
          ↓
      implementation
          ↓
      verification / review
          ↓
       PR → dev
          ↓
         dev
          ↓
   prepare promotion
          ↓
   EXPLICIT USER APPROVAL
          ↓
        main
```

Routine verified integration into `dev` is autonomous unless repository-specific policy is stricter. Direct development on `main` is prohibited.

## Policy Map

Detailed behavior belongs in canonical policy files, not this README:

| Concern | Canonical source |
| --- | --- |
| Requirements | `OS_REQUIREMENTS.md` |
| Constitutional invariants | `core/PRINCIPLES.md` |
| Lifecycle / orchestration | `core/ORCHESTRATION.md` |
| Model / effort routing | `core/ROUTING.md` |
| Context | `core/CONTEXT_POLICY.md` |
| Verification / review | `core/QUALITY_GATES.md` |
| Skills | `core/SKILL_POLICY.md` |
| Human authority | `core/ESCALATION_POLICY.md` |
| Learning / promotion | `core/LEARNING_POLICY.md` |
| Eval framework | `evals/README.md` |
| Claude Code runtime | `runtime/README.md` |

## Repository Layout

```text
Agentic-OS/
├── OS_REQUIREMENTS.md
├── README.md
├── CHANGELOG.md
├── core/
├── agents/
├── skills/
├── templates/
├── evals/
│   ├── scenarios/
│   └── suites/
├── runtime/
│   ├── CLAUDE.md
│   └── agents/
├── scripts/
│   └── run_evals.py
├── install.sh
└── .github/workflows/methodology-static.yml
```

## Next: Step 15 — Real Project Trial

After pulling the Step 14 changes onto a real Claude Code machine:

1. install/check the global runtime;
2. confirm Claude sees the global kernel and namespaced PM;
3. run static checks;
4. run `core-v0` and inspect the baseline;
5. use the OS on one meaningful real project;
6. record quality, token/context behavior, friction, failures, and any learning candidates;
7. revise only from observed evidence.

The goal of V0 is not maximum ceremony. It is a small, inspectable operating system that can prove when additional complexity is worth adding.
