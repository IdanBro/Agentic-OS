---
name: methodology-os
description: Activate Methodology OS for complex, multi-stage, medium/high-risk, long-running, or context-heavy work. Use proportional planning, bounded delegation, evidence-based verification, durable state, Git integration, and human gates. Do not use for trivial one-step work.
---

# Methodology OS

Use this skill as the lightweight entrypoint for Methodology OS.

Do **not** load every OS policy file by default. Load only the policy needed for the current decision.

## 1. Activate Proportionally

Classify the work before adding process:

- **Lite** — small, low-risk, obvious, cheaply verified.
- **Standard** — normal multi-step or medium-risk work.
- **Full** — large, high-risk, ambiguous, long-running, or coordination-heavy work.

Use the lightest workflow that still protects the required professional quality bar.

## 2. Establish the Contract

Determine:

- requested outcome,
- important constraints,
- success/acceptance criteria,
- scope boundaries,
- risk,
- human-authority gates.

Inspect available project context before asking questions that can be answered safely from evidence.

## 3. Use the Relevant OS Policy Only When Needed

Policy map:

- lifecycle / orchestration → `core/ORCHESTRATION.md`
- model and effort selection → `core/ROUTING.md`
- context packaging / handoff triggers → `core/CONTEXT_POLICY.md`
- skill selection / loading → `core/SKILL_POLICY.md`
- verification / review / integration gates → `core/QUALITY_GATES.md`
- escalation / autonomy → `core/ESCALATION_POLICY.md` once implemented
- learning / global promotion → `core/LEARNING_POLICY.md` once implemented

The global installation layer should provide access to the canonical Methodology OS source. Do not copy whole policy files into the current prompt merely to be thorough.

## 4. Plan Only as Much as Needed

For Standard/Full work, use `methodology-planning` when a durable or structured plan materially helps.

For Lite work, a short internal plan may be sufficient.

If key uncertainty would materially alter the plan, investigate first rather than planning around guesses.

## 5. Delegate for a Reason

Delegate when it improves one or more of:

- context isolation,
- specialization,
- independent judgment,
- parallelism,
- preservation of PM context.

Do not delegate a tiny task when coordination costs more than execution.

Use bounded Task Packets with observable acceptance and verification requirements.

## 6. Load Skills Selectively

Use `core/SKILL_POLICY.md` for skill routing.

Default behavior:

- no skill when normal role competence is sufficient;
- prefer project/nested skills for local conventions;
- add the narrowest relevant domain skill;
- invoke methodology subskills only when their procedure is active;
- do not preload broad skill bundles "just in case".

## 7. Require Evidence

For delegated work:

```text
worker execution
→ worker self-verification
→ PM independent verification
→ Reviewer for medium/high risk
→ integration readiness
→ dev integration
→ post-integration verification when required
```

Worker confidence is not project truth.

## 8. Preserve State

For work that needs durable continuity, keep project truth outside the conversation using the canonical state artifacts.

Do not use chat history as the only record of:

- objective,
- current state,
- important decisions,
- verification status,
- blockers,
- next actions.

When PM context degrades, use `methodology-handoff` rather than carrying an increasingly noisy session indefinitely.

## 9. Preserve Human Authority

Continue autonomously through routine execution.

Stop at defined high-impact gates, especially significant architecture, scope, breaking interfaces, security tradeoffs, destructive operations, material cost, irreversible behavior, and promotion to `main`.

Never merge to `main` without explicit user approval.

## 10. Completion

Do not declare the task/project complete until:

- requested outcome is satisfied;
- acceptance criteria are met;
- required verification/review gates passed;
- final state matches the evidence;
- important project state/decisions are current;
- pending human-gated actions are clearly separated from completed work.

After a meaningful milestone, `methodology-retrospective` may be used to capture learning candidates without silently changing global policy.
