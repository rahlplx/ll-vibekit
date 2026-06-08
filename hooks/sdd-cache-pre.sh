#!/bin/bash
# Pre-write cache: check DECISIONS.md before any file write
# Source: addy-skills/hooks/sdd-cache-pre.sh pattern

FILE="$1"
if [ -z "$FILE" ]; then exit 0; fi

# Check if file is in a sensitive location
if [[ "$FILE" == *"go/db/migrations"* ]]; then
    echo "MIGRATION FILE DETECTED: $FILE"
    echo "Reminder: Check these before proceeding:"
    echo "  - Does new table have tenant_id FK?"
    echo "  - Does new table have RLS enabled?"
    echo "  - Does new table have is_deleted column?"
    echo "  - Are you using port 6432 (PgBouncer) not 5432?"
fi

if [[ "$FILE" == *"src/experts"* ]]; then
    echo "EXPERT FILE DETECTED: $FILE"
    echo "Reminder: Check these before proceeding:"
    echo "  - Is embedding model bge-m3 (not bge-base-en-v1.5)?"
    echo "  - Is auto-approve threshold 0.95 (not 0.90)?"
    echo "  - Is LiteLLM call async (acompletion)?"
fi
