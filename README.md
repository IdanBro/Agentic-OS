# Agentic OS

Agentic OS is a Claude Code plugin for running complex project work with high autonomy, professional-quality output, bounded delegation, independent verification, durable state, efficient context use, and explicit human authority over consequential decisions.

The repository is the plugin source of truth.

## Supported Workflow

Agentic OS is currently designed for **local Claude Code sessions**: Claude Desktop local Code sessions, the Claude Code terminal, or supported local IDE integrations.

The recommended operating model is:

```text
GitHub repository = source of truth
        ↓ clone / pull
local working copy
        ↓
local Claude Code session
        ↓
/agentic-os:pm-mode
        ↓
Project Manager → workers → verification → review
        ↓
push branch / PR
        ↓
GitHub
```

A local clone is only a working copy. The project remains GitHub-first and can be deleted locally after committed work is pushed.

### Cloud sessions

Do **not** rely on Agentic OS PM mode in Anthropic-hosted Claude Code cloud sessions at this time.

Observed behavior: the synced skill can appear in `/skills` or autocomplete while invocation still fails in the cloud runtime. Local sessions execute the skill correctly.

Use cloud sessions for bounded standalone execution tasks when useful, but use a **local session as the Agentic OS Project Manager** until cloud plugin/skill execution is verified end-to-end.

## Entry Point

Activate Agentic OS explicitly in a local Claude Code session:

```text
/agentic-os:pm-mode
```

This turns the **current main session** into the Agentic OS Project Manager for the remainder of that session. No SessionStart hook or startup script is required.

## Plugin Architecture

```text
Agentic-OS/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── agents/
│   ├── project-manager.md
│   ├── implementer.md
│   ├── reviewer.md
│   └── debugger.md
├── skills/
│   ├── pm-mode/
│   ├── methodology-os/
│   ├── methodology-planning/
│   ├── methodology-handoff/
│   └── methodology-retrospective/
├── core/
├── templates/
├── evals/
├── trials/
└── scripts/
```

Claude Code auto-discovers the plugin's agents and skills. Canonical policies and templates remain in the plugin package and are loaded on demand through `${CLAUDE_PLUGIN_ROOT}`.

There is no separate local runtime layer and no runtime GitHub fetching.

## Installation

### Recommended: install once at User scope

In a **local Claude Code** session:

```text
/plugin marketplace add IdanBro/Agentic-OS
/plugin install agentic-os@idanbro-agentic-os
```

When Claude asks for installation scope, choose **User**.

User scope makes the plugin available to your local Claude Code sessions across projects on that machine.

Because the marketplace repository is private, the machine/account must have GitHub access to `IdanBro/Agentic-OS`.

If private-repository access fails, authenticate GitHub first, for example:

```bash
gh auth login
gh repo view IdanBro/Agentic-OS
```

If the plugin is already present through Claude account sync, do not reinstall it unnecessarily; verify that it is enabled and available in the local session.

### Update

Refresh the marketplace and plugin:

```text
/plugin marketplace update idanbro-agentic-os
/plugin update agentic-os@idanbro-agentic-os
```

Then open a **new local Code session**.

### Verify installation

In the new local session:

1. Run `/skills` and confirm `pm-mode` is listed.
2. Invoke:

```text
/agentic-os:pm-mode
```

3. Confirm the session reports that it is operating as the Agentic OS Project Manager and can access the plugin agents: Implementer, Reviewer, and Debugger.

If the skill is listed but invocation fails, check whether the session is cloud-hosted. Re-test in a local session before changing the plugin installation.

For installation/configuration diagnostics, use `/doctor` or `claude doctor`.

## Normal Usage

1. Clone or pull the GitHub repository you want to work on.
2. Open that working copy in a **local** Claude Code session.
3. Invoke:

```text
/agentic-os:pm-mode
```

4. Give the current session the project outcome, for example:

```text
Build the application described in README.md.
```

The skill is a role switch, not a separate workflow and not another PM agent. It loads the canonical Project Manager contract into the **current main session**.

The Project Manager owns:

- Lite / Standard / Full workflow depth;
- repository investigation;
- planning and decomposition;
- bounded delegation to Implementer / Reviewer / Debugger;
- model and effort routing;
- skill selection;
- state artifacts;
- independent verification and review;
- Git workflow;
- human escalation.

For Standard/Full work, the main session remains the PM rather than becoming the primary implementation worker.

## GitHub-First Working Model

Agentic OS does not require projects to live permanently on the local machine.

A practical workflow is:

```bash
git clone git@github.com:OWNER/REPO.git
cd REPO
claude
```

Activate `/agentic-os:pm-mode`, complete the work on a non-main branch, push the branch / PR, then delete the local clone whenever you no longer need it.

Project-specific Claude instructions may live in the project repository, for example `.claude/CLAUDE.md` or project skills. Do not copy Agentic OS itself into each project.

## Architecture

```text
User objective
      ↓
Project Manager
      ├── Implementer — bounded execution + self-verification
      ├── Reviewer    — independent review
      └── Debugger    — diagnosis-first investigation
      ↓
PM independent verification
      ↓
quality / authority gates
      ↓
working branch / PR / integration
      ↓
explicit human gate for main
```

V0 deliberately keeps orchestration shallow: workers do not recursively orchestrate other workers.

## Core Rules

The governing rule is:

> Use the lightest workflow that still protects the required professional quality bar.

Priority order:

1. professional-quality output;
2. efficient token/context use;
3. high autonomy for routine work;
4. evidence-based completion;
5. human control over consequential decisions.

### Verification

Worker `PASS` is never project truth by itself.

```text
worker self-verification
→ PM independent verification
→ independent Reviewer for medium/high risk
→ integration readiness
```

Verification states:

```text
PASS | FAIL | INCONCLUSIVE | NOT_RUN | N/A
```

### Authority

```text
A0 — AUTONOMOUS
A1 — AUTONOMOUS + RECORD
A2 — HUMAN GATE
A3 — BLOCKED
```

`main` remains explicitly human-gated.

### Context

Context is a working set, not an archive. High-volume exploration belongs in bounded workers; the PM retains compact conclusions and evidence.

### Learning

Project-specific learning may stay local. Global Agentic OS behavior changes remain proposals until explicitly promoted by the human and passed through normal eval/review gates.

## Policy Map

| Concern | Canonical source |
| --- | --- |
| Requirements | `OS_REQUIREMENTS.md` |
| Principles | `core/PRINCIPLES.md` |
| Lifecycle / orchestration | `core/ORCHESTRATION.md` |
| Model / effort routing | `core/ROUTING.md` |
| Context | `core/CONTEXT_POLICY.md` |
| Verification / review | `core/QUALITY_GATES.md` |
| Skills | `core/SKILL_POLICY.md` |
| Human authority | `core/ESCALATION_POLICY.md` |
| Learning / promotion | `core/LEARNING_POLICY.md` |

## Evals

Static validation:

```bash
python3 scripts/validate_runtime.py
python3 scripts/run_evals.py --static-only
```

Behavioral suites load the current repository directly as a Claude plugin with `--plugin-dir`:

```bash
python3 scripts/run_evals.py core-v0
python3 scripts/run_evals.py routing-v0
python3 scripts/run_evals.py learning-v0
```

Optional semantic judging:

```bash
python3 scripts/run_evals.py core-v0 --semantic-judge
```

## Distribution Model

```text
GitHub Agentic-OS repo
        ↓
private Agentic OS marketplace
        ↓
agentic-os plugin
        ↓
User-scope local installation / Claude account sync
        ↓
local Claude Code sessions
        ↓
GitHub project working copies
```

Updating Agentic OS means updating the plugin source in this repository and then updating the installed plugin. Projects do not carry copies of Agentic OS.

## Development Branch Policy

Normal Agentic OS development happens on feature/fix branches and integrates into `dev`.

Promotion to `main` remains explicitly human-gated. `main` is the stable marketplace/release surface.

## Status

- Core Methodology OS policies: complete
- Agents and skills: complete
- Behavioral eval framework: complete
- Real-project trial: active
- Plugin-native packaging: complete
- Local PM-mode workflow: supported
- Anthropic-hosted cloud PM-mode workflow: not currently supported
