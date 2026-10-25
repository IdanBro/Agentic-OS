#!/usr/bin/env bash
set -euo pipefail

# Methodology OS local installer for Claude Code (Linux/macOS/WSL).
# Source of truth stays in this Git repository; ~/.claude receives only
# a stable anchor, namespaced agent adapters, skill symlinks, and a small
# managed CLAUDE.md import block.

MODE="install"
FORCE=0
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
ANCHOR="$CLAUDE_HOME/methodology-os"
START_MARKER="<!-- >>> METHODOLOGY-OS MANAGED BLOCK >>> -->"
END_MARKER="<!-- <<< METHODOLOGY-OS MANAGED BLOCK <<< -->"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
CREATED_WATCH_DIR=0

AGENT_LINKS=(
  "methodology-project-manager.md:runtime/agents/methodology-project-manager.md"
  "methodology-implementer.md:runtime/agents/methodology-implementer.md"
  "methodology-reviewer.md:runtime/agents/methodology-reviewer.md"
  "methodology-debugger.md:runtime/agents/methodology-debugger.md"
)

SKILLS=(
  "methodology-start"
  "methodology-os"
  "methodology-planning"
  "methodology-handoff"
  "methodology-retrospective"
)

usage() {
  cat <<'EOF'
Usage: ./install.sh [--check | --uninstall] [--force] [--claude-home PATH]

  (no flag)        Install/update Methodology OS runtime links.
  --check          Validate the current installation without changing files.
  --uninstall      Remove only Methodology OS-managed links/import block.
  --force          Back up conflicting destinations and replace them.
  --claude-home    Override ~/.claude (useful for testing).
  -h, --help       Show this help.

The installer never modifies main/project repositories other than the local
Claude configuration paths you explicitly target.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check)
      MODE="check"
      shift
      ;;
    --uninstall)
      MODE="uninstall"
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --claude-home)
      [[ $# -ge 2 ]] || { echo "ERROR: --claude-home requires a path" >&2; exit 2; }
      CLAUDE_HOME="$2"
      ANCHOR="$CLAUDE_HOME/methodology-os"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

canonical_path() {
  local p="$1"
  if command -v realpath >/dev/null 2>&1; then
    realpath -m "$p"
  elif command -v python3 >/dev/null 2>&1; then
    python3 - "$p" <<'PY'
import os, sys
print(os.path.realpath(os.path.expanduser(sys.argv[1])))
PY
  else
    echo "$p"
  fi
}

same_link_target() {
  local dest="$1" expected="$2"
  [[ -L "$dest" ]] || return 1
  [[ "$(canonical_path "$dest")" == "$(canonical_path "$expected")" ]]
}

backup_conflict() {
  local path="$1"
  local backup="${path}.pre-methodology-os-${TIMESTAMP}"
  echo "Backing up conflict: $path -> $backup"
  mv "$path" "$backup"
}

ensure_dir() {
  local path="$1"
  if [[ ! -d "$path" ]]; then
    mkdir -p "$path"
    CREATED_WATCH_DIR=1
  fi
}

ensure_link() {
  local source="$1" dest="$2"

  if same_link_target "$dest" "$source"; then
    echo "OK link: $dest"
    return 0
  fi

  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ "$FORCE" -ne 1 ]]; then
      echo "ERROR: destination exists and is not the expected symlink: $dest" >&2
      echo "       Re-run with --force to back it up and replace it." >&2
      return 1
    fi
    backup_conflict "$dest"
  fi

  ln -s "$source" "$dest"
  echo "Linked: $dest -> $source"
}

strip_managed_block() {
  local source_file="$1" output_file="$2"
  awk -v start="$START_MARKER" -v end="$END_MARKER" '
    $0 == start { skipping = 1; next }
    $0 == end   { skipping = 0; next }
    !skipping   { print }
  ' "$source_file" > "$output_file"
}

install_claude_import() {
  local file="$CLAUDE_HOME/CLAUDE.md"
  local tmp
  tmp="$(mktemp)"

  if [[ -L "$file" ]]; then
    echo "ERROR: $file is a symlink. Refusing to edit its target automatically." >&2
    echo "       Add this import manually, or replace the symlink intentionally:" >&2
    echo "       @${ANCHOR}/runtime/CLAUDE.md" >&2
    rm -f "$tmp"
    return 1
  fi

  if [[ -f "$file" ]]; then
    cp -a "$file" "${file}.pre-methodology-os-${TIMESTAMP}"
    strip_managed_block "$file" "$tmp"
  else
    : > "$tmp"
  fi

  # Keep the user's existing content untouched except for replacing our own
  # previously managed block. A blank line is harmless and keeps Markdown tidy.
  {
    cat "$tmp"
    [[ ! -s "$tmp" ]] || printf '\n'
    printf '%s\n' "$START_MARKER"
    printf '# Methodology OS\n\n'
    printf 'The following import is managed by `Agentic-OS/install.sh`.\n\n'
    printf '@%s/runtime/CLAUDE.md\n' "$ANCHOR"
    printf '%s\n' "$END_MARKER"
  } > "$file"

  rm -f "$tmp"
  echo "Updated managed import block: $file"
}

remove_managed_block() {
  local file="$CLAUDE_HOME/CLAUDE.md"
  local tmp

  [[ -f "$file" && ! -L "$file" ]] || return 0
  grep -Fqx "$START_MARKER" "$file" || return 0

  tmp="$(mktemp)"
  strip_managed_block "$file" "$tmp"
  mv "$tmp" "$file"
  echo "Removed Methodology OS import block from $file"
}

remove_managed_link() {
  local dest="$1" expected="$2"
  if same_link_target "$dest" "$expected"; then
    rm "$dest"
    echo "Removed managed link: $dest"
  elif [[ -e "$dest" || -L "$dest" ]]; then
    echo "Leaving non-managed path untouched: $dest"
  fi
}

check_frontmatter_name() {
  local file="$1" expected="$2"
  local actual
  actual="$(awk 'NR <= 20 && /^name:[[:space:]]*/ {sub(/^name:[[:space:]]*/, ""); print; exit}' "$file")"
  [[ "$actual" == "$expected" ]]
}

check_installation() {
  local failures=0
  local claude_file="$CLAUDE_HOME/CLAUDE.md"

  echo "Methodology OS installation check"
  echo "  repo:        $REPO_ROOT"
  echo "  claude home: $CLAUDE_HOME"

  if same_link_target "$ANCHOR" "$REPO_ROOT"; then
    echo "PASS anchor"
  else
    echo "FAIL anchor: $ANCHOR does not point to $REPO_ROOT" >&2
    failures=$((failures + 1))
  fi

  for pair in "${AGENT_LINKS[@]}"; do
    local dest_name="${pair%%:*}"
    local rel_source="${pair#*:}"
    local source="$REPO_ROOT/$rel_source"
    local dest="$CLAUDE_HOME/agents/$dest_name"
    local expected_name="${dest_name%.md}"

    if same_link_target "$dest" "$source" && check_frontmatter_name "$source" "$expected_name"; then
      echo "PASS agent $expected_name"
    else
      echo "FAIL agent $expected_name" >&2
      failures=$((failures + 1))
    fi
  done

  for skill in "${SKILLS[@]}"; do
    local source="$REPO_ROOT/skills/$skill"
    local dest="$CLAUDE_HOME/skills/$skill"
    if same_link_target "$dest" "$source" && [[ -f "$source/SKILL.md" ]]; then
      echo "PASS skill $skill"
    else
      echo "FAIL skill $skill" >&2
      failures=$((failures + 1))
    fi
  done

  if [[ -f "$claude_file" ]] \
     && grep -Fqx "$START_MARKER" "$claude_file" \
     && grep -Fqx "@${ANCHOR}/runtime/CLAUDE.md" "$claude_file" \
     && grep -Fqx "$END_MARKER" "$claude_file"; then
    echo "PASS CLAUDE.md kernel import"
  else
    echo "FAIL CLAUDE.md kernel import" >&2
    failures=$((failures + 1))
  fi

  if command -v claude >/dev/null 2>&1; then
    echo "PASS Claude Code executable: $(claude --version 2>/dev/null || echo 'version unavailable')"
  else
    echo "WARN Claude Code executable not found in PATH; files are installed but runtime cannot be exercised yet."
  fi

  if [[ "$failures" -gt 0 ]]; then
    echo "CHECK FAILED: $failures issue(s)" >&2
    return 1
  fi

  echo "CHECK PASSED"
}

install_runtime() {
  [[ -d "$REPO_ROOT/agents" && -d "$REPO_ROOT/skills" && -d "$REPO_ROOT/runtime" ]] || {
    echo "ERROR: run install.sh from a valid Agentic-OS checkout." >&2
    return 1
  }

  ensure_dir "$CLAUDE_HOME"
  ensure_dir "$CLAUDE_HOME/agents"
  ensure_dir "$CLAUDE_HOME/skills"

  ensure_link "$REPO_ROOT" "$ANCHOR"

  for pair in "${AGENT_LINKS[@]}"; do
    local dest_name="${pair%%:*}"
    local rel_source="${pair#*:}"
    ensure_link "$REPO_ROOT/$rel_source" "$CLAUDE_HOME/agents/$dest_name"
  done

  for skill in "${SKILLS[@]}"; do
    ensure_link "$REPO_ROOT/skills/$skill" "$CLAUDE_HOME/skills/$skill"
  done

  install_claude_import
  check_installation

  echo
  echo "Methodology OS installed."
  echo "Start a full session with:"
  echo "  claude --agent methodology-project-manager"
  echo "Or start Methodology OS in the current project from a normal session:"
  echo "  /methodology-start <objective>"
  echo "Lightweight methodology guidance remains available as:"
  echo "  /methodology-os"

  if [[ "$CREATED_WATCH_DIR" -eq 1 ]]; then
    echo
    echo "NOTE: A Claude configuration directory was created for the first time."
    echo "Restart any Claude Code session that was already running so its file watchers see it."
  fi
}

uninstall_runtime() {
  for pair in "${AGENT_LINKS[@]}"; do
    local dest_name="${pair%%:*}"
    local rel_source="${pair#*:}"
    remove_managed_link "$CLAUDE_HOME/agents/$dest_name" "$REPO_ROOT/$rel_source"
  done

  for skill in "${SKILLS[@]}"; do
    remove_managed_link "$CLAUDE_HOME/skills/$skill" "$REPO_ROOT/skills/$skill"
  done

  remove_managed_link "$ANCHOR" "$REPO_ROOT"
  remove_managed_block

  echo "Methodology OS managed runtime links removed. Backups, repositories, and unrelated Claude configuration were left untouched."
}

case "$MODE" in
  install) install_runtime ;;
  check) check_installation ;;
  uninstall) uninstall_runtime ;;
  *) echo "ERROR: unsupported mode: $MODE" >&2; exit 2 ;;
esac
