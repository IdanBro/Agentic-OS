# Methodology OS — Decisions Template

> Purpose: preserve the rationale for **material, non-obvious decisions** that future agents may otherwise reopen, misunderstand, or reverse accidentally.

This is a lightweight decision record, not a meeting log.

## Usage Rules

Create an entry when a decision materially affects one or more of:

- architecture or system shape,
- interfaces or compatibility,
- security or operational behavior,
- scope or success criteria,
- major dependency choice,
- deployment / migration strategy,
- meaningful cost tradeoff,
- irreversible or difficult-to-reverse behavior,
- a plan change whose rationale will matter later.

Do **not** create entries for:

- obvious implementation details,
- routine formatting choices,
- every library method or variable name,
- chronological progress,
- temporary hypotheses,
- decisions that can be cheaply rediscovered from clear repository conventions.

Use stable IDs: `D-001`, `D-002`, ...

---

## Decision Index

| ID | Title | Status | Date |
| --- | --- | --- | --- |
| `D-001` | `<title>` | `<active / superseded / rejected>` | `<YYYY-MM-DD>` |

---

## D-001 — `<Decision title>`

- **Date:** `<YYYY-MM-DD>`
- **Status:** `<active | superseded | rejected>`
- **Decision owner:** `<PM / user / project authority>`
- **Human approval required:** `<yes/no>`
- **Human approval:** `<reference/date/n/a>`

### Context

`<What problem, constraint, or tradeoff required a decision?>`

### Decision

`<What was decided, stated unambiguously?>`

### Rationale

- `<reason>`
- `<reason>`

Focus on why this option was selected, not on retelling the entire investigation.

### Alternatives Considered

- **`<alternative>`** — `<why it was not selected>`
- **`<alternative>`** — `<why it was not selected>`

Omit alternatives that were never serious candidates.

### Consequences

**Positive / intended:**
- `<consequence>`

**Tradeoffs / costs:**
- `<consequence>`

**Follow-up obligations:**
- `<migration, validation, documentation, monitoring, or none>`

### Evidence / References

- `<file / issue / benchmark / experiment / external reference>`

### Supersession

- **Supersedes:** `<D-### or none>`
- **Superseded by:** `<D-### or none>`

---

## Additional Entries

Copy the decision block above and increment the ID.

## Maintenance Rules

The Project Manager owns consistency of this log.

1. Prefer append-only decision entries.
2. Do not rewrite historical rationale merely because a later decision differs.
3. When a decision changes, mark the old entry `superseded` and link the new entry.
4. A rejected proposal may be recorded only if future agents are likely to reconsider it and the reason for rejection has durable value.
5. Human-gated decisions must record the approval state accurately; absence of a recorded approval is not permission.
6. Keep each entry concise enough that a fresh PM can scan the index and read only relevant decisions.
