#!/bin/bash
# Auto-loads key context at session start
# Source: addy-skills/hooks/session-start.sh pattern

echo "=== ll-vibekit session start ==="
echo "Loading key context files..."

# Always load: rules + current state
cat CLAUDE.md
cat RULES.md
cat WORKING-CONTEXT.md

# Load MEMORY if exists
if [ -f "MEMORY/stack.md" ]; then
    cat MEMORY/stack.md
fi

echo ""
echo "Context loaded. Ready for tasks."
echo "Tip: Run /route to auto-detect your task type."
