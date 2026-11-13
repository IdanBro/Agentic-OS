# Agentic OS

Agentic OS is a Claude Code plugin for running complex project work with high autonomy, professional-quality output, bounded delegation, independent verification, durable state, efficient context use, and explicit human authority over consequential decisions.

The repository itself is the plugin source of truth.

## Goal

Install Agentic OS once, then use it from any Claude Code project without relying on local `~/.claude` configuration, symlinks, copied prompts, or runtime GitHub fetching.

The intended user experience is:

```text
open Claude Code
→ Agentic OS plugin is already available
→ open/connect any project repository
→ give Claude the outcome you want
→ Agentic OS automatically selects the workflow, skills, agents, verification, and review strategy
```

For explicit activation:

```text
/agentic-os:pm-mode
```

The SessionStart hook advertises Agentic OS capabilities, while `/agentic-os:pm-mode` explicitly makes the current conversation the Project Manager session.

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
├── hooks/
│   └── hooks.json
├── core/
├── templates/
├── evals/
├── trials/
└── scripts/
```

Claude Code auto-discovers the plugin's agents, skills, and hooks. Canonical policies and templates stay in the same plugin package and are loaded on demand through `${CLAUDE_PLUGIN_ROOT}`.

There is no separate local runtime layer.

## Install from GitHub

Agentic OS is exposed as a private Claude plugin marketplace from this repository.

In Claude Code:

```text
/plugin marketplace add IdanBro/Agentic-OS
/plugin install agentic-os@idanbro-agentic-os
```

Because the repository is private, the environment/account adding the marketplace must have access to `IdanBro/Agentic-OS`.

Plugins added to a Claude account can sync into Claude Code sessions signed in with the same Claude account on Claude Code v2.1.273 or later. The plugin then runs natively with its skills, subagents, and hooks; the project itself does not need Agentic OS files.

## Normal Usage

Open any project:

```bash
cd ~/projects/my-project
claude
```

Then either give Claude a complex project goal normally, or invoke Agentic OS explicitly:

```text
/agentic-os:pm-mode

Then tell the Project Manager what outcome you want, for example:

```text
Implement the authentication feature end-to-end
```

Agentic OS is responsible for deciding:

- Lite / Standard / Full workflow depth;
- repository investigation depth;
- planning and decomposition;
- Implementer / Reviewer / Debugger use;
- model and effort routing;
- skill selection;
- state artifacts;
- verification depth;
- independent review requirements;
- Git workflow;
- human escalation.

The user should not have to manually orchestrate those pieces.

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
Claude account
        ↓
Claude Code sessions
        ↓
any project repository
```

Updating Agentic OS means publishing/updating the plugin source in this repository, not editing per-machine configuration.

## Development Branch Policy

Normal Agentic OS development happens on feature/fix branches and integrates into `dev`.

Promotion to `main` remains explicitly human-gated. Since the GitHub marketplace is intended to serve stable releases, `main` is the release surface once a plugin version is approved.

## Status

- Core Methodology OS policies: complete
- Agents and skills: complete
- Behavioral eval framework: complete
- Real-project trial: active
- Plugin-native packaging: in progress
