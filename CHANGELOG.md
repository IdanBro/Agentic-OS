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

### Changed
- Updated `README.md` to reflect completion of Steps 1–5 and make Step 6 — Context Architecture the next implementation stage.
- Documented the current lifecycle modes, core execution flow, Git operating model, agent architecture, routing model, and incremental development strategy in the repository overview.
- Kept agent model selection on `inherit` so `core/ROUTING.md` remains the canonical source for per-task model and effort decisions.
- Deliberately disabled nested delegation for V0 workers even though current Claude Code supports nested subagents; the PM remains the single orchestration authority until deeper delegation proves useful.
- Established `Sonnet / medium` as the default normal bounded-worker hypothesis and `Opus / high` as the default complex-reasoning hypothesis, both subject to later evals.
- Reserved Fable for hardest long-horizon or highly ambiguous autonomous work rather than treating it as a prestige/default model.
- Defined total expected workflow cost, including retries and rework, as the optimization target rather than the price of an individual model call.

## Development Milestones

- **Step 1 — Requirements & Philosophy:** complete
- **Step 2 — Constitution / Core Principles:** complete
- **Step 3 — Project Lifecycle / Orchestration:** complete
- **Step 4 — Agent Architecture:** complete
- **Step 5 — Model & Effort Routing:** complete
- **Step 6 — Context Architecture:** next
