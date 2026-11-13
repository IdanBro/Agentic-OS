# Methodology OS — Real Project Trial Protocol

Step 15 validates the OS on real work rather than synthetic scenarios.

## Goal

Determine whether Methodology OS improves quality and autonomy on a real project without introducing unacceptable ceremony, token/context cost, or user interruption.

## First-Trial Selection

Prefer a task that is:
- real and useful,
- bounded enough to finish in one or a few sessions,
- medium risk rather than trivial or production-critical,
- large enough to exercise planning, delegation, PM verification, Reviewer, Git integration, and state,
- non-destructive and recoverable,
- supported by meaningful automated or deterministic verification.

Avoid for Trial 1:
- production emergencies,
- irreversible migrations,
- purely cosmetic one-file edits,
- tasks whose correctness cannot be meaningfully checked,
- work requiring hidden credentials or unavailable external systems.

## Trial Procedure

1. Start from the real project repository.
2. Ensure the working tree is understood and preserve existing project instructions.
3. Use a **local Claude Code session** for the trial. Clone/pull the GitHub repository as the working copy if needed, then activate:

```text
/agentic-os:pm-mode
```

Anthropic-hosted cloud sessions are not currently a valid PM-mode trial surface: the skill may be visible through sync/autocomplete while invocation still fails in the cloud runtime.

4. Give the current PM session the real user outcome, not a pre-written implementation plan.
5. Allow the PM to classify mode, risk, authority, plan, workers, routing, skills, and verification according to the OS.
6. Do not manually rescue routine decisions unless the PM is genuinely blocked or crosses a human gate.
7. Let the OS use its normal Git workflow on a non-main branch.
8. Require the real task to reach the appropriate quality gates before integration.
9. Do not merge to `main` without explicit user approval.
10. Complete `TRIAL_REPORT.md` immediately after the trial while evidence is fresh.

## Evidence to Capture

Capture references, not transcripts, where possible:
- task objective and acceptance criteria,
- workflow mode and risk,
- plan/state artifacts actually created,
- worker roles used,
- model/effort routes when visible,
- skills invoked,
- human gates requested,
- worker self-verification,
- PM independent verification,
- Reviewer result for medium/high risk,
- final tests/checks,
- Git branch/commits/PR,
- failures/retries/debugging paths,
- rough elapsed time,
- reported/estimated model cost when available,
- places where the user had to intervene.

## Success Criteria

Trial 1 is successful when:
1. the requested project outcome is achieved or a legitimate blocker is identified;
2. required quality gates are not silently skipped;
3. no unauthorized consequential action occurs;
4. medium/high-risk delegated work receives independent review;
5. state remains recoverable across session boundaries if a handoff is needed;
6. context/ceremony remains proportionate to the task;
7. failures trigger diagnosis or replan instead of blind repetition;
8. Git integration stays off `main` unless explicitly approved;
9. the trial produces concrete observations about the methodology.

A successful trial does **not** require the OS to be flawless. Finding a real workflow defect is valuable if it is detected, explained, and converted into a bounded learning candidate rather than patched ad hoc.

## Failure Classification

After the trial, classify each important issue as one of:
- `POLICY_DEFECT` — canonical rule is wrong or incomplete;
- `RUNTIME_DEFECT` — installation/agent/skill/tool wiring failed;
- `EVAL_GAP` — behavior was important but existing evals would not catch it;
- `CONTEXT_DEFECT` — wrong/missing/excess context caused failure;
- `ROUTING_DEFECT` — model/effort/skill/worker selection was poor;
- `DELEGATION_DEFECT` — Task Packet/scope/authority/return contract was weak;
- `VERIFICATION_DEFECT` — evidence or review process was inadequate;
- `STATE_DEFECT` — durable project truth/handoff was wrong or too heavy;
- `CEREMONY_COST` — process overhead exceeded its value;
- `PROJECT_SPECIFIC` — issue belongs to the project, not the global OS.

## Promotion Discipline

Project-specific improvements may remain local.

Potential global improvements follow `core/LEARNING_POLICY.md`:
observation → candidate → evidence/validation → READY_FOR_PROMOTION → explicit human promotion → implementation/evals/review.

Do not silently change global OS policy during the trial merely to make the current project easier.