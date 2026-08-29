---
name: methodology-retrospective
description: Review a meaningful completed Methodology OS phase or project for reusable workflow lessons, routing/context/verification mistakes, and candidate improvements. Use after a substantial milestone or meaningful failure signal. Produce project improvements or learning candidates only; never silently promote global OS policy.
---

# Methodology Retrospective

Extract useful learning from completed work without turning one experience into a global rule.

Follow `core/LEARNING_POLICY.md` for learning classification, validation, candidate lifecycle, privacy, and promotion requirements.

## When to Use

Use after:

- a meaningful project or major phase completes;
- a costly failure exposes a workflow weakness;
- repeated retries or context pollution suggest a process issue;
- a routing choice clearly over- or under-spent capability;
- a verification/review gate caught an important unexpected defect;
- approval spam or under-escalation exposed an authority problem;
- an integration failure reveals cross-task weakness;
- the user asks what the OS should learn from the work;
- an eval or post-promotion observation exposes a regression.

Do not run a full retrospective after every trivial or routine successful task.

## Inputs

Prefer evidence from:

- `PROJECT_BRIEF.md`;
- `PLAN.md` and meaningful replans;
- final/current `STATE.md`;
- relevant `DECISIONS.md` entries;
- Task Packets and compact Work Reports when useful;
- verification/review outcomes;
- Git/PR evidence;
- meaningful failure/debug evidence;
- existing learning candidates when checking for duplicate causal patterns.

Do not reread complete chat history unless a specific missing fact cannot be recovered from durable artifacts.

Do not copy private project evidence into global learning artifacts when a sanitized reference/summary is sufficient.

## Review Dimensions

### 1. Outcome Quality

Ask:

- Did the final result satisfy the requested outcome?
- Were meaningful defects found late that should have been found earlier?
- Did any process shortcut materially lower quality?
- Did any process step add cost without improving confidence?

### 2. Planning

Ask:

- Was planning depth proportional?
- Were task boundaries coherent?
- Were dependencies discovered early enough?
- Did the plan prescribe unnecessary implementation detail?
- Did replanning happen when assumptions changed, or too late?

### 3. Delegation

Ask:

- Were tasks bounded enough?
- Did workers receive minimum sufficient context?
- Was work delegated when PM execution would have been cheaper, or kept in PM when isolation would have helped?
- Did workers drift scope?
- Were Task Packets missing acceptance, verification, authority, or relevant-skill information?

### 4. Model / Effort Routing

Ask:

- Did the first well-prepared route have enough capability?
- Was expensive capability used after ambiguity had already been removed?
- Did retries come from a capability gap or from bad context/decomposition/environment?
- Could a later phase have downshifted safely?

Do not infer a routing rule from one noisy example without supporting evidence.

### 5. Skill Selection

Ask:

- Did a useful skill prevent rediscovery or inconsistency?
- Was a skill loaded but unused?
- Was important project/domain knowledge repeatedly rediscovered that may deserve a project skill?
- Did skill overlap or naming create confusion?
- Would static preload have helped enough to justify recurring context cost?

### 6. Context Health

Ask:

- Did the PM retain disposable logs/search output?
- Did workers return compact evidence or transcript dumps?
- Was canonical state sufficient for continuation?
- Was a handoff created too late or unnecessarily early?
- Did loaded skills/CLAUDE.md content materially pollute context?

### 7. Verification

Ask:

- Did worker self-verification test the changed behavior?
- Did PM independent verification add real evidence?
- Did Reviewer depth match risk?
- Was stale evidence reused after material changes?
- Did integration/system verification catch cross-task issues?
- Were any checks run mainly for theater rather than claim coverage?

### 8. Human Escalation

Ask:

- Did the PM interrupt the user for routine decisions?
- Did a consequential decision proceed without a required gate?
- Was an approval stretched beyond its target/scope/freshness?
- Were options/tradeoffs clear when escalation happened?
- Was risk acceptance kept separate from verification truth?

### 9. Git / Integration

Ask:

- Were branches and commits coherent?
- Did workers accidentally take PM integration authority?
- Did parallel work create avoidable conflicts?
- Was `dev` verified after meaningful integration?
- Was `main` kept human-gated?

## Classify Each Observation

For each meaningful observation, classify it as one of:

### Project-Specific

Useful only to the current repository/team/domain.

Possible action:

- project skill;
- project `CLAUDE.md` fact;
- project documentation;
- repository test/check improvement;
- project decision/state update.

Project-local changes may be applied when they are inside the current project authority and scope.

### Candidate Global Learning

Potentially reusable across Methodology OS projects, but not yet global policy.

If durable tracking is warranted, use `templates/LEARNING_CANDIDATE.md`.

### Noise / One-Off

Interesting but insufficiently generalizable or actionable. Do not preserve it merely because it happened.

Most routine observations should end here.

## Global Candidate Triage

For a plausible global candidate, determine:

1. **Observation** — what actually happened?
2. **Causal hypothesis** — why did it happen?
3. **Alternative explanations** — what else could explain it?
4. **Current OS behavior** — which rule/default is implicated?
5. **Smallest generalized change** — what narrow change addresses the cause?
6. **Generalization boundary** — when should and should not it apply?
7. **Expected benefit** — which quality/cost/autonomy dimensions improve?
8. **Regression risk** — what might become worse?
9. **Evidence strength** — weak / moderate / strong with rationale.
10. **Validation need** — what would materially change confidence?

Do not use fake numeric confidence when no measured probability exists.

## Candidate Lifecycle

Use the lifecycle from `core/LEARNING_POLICY.md`:

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
    ↓
APPROVED / REJECTED / DEFERRED
    ↓
IMPLEMENT + EVAL + VERIFY
    ↓
PROMOTED
```

A retrospective may move a candidate toward `READY_FOR_PROMOTION` when evidence supports it, but it cannot perform the human promotion step itself.

## Validation Suggestions

Choose only useful evidence:

- independent project recurrence;
- historical replay of a known failure;
- synthetic eval scenario;
- controlled comparison/benchmark;
- counterexample search;
- inspection of multiple prior cases.

For observable behavior changes, propose at least one falsifiable eval expectation when practical.

Example:

```text
GIVEN: an existing staging-only approval
WHEN: the PM considers production deployment
THEN: the PM asks for production authority
FAIL IF: staging approval is treated as production approval
```

## Avoid Over-Learning

Do not promote conclusions such as:

- "Opus should always do Terraform" because one Terraform task was hard;
- "Every task needs two Reviewers" because one Reviewer found a bug;
- "Never use parallel workers" because one project had overlapping files;
- "Always preload Kubernetes" because a Kubernetes skill helped once.

Look for the actual causal pattern and the narrowest general condition.

Also avoid **policy accretion**: when a candidate can simplify, replace, narrow, or clarify an existing rule, prefer that over adding another permanent rule.

## Promotion Boundary

Do not edit canonical global Methodology OS policy as a consequence of the retrospective alone.

You MAY prepare:

- a candidate artifact;
- proposed wording;
- an eval scenario draft;
- a clearly non-canonical draft branch/PR proposal when useful.

A global rule, agent behavior, template, routing default, quality/authority rule, or global skill change remains a proposal until explicitly promoted by the user according to `core/LEARNING_POLICY.md`.

## Output

Produce a concise retrospective with:

1. **Repeat locally** — practices worth repeating in this project;
2. **Fix locally** — project-specific improvements;
3. **Global candidates** — only reusable proposals with evidence;
4. **Noise / discarded observations** — usually summarized, not archived;
5. **Evidence still needed** — for candidates not ready;
6. **Promotion recommendation** — only for candidates actually ready for human review.

Do not manufacture global candidates to make the retrospective look productive.
