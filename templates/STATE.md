# Methodology OS — State Template

> Purpose: provide the **current operational truth** of the project. A replacement Project Manager should be able to read this file and quickly understand where the project stands and what should happen next.

This file is a snapshot, not a transcript.

## Metadata

- **Last updated:** `<YYYY-MM-DD HH:MM>`
- **Lifecycle mode:** `<Lite | Standard | Full>`
- **Lifecycle phase:** `<INTAKE | TRIAGE | INVESTIGATE | PLAN | HUMAN_GATE | PREPARE | EXECUTE | VERIFY | REVIEW | DIAGNOSE | INTEGRATE | COMPLETE | BLOCKED>`
- **Active plan:** `<PLAN.md version>`
- **Repository / artifact:** `<reference>`
- **Current branch:** `<branch or n/a>`
- **Base branch:** `<usually dev or n/a>`

## 1. Current Objective

`<What outcome is the PM actively trying to advance right now?>`

## 2. Current Position

- **Active phase/task:** `<plan ID or concise description>`
- **Owner:** `<PM | worker type / agent reference>`
- **Current status:** `<ready | in progress | awaiting human gate | verifying | review pending | diagnosing | blocked | integrating>`

## 3. Completed Outcomes

Keep only milestone-level outcomes that matter for understanding the remaining work.

- `<plan ID>` — `<verified outcome>`
- `<plan ID>` — `<verified outcome>`

Do not list every command, edit, or worker action.

## 4. In Progress

- `<plan ID>` — `<what is currently happening and who owns it>`

If nothing is active, write `None.`

## 5. Next Actions

Ordered, executable next actions only.

1. `<next action>`
2. `<next action>`
3. `<next action>`

Prefer references to plan IDs rather than repeating full task descriptions.

## 6. Blockers / Pending Human Input

- `<blocker, required decision, or approval>`

If none, write `None.`

Do not classify ordinary implementation choices as human blockers.

## 7. Verification Snapshot

Record the evidence that materially supports the current state.

| Claim / Area | Status | Evidence |
| --- | --- | --- |
| `<claim>` | `<PASS / FAIL / PARTIAL / NOT RUN>` | `<command/result/reference>` |

Keep evidence compact. Full logs stay outside this file.

## 8. Git / Integration State

For source-controlled engineering work:

- **Task branch:** `<branch>`
- **Latest relevant commit:** `<SHA / none>`
- **PR:** `<number/reference / none>`
- **Integrated into `dev`:** `<yes/no/n/a>`
- **`main` promotion:** `<not prepared / prepared / awaiting explicit approval / approved / n/a>`
- **Known working-tree concern:** `<none or concise concern>`

For non-Git work, replace this section with equivalent artifact integration state.

## 9. Open Risks / Uncertainties

Only unresolved items that may change planning, verification, or outcome confidence.

- `<risk or uncertainty>` — `<current mitigation / next evidence needed>`

If none, write `None.`

## 10. Active Decision References

Reference relevant entries from `DECISIONS.md`.

- `<D-###>` — `<short title>`

Do not duplicate full rationale here.

## 11. Important References

Only the small set likely needed by the next PM action.

- `<path / document / PR / issue / external reference>` — `<why it matters>`

## 12. Context Health

- **Can a replacement PM reconstruct the current state from canonical artifacts?** `<yes/no>`
- **Is current conversation history carrying important truth not yet externalized?** `<yes/no>`
- **Is a handoff recommended before substantial additional work?** `<yes/no + reason>`

## Maintenance Rules

The Project Manager owns this artifact and updates it whenever the **operational truth materially changes**.

Typical update triggers:

- phase transition,
- task starts or completes,
- verification changes confidence,
- blocker appears or clears,
- meaningful replan,
- integration/PR/branch state changes,
- important risk changes,
- before a handoff.

Rules:

1. Replace stale state instead of appending history.
2. Remove obsolete next actions and resolved blockers.
3. Keep completed history at milestone granularity.
4. Never record a claim as verified without evidence.
5. Never use this file to store raw logs or long worker reports.
6. Prefer references to `PROJECT_BRIEF.md`, `PLAN.md`, and `DECISIONS.md` over duplication.
7. If the file becomes difficult to scan, prune obsolete detail before adding more.

`STATE.md` is the default first file a replacement PM should read after the Project Brief.
