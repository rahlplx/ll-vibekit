#!/bin/bash
# session-end.sh — capture session + run full eval pipeline
# Usage: bash hooks/session-end.sh SESSION_ID [outcome]
# outcome: shipped | abandoned | in-progress | blocked

SESSION_ID="$1"
OUTCOME="${2:-abandoned}"

if [ -z "$SESSION_ID" ]; then
  echo "Usage: bash hooks/session-end.sh SESSION_ID [outcome]"
  exit 1
fi

echo "=== ll-vibekit session end: $SESSION_ID ==="

# 1. End the OTel trace
python3 scripts/otel-harness.py end "$SESSION_ID" "$OUTCOME" 2>/dev/null || true

# 2. Score the session + update MEMORY/
python3 scripts/eval-session.py 2>/dev/null || true

# 3. Update skill performance stats
python3 scripts/eval-skills.py 2>/dev/null || true

# 4. Update agent performance stats
python3 scripts/eval-agents.py 2>/dev/null || true

# 5. Update intelligence summary
python3 scripts/intelligence-report.py --update 2>/dev/null || true

echo "Session $SESSION_ID recorded."
echo "Run /report for weekly intelligence. Run /harness-health for full check."
