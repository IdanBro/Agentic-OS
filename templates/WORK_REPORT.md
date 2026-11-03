# Methodology OS — Work Report Template

> Purpose: return a compact, evidence-oriented result from a delegated execution task to the Project Manager.

The report is a context boundary. It should preserve what the PM needs to verify, decide, integrate, or route next — not reproduce the worker's transcript.

This template is the default for Implementers and other change-producing workers. Reviewer and Debugger role definitions may use stricter specialized output formats.

---

## Metadata

- **Task ID:** `<stable task/plan ID>`
- **Worker role:** `<implementer / other>`
- **Status:** `<PASS | PARTIAL | BLOCKED | FAILED>`
- **Packet version:** `<v# if relevant>`
- **Branch / artifact:** `<reference or n/a>`

Status semantics:

- **PASS** — all acceptance criteria are believed satisfied and required self-verification was completed. PM verification is still required.
- **PARTIAL** — useful scoped progress exists, but acceptance is incomplete. The task remains open.
- **BLOCKED** — further meaningful progress requires a PM/human decision, permission, dependency, or external condition.
- **FAILED** — the attempted approach did not achieve the outcome and continuing without diagnosis/replanning would be guesswork or repetition.

Never use `PASS` to mean "I made changes" or "the code looks plausible."

---

## 1. Outcome Summary

In 1–4 bullets, state the meaningful result.

- `<what became true / what changed>`
- `<important result>`

For `PARTIAL`, distinguish completed value from remaining work.

For `BLOCKED` or `FAILED`, state the point at which the task stopped.

---

## 2. Acceptance Criteria

Report against the packet's stable acceptance IDs.

| Criterion | Status | Evidence / Note |
| --- | --- | --- |
| `AC-1` | `<PASS / FAIL / PARTIAL / NOT VERIFIED>` | `<compact evidence or reason>` |
| `AC-2` | `<PASS / FAIL / PARTIAL / NOT VERIFIED>` | `<compact evidence or reason>` |

Rules:

1. Do not mark an acceptance criterion `PASS` merely because implementation code exists.
2. If a criterion was changed by the PM during execution, reference the current packet version.
3. If evidence shows a criterion is invalid or contradictory, report that explicitly rather than silently redefining it.

---

## 3. Meaningful Changes

List only changes the PM may need to inspect, verify, or understand.

- `<path / component>` — `<meaningful change>`
- `<path / component>` — `<meaningful change>`

Do not enumerate trivial edits line by line.

### Supporting Changes Outside Initial Paths

If the worker used the Task Packet supporting-change rule, list each such change and why it was required.

- `<path/component>` — `<why directly required>`

If none, write `None.`

---

## 4. Verification Performed

Record only checks actually executed or directly inspected.

| Check | Result | Evidence |
| --- | --- | --- |
| `<command / inspection>` | `<PASS / FAIL>` | `<concise output/result/reference>` |

Examples:

- `pytest tests/auth -q` — PASS — `18 passed`
- `helm lint charts/api` — PASS — no lint errors
- rendered Deployment inspection — PASS — readiness/liveness probes present

Do not paste full logs unless the relevant evidence cannot be represented compactly.

### Required Verification Not Performed

- `<check>` — `<why it could not be performed>`

If none, write `None.`

A required check that was not performed is a material uncertainty and may prevent worker `PASS` depending on the acceptance contract.

---

## 5. Evidence for PM Verification

Provide the smallest set of references/evidence that lets the PM independently verify important claims.

- `<file/path/line/diff/command/artifact reference>` — `<claim it supports>`
- `<reference>` — `<claim it supports>`

Do not ask the PM to trust your narrative.

Prefer evidence the PM can independently re-open or re-run.

---

## 6. Assumptions / Scope Notes

Record only assumptions or scope choices that affected the result.

- `<low-impact inference made>`
- `<small supporting change>`
- `<unexpected local constraint>`

If none, write `None.`

Do not use this section as a chronological work log.

---

## 7. Remaining Uncertainty

- `<unverified behavior / residual risk / unknown>`

If none, write `None known within task scope.`

A worker may still return `PASS` with a minor, explicitly bounded residual uncertainty only when the packet's required criteria and checks are satisfied and the uncertainty does not materially undermine the completion claim.

Material uncertainty should produce `PARTIAL`, `BLOCKED`, or `FAILED` instead.

---

## 8. Non-PASS Continuation

Complete this section only for `PARTIAL`, `BLOCKED`, or `FAILED`.

### What Remains

`<specific unsatisfied outcome / acceptance criterion>`

### Why It Remains

`<cause, blocker, or current evidence>`

### Minimum Next Action

`<the smallest justified next step>`

### PM Decision Required

`<exact decision/permission, or "None — recommend debugger/replan">`

For `BLOCKED`, identify the **minimum decision or dependency** needed to resume.

For `FAILED`, include what has already been ruled out so the next agent does not repeat uninformative attempts.

---

## 9. Observations Outside Scope

Optional. Report an adjacent issue only when it has plausible future value or risk.

- `<observation>` — `<why the PM may care>`

Do not fix unrelated issues merely because they were discovered.

If none, omit this section or write `None.`

---

## Compact Report Form

For small, successful bounded tasks, the report may be compressed to:

```text
TASK: <ID>
STATUS: PASS

OUTCOME
- <meaningful result>

ACCEPTANCE
- AC-1: PASS — <evidence>
- AC-2: PASS — <evidence>

CHANGED
- <path>: <change>

VERIFIED
- <check>: PASS — <result>

PM EVIDENCE
- <reference>

UNCERTAINTY
- None known within scope.
```

Do not use the compact form when status is not `PASS`, when risk is high, or when material assumptions/uncertainty need explanation.

---

## Report Quality Rules

A good report lets the PM answer:

1. What actually changed or was achieved?
2. Which acceptance criteria are satisfied?
3. What was genuinely verified?
4. What evidence can I independently check?
5. Did the worker cross or stretch scope?
6. What remains uncertain?
7. If incomplete, what is the next decision/action?

The report SHOULD NOT contain:

- hidden chain-of-thought or long reasoning narratives;
- full command transcripts;
- large logs;
- full diffs the PM can inspect directly;
- repeated project background;
- confidence language without evidence;
- claims that the overall project is complete.

The PM must independently verify the task after receiving this report. Worker `PASS` is input to verification, not a quality gate by itself.