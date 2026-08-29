# Changelog

All notable Methodology OS changes are recorded here as the system is developed incrementally.

## Unreleased

### Added
- Initial Methodology OS repository structure.
- `OS_REQUIREMENTS.md` defining scope, autonomy, quality, token efficiency, Git workflow, verification, documentation, state, and learning requirements.
- `core/PRINCIPLES.md` with the first 15 constitutional invariants.
- `core/ORCHESTRATION.md` defining the canonical project lifecycle and orchestration state machine.
- Lite, Standard, and Full lifecycle modes so process depth scales with complexity and risk.
- Explicit intake, triage, investigation, planning, execution, verification, review, integration, and completion states.
- Failure recovery through diagnosis and replanning instead of blind retries.
- Git lifecycle rules that integrate task branches into `dev` while keeping `main` human-gated.
- Orchestration anti-patterns covering ceremony-first workflows, vague delegation, worker-report trust, context dumping, premature parallelism, approval spam, transcript state, and autonomous promotion to `main`.
- `agents/project-manager.md` defining the main orchestration role, lifecycle ownership, task-packet rules, independent verification, context hygiene, Git authority, and human escalation behavior.
- `agents/implementer.md` defining bounded execution, self-verification, authority limits, context discipline, and an evidence-oriented worker report contract.
- `agents/reviewer.md` defining an independent read-only review role with anti-anchoring behavior, severity levels, verification assessment, and explicit review verdicts.
- `agents/debugger.md` defining a diagnosis-first read-only role based on evidence collection, hypothesis testing, root-cause confidence, fix direction, and validation planning.
- `core/ROUTING.md` defining centralized model and effort selection based on ambiguity, reasoning complexity, scope, risk, horizon, verification difficulty, and retry cost.
- V0 capability semantics for Haiku, Sonnet, Opus, and Fable, while preferring provider-aware family aliases over pinned versions.
- Independent effort routing across `low`, `medium`, `high`, `xhigh`, and `max` with explicit exceptional-use rules for the highest levels.
- Evidence-driven escalation rules that distinguish context, environment, decomposition, depth, capability, and horizon failures before changing model configuration.
- Downshift rules that intentionally move bounded execution to cheaper workers after expensive planning or investigation resolves ambiguity.
- Stable-PM routing guidance that keeps task-level model/effort variation in workers where practical, reducing unnecessary long-session routing churn.
- `core/CONTEXT_POLICY.md` defining context classes, role-specific working sets, reference-first packaging, worker-boundary compression, fresh/resume/fork rules, skill-loading discipline, context-health checks, and handoff triggers.
- A five-class context model covering constitutional, durable project, task, ephemeral execution, and evidence context.
- Explicit reviewer anti-anchoring context rules that keep Implementer conclusions out of the first independent review pass when practical.
- Resume-vs-fresh-agent rules that preserve useful local exploration without carrying stale or biased worker context by habit.
- Fork policy that reserves inherited full-conversation context for cases where re-packaging the required background would be more expensive or lossy.
- Context packaging and return checklists for PM→worker and worker→PM boundaries.
- V0 context-routing matrix and testable context invariants for later evals.
- `templates/PROJECT_BRIEF.md` defining the stable project contract: outcome, success criteria, scope, constraints, quality bar, human gates, and durable starting context.
- `templates/PLAN.md` defining versioned phases/tasks, stable work IDs, dependencies, acceptance criteria, verification intent, integration strategy, replanning rules, and anticipated gates without duplicating live status.
- `templates/STATE.md` defining the canonical hot snapshot for current objective, active work, next actions, blockers, verification evidence, Git/integration state, risks, and context health.
- `templates/DECISIONS.md` defining lightweight durable decision records with stable IDs, rationale, alternatives, consequences, evidence, approval state, and supersession links.
- `templates/HANDOFF.md` defining a compressed PM-to-PM ownership-transfer snapshot with successor start checks, current evidence, blockers, decisions, failed approaches worth preserving, and Git freshness validation.
- Project-state usage rules that scale artifact depth to Lite, Standard, and Full work while avoiding documentation theatre.
- `templates/TASK_PACKET.md` defining bounded worker objectives, acceptance criteria, minimum-sufficient references, required verification, authority envelopes, supporting-change rules, Git boundaries, failure handling, and compact packet form.
- `templates/WORK_REPORT.md` defining evidence-oriented worker returns with acceptance status, meaningful changes, actual verification, PM-verifiable evidence, assumptions, residual uncertainty, and non-PASS continuation requirements.
- Canonical execution-worker statuses: `PASS`, `PARTIAL`, `BLOCKED`, and `FAILED`, with only `PASS` eligible to proceed to independent PM verification.
- Scope-drift handling that permits low-risk directly-required supporting changes while returning material scope/architecture/dependency/security/cost decisions to the PM.
- Explicit compact delegation/report forms for small Standard-mode tasks so bounded delegation does not require full ceremony.

### Changed
- Updated `README.md` to reflect completion of Steps 1–8 and make Step 9 — Verification System the next implementation stage.
- Documented the current lifecycle modes, core execution flow, Git operating model, agent architecture, routing model, context architecture, project-state model, delegation protocol, and incremental development strategy in the repository overview.
- Kept agent model selection on `inherit` so `core/ROUTING.md` remains the canonical source for per-task model and effort decisions.
- Deliberately disabled nested delegation for V0 workers even though current Claude Code supports nested subagents; the PM remains the single orchestration authority until deeper delegation proves useful.
- Established `Sonnet / medium` as the default normal bounded-worker hypothesis and `Opus / high` as the default complex-reasoning hypothesis, both subject to later evals.
- Reserved Fable for hardest long-horizon or highly ambiguous autonomous work rather than treating it as a prestige/default model.
- Defined total expected workflow cost, including retries and rework, as the optimization target rather than the price of an individual model call.
- Established fresh isolated subagents as the default worker boundary and references to accessible repository content as the default transfer mechanism.
- Defined global/project `CLAUDE.md` and preloaded skills as recurring context costs that must remain concise and task-relevant.
- Explicitly rejected auto memory, conversation history, and automatic compaction as substitutes for canonical project state.
- Chose qualitative context-health and handoff triggers for V0 instead of hard-coded token percentages that may become model/provider-specific.
- Established `STATE.md` as the sole hot operational snapshot; `PLAN.md` intentionally does not maintain a second live progress tracker.
- Defined `PROJECT_BRIEF.md` as stable contract state, `DECISIONS.md` as durable rationale, and `HANDOFF.md` as transfer-only compression rather than parallel sources of current truth.
- Deferred `TASK_PACKET.md` and `WORK_REPORT.md` from Step 7 to Step 8 so delegation contracts remain separate from project-state artifacts; both are now implemented.
- Updated the Implementer contract to use the canonical Task Packet / Work Report schemas and the four-state execution vocabulary.
- Clarified that worker `PASS` is an evidence-bearing claim, not PM verification, review approval, integration approval, or project completion.

## Development Milestones

- **Step 1 — Requirements & Philosophy:** complete
- **Step 2 — Constitution / Core Principles:** complete
- **Step 3 — Project Lifecycle / Orchestration:** complete
- **Step 4 — Agent Architecture:** complete
- **Step 5 — Model & Effort Routing:** complete
- **Step 6 — Context Architecture:** complete
- **Step 7 — Project State:** complete
- **Step 8 — Delegation Protocol:** complete
- **Step 9 — Verification System:** next
