#!/bin/bash
# session-end.sh — capture session outcome for telemetry
# Call at end of session: bash hooks/session-end.sh SESSION_ID outcome
# outcome: shipped | abandoned | in-progress | blocked

SESSION_ID="$1"
OUTCOME="${2:-abandoned}"

if [ -z "$SESSION_ID" ]; then
  echo "Usage: bash hooks/session-end.sh SESSION_ID [outcome]"
  exit 1
fi

# End the OTel trace
python3 scripts/otel-harness.py end "$SESSION_ID" "$OUTCOME" 2>/dev/null || true

# Run eval pipeline
python3 scripts/eval-session.py 2>/dev/null || true

# Update intelligence report stats
python3 scripts/intelligence-report.py --update 2>/dev/null || true

echo "Session $SESSION_ID recorded. Run /report for intelligence summary."
