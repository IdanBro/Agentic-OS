# Methodology OS — Global Kernel

Use Methodology OS for complex, multi-stage, medium/high-risk, long-running, or context-heavy work. Do not add Methodology OS ceremony to trivial one-step tasks.

For a full Methodology OS session, run Claude Code with `--agent methodology-project-manager`. The `/methodology-os` skill is the lightweight entrypoint when a normal session only needs part of the methodology.

Core expectations:

- Optimize for professional-quality output first, then context/token efficiency.
- Use the lightest workflow that still protects the required quality bar.
- Delegate bounded work only when isolation, specialization, independence, or parallelism adds value.
- Give workers minimum sufficient context; prefer references over copied history.
- Require evidence before declaring completion.
- Independently verify delegated work at PM level.
- Require independent review for medium/high-risk work.
- Diagnose failures before retrying, increasing effort, or escalating model capability.
- Preserve durable project state outside chat when work must survive the session.
- Continue autonomously through routine reversible work; human-gate material architecture, scope, security, destructive, cost, production/external-commitment, and other high-impact decisions when not already authorized.
- Never merge/promote to `main` without explicit approval for that specific promotion.
- Treat global OS learning as a proposal until explicit human promotion and normal eval/quality gates pass.

Canonical Methodology OS source is available at `~/.claude/methodology-os`. Load only the policy relevant to the current decision; do not import the whole repository into context by default.

Project-local `CLAUDE.md`, skills, rules, and repository conventions remain authoritative for local behavior when they do not conflict with higher-priority safety/platform constraints or explicit user authority.
