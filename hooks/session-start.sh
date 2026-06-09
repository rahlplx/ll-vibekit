#!/bin/bash
# session-start.sh — load project context at session start
# Source: addy-skills/hooks/session-start.sh pattern
# Reads .vibekit.json if present for project-specific context

echo "=== ll-vibekit session start ==="

# Detect project root (where .vibekit.json lives)
if [ -f ".vibekit.json" ]; then
    PROJECT_ROOT="."
elif [ -f "../.vibekit.json" ]; then
    PROJECT_ROOT=".."
else
    PROJECT_ROOT="."
fi

# Load PROJECT.md if it exists (most important — do this first)
if [ -f "$PROJECT_ROOT/PROJECT.md" ]; then
    echo "--- PROJECT.md ---"
    cat "$PROJECT_ROOT/PROJECT.md"
    echo ""
fi

# Load CLAUDE.md from ll-vibekit (universal rules)
VIBEKIT_DIR="$(dirname "${BASH_SOURCE[0]}")/.."
if [ -f "$VIBEKIT_DIR/CLAUDE.md" ]; then
    echo "--- CLAUDE.md (universal rules) ---"
    cat "$VIBEKIT_DIR/CLAUDE.md"
    echo ""
fi

# Load WORKING-CONTEXT.md (previous session state)
if [ -f "$PROJECT_ROOT/WORKING-CONTEXT.md" ]; then
    echo "--- WORKING-CONTEXT.md ---"
    cat "$PROJECT_ROOT/WORKING-CONTEXT.md"
    echo ""
fi

# Show .vibekit.json test commands if present
if [ -f "$PROJECT_ROOT/.vibekit.json" ]; then
    echo "--- Project Commands (.vibekit.json) ---"
    python3 -c "
import json, sys
data = json.load(open('$PROJECT_ROOT/.vibekit.json'))
cmds = data.get('test_commands', {})
for k,v in cmds.items():
    print(f'  {k}: {v}')
" 2>/dev/null || true
    echo ""
fi

echo "=== Context loaded. Run /route to begin. ==="
