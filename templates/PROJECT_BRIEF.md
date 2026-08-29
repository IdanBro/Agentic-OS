# Methodology OS — Project Brief Template

> Purpose: define the stable contract for a project. This file explains **what outcome is being pursued and what constraints matter**. It is not a task tracker or session log.

## Metadata

- **Project:** `<name>`
- **Created:** `<YYYY-MM-DD>`
- **Last materially updated:** `<YYYY-MM-DD>`
- **Primary repository/artifact:** `<path or reference>`

## 1. Outcome

Describe the desired end state in one concise paragraph.

`<What should be true when this project is successfully complete?>`

## 2. Success Criteria

List observable project-level criteria. Prefer outcomes over activities.

- `<criterion>`
- `<criterion>`
- `<criterion>`

## 3. In Scope

- `<included capability / workstream / artifact>`
- `<included capability / workstream / artifact>`

## 4. Out of Scope

Use this section only where boundaries prevent scope creep or ambiguity.

- `<explicit non-goal>`
- `<explicit non-goal>`

## 5. Constraints

Record constraints that materially influence planning or implementation.

- **Technical:** `<constraint or none>`
- **Operational:** `<constraint or none>`
- **Compatibility:** `<constraint or none>`
- **Time / sequencing:** `<constraint or none>`
- **Cost:** `<constraint or none>`
- **Other:** `<constraint or none>`

Do not copy general Methodology OS rules here unless this project adds a project-specific constraint.

## 6. Quality Bar

Record project-specific quality expectations beyond the global Methodology OS baseline.

Examples:

- required backward compatibility,
- latency or reliability targets,
- security expectations,
- documentation requirements,
- required test depth,
- artifact quality requirements.

`<project-specific quality bar or "global baseline applies">`

## 7. Known Starting Context

Record only durable facts that materially affect the project and cannot be cheaply rediscovered.

- `<fact / architecture constraint / existing dependency>`
- `<fact / architecture constraint / existing dependency>`

Prefer references to source files or documents over copied content.

## 8. Authority & Human Gates

Use `core/ESCALATION_POLICY.md` for the global authority model.

### Project-Specific Human Gates

Record approvals required **in addition to** Methodology OS global gates.

- `<decision or operation requiring explicit user approval>`

If there are no additional gates, write:

`None beyond Methodology OS global gates.`

### Standing / Pre-Authorized Envelopes

Record only durable project-level authority that the user explicitly delegated and that would otherwise cause repeated approval requests.

| Action / Decision Class | Target / Scope | Conditions / Limits | Approval Reference |
| --- | --- | --- | --- |
| `<authorized action>` | `<system/environment/scope>` | `<conditions, limits, expiry/freshness assumptions>` | `<reference/date>` |

If none, write `None.`

Rules:

1. Do not infer an approval envelope from silence or general enthusiasm for the project.
2. Keep envelopes bounded by target, scope, operation, conditions, and material risk/cost assumptions.
3. A project-level envelope does not authorize actions outside its stated target or conditions.
4. When material circumstances change, reassess the envelope before relying on it.
5. `main` promotion remains explicitly human-gated per global policy; a general project-autonomy statement is not blanket approval for future main merges.
6. Temporary/task-specific approval is normally referenced from `DECISIONS.md` or current state rather than bloating the stable Project Brief.

## 9. Canonical References

- **Plan:** `PLAN.md`
- **Current state:** `STATE.md`
- **Decision log:** `DECISIONS.md`
- **Latest handoff:** `HANDOFF.md` when present
- **Project-specific references:** `<paths / URLs / docs>`

## Maintenance Rules

The Project Manager owns this artifact.

Update it only when the accepted project contract materially changes, such as:

- objective changes,
- scope changes,
- success criteria changes,
- important constraint changes,
- new human gates,
- durable standing authority changes.

Do **not** update it for:

- lifecycle mode or phase changes,
- routine task completion,
- command output,
- temporary blockers,
- implementation detail,
- chronological progress,
- one-off approvals that belong in a decision/state record.

Operational mode and phase belong in `STATE.md`.

When a material brief change requires human approval, obtain that approval before treating the changed brief as canonical.
