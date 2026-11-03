#!/usr/bin/env bash
set -euo pipefail

cat <<'JSON'
{"continue":true,"suppressOutput":true,"systemMessage":"Agentic OS plugin is enabled. Native Methodology OS skills and specialized project-manager, implementer, reviewer, and debugger subagents are available in this session. For complex, multi-stage, medium/high-risk, long-running, or context-heavy project work, activate methodology-start automatically unless the user explicitly requests a lighter approach. For trivial one-step work, avoid unnecessary methodology ceremony."}
JSON
