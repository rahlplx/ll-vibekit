#!/bin/bash
# Pre-commit: validate DECISIONS.md compliance
# Source: rohitg00/awesome-claude-code-toolkit

echo "Running pre-commit checks..."

# Check for forbidden patterns
STAGED=$(git diff --cached --name-only)

for file in $STAGED; do
  if [[ -f "$file" ]]; then
    # Check for English-only embedding model
    if grep -q "bge-base-en-v1.5" "$file"; then
      echo "❌ BLOCKED: $file uses bge-base-en-v1.5 (English-only). Use BAAI/bge-m3"
      exit 1
    fi
    # Check for PG LISTEN/NOTIFY
    if grep -q "LISTEN\|NOTIFY" "$file" && [[ "$file" == *.sql ]]; then
      echo "❌ BLOCKED: $file uses PG LISTEN/NOTIFY. Use Valkey pub/sub"
      exit 1
    fi
    # Check for DELETE FROM (should be is_deleted)
    if grep -qE "DELETE FROM" "$file" && [[ "$file" == *.sql || "$file" == *.go ]]; then
      echo "❌ BLOCKED: $file uses DELETE FROM. Use is_deleted=true"
      exit 1
    fi
  fi
done

echo "✓ Pre-commit checks passed"
exit 0
