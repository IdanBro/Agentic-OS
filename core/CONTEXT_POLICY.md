# Methodology OS — Context Architecture

This document defines how Methodology OS selects, transfers, retains, isolates, and discards context across the Project Manager and delegated agents.

The objective is not to give every agent all available information. The objective is to give each agent the **minimum sufficient context** required to do its job professionally, while keeping durable project truth outside any single conversation.

The Project Manager owns context routing and context hygiene.

---

## 1. Core Principle

> Context is a working set, not an archive.

Every item placed into an agent context has a recurring cost: it competes for attention, consumes tokens, can anchor later reasoning, and may survive for many turns or through compaction.

Therefore:

1. include information because it is needed, not because it exists;
2. prefer references to repository-accessible content over copied content;
3. isolate verbose exploration, logs, and implementation detail in workers;
4. return conclusions and evidence, not transcripts;
5. persist durable project truth in canonical artifacts rather than conversation history;
6. create a fresh context when accumulated history becomes more harmful than useful.

---

## 2. Context Classes

Methodology OS distinguishes five context classes.

### 2.1 Constitutional Context

Rules that should apply broadly across work.

Examples:

- Methodology OS principles,
- global human gates,
- stable personal workflow rules,
- project-wide conventions that every relevant agent must respect.

Constitutional context should be concise because it is frequently loaded.

Put multi-step procedures, detailed reference material, or task-specific knowledge elsewhere.

### 2.2 Durable Project Context

Information that remains useful across phases or sessions.

Examples:

- project objective,
- current architecture at the level necessary for future work,
- accepted constraints,
- important decisions and rationale,
- current project state,
- unresolved risks,
- verified commands or conventions that cannot be derived cheaply.

Durable project context belongs in canonical project artifacts such as `PROJECT_BRIEF.md`, `STATE.md`, `DECISIONS.md`, and `HANDOFF.md`, not only in chat history.

### 2.3 Task Context

Information required to complete one bounded unit of work.

Examples:

- objective,
- scope,
- acceptance criteria,
- relevant file paths,
- interfaces or dependencies,
- required verification,
- authority boundaries.

Task context is the normal payload passed from PM to worker.

### 2.4 Ephemeral Execution Context

High-volume or short-lived information generated while doing the work.

Examples:

- search output,
- build logs,
- stack traces,
- command output,
- raw API responses,
- temporary hypotheses,
- intermediate file contents,
- failed experiments that have no continuing value.

Ephemeral context SHOULD remain inside the worker that needs it and SHOULD NOT be promoted into PM context unless it changes a decision, risk, project state, or next action.

### 2.5 Evidence Context

Compact proof supporting a claim.

Examples:

- exact command plus pass/fail result,
- short relevant error excerpt,
- changed-file list,
- test counts,
- validation result,
- commit SHA,
- PR number,
- a precise file/line reference.

Evidence is preferred over raw execution transcript.

---

## 3. Context Ownership by Role

### 3.1 Project Manager

The PM should retain the smallest working set that allows it to coordinate the entire project.

PM context SHOULD contain:

- requested outcome,
- important user constraints,
- current lifecycle mode and phase,
- high-level plan and dependencies,
- canonical current state,
- important decisions,
- risk and escalation status,
- compact worker conclusions,
- compact verification evidence,
- Git/integration state,
- references to canonical artifacts.

PM context SHOULD NOT accumulate:

- entire source files that workers can read themselves,
- full test/build logs,
- long repository searches,
- repeated command output,
- every worker reasoning step,
- complete worker transcripts,
- obsolete plans,
- low-value chronological history.

The PM's value is coordination and judgment. Its context should reflect that role.

### 3.2 Implementer

The Implementer receives a bounded task packet plus access to the repository/artifacts required to execute it.

Prefer giving:

- objective,
- why the task matters when that changes implementation choices,
- explicit scope,
- out-of-scope boundaries when useful,
- acceptance criteria,
- relevant paths/interfaces,
- required verification,
- authority limits.

Do not copy large file bodies into the task packet when the worker can read those files directly.

Do not send unrelated project history.

The Implementer may discover additional local context itself. That exploration belongs in its own context unless the result affects project-level state.

### 3.3 Reviewer

Reviewer context must preserve independence.

First-pass reviewer context SHOULD contain:

- intended outcome,
- acceptance criteria,
- relevant constraints,
- risk classification,
- actual diff/current artifact/repository references,
- required quality gates.

First-pass reviewer context SHOULD NOT contain, unless necessary:

- the Implementer's reasoning narrative,
- the Implementer's confidence statement,
- suggested verdict,
- long implementation report.

After the independent pass, the PM MAY provide the worker report to reconcile discrepancies or verify claimed checks.

For a re-review after fixes, provide the prior material findings that must be closed, but avoid carrying unrelated previous commentary.

### 3.4 Debugger

Debugger context should start from observable behavior rather than a preferred theory.

Provide:

- expected behavior,
- observed behavior,
- reproduction information when known,
- short relevant error/log evidence,
- environment facts that may affect the failure,
- affected scope,
- prior failed approaches only when repeating them would be costly or misleading.

Do not dump all logs by default. Point the Debugger to where logs or artifacts can be obtained and let it select what it needs.

Do not present the PM's favored root-cause theory as fact.

---

## 4. Fresh Subagents Are the Default Isolation Boundary

A normal custom subagent starts with a fresh context and receives a delegation message rather than the PM's conversation history.

Methodology OS SHOULD exploit this deliberately.

Use a fresh worker when:

- the task is self-contained enough to describe as a bounded outcome;
- exploration or execution will create verbose output;
- independent reasoning is valuable;
- old PM history would create anchoring or noise;
- only a compact result needs to return.

The PM MUST assume that a fresh worker has **not** seen:

- previous conversation turns,
- files the PM already read,
- previously invoked skills,
- worker transcripts from other agents.

If information matters, include it in the task packet or give a reference the worker can access.

---

## 5. Do Not Duplicate Automatically Loaded Context

Custom Claude Code subagents already receive environment-provided context such as the applicable `CLAUDE.md` hierarchy and a Git-status snapshot.

Therefore the PM SHOULD NOT paste global/project instructions into every task packet merely to be safe.

Instead:

- task packets contain task-specific deltas;
- global behavior lives in the global Methodology OS layer;
- project-wide conventions live in the project's Claude configuration where appropriate;
- domain procedures live in skills;
- durable project state lives in canonical state artifacts.

Important caveat: a worker's initial Git-status snapshot can reflect the parent session start rather than the latest repository state. When current Git state matters, the worker or PM MUST query it explicitly rather than trusting the startup snapshot.

Built-in Explore and Plan agents intentionally load less project startup context than normal custom agents. Do not assume they have read project `CLAUDE.md` instructions; use them for discovery/research, then apply project rules in the PM before making decisions.

---

## 6. Reference First, Copy Only When Necessary

When an agent can access a file, artifact, URL, commit, PR, or repository object directly, prefer a reference.

Prefer:

```text
Inspect `src/auth/session.ts` and `tests/auth/session.test.ts`.
```

Over:

```text
Here are 600 lines copied from both files...
```

Prefer:

```text
Review the diff from base `dev` to the current task branch.
```

Over pasting the complete diff into the delegation message when the reviewer can obtain it itself.

Copy content into the task packet only when:

- the worker cannot access the source directly;
- the exact snapshot must be frozen for correctness;
- the relevant fragment is very small and copying is cheaper than rediscovery;
- external information may disappear or change during the task;
- the copied excerpt itself is the required evidence.

When copying, include only the smallest useful fragment.

---

## 7. Discovery Should Happen Close to Execution

The PM SHOULD avoid reading large portions of a repository only to explain them again to a worker.

Preferred pattern:

```text
PM identifies task boundary
        ↓
worker receives paths / search target
        ↓
worker explores locally
        ↓
worker implements or reports
        ↓
PM receives compact result
```

For broad codebase discovery, use a read-only exploration context when that avoids flooding the PM.

Promote only findings that affect:

- plan,
- scope,
- dependency graph,
- architecture,
- risk,
- acceptance criteria,
- project state.

---

## 8. Worker Output Contract — Compress at the Boundary

A worker response to the PM is a context boundary.

By default, the worker SHOULD return:

1. **Status** — `DONE`, `BLOCKED`, `PARTIAL`, or role-specific verdict.
2. **Outcome** — what changed or what was concluded.
3. **Files / artifacts** — concise references, not content dumps.
4. **Verification evidence** — checks actually run and results.
5. **Decisions / assumptions** — only material ones.
6. **Residual risk / uncertainty** — what remains unproven.
7. **Recommended next action** — only when useful.

Do not return:

- full command histories,
- complete logs,
- exhaustive search results,
- lengthy self-narration,
- unchanged file content,
- repeated task instructions.

If raw evidence is needed later, preserve its location and return a reference.

A concise report that omits a material failure is bad compression. Compression must preserve decision-relevant information.

---

## 9. PM Intake of Worker Results

The PM SHOULD NOT blindly retain every worker result verbatim.

For each returned result, classify information as:

### Retain in PM working context

- completion state,
- material finding,
- verified evidence,
- blocker,
- risk,
- decision requiring action,
- next dependency.

### Persist to canonical project state

- durable decision,
- completed milestone,
- unresolved issue,
- changed architecture,
- handoff-critical fact.

### Leave in worker transcript / artifact

- raw logs,
- intermediate hypotheses,
- detailed exploration,
- redundant explanation.

The PM should summarize once and refer back rather than repeatedly restating the same result.

---

## 10. Resume an Agent vs Spawn a Fresh Agent

Resume an existing worker when:

- the same bounded task continues;
- its accumulated local exploration is still valuable;
- the follow-up depends heavily on details already discovered;
- independence is not required.

Spawn a fresh worker when:

- starting a new bounded task;
- independent review is required;
- prior reasoning may anchor the next analysis;
- the previous worker context is noisy or dominated by failed approaches;
- the new task can be described more cheaply than restoring old context.

Do not resume an Implementer as the independent Reviewer of its own work.

Do not resume a Debugger merely because it is available if a fresh independent diagnosis would reduce anchoring after an uncertain conclusion.

---

## 11. Fork Policy

A fork inherits the parent's full conversation history. This can save re-explanation and reuse shared context, but it sacrifices the input isolation of a fresh worker.

Fresh non-fork subagents are the default Methodology OS worker mechanism.

Use a fork only when:

- the side task genuinely requires a large fraction of the PM's existing conversation;
- summarizing that background accurately would itself be expensive or lossy;
- the task benefits from trying an alternate approach from the exact same starting state;
- preserving prompt-cache reuse materially outweighs the cost of inheriting history.

Avoid a fork when:

- independent review is required;
- old reasoning may anchor the worker;
- the PM context is already polluted;
- the task can be described with a small task packet;
- the purpose of delegation is specifically to escape accumulated context.

A fork may keep tool-call noise out of the PM after it starts, but it does not provide a clean initial reasoning context.

---

## 12. Skill Loading Policy

Skills are context, not free metadata.

The full body of a preloaded skill is injected into a subagent at startup. A skill loaded into the main conversation also remains in context across turns.

Therefore:

- preload only skills the worker is very likely to need throughout the task;
- do not attach large skill bundles by role by default;
- prefer discoverable/on-demand skills when relevance is uncertain;
- keep skill bodies concise;
- separate reference knowledge from long procedural workflows;
- do not duplicate the same instruction in CLAUDE.md, agent prompt, task packet, and skill unless enforcement genuinely requires repetition.

Detailed skill architecture is defined in the dedicated Skills stage. This policy governs only context cost.

---

## 13. CLAUDE.md Policy

`CLAUDE.md` content is persistent context and should earn its recurring cost.

Use it for facts and rules an agent should hold in most relevant sessions, such as:

- stable project conventions,
- build/test entry points,
- key repository layout,
- short non-negotiable workflow constraints.

Move content elsewhere when it is:

- a multi-step procedure → Skill;
- relevant only to a path/domain → scoped rule or skill;
- current project progress → STATE;
- a decision history → DECISIONS;
- a one-task instruction → TASK_PACKET;
- a temporary lesson → retrospective/learning candidate.

Global `~/.claude/CLAUDE.md` MUST remain a small kernel. It must not import the full Methodology OS policy corpus into every session.

---

## 14. Auto Memory Is Not Canonical Project State

Auto memory can preserve useful learnings, but Methodology OS MUST NOT depend on it as the authoritative record of:

- current project state,
- approved plan,
- completion status,
- architecture decisions,
- user approvals,
- required next step.

Canonical project artifacts remain the source of truth because they are explicit, reviewable, versionable, and suitable for handoff.

Auto memory may complement them with stable learned patterns where appropriate.

---

## 15. State Externalization

When information is needed beyond the current conversational phase, move it out of transient conversation into the correct durable artifact.

The PM SHOULD externalize:

- project objective and constraints,
- current plan,
- completed/pending work,
- important decisions,
- blockers and risks,
- verification status,
- next action.

Do not externalize every event.

The state layer should answer:

> What must a competent new PM know to continue correctly?

The detailed schemas for these artifacts are defined in Step 7.

---

## 16. Context Health Checks

The PM should periodically evaluate context health, especially after large phases, debugging sessions, repeated failures, or several worker returns.

Warning signs include:

- old implementation detail repeatedly reappearing despite no longer being relevant;
- difficulty distinguishing current state from superseded plans;
- repeated summaries of the same worker output;
- many large tool results in the PM history;
- compaction occurring while substantial work still remains;
- decisions depending on facts that exist only deep in conversation history;
- the PM needing to reread its own earlier exploration to know what is true;
- conflicting versions of state in the conversation.

When these appear, do not respond by adding another large summary to the same context indefinitely.

Instead:

1. reconcile the canonical project state;
2. persist durable decisions and unresolved items;
3. create a structured handoff if meaningful work remains;
4. continue in a fresh PM context when the clean-context benefit exceeds handoff cost.

Do not wait for the context window to be technically exhausted.

---

## 17. Compaction Policy

Claude Code can compact main and subagent conversations automatically. Compaction is useful but is not a substitute for context architecture.

Methodology OS MUST NOT assume that every pre-compaction detail will retain equal salience afterward.

Before or after material compaction during long work, ensure that durable truth is already represented in canonical artifacts.

Never rely on conversation compaction as the sole persistence mechanism for:

- approvals,
- architectural decisions,
- unresolved blockers,
- task completion state,
- next-step ownership.

A worker that compacted successfully can continue its bounded task. A PM whose context has compacted repeatedly during a long-running project should consider handoff if the remaining work is substantial.

---

## 18. Handoff Trigger

Create a PM handoff when one or more of these is true:

- the remaining project horizon is substantial and current PM context is noisy;
- multiple compactions or major phase transitions have reduced confidence in context cleanliness;
- the PM is carrying large amounts of obsolete implementation history;
- state reconstruction from the conversation is becoming difficult;
- a natural phase boundary makes a fresh PM cheaper than continuing;
- the user intentionally moves work to another session/account/environment.

Do not hand off merely because the session is old.

Do not hand off a five-minute remaining task if the handoff would cost more than finishing safely.

The handoff should contain curated durable state, not a transcript summary.

---

## 19. High-Volume Operations

The following operations SHOULD normally happen outside PM context when they are expected to be verbose:

- broad repository search,
- large log investigation,
- dependency inventory,
- test-suite failure analysis,
- large diff inspection,
- documentation corpus research,
- data exploration,
- multi-file implementation,
- repeated experimental commands.

Delegate them to a bounded worker or exploration context and request a compact result.

Exception: keep the work in the PM when the raw detail must be repeatedly referenced across several tightly coupled phases and delegation would create more context reconstruction than it saves.

---

## 20. Context Budget by Workflow Mode

Context discipline scales with workflow mode, not by fixed token quotas.

### Lite

- PM may execute directly.
- Avoid creating a worker solely for theoretical context savings.
- Keep the task local and finish quickly.

### Standard

- PM keeps plan/state/dependencies.
- Implementation and verbose exploration are delegated when beneficial.
- Worker reports are compact.
- Externalize durable state at meaningful milestones.

### Full

- Strong separation between orchestration and execution.
- Prefer dedicated exploration/debug/review contexts.
- Maintain canonical state continuously enough to support replacement PM.
- Use phase boundaries for context pruning and possible handoff.
- Consider separate sessions for work whose duration or parallelism exceeds a single context lifecycle.

The OS intentionally avoids hard-coded token thresholds because model context sizes and product behavior may change. Evals may later justify measured thresholds.

---

## 21. Context Packaging Checklist

Before delegating, the PM should be able to answer:

1. What exact outcome does this worker own?
2. What information is necessary to make correct decisions?
3. Which information can the worker discover itself?
4. Which content is already loaded automatically?
5. Can I pass a path/reference instead of content?
6. Am I accidentally giving the worker a preferred conclusion?
7. Which skills are genuinely needed?
8. What evidence must return?
9. What must remain outside the PM after completion?

If the task packet is longer than the work it describes, reconsider decomposition or references.

---

## 22. Context Return Checklist

When a worker returns, the PM should ask:

1. What changed in project truth?
2. What evidence supports that change?
3. What needs to be persisted?
4. What can remain in the worker transcript?
5. Did this result create a new decision, risk, or dependency?
6. Is independent review now required?
7. Is the PM context still clean enough for the remaining horizon?

---

## 23. Anti-Patterns

### Context Dumping

Giving every agent the full project history "just in case."

### PM as Repository Cache

Reading files into PM context solely so the PM can repeat them to workers.

### Report Flooding

Workers returning all logs and reasoning rather than conclusions plus evidence.

### Duplicate Persistence

Keeping the same rule in global CLAUDE.md, project CLAUDE.md, agent prompt, task packet, and skill without a clear reason.

### Reviewer Anchoring

Giving the reviewer the implementer's explanation before it independently inspects the result.

### Resume by Habit

Continuing an old worker whose accumulated context is no longer an asset.

### Fork by Convenience

Forking the PM conversation for tasks that could be described cleanly to a fresh subagent.

### Memory as Database

Treating auto memory or conversation history as canonical project state.

### Compaction as Architecture

Assuming automatic compaction removes the need for state files and handoffs.

### Fixed Token Superstition

Hard-coding context percentages without evidence that those thresholds improve outcomes across models and providers.

---

## 24. V0 Context Routing Matrix

| Information | PM | Implementer | Reviewer | Debugger |
| --- | --- | --- | --- | --- |
| User outcome | Keep | Task-specific form | Relevant form | Relevant if diagnosing outcome failure |
| Global principles | Kernel / automatic | Automatic | Automatic | Automatic |
| Full project plan | Keep/reference | Only relevant slice | Usually no | Only if causal context requires |
| Current task packet | Coordinate | Full | Acceptance subset | Symptom-oriented subset |
| Relevant source files | Reference | Read directly | Read directly | Read directly |
| Raw logs | Avoid | Only if needed | Avoid unless verifying | Read/select directly |
| Worker reasoning | Avoid | Local only | Do not preload | Do not preload as fact |
| Worker report | Compact | Produce | After independent pass if useful | Only material prior findings |
| Decisions | Keep/reference | Relevant decisions only | Relevant constraints only | Relevant causal decisions only |
| STATE / HANDOFF | Canonical/reference | Only needed slice | Only needed slice | Only needed slice |
| Skills | On demand | Only relevant | Only relevant | Only relevant |

---

## 25. V0 Invariants

The following are testable requirements for future evals:

1. A worker should not require the PM's full conversation to perform a bounded task.
2. The PM should not receive raw logs when a compact finding and reference are sufficient.
3. Reviewer first-pass context should avoid implementer conclusions when independent inspection is possible.
4. A task packet should reference accessible files instead of copying large file bodies by default.
5. Durable project truth must survive replacement of the PM session.
6. Skill preloading must have an explicit task-relevance reason.
7. A noisy PM should prefer state reconciliation and handoff over indefinite context accumulation.
8. Auto memory and compaction must not be treated as canonical state.
9. Fresh workers are preferred over forks unless inherited context has clear net value.
10. Context savings must never remove information required for correctness, verification, or human authority.

---

## 26. Decision Rule

When deciding whether to include an item in context, ask:

> Will this information materially improve this agent's ability to make the next required decision or produce verifiable output?

If yes, include or reference it at the narrowest useful scope.

If no, leave it out.

That is the canonical Methodology OS context rule.
