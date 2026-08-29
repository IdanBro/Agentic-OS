# Methodology OS — Plan Template

> Purpose: define the current intended path from the Project Brief to completion. This file describes **how the work is expected to proceed**. Live status belongs in `STATE.md`.

## Metadata

- **Plan version:** `<v1>`
- **Created:** `<YYYY-MM-DD>`
- **Last materially updated:** `<YYYY-MM-DD>`
- **Based on Project Brief:** `<brief version/date>`
- **Lifecycle mode:** `<Standard | Full>`

## 1. Planning Objective

`<Concise statement of what this plan is intended to deliver.>`

## 2. Assumptions

Record only assumptions that materially affect sequencing or design.

- `<assumption>`
- `<assumption>`

If an assumption becomes false, the PM evaluates whether replanning is required.

## 3. Work Breakdown

Use stable IDs so `STATE.md`, task packets, reviews, and decisions can reference work without copying descriptions.

### P1 — `<Phase name>`

**Outcome:** `<phase-level outcome>`

**Dependencies:** `<none | phase/task IDs>`

**Exit criteria:**
- `<observable criterion>`
- `<observable criterion>`

#### P1-T1 — `<Task name>`

- **Objective:** `<bounded task outcome>`
- **Scope:** `<relevant files/components/artifacts or domain>`
- **Dependencies:** `<none | IDs>`
- **Acceptance:** `<observable acceptance criteria>`
- **Verification intent:** `<what must be proven>`
- **Likely execution:** `<PM direct | Implementer | investigation | other>`
- **Risk:** `<low | medium | high>`

#### P1-T2 — `<Task name>`

- **Objective:** `<bounded task outcome>`
- **Scope:** `<scope>`
- **Dependencies:** `<none | IDs>`
- **Acceptance:** `<criteria>`
- **Verification intent:** `<verification>`
- **Likely execution:** `<execution route>`
- **Risk:** `<low | medium | high>`

### P2 — `<Phase name>`

Repeat only as needed.

## 4. Dependency / Ordering Notes

Capture sequencing logic that is not obvious from task IDs.

- `<why X must precede Y>`
- `<what may run in parallel and why>`

## 5. Integration Strategy

For engineering work, describe how bounded changes become an integrated result.

- **Base branch:** `<usually dev>`
- **Task branch strategy:** `<branching approach>`
- **Integration checkpoints:** `<phase-level or final>`
- **System verification point:** `<when/how>`

For non-engineering work, replace this with the equivalent artifact integration strategy.

## 6. Risk-Driven Review Plan

Record only review requirements known at planning time.

| Area / Task | Risk | Planned independent review |
| --- | --- | --- |
| `<ID>` | `<low/medium/high>` | `<none / conditional / required>` |

Detailed verification rules remain governed by `core/QUALITY_GATES.md` when implemented.

## 7. Human Gates

List anticipated gates that may stop autonomous progression.

- `<gate and when it occurs>`

Do not invent approvals for routine work.

## 8. Completion Condition

The plan is complete when:

- all required project-level success criteria are satisfied,
- required task/phase acceptance criteria are satisfied,
- required verification and review gates pass,
- integrated state is coherent,
- no known blocker prevents the requested outcome,
- any required human gate is resolved.

## Replanning Rules

The Project Manager owns this artifact.

Replan when evidence shows the current path is materially wrong, incomplete, unsafe, or inefficient.

When replanning:

1. change the plan to the new intended path;
2. increment the plan version for a material restructure;
3. update `STATE.md` to reference the active plan version;
4. record a decision in `DECISIONS.md` only when the change is materially consequential or non-obvious;
5. preserve failed approaches only if repeating them would be costly.

Do **not** use this file as a progress diary. Do not append a chronological history of every plan revision. Git history and material decisions provide historical traceability.
