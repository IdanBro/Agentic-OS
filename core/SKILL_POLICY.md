# Methodology OS — Skill Architecture & Loading Policy

This document defines how Methodology OS discovers, selects, loads, composes, and evolves reusable skills.

Its purpose is to make specialized capability available **only when it materially helps the current task**, without turning the global Claude environment into a permanent prompt dump.

The Project Manager owns skill selection for orchestrated work.

---

## 1. Core Rule

> Skills are optional capability modules. Load the smallest relevant set, at the latest useful moment, and do not preload knowledge merely because it might become useful.

A skill should exist because it provides reusable procedural or domain value that would otherwise be repeatedly rediscovered or pasted into prompts.

A skill is not:

- project state,
- a replacement for an agent role,
- a copy of global OS policy,
- a place to store one-off task details,
- an excuse to preload every technology used by a repository.

---

## 2. Why Skills Exist

Use a skill when one or more are true:

- a repeatable multi-step procedure should be followed consistently;
- domain knowledge materially improves execution quality;
- project/team conventions are non-obvious and repeatedly needed;
- deterministic scripts or references should travel with an instruction set;
- a recurring task benefits from a compact reusable workflow;
- moving procedural detail out of `CLAUDE.md` reduces recurring context cost.

Do not create a skill when:

- the information belongs in normal project documentation;
- the instruction is a one-time Task Packet detail;
- a short repository convention belongs in project `CLAUDE.md`;
- the behavior is already covered adequately by an existing skill;
- the skill would only wrap one obvious command with no reusable judgment or workflow.

---

## 3. Skill Sources and Intended Scope

Methodology OS recognizes four practical skill scopes.

### 3.1 Personal / Global Skills

Location in Claude Code:

`~/.claude/skills/<skill-name>/SKILL.md`

Use for capabilities that should be available across projects, such as Methodology OS itself or genuinely reusable personal workflows.

Global skills should remain curated because their descriptions are part of the discoverable skill set in normal sessions.

### 3.2 Project Skills

Location:

`.claude/skills/<skill-name>/SKILL.md`

Use for project-specific procedures, conventions, build/run recipes, deployment knowledge, domain constraints, or other shared repository behavior.

Prefer project skills over global duplication when the knowledge is specific to one repository.

### 3.3 Nested Project Skills

Location below a package/component:

`<subdir>/.claude/skills/<skill-name>/SKILL.md`

Use in monorepos when a capability or convention applies only to one package or subtree.

This is preferable to forcing every worker in the repository to carry package-specific instructions.

### 3.4 Plugin Skills

Plugins may package skills with agents, hooks, MCP servers, and other extensions.

V0 does not require Methodology OS to be a plugin. Plugin packaging is a future distribution option if it provides a concrete portability or installation advantage.

---

## 4. Naming Policy

Global Methodology OS skills MUST use distinctive names so they do not accidentally shadow generic project skills.

V0 core names:

- `methodology-start`
- `methodology-os`
- `methodology-planning`
- `methodology-handoff`
- `methodology-retrospective`

Avoid global names such as:

- `deploy`
- `review`
- `handoff`
- `terraform`
- `kubernetes`

unless the user intentionally wants the global skill to own that generic command name.

When a name collision exists, the PM must not assume the project-local implementation is the one that will run. Prefer unique names and inspect skill provenance when ambiguity matters.

---

## 5. Skill Content Types

A skill should primarily be one of these types.

### 5.1 Reference Skill

Provides reusable knowledge or conventions used inline with current work.

Examples:

- API conventions,
- repository architecture rules,
- Kubernetes platform conventions,
- organization-specific security patterns.

Reference skills normally remain in the current conversation after invocation because their guidance should continue to apply to the task.

### 5.2 Task / Procedure Skill

Provides an explicit workflow for an action.

Examples:

- project planning,
- preparing a handoff,
- running a release checklist,
- migration procedure,
- incident triage.

Task skills should describe observable outcomes and checks rather than narrating background theory.

### 5.3 Isolated / Forked Skill

Uses a separate subagent context for a self-contained task that would otherwise add substantial disposable context.

Good candidates:

- high-volume repository research,
- PR analysis,
- log-heavy investigation,
- bounded research with a compact return.

Do not use fork mode for passive reference guidance that needs to influence the current PM or worker throughout the task.

---

## 6. Progressive Disclosure

The main `SKILL.md` should contain only:

- purpose,
- trigger conditions,
- essential procedure or guidance,
- navigation to supporting resources,
- important boundaries.

Move detailed material into supporting files when it is not required on every invocation.

Recommended shape:

```text
skill-name/
├── SKILL.md
├── reference.md        # optional detailed knowledge
├── examples.md         # optional worked examples
└── scripts/            # optional deterministic helpers
```

Supporting files are read or executed only when needed.

Do not duplicate large external documentation inside a skill when a stable reference or targeted source lookup is sufficient.

---

## 7. Skill Descriptions Are Routing Metadata

The description is not marketing copy. It is routing metadata used to decide whether a skill should be loaded.

A good description states:

1. what capability the skill provides;
2. when it should be used;
3. important non-trigger conditions when confusion is likely.

Prefer:

> Plan or replan Standard/Full Methodology OS work using project brief, state, dependencies, acceptance criteria, risk, and verification strategy. Use when work needs a structured execution plan; do not use for trivial one-step tasks.

Avoid:

> Helps with planning.

Descriptions should be specific enough that similarly named skills can be distinguished without loading their full bodies.

---

## 8. Default Loading Strategy

### 8.1 Main Session

Default: **discover descriptions, invoke body on demand**.

Do not invoke a skill merely because its domain keyword appears in the project.

Invoke when the skill is expected to materially improve:

- correctness,
- consistency,
- context efficiency,
- verification quality,
- procedural reliability.

Once a skill body is loaded, treat it as continuing context cost for the current session. Do not repeatedly load overlapping skills that say the same thing.

### 8.2 Workers / Subagents

V0 default: **do not statically preload skills into generic worker definitions**.

The Implementer, Reviewer, and Debugger remain reusable roles. They should discover/invoke relevant project, personal, or plugin skills only when the task needs them.

Static preloading via an agent `skills:` field is justified only when:

1. nearly every invocation of that agent genuinely needs the skill;
2. the skill is short and stable;
3. startup context cost is lower than repeated discovery/invocation cost;
4. preloading does not reduce role generality in a harmful way.

If these conditions are not met, leave the skill out of `skills:`.

---

## 9. Skill Selection Algorithm

Before execution, the PM should ask:

### Step 1 — Does the task need a skill at all?

If normal repository inspection and role competence are sufficient, use no skill.

### Step 2 — Is there project-local knowledge?

Look for project or nested skills that encode repository-specific procedures or conventions.

Local knowledge is usually more relevant than generic domain guidance, but naming/provenance must be checked where collisions are possible.

### Step 3 — Is domain expertise materially useful?

Select the narrowest domain skill that matches the actual task.

Example:

```text
Task: modify readiness probes in one Helm chart

Good:
- Helm chart conventions skill
- Kubernetes probe skill, only if the repository/platform behavior requires it

Bad:
- Kubernetes
- Helm
- Terraform
- AWS
- Security
- DevOps best practices
all loaded "just in case"
```

### Step 4 — Is a methodology procedure needed?

Invoke Methodology OS subskills only when their procedure is active:

- planning → `methodology-planning`
- session transfer → `methodology-handoff`
- milestone learning capture → `methodology-retrospective`

### Step 5 — Remove overlap

If two skills contain substantially overlapping instructions, choose the more specific/relevant one unless both provide distinct value.

### Step 6 — Record only material skill decisions

Do not turn skill selection into documentation ceremony.

Record a skill choice in a Task Packet or state only when it affects execution, reproducibility, or future continuation.

---

## 10. Task Packet Skill Guidance

A Task Packet MAY include an optional section:

```text
SKILLS
- Required/on-demand: <skill-name> — <why>
- Optional discovery: <skill-name or none>
```

This means the worker should invoke the named skill when its guidance is required.

It does not mean the full skill body must be copied into the packet.

For Reviewer first-pass independence, do not preload or force implementation-oriented skills whose assumptions could anchor the review unless the skill contains required project conventions.

For Debugger work, prefer diagnostic/domain skills that help interpret evidence; do not preload a skill that asserts the suspected root cause.

---

## 11. Preloading Policy

Preloading is a context optimization only when the skill is truly universal for that agent.

Do not preload a skill because:

- it is frequently useful across some tasks;
- it might save one invocation;
- the repository happens to use that technology;
- it makes the agent look more specialized.

The cost of preloading is paid on every subagent launch.

V0 core agents intentionally have no Methodology OS domain skill preloads.

Future evals may justify a dedicated specialized agent with preloaded skills, for example a platform-specific reviewer. That should be added because measured task quality or cost improves, not by intuition alone.

---

## 12. Invocation Control

Choose skill invocation behavior based on consequence.

### Model-Invocable by Default

Appropriate for:

- reference knowledge,
- planning,
- analysis,
- handoff preparation,
- non-destructive internal procedures.

### User-Only Invocation

Use manual-only invocation for workflows where autonomous triggering would itself be consequential, such as:

- production deployment,
- sending external messages,
- destructive migration,
- billing-sensitive action,
- irreversible release action.

Do not encode permission to perform a high-impact action merely by making a skill available.

Methodology OS human gates still apply.

### Model-Only Invocation

Use for internal background knowledge that does not make sense as a user command.

V0 Methodology OS core skills remain user-invocable so they can also be tested explicitly.

---

## 13. Tool Permissions in Skills

`allowed-tools` is a convenience grant, not an authority escalation mechanism.

Rules:

- grant only tools/command patterns the procedure repeatedly and safely needs;
- prefer narrow command patterns over broad shell access;
- do not use `allowed-tools` to bypass a Methodology OS human gate;
- keep destructive or external-side-effect operations behind the appropriate permission/approval path;
- remember that tool grants are temporary while skill instructions may remain in context.

`disallowed-tools` may be used to enforce a narrow autonomous workflow when there is a concrete safety or scope reason.

---

## 14. Model and Effort in Skills

Model and effort routing belongs primarily in `core/ROUTING.md` and the PM.

Default Methodology OS skills should not pin a model or effort level.

A skill-specific model override is justified only when the skill itself creates an isolated execution environment whose capability requirements are stable and meaningfully different from the caller's route.

Avoid hidden routing inside skills that makes cost or capability hard for the PM to reason about.

---

## 15. Dynamic Context Injection

Dynamic shell/context injection may be useful when a skill requires a small current snapshot before execution.

Use it when:

- the data must be current at invocation time;
- the command is safe and deterministic;
- output is predictably bounded;
- inlining the result materially improves the workflow.

Avoid it when:

- output can be large or noisy;
- the worker can inspect the source directly;
- the command has side effects;
- a failed command would unnecessarily abort the entire skill;
- the output will become stale quickly while remaining in context.

For high-volume evidence, prefer targeted tool use or a forked worker that returns a compact summary.

---

## 16. `context: fork` Policy

Use an isolated skill when all are true:

- the task is self-contained;
- the skill body contains an actionable task, not just guidance;
- substantial disposable context is expected;
- a compact result can be returned to the caller;
- losing parent conversation history does not remove essential state.

Do not use `context: fork` for the four V0 Methodology OS core skills. Planning, handoff, and retrospective operate on current PM/project state and should remain visible to the orchestrator.

A future research/debug skill may legitimately use forked execution.

---

## 17. Skill Size and Quality Standard

A high-quality skill should:

- have a specific trigger description;
- be concise enough to justify its context cost;
- describe outcomes and boundaries clearly;
- avoid hidden assumptions about project state;
- point to supporting files rather than embedding everything;
- avoid duplicating global policies;
- preserve existing authority and quality gates;
- work from references instead of copied project history where possible;
- make its expected output clear.

Keep `SKILL.md` comfortably below the Claude Code recommended maximum; move detailed references to supporting files.

---

## 18. Skill vs Agent Decision

Use a **skill** when the reusable value is primarily:

- knowledge,
- procedure,
- conventions,
- a deterministic helper workflow.

Use an **agent** when the reusable value is primarily:

- a distinct role,
- independent context,
- independent judgment,
- different tool/permission boundaries,
- a specialized system prompt.

Use both when a role repeatedly needs a specific knowledge/procedure layer and preloading or deliberate invocation is justified.

Do not create an agent merely to store a long prompt that belongs in a skill.

Do not create a skill merely to rename an existing agent role.

---

## 19. Skill vs `CLAUDE.md` Decision

Put information in `CLAUDE.md` only when Claude should know it broadly and repeatedly throughout the applicable scope.

Put information in a skill when:

- it is procedural;
- it is specialized;
- it is only relevant to some tasks;
- loading it on demand saves recurring context.

The global `~/.claude/CLAUDE.md` Methodology OS kernel should remain small and route complex work toward the `methodology-os` skill rather than embedding the whole OS.

---

## 20. V0 Core Skill Set

### `methodology-start`

User-facing launcher for starting a full Methodology OS project workflow from the current repository. It bootstraps local context, establishes the objective, then routes execution through the PM operating model without requiring the user to choose agents, workflow depth, routing, or verification strategy manually.

### `methodology-os`

Global entrypoint for activating the Methodology OS operating pattern on complex/multi-stage work.

### `methodology-planning`

Creates or revises proportional project plans from the project brief, current state, decisions, dependencies, risk, acceptance, and verification needs.

### `methodology-handoff`

Reconciles canonical state and produces a compressed PM-to-PM continuation artifact when context/session ownership should transfer.

### `methodology-retrospective`

Examines a meaningful completed phase/project for workflow lessons and candidate improvements without automatically changing global OS policy.

These are methodology capabilities, not technology/domain skills.

---

## 21. Domain Skills

Domain skills should remain separate from the global methodology core.

Possible examples:

- Kubernetes platform conventions,
- Helm authoring conventions,
- Terraform module standards,
- AWS organization patterns,
- Python testing conventions,
- organization security requirements.

Methodology OS should route them when useful but should not absorb their full knowledge into global policy.

Project-specific domain skills should be preferred over generic global skills when local behavior is materially different.

---

## 22. Skill Lifecycle

A reusable skill should evolve through evidence, not enthusiasm.

Suggested lifecycle:

```text
recurring need observed
      ↓
small skill candidate
      ↓
project/personal trial
      ↓
evaluate triggering + quality + context cost
      ↓
refine or remove
      ↓
promote broadly only when justified
```

Global Methodology OS skill changes are OS changes and remain subject to the human-promotion rule.

The detailed learning/promotion process is defined in Step 12 by `core/LEARNING_POLICY.md`.

---

## 23. Anti-Patterns

### Skill Hoarding

Installing dozens of global skills "just in case" creates discovery noise and recurring description cost.

### Preload Everything

Putting every domain skill in every worker's `skills:` list defeats context isolation.

### Giant Skill

One skill containing all Kubernetes, Terraform, Git, AWS, CI/CD, security, and Methodology OS knowledge becomes a hidden monolith.

### Duplicate Policy

Copying `QUALITY_GATES.md` or `ROUTING.md` into multiple skill bodies guarantees future drift.

### Keyword Triggering

A task mentioning "Kubernetes" does not automatically require every Kubernetes-related skill.

### Permission by Skill

A deployment skill existing does not authorize deployment.

### Skill-as-State

Do not put project progress, current blockers, or active approvals into a reusable skill.

### Skill-as-Transcript

Do not preserve session history inside a skill because it may be useful later.

### Forked Reference Guide

Do not use `context: fork` for passive guidance with no self-contained task.

---

## 24. V0 Testable Invariants

A compliant Methodology OS run should satisfy:

1. Generic core workers have no unnecessary static skill preloads.
2. Skills are selected because they materially support the current task, not because their technology appears somewhere in the repo.
3. Project/nested skills are considered for project-specific behavior before generic guidance is copied into prompts.
4. Task Packets reference relevant skills instead of copying full skill bodies.
5. Reviewer independence is not undermined by unnecessary implementation-oriented skill loading.
6. Global core skill names avoid generic collisions.
7. Model/effort routing remains visible to the PM rather than being silently duplicated across skills.
8. High-impact side-effect skills cannot bypass human gates.
9. Skills use progressive disclosure instead of giant `SKILL.md` bodies.
10. Global skill changes remain human-promoted OS changes.

These invariants should become part of the Step 13 eval suite.
