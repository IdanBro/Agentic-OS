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

### Changed
- Updated `README.md` to reflect completion of Steps 1–3 and make Step 4 — Agent Architecture the next implementation stage.
- Documented the current lifecycle modes, core execution flow, Git operating model, and incremental development strategy in the repository overview.

## Development Milestones

- **Step 1 — Requirements & Philosophy:** complete
- **Step 2 — Constitution / Core Principles:** complete
- **Step 3 — Project Lifecycle / Orchestration:** complete
- **Step 4 — Agent Architecture:** next
