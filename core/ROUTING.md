# Methodology OS — Model & Effort Routing

This document defines how Methodology OS selects model capability and effort for the Project Manager and delegated agents.

The goal is not to minimize raw token use. The goal is to obtain the required professional quality with the least unnecessary model capability, reasoning depth, tool activity, and retry cost.

The Project Manager owns routing decisions.

---

## 1. Routing Objective

For each unit of work, select the least expensive configuration that is reasonably expected to satisfy the required quality bar on the first well-prepared attempt.

Routing MUST balance:

1. professional quality,
2. correctness and risk,
3. token/context efficiency,
4. expected retry cost,
5. latency only after the above are protected.

The OS MUST NOT optimize for a cheap first attempt when that attempt is predictably likely to fail and create more total work.

The default principle is:

> Right-size capability first, then right-size effort.

---

## 2. Keep Role, Model, and Effort Separate

A role answers:

> Who should own this kind of work?

A model answers:

> How much underlying capability is needed?

Effort answers:

> How deeply should that model reason, explore, call tools, and verify on this request?

These are separate routing decisions.

Examples:

- `implementer` + Sonnet + medium,
- `reviewer` + Opus + high,
- `debugger` + Fable + high.

Do not encode permanent model assumptions into role definitions unless repeated eval evidence justifies doing so.

---

## 3. Prefer Family Aliases Over Pinned Versions

Methodology OS SHOULD use Claude Code family aliases where possible:

- `haiku`,
- `sonnet`,
- `opus`,
- `fable`.

Aliases allow Claude Code to resolve to the recommended current model for the configured provider.

Pin a full model ID only when reproducibility, compatibility, provider constraints, or an evaluated regression requires it.

The PM MUST NOT assume that an alias resolves to the same exact model on every provider.

If an organization allowlist or provider substitutes a requested model, treat the actual resolved model as the execution model and record a material substitution when it affects confidence or verification.

---

## 4. Model Capability Ladder

The following is the V0 semantic routing model.

### 4.1 Haiku — Narrow Efficiency Tier

Use Haiku only for very simple, short, low-risk work where the required reasoning is obvious and bounded.

Good candidates:

- simple classification,
- targeted repository lookup,
- extracting a known fact,
- straightforward formatting or transformation,
- mechanical inspection with an explicit checklist,
- other tasks where mistakes are cheap and easy to detect.

Do NOT use Haiku as the default implementation model merely because it is cheaper.

Avoid Haiku for:

- architecture,
- non-trivial debugging,
- ambiguous implementation,
- multi-component changes,
- high-risk review,
- security-sensitive reasoning,
- tasks whose failure would trigger expensive retries.

Some Haiku generations may not support the full effort ladder. The PM must respect the capabilities of the actual resolved model rather than assuming an effort level is available.

---

### 4.2 Sonnet — Default Execution Tier

Sonnet is the default model family for bounded day-to-day execution.

Good candidates:

- normal feature implementation,
- configuration and infrastructure changes with clear scope,
- CI/CD work with defined acceptance criteria,
- routine refactors,
- test implementation,
- documentation or artifact production,
- localized debugging with a reproducible failure,
- medium-risk review when the change is well bounded.

Sonnet SHOULD be the first choice for an Implementer unless task characteristics justify Opus or Fable.

The PM should improve task definition before escalating a well-bounded implementation away from Sonnet.

---

### 4.3 Opus — Complex Reasoning Tier

Use Opus when the work requires materially stronger reasoning, synthesis, judgment, or investigation than normal bounded execution.

Good candidates:

- architecture decisions,
- complex planning,
- cross-component reasoning,
- difficult code or infrastructure changes,
- ambiguous requirements with meaningful consequences,
- non-trivial root-cause analysis,
- high-risk independent review,
- security, networking, distributed-systems, or production reasoning where subtle mistakes matter,
- recovery after evidence indicates a capability gap rather than merely insufficient effort.

Opus SHOULD be preferred over repeatedly retrying Sonnet when the problem is intrinsically difficult.

Opus SHOULD NOT be used automatically for every DevOps, Kubernetes, Terraform, security-adjacent, or backend task. Technology name is not a routing criterion by itself.

---

### 4.4 Fable — Long-Horizon / Hardest-Problem Tier

Use Fable for work whose value comes from sustained autonomous investigation, long-horizon coherence, broad exploration, and repeated self-verification.

Good candidates:

- tasks larger than a normal single-sitting implementation,
- highly ambiguous root-cause investigations,
- complex outages or system-wide failures,
- difficult architecture problems with many interacting unknowns,
- long autonomous investigations where stopping and restarting would lose important reasoning state,
- large multi-stage work where Fable's extra autonomy is expected to outperform a smaller worker decomposition.

Fable is not the default merely because a task is important.

Prefer Opus when the problem is hard but bounded. Prefer Fable when the combination of hardness, ambiguity, horizon, and autonomous investigation justifies the extra capability and possible cost.

Fable availability may depend on the account, organization, provider, or usage-credit configuration. A route that would create a material new charge or require usage-credit consent crosses the existing cost/escalation policy and MUST NOT silently bill without appropriate authorization.

If Fable is unavailable, route to Opus at an appropriate effort level and compensate with stronger decomposition, explicit investigation phases, or independent verification.

---

## 5. Effort Ladder

Effort controls how much work a supported model puts into the request, including reasoning depth, tool usage, and self-verification.

Effort is not a strict token budget.

### 5.1 Low

Use for short, obvious, tightly scoped work where additional exploration has little expected value.

Examples:

- simple lookups,
- mechanical checks,
- trivial transformations,
- tightly specified low-risk subagent tasks.

Low effort is an efficiency tool, not a default for all subagents.

---

### 5.2 Medium

Use as the default cost-conscious setting for well-bounded work that still requires real reasoning and tool use.

Typical uses:

- normal bounded implementation,
- routine CI/config changes,
- medium-risk review with clear criteria,
- structured research with limited ambiguity.

For Methodology OS, `Sonnet + medium` is the default worker baseline when the task packet is strong and risk is not high.

---

### 5.3 High

Use when quality and reasoning depth materially matter.

Typical uses:

- PM orchestration,
- difficult implementation,
- meaningful planning,
- non-trivial debugging,
- high-risk review,
- tasks with several interacting constraints.

High is the default quality-oriented level for intelligence-sensitive work.

---

### 5.4 XHigh

Use for advanced coding or agentic work that genuinely benefits from extended exploration and deeper reasoning.

Typical signals:

- long-running task,
- repeated tool use is expected,
- substantial search/investigation,
- deep cross-system reasoning,
- high cost of a subtle mistake,
- high effort succeeded partially but left material uncertainty.

Do not select `xhigh` merely because the task is labeled Full Mode.

---

### 5.5 Max

Use only when the absolute highest available capability is justified and token efficiency is temporarily secondary.

Good reasons include:

- a critical problem remains unresolved after a well-diagnosed lower-effort attempt,
- an exceptionally difficult decision has high downside if wrong,
- evals demonstrate meaningful gains at `max`,
- the user explicitly requests maximum depth.

`max` is an exception, not a normal route.

The PM MUST record the reason for choosing `max`.

---

## 6. Routing Dimensions

Before choosing a model and effort, evaluate the following dimensions.

### Ambiguity

How much of the problem is unknown or underspecified?

- Low: clear desired change and known path.
- Medium: some discovery or judgment required.
- High: problem itself must be discovered or reframed.

### Reasoning Complexity

How difficult is the conceptual work?

- Low: mechanical or local.
- Medium: several interacting constraints.
- High: architecture, distributed behavior, subtle causal reasoning, or broad synthesis.

### Scope / Breadth

How much of the system must be understood simultaneously?

- Low: one local file/component.
- Medium: several related files/components.
- High: cross-system or system-wide.

### Risk / Blast Radius

What happens if the result is wrong?

- Low: cheap and reversible.
- Medium: meaningful regression or rework.
- High: production, security, data, infrastructure, financial, or other consequential impact.

### Horizon / Tool Depth

How much sustained work is expected?

- Low: a few direct operations.
- Medium: iterative implementation and verification.
- High: extended investigation, many tool calls, or long autonomous execution.

### Verification Difficulty

How hard is it to prove correctness?

- Low: one obvious deterministic check.
- Medium: several tests or artifact inspections.
- High: indirect evidence, integration/system behavior, or subtle regressions.

### Retry Cost

How expensive would a weak first attempt be?

Include:

- extra model calls,
- context pollution,
- repeated repository exploration,
- reverted code,
- duplicated reviews,
- human interruption,
- operational risk.

A high expected retry cost justifies stronger initial routing.

---

## 7. V0 Base Routes by Agent

These are starting points, not rigid rules.

| Agent / Work | Default route | Escalate when |
| --- | --- | --- |
| PM — Lite | Sonnet / medium or high | ambiguity or consequence increases |
| PM — Standard | Sonnet / high | planning requires substantial cross-system judgment |
| PM — Full | Opus / high | horizon/ambiguity becomes extreme or prolonged |
| PM — exceptional long-horizon | Fable / high | use `xhigh` only when extended depth is justified |
| Implementer — trivial/mechanical | Haiku where safe, otherwise Sonnet / low | task stops being mechanical |
| Implementer — normal bounded work | Sonnet / medium | complexity, risk, or uncertainty increases |
| Implementer — difficult bounded work | Sonnet / high or Opus / high | evidence shows capability gap |
| Reviewer — medium risk | Sonnet / medium or high | subtle cross-component/high-risk reasoning needed |
| Reviewer — high risk | Opus / high | system-wide or exceptionally difficult review |
| Reviewer — exceptional system-wide audit | Fable / high | only when long-horizon breadth justifies it |
| Debugger — localized/reproducible | Sonnet / high | root cause remains conceptually ambiguous |
| Debugger — non-trivial/ambiguous | Opus / high | sustained investigation or broader unknowns dominate |
| Debugger — long-horizon/system-wide | Fable / high | `xhigh` only when long exploration is justified |

The PM MUST adjust these routes using the dimensions above.

---

## 8. PM Session Stability

The PM's context is long-lived relative to workers.

Therefore, prefer a stable PM model and effort for a session rather than repeatedly changing effort every turn.

Reason:

- routing churn complicates behavior,
- effort changes can reduce prompt-cache reuse,
- the PM should remain a stable orchestrator while task-specific workers absorb routing variation.

Default V0 strategy:

```text
Stable PM session
      ↓
per-task routing
      ↓
worker(model, effort)
```

If the PM itself is clearly underpowered for the project's planning/orchestration complexity, upgrade the PM deliberately rather than oscillating between settings.

---

## 9. Routing Algorithm

For every delegated task, the PM MUST make an explicit routing decision before the worker is created.

Before the **first worker dispatch in a session**, the PM MUST read this file in full unless it is already loaded and current. Subsequent workers may reuse the loaded policy, but each worker still requires a fresh task-specific route.

`model: inherit` in a worker definition is only a fallback for compatibility. It MUST NOT be treated as the default routing policy. If the PM intentionally selects `inherit`, that choice must be explicit and justified; otherwise both model family and effort must be specified directly.

The PM follows this sequence.

### Step 1 — Define the quality bar

Determine:

- expected outcome,
- acceptance criteria,
- risk level,
- required verification.

Do not route an undefined task.

### Step 2 — Improve the task packet

Before buying more capability, reduce avoidable ambiguity through:

- relevant file/context selection,
- explicit scope,
- acceptance criteria,
- known constraints,
- verification instructions.

A stronger task packet often makes a cheaper model sufficient.

### Step 3 — Choose the lowest suitable model family

Ask:

> Is this mechanical, normal bounded execution, complex reasoning, or long-horizon hard work?

Map initially to:

```text
mechanical      → Haiku / Sonnet
bounded         → Sonnet
complex         → Opus
long + hardest  → Fable
```

### Step 4 — Choose effort

Ask:

> Given this model, how deeply must it investigate and verify?

Map initially to:

```text
obvious          → low
bounded          → medium
intelligence-sensitive → high
extended agentic → xhigh
exceptional      → max
```

### Step 5 — Commit the route before dispatch

Record/pass the selected model family and effort in the worker launch and, when a Task Packet is used, in its routing metadata.

The PM MUST NOT create the worker first and decide whether the inherited model was appropriate afterward.

### Step 6 — Check cost and availability constraints

Verify that:

- the selected model is available,
- the selected effort is supported,
- the route does not create an unauthorized material charge,
- an organization/provider restriction has not silently substituted the model.

### Step 7 — Execute once with evidence

Do not pre-plan a chain of retries.

The first attempt should be credible enough to succeed.

### Step 8 — If it fails, diagnose the failure class before escalating

See the escalation matrix below.

---

## 10. Failure Classification Before Escalation

A failure does not automatically mean the model was too weak.

Classify the failure first.

### A. Context Failure

Symptoms:

- missing file or constraint,
- misunderstood project convention,
- worker lacked necessary evidence.

Action:

> Fix context/task packet. Do not upgrade model by default.

### B. Tool / Environment Failure

Symptoms:

- unavailable command,
- permission issue,
- broken dependency/environment,
- external service unavailable.

Action:

> Fix or work around the environment. Model escalation is usually irrelevant.

### C. Decomposition Failure

Symptoms:

- task too broad,
- too many concerns mixed together,
- unclear ownership,
- verification cannot isolate success.

Action:

> Re-scope or split the task before increasing capability.

### D. Depth Failure

Symptoms:

- model chose a plausible path but did not investigate enough,
- skipped relevant checks,
- stopped too early,
- reasoning was too shallow although the task was within capability.

Action:

> Raise effort within the same model first.

Example:

```text
Sonnet / medium
      ↓ depth failure
Sonnet / high
```

### E. Capability Failure

Symptoms:

- reasoning repeatedly misunderstands the core problem despite sufficient context,
- architecture/tradeoff synthesis is weak,
- causal reasoning remains poor after adequate effort,
- the model cannot maintain the required conceptual scope.

Action:

> Upgrade model family.

Example:

```text
Sonnet / high
      ↓ capability failure
Opus / high
```

### F. Horizon Failure

Symptoms:

- task exceeds practical single-worker horizon,
- repeated restarts lose important investigation state,
- very broad autonomous exploration is the dominant requirement.

Action:

> Consider Fable, or redesign the decomposition/handoff strategy.

---

## 11. Escalation Rules

Escalation MUST be evidence-driven.

### Rule 1 — No blind same-configuration retry

Do not rerun the same prompt with the same configuration unless new evidence, context, or a transient failure makes a different outcome reasonably likely.

### Rule 2 — Raise effort for depth, not capability

Use:

```text
medium → high → xhigh
```

when the model understands the problem but needs more exploration or verification.

### Rule 3 — Raise model for capability

Use:

```text
Haiku → Sonnet → Opus → Fable
```

only when the nature of the task requires more capability.

The ladder is conceptual; do not mechanically traverse every rung.

### Rule 4 — Do not jump to `max` without justification

`max` requires an explicit recorded reason tied to:

- unresolved critical difficulty,
- exceptional consequence,
- measured eval benefit,
- or explicit user intent.

### Rule 5 — Account for total expected cost

A stronger first route can be cheaper overall than:

```text
cheap attempt
→ failure
→ investigation
→ retry
→ review
→ rework
```

Optimize total workflow cost, not per-call price.

---

## 12. Downshift Rules

Routing should also move downward when appropriate.

Downshift when:

- the problem has become well understood after investigation,
- the remaining tasks are mechanical,
- acceptance criteria are deterministic,
- a high-capability PM has decomposed work into simple bounded packets,
- eval evidence shows a cheaper configuration preserves quality.

Example:

```text
Opus PM resolves architecture
        ↓
Sonnet / medium implementers execute bounded tasks
        ↓
Opus / high reviewer checks critical integration
```

This is a preferred pattern: expensive reasoning where it matters, cheaper execution where it does not.

---

## 13. Risk Overrides

Risk can raise routing even when implementation complexity is moderate.

Examples:

- authentication/authorization,
- security policy,
- production networking,
- data migration,
- destructive infrastructure operations,
- critical release logic.

For high-risk tasks, the PM SHOULD prefer stronger reasoning and/or independent review rather than relying on a low-cost implementation route alone.

Risk does not always mean the Implementer itself must be Opus. A valid route may be:

```text
Sonnet / medium implementer
        +
Opus / high independent reviewer
        +
PM verification
```

Choose where additional capability creates the most value.

---

## 14. Routing Examples

### Example A — Rename a Terraform variable in three files

Characteristics:

- low ambiguity,
- low reasoning complexity,
- deterministic verification.

Route:

```text
Implementer → Sonnet / low or medium
Reviewer    → not required by routing alone
PM          → inspect diff + validate
```

### Example B — Add a normal API endpoint with clear repository patterns

Characteristics:

- bounded implementation,
- moderate verification,
- low/medium risk.

Route:

```text
Implementer → Sonnet / medium
PM          → independent verification
Reviewer    → based on risk/quality policy
```

### Example C — Complex Helm/ArgoCD deployment change spanning multiple services

Characteristics:

- cross-component reasoning,
- meaningful operational risk,
- several verification layers.

Possible route:

```text
PM          → Sonnet / high or Opus / high
Implementer → Sonnet / high
Reviewer    → Opus / high
```

### Example D — Intermittent Kubernetes networking failure with unclear cause

Characteristics:

- high ambiguity,
- causal reasoning,
- distributed-system behavior.

Route:

```text
Debugger → Opus / high
```

Escalate to Opus / xhigh for insufficient investigation depth, or Fable / high when the investigation becomes long-horizon and system-wide.

### Example E — Large production outage with several plausible interacting causes

Characteristics:

- high ambiguity,
- broad scope,
- long investigation,
- expensive mistakes.

Possible route:

```text
PM / investigation lead → Fable / high
specialized bounded work → Sonnet or Opus as appropriate
critical review          → Opus / high
```

### Example F — Security-sensitive authentication design

Characteristics:

- high consequence,
- architecture judgment,
- subtle failure modes.

Route:

```text
PM / design reasoning → Opus / high or xhigh
Implementation        → Sonnet / high or Opus / high depending complexity
Reviewer              → Opus / high
```

### Example G — Generate a list of filenames matching a known pattern

Characteristics:

- simple,
- cheap to verify,
- no architectural reasoning.

Route:

```text
Haiku where appropriate, or built-in Explore
```

Do not spend Opus/Fable merely because the repository is large.

---

## 15. Built-In Agent Considerations

Claude Code includes built-in agents such as Explore and Plan.

Use them when they already solve the problem efficiently instead of duplicating the same behavior with a custom worker.

Exploration should often be isolated from the PM context when it will generate large search results or file contents.

Built-in agent model behavior may change with Claude Code versions. Methodology OS SHOULD rely on documented semantics rather than hard-coded historical assumptions.

---

## 16. Anti-Patterns

### Prestige Routing

Bad:

> This project is important, therefore use Fable everywhere.

Importance is not a model-selection dimension by itself.

### Technology Routing

Bad:

> Kubernetes always means Opus.

Route the actual task complexity and risk.

### Cheap-First Retry Spiral

Bad:

```text
Haiku
→ fail
→ Sonnet low
→ fail
→ Sonnet medium
→ fail
→ Opus
```

If the task is obviously complex, start at the appropriate tier.

### High-Effort Everywhere

Bad:

> Every worker runs at high/xhigh because quality matters.

Quality also comes from bounded tasks, good context, verification, and specialized review.

### Model Escalation for Missing Context

Bad:

> Worker did not know an unstated constraint, so use Opus.

Fix the context.

### Effort Escalation for Conceptual Failure

Bad:

> Sonnet repeatedly misunderstands the architecture, so set max.

If capability is the problem, use a stronger model.

### Dynamic PM Thrashing

Bad:

> Change PM effort every few turns.

Keep long-lived PM configuration stable where practical; put task-level variability into workers.

---

## 17. Routing Record

For Standard and Full Mode, the PM SHOULD be able to explain important non-default routing decisions concisely.

A routing note may contain:

```text
agent: debugger
model: opus
effort: high
reason: ambiguous cross-service failure requiring causal reasoning
```

Do not create verbose routing logs for obvious default choices.

Always record exceptional choices such as:

- Fable selected instead of Opus,
- `xhigh` or `max`,
- a material provider/model substitution,
- a route that introduces material usage-credit cost,
- deliberate downgrade despite elevated risk.

---

## 18. V0 Defaults

Until evals provide better evidence, use these defaults:

```text
PM — Standard:
  sonnet / high

PM — Full:
  opus / high

Implementer — normal bounded task:
  sonnet / medium

Implementer — difficult bounded task:
  sonnet / high

Reviewer — medium risk:
  sonnet / medium or high

Reviewer — high risk:
  opus / high

Debugger — localized:
  sonnet / high

Debugger — non-trivial / ambiguous:
  opus / high

Fable:
  reserved for hardest long-horizon / highly ambiguous autonomous work

max effort:
  exceptional and explicitly justified
```

These defaults are hypotheses to test, not permanent truths.

Step 13 evals MUST test whether lower-cost routes preserve the quality bar and whether stronger routes materially improve difficult workloads.

---

## 19. Testable Routing Invariants

A routing decision is healthy when the following are true:

1. The role was selected for responsibility, not prestige.
2. The model was selected based on required capability.
3. Effort was selected based on required depth.
4. Technology name alone did not determine the route.
5. Context/decomposition failures were fixed before unnecessary escalation.
6. A failed route was diagnosed before retrying.
7. `xhigh`, `max`, and Fable have explicit justification when used.
8. A cheaper configuration is preferred when evidence shows it preserves quality.
9. High-risk work receives sufficient verification even if implementation uses a cheaper model.
10. Material model substitutions or new usage-credit costs are not silently ignored.
11. The PM avoids unnecessary effort churn in its long-lived context.
12. Routing optimizes expected total workflow cost, not the cheapest individual request.

---

## 20. References and Version Sensitivity

This policy is designed around Claude Code's documented model aliases, subagent model/effort overrides, and Claude's effort parameter.

Relevant official documentation:

- Claude Code model configuration: https://code.claude.com/docs/en/model-config
- Claude Code custom subagents: https://code.claude.com/docs/en/sub-agents
- Claude Platform effort guidance: https://platform.claude.com/docs/en/build-with-claude/effort
- Claude model selection guidance: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model

Model availability, alias resolution, effort support, pricing, and recommended defaults can change.

Therefore:

> Treat current model details as runtime capabilities, while keeping the routing methodology stable.
