#!/bin/bash
# ll-vibekit install script
# Source: ECC + caveman install.sh pattern
# Usage: bash install.sh [--project /path/to/your/project]

set -e

PROJECT="${1:-$(pwd)}"
VIBEKIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "╔══════════════════════════════════════╗"
echo "║  ll-vibekit — Lab Launchpad Harness  ║"
echo "╚══════════════════════════════════════╝"
echo ""
echo "Installing into: $PROJECT"
echo "Harness from:    $VIBEKIT_DIR"
echo ""

# Create .claude directory in target project
mkdir -p "$PROJECT/.claude/commands"
mkdir -p "$PROJECT/.claude/hooks"

# Link commands
echo "→ Linking slash commands..."
for cmd in "$VIBEKIT_DIR"/.claude/commands/*.md; do
    cp "$cmd" "$PROJECT/.claude/commands/"
    echo "  ✓ $(basename $cmd)"
done

# Link hooks
echo "→ Installing hooks..."
cp -r "$VIBEKIT_DIR/hooks" "$PROJECT/ll-vibekit-hooks"
echo "  ✓ hooks/ installed to ll-vibekit-hooks/"

# Copy INITIAL.md if not exists
if [ ! -f "$PROJECT/INITIAL.md" ]; then
    cp "$VIBEKIT_DIR/INITIAL.md" "$PROJECT/INITIAL.md"
    echo "  ✓ INITIAL.md created"
fi

# Copy HUMAN-TODO.md if not exists
if [ ! -f "$PROJECT/HUMAN-TODO.md" ]; then
    cp "$VIBEKIT_DIR/HUMAN-TODO.md" "$PROJECT/HUMAN-TODO.md"
    echo "  ✓ HUMAN-TODO.md created"
fi

echo ""
echo "✅ ll-vibekit installed!"
echo ""
echo "Next steps:"
echo "  1. Fill INITIAL.md with your feature request"
echo "  2. Open Claude Code in $PROJECT"
echo "  3. Run: /route"
echo "  4. Run: /generate-prp INITIAL.md"
echo ""
