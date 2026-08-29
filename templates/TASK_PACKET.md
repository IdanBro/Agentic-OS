# Methodology OS — Task Packet Template

> Purpose: define one bounded delegation contract from the Project Manager to one worker.

A task packet should let the worker understand **what must become true, what authority it has, what evidence is required, and when it must return control to the PM** without receiving unnecessary project history.

The packet is not a mini project brief and not a transcript of PM reasoning.

---

## Metadata

- **Task ID:** `<stable plan/work ID, e.g. P2-T3>`
- **Parent plan:** `<PLAN.md version / phase>`
- **Worker role:** `<implementer | reviewer | debugger | other approved role>`
- **Risk:** `<low | medium | high>`
- **Model / effort route:** `<optional execution route or inherit>`
- **Repository / artifact:** `<reference>`
- **Branch / worktree:** `<reference or n/a>`
- **Packet version:** `<v1, v2, ... when reissued>`

Use one stable task ID across retries, debugging, fixes, and re-review. Increment packet version only when the contract materially changes.

---

## 1. Objective

State one concrete outcome.

`<What observable result should exist when this worker finishes?>`

The objective SHOULD be singular enough that the worker can tell whether it succeeded.

If the packet contains multiple independent outcomes with different acceptance or verification paths, split them into separate tasks unless keeping them together materially improves coherence.

---

## 2. Why This Matters

Include only when purpose affects implementation or review judgment.

`<Short decision context, user need, dependency, or system reason.>`

Omit project history that does not change the worker's choices.

---

## 3. In Scope

Describe the bounded change or investigation area.

- `<component / behavior / artifact>`
- `<path or interface reference>`
- `<specific outcome>`

Paths are starting references, not necessarily an exhaustive allowlist unless explicitly marked as one.

The worker MAY inspect adjacent files or dependencies when necessary to understand the task.

### Supporting-Change Rule

The worker MAY make a small supporting change outside the initially named paths when all of the following are true:

1. it is directly required to satisfy the objective correctly;
2. it does not materially expand product/project scope;
3. it does not cross an authority or human gate;
4. it remains low-risk and consistent with existing design;
5. it is reported explicitly in the work report.

Otherwise return control to the PM before expanding the change.

---

## 4. Out of Scope

Include only boundaries that prevent plausible drift.

- `<non-goal>`
- `<adjacent component that must not be changed>`
- `<migration/refactor intentionally deferred>`

Do not create artificial boundaries merely to make the packet look detailed.

---

## 5. Relevant Context / References

Prefer references the worker can inspect directly.

- `<file / directory / PR / issue / document / URL>` — `<why it matters>`
- `<D-###>` — `<relevant durable decision>`
- `<STATE/PLAN reference>` — `<only if needed>`

Include concise facts only when they are not cheaply discoverable or when the exact snapshot matters.

Do NOT paste:

- full project history,
- large source files the worker can read itself,
- long logs the worker can obtain directly,
- previous worker reasoning unless it is specifically required.

### Role-Specific Context

For a **Reviewer**, preserve independence on the first pass: provide outcome, acceptance, constraints, risk, and the actual change/artifact. Do not provide the Implementer's conclusions or confidence unless necessary.

For a **Debugger**, provide expected behavior, observed behavior, reproduction/evidence, and relevant environment facts. Do not frame a favored root-cause theory as fact.

---

## 6. Acceptance Criteria

Define observable conditions using stable IDs.

- **AC-1:** `<observable condition>`
- **AC-2:** `<observable condition>`
- **AC-3:** `<observable condition>`

Good acceptance criteria describe what must be true, not how to implement it.

Prefer:

`AC-1: Rendering the chart with default values produces a valid Deployment with both readiness and liveness probes.`

Over:

`AC-1: Edit deployment.yaml and add probes.`

The worker may recommend a change to an acceptance criterion if evidence shows it is impossible, unsafe, contradictory, or based on a false assumption, but may not silently redefine it.

---

## 7. Required Verification

List checks that the worker must actually execute or perform before claiming a successful execution status or specialized verdict.

### Must Perform

- `<command / inspection / behavior check>`
- `<command / inspection / behavior check>`

### Additional Verification Allowed

The worker SHOULD add targeted checks when they materially increase confidence and remain within scope.

Do not require expensive broad checks that have little relationship to the task merely for ceremony.

If a required check cannot be run, the worker must report why and may not represent it as passed.

---

## 8. Authority Envelope

### Worker May Decide Autonomously

Unless this packet says otherwise, the worker MAY:

- follow established repository/project conventions;
- choose local implementation details when its role permits changes;
- inspect additional relevant context;
- perform bounded diagnosis of failures;
- add targeted tests or validation required by the task when its role permits changes;
- make low-impact supporting changes allowed by the supporting-change rule when its role permits changes;
- correct an obvious local mistake introduced by its own work.

Read-only roles remain read-only even when this generic packet describes permissions available to execution workers.

### Worker Must Return to PM Before

- materially changing architecture;
- materially changing project scope or success criteria;
- introducing a major/new strategic dependency;
- making a breaking interface or compatibility choice;
- accepting a meaningful security/operational tradeoff;
- performing destructive or difficult-to-reverse operations not explicitly authorized;
- creating material new cost or billing impact;
- changing the Git integration strategy;
- merging to `dev` unless explicitly delegated;
- merging to `main` under any circumstance without explicit user approval.

### Ambiguity Rule

If a missing detail is low-impact and can be inferred safely from surrounding evidence or conventions, infer it and record the assumption briefly.

If choosing among plausible options would create materially different long-term outcomes, return control to the PM.

Do not turn every uncertainty into a clarification request.

---

## 9. Git / Artifact Boundaries

Default engineering authority for change-producing workers:

- work in the branch/worktree prepared by the PM;
- modify scoped files/artifacts as needed;
- do not commit, push, open PRs, or merge unless explicitly delegated below.

Read-only roles do not gain write authority from this section.

### Explicitly Delegated Git Actions

`<none by default, or exact allowed action>`

Any explicit Git delegation is bounded to the stated action. It does not imply broader integration authority.

---

## 10. Failure / Block Handling

A failed attempt should produce information.

Every worker SHOULD:

1. preserve concise failure evidence;
2. make a bounded attempt to identify the cause when within role scope;
3. stop repeated guess-and-retry behavior when attempts stop producing new information;
4. return the smallest useful next decision or evidence requirement.

### Execution-Worker Status

Change-producing/execution workers use:

- **PASS** — the worker believes all acceptance criteria are satisfied and required self-verification is complete. This is a worker claim, not PM approval.
- **PARTIAL** — useful scoped progress exists, but one or more acceptance criteria are not satisfied. The task remains open.
- **BLOCKED** — meaningful progress cannot continue without a PM/human decision, unavailable dependency, permission, or external condition.
- **FAILED** — the attempted approach did not achieve the objective and there is no justified in-scope next attempt without diagnosis/replanning.

`PARTIAL`, `BLOCKED`, and `FAILED` must never be treated as task completion.

### Specialized Role Outcomes

Reviewer and Debugger agents keep the outcome vocabulary defined by their role contracts, such as:

- Reviewer: `PASS | PASS_WITH_NOTES | FAIL | INCONCLUSIVE`
- Debugger: `CONFIRMED | LIKELY | INCONCLUSIVE`

Do not translate those specialized outcomes into execution-worker statuses unless the PM explicitly asks for an additional execution status.

The specialized vocabulary does not weaken the same requirements for bounded scope, evidence, uncertainty reporting, or PM-controlled escalation.

---

## 11. Return Contract

Use `WORK_REPORT.md` for change-producing/execution work unless the role has a stricter specialized return contract.

The PM needs conclusions and evidence, not a transcript.

At minimum return:

- task ID and status/verdict/diagnosis as applicable;
- concise outcome/change summary;
- acceptance-criteria status where applicable;
- verification actually performed;
- evidence needed for independent PM verification;
- remaining uncertainty;
- scope/assumption notes;
- exact blocker or recommended next action when incomplete.

Reviewer and Debugger role definitions add specialized verdict/finding/diagnosis structures. Those specialized structures take precedence where they are stricter, while the same bounded-task and evidence principles still apply.

---

## 12. PM Dispatch Checklist

Before sending the packet, the PM should be able to answer `yes` to the relevant items:

- [ ] Is the objective concrete and bounded?
- [ ] Can the worker determine success without reconstructing hidden PM intent?
- [ ] Are acceptance criteria observable rather than implementation-prescriptive?
- [ ] Is required context referenced instead of unnecessarily copied?
- [ ] Are important scope boundaries explicit?
- [ ] Is the worker's authority sufficient to make progress without approval spam?
- [ ] Does the packet preserve the worker role's read/write boundaries?
- [ ] Are high-impact authority limits preserved?
- [ ] Is verification proportional to risk and feasible for this worker?
- [ ] Is the return contract clear enough for independent PM verification?
- [ ] Would splitting this packet further improve isolation, independence, or parallelism enough to justify the overhead?

If the last answer is no, keep the task together.

---

## Compact Packet Form

For small Standard-mode delegations, the full headings are optional. The semantic contract may be compressed to:

```text
TASK: <ID>
OBJECTIVE: <bounded outcome>
SCOPE: <references / boundaries>
ACCEPTANCE: <observable criteria>
VERIFY: <required checks>
AUTHORITY: <only unusual limits or permissions>
RETURN: <WORK_REPORT or specialized role contract>
```

Do not use the compact form when omitted fields would force the worker to infer a material decision.