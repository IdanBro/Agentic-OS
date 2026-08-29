# Methodology OS — Handoff Template

> Purpose: transfer project ownership from one Project Manager context to another without transferring the full conversation history.

A handoff is a **compressed transition snapshot**. It supplements canonical state artifacts; it does not replace them.

## Handoff Metadata

- **Created:** `<YYYY-MM-DD HH:MM>`
- **From:** `<current PM/session identifier if useful>`
- **To:** `Fresh Methodology OS Project Manager`
- **Lifecycle mode:** `<Standard | Full>`
- **Lifecycle phase:** `<phase>`
- **Active plan:** `<PLAN.md version>`
- **Current branch:** `<branch or n/a>`
- **Latest relevant commit:** `<SHA or n/a>`
- **State freshness:** `<STATE.md last-updated timestamp>`

## 1. Mission

`<One concise paragraph describing the project outcome and the immediate purpose of the continuation.>`

Do not restate the entire Project Brief. Reference it below.

## 2. Read First

The successor PM SHOULD read, in this order unless the handoff says otherwise:

1. `PROJECT_BRIEF.md`
2. `STATE.md`
3. the relevant section of `PLAN.md`
4. referenced active entries in `DECISIONS.md`
5. the specific implementation/review artifacts listed below

Do not read old chat history by default.

## 3. Current Position

- **Active task / phase:** `<plan ID>`
- **Status:** `<in progress / ready to verify / review pending / blocked / integrating>`
- **Current owner:** `<PM / worker>`
- **Why work stopped here:** `<context handoff / session boundary / blocker / phase boundary / explicit user request>`

## 4. What Is Already Complete

Only outcomes the successor might otherwise repeat.

- `<plan ID>` — `<completed and verified outcome>`
- `<plan ID>` — `<completed and verified outcome>`

## 5. Immediate Next Actions

These should be executable without reconstructing the prior conversation.

1. `<next action>`
2. `<next action>`
3. `<next action>`

If a next action depends on a human gate, say so explicitly.

## 6. Verification Status

Summarize only the evidence needed to avoid false assumptions.

Use the canonical verification-gate vocabulary from `core/QUALITY_GATES.md`.

| Area / Claim | Status | Evidence / Reference |
| --- | --- | --- |
| `<area>` | `<PASS / FAIL / INCONCLUSIVE / NOT_RUN / N/A>` | `<compact evidence>` |

Do not paste full logs.

Do not convert missing or stale evidence into `PASS`; preserve residual uncertainty explicitly.

## 7. Open Blockers / Human Gates

- `<blocker or approval needed>`

If none, write `None.`

For human gates, distinguish clearly between:

- **not requested**,
- **requested / awaiting approval**,
- **explicitly approved**.

Never infer approval from silence or from the existence of this handoff.

## 8. Open Risks / Uncertainties

- `<risk>` — `<what evidence or action would resolve it>`

Include only unresolved items.

## 9. Decisions That Matter Now

- `<D-###>` — `<title and why the successor needs it>`

Reference `DECISIONS.md`; do not copy full rationale unless access to the source is unavailable.

## 10. Failed Approaches Worth Remembering

Include only failures where repeating the approach would waste meaningful time, tokens, or risk.

- **Attempt:** `<what was tried>`
  - **Result:** `<what happened>`
  - **Evidence:** `<short reference>`
  - **Why not repeat:** `<reason>`

If none, write `None.`

## 11. Important Files / Artifacts

- `<path / PR / issue / artifact>` — `<why it matters now>`
- `<path / PR / issue / artifact>` — `<why it matters now>`

Keep this list narrow. The successor can discover additional context as needed.

## 12. Git / Integration Snapshot

For engineering work:

- **Base branch:** `<dev or other>`
- **Current branch:** `<branch>`
- **Latest relevant commit:** `<SHA>`
- **Open PR:** `<number/reference / none>`
- **Integrated into `dev`:** `<yes/no>`
- **Promotion to `main`:** `<not prepared / prepared / awaiting approval / explicitly approved>`
- **Working tree expected clean:** `<yes/no/unknown>`

The successor PM MUST query current Git state before relying on this snapshot if any new work may have occurred since handoff creation.

## 13. Successor Start Checklist

Before continuing implementation, the successor PM should:

- [ ] read the canonical state artifacts listed above;
- [ ] confirm the current branch/artifact state rather than assuming the snapshot is still current;
- [ ] reconcile any mismatch between `STATE.md`, Git/artifacts, and this handoff;
- [ ] preserve existing human gates;
- [ ] continue from the next action instead of re-running completed exploration by default;
- [ ] update `STATE.md` once ownership is successfully resumed.

## Handoff Creation Rules

Create or refresh a handoff when:

- PM context has become noisy or degraded;
- a fresh PM is preferable to further compaction;
- a long-running project crosses a meaningful session boundary;
- ownership is intentionally being transferred;
- the user asks for a continuation artifact.

Before creating the handoff:

1. reconcile `STATE.md` with actual repository/artifact state;
2. update material decisions;
3. ensure verification claims have evidence;
4. remove stale blockers and next actions;
5. capture only failed approaches worth preserving.

Do not use a handoff as a transcript dump. If the handoff becomes large because it repeats the Project Brief, Plan, State, or Decisions, replace repetition with references.
