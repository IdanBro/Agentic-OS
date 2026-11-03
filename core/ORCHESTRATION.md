# Methodology OS — Project Lifecycle and Orchestration

This document defines the canonical lifecycle for work coordinated by Methodology OS.

It describes **how work moves through the system**. It does not define the detailed model-routing table, reviewer rules, context budgets, or escalation matrix; those belong to their dedicated policy files.

The Project Manager (PM) owns lifecycle progression and canonical project state.

---

## 1. Design Goals

The orchestration layer MUST:

1. Scale process depth to task complexity and risk.
2. Preserve high autonomy for routine work.
3. Avoid unnecessary agents, planning, reviews, and documents.
4. Keep execution work bounded and independently verifiable.
5. Preserve enough external state for another PM to continue.
6. Keep `main` human-gated.
7. Recover deliberately from failures instead of blindly retrying.
8. Support both engineering and non-engineering work.

The default philosophy is:

> Use the lightest workflow that still protects the required quality bar.

---

## 2. Lifecycle Modes

The PM MUST classify the work before choosing process depth.

### 2.1 Lite Mode

Use when the work is small, low-risk, well understood, and can be completed safely without multi-agent orchestration.

Typical characteristics:

- one bounded outcome,
- few files or one localized artifact,
- no significant architecture decision,
- low ambiguity,
- low blast radius,
- verification is simple.

Default behavior:

```text
INTAKE
  ↓
TRIAGE
  ↓
EXECUTE
  ↓
VERIFY
  ↓
COMPLETE
```

Lite Mode MAY execute in the PM/main session without a worker if delegation would cost more context or coordination than it saves.

Lite Mode still obeys the Constitution, especially evidence-before-completion and the `main` gate.

---

### 2.2 Standard Mode

Use for normal multi-step work with moderate complexity or risk.

Typical characteristics:

- multiple implementation steps,
- several relevant files or components,
- meaningful verification,
- moderate risk,
- delegation can reduce context load or improve specialization.

Default behavior:

```text
INTAKE
  ↓
TRIAGE
  ↓
PLAN
  ↓
PREPARE
  ↓
EXECUTE TASK LOOP
  ↓
VERIFY
  ↓
OPTIONAL REVIEW
  ↓
INTEGRATE
  ↓
COMPLETE
```

This is the default Methodology OS workflow for most engineering project work.

---

### 2.3 Full Mode

Use for large, high-risk, ambiguous, long-running, or highly parallel work.

Typical characteristics:

- architecture or system-wide changes,
- high-risk production impact,
- substantial ambiguity,
- many dependent tasks,
- multiple domains or specialists,
- likely long context growth,
- work that benefits materially from parallelism.

Default behavior:

```text
INTAKE
  ↓
TRIAGE
  ↓
INVESTIGATE (when needed)
  ↓
STRUCTURED PLAN
  ↓
HUMAN GATE (when required)
  ↓
PREPARE
  ↓
EXECUTE / VERIFY / REVIEW LOOPS
  ↓
PHASE INTEGRATION
  ↓
SYSTEM VERIFICATION
  ↓
INTEGRATE
  ↓
COMPLETE OR PREPARE MAIN PROMOTION
```

Full Mode MAY use multiple workers or coordinated parallel execution when task independence and expected benefit justify the added complexity.

---

## 3. Activation Rules

Methodology OS SHOULD activate when at least one of the following is true:

- the user explicitly requests Methodology OS,
- the work contains multiple dependent stages,
- the task is materially ambiguous,
- the task is medium or high risk,
- the expected work will generate substantial exploration, logs, or tool output,
- the work is expected to span a long session,
- independent execution/review would materially improve quality,
- the work requires structured state or handoff.

Methodology OS SHOULD NOT force Standard or Full Mode onto trivial work merely because the capability exists.

---

## 4. Canonical State Machine

The PM owns the following lifecycle states.

```text
INTAKE → TRIAGE → [INVESTIGATE] → PLAN → [HUMAN GATE] → PREPARE
                                                      ↓
                                               EXECUTE TASK
                                                      ↓
                                                   VERIFY
                                              ┌───────┴───────┐
                                            pass             fail
                                              │                │
                                              ▼                ▼
                                         [REVIEW]          DIAGNOSE
                                              │            ┌───┴────┐
                                              │          FIX      REPLAN
                                              │            │         │
                                              └────────────┴─────────┘
                                                           ↓
                                                     EXECUTE TASK

When all required tasks pass: INTEGRATE → SYSTEM CHECK → COMPLETE.

If progress cannot responsibly continue: BLOCKED.
`BLOCKED` never transitions to `COMPLETE` without first being resolved.
```

`HANDOFF` is a side transition that may occur from any long-running state when the PM context is no longer efficient or reliable.

---

## 5. State Definitions

### 5.1 INTAKE

Purpose: understand the requested outcome before deciding how to work.

The PM MUST identify, as far as the available information allows:

- desired outcome,
- explicit constraints,
- relevant repository/project context,
- success criteria,
- user-defined boundaries,
- whether the task is engineering or another work domain.

The PM SHOULD resolve ambiguity through inspection before asking the user when the answer can be derived safely from the project or available evidence.

Exit condition:

> The requested outcome is sufficiently understood to classify the work.

---

### 5.2 TRIAGE

Purpose: choose the appropriate operating mode and initial execution strategy.

The PM evaluates:

- complexity,
- ambiguity,
- risk/blast radius,
- reversibility,
- dependencies,
- expected context volume,
- parallelizability,
- verification difficulty.

The PM selects:

- Lite / Standard / Full Mode,
- whether investigation is needed before planning,
- whether a human gate is already required,
- whether Git/project state must be initialized.

The detailed model and effort selection is governed by `ROUTING.md`.

Exit condition:

> Operating mode and next lifecycle state are explicit.

---

### 5.3 INVESTIGATE

Purpose: reduce uncertainty before committing to a plan or implementation.

Use when important facts are unknown or assumptions would materially affect the solution.

Investigation SHOULD be read-only unless a controlled experiment is explicitly justified.

Typical investigation outputs:

- relevant architecture facts,
- repository map,
- dependency relationships,
- hypotheses,
- constraints discovered from code/configuration,
- unresolved questions,
- recommendation for planning.

High-volume exploration SHOULD be delegated when doing so keeps disposable search/log context out of the PM session.

Exit condition:

> Uncertainty has been reduced enough to create a defensible plan, or the PM has identified a true blocker requiring escalation.

---

### 5.4 PLAN

Purpose: convert the outcome into an executable structure.

Planning depth MUST scale with complexity.

A plan MAY contain:

- phases,
- tasks,
- dependencies,
- acceptance criteria,
- risk classification,
- verification strategy,
- integration strategy,
- identified human gates.

Tasks intended for delegation MUST be bounded enough to become Task Packets.

The PM SHOULD avoid prematurely specifying implementation details that are better decided by the worker within its granted authority.

Exit condition:

> There is a viable path from current state to the requested outcome, with enough structure to begin safely.

---

### 5.5 HUMAN GATE

Purpose: preserve user authority over high-impact decisions.

A Human Gate occurs only when required by the Constitution or `ESCALATION_POLICY.md`.

The PM SHOULD present:

1. the decision to be made,
2. the recommended option,
3. meaningful alternatives,
4. material tradeoffs,
5. the consequence of delaying the decision.

The PM MUST NOT use Human Gates for routine implementation preferences merely to transfer responsibility back to the user.

Exit condition:

> Required approval or direction has been received, or the project becomes BLOCKED.

---

### 5.6 PREPARE

Purpose: create a safe execution environment before implementation begins.

For engineering repositories, the PM MUST inspect repository state before modification.

Default Git preparation:

1. identify repository conventions and current branch,
2. confirm the intended integration branch (`dev` by default under this OS),
3. avoid modifying an unrelated dirty working tree,
4. synchronize safely when appropriate,
5. create or select a dedicated working branch,
6. use a worktree when isolation materially benefits parallel or risky work.

Default branch intent:

```text
working branch
    ↓
verification / review
    ↓
dev
    ↓
main only with explicit user approval
```

Branch naming conventions will be defined in the Git-specific operating policy when added.

For non-engineering work, PREPARE means initializing the required project artifacts, files, research workspace, or other execution environment.

Exit condition:

> Work can begin without violating project-state or branch-safety requirements.

---

## 6. The Task Execution Loop

Standard and Full Mode operate primarily through a task loop.

```text
SELECT READY TASK
       ↓
BUILD TASK PACKET
       ↓
SELECT EXECUTION STRATEGY
       ↓
EXECUTE
       ↓
WORKER SELF-VERIFY
       ↓
WORK REPORT
       ↓
PM INDEPENDENT VERIFY
       ↓
RISK-BASED REVIEW
       ↓
ACCEPT / FIX / REPLAN
       ↓
UPDATE STATE
       ↓
NEXT READY TASK
```

### 6.1 Select Ready Task

A task is ready when:

- required dependencies are satisfied,
- required approvals are present,
- sufficient context is available,
- executing it will not knowingly conflict with another active task.

Prefer the task that best advances the critical path unless parallelism or risk reduction provides a better reason.

---

### 6.2 Build Task Packet

Delegated execution MUST use a bounded Task Packet.

A Task Packet SHOULD contain only the information required for the task, including where applicable:

- objective,
- rationale,
- scope,
- explicit out-of-scope boundaries,
- acceptance criteria,
- relevant files/components,
- project conventions,
- required verification,
- expected report format.

Detailed schema is defined by `templates/TASK_PACKET.md`.

---

### 6.3 Select Execution Strategy

The PM chooses among:

- execute directly in the PM session,
- delegate to one specialized worker,
- delegate independent tasks in parallel,
- invoke a debugger/investigator,
- use a coordinated team only when the coordination benefit exceeds its overhead.

Delegation is a tool, not a requirement.

The PM SHOULD delegate when one or more of the following are true:

- execution would add substantial disposable context,
- a specialized prompt/skill materially improves results,
- independent context reduces anchoring,
- parallel execution provides meaningful value,
- the PM should preserve its context for orchestration.

The PM SHOULD execute directly when delegation would add unnecessary coordination overhead to a small bounded task.

---

### 6.4 EXECUTE

The worker executes only within the granted task scope and authority.

A worker MAY make routine implementation decisions required to satisfy the Task Packet.

A worker MUST stop and report rather than silently expand scope when it discovers:

- a required high-impact decision,
- a contradiction in project requirements,
- a blocker outside its authority,
- evidence that the planned task is unsafe or based on a false assumption.

---

### 6.5 Worker Self-Verification

Before returning completion, the worker MUST verify its own work using the checks specified in the Task Packet plus any obviously necessary domain checks discovered during execution.

The worker MUST distinguish:

- checks actually executed,
- observed results,
- checks not executed,
- remaining uncertainty.

A claim of success without evidence is not a valid Work Report.

---

### 6.6 Work Report

The worker returns a concise report containing, where applicable:

- outcome,
- files/artifacts changed,
- important implementation decisions,
- verification executed and results,
- unresolved concerns,
- deviations from the Task Packet,
- recommended follow-up if needed.

The Work Report is a communication artifact, not canonical proof. The PM verifies independently.

---

## 7. PM Independent Verification

After every delegated task, the PM MUST independently verify enough of the result to support acceptance.

Verification depth scales with risk but is never zero.

The PM SHOULD prefer direct evidence such as:

- diff inspection,
- targeted tests,
- lint/static validation,
- rendered configuration,
- build execution,
- runtime behavior,
- inspection of generated artifacts.

The PM MUST NOT merely restate the worker's report as verification.

If PM verification fails, transition to `DIAGNOSE`.

If PM verification passes, determine whether independent review is required before integration.

Detailed quality-gate requirements are defined in `QUALITY_GATES.md`.

---

## 8. REVIEW

Independent review is risk-based.

The reviewer SHOULD evaluate the actual project state against requirements without being unnecessarily anchored by the implementer's reasoning.

The reviewer SHOULD receive:

- goal/requirements,
- acceptance criteria,
- relevant repository or artifact state,
- appropriate project conventions.

The reviewer SHOULD NOT require the complete worker transcript unless it is directly relevant.

Possible review results:

- `PASS` — acceptable to integrate,
- `PASS_WITH_NOTES` — acceptable, with non-blocking observations,
- `CHANGES_REQUIRED` — return to execution,
- `REPLAN_REQUIRED` — implementation exposed a problem with the plan,
- `ESCALATE` — a high-impact unresolved decision requires the user.

---

## 9. Failure Recovery

Failure is part of the lifecycle and MUST produce new information.

### 9.1 DIAGNOSE

When execution, verification, or review fails, the PM first determines what kind of failure occurred:

- implementation defect,
- incorrect assumption,
- incomplete context,
- wrong task decomposition,
- environment/tooling issue,
- model capability issue,
- insufficient reasoning/verification depth,
- external blocker,
- requirement conflict.

The PM MUST NOT repeatedly retry the same approach without a changed hypothesis or new evidence.

---

### 9.2 FIX IN PLACE

Use when the plan remains valid and the defect is localized.

```text
DIAGNOSE
   ↓
corrective Task Packet
   ↓
EXECUTE
   ↓
VERIFY
```

---

### 9.3 REPLAN

Use when new evidence invalidates material assumptions, dependencies, task boundaries, or the chosen approach.

Replanning SHOULD preserve valid completed work and avoid restarting from zero without reason.

Material plan changes MAY trigger a Human Gate if they cross escalation thresholds.

---

### 9.4 BLOCKED

Enter BLOCKED when progress depends on unavailable information, external access, unresolved human authority, or another condition the PM cannot responsibly resolve.

The PM MUST record:

- blocker,
- evidence,
- impact,
- what was attempted,
- exact action required to unblock.

A blocked project is not complete.

---

## 10. Parallel Execution

Parallelism is optional and must justify its coordination cost.

Parallel execution SHOULD be considered when tasks:

- are truly independent or have clear boundaries,
- do not contend for the same mutable state,
- benefit materially from elapsed-time reduction or context isolation,
- can be integrated deterministically.

Parallel execution SHOULD be avoided when:

- tasks modify overlapping files or architecture,
- one task depends on findings from another,
- integration risk exceeds the expected benefit,
- the work is too small to justify coordination.

For engineering work, isolated worktrees or equivalent isolation SHOULD be preferred when multiple workers modify the repository concurrently.

The PM remains responsible for integration and conflict resolution strategy.

---

## 11. INTEGRATE

Integration occurs only after required execution, PM verification, and review gates pass.

For engineering work, the PM SHOULD:

1. inspect the final diff,
2. ensure logical commits are clean and appropriately scoped,
3. run required pre-integration checks,
4. open or update a PR from the working branch into `dev` when the repository has a remote PR workflow,
5. merge the verified working branch/PR into `dev` when permitted by repository rules,
6. verify the integrated `dev` state when the change is significant,
7. update canonical project state.

The PM MAY autonomously integrate verified work into `dev` unless a repository-specific rule or explicit user instruction says otherwise. If no remote PR workflow exists, local branch integration is acceptable.

For promotion to `main`, the PM SHOULD prepare a `dev` → `main` PR when the repository supports PRs, but MUST NOT merge it without explicit user approval.

When the user has not approved a `main` promotion, the furthest autonomous lifecycle state is:

> verified and integrated in `dev`, with main promotion prepared if appropriate.

---

## 12. Project Completion

The PM MAY declare the requested work complete only when:

- requested outcome is satisfied,
- applicable acceptance criteria pass,
- required task verification is complete,
- required independent reviews are resolved,
- integration state is correct,
- no known critical blocker remains,
- canonical state and important decisions are current,
- any required human-gated action is clearly distinguished from completed autonomous work.

For engineering work where the requested final state is production/main but user approval is still pending, the PM MUST report:

> Implementation complete; main promotion pending explicit user approval.

It MUST NOT mislabel this as fully deployed/released if that has not occurred.

---

## 13. Handoff

`HANDOFF` is an operational transition, not a failure state.

The PM SHOULD initiate handoff when continuing in the current context is likely to reduce quality or efficiency, including when:

- the PM context contains substantial obsolete detail,
- repeated compaction would remove important distinctions,
- the project spans many phases,
- another PM/session needs to continue,
- context selection has become harder than reconstructing from curated state.

Before handoff, the PM MUST ensure project artifacts capture enough current truth for continuation.

The handoff SHOULD include:

- goal,
- current lifecycle state,
- completed work,
- active/incomplete work,
- key decisions,
- important files/artifacts,
- verification status,
- known risks/blockers,
- failed approaches worth preserving,
- exact recommended next action.

The replacement PM SHOULD validate the handoff against current project state before continuing.

---

## 14. Canonical Project Artifacts

Standard/Full projects SHOULD maintain external state artifacts as needed.

Recommended artifacts:

| Artifact | Purpose |
|---|---|
| `PROJECT_BRIEF.md` | Stable definition of outcome and constraints |
| `PLAN.md` | Current execution structure and dependencies |
| `STATE.md` | Concise current truth and next action |
| `DECISIONS.md` | Durable decisions and rationale |
| `TASK_PACKET.md` | Contract for bounded delegated work |
| `WORK_REPORT.md` | Worker result and verification evidence |
| `HANDOFF.md` | Curated session-to-session continuity |

These files SHOULD NOT all be created for every task.

Artifact creation must satisfy Constitution P13 and P15: documentation and complexity must earn their cost.

Detailed templates are defined under `templates/`.

---

## 15. Required State Updates

The PM SHOULD update canonical state at meaningful lifecycle boundaries rather than after every tool call.

Recommended update points:

- after initial plan approval/commitment,
- after a task or phase is accepted,
- after a durable decision,
- after discovery of a meaningful blocker/risk,
- after material replanning,
- after integration,
- before handoff,
- at project completion.

State updates SHOULD describe current truth, not chronological activity.

---

## 16. Engineering Git Lifecycle

Unless project-specific rules override it, engineering work follows:

```text
             user objective
                   ↓
             inspect repo
                   ↓
             classify/plan
                   ↓
          working branch created
                   ↓
        implementation task loop
                   ↓
        verification + review
                   ↓
           logical commits
                   ↓
             PR / integrate
                   ↓
                  dev
                   ↓
        integrated verification
                   ↓
         main promotion prepared
                   ↓
          EXPLICIT USER APPROVAL
                   ↓
                 main
```

Rules:

- no direct development on `main`,
- no autonomous merge to `main`,
- routine verified branch integration into `dev` is allowed by default,
- project-specific branch protection and PR rules take precedence,
- destructive Git operations require caution and may require escalation.

---

## 17. Non-Engineering Lifecycle

For research, writing, planning, analysis, and other non-code work, the same lifecycle semantics apply without forcing Git-specific mechanics.

Example:

```text
INTAKE
  ↓
TRIAGE
  ↓
PLAN / INVESTIGATE
  ↓
EXECUTE bounded research/writing tasks
  ↓
VERIFY evidence / requirements
  ↓
REVIEW when risk or quality warrants it
  ↓
INTEGRATE into final artifact
  ↓
COMPLETE
```

The OS core remains domain-neutral; domain-specific skills define the appropriate quality checks.

---

## 18. PM Decision Order

At every lifecycle transition, the PM SHOULD reason in this order:

1. **What outcome must be true next?**
2. **What evidence will prove it?**
3. **What is the smallest safe unit of work?**
4. **Does this need delegation?**
5. **What context is actually required?**
6. **What capability/effort is justified?**
7. **What could make this unsafe or require human authority?**
8. **What state must survive after this step?**

This order intentionally places outcome, evidence, and task boundaries before model/tool selection.

---

## 19. Anti-Patterns

The PM MUST avoid the following patterns:

### Ceremony-First Orchestration
Creating a plan, worker, reviewer, task file, and handoff for a trivial task.

### Vague Delegation
Sending a worker a broad responsibility with no bounded outcome or acceptance criteria.

### Worker-Report Trust
Accepting `tests pass` or `done` without PM evidence.

### Context Dumping
Passing full project history because context selection was not performed.

### Premature Parallelism
Spawning multiple agents before dependencies and write boundaries are understood.

### Infinite Retry
Repeating similar attempts without new evidence or a revised hypothesis.

### Silent Scope Expansion
Allowing execution to grow beyond the approved objective without recognizing the change.

### Approval Spam
Asking the user to approve routine choices that fall within PM authority.

### Autonomous Main Promotion
Merging or pushing a change into `main` without explicit approval.

### Transcript State
Treating session history as the canonical representation of project status.

---

## 20. Orchestration Invariants

A valid Methodology OS run must preserve all of the following:

1. Workflow depth is proportional to complexity and risk.
2. Every delegated task is bounded.
3. Every worker self-verifies.
4. Every delegated task receives independent PM verification.
5. Required reviewers are independent enough to provide meaningful challenge.
6. Failed attempts produce diagnosis or new evidence before repetition.
7. Canonical state remains resumable for significant work.
8. High-impact decisions remain human-gated.
9. `main` remains human-gated.
10. Added orchestration complexity has a concrete purpose.

---

## 21. Relationship to Other Policies

This document owns **workflow progression**.

Detailed behavior is delegated to:

- `PRINCIPLES.md` — constitutional invariants,
- `ROUTING.md` — model, effort, and execution routing,
- `QUALITY_GATES.md` — risk levels and verification/review requirements,
- `CONTEXT_POLICY.md` — context selection, retention, and handoff thresholds,
- `ESCALATION_POLICY.md` — exact human escalation triggers,
- `LEARNING_POLICY.md` — retrospectives and OS-learning candidates,
- `templates/*` — canonical artifact schemas.

When detailed policy is not yet implemented, this orchestration document provides the default V0 behavior.
