# Methodology OS — Claude Code Runtime

This directory contains the thin runtime layer that exposes the canonical Methodology OS repository to Claude Code without duplicating the full policies into every session.

## Architecture

```text
Agentic-OS Git checkout
        │
        ├── core/ + agents/ + skills/ + evals/
        │        canonical source of truth
        │
        └── runtime/
             ├── CLAUDE.md
             └── agents/
                    namespaced runtime adapters

~/.claude/
├── methodology-os -> <Agentic-OS checkout>
├── CLAUDE.md
│    └── managed import -> ~/.claude/methodology-os/runtime/CLAUDE.md
├── agents/
│    ├── methodology-project-manager.md -> runtime adapter
│    ├── methodology-implementer.md -> runtime adapter
│    ├── methodology-reviewer.md -> runtime adapter
│    └── methodology-debugger.md -> runtime adapter
└── skills/
     ├── methodology-start -> project launcher skill
     ├── methodology-os -> source skill
     ├── methodology-planning -> source skill
     ├── methodology-handoff -> source skill
     └── methodology-retrospective -> source skill
```

The runtime adapters exist to give global agents collision-resistant names while keeping the detailed role contracts in `agents/*.md` as the single canonical source.

## Install

From the Agentic-OS repository root:

```bash
bash install.sh
bash install.sh --check
```

The installer is idempotent. Existing conflicting paths are not replaced unless `--force` is explicitly supplied. Existing `~/.claude/CLAUDE.md` content is preserved; the installer manages only a marked import block and creates a timestamped backup before modifying a regular file.

If `~/.claude/CLAUDE.md` is itself a symlink, the installer refuses to edit through it and prints the import you can add manually.

## Start a Full Methodology OS Session

```bash
claude --agent methodology-project-manager
```

Claude Code runs that agent as the main session, while the PM can delegate to the namespaced Methodology OS workers.

For the normal workflow, start Methodology OS in the current project with:

```text
/methodology-start <objective>
```

If no objective is supplied, the launcher bootstraps the repository and asks one concise outcome question.

For lightweight methodology guidance without handing over the full project lifecycle, use:

```text
/methodology-os
```

## Verify Loaded Configuration

Inside Claude Code:

```text
/context
```

Confirm the user `CLAUDE.md` is loaded. Agent availability can be tested by starting a session with:

```bash
claude --agent methodology-project-manager
```

If the top-level `~/.claude/agents` or `~/.claude/skills` directory was created after a Claude Code session had already started, restart that session so the file watchers see the new directory.

## Evals

Static checks only:

```bash
python3 scripts/run_evals.py --static-only
```

Blocking core behavioral suite:

```bash
python3 scripts/run_evals.py core-v0
```

Include semantic `must` / `must_not` judging when a deeper release check is justified:

```bash
python3 scripts/run_evals.py core-v0 --semantic-judge
```

Targeted suites:

```bash
python3 scripts/run_evals.py routing-v0
python3 scripts/run_evals.py learning-v0
python3 scripts/run_evals.py full-v0
```

By default each scenario runs in a fresh non-persistent Claude Code session using the installed `methodology-project-manager`, `sonnet`, `high` effort, read-only tools, a turn cap, and a per-scenario budget cap. All of those runtime parameters are recorded in the optional JSON report and can be changed through runner flags.

The runner does not give the PM the scenario's expected answer. It provides only the situation, invariant, and relevant policy references, then grades the structured result separately.

## Uninstall

```bash
bash install.sh --uninstall
```

Uninstall removes only symlinks that still point to this checkout and the installer-managed CLAUDE.md block. It leaves backups, repositories, unrelated agents/skills, and other Claude Code configuration untouched.

## Source-of-Truth Rule

Do not hand-edit the installed Methodology OS symlink targets in `~/.claude` as if they were separate configuration copies. Edit the Git repository on a feature branch, verify the change, merge it through the Methodology OS workflow, then the symlinked runtime sees the updated source automatically.
