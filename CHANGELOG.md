# Changelog


## 0.2.0 — PM delegation enforcement

- Standard/Full substantive implementation is now worker-owned by policy.
- The Project Manager may no longer use model capability/speed as a reason to implement a full feature or project itself.
- Direct PM edits in Standard/Full are limited to narrow supporting glue, integration, verification, conflict resolution, and localized follow-up fixes.
- Full-mode work must delegate substantive workstreams and should parallelize independent ready tasks when coordination cost is justified.
- Added blocking eval E-015 to catch monolithic PM implementation of a full application.
- SessionStart routing now reinforces PM/worker separation.

## Plugin-native distribution

Replaced the local symlink/runtime installation model with a native Claude Code plugin:

- repository root is now the `agentic-os` plugin;
- added plugin and marketplace manifests under `.claude-plugin/`;
- existing `agents/` and `skills/` are auto-discovered as native plugin components;
- added a SessionStart routing hook for automatic methodology activation on appropriate project work;
- canonical policy/template references use `${CLAUDE_PLUGIN_ROOT}`;
- removed `install.sh`, global `CLAUDE.md` kernel, runtime adapters, and runtime GitHub fetching;
- behavioral evals load the repository directly with `--plugin-dir`;
- `main` is intended to serve as the stable marketplace/release surface after explicit promotion approval.


Notable Methodology OS changes are recorded here by development milestone. Detailed behavior belongs in the canonical policy, agent, skill, template, eval, and runtime files rather than in duplicated changelog prose.

## Unreleased

### Step 14 — Claude Code Integration

Added the first installable global Claude Code runtime:

- `runtime/CLAUDE.md` — small global kernel that points to the canonical repository without loading every policy into every session.
- Namespaced global agent adapters:
  - `methodology-project-manager`
  - `methodology-implementer`
  - `methodology-reviewer`
  - `methodology-debugger`
- Runtime adapters preserve worker tool/permission boundaries while reading the canonical role contracts from `agents/*.md`.
- `install.sh` with install, `--check`, `--uninstall`, `--force`, conflict backup, managed `CLAUDE.md` import block, agent/skill symlinks, and an optional `CLAUDE_HOME` override for isolated tests.
- `scripts/run_evals.py` — executable structured Claude Code eval harness with static checks, fresh scenario sessions, exact hard-assertion grading, optional semantic judging, model/effort selection, turn limits, budget caps, and JSON reports.
- `.github/workflows/methodology-static.yml` — zero-Claude-token CI for Bash/Python syntax, static contracts, and isolated install/check/uninstall lifecycle.
- `runtime/README.md` with installation, runtime, eval, and uninstall instructions.
- Updated `evals/README.md` from a future runner contract to the executable Step 14 workflow.
- Marked `install.sh` and `scripts/run_evals.py` executable in Git.
- Simplified the root README into a concise entrypoint and policy/runtime map instead of duplicating detailed policy content.

Runtime design decisions:

- the Git checkout remains the source of truth;
- `~/.claude/methodology-os` is a stable symlink anchor;
- global agent/skill names are namespaced to reduce collisions with project-local assets;
- existing user `~/.claude/CLAUDE.md` content is preserved and only a marked import block is managed;
- the behavioral eval runner does not receive scenario expected answers and operates read-only in decision-simulation mode;
- real local Claude Code smoke/eval execution is required before the Step 15 real-project trial.

### Step 13 — Evals

Added the V0 behavioral regression framework:

- machine-readable scenario, result, and suite JSON Schemas;
- 14 initial scenarios covering authority, verification, routing, skills, learning, and failure recovery;
- `core-v0`, `routing-v0`, `learning-v0`, and `full-v0` suites;
- deterministic hard assertions with optional semantic `must` / `must_not` evaluation;
- blocking critical scenarios for `main` authority, approval leakage, verification truth, and global self-modification;
- cost discipline through small core and targeted suites rather than mandatory full-suite execution.

### Step 12 — Learning System

Implemented governed Methodology OS learning:

- `core/LEARNING_POLICY.md` separates project-specific learning, candidate global learning, and promoted global behavior;
- lifecycle: `OBSERVATION → CANDIDATE → NEEDS_EVIDENCE/VALIDATING → READY_FOR_PROMOTION → HUMAN GATE → IMPLEMENT/EVAL/VERIFY → PROMOTED`;
- L1/L2/L3 change-impact classes scale evidence and review requirements;
- causal/generalization tests prevent one-incident and technology-label overfitting;
- global promotion is explicitly human-gated;
- private project evidence is sanitized/reference-first;
- `templates/LEARNING_CANDIDATE.md` supports durable candidates only when warranted;
- `methodology-retrospective` and the PM were connected to the governed learning flow.

### Step 11 — Escalation & Autonomy

Implemented `core/ESCALATION_POLICY.md`:

- `A0 — AUTONOMOUS`
- `A1 — AUTONOMOUS + RECORD`
- `A2 — HUMAN GATE`
- `A3 — BLOCKED`

Added bounded approval envelopes, non-transitive/freshness semantics, consequence-based escalation, Git authority rules, exact-action approval without duplicate confirmation, and durable approval state support.

### Step 10 — Skills Architecture

Implemented `core/SKILL_POLICY.md` and the first global methodology skills:

- `methodology-os`
- `methodology-planning`
- `methodology-handoff`
- `methodology-retrospective`

Established on-demand loading, zero-skill default, project-skill preference for local conventions, no generic worker preload, namespaced global skill names, and the rule that skills never expand authority.

### Step 9 — Verification System

Implemented `core/QUALITY_GATES.md`:

- worker self-verification;
- mandatory independent PM verification for delegated work;
- mandatory independent Reviewer for medium/high risk;
- integration and post-integration gates;
- canonical verification states `PASS / FAIL / INCONCLUSIVE / NOT_RUN / N/A`;
- evidence freshness and re-verification after material changes;
- explicit separation between technical verification and human risk acceptance.

### Step 8 — Delegation Protocol

Implemented:

- `templates/TASK_PACKET.md` for bounded PM→worker contracts;
- `templates/WORK_REPORT.md` for compact evidence-oriented worker returns;
- execution statuses `PASS / PARTIAL / BLOCKED / FAILED`;
- scope-drift and supporting-change rules;
- PM handling for worker return states and specialized Reviewer/Debugger vocabularies.

### Step 7 — Project State

Implemented canonical durable project artifacts:

- `PROJECT_BRIEF.md`
- `PLAN.md`
- `STATE.md`
- `DECISIONS.md`
- `HANDOFF.md`

Established `STATE.md` as the sole hot operational snapshot and kept stable contract, intended plan, durable rationale, and handoff compression as distinct responsibilities.

### Step 6 — Context Architecture

Implemented `core/CONTEXT_POLICY.md`:

- constitutional, durable-project, task, ephemeral, and evidence context classes;
- reference-first packaging;
- worker-boundary compression;
- role-specific context rules;
- fresh/resume/fork guidance;
- selective skill loading;
- qualitative context-health and handoff triggers.

Core principle: **context is a working set, not an archive**.

### Step 5 — Model & Effort Routing

Implemented `core/ROUTING.md`:

- centralized Haiku/Sonnet/Opus/Fable capability semantics;
- independent effort routing;
- routing based on ambiguity, complexity, scope, risk, horizon, verification difficulty, and retry cost;
- context/environment/decomposition diagnosis before model escalation;
- effort-first escalation for insufficient depth;
- model escalation only for genuine capability gaps;
- downshifting after expensive reasoning removes ambiguity.

### Step 4 — Agent Architecture

Implemented four V0 role contracts:

- Project Manager — orchestration/state/Git/verification/human gates;
- Implementer — bounded change + self-verification;
- Reviewer — independent read-only review;
- Debugger — diagnosis-first read-only investigation.

V0 intentionally keeps worker nesting disabled even though Claude Code supports deeper agent hierarchies.

### Step 3 — Project Lifecycle / Orchestration

Implemented `core/ORCHESTRATION.md` with:

- Lite / Standard / Full modes;
- lifecycle state machine;
- bounded task loop;
- diagnosis and replan instead of blind retries;
- proportional planning and parallelism;
- Git lifecycle through working branches and `dev`;
- human-gated `main` promotion;
- structured handoffs and state updates.

### Step 2 — Constitution / Core Principles

Implemented `core/PRINCIPLES.md` with 15 durable invariants covering professional quality, evidence, independent verification, context efficiency, bounded delegation, routing, human authority, Git safety, durable state, diagnosis, documentation cost, learning governance, and complexity discipline.

### Step 1 — Requirements & Philosophy

Implemented `OS_REQUIREMENTS.md` defining:

- high autonomy for routine work;
- professional quality and token/context efficiency as primary goals;
- meaningful human escalation boundaries;
- independent verification;
- medium/high-risk review;
- off-main Git workflow with autonomous verified `dev` integration;
- human-gated `main`;
- balanced documentation;
- durable state/handoffs;
- human-promoted global learning.

## Development Milestones

- ✅ 1. Requirements & Philosophy
- ✅ 2. Constitution / Core Principles
- ✅ 3. Project Lifecycle / Orchestration
- ✅ 4. Agent Architecture
- ✅ 5. Model & Effort Routing
- ✅ 6. Context Architecture
- ✅ 7. Project State
- ✅ 8. Delegation Protocol
- ✅ 9. Verification System
- ✅ 10. Skills Architecture
- ✅ 11. Escalation & Autonomy
- ✅ 12. Learning System
- ✅ 13. Evals
- ✅ 14. Claude Code Integration — repository/runtime implementation
- ➡️ 15. Real Project Trial
