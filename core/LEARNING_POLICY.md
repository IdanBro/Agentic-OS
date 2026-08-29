# Methodology OS — Learning & Promotion Policy

This document defines how Methodology OS learns from completed work without silently rewriting its own global behavior.

The system may observe patterns, preserve evidence, propose experiments, create candidate improvements, and prepare non-canonical change proposals. A candidate becomes global Methodology OS behavior only after sufficient validation and explicit human promotion.

The Project Manager owns learning triage. The `methodology-retrospective` skill is the default procedure for extracting learning candidates from meaningful work.

---

## 1. Core Rule

> Learn from evidence, generalize cautiously, and promote globally only with explicit human approval.

Methodology OS learning means changing durable instructions, defaults, templates, skills, agents, evals, or workflow policy based on observed evidence.

It does **not** mean:

- changing model weights,
- treating conversation memory as training,
- silently mutating global policy,
- turning every failure into a permanent rule,
- optimizing one metric without considering regressions,
- copying project-specific behavior into the global OS without proving generality.

Project experience may create evidence. Evidence may create a candidate. A candidate is not yet policy.

---

## 2. Learning Layers

The system separates three kinds of learning.

### 2.1 Project-Specific Learning

Knowledge that is useful inside one repository, team, environment, or project but should not become a global Methodology OS rule.

Examples:

- this repository uses `make verify` before PRs;
- this project requires Terraform 1.9;
- a particular service has an unusual deployment dependency;
- this team always renders Helm charts with a specific values hierarchy;
- a local reviewer must inspect a regulated artifact.

Possible destinations:

- project `CLAUDE.md`;
- project/nested Skill;
- project documentation;
- repository test/check tooling;
- `DECISIONS.md` or another durable project artifact.

Project-specific learning MAY be applied autonomously when it is inside the accepted project scope and authority envelope. Material policy, architecture, security, cost, or scope consequences remain governed by `core/ESCALATION_POLICY.md`.

### 2.2 Candidate Global Learning

A potentially reusable improvement to Methodology OS that has not yet earned global promotion.

Examples:

- a Task Packet field repeatedly prevents a class of scope drift;
- medium-risk Reviewer prompts miss the same operational failure mode across projects;
- a routing default consistently overspends capability after ambiguity is removed;
- PM handoffs repeatedly omit one category of approval state;
- a skill-loading pattern produces measurable context waste across domains.

Candidate global learning MUST remain visibly non-canonical until promoted.

### 2.3 Promoted Global Learning

A candidate that has:

1. sufficient evidence for its consequence level;
2. a plausible causal explanation;
3. a bounded generalized rule/change;
4. an evaluation or verification plan;
5. an explicit human promotion decision;
6. implementation through the normal Git/quality-gate workflow.

Only this layer changes Methodology OS global behavior.

---

## 3. Learning Signal Sources

Useful signals include:

- repeated implementation or verification failures;
- Reviewer findings that expose a workflow blind spot;
- a human correction to the PM's workflow or authority behavior;
- repeated approval spam or under-escalation;
- context pollution or premature handoffs;
- worker scope drift caused by weak delegation;
- routing choices that cause avoidable retries or expensive over-capability;
- skills that are repeatedly loaded but unused;
- project knowledge that is repeatedly rediscovered;
- integration failures despite individually passing tasks;
- stale verification evidence being reused;
- successful workflow patterns that consistently improve quality or efficiency;
- future eval failures or regressions.

Not every signal deserves preservation.

A learning signal is valuable when understanding it may materially improve future:

- quality,
- reliability,
- token/context efficiency,
- elapsed time,
- autonomy,
- verification confidence,
- human interaction quality.

---

## 4. Observation Is Not Causation

The PM must distinguish what happened from why it happened.

Example:

```text
Observed:
Opus solved the debugging task after Sonnet failed.
```

Invalid immediate conclusion:

```text
Global rule:
Always use Opus for debugging.
```

Possible actual causes include:

- the first Task Packet omitted critical context;
- the second attempt had better reproduction evidence;
- Sonnet effort was too low;
- the first hypothesis was wrong;
- the problem genuinely required higher capability.

A candidate should state the causal hypothesis explicitly and identify alternative explanations when material.

Do not convert correlation into a global default merely because the later attempt succeeded.

---

## 5. Canonical Candidate Lifecycle

Global learning candidates use the following lifecycle:

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

A candidate may also become `DEFERRED` or `SUPERSEDED`.

### 5.1 OBSERVATION

A noteworthy event occurred, but no generalized change has been justified.

Most observations should die here.

### 5.2 CANDIDATE

There is a plausible reusable pattern and a proposed generalized improvement worth evaluating.

A candidate MUST identify:

- observed problem/opportunity;
- evidence;
- causal hypothesis;
- generalization boundary;
- smallest proposed change;
- expected benefit;
- possible regression/cost.

### 5.3 NEEDS_EVIDENCE

The candidate is plausible but current evidence is too weak, too project-specific, or too confounded to justify promotion.

Record what evidence would materially change confidence.

Do not create busywork merely to advance the status.

### 5.4 VALIDATING

The candidate is being tested through one or more of:

- another independent project occurrence;
- a controlled comparison;
- targeted retrospective evidence;
- synthetic or repository eval scenario;
- replay of a prior failure;
- benchmark/measurement when relevant;
- direct inspection of multiple historical cases.

### 5.5 READY_FOR_PROMOTION

Evidence is strong enough that the PM can recommend a bounded global change and describe its likely tradeoffs.

This status still does not authorize global policy modification.

### 5.6 APPROVED

The human authority explicitly approved promotion of the bounded candidate.

Approval applies only to the stated generalized change/envelope. Materially broader changes require a new promotion decision.

### 5.7 PROMOTED

The approved change has been implemented, passed required quality/eval gates, and integrated into the canonical Methodology OS development branch according to repository policy.

Promotion to `dev` and promotion to `main` remain separate authority events. Approval of the learning candidate does not automatically authorize a `main` merge.

### 5.8 REJECTED

The candidate should not be promoted because evidence, benefit, generalizability, complexity cost, or regression risk is insufficient.

Preserve rejected candidates only when future agents are reasonably likely to rediscover the same proposal and the rejection rationale has durable value.

### 5.9 DEFERRED

The candidate may be useful, but validating or implementing it is not currently worth the cost.

### 5.10 SUPERSEDED

A newer candidate or policy makes this candidate obsolete. Link the replacement where practical.

---

## 6. Evidence Strength and Generalizability

Do not use a fixed global rule such as "three projects are required" for every learning.

Evidence requirements should scale with:

- blast radius of the proposed rule;
- reversibility;
- how often the rule will execute;
- context/token cost if wrong;
- quality/security/authority consequences;
- confidence in the causal mechanism;
- diversity of evidence sources.

### Weak Evidence

Examples:

- one noisy project occurrence;
- subjective preference without outcome evidence;
- a successful retry where several variables changed;
- one worker's opinion;
- one unusual repository constraint.

Normally `NEEDS_EVIDENCE` or project-specific.

### Moderate Evidence

Examples:

- repeated pattern within one substantial project;
- same failure in multiple independent tasks;
- a reproducible synthetic scenario;
- one strong incident with clear root cause and narrow proposed fix;
- Reviewer/PM evidence showing an existing rule is internally inconsistent.

May justify validation or a low-blast-radius promotion recommendation.

### Strong Evidence

Examples:

- repeated independent project occurrences;
- reproducible eval failures resolved by the proposed change;
- controlled comparisons with materially better outcomes;
- multiple evidence sources pointing to the same causal pattern;
- a clear constitutional/policy inconsistency whose correction has low regression risk.

Strong evidence supports `READY_FOR_PROMOTION`, subject to change impact.

Avoid fake numeric precision. Use concise qualitative evidence strength with rationale unless a real measurement exists.

---

## 7. Generalization Test

Before proposing a global rule, ask:

1. Is the cause specific to this repository, domain, user preference, environment, or toolchain?
2. Would the proposed rule still make sense in a materially different project?
3. What projects should **not** follow the rule?
4. Is there a narrower condition that captures the successful pattern with less collateral cost?
5. Does the rule solve the cause or merely react to the symptom?
6. Could the same benefit be achieved as a project skill/check instead of global policy?

Every global candidate SHOULD define its **generalization boundary**.

Prefer:

```text
When a delegated infrastructure task can modify persistent production state,
require rollback/recovery evidence before integration.
```

Over:

```text
Terraform tasks need more verification.
```

The first captures a consequence. The second overfits a technology label.

---

## 8. Smallest Generalized Change

Prefer the smallest durable change that addresses the demonstrated failure mode.

Potential change surfaces, from narrower to broader, include:

1. example/reference;
2. template field/checklist;
3. Skill instruction;
4. agent role instruction;
5. routing default;
6. quality/authority/context policy;
7. orchestration behavior;
8. constitutional principle.

Do not change a higher layer when a lower layer solves the problem reliably.

Example:

```text
Problem:
Workers repeatedly omit rollback evidence in one deployment workflow.
```

Prefer a deployment/project Skill or verification template improvement before changing a constitutional principle.

---

## 9. Change Impact Classes

Promotion evidence should scale with the scope of the proposed OS change.

### L1 — Narrow Guidance

Examples:

- improve wording/example;
- add a template prompt/checklist item;
- refine one Skill procedure.

Expected promotion bar:

- clear evidence/problem;
- low regression risk;
- targeted verification/eval when practical;
- explicit human promotion.

### L2 — Role / Routing / Workflow Default

Examples:

- change Implementer behavior;
- change Reviewer default depth;
- change model/effort default;
- add a new recurring state artifact;
- change default skill-loading behavior.

Expected promotion bar:

- stronger generalizability evidence;
- alternative explanations considered;
- explicit regression analysis;
- targeted eval scenario(s);
- explicit human promotion.

### L3 — Global Policy / Constitution / Authority Gate

Examples:

- weaken or strengthen human escalation;
- change `main` authority;
- change mandatory verification requirements;
- modify constitutional principles;
- introduce a mandatory global workflow phase.

Expected promotion bar:

- strong evidence and clear causal rationale;
- broad regression/interaction analysis;
- multiple or high-quality evals;
- independent review appropriate to high impact;
- explicit human promotion.

Constitution changes should be rare.

---

## 10. Candidate Artifact

Use `templates/LEARNING_CANDIDATE.md` for global candidates when durable tracking is warranted.

A candidate artifact is not required for every retrospective observation.

Create one when:

- the proposed improvement may become global;
- evidence will accumulate across sessions/projects;
- validation requires follow-up;
- the user may later decide whether to promote it;
- a future PM needs to understand why the proposal exists.

Candidate artifacts should be concise and evidence-oriented.

The exact persistent location is an installation/runtime concern and may vary until Step 14. The schema, not the filesystem path, is canonical in V0.

---

## 11. Candidate Storage and Privacy

Global learning must not become a channel for leaking project-private information into the global OS.

When preserving evidence:

- abstract the causal pattern;
- use references rather than copying proprietary files/logs;
- never copy secrets, credentials, private data, or sensitive customer content;
- keep project-specific evidence in its original project when appropriate;
- include only the minimum evidence needed to evaluate the methodology claim.

A global candidate should be understandable without requiring confidential source content whenever possible.

If evidence cannot be safely globalized, record a sanitized summary and keep the detailed source project-local.

---

## 12. Validation Strategies

Choose the cheapest strategy that can meaningfully challenge the candidate.

### Cross-Project Evidence

Look for the same mechanism in independent projects/domains.

Useful for broad workflow defaults.

### Historical Replay

Apply the proposed rule to a known failure and determine whether it would have prevented or detected it earlier.

Useful but weaker than independent future evidence because hindsight may bias the test.

### Synthetic Eval Scenario

Construct a controlled scenario that distinguishes compliant from non-compliant behavior.

Examples:

- worker says `PASS` but PM receives no evidence;
- old staging approval is incorrectly reused for production;
- high-volume skill preload is selected despite no task relevance.

### A/B or Controlled Comparison

When practical, compare two workflow variants while holding important factors stable.

Useful for routing/context-efficiency claims.

### Counterexample Search

Actively search for situations where the proposed rule would be harmful or wasteful.

Every meaningful global candidate should include at least one plausible counterexample or state why none is known.

---

## 13. Evals as Promotion Evidence

Step 13 defines the full eval framework. This policy establishes the learning relationship now.

A candidate that changes observable agent behavior SHOULD define at least one eval expectation before promotion.

Examples:

```text
Candidate:
Do not preload domain skills into generic Implementers.

Eval expectation:
For a bounded non-domain-specific task, the PM chooses zero skills rather than preloading unrelated installed skills.
```

or:

```text
Candidate:
Approval must be target-specific.

Eval expectation:
A prior staging approval must not authorize production.
```

Promotion should prefer changes that can be falsified by a scenario over vague aspirational wording.

A change that cannot be meaningfully evaluated should state how its effect will be reviewed after promotion.

---

## 14. Human Promotion Gate

Global promotion is always human-gated under P14.

When a candidate reaches `READY_FOR_PROMOTION`, present:

1. **Candidate** — the generalized behavior change.
2. **Observed problem/opportunity** — what drove it.
3. **Evidence** — concise supporting evidence.
4. **Causal rationale** — why this change addresses the cause.
5. **Generalization boundary** — when it should and should not apply.
6. **Expected benefit** — quality/tokens/speed/reliability/autonomy.
7. **Regression risk** — what may become worse.
8. **Change surface** — policies/agents/skills/templates likely affected.
9. **Eval plan** — how the change will be challenged.
10. **Recommendation** — promote / keep validating / reject.

The user may:

- approve the candidate as proposed;
- approve a narrower variant;
- request more validation;
- reject it;
- defer it.

Do not infer promotion approval from enthusiasm about the retrospective itself.

---

## 15. Draft Proposals Before Approval

The PM MAY prepare a non-canonical proposal before promotion approval when doing so makes the decision easier to evaluate.

Allowed examples:

- proposed wording;
- candidate artifact;
- eval scenario draft;
- unmerged feature branch;
- draft PR that is clearly labeled as a proposal.

Before human promotion, the proposal MUST NOT be treated as active global behavior or integrated into the canonical Methodology OS `dev` branch.

Creating a draft is not promotion.

---

## 16. Promotion Implementation Workflow

After explicit promotion approval:

```text
approved candidate
      ↓
create/update feature branch
      ↓
implement smallest approved change
      ↓
add/update eval scenarios
      ↓
self-verify
      ↓
PM independent verification
      ↓
Reviewer according to change risk
      ↓
PR → dev
      ↓
merge to dev when gates pass
      ↓
mark candidate PROMOTED
```

If implementation reveals that the approved change must materially expand beyond the approval envelope, return to the human promotion gate.

Promotion approval is not permission to rewrite adjacent policy opportunistically.

`main` promotion remains separately human-gated by `core/ESCALATION_POLICY.md`.

---

## 17. Post-Promotion Observation

A promoted rule is still a hypothesis about future usefulness.

After promotion, watch for:

- eval regressions;
- new failure modes;
- excessive ceremony/context cost;
- reduced autonomy;
- quality improvement or degradation;
- repeated exceptions;
- domain conflicts.

When new evidence challenges a promoted rule:

- create a new candidate or regression observation;
- do not silently mutate the rule;
- preserve supersession/reversion rationale when durable.

Global learning is iterative but remains governed.

---

## 18. Reversion and Supersession

A promoted learning may be reverted or narrowed when evidence shows net harm.

Reversion should identify:

- which behavior regressed;
- evidence of the regression;
- whether the original causal hypothesis was wrong or over-generalized;
- whether a narrower replacement exists;
- eval changes required to prevent recurrence.

Do not preserve a bad rule merely because it was previously approved.

A material global reversion is itself a global policy change and requires appropriate human promotion/authority.

---

## 19. Project Learning vs Global Learning Examples

### Example A — Project Command

Observation:

```text
Every worker in Repository X independently discovers `make verify`.
```

Correct action:

```text
Project-specific learning
→ project CLAUDE.md or project skill
```

Incorrect action:

```text
Global Methodology OS rule:
all projects must run make verify
```

### Example B — Scope Drift

Observation:

```text
Across several projects, workers expand task scope when Task Packets list paths without explaining whether they are strict boundaries.
```

Possible global candidate:

```text
Task Packets should explicitly distinguish starting references from hard allowlists.
```

This is broad enough to validate across domains.

### Example C — Routing

Observation:

```text
One difficult Terraform task needed Opus.
```

Correct status:

```text
observation / needs evidence
```

Not:

```text
Terraform → Opus default
```

### Example D — Reviewer Catch

Observation:

```text
A Reviewer catches a serious bug missed by PM verification.
```

First question:

```text
Was the root cause:
- missing acceptance criteria?
- weak PM verification?
- missing domain skill?
- genuinely independent review value?
```

Do not automatically add another Reviewer globally.

---

## 20. Human Corrections as Learning Signals

A user correction is high-value evidence about the current interaction but not automatically a universal rule.

Classify the correction:

### Explicit Global Preference / Policy

Example:

```text
Never merge to main without asking me.
```

If the user explicitly intends this as global Methodology OS behavior, it may be treated as a candidate/promotion direction subject to conflict checks and implementation workflow.

### Project-Specific Direction

Example:

```text
For this repo, don't change the database schema.
```

Keep project-local.

### One-Off Choice

Example:

```text
Use option B this time.
```

Do not learn a durable rule unless the user indicates a broader preference or repeated evidence justifies one.

---

## 21. Do Not Optimize One Metric in Isolation

Methodology OS optimizes a multi-objective system.

A learning that saves tokens but materially increases retries or defects is not an improvement.

A learning that increases quality slightly but doubles ceremony on trivial work may be net harmful.

Evaluate candidates against at least the dimensions they materially affect:

- professional quality;
- reliability;
- token/context usage;
- elapsed time;
- autonomy;
- human interruption burden;
- maintainability/complexity.

When tradeoffs are uncertain, make them explicit rather than hiding them behind a single score.

---

## 22. Retrospective Trigger Policy

Do not run a full retrospective after every task.

Run or consider `methodology-retrospective` when:

- a meaningful phase/project completes;
- a costly failure occurred;
- repeated retries or replans happened;
- Reviewer/verification caught a surprising material issue;
- context/handoff behavior was notably poor or notably effective;
- model/effort/skill routing created obvious over/under-spend;
- the user asks what should be learned;
- a future eval detects a regression.

For routine successful work with no meaningful signal, skip the retrospective.

Learning ceremony must justify itself under P15.

---

## 23. Retrospective Output Contract

A useful retrospective should separate:

1. **Repeat locally** — successful project-specific practices.
2. **Fix locally** — repository/process improvements that belong only to this project.
3. **Global candidates** — reusable proposals requiring validation/promotion.
4. **Noise** — observations not worth preserving.
5. **Evidence gaps** — what would be needed to strengthen a candidate.

Do not create global candidate artifacts for `Noise`.

Do not promote a candidate merely because it appears in a retrospective.

---

## 24. Candidate Deduplication

Before creating a new global candidate, check whether the same underlying proposal already exists when a candidate registry/reference is available.

If similar:

- add new evidence to the existing candidate;
- refine the generalization boundary;
- link a related but distinct candidate;
- avoid parallel near-duplicate rules.

Deduplicate by causal mechanism, not by identical wording.

---

## 25. Learning and Context Hygiene

Learning artifacts must not become a transcript archive.

Keep:

- causal pattern;
- evidence references;
- decision-relevant observations;
- proposed change;
- validation state;
- promotion state.

Do not keep:

- complete worker transcripts;
- raw logs that can be referenced;
- full chat histories;
- every failed command;
- generic praise/criticism without actionable mechanism.

A future PM should be able to evaluate the candidate without inheriting the original session context.

---

## 26. Learning and Authority

Learning does not grant authority.

A retrospective may recommend:

```text
"production rollback should be automated"
```

but it cannot perform or globally require consequential production actions outside the normal escalation process.

A candidate may recommend changing `ESCALATION_POLICY.md`, but that is an L3 global change and requires explicit human promotion plus appropriate verification/review.

The learning system is subordinate to:

- platform/safety rules;
- the Constitution;
- human authority;
- current project scope;
- quality gates.

---

## 27. Anti-Patterns

### One-Incident Constitution

One failure occurs and the OS gains a permanent mandatory rule.

Invalid unless the incident exposes a clear invariant-level defect with sufficient evidence and human promotion.

### Technology Label Learning

```text
Terraform was hard
→ Terraform always needs Opus
```

Invalid. Learn the causal task characteristics.

### Success Bias

A later attempt succeeded, therefore every difference in that attempt was beneficial.

Invalid. Isolate the plausible cause.

### Retrospective Theater

Producing a long lesson list after every routine task.

Invalid. Preserve only actionable, reusable signal.

### Silent Global Mutation

A retrospective directly edits global agents/policies and merges them into canonical `dev` without human promotion.

Invalid.

### Candidate Graveyard

Recording hundreds of weak candidates that nobody will validate.

Invalid. Reject/noise-filter aggressively.

### Metric Tunnel Vision

Promoting a token-saving rule while ignoring higher retry/defect cost.

Invalid.

### Confidentiality Leakage

Copying project-private code/logs/data into a global learning artifact.

Invalid.

### Policy Accretion

Every learning adds another permanent rule rather than simplifying or replacing an existing one.

Invalid. Prefer simplification, refinement, or supersession when possible.

---

## 28. V0 Learning Decision Matrix

| Signal | Default Action |
| --- | --- |
| Routine successful task, no unusual signal | No retrospective |
| Local repo convention repeatedly rediscovered | Project-specific learning |
| One noisy failure with unclear cause | Observation only |
| Repeated project-local failure with clear local cause | Project fix/skill/check |
| Plausible reusable pattern, weak evidence | Global candidate → `NEEDS_EVIDENCE` |
| Reproducible cross-project/eval pattern | Candidate → `VALIDATING` / `READY_FOR_PROMOTION` |
| Candidate ready, low/medium impact | Human promotion gate |
| Candidate changes authority/constitution/global mandatory gates | High-bar L3 human promotion gate |
| Human approves bounded global change | Implement + eval + verify + PR→`dev` |
| Candidate rejected/noisy | Reject/drop; preserve only if future value exists |
| Promoted rule later regresses | New regression candidate / reversion proposal |

---

## 29. Testable Invariants for Future Evals

A compliant Methodology OS learning system should satisfy:

1. One project failure does not automatically become a global rule.
2. Project-specific conventions are routed locally rather than globalized by default.
3. Every global candidate states evidence, causal hypothesis, generalization boundary, benefit, and regression risk.
4. Candidate status is distinct from active global policy.
5. Global promotion requires explicit human approval.
6. A draft branch/PR is not treated as active policy before promotion.
7. Promotion approval does not authorize unrelated broader OS changes.
8. Observable behavior changes define an eval or validation expectation when practical.
9. Candidate evidence does not copy secrets/private project content into the global OS.
10. Human corrections are classified as global, project-specific, or one-off rather than blindly universalized.
11. Learning does not weaken quality or authority gates silently.
12. A promoted rule can be challenged, narrowed, superseded, or reverted when later evidence shows harm.
13. Retrospectives are skipped when there is no meaningful reusable signal.
14. Candidate duplication is reduced by merging evidence around the same causal mechanism.
15. Constitution-level changes have a materially higher promotion bar than wording/template refinements.

These invariants should become scenarios in the Step 13 eval suite.
