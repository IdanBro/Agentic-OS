# Methodology OS

A reusable operating methodology for running complex Claude-based work with high autonomy, professional quality, strong verification, and efficient context/token usage.

The OS is designed as a global, project-agnostic core that can be specialized for engineering, DevOps, research, planning, writing, and other multi-stage work.

## Design Priorities

1. Professional-quality output.
2. Efficient token and context usage.
3. High autonomy for routine execution.
4. Human control over high-impact decisions.
5. Evidence-based completion and independent verification.

## Current Status

- Step 1 — Requirements & Philosophy: complete
- Step 2 — Constitution / Core Principles: complete
- Step 3 — Project Lifecycle / Orchestration: complete
- Step 4 — Agent Architecture: complete
- Step 5 — Model & Effort Routing: next

The current orchestration layer defines three execution depths:

- **Lite** — small, low-risk, well-understood work with minimal ceremony.
- **Standard** — normal multi-step work with planning, bounded execution, and verification.
- **Full** — large, ambiguous, high-risk, long-running, or highly parallel work with structured investigation, review, integration, and handoff behavior.

The guiding rule is:

> Use the lightest workflow that still protects the required quality bar.

## Core Lifecycle

```text
INTAKE
  ↓
TRIAGE
  ↓
[INVESTIGATE]
  ↓
PLAN
  ↓
[HUMAN GATE]
  ↓
PREPARE
  ↓
EXECUTE TASK
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

Failed verification routes through diagnosis and replanning rather than blind retry loops.

## Agent Architecture

V0 deliberately starts with four roles:

| Agent | Role | Default authority |
| --- | --- | --- |
| `project-manager` | Owns lifecycle, planning, routing, verification, state, Git integration, and human gates | Orchestrates and integrates |
| `implementer` | Executes one bounded task and self-verifies the resulting change | May modify scoped work |
| `reviewer` | Independently checks requirements, correctness, regressions, and verification quality | Read-only |
| `debugger` | Diagnoses non-trivial failures and returns root cause, fix direction, and validation plan | Read-only / diagnosis-first |

The PM is intended to run as the main Claude Code session agent. Workers receive bounded task context and return compact evidence-oriented reports.

Worker nesting is intentionally disabled in V0 even though current Claude Code supports nested subagents. The PM remains the single orchestration authority until observed use cases justify deeper delegation.

Agent definitions currently use `model: inherit`. Claude Code supports per-invocation model selection for subagents, so concrete Sonnet / Opus / Fable and effort-routing policy is intentionally centralized in Step 5 rather than hard-coded into role definitions.

## Git Operating Model

For engineering work, normal development happens on task branches and integrates into `dev`.

```text
dev
 └── task / feature / fix branch
          ↓
      implementation
          ↓
      verification
          ↓
        review
          ↓
       PR → dev
          ↓
         dev
          ↓
   prepare promotion
          ↓
   USER APPROVAL
          ↓
        main
```

`main` is human-gated. The OS must never merge to `main` without explicit user approval.

## Repository Layout

```text
Agentic-OS/
├── README.md
├── OS_REQUIREMENTS.md
├── CHANGELOG.md
├── core/
│   ├── PRINCIPLES.md
│   ├── ORCHESTRATION.md
│   ├── ROUTING.md
│   ├── QUALITY_GATES.md
│   ├── CONTEXT_POLICY.md
│   ├── LEARNING_POLICY.md
│   └── ESCALATION_POLICY.md
├── agents/
│   ├── project-manager.md
│   ├── implementer.md
│   ├── reviewer.md
│   └── debugger.md
├── skills/
│   ├── methodology-os/
│   ├── project-planning/
│   ├── handoff/
│   └── retrospective/
├── templates/
│   ├── PROJECT_BRIEF.md
│   ├── PLAN.md
│   ├── STATE.md
│   ├── TASK_PACKET.md
│   ├── WORK_REPORT.md
│   ├── DECISIONS.md
│   └── HANDOFF.md
└── evals/
    └── scenarios/
```

Some files are intentionally placeholders until their design stage is completed.

## Development Model

The Methodology OS is being built incrementally. Each stage should introduce only the complexity required to solve a defined orchestration problem.

Global Claude Code installation and `~/.claude` integration are intentionally deferred until the core agents, routing, and context policies are mature enough for safe dogfooding.
