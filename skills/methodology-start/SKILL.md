---
name: methodology-start
description: Starts a full Agentic OS / Methodology OS project workflow in the current repository. Use when the user wants Claude to take ownership of a project task end-to-end with proportional planning, specialized subagents, verification, review, Git workflow, durable state, and human gates. The Agentic OS plugin must already be installed; do not fetch the control plane from GitHub at runtime.
---

# Methodology Start

This is the user-facing launcher for Agentic OS in the current project.

The Agentic OS plugin is the control plane. Its agents, skills, policies, templates, and supporting files are available under `${CLAUDE_PLUGIN_ROOT}`.

Do not fetch Methodology OS source from GitHub during normal execution. Do not depend on `~/.claude`. The installed plugin package is the runtime source for the current session.

## 1. Load the Project Manager Contract

Before substantial project work, read:

`${CLAUDE_PLUGIN_ROOT}/agents/project-manager.md`

Treat that file as the canonical Project Manager role contract for this run.

Load only the additional policies needed for the current decision from:

- `${CLAUDE_PLUGIN_ROOT}/core/PRINCIPLES.md`
- `${CLAUDE_PLUGIN_ROOT}/core/ORCHESTRATION.md`
- `${CLAUDE_PLUGIN_ROOT}/core/ROUTING.md`
- `${CLAUDE_PLUGIN_ROOT}/core/CONTEXT_POLICY.md`
- `${CLAUDE_PLUGIN_ROOT}/core/QUALITY_GATES.md`
- `${CLAUDE_PLUGIN_ROOT}/core/SKILL_POLICY.md`
- `${CLAUDE_PLUGIN_ROOT}/core/ESCALATION_POLICY.md`
- `${CLAUDE_PLUGIN_ROOT}/core/LEARNING_POLICY.md`

Do not load the whole plugin into context merely to be thorough.

## 2. Bootstrap the Current Project

Inspect the current working directory enough to establish:

- repository root and Git state;
- current/default/integration branches when discoverable;
- README / assignment / task documentation;
- project-local `CLAUDE.md`, rules, and skills;
- language/toolchain and obvious build/test/lint commands;
- existing planning/state artifacts;
- uncommitted user work that must be preserved.

Keep the scan bounded. Do not recursively read the whole repository by default.

## 3. Establish the Objective

Treat text supplied with this skill invocation as the user's objective.

If an explicit objective already exists in the current conversation, use it and do not ask again.

If no objective exists:

1. finish the bounded project bootstrap;
2. summarize the project briefly if useful;
3. ask exactly one concise question: what outcome should be delivered?

Do not invent a major implementation objective from TODOs, open files, issue names, or README aspirations.

## 4. Run Methodology OS Natively

Once the objective is known, apply the `methodology-os` skill and follow the Project Manager contract.

The user should not need to manually choose:

- Lite / Standard / Full;
- worker agents;
- model/effort routes;
- skills;
- state artifacts;
- Reviewer usage;
- verification depth.

Those are PM responsibilities.

Use the plugin-provided specialized subagents as the normal execution path for Standard/Full substantive work:

- `implementer`
- `reviewer`
- `debugger`

Do not manually reconstruct or inject their role prompts from files unless plugin agent discovery is actually broken. Their definitions are native plugin components.

**Delegation invariant:**

- Lite work may stay in the main session when truly small and cheap to verify.
- Standard work that includes substantive implementation MUST delegate at least one bounded implementation task.
- Full work MUST delegate substantive implementation workstreams; the PM must not act as the primary coder/author.
- The PM may directly perform only narrow supporting glue, integration, verification, or localized follow-up fixes.
- A strong model being capable of doing everything itself is not a reason to bypass workers.

Before the first substantive change-producing action in Standard/Full mode, identify the worker-owned task(s) and dispatch the first ready task.

## 5. Git Defaults

Respect project-local Git policy when present.

Otherwise:

- never develop directly on `main`;
- preserve uncommitted user work;
- create/select an appropriate working branch before change-producing work;
- use `dev` only when it already exists and fits the repository;
- do not create `dev` merely because Agentic OS often uses it;
- never merge/promote to `main` without explicit approval for that exact promotion.

## 6. Work Autonomously

Continue without asking the user about routine, reversible implementation choices.

Escalate only according to:

`${CLAUDE_PLUGIN_ROOT}/core/ESCALATION_POLICY.md`

Do not ask the user to choose agents, models, test commands, branch names, implementation details, or review depth unless the choice genuinely crosses a human gate or required information cannot be recovered safely.

## 7. Verification Contract

Do not accept worker `PASS` as project truth.

For delegated work:

`worker self-verification → PM independent verification → independent Reviewer for medium/high risk → integration readiness`

A pre-implementation audit does not replace review of the final relevant diff.

If the PM directly performs a small follow-up fix, include that fix in the final independent review whenever review is required.

Use:

`${CLAUDE_PLUGIN_ROOT}/core/QUALITY_GATES.md`

as the canonical verification policy.

## 8. Skills and Templates

Methodology skills are native plugin components. Invoke them on demand rather than fetching them from GitHub:

- `methodology-os`
- `methodology-planning`
- `methodology-handoff`
- `methodology-retrospective`

When a canonical artifact template is needed, read it from:

`${CLAUDE_PLUGIN_ROOT}/templates/`

Do not reconstruct canonical templates from memory.

## 9. State and Documentation

Create durable project state only when continuity or complexity warrants it.

Prefer existing project deliverables when they already satisfy the same need. Do not create duplicate planning/status files merely to demonstrate methodology usage.

## 10. Completion

At the end, report concisely:

- delivered outcome;
- verification evidence;
- review status/findings;
- branch / PR / integration state;
- unresolved risks or human gates;
- meaningful Agentic OS friction or learning signals.

Do not merge to `main` unless explicitly authorized.
