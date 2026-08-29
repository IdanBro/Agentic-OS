---
name: methodology-retrospective
description: Review a meaningful completed Methodology OS phase or project for reusable workflow lessons, routing/context/verification mistakes, and candidate improvements. Use after a substantial milestone or when explicitly requested. Produce learning candidates only; never silently change global OS policy.
---

# Methodology Retrospective

Extract useful learning from completed work without turning one experience into a global rule.

This V0 skill captures evidence and candidates. The full learning/promotion policy is defined later in `core/LEARNING_POLICY.md`.

## When to Use

Use after:

- a meaningful project or major phase completes;
- a costly failure exposes a workflow weakness;
- repeated retries or context pollution suggest a process issue;
- a routing choice clearly over- or under-spent capability;
- a verification/review gate caught an important defect;
- the user asks what the OS should learn from the work.

Do not run a full retrospective after every trivial task.

## Inputs

Prefer evidence from:

- `PROJECT_BRIEF.md`;
- `PLAN.md` and meaningful replans;
- final/current `STATE.md`;
- relevant `DECISIONS.md` entries;
- Task Packets and compact Work Reports when useful;
- verification/review outcomes;
- Git/PR evidence;
- meaningful failure/debug evidence.

Do not reread complete chat history unless a specific missing fact cannot be recovered from durable artifacts.

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
- Were Task Packets missing acceptance, verification, or authority information?

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
- Were options/tradeoffs clear when escalation happened?
- Was risk acceptance kept separate from verification truth?

### 9. Git / Integration

Ask:

- Were branches and commits coherent?
- Did workers accidentally take PM integration authority?
- Did parallel work create avoidable conflicts?
- Was `dev` verified after meaningful integration?
- Was `main` kept human-gated?

## Classify Each Learning

For each meaningful observation, classify it as one of:

### Project-Specific

Useful only to the current repository/team/domain.

Possible action:

- project skill;
- project `CLAUDE.md` fact;
- project documentation;
- repository test/check improvement.

### Candidate Global Learning

Potentially reusable across Methodology OS projects, but not yet approved as policy.

### Noise / One-Off

Interesting but insufficiently generalizable or actionable. Do not preserve it merely because it happened.

## Candidate Format

For each candidate global learning, record:

```text
CANDIDATE: <short title>

OBSERVED PROBLEM / OPPORTUNITY
- <what happened>

EVIDENCE
- <specific project evidence>

CURRENT OS BEHAVIOR
- <relevant rule/process>

PROPOSED CHANGE
- <smallest generalized change>

EXPECTED BENEFIT
- quality / tokens / speed / reliability

POSSIBLE COST / REGRESSION
- <what could become worse>

GENERALIZABILITY
- low / medium / high + reason

NEEDS MORE EVIDENCE
- yes/no + what evidence

PROMOTION STATUS
- candidate only; human approval required
```

## Avoid Over-Learning

Do not promote conclusions such as:

- "Opus should always do Terraform" because one Terraform task was hard;
- "Every task needs two Reviewers" because one Reviewer found a bug;
- "Never use parallel workers" because one project had overlapping files;
- "Always preload Kubernetes" because a Kubernetes skill helped once.

Look for the actual causal pattern.

## Output

Produce a concise retrospective with:

1. what worked well enough to repeat;
2. what materially failed or cost too much;
3. project-specific improvements;
4. candidate global learnings;
5. evidence still needed before global promotion.

Do not edit global Methodology OS policy automatically.

A global rule, agent behavior, template, routing default, or global skill change remains a proposal until explicitly approved by the user.
