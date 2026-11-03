---
name: methodology-handoff
description: Prepare a Methodology OS PM-to-PM handoff when context becomes noisy, a session boundary is reached, or ownership must transfer. Reconcile canonical state and actual Git/artifact state first, then create a compact continuation snapshot without copying chat history.
---

# Methodology Handoff

Transfer ownership without transferring the full conversation.

A handoff is successful when a fresh PM can continue safely from canonical project artifacts and current evidence.

## When to Use

Use this skill when:

- PM context has become materially noisy or polluted;
- repeated compaction would risk losing important distinctions;
- a long-running project crosses a meaningful session boundary;
- ownership intentionally moves to another PM/session;
- the user explicitly asks for a continuation/handoff artifact.

Do not create handoffs routinely after every small task.

## Workflow

### 1. Reconcile Actual State First

Before writing a handoff, inspect the current reality.

For engineering work, confirm where relevant:

- current branch;
- latest relevant commit;
- open PR/integration state;
- whether expected changes actually exist;
- current verification/review state;
- whether `dev` integration occurred;
- current `main` promotion state.

For non-Git work, inspect the equivalent canonical artifact state.

Do not let an older `STATE.md` or chat summary overrule newer observable state.

### 2. Reconcile Canonical Project State

Update `STATE.md` so it reflects current truth.

Remove:

- stale next actions;
- resolved blockers;
- obsolete risks;
- verification claims whose evidence is no longer current.

Preserve only milestone-level completed outcomes needed for continuation.

### 3. Update Durable Decisions

If a material non-obvious decision was made and its rationale matters later, update `DECISIONS.md` before handoff.

Do not turn the decision log into session history.

Human-gated decisions must preserve approval state accurately.

### 4. Verify Evidence Freshness

A handoff must not carry stale confidence forward.

Check whether:

- tests/checks apply to the final state;
- review applies to the current diff/artifact;
- unresolved `INCONCLUSIVE` or `NOT_RUN` items remain visible;
- risk acceptance is distinguished from verification truth.

### 5. Create `HANDOFF.md`

Use the canonical template.

Include only what a replacement PM needs to resume:

- immediate mission;
- current lifecycle position;
- verified completed outcomes worth remembering;
- ordered next actions;
- compact verification status;
- blockers/human gates;
- unresolved risks;
- relevant decision IDs;
- failed approaches worth not repeating;
- narrow list of important files/artifacts;
- current Git/integration snapshot.

### 6. Prefer References Over Copying

Reference:

- `PROJECT_BRIEF.md` for stable mission/scope;
- `PLAN.md` for intended structure;
- `STATE.md` for current truth;
- `DECISIONS.md` for rationale;
- PRs/issues/files for source evidence.

Do not duplicate their full contents into the handoff.

Do not paste raw logs or the old conversation transcript.

### 7. Preserve Human Gates

Never infer approval from:

- silence;
- a previous PM's confidence;
- a stale state label;
- the existence of the handoff itself.

The handoff must distinguish:

- approval not requested;
- requested / awaiting approval;
- explicitly approved.

`main` remains human-gated.

### 8. Define the Successor Start

The handoff should instruct the next PM to:

1. read `PROJECT_BRIEF.md` and `STATE.md` first;
2. inspect only relevant plan/decision sections;
3. query current Git/artifact state when it may have changed;
4. reconcile mismatches before execution;
5. continue from the next action instead of repeating completed exploration;
6. update `STATE.md` once ownership is resumed.

## Compression Standard

Keep information if losing it would likely cause:

- duplicated work;
- a wrong implementation decision;
- a missed human gate;
- stale verification being trusted;
- repeated failed investigation;
- inability to resume the critical path.

Remove information that is merely chronological or cheaply rediscoverable.

## Completion Rule

The handoff is complete when a fresh PM can determine:

- what outcome matters now;
- where the project actually stands;
- what has been verified;
- what remains uncertain or blocked;
- what decision/gate is pending;
- what to do next;

without reading the previous chat by default.
