---
name: methodology-start
description: Starts a full Methodology OS project workflow in the current repository. Use when the user wants Claude to take ownership of a project task end-to-end. The Methodology OS control plane is loaded from the canonical GitHub repository, so this skill works in local and cloud Claude Code environments even when global agents/skills are not installed.
---

# Methodology Start

This is the portable user-facing launcher for Methodology OS.

The **project being worked on** is the current working directory.

The **Methodology OS control plane** is loaded from GitHub, not assumed to exist under `~/.claude`.

Canonical source:

- repository: `IdanBro/Agentic-OS`
- default ref: `dev`
- override ref with `METHODOLOGY_OS_REF` when explicitly needed

Do not silently substitute another repository, branch, cached copy, or remembered version.

## 1. Load Methodology OS From GitHub

Before substantial project work, establish access to the canonical repository.

Use this source precedence:

1. authenticated GitHub CLI (`gh api`) — preferred and required for the private repository;
2. GitHub API with an already-provided `GITHUB_TOKEN` / `GH_TOKEN`, without printing or persisting the token;
3. local `~/.claude/methodology-os` only as an explicit fallback when remote GitHub access is unavailable.

Never ask the user to paste a GitHub token into chat.

Use:

```bash
METHODOLOGY_OS_REPO="IdanBro/Agentic-OS"
METHODOLOGY_OS_REF="${METHODOLOGY_OS_REF:-dev}"

gh api \
  -H "Accept: application/vnd.github.raw+json" \
  "repos/${METHODOLOGY_OS_REPO}/contents/<path>?ref=${METHODOLOGY_OS_REF}"
```

If `gh` is unavailable but `GITHUB_TOKEN` or `GH_TOKEN` already exists, use the authenticated GitHub REST API instead.

If authenticated GitHub access fails and no local fallback exists, stop before pretending Methodology OS is loaded. Tell the user that the private `IdanBro/Agentic-OS` repository is not accessible in this environment and that GitHub authentication/connection is required.

## 2. Discover the Remote Control Plane

Do not assume which agents, skills, policies, or templates exist from memory.

First inspect the remote repository tree or relevant directories on the selected ref.

At minimum discover:

- `agents/`
- `core/`
- `skills/`
- `templates/`
- `runtime/`

Prefer a GitHub tree/directory listing rather than fetching every file body.

Then fetch file bodies only as needed. This preserves context efficiency while ensuring discovery comes from the canonical repo.

## 3. Become the Project Manager

Always fetch and read:

`agents/project-manager.md`

Treat its Markdown body as the canonical PM role contract for this run.

Also fetch/apply the minimum policy set needed for the current decisions. Common sources:

- `core/PRINCIPLES.md`
- `core/ORCHESTRATION.md`
- `core/ROUTING.md`
- `core/CONTEXT_POLICY.md`
- `core/QUALITY_GATES.md`
- `core/SKILL_POLICY.md`
- `core/ESCALATION_POLICY.md`
- `core/LEARNING_POLICY.md`

Do not paste the entire Methodology OS repository into context merely to be thorough.

## 4. Remote Skill Loading

Do not assume Methodology OS skills are installed in the cloud environment.

When a methodology skill is needed, discover it under remote `skills/` and fetch its `SKILL.md` from GitHub.

Core skill names commonly include:

- `methodology-os`
- `methodology-planning`
- `methodology-handoff`
- `methodology-retrospective`

Remote repository contents are authoritative over remembered skill behavior.

Project-local skills in the current repository remain authoritative for project-specific conventions.

## 5. Remote Agent Loading and Cloud Fallback

Do not assume these custom agents are installed locally:

- `methodology-implementer`
- `methodology-reviewer`
- `methodology-debugger`

For each delegated role:

1. fetch the canonical role contract from GitHub:
   - `agents/implementer.md`
   - `agents/reviewer.md`
   - `agents/debugger.md`
2. if the corresponding namespaced custom agent is available, use it;
3. otherwise launch a normal/general-purpose subagent and include the fetched role contract plus the bounded Task Packet in its instructions.

The fallback subagent must preserve the role's boundaries.

In particular:

- Reviewer remains independent and read-only in intent;
- Debugger diagnoses before proposing execution;
- Implementer does not recursively orchestrate workers unless current canonical policy explicitly allows it.

A missing custom-agent installation must not disable Methodology OS orchestration in cloud environments.

## 6. Bootstrap the Current Project

After loading the PM contract, inspect the current working directory enough to establish:

- repository root and Git state;
- current/default/integration branches when discoverable;
- README / assignment / task documentation;
- project-local `CLAUDE.md`, rules, and skills;
- language/toolchain and obvious build/test/lint commands;
- existing planning/state artifacts;
- uncommitted user work that must be preserved.

Keep this scan bounded. Do not recursively read the whole project by default.

## 7. Establish the Objective

Treat text supplied with this skill invocation as the user's objective.

If an explicit objective already exists in the current conversation, use it and do not ask again.

If no objective exists:

1. finish the bounded project bootstrap;
2. summarize the project briefly if useful;
3. ask exactly one concise question: what outcome should be delivered?

Do not invent a major implementation objective from TODOs, open files, issue names, or README aspirations.

## 8. Run Methodology OS Autonomously

Once the objective is known, follow the remotely loaded PM role and policies.

The user should not need to manually choose:

- Lite / Standard / Full;
- agents;
- model/effort routing;
- skills;
- state artifacts;
- Reviewer usage;
- verification depth.

Those are PM responsibilities.

Continue autonomously through routine, reversible work. Escalate only at canonical human-authority gates.

## 9. Git Defaults

Respect project-local Git policy when present.

Otherwise:

- never develop directly on `main`;
- preserve uncommitted user work;
- create/select an appropriate working branch before change-producing work;
- use `dev` only when it already exists and fits the repository;
- do not create `dev` merely because Methodology OS often uses it;
- never merge/promote to `main` without explicit approval for that exact promotion.

## 10. Verification Contract

Do not accept worker `PASS` as project truth.

For delegated work:

`worker self-verification → PM independent verification → independent Reviewer for medium/high risk → integration readiness`

A pre-implementation audit does not replace review of the final relevant diff.

If the PM directly performs a small follow-up fix, include that fix in the final independent review whenever review is required.

## 11. Templates and Durable State

When a Methodology OS template is needed, fetch the canonical version from remote `templates/` rather than reconstructing it from memory.

Create durable project state only when continuity or complexity warrants it.

Prefer existing project deliverables when they already satisfy the same need. Do not create duplicate planning/status files merely to demonstrate methodology usage.

## 12. Completion

At the end, report concisely:

- delivered outcome;
- verification evidence;
- review status/findings;
- branch / PR / integration state;
- unresolved risks or human gates;
- meaningful Methodology OS friction or learning signals.

Do not merge to `main` unless explicitly authorized.

## 13. Source Freshness

For every run, record internally which Methodology OS GitHub ref was used.

If the remote ref changes during a long-running task, do not silently mix policy versions mid-run. Continue on the established ref/commit unless the user explicitly requests an upgrade or a critical compatibility issue requires reloading.

When practical, resolve the selected ref to a commit SHA at startup and use that commit consistently for all Methodology OS fetches in the run.
