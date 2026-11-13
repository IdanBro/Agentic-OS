#!/usr/bin/env bash
set -euo pipefail

cat <<'JSON'
{"continue":true,"suppressOutput":true,"systemMessage":"Agentic OS plugin is enabled. The user-facing session entrypoint is /agentic-os:pm-mode, which turns the current main Claude Code conversation into the Agentic OS Project Manager for the rest of the session. Native implementer, reviewer, and debugger subagents are available to that PM. Do not silently claim PM mode is active unless the pm-mode skill has been invoked by the user or explicitly selected in the conversation."}
JSON
