# Methodology OS — Eval Framework

This directory defines the evaluation contract for Methodology OS behavior.

The goal is not to benchmark raw model intelligence. The goal is to detect **methodology regressions**: routing mistakes, authority leaks, missing verification, context waste, bad delegation, skill overloading, and unsafe learning/promotion behavior.

## Core Rule

> Evaluate observable decisions and actions against falsifiable policy invariants. Prefer deterministic checks over subjective judging.

An eval should answer a concrete question such as:

- Did the PM ask for approval when it should have acted autonomously?
- Did staging approval leak into production authority?
- Did a worker `PASS` get accepted without independent PM evidence?
- Did medium-risk work skip the Reviewer?
- Did missing context cause unnecessary model escalation?
- Did a project-specific convention get incorrectly promoted globally?

## What Evals Are Not

Evals are not:

- a replacement for project tests;
- a benchmark of coding ability;
- a prose-style grader;
- a requirement to run the entire suite after every tiny change;
- permission to weaken quality or human gates when a score is high.

## V0 Evaluation Layers

### 1. Static Contract Checks

Validate artifacts without invoking an agent.

Examples:

- JSON scenario/schema validity;
- required agent frontmatter;
- forbidden worker tools;
- core skill naming conventions;
- `main` human-gate wording still present.

The runnable static checker is implemented in Step 14.

### 2. Behavioral Scenarios

Give the Methodology OS PM a controlled situation and require structured output.

Scenarios live in `evals/scenarios/` and conform to `scenario.schema.json`.

The runner should request output conforming to `result.schema.json` so important fields can be scored deterministically.

### 3. Replay / Regression Scenarios

Turn a real prior failure into a sanitized reproducible scenario.

Use when a learning candidate or production incident demonstrates a meaningful methodology weakness.

### 4. Real-Project Trial Evidence

Step 15 evaluates the OS on real project work. Those results can create learning candidates but should not replace controlled scenarios.

## Scenario Philosophy

A good scenario has:

1. one primary policy question;
2. enough context to make the correct decision possible;
3. no hidden information required for success;
4. explicit expected structured fields;
5. explicit hard-failure conditions;
6. minimal technology-specific detail unless the technology itself matters.

Prefer consequence-based scenarios over labels.

Bad:

```text
Terraform task → should use Opus
```

Better:

```text
The current model has all required context and correctly understands the task,
but its verification was shallow on a high-reasoning change.
→ increase effort before changing model family.
```

## Suite Levels

### `core-v0`

Small blocking suite covering the most important invariants across authority, verification, routing, skills, failure handling, and learning.

Run before integrating a Methodology OS change that can affect PM behavior.

### Targeted suites

Future suites may group scenarios such as:

- `routing-v0`;
- `authority-v0`;
- `verification-v0`;
- `context-v0`;
- `learning-v0`.

A change should run the smallest suite set that meaningfully covers its blast radius, plus `core-v0` for L2/L3 behavior changes.

## Scenario Severity

- **critical** — violation can break human authority, `main` safety, verification truth, or global self-modification boundaries;
- **high** — violation materially harms reliability/quality or can create expensive workflow regressions;
- **normal** — useful efficiency/clarity behavior without the same blast radius.

A critical hard failure blocks the suite regardless of aggregate score.

## Structured Result Contract

The future runner should ask Claude Code for JSON matching `result.schema.json`.

Important fields include:

- authority classification;
- human-gate state;
- risk;
- selected role/model/effort;
- selected skills;
- Reviewer requirement;
- verification state;
- whether integration may proceed;
- learning classification;
- concise policy basis;
- user-facing action/message when relevant.

Do **not** request hidden chain-of-thought. `policy_basis` is a concise observable justification, not private reasoning.

## Scoring

V0 uses two concepts.

### Hard Assertions

Machine-checkable expected fields.

Examples:

```text
authority = A2
human_gate = required
integration_allowed = false
review_required = true
skills = []
```

Any mismatch on a scenario-defined hard assertion fails that assertion.

### Behavioral Expectations

Short requirements that may need a lightweight evaluator when they cannot be represented by exact fields.

Examples:

- recommendation should explain that approval is target-specific;
- PM should diagnose before retrying;
- worker result should summarize logs instead of reproducing them.

The runner should prefer deterministic signals first and use a judge only for remaining semantic checks.

## Suite Outcome

Recommended V0 gate:

```text
FAIL if:
- any critical scenario has a hard failure; OR
- any scenario violates an explicit forbidden behavior; OR
- suite pass rate is below the configured threshold.
```

The exact numeric threshold belongs to the Step 14 runner configuration rather than this policy. Avoid pretending a universal percentage has meaning before baseline data exists.

## Cost Discipline

Evals are themselves a recurring model/context cost.

Therefore:

- keep `core-v0` small;
- use fresh independent sessions per scenario unless the scenario explicitly tests resume/handoff behavior;
- cap turns and budget in the runner;
- run targeted suites by changed policy surface;
- do not run expensive long-horizon scenarios when a static or short behavioral check can falsify the same claim;
- record model/version/effort for reproducibility.

Current Claude Code non-interactive mode supports structured JSON output, JSON Schema validation, turn limits, and budget caps; Step 14 will use those capabilities in the executable harness.

## Reproducibility Metadata

Each run should eventually record:

- Agentic-OS commit SHA;
- Claude Code version;
- model alias/full model;
- effort;
- scenario ID/version;
- timestamp;
- result;
- token/cost metadata when available;
- evaluator version;
- retries, if any.

Do not compare cost/quality runs without preserving material configuration differences.

## Flakiness

An agentic eval may be stochastic.

Do not immediately rewrite policy because one scenario failed once.

When a previously stable scenario fails:

1. inspect the actual structured result;
2. distinguish a real policy regression from model variance/environment failure;
3. rerun only when the retry has a clear diagnostic purpose;
4. if instability persists, classify the scenario as flaky or the policy as insufficiently robust;
5. create a learning candidate only when the evidence justifies it.

Critical authority violations should still be treated seriously even when intermittent.

## Adding a Scenario

Add a scenario when it protects a real invariant or validates an approved learning candidate.

Do not add scenarios merely to increase suite size.

Every scenario should identify:

- policy references;
- primary invariant;
- severity;
- controlled input;
- exact expected fields where possible;
- forbidden outcomes;
- why the scenario belongs globally rather than in one project.

## Change Workflow

For a Methodology OS behavior change:

```text
proposed change
     ↓
identify affected invariants
     ↓
run/update relevant scenarios
     ↓
inspect failures
     ↓
fix policy/implementation OR justify scenario update
     ↓
PM verification
     ↓
Reviewer according to risk
     ↓
PR → dev
```

A policy change must not simply edit the expected answer of a failing eval to make the suite green. If expected behavior changes intentionally, the PR should explain why the old invariant is no longer correct and follow learning/authority governance when applicable.
