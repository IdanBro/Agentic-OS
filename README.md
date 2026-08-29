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
- Step 4 — Agent Architecture: next

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
