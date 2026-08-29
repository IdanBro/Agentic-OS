# Methodology OS — Verification & Quality Gates

This document defines the canonical verification system for Methodology OS.

Its purpose is to prevent agent confidence, plausible-looking changes, or incomplete testing from being mistaken for completion. The system separates **worker self-verification**, **Project Manager independent verification**, **independent review**, **integration verification**, and **human-gated promotion**.

The Project Manager owns gate selection, gate execution coordination, evidence quality, and the final decision to accept or reject a task for integration.

---

## 1. Core Rule

> A claim becomes project truth only when it has evidence appropriate to its risk and has passed every required gate.

Verification is not a single test command. It is a chain of evidence and independent checks whose depth scales with consequence, ambiguity, and verification difficulty.

The system MUST distinguish:

- implementation from verification,
- worker confidence from evidence,
- self-verification from independent verification,
- review from PM verification,
- branch verification from integrated-system verification,
- technical readiness from human approval.

Human approval never converts an unverified claim into a verified one.

---

## 2. Canonical Gate Chain

For delegated change-producing work, the normal chain is:

```text
TASK CONTRACT
    ↓
WORKER EXECUTION
    ↓
G1 — WORKER SELF-VERIFICATION
    ↓
WORK REPORT
    ↓
G2 — PM INDEPENDENT VERIFICATION
    ↓
G3 — INDEPENDENT REVIEW (medium/high risk)
    ↓
G4 — INTEGRATION READINESS
    ↓
MERGE / INTEGRATE INTO dev
    ↓
G5 — POST-INTEGRATION / SYSTEM VERIFICATION
    ↓
READY FOR NEXT PHASE
```

When the requested outcome requires promotion to `main`:

```text
verified dev state
    ↓
G6 — MAIN PROMOTION READINESS
    ↓
HUMAN APPROVAL
    ↓
merge / release / promote
```

Not every task requires every expensive check, but no required gate may be silently skipped.

---

## 3. Risk Classification Drives Verification Depth

Risk is about the consequence and detectability of being wrong, not the number of changed lines.

The PM assigns risk before execution and revises it upward when new evidence warrants it.

### 3.1 Low Risk

Typical characteristics:

- local and easily reversible,
- small blast radius,
- deterministic outcome,
- easy to verify,
- little security/operational consequence,
- cheap failure and recovery.

Examples:

- formatting,
- copy/text corrections,
- mechanical renames,
- narrow documentation edits,
- trivial non-sensitive configuration changes,
- obvious test-only maintenance.

Required:

- worker/self-verification where delegated,
- PM verification,
- no independent Reviewer by default.

### 3.2 Medium Risk

Typical characteristics:

- normal functional behavior changes,
- several interacting files/components,
- meaningful regression potential,
- infrastructure/configuration changes with non-trivial effect,
- CI/CD or deployment behavior changes,
- meaningful refactoring,
- verification requires more than one obvious check.

Examples:

- normal feature implementation,
- Helm or Kubernetes deployment changes,
- Terraform changes that are not high-blast-radius production operations,
- CI/CD pipeline changes,
- API behavior changes,
- meaningful application refactors.

Required:

- worker/self-verification,
- PM independent verification,
- independent Reviewer,
- appropriate pre-integration checks.

**V0 clarification:** once work is classified `medium`, independent review is mandatory. If the PM concludes review is unnecessary, it must first determine whether the work was over-classified and can defensibly be reclassified `low`. Token cost alone is not a reason to waive a medium-risk review.

### 3.3 High Risk

Typical characteristics:

- large blast radius,
- production or critical infrastructure impact,
- difficult rollback,
- security/authentication/authorization consequences,
- data integrity or migration risk,
- networking or distributed-system subtlety,
- destructive or irreversible behavior,
- architecture with meaningful long-term consequences,
- verification is indirect or difficult.

Examples:

- authentication or authorization changes,
- security-sensitive logic,
- production networking,
- data migration,
- destructive infrastructure changes,
- critical deployment/rollback logic,
- architecture changes,
- production stateful-system changes.

Required:

- worker/self-verification,
- deeper PM independent verification,
- independent Reviewer,
- explicit residual-risk assessment,
- stronger integration/system verification,
- any applicable human gate before consequential execution.

When uncertainty exists between two risk levels, investigate enough to classify confidently or use the higher level.

---

## 4. Verification Status Vocabulary

For a verification claim or gate, use:

- `PASS` — sufficient relevant evidence supports the claim.
- `FAIL` — evidence shows the claim or criterion is not satisfied.
- `INCONCLUSIVE` — evidence is insufficient or conflicting.
- `NOT_RUN` — an expected check was not executed.
- `N/A` — the check genuinely does not apply, with a reason when non-obvious.

`INCONCLUSIVE` is not a soft pass.

`NOT_RUN` is not evidence of success.

`N/A` must not be used to hide an unavailable or inconvenient check.

Worker execution statuses (`PASS / PARTIAL / BLOCKED / FAILED`) remain separate from verification-gate statuses.

Reviewer verdicts (`PASS / PASS_WITH_NOTES / FAIL / INCONCLUSIVE`) also remain separate.

---

## 5. Evidence Standard

Evidence should be proportional to the claim.

### Strong Evidence

Examples include:

- deterministic automated tests that exercise the changed behavior,
- successful build/compile/type-check/static validation,
- rendered configuration inspected against acceptance criteria,
- dry-run/plan output for infrastructure changes,
- runtime behavior observed in an appropriate environment,
- targeted negative/failure-path tests,
- direct inspection of the final diff/artifact,
- integration/system checks after merge,
- reproducible command output tied to the final state.

### Supporting but Insufficient Evidence by Itself

Examples include:

- code looks correct,
- worker says tests passed,
- no obvious error was seen,
- compilation alone for behavior-sensitive changes,
- a test suite unrelated to the modified behavior,
- a workaround appears to work once,
- a reviewer expresses confidence without evidence.

The PM MUST map important claims to evidence rather than collect checks with no relationship to the acceptance criteria.

---

## 6. Evidence Freshness

Verification applies to a specific state of the artifact.

If relevant code/configuration/artifacts change after a check, the PM MUST determine whether the evidence has become stale.

Affected checks MUST be rerun.

Examples:

- tests run before a subsequent logic change are not evidence for the final logic;
- a Terraform plan generated before configuration edits is stale;
- a rendered Helm manifest inspected before values change is stale;
- review of an old diff does not approve a materially changed final diff.

The PM should prefer evidence tied to a commit, branch head, artifact version, or clearly identified final state when practical.

---

## 7. G1 — Worker Self-Verification

Every change-producing worker verifies its own work before returning `PASS`.

The Task Packet defines required checks; the worker may add obvious targeted checks discovered during execution.

A worker `PASS` requires:

1. all acceptance criteria are believed satisfied;
2. required checks that can be executed were actually executed;
3. results are reported accurately;
4. the changed diff/artifact was inspected for accidental scope expansion;
5. material remaining uncertainty is absent or explicitly bounded.

If a required check cannot be run, the worker reports it explicitly. The PM decides whether this makes the result `PARTIAL`, `BLOCKED`, `FAILED`, or a candidate for verification with residual uncertainty.

Worker self-verification is necessary but never sufficient for delegated-task acceptance.

---

## 8. G2 — PM Independent Verification

After every delegated task eligible for acceptance, the PM independently checks the result.

The PM MUST NOT satisfy this gate by paraphrasing the Work Report.

At minimum the PM should inspect:

- the actual final change/artifact,
- acceptance criteria against the final state,
- worker evidence for plausibility and relevance,
- at least one direct verification path appropriate to the task.

### Low-Risk PM Verification

Normally sufficient:

- inspect the final diff/artifact,
- verify acceptance criteria,
- rerun or directly inspect one relevant deterministic check when appropriate.

### Medium-Risk PM Verification

Normally include:

- inspect the final diff and relevant surrounding context,
- map every material acceptance criterion to evidence,
- independently rerun targeted checks or equivalent validation,
- inspect likely regression boundaries,
- confirm required verification is fresh,
- confirm no authority/scope boundary was crossed.

### High-Risk PM Verification

Normally include:

- all medium-risk behavior,
- direct inspection of critical paths and failure modes,
- negative-path or rollback/recovery validation where relevant,
- broader integration/system evidence proportional to blast radius,
- explicit review of residual uncertainty,
- confirmation that destructive/security/production/human gates were preserved.

The PM may use different evidence from the worker. Independence means performing a real check, not necessarily duplicating every worker command.

---

## 9. Direct PM Execution

Lite tasks may be executed directly by the PM when delegation would add more overhead than value.

For direct PM work:

- the PM performs implementation self-verification;
- low-risk work does not require a second agent solely for ceremony;
- medium/high-risk work still requires an independent Reviewer before integration;
- the PM must not call its own implementation inspection "independent PM verification" when no worker boundary existed.

For medium/high direct execution, the Reviewer provides the independent second perspective.

---

## 10. G3 — Independent Review

Independent review is required for all `medium` and `high` risk work in V0.

The Reviewer should receive requirements, acceptance criteria, risk, relevant project constraints, and the actual final change/artifact.

On the first pass, avoid providing the Implementer's reasoning or confidence when direct inspection is possible.

### Medium-Risk Review

Use a focused review:

- requirement/result mismatch,
- correctness,
- likely regressions,
- verification adequacy,
- unnecessary complexity,
- relevant operational/security concerns.

The objective is not maximum commentary. It is an independent attempt to find material defects at reasonable cost.

### High-Risk Review

Use a deeper review:

- critical-path correctness,
- failure/rollback behavior,
- security and operational consequences,
- cross-component assumptions,
- data/state integrity where relevant,
- adequacy of negative-path verification,
- hidden blast radius,
- residual risks that would matter in production.

### Reviewer Verdict Handling

Canonical Reviewer verdicts are:

- `PASS` — review gate passes.
- `PASS_WITH_NOTES` — gate passes if notes are truly non-blocking.
- `FAIL` — integration is blocked until findings are resolved, accepted through an appropriate authority path, or the plan is changed.
- `INCONCLUSIVE` — integration is blocked because the reviewer could not reach a reliable verdict.

The orchestration layer may translate a `FAIL` into `FIX`, `REPLAN`, or `ESCALATE` depending on the finding. It must not invent separate Reviewer-return vocabularies.

### Re-review After Changes

When review causes implementation changes:

- medium risk: re-review the affected findings/change surface;
- high risk: Reviewer must inspect the final materially changed state before integration.

A review of a superseded diff is not a gate pass for the final diff.

---

## 11. Review Findings and Blocking Behavior

The Reviewer role uses finding severity:

- `CRITICAL`
- `HIGH`
- `MEDIUM`
- `LOW`

The Reviewer verdict, not raw finding count, is the canonical review-gate result.

Guidance:

- `CRITICAL` or `HIGH` should normally produce `FAIL`;
- `MEDIUM` should normally be resolved before integration unless there is a documented reason it is non-blocking for the current contract;
- `LOW` is normally advisory.

A finding cannot be dismissed merely because the implementation passes tests; evidence must address the failure scenario raised by the finding.

For high-risk work, accepting a material unresolved risk may itself require a human gate.

---

## 12. Failed Verification

If G1, G2, or G3 fails:

```text
failure evidence
    ↓
DIAGNOSE
    ↓
choose:
  FIX IN PLACE
  DEBUGGER
  REPLAN
  HUMAN GATE
    ↓
re-execute relevant gates
```

Do not repeatedly rerun the same failing action without a changed hypothesis or new evidence.

A fix invalidates affected prior evidence and affected review conclusions.

---

## 13. G4 — Integration Readiness

Before treating a working branch/task artifact as ready to integrate into `dev`, the PM must confirm:

- task acceptance criteria are satisfied;
- required worker verification completed;
- PM verification passed;
- required Reviewer gate passed;
- blocking findings are resolved;
- final diff/artifact is the one that was verified/reviewed;
- required repository/CI checks are passing or their absence is explicitly understood;
- scope is coherent and appropriate for integration;
- no known critical/high blocker remains;
- canonical state is updated enough to reflect the integration action.

A commit is not proof of correctness.

A PR is not proof of correctness.

A green CI status is not by itself proof that acceptance criteria are satisfied.

### Before Commit

Normal non-WIP commits should represent a coherent state that has at least passed relevant local/self checks.

The PM MAY create an explicitly temporary/WIP checkpoint commit when operationally useful, but must not treat that commit as verified or integration-ready.

### Before Opening a PR

A draft PR may be opened before all gates pass when it helps collaboration or CI.

A PR presented as ready for merge should have passed G1/G2 and any required G3 review, unless repository workflow intentionally performs the Reviewer gate inside the PR itself.

---

## 14. G5 — Post-Integration / System Verification

Merging verified tasks can still create integration failures.

After integration into `dev`, verification depth scales with risk and number of interacting changes.

### Low Risk

Post-integration re-verification may be omitted when integration cannot materially change behavior and branch-level evidence remains valid.

### Medium Risk

Run an appropriate integrated smoke/targeted check when the merged state, dependency interaction, or CI environment could differ materially from the working branch.

### High Risk

Run system/integration verification appropriate to the blast radius whenever feasible.

Examples:

- integrated test suite,
- rendered/deployed configuration validation,
- staging/runtime smoke test,
- infrastructure plan against the intended environment,
- critical-path behavior and failure-path validation.

If high-risk integrated behavior cannot be verified in an appropriate environment, record the residual uncertainty explicitly before any promotion decision.

---

## 15. Parallel Work and Aggregate Verification

Each parallel worker/task must pass its own required gates.

The PM must then verify the aggregate state because independently correct changes can conflict when combined.

Aggregate checks should address:

- overlapping assumptions,
- interface compatibility,
- merge conflict resolution,
- ordering/dependency behavior,
- shared configuration/state,
- system-level regressions.

Do not infer aggregate correctness from every worker individually returning `PASS`.

---

## 16. G6 — Main Promotion Readiness

Promotion to `main` has two separate requirements:

1. technical readiness,
2. explicit human approval.

Technical readiness means, where applicable:

- requested pre-promotion outcome is satisfied in `dev`;
- required task and aggregate gates passed;
- required CI/system checks are current;
- blocking review findings are closed;
- important residual risks are visible;
- release/deployment instructions or rollback expectations are known when relevant;
- the promotion diff is understood.

Only after technical readiness is established should the PM request/consume the explicit user approval required to merge to `main`.

The PM MUST NOT phrase pending human approval as if the work is fully released or deployed.

Human approval does not authorize unrelated changes or waive undisclosed failed verification.

---

## 17. Verification Gaps and Residual Risk

Some claims cannot be fully verified in the available environment.

When a gap exists, record:

- what could not be verified,
- why,
- what evidence is available instead,
- the plausible consequence if the assumption is wrong,
- the next best validation point,
- whether the residual risk crosses a human gate.

Do not convert environmental limitation into a fake `PASS`.

For low-risk work, a small bounded uncertainty may be acceptable when the acceptance contract is still convincingly satisfied.

For medium/high-risk work, material verification gaps normally keep the gate `INCONCLUSIVE` until resolved or explicitly handled through the appropriate risk/authority path.

---

## 18. Gate Waivers and Risk Acceptance

Required gates are not skipped for convenience.

A check may be `N/A` only when it genuinely does not apply.

A check that cannot be executed remains `NOT_RUN` or contributes to `INCONCLUSIVE`; it does not become `N/A`.

When a human with appropriate authority explicitly accepts a known residual risk:

- preserve the failed/unverified status accurately;
- record the accepted risk and approval reference where project state requires it;
- do not rewrite the underlying verification claim as `PASS`.

Risk acceptance and verification truth are separate concepts.

---

## 19. Domain-Specific Verification

This core policy is domain-neutral.

Skills and project conventions may add stronger domain gates, for example:

### Software

- unit/integration/e2e tests,
- lint/type/build,
- runtime behavior,
- compatibility checks.

### Infrastructure / DevOps

- syntax/static checks,
- Terraform plan,
- Helm render/lint,
- policy/security checks,
- dry-runs,
- deployment health,
- rollback readiness.

### Research / Analysis

- source quality,
- factual cross-checking,
- claim/source traceability,
- calculation reproduction,
- uncertainty disclosure.

### Documents / Artifacts

- requirement completeness,
- structural consistency,
- factual correctness,
- formatting/render inspection,
- final-file opening/validation.

Domain policy may strengthen this file but may not weaken global evidence or human-authority requirements without explicit user direction.

---

## 20. Verification Recording

Canonical project state should retain only compact verification truth.

Record, when material:

- claim/gate,
- status,
- concise evidence/reference,
- freshness/version when important,
- remaining uncertainty.

Do not paste complete logs into `STATE.md` or `HANDOFF.md`.

Verbose execution evidence remains in the worker/CI/tool context or external artifact; state keeps only what a replacement PM needs.

---

## 21. Definition of Done Under This Policy

A delegated task may be accepted as done only when:

- worker result is eligible for acceptance (`PASS` for execution work);
- acceptance criteria are satisfied;
- G1 worker self-verification passed;
- G2 PM independent verification passed;
- G3 independent review passed when risk is medium/high;
- required evidence is fresh for the final state;
- material residual uncertainty is resolved or explicitly handled;
- project state is updated as required.

A phase/project may be complete only when additionally:

- all required tasks are accepted;
- aggregate/integration verification is complete;
- no known blocking review/verification issue remains;
- human-gated actions are accurately distinguished from completed autonomous work.

---

## 22. Anti-Patterns

### Worker-Report Trust

```text
worker: tests pass
PM: accepted
```

Invalid. The PM must independently check.

### Test-Count Theater

Running many unrelated tests does not compensate for failing to test the changed behavior.

### Green-CI Absolutism

CI passing is evidence, not a complete correctness proof.

### Reviewer as Formatter

A Reviewer should search for material correctness/risk issues, not manufacture style comments to justify its existence.

### Stale Evidence

Do not cite checks against a state that materially changed afterward.

### Review of the Wrong Diff

A Reviewer PASS on an old revision does not approve later material changes.

### Human-Approval Laundering

Do not ask the user to "approve" an unverified implementation as a substitute for verification.

### Verification Dumping

Do not move raw logs into PM/project state merely to demonstrate thoroughness.

### Permanent High-Cost Verification

Do not run maximum-depth system checks on trivial work when a smaller deterministic check proves the same claim.

---

## 23. V0 Gate Matrix

| Risk | Worker/Self Verify | PM Verify | Independent Reviewer | Post-Integration |
| --- | --- | --- | --- | --- |
| Low | Required | Required for delegated work | Normally no | Only when integration can matter |
| Medium | Required | Required | Required | Targeted/integrated when relevant |
| High | Required | Required, deep | Required, deep | Strong system/integration evidence when feasible |

For direct PM execution, replace worker self-verification with PM self-verification; medium/high still require an independent Reviewer.

---

## 24. Testable Invariants for Future Evals

A compliant Methodology OS run should satisfy:

1. No delegated worker `PASS` is accepted without PM independent verification.
2. Medium/high-risk work reaches an independent Reviewer before integration.
3. Reviewer `FAIL` or `INCONCLUSIVE` blocks integration.
4. Verification claims identify evidence actually obtained.
5. Missing checks are never represented as passing.
6. Material changes invalidate affected stale evidence/reviews.
7. Integrated parallel work receives aggregate verification when interactions are plausible.
8. A green CI result is not treated as a substitute for acceptance-criteria verification.
9. Main promotion remains technically verified and separately human-gated.
10. Risk acceptance never rewrites an unverified fact into a verified one.

These invariants should become scenarios in the Methodology OS eval suite.