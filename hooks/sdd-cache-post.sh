#!/bin/bash
# Post-write cache: log what was written for context restore
# Source: addy-skills/hooks/sdd-cache-post.sh pattern

FILE="$1"
if [ -z "$FILE" ]; then exit 0; fi

# Log to WORKING-CONTEXT.md append section
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
echo "  - [$TIMESTAMP] Modified: $FILE" >> WORKING-CONTEXT.md 2>/dev/null || true
