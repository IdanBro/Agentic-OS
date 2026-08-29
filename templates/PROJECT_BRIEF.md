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

## 8. Human Gates

Record project-specific approvals in addition to global gates.

- `<decision or operation requiring explicit user approval>`

If there are no additional gates, write:

`None beyond Methodology OS global gates.`

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
- new human gates.

Do **not** update it for:

- lifecycle mode or phase changes,
- routine task completion,
- command output,
- temporary blockers,
- implementation detail,
- chronological progress.

Operational mode and phase belong in `STATE.md`.

When a material brief change requires human approval, obtain that approval before treating the changed brief as canonical.
