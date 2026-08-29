---
name: methodology-planning
description: Plan or replan Standard/Full Methodology OS work using the project brief, current state, dependencies, acceptance criteria, risk, verification strategy, and human gates. Use when work needs a structured execution plan; do not use for trivial one-step tasks.
---

# Methodology Planning

Create or revise the smallest plan that makes execution safe, bounded, and verifiable.

## Inputs

Use the current project sources where available:

- `PROJECT_BRIEF.md` — stable outcome, scope, constraints, success criteria;
- `STATE.md` — current operational truth;
- `DECISIONS.md` — relevant durable decisions;
- repository/artifact evidence needed to understand dependencies;
- explicit user constraints and approvals.

Do not reconstruct the project from chat history when canonical state exists.

## Workflow

### 1. Confirm the Outcome

State what must become true when the planned work succeeds.

If the project brief is materially ambiguous, inspect available evidence first. Escalate only when the ambiguity represents a real high-impact choice that cannot be safely resolved from context.

### 2. Choose Planning Depth

- Lite work normally does not need a durable plan artifact.
- Standard work gets a concise phase/task plan when multiple steps, dependencies, or meaningful verification exist.
- Full work gets structured phases, dependencies, risk, integration, and human gates.

Do not turn planning depth into ceremony.

### 3. Decompose by Outcomes

Create tasks that have:

- a stable ID;
- one coherent outcome;
- dependencies;
- observable acceptance criteria;
- verification intent;
- risk classification;
- relevant human gates.

Tasks intended for workers must be bounded enough to become Task Packets.

Avoid task descriptions such as:

- "do backend";
- "handle Kubernetes";
- "finish infra".

### 4. Preserve Worker Autonomy

Plan **what must become true** more than **exactly how to code it**.

Do not freeze low-impact implementation choices that a bounded worker can make safely from project conventions.

Specify implementation approach when:

- architecture has already been decided;
- compatibility demands it;
- the approach is part of acceptance;
- allowing arbitrary choice would create material divergence or risk.

### 5. Identify Dependencies

Mark true sequencing dependencies explicitly.

Do not invent dependencies merely to make the plan look structured.

Identify work that can run in parallel only when:

- tasks are meaningfully independent;
- mutable state does not overlap dangerously;
- integration is deterministic enough to justify the coordination cost.

### 6. Attach Verification Intent

Each meaningful task should say how success will later be demonstrated.

Examples:

- targeted test behavior;
- build/type/lint checks;
- rendered configuration inspection;
- Terraform plan;
- runtime smoke test;
- source/claim cross-check;
- artifact render inspection.

Do not confuse a planned check with evidence that it has already run.

### 7. Identify Risk and Review Needs

Classify work as low, medium, or high risk based on consequence and detectability of failure.

Remember:

- medium/high risk requires an independent Reviewer under V0;
- high-risk work needs deeper PM verification and stronger system evidence;
- human gates are separate from Reviewer gates.

### 8. Identify Human Gates

Mark only consequential decisions/operations that require explicit approval.

Do not ask the user to choose routine implementation details.

### 9. Define Integration Strategy

For engineering work, normally plan toward:

```text
working branch
→ task verification/review
→ dev
→ system verification when needed
→ main only after explicit user approval
```

Respect stronger repository-specific conventions when present.

### 10. Write or Revise `PLAN.md`

Use the canonical template.

A plan revision should:

- preserve stable work IDs where meaning is unchanged;
- increment plan version when the execution contract materially changes;
- record why meaningful replanning occurred;
- preserve valid completed work rather than restarting from zero.

Do not duplicate live progress into the plan. `STATE.md` owns current operational status.

## Replanning Trigger

Replan when evidence invalidates a material assumption, dependency, task boundary, acceptance condition, or approach.

Do not replan merely because implementation required a small local adjustment.

## Output Standard

A good plan lets the PM answer:

1. What outcome are we pursuing?
2. What are the bounded work items?
3. What must happen first?
4. What can happen independently?
5. How will each meaningful outcome be verified?
6. Where are the meaningful risks?
7. Where must the user explicitly decide?
8. How does the work integrate safely?

Keep the result compact enough that workers can receive only the relevant slice rather than the entire project plan.
