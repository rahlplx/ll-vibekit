#!/bin/bash
# ll-vibekit install.sh
# Universal vibe coding harness installer
# Usage: bash install.sh [--project /path/to/project]
set -e

PROJECT="${1:-$(pwd)}"
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "╔════════════════════════════════════╗"
echo "║  ll-vibekit — Universal Harness    ║"
echo "╚════════════════════════════════════╝"
echo "Project: $PROJECT"
echo ""

# Create .claude dirs
mkdir -p "$PROJECT/.claude/commands"
mkdir -p "$PROJECT/.claude/hooks"

# Copy slash commands
echo "→ Installing commands..."
for f in "$KIT"/.claude/commands/*.md; do
    cp "$f" "$PROJECT/.claude/commands/"
    echo "  ✓ $(basename $f)"
done

# Copy hooks
echo "→ Installing hooks..."
mkdir -p "$PROJECT/ll-vibekit-hooks"
cp -r "$KIT/hooks/." "$PROJECT/ll-vibekit-hooks/"
echo "  ✓ hooks installed"

# Copy PROJECT.md template if not exists
if [ ! -f "$PROJECT/PROJECT.md" ]; then
    cp "$KIT/PROJECT.md" "$PROJECT/PROJECT.md"
    echo "  ✓ PROJECT.md template created"
fi

# Copy INITIAL.md template if not exists
if [ ! -f "$PROJECT/INITIAL.md" ]; then
    cp "$KIT/INITIAL.md" "$PROJECT/INITIAL.md"
    echo "  ✓ INITIAL.md template created"
fi

# Copy WORKING-CONTEXT.md if not exists
if [ ! -f "$PROJECT/WORKING-CONTEXT.md" ]; then
    cp "$KIT/WORKING-CONTEXT.md" "$PROJECT/WORKING-CONTEXT.md"
    echo "  ✓ WORKING-CONTEXT.md created"
fi

# Copy HUMAN-TODO.md template if not exists
if [ ! -f "$PROJECT/HUMAN-TODO.md" ]; then
    cp "$KIT/HUMAN-TODO.md" "$PROJECT/HUMAN-TODO.md"
    echo "  ✓ HUMAN-TODO.md template created"
fi

# Create MEMORY/ if not exists
mkdir -p "$PROJECT/MEMORY"
for f in stack.md modules.md mistakes.md patterns.md; do
    if [ ! -f "$PROJECT/MEMORY/$f" ]; then
        cp "$KIT/MEMORY/$f" "$PROJECT/MEMORY/$f"
        echo "  ✓ MEMORY/$f template created"
    fi
done

# Create PRPs/ if not exists
mkdir -p "$PROJECT/PRPs/templates"
if [ ! -f "$PROJECT/PRPs/templates/prp_base.md" ]; then
    cp "$KIT/PRPs/templates/prp_base.md" "$PROJECT/PRPs/templates/prp_base.md"
    echo "  ✓ PRPs/templates/prp_base.md created"
fi

# Run discovery if python3 available
echo ""
if command -v python3 &> /dev/null; then
    echo "→ Running project discovery..."
    python3 "$KIT/scripts/discover-project.py" "$PROJECT" 2>/dev/null || true
fi

echo ""
echo "✅ ll-vibekit installed!"
echo ""
echo "NEXT STEPS:"
echo "  1. Open Claude Code in: $PROJECT"
echo "  2. Run: /setup discover  (to auto-fill PROJECT.md)"
echo "     OR edit PROJECT.md manually with your project details"
echo "  3. Fill INITIAL.md with your first feature"
echo "  4. Run: /generate-prp INITIAL.md"
echo ""
