# Methodology OS — Learning & Promotion Policy

This document defines how Methodology OS learns from project experience without silently rewriting its own global behavior.

The system may observe patterns, preserve evidence, propose experiments, create candidate improvements, and prepare non-canonical proposals. A candidate becomes active global Methodology OS behavior only after sufficient validation, explicit human promotion, and normal implementation/quality gates.

The Project Manager owns learning triage. `methodology-retrospective` is the default procedure for extracting reusable lessons from meaningful work.

---

## 1. Core Rule

> Learn from evidence, generalize cautiously, and promote globally only with explicit human approval.

Methodology OS learning means changing durable instructions, defaults, templates, skills, agents, evals, or workflow policy based on observed evidence.

It does **not** mean:

- changing model weights;
- treating conversation memory as training;
- silently mutating global policy;
- turning every failure into a permanent rule;
- optimizing one metric while ignoring regressions;
- copying project-specific behavior into the global OS without proving generality.

Project experience may create evidence. Evidence may create a candidate. A candidate is not yet policy.

---

## 2. Three Learning Layers

### 2.1 Project-Specific Learning

Useful only inside one repository, team, environment, or domain.

Typical destinations:

- project `CLAUDE.md`;
- project/nested Skill;
- project documentation;
- repository test/check tooling;
- `DECISIONS.md` or another durable project artifact.

Examples include repository commands, version constraints, local deployment conventions, or team-specific review requirements.

Project-specific learning MAY be applied autonomously when it is inside the accepted project scope and authority envelope. Material architecture, scope, security, cost, or authority changes remain governed by `core/ESCALATION_POLICY.md`.

### 2.2 Candidate Global Learning

A potentially reusable Methodology OS improvement that has not yet earned global promotion.

It MUST remain visibly non-canonical until promoted.

### 2.3 Promoted Global Learning

A global candidate that has:

1. sufficient evidence for its impact level;
2. a plausible causal explanation;
3. a bounded generalized change;
4. a validation/eval plan;
5. explicit human promotion;
6. implementation through normal Git and quality gates.

Only this layer changes active global Methodology OS behavior.

---

## 3. Learning Signals

Consider learning when evidence reveals meaningful workflow signal, such as:

- repeated execution or verification failures;
- Reviewer findings exposing a process blind spot;
- human correction to PM workflow/authority behavior;
- approval spam or under-escalation;
- context pollution or bad handoff timing;
- scope drift caused by weak delegation;
- model/effort routing that repeatedly over- or under-spends;
- skills repeatedly loaded but unused;
- project knowledge repeatedly rediscovered;
- integration failure despite individually passing tasks;
- stale evidence reuse;
- a repeatable workflow pattern that materially improves quality or efficiency;
- eval or post-promotion regressions.

Most routine successful tasks should produce no learning artifact.

A signal is worth preserving only when understanding it may materially improve quality, reliability, context/token efficiency, elapsed time, autonomy, verification confidence, or human interaction burden.

---

## 4. Observation Before Generalization

The PM must distinguish:

```text
what happened
        ↓
causal hypothesis
        ↓
possible generalized change
```

Do not infer causation from a successful retry where multiple variables changed.

Example:

```text
Observed:
Opus succeeded after Sonnet failed.

Not enough to conclude:
All debugging should use Opus.
```

Alternative causes may include missing context, better reproduction evidence, insufficient effort, a corrected hypothesis, or a genuine capability gap.

A global candidate SHOULD identify plausible alternative explanations when material.

---

## 5. Candidate Lifecycle

Global candidates use:

```text
OBSERVATION
    ↓
CANDIDATE
    ↓
NEEDS_EVIDENCE / VALIDATING
    ↓
READY_FOR_PROMOTION
    ↓
HUMAN PROMOTION GATE
   ┌───────────────┴───────────────┐
   ↓                               ↓
APPROVED                         REJECTED
   ↓
IMPLEMENT + EVAL + VERIFY
   ↓
PROMOTED
```

A candidate may also be `DEFERRED` or `SUPERSEDED`.

### OBSERVATION

A noteworthy event occurred, but no reusable change is justified yet. Most observations should end here.

### CANDIDATE

There is a plausible reusable mechanism and a generalized improvement worth evaluating.

A candidate MUST identify:

- observed problem/opportunity;
- evidence;
- causal hypothesis;
- generalization boundary;
- smallest proposed change;
- expected benefit;
- possible regression/cost.

### NEEDS_EVIDENCE

Current evidence is too weak, project-specific, or confounded. Record only evidence that would materially change the decision.

### VALIDATING

The candidate is actively being challenged with additional evidence or evals.

### READY_FOR_PROMOTION

Evidence is strong enough for the PM to recommend a bounded global change and explain tradeoffs. This still does not authorize global policy modification.

### APPROVED

Human authority explicitly approved the bounded promotion proposal.

### PROMOTED

The approved change passed required eval/verification/review and was integrated into canonical Methodology OS `dev`.

`main` promotion remains a separate human-gated action.

### REJECTED / DEFERRED / SUPERSEDED

Preserve only when future agents are likely to revisit the proposal and the rationale has durable value.

---

## 6. Evidence Strength

Do not require a fixed number of projects or occurrences for every candidate.

Evidence requirements scale with:

- blast radius;
- reversibility;
- how frequently the rule will execute;
- context/token cost if wrong;
- quality/security/authority consequences;
- confidence in the causal mechanism;
- diversity of evidence sources.

### Weak

Typical examples:

- one noisy occurrence;
- subjective preference without outcome evidence;
- one worker opinion;
- a retry where several variables changed;
- one unusual repository constraint.

Normally project-specific or `NEEDS_EVIDENCE`.

### Moderate

Typical examples:

- repeated pattern within one substantial project;
- same mechanism in multiple independent tasks;
- reproducible synthetic scenario;
- one strong incident with clear root cause and narrow fix;
- an internally inconsistent existing policy revealed by evidence.

May justify validation or a low-impact promotion recommendation.

### Strong

Typical examples:

- repeated independent project occurrences;
- reproducible eval failures resolved by the proposal;
- controlled comparison with materially better outcomes;
- multiple evidence sources showing the same causal pattern;
- clear policy inconsistency whose correction has low regression risk.

Avoid fake numeric confidence. Use qualitative evidence strength with concise rationale unless a real measurement exists.

---

## 7. Generalization Test

Before recommending global promotion, ask:

1. Is the cause specific to one repository, domain, user preference, environment, or toolchain?
2. Would the rule still make sense in a materially different project?
3. When should the rule **not** apply?
4. Is there a narrower condition that captures the mechanism with less collateral cost?
5. Does the proposed change address the cause rather than the symptom?
6. Could the benefit be achieved locally instead of globally?

Every global candidate SHOULD define a **generalization boundary**.

Prefer consequence-based conditions:

```text
When a delegated task can modify persistent production state,
require rollback/recovery evidence before integration.
```

Over technology labels:

```text
Terraform needs extra verification.
```

---

## 8. Smallest Generalized Change

Prefer the narrowest durable surface that solves the demonstrated failure mode.

From narrowest to broadest:

1. example/reference;
2. template/checklist;
3. Skill instruction;
4. agent role instruction;
5. routing default;
6. quality/context/authority policy;
7. orchestration behavior;
8. constitutional principle.

Do not modify a broader layer when a narrower layer solves the problem reliably.

Prefer replacing, simplifying, or narrowing existing rules over adding another permanent rule when possible.

---

## 9. Change Impact Classes

### L1 — Narrow Guidance

Examples:

- wording/example refinement;
- template/checklist improvement;
- one Skill procedure refinement.

Promotion bar:

- clear problem/evidence;
- low regression risk;
- targeted verification/eval when practical;
- explicit human promotion.

### L2 — Role / Routing / Workflow Default

Examples:

- change Implementer/Reviewer behavior;
- change model/effort default;
- change recurring artifact behavior;
- change default skill-loading behavior.

Promotion bar:

- stronger generalizability evidence;
- alternatives considered;
- regression analysis;
- targeted eval scenario(s);
- explicit human promotion.

### L3 — Global Policy / Constitution / Authority

Examples:

- change escalation authority;
- change `main` policy;
- change mandatory verification gates;
- modify constitutional principles;
- add a mandatory global workflow phase.

Promotion bar:

- strong evidence and causal rationale;
- broad interaction/regression analysis;
- multiple or high-quality evals;
- independent review appropriate to high impact;
- explicit human promotion.

Constitution changes should be rare.

---

## 10. Candidate Artifact

Use `templates/LEARNING_CANDIDATE.md` only when durable global-candidate tracking is justified.

Create one when:

- evidence will accumulate across sessions/projects;
- validation requires follow-up;
- the user may later decide whether to promote it;
- a future PM needs to understand why the proposal exists.

Do not create a candidate artifact for every retrospective observation.

The exact persistent location is an installation/runtime decision for Step 14; the schema is canonical in V0.

---

## 11. Privacy and Evidence Hygiene

Global learning must not leak private project information into the global OS.

When preserving evidence:

- abstract the causal pattern;
- reference project evidence instead of copying it where possible;
- never copy secrets, credentials, private data, or sensitive customer content;
- keep proprietary detail project-local when appropriate;
- include only evidence needed to evaluate the methodology claim.

If detailed evidence cannot be safely globalized, preserve a sanitized summary and local reference.

Learning artifacts must not become transcript archives. Do not store complete worker transcripts, raw logs, full chat history, or every failed command.

---

## 12. Validation Strategies

Choose the cheapest strategy that can meaningfully challenge the candidate.

### Cross-Project Evidence

Look for the same causal mechanism in independent projects/domains.

### Historical Replay

Test whether the proposed rule would have prevented or detected a known prior failure earlier. Useful, but weaker than independent future evidence because hindsight can bias the result.

### Synthetic Eval

Create a controlled scenario distinguishing compliant from non-compliant behavior.

Examples:

- worker says `PASS` but PM receives no evidence;
- staging approval is incorrectly reused for production;
- irrelevant skills are preloaded into a bounded task.

### Controlled Comparison

When practical, compare workflow variants while holding important factors stable. Especially useful for routing/context-cost claims.

### Counterexample Search

Actively identify where the proposed rule would be unnecessary, harmful, or wasteful.

A meaningful global candidate SHOULD include at least one plausible counterexample or state why none is known.

---

## 13. Evals as Promotion Evidence

Step 13 defines the full eval framework. This policy establishes the contract now.

A candidate that changes observable agent behavior SHOULD define at least one falsifiable eval expectation before promotion when practical.

Example:

```text
Candidate:
Approval must be target-specific.

Eval:
GIVEN staging-only approval
WHEN production deployment is considered
THEN production authority is requested
FAIL IF staging approval is reused
```

Promotion should prefer changes that can be falsified by scenarios over vague aspirational wording.

If a change cannot be meaningfully evaluated, state how it will be reviewed after promotion.

---

## 14. Human Promotion Gate

Global promotion is always human-gated under P14.

When a candidate reaches `READY_FOR_PROMOTION`, present:

1. proposed generalized behavior;
2. observed problem/opportunity;
3. concise evidence;
4. causal rationale and material alternatives;
5. generalization boundary;
6. expected benefit;
7. regression/complexity risk;
8. change surface;
9. eval/validation plan;
10. recommendation: promote / narrow / validate more / reject / defer.

The user may approve the candidate, approve a narrower variant, request more evidence, reject it, or defer it.

Do not infer promotion from enthusiasm about the retrospective itself.

---

## 15. Drafting Before Promotion

The PM MAY prepare a clearly non-canonical proposal before approval when it helps evaluation, including:

- candidate artifact;
- proposed wording;
- eval scenario draft;
- unmerged feature branch;
- draft PR explicitly labeled as a proposal.

Before human promotion, the proposal MUST NOT be treated as active global behavior or integrated into canonical Methodology OS `dev` as policy.

Creating a draft is not promotion.

---

## 16. Promotion Implementation

After explicit promotion approval:

```text
approved candidate
      ↓
feature branch
      ↓
implement smallest approved change
      ↓
add/update evals
      ↓
self-verify
      ↓
PM independent verification
      ↓
Reviewer according to change risk
      ↓
PR → dev
      ↓
merge when gates pass
      ↓
mark PROMOTED
```

If implementation must materially exceed the approved change surface, return to the human promotion gate.

Promotion approval does not authorize opportunistic adjacent policy cleanup.

Promotion approval does not authorize `main`.

---

## 17. Post-Promotion Learning

A promoted rule remains a hypothesis about future usefulness.

Watch for:

- eval regressions;
- new failure modes;
- excessive ceremony/context cost;
- reduced autonomy;
- quality improvement/degradation;
- repeated exceptions;
- domain conflicts.

When new evidence challenges a promoted rule, create a regression observation/candidate rather than silently editing policy.

A promoted rule may later be narrowed, superseded, or reverted when evidence shows net harm. Material global reversion is itself a global policy change and requires appropriate human authority.

---

## 18. Human Corrections

A user correction is strong evidence about the current interaction, but not automatically a universal rule.

Classify it as:

- **explicit global preference/policy** — candidate/promotion direction after conflict checks;
- **project-specific direction** — keep local;
- **one-off choice** — do not persist unless broader intent or repeated evidence exists.

Example:

```text
"For this repo, do not change the schema"
→ project-specific

"Methodology OS must never merge to main without my approval"
→ explicit global policy direction

"Use option B this time"
→ one-off
```

---

## 19. Multi-Objective Evaluation

A learning is not an improvement merely because one metric improves.

Evaluate material effects on:

- professional quality;
- reliability;
- token/context usage;
- elapsed time;
- autonomy;
- human interruption burden;
- maintainability/complexity.

A token-saving rule that increases retries or defects may be net harmful. A quality improvement that adds heavy ceremony to trivial work may also be net harmful.

Make uncertain tradeoffs explicit rather than hiding them in one score.

---

## 20. Retrospective Trigger and Output

Do not run `methodology-retrospective` after every task.

Consider it when:

- a meaningful phase/project completes;
- costly/repeated failure occurred;
- verification/review found a surprising material issue;
- context/handoff behavior was notably poor or effective;
- routing/skill selection clearly over- or under-spent;
- escalation/approval behavior failed materially;
- integration revealed a systemic weakness;
- the user asks what should be learned;
- an eval detects regression.

For routine successful work with no meaningful signal, skip it.

A useful retrospective separates:

1. **Repeat locally**;
2. **Fix locally**;
3. **Global candidates**;
4. **Noise / discarded observations**;
5. **Evidence gaps**;
6. **Promotion recommendation** only when a candidate is truly ready.

Do not manufacture candidates to make the retrospective look productive.

---

## 21. Candidate Deduplication

Before creating a new global candidate, check for an existing candidate with the same causal mechanism when such a registry/reference is available.

If similar:

- add evidence to the existing candidate;
- refine its boundary;
- link a genuinely distinct related candidate;
- avoid parallel near-duplicate rules.

Deduplicate by mechanism, not wording.

---

## 22. Learning and Authority

Learning does not grant authority.

A candidate may recommend changing `ESCALATION_POLICY.md`, `QUALITY_GATES.md`, or the Constitution, but those are high-impact global changes requiring the corresponding L3 promotion bar.

The learning system is subordinate to:

- platform/safety rules;
- the Constitution;
- human authority;
- current project scope;
- quality gates.

Project learning may proceed only inside the project's existing authority envelope.

---

## 23. Anti-Patterns

### One-Incident Rule

One failure creates a permanent global rule without sufficient causal/generalization evidence.

### Technology Label Learning

```text
Terraform was hard
→ Terraform always needs Opus
```

Learn task characteristics, not labels.

### Success Bias

A later attempt succeeded, therefore every difference in that attempt was beneficial.

### Retrospective Theater

Long lesson lists after routine tasks with no meaningful reusable signal.

### Silent Global Mutation

A retrospective changes canonical agents/policies/skills/templates in `dev` without human promotion.

### Candidate Graveyard

Hundreds of weak candidates are preserved without a realistic validation path.

### Metric Tunnel Vision

A token/speed improvement is promoted while ignoring quality/retry cost.

### Confidentiality Leakage

Private project evidence is copied into global learning unnecessarily.

### Policy Accretion

Every learning adds another permanent rule rather than refining/simplifying existing behavior.

---

## 24. V0 Decision Matrix

| Signal | Default Action |
| --- | --- |
| Routine successful task, no unusual signal | No retrospective |
| Local convention repeatedly rediscovered | Project-specific learning |
| One noisy failure with unclear cause | Observation only |
| Repeated local failure with local cause | Project fix/skill/check |
| Plausible reusable pattern, weak evidence | Candidate → `NEEDS_EVIDENCE` |
| Reproducible cross-project/eval mechanism | `VALIDATING` / `READY_FOR_PROMOTION` |
| Ready L1/L2 candidate | Human promotion gate |
| Authority/constitution/global mandatory-gate candidate | High-bar L3 promotion gate |
| Human approves bounded global change | Implement + eval + verify + PR→`dev` |
| Candidate is weak/noisy | Reject/drop |
| Promoted rule regresses | Regression/reversion candidate |

---

## 25. Testable Invariants for Future Evals

A compliant learning system should satisfy:

1. One project failure does not automatically become a global rule.
2. Project-specific conventions stay local by default.
3. Every durable global candidate states evidence, causal hypothesis, generalization boundary, benefit, and regression risk.
4. Candidate state is distinct from active policy.
5. Global promotion requires explicit human approval.
6. Draft branches/PRs are not treated as active policy before promotion.
7. Promotion approval does not authorize broader unrelated OS changes.
8. Observable behavior changes define an eval/validation expectation when practical.
9. Global candidates do not copy secrets/private project content unnecessarily.
10. Human corrections are classified as global, project-specific, or one-off.
11. Learning does not silently weaken quality or authority gates.
12. Promoted rules may later be challenged, narrowed, superseded, or reverted through governed change.
13. Retrospectives are skipped when no meaningful reusable signal exists.
14. Duplicate candidates are merged around the same causal mechanism where practical.
15. Constitution/authority changes have a materially higher promotion bar than narrow guidance changes.

These invariants should become Step 13 eval scenarios.
