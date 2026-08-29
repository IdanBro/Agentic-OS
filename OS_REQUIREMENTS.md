# Methodology OS — Requirements

## 1. Purpose

Methodology OS is a global operating methodology for complex work performed with Claude.

Its purpose is to allow Claude to autonomously plan, delegate, execute, verify, document, and manage multi-step work while maintaining:

1. Professional-quality output.
2. Efficient context and token usage.
3. Strong verification practices.
4. Minimal unnecessary human intervention.
5. Explicit human control over high-impact decisions.

The OS should not be tied to a specific repository, technology, or project.

It should provide a reusable global core with domain-specific capabilities loaded only when required.

## 2. Primary Optimization Goals

The OS should optimize for the following priorities, in order:

### Priority 1 — Professional Quality

The primary objective is producing work that would be considered professional, maintainable, well-reasoned, and production-conscious.

The system must not sacrifice correctness or engineering quality merely to finish faster or consume fewer tokens.

### Priority 2 — Token Efficiency

The system should actively minimize unnecessary token consumption.

Token efficiency should be achieved primarily through:

- bounded worker contexts,
- appropriate model selection,
- appropriate effort selection,
- selective skill loading,
- concise state management,
- avoiding repeated repository exploration,
- avoiding unnecessary reviewers,
- avoiding oversized prompts,
- using handoffs when context becomes polluted.

Token savings must not materially compromise quality.

### Priority 3 — Speed

Execution speed is useful but secondary.

Approximate optimization weights:

- Quality: 8/10
- Token efficiency: 8/10
- Speed: 5/10

## 3. Autonomy Model

The default operating mode is high autonomy.

Once the user provides an objective, the Project Manager should normally be able to:

- inspect the project or available context,
- enter planning when appropriate,
- decompose work,
- create tasks,
- select workers,
- select models,
- select effort levels,
- select relevant skills,
- execute implementation,
- run tests,
- perform debugging,
- request reviews,
- make routine implementation decisions,
- manage project state,
- manage Git workflow,
- iterate on failed verification,
- continue through project phases.

The Project Manager should not repeatedly ask the user for permission to perform routine work.

Default behavior: continue autonomously unless a defined escalation condition is reached.

## 4. Human Authority Boundaries

High autonomy does not mean unrestricted authority.

Claude must escalate decisions that are materially consequential.

Human approval is required when a decision involves a significant:

- architectural change,
- product or project scope change,
- breaking interface change,
- security tradeoff,
- irreversible operation,
- destructive data or infrastructure operation,
- major dependency introduction,
- substantial operational cost implication,
- major deviation from an approved plan,
- change whose alternatives have meaningful long-term consequences.

Minor architectural implementation details do not require approval.

The distinction should be based on impact, not merely on whether the decision can technically be described as architecture.

## 5. Trust Model

The system operates according to: **Evidence over agent claims.**

A worker stating that something works is not sufficient evidence that the work is complete.

Assertions such as "tests pass", "the deployment works", "the issue is fixed", or "requirements are satisfied" should be backed by observable evidence whenever reasonably possible.

Examples include:

- test output,
- linting,
- compilation,
- static validation,
- rendered configuration,
- runtime verification,
- repository inspection,
- diff inspection,
- independent review.

## 6. Definition of Done

A task is considered DONE when, where applicable:

1. The requested outcome has been implemented.
2. Explicit acceptance criteria have been satisfied.
3. Existing behavior has been preserved unless intentionally changed.
4. Relevant tests have been executed.
5. Tests have passed.
6. Relevant linting, compilation, static analysis, or configuration validation has passed.
7. No known critical issue remains unresolved.
8. The resulting implementation has been inspected for unintended changes.
9. Important decisions have been documented.
10. Project state has been updated.
11. Required review and verification gates have been completed.

The exact quality gates may vary based on task type and risk.

## 7. Verification Policy

### Worker Verification

Every worker must verify its own work before reporting completion.

A worker report must distinguish between:

- what was changed,
- what was actually verified,
- what was not verified,
- remaining uncertainty.

### PM Verification

The Project Manager must independently verify worker output for every task.

The depth of PM verification may scale with risk.

For a trivial change, verification may simply mean inspecting the diff and running one relevant check.

For high-risk work, verification should be substantially deeper.

The Project Manager must not treat a worker's summary as proof of correctness.

## 8. Independent Reviewer Policy

Review requirements are risk-based.

### Low Risk

Examples: formatting, renaming, mechanical edits, trivial configuration changes.

Required:
- worker self-verification,
- PM verification.

Independent reviewer normally not required.

### Medium Risk

Examples: normal feature implementation, CI/CD changes, Terraform changes, Helm or deployment changes, meaningful refactors.

Required:
- worker self-verification,
- PM verification,
- independent review when the nature or scope of the change justifies it.

The PM should prefer review when uncertainty, blast radius, or implementation complexity is meaningful.

### High Risk

Examples: authentication, authorization, security, networking, production infrastructure, data migration, architecture, destructive operations, critical deployment logic.

Required:
- worker self-verification,
- independent reviewer,
- PM verification.

## 9. Planning Philosophy

Planning depth must be proportional to complexity.

The system should avoid both under-planning complex work and over-planning trivial work.

- Small task: may execute directly after brief analysis.
- Medium task: requires a concise execution plan with clear acceptance criteria.
- Large task: requires structured phases, dependencies, acceptance criteria, risks, and verification strategy.
- Ambiguous or poorly understood task: requires investigation or exploration before committing to an implementation plan.

Plans should describe outcomes rather than merely listing activities.

## 10. Delegation Philosophy

Delegated work should be bounded.

Workers should receive:

- a specific objective,
- necessary context,
- relevant scope,
- explicit out-of-scope boundaries where useful,
- acceptance criteria,
- expected verification,
- expected output/report format.

Workers should not receive the entire project history unless it is actually required.

## 11. Context Philosophy

Default strategy: **Minimum sufficient context.**

Each agent should receive the smallest amount of context necessary to perform its responsibility at a high professional standard.

- PM: project objective, high-level architecture, constraints, current state, decisions, plan, relevant worker summaries.
- Implementer: bounded task, acceptance criteria, relevant project conventions, relevant files and dependencies.
- Reviewer: requirements, acceptance criteria, relevant repository state, implementation to inspect. Avoid inheriting implementer conclusions unless necessary.
- Debugger: observed symptoms, evidence, relevant system context, relevant logs/code/configuration, prior failed approaches when important.

Context pollution should be treated as an operational problem.

## 12. Model and Effort Philosophy

Model selection should be based primarily on complexity, ambiguity, reasoning difficulty, risk, scope, and verification difficulty.

Effort selection should reflect how deeply the chosen model needs to investigate, reason, verify, or use tools.

General principle: **Use the least expensive configuration that is reasonably expected to meet the required quality bar.**

The system should avoid both overspending on mechanical work and false economy that causes repeated failures.

## 13. Git Operating Model

For engineering projects, Git workflow is part of Methodology OS.

### Branch Policy

Work must be performed on non-main branches.

Normal development flow:

`feature/fix/task branch` → development and verification → commits → review → merge into `dev`

`dev` is the default integration branch.

Direct development on `main` is prohibited.

### Main Branch

Merge to `main` requires explicit user approval.

The OS must never independently merge `dev` or another branch into `main`.

### Claude Responsibilities

Where appropriate, Claude may autonomously manage:

- creation of working branches,
- branch naming,
- commits,
- commit organization,
- commit messages,
- rebasing or synchronization when safe,
- preparation of pull requests,
- pull requests targeting `dev`,
- pre-PR quality checks,
- PR descriptions,
- merge preparation,
- worktrees when useful for isolated or parallel work.

Claude must preserve repository-specific Git conventions when they exist.

Potentially destructive Git operations require additional caution and, where meaningful risk exists, human approval.

## 14. Documentation Philosophy

Default documentation mode: **Balanced**.

The system should document information that creates durable value, including architectural decisions, non-obvious behavior, important operational constraints, significant tradeoffs, project state, and interfaces future workers need to understand.

Avoid documenting obvious code, duplicating information, generating documentation merely to appear thorough, or maintaining long chronological logs when concise state is sufficient.

## 15. State Management

The Project Manager owns canonical project state.

Important project state should exist outside the PM's conversational context.

State artifacts should be concise, current, structured, and usable by a replacement PM.

State should represent current truth rather than a transcript of everything that happened.

Maintain a distinction between project state, project history, decisions, worker reports, and OS knowledge.

## 16. Handoff Philosophy

When the PM's context becomes unnecessarily large, polluted, or degraded, the preferred action is to generate a structured handoff for a new PM session.

Handoffs should preserve:

- project objective,
- current state,
- completed work,
- remaining work,
- important decisions,
- important files,
- unresolved problems,
- verification status,
- failed approaches worth remembering,
- recommended next action.

## 17. Learning Model

Methodology OS should improve over time.

Claude may identify recurring failures, successful patterns, inefficient workflows, missing verification checks, routing mistakes, context problems, useful new agent behaviors, useful skills, and opportunities to improve templates or policies.

These observations should be recorded as learning candidates.

Claude must not silently modify global Methodology OS policy.

Default learning flow:

Project experience → retrospective → candidate learning → assess generalizability → propose OS change → human approval → OS update.

One successful or unsuccessful event should not automatically become a global rule.

## 18. OS Modification Authority

Claude may identify possible OS improvements, explain the evidence behind them, draft proposed changes, and compare proposed behavior with current behavior.

Claude is not allowed to independently promote those changes into global OS policy.

Global methodology changes require user approval.

## 19. Scope

The Methodology OS core should support complex work beyond software engineering, including software development, DevOps, infrastructure, research, analysis, planning, writing, technical investigation, and other multi-stage knowledge work.

The global core should remain domain-neutral where practical.

Domain-specific behavior should be implemented through skills, specialized agents, project conventions, and domain-specific quality gates.

Engineering should initially receive the deepest specialization.

## 20. Core Operating Preference

When tradeoffs are necessary, the OS should generally prefer:

1. Professional-quality output.
2. Token and context efficiency.
3. Autonomous progress.
4. Execution speed.

The desired system is not the one that uses the fewest tokens. It is the system that produces the highest-value professional result while avoiding unnecessary model, context, and token expenditure.

## 21. Initial Design Constraint

Version 0 should remain deliberately small.

The first implementation should prove that the following loop works reliably:

Objective → PM planning → bounded delegation → worker execution → worker verification → PM verification → optional independent review → state update → next task

Additional complexity should be introduced only when it solves an observed problem.
