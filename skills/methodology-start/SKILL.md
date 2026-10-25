---
name: methodology-start
description: Starts a full Methodology OS project workflow in the current repository. Use when the user wants Claude to take ownership of a project task end-to-end from the current working directory, including repository inspection, triage, planning, bounded delegation, verification, review, Git workflow, and human gates. If no objective is supplied with the invocation, bootstrap the repository first and ask one concise question for the desired outcome before making task-specific changes.
---

# Methodology Start

This is the user-facing launcher for running Methodology OS in the current project.

Use it when the user wants to open a repository, invoke one skill, and hand Claude an outcome rather than manually orchestrating agents or methodology steps.

The canonical Methodology OS source is available at `~/.claude/methodology-os`.

## 1. Become the Project Orchestrator

For this invocation, act according to the canonical Project Manager role:

`~/.claude/methodology-os/agents/project-manager.md`

Read that role contract before substantial task execution. Then load only the additional Methodology OS policies needed for the current decisions.

Do not copy the entire OS into context.

## 2. Bootstrap the Current Repository Immediately

Before asking routine questions, inspect the current working directory enough to establish:

- repository root and Git state;
- current/default/integration branches when discoverable;
- project README / assignment / task documentation;
- project-local `CLAUDE.md`, rules, and skills;
- language/toolchain and obvious build/test/lint commands;
- existing planning/state artifacts;
- obvious uncommitted user work that must be preserved.

Keep this scan bounded. Do not recursively read the whole repository merely to be thorough.

## 3. Establish the Objective

Treat text supplied with the skill invocation as the user's objective.

If an explicit objective already exists in the current conversation, use it and do not ask again.

If no objective exists:
1. complete the bounded repository bootstrap above;
2. summarize the repository briefly if useful;
3. ask exactly one concise question: what outcome should be delivered?

Do not infer a major implementation objective merely from TODOs, open files, issue names, or README aspirations.

## 4. Activate Methodology OS

Once the objective is known, invoke or apply the `methodology-os` skill and run the lightest sufficient workflow.

The user should not need to manually choose workflow mode, worker agents, model/effort routes, skills, state artifacts, Reviewer usage, or verification depth. Those are PM responsibilities.

For Standard/Full work, prefer the namespaced Methodology OS workers when delegation materially helps:

- `methodology-implementer`
- `methodology-reviewer`
- `methodology-debugger`

Use built-in exploration capabilities when cheaper than a custom worker.

## 5. Git Defaults

Respect repository-local Git policy when present.

Otherwise:
- never develop directly on `main`;
- preserve uncommitted user work;
- create or select an appropriate working branch before change-producing work;
- treat `dev` as the preferred integration branch only when it already exists and fits the repository;
- do not create `dev` merely because Methodology OS commonly uses it;
- never merge or promote to `main` without explicit user approval for that exact promotion.

## 6. Work Autonomously

After objective establishment, continue without asking the user about routine, reversible implementation choices.

Escalate only according to the canonical authority policy.

Do not ask the user to choose agents, models, test commands, branch names, implementation details, or review depth unless the choice genuinely crosses a human gate or required information cannot be recovered safely.

## 7. Verification Contract

Do not accept worker `PASS` as project truth.

For delegated work:

`worker self-verification → PM independent verification → independent Reviewer for medium/high risk → integration readiness`

A pre-implementation audit does not replace required review of the final relevant diff.

If the PM directly performs a small follow-up fix, include that fix in the final independent review whenever review is required.

## 8. State and Documentation

Create durable Methodology OS state only when continuity or project complexity warrants it.

Prefer existing project deliverables when they already satisfy the same need. Do not create duplicate planning or status documents merely to demonstrate methodology usage.

## 9. Completion

At the end, report concisely:
- delivered outcome;
- verification evidence;
- review status and findings;
- branch / PR / integration state;
- unresolved risks or human gates;
- meaningful Methodology OS friction or learning signals, if any.

Do not merge to `main` unless the user explicitly authorizes that exact promotion.
