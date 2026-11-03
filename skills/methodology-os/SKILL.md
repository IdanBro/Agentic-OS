---
name: methodology-os
description: Activate Methodology OS for complex, multi-stage, medium/high-risk, long-running, or context-heavy work. Use proportional planning, bounded delegation, evidence-based verification, durable state, selective skills, authority gates, and governed learning. Do not use for trivial one-step work.
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

- lifecycle / orchestration → `${CLAUDE_PLUGIN_ROOT}/core/ORCHESTRATION.md`
- model and effort selection → `${CLAUDE_PLUGIN_ROOT}/core/ROUTING.md`
- context packaging / handoff triggers → `${CLAUDE_PLUGIN_ROOT}/core/CONTEXT_POLICY.md`
- skill selection / loading → `${CLAUDE_PLUGIN_ROOT}/core/SKILL_POLICY.md`
- verification / review / integration gates → `${CLAUDE_PLUGIN_ROOT}/core/QUALITY_GATES.md`
- escalation / autonomy → `${CLAUDE_PLUGIN_ROOT}/core/ESCALATION_POLICY.md`
- learning / global promotion → `${CLAUDE_PLUGIN_ROOT}/core/LEARNING_POLICY.md`

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

Use `${CLAUDE_PLUGIN_ROOT}/core/SKILL_POLICY.md` for skill routing.

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

Use `${CLAUDE_PLUGIN_ROOT}/core/ESCALATION_POLICY.md`.

Continue autonomously through routine execution and decisions already inside a valid approval envelope.

Stop at unapproved consequential gates such as significant architecture, material scope, breaking interfaces, security tradeoffs, destructive/irreversible operations, material production effects, substantial cost/vendor commitments, consequential external commitments, and promotion to `main`.

A clear specific user instruction can satisfy the gate for that exact action; do not ask for duplicate confirmation merely for ceremony.

Never stretch an approval to a different target/scope/risk, and never merge to `main` without explicit approval for that promotion.

## 10. Learn Without Silent Self-Modification

Use `${CLAUDE_PLUGIN_ROOT}/core/LEARNING_POLICY.md` and `methodology-retrospective` only when meaningful reusable signal exists.

Classify learning as:

```text
project-specific
→ improve this project when authorized

global candidate
→ preserve / validate
→ NOT active policy

promoted global learning
→ explicit human promotion
→ eval + verify + review + PR→dev
```

Do not turn one failure into a permanent global rule.

Learn the causal condition rather than a technology label. State the generalization boundary and regression risk before recommending promotion.

A draft candidate, eval, branch, or PR may help evaluate a proposal, but it is not active Methodology OS behavior until explicitly promoted and integrated.

Never copy secrets or unnecessary private project evidence into global learning artifacts.

## 11. Completion

Do not declare the task/project complete until:

- requested outcome is satisfied;
- acceptance criteria are met;
- required verification/review gates passed;
- final state matches the evidence;
- important project state/decisions are current;
- pending human-gated actions are clearly separated from completed work.

After a meaningful milestone, use `methodology-retrospective` only when there is enough signal to justify the learning cost.
