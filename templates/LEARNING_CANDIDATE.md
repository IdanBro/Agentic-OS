# Methodology OS — Learning Candidate Template

> Purpose: preserve one potentially reusable Methodology OS improvement while it is being evaluated. A candidate is **not active global policy** until explicitly promoted and integrated through the approved workflow.

Create this artifact only when a global candidate is worth durable follow-up. Do not create one for every retrospective observation.

---

## Metadata

- **Candidate ID:** `<LC-001>`
- **Title:** `<short causal title>`
- **Created:** `<YYYY-MM-DD>`
- **Last updated:** `<YYYY-MM-DD>`
- **Status:** `<CANDIDATE | NEEDS_EVIDENCE | VALIDATING | READY_FOR_PROMOTION | APPROVED | PROMOTED | REJECTED | DEFERRED | SUPERSEDED>`
- **Change impact:** `<L1 narrow guidance | L2 role/routing/workflow default | L3 global policy/constitution/authority>`
- **Evidence strength:** `<weak | moderate | strong + concise reason>`
- **Generalizability:** `<low | medium | high + concise reason>`
- **Owner:** `<PM / user / other>`
- **Source project(s):** `<references; avoid confidential details>`

---

## 1. Observed Problem / Opportunity

Describe what happened without prematurely claiming the cause.

`<Observable workflow problem, repeated cost, quality gap, or successful pattern.>`

Separate observation from interpretation.

---

## 2. Evidence

List only evidence that materially supports the candidate.

- `<project/task/eval reference>` — `<what it demonstrates>`
- `<project/task/eval reference>` — `<what it demonstrates>`

Do not paste raw logs, private code, secrets, credentials, customer data, or full conversation history.

When detailed evidence is project-private, keep it project-local and record only a sanitized causal summary/reference here.

---

## 3. Causal Hypothesis

`<Why does the current Methodology OS behavior appear to cause or fail to prevent the observed outcome?>`

### Alternative Explanations

- `<plausible alternative cause>`
- `<plausible alternative cause>`

If alternative explanations have been ruled out, state the evidence briefly.

---

## 4. Current OS Behavior

Reference the current behavior that may need refinement.

- **Policy / agent / skill / template:** `<reference>`
- **Current rule/default:** `<concise description>`

Do not duplicate complete policy text.

---

## 5. Proposed Generalized Change

State the **smallest generalized change** that addresses the causal hypothesis.

`<Proposed rule/default/template/skill/agent/eval change.>`

Avoid technology labels when the real cause is risk, ambiguity, context shape, authority, verification difficulty, or another general task characteristic.

---

## 6. Generalization Boundary

### Should Apply When

- `<condition>`
- `<condition>`

### Should Not Apply When

- `<counterexample / excluded condition>`
- `<counterexample / excluded condition>`

If this section cannot be written clearly, the candidate is probably not ready for promotion.

---

## 7. Expected Benefit

Describe only dimensions materially affected.

- **Quality:** `<benefit / neutral / unknown>`
- **Reliability:** `<benefit / neutral / unknown>`
- **Tokens / context:** `<benefit / cost / neutral / unknown>`
- **Elapsed time:** `<benefit / cost / neutral / unknown>`
- **Autonomy:** `<benefit / cost / neutral / unknown>`
- **Human interruption:** `<benefit / cost / neutral / unknown>`
- **Complexity / maintenance:** `<benefit / cost / neutral / unknown>`

Do not hide a tradeoff behind one aggregate score.

---

## 8. Regression / Complexity Risk

What could become worse if this candidate is promoted?

- `<risk>` — `<likely affected scenarios>`
- `<risk>` — `<likely affected scenarios>`

### Counterexample Search

`<A plausible case where the proposed rule would be unnecessary, harmful, or too expensive.>`

---

## 9. Validation Plan

Choose only evidence that could meaningfully change the decision.

- [ ] `<cross-project evidence>`
- [ ] `<historical replay>`
- [ ] `<synthetic eval>`
- [ ] `<controlled comparison / benchmark>`
- [ ] `<counterexample / regression test>`

### Evidence Still Needed

`<What evidence would move this candidate toward READY_FOR_PROMOTION or rejection?>`

If none, write `None; current evidence is sufficient for promotion review.`

---

## 10. Eval Expectations

For observable behavior changes, define at least one falsifiable scenario when practical.

```text
GIVEN: <scenario>
WHEN: <Methodology OS decision/action>
THEN: <expected compliant behavior>
FAIL IF: <behavior that would violate the candidate>
```

Additional evals:

- `<scenario reference / none yet>`

---

## 11. Proposed Change Surface

Likely files/components affected if promoted:

- `<core policy>`
- `<agent>`
- `<skill>`
- `<template>`
- `<eval>`

Keep the scope bounded to the candidate. Adjacent cleanup is not implicitly approved.

---

## 12. Promotion Recommendation

- **Recommendation:** `<promote | keep validating | narrow | reject | defer>`
- **Reason:** `<concise evidence-based rationale>`

If `promote`, explain why current evidence is sufficient for this impact level.

---

## 13. Human Promotion Decision

- **Decision:** `<pending | approved | approved narrower variant | rejected | deferred>`
- **Approved scope:** `<exact generalized change or n/a>`
- **Decision reference/date:** `<reference / n/a>`
- **Conditions:** `<required eval/review/implementation conditions / none>`

Do not infer approval from silence or from the user agreeing that the observation was interesting.

---

## 14. Implementation / Promotion Record

Complete only after approval and implementation begins.

- **Feature branch:** `<reference / n/a>`
- **PR:** `<reference / n/a>`
- **Eval changes:** `<references / n/a>`
- **Verification:** `<compact evidence / n/a>`
- **Reviewer:** `<result/reference / n/a>`
- **Integrated into `dev`:** `<yes/no/n/a>`
- **Promoted global behavior active in dev:** `<yes/no>`
- **`main` promotion:** `<not requested | awaiting separate approval | approved | complete | n/a>`

Promotion approval does not automatically authorize `main`.

---

## 15. Post-Promotion Evidence

Use only when later evidence materially changes confidence in the promoted rule.

- `<evidence>` — `<supports / challenges the candidate>`

### Follow-Up

`<none | narrow | supersede | revert | more evals>`

---

## Maintenance Rules

1. Preserve the distinction between observation, causal hypothesis, and policy proposal.
2. Keep evidence concise and reference-first.
3. Never store sensitive project information globally merely to support a methodology claim.
4. Update status when validation or human promotion state changes materially.
5. Do not mark `PROMOTED` until the approved change is actually integrated into canonical Methodology OS `dev` and required gates pass.
6. Link superseding candidates instead of rewriting old rationale.
7. Reject or drop weak candidates rather than building a candidate graveyard.
8. If implementation must materially exceed the approved change surface, return to the human promotion gate.
