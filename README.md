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
- Step 5 — Model & Effort Routing: complete
- Step 6 — Context Architecture: complete
- Step 7 — Project State: complete
- Step 8 — Delegation Protocol: complete
- Step 9 — Verification System: complete
- Step 10 — Skills Architecture: next

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

## Model & Effort Routing

Model routing is centralized in `core/ROUTING.md` instead of being duplicated across agent definitions.

V0 uses the following capability semantics:

```text
Haiku  → very simple, short, low-risk work
Sonnet → default bounded execution / daily coding
Opus   → complex reasoning, difficult debugging, high-risk review
Fable  → hardest long-horizon and highly ambiguous autonomous work
```

Effort is routed separately from model capability:

```text
low    → obvious, tightly scoped
medium → bounded cost-conscious execution
high   → intelligence-sensitive work
xhigh  → extended agentic/coding depth
max    → exceptional, explicitly justified
```

Default worker baseline:

```text
Implementer → Sonnet / medium
```

Default complex reasoning baseline:

```text
Opus / high
```

The PM diagnoses failures before escalating. Missing context, bad decomposition, or environment failures should be fixed directly rather than buying a stronger model. Insufficient depth generally raises effort; genuine capability gaps raise the model family.

The routing objective is:

> Use the least expensive configuration reasonably expected to meet the quality bar on the first well-prepared attempt, optimizing total workflow cost rather than per-call price.

## Context Architecture

Context routing is centralized in `core/CONTEXT_POLICY.md`.

The canonical rule is:

> Context is a working set, not an archive.

The OS separates:

```text
constitutional context
→ small, broadly applicable rules

durable project context
→ objective, state, decisions, risks

task context
→ bounded worker input

ephemeral execution context
→ logs, searches, experiments kept local

evidence context
→ compact proof returned across boundaries
```

Fresh isolated subagents are the normal worker boundary. The PM keeps orchestration state and receives compact conclusions/evidence rather than raw execution transcripts. Accessible files and repository objects are referenced instead of copied by default.

Reviewer first-pass context deliberately avoids Implementer conclusions when independent inspection is possible. Forked subagents are reserved for cases where inheriting a large amount of PM context has clear net value; they are not the default.

Skills and `CLAUDE.md` are treated as recurring context costs. The global Claude kernel should remain small, preloaded skills require task relevance, and auto memory or automatic compaction never replace canonical project state.

Context health is evaluated qualitatively rather than through fixed token-percentage thresholds. When current conversation history becomes noisy or state becomes difficult to reconstruct, the PM externalizes durable truth and prepares a structured handoff before starting a fresh PM context.

## Project State

Project continuity is externalized through five canonical artifact types:

```text
PROJECT_BRIEF.md
→ stable outcome, scope, constraints, success criteria

PLAN.md
→ intended path, phases, task IDs, dependencies, acceptance

STATE.md
→ current operational truth and next actions

DECISIONS.md
→ material non-obvious decisions and rationale

HANDOFF.md
→ compressed ownership-transfer snapshot
```

These artifacts deliberately do not duplicate one another. `STATE.md` is the hot snapshot; `PLAN.md` describes intended structure rather than maintaining a second live task tracker; `DECISIONS.md` stores only durable rationale; and `HANDOFF.md` references canonical artifacts rather than copying them.

State depth scales with workflow depth. Lite work normally avoids the full artifact set. Standard work creates only the state artifacts that materially improve recoverability. Full work uses the complete set when the project's duration, ambiguity, or risk justifies it.

A fresh PM should normally begin with `PROJECT_BRIEF.md` and `STATE.md`, then read only the relevant plan and decision sections. Handoffs require the successor to verify current Git/artifact state before trusting the snapshot.

## Delegation Protocol

Delegation uses two canonical boundary artifacts:

```text
PM
 │
 │ TASK_PACKET.md
 ▼
Worker
 │
 │ WORK_REPORT.md
 ▼
PM
 │
 ▼
Independent PM verification
```

`TASK_PACKET.md` defines one bounded outcome, observable acceptance criteria, required verification, minimum-sufficient references, and an explicit authority envelope. It is detailed enough to prevent hidden-intent guessing without becoming a copy of the project plan or repository.

Workers may inspect adjacent context autonomously. A small supporting change outside initially named paths is allowed only when it is directly required, low-risk, consistent with existing design, and reported. Material scope, architecture, dependency, security, compatibility, cost, or destructive-operation changes return to the PM instead of expanding silently.

Execution workers use four statuses:

```text
PASS
→ acceptance believed satisfied; eligible for PM verification

PARTIAL
→ useful progress, acceptance incomplete

BLOCKED
→ decision/dependency/permission required

FAILED
→ current approach did not achieve the objective;
  further attempts need diagnosis or replan
```

Only `PASS` can proceed toward acceptance, and worker `PASS` is never equivalent to PM verification or integration approval.

`WORK_REPORT.md` compresses the worker context at the return boundary. It reports acceptance status, meaningful changes, checks actually performed, evidence the PM can independently inspect, scope notes, and remaining uncertainty — not full logs, full diffs, or hidden reasoning.

For small Standard-mode work, both packet and report may use compact forms. High-risk or incomplete work keeps the richer structure.

## Verification System

Verification and integration gates are centralized in `core/QUALITY_GATES.md`.

The core rule is:

> A claim becomes project truth only when it has evidence appropriate to its risk and has passed every required gate.

The normal delegated-task chain is:

```text
worker self-verification
        ↓
PM independent verification
        ↓
independent Reviewer when required
        ↓
integration readiness
        ↓
merge to dev
        ↓
post-integration/system verification when required
```

V0 uses this gate matrix:

| Risk | Worker/Self Verify | PM Verify | Independent Reviewer | Post-Integration |
| --- | --- | --- | --- | --- |
| Low | Required | Required for delegated work | Normally no | Only when integration can matter |
| Medium | Required | Required | Required | Targeted/integrated when relevant |
| High | Required | Required, deep | Required, deep | Strong system/integration evidence when feasible |

Medium-risk review is deliberately mandatory in V0. If review is genuinely unnecessary, the PM must determine that the task is actually low-risk rather than silently waiving the medium-risk gate.

Verification claims use `PASS / FAIL / INCONCLUSIVE / NOT_RUN / N/A`. Worker execution statuses and Reviewer verdicts remain separate vocabularies.

Evidence is state-specific: material changes after a test or review invalidate affected evidence. Reviewer `FAIL` or `INCONCLUSIVE` blocks integration, and a review of a superseded diff does not approve the final diff.

A green CI run is evidence, not a substitute for acceptance verification. Likewise, human approval is separate from technical verification and never turns an unverified claim into `PASS`.

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

Global Claude Code installation and `~/.claude` integration are intentionally deferred until the skills and escalation/autonomy policies are mature enough for safe global dogfooding.
