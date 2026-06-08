#!/bin/bash
# Prevent over-engineering: flag when output is getting too large
# Source: addy-skills/hooks/simplify-ignore.sh pattern

INPUT="$1"
LINE_COUNT=$(echo "$INPUT" | wc -l)

if [ "$LINE_COUNT" -gt 300 ]; then
    echo "WARNING: This file is $LINE_COUNT lines."
    echo "Karpathy Rule 2: No over-engineering."
    echo "Can this be simplified to under 150 lines?"
    echo "If yes: pause and simplify. If no: proceed."
fi
