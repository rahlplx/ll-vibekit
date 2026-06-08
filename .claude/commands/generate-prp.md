# /generate-prp — Generate Product Requirements Prompt
> Source: coleam00/context-engineering-intro

Read the feature request in $ARGUMENTS (default: INITIAL.md).

## Step 1: Read
Read $ARGUMENTS completely. Understand: what, which layers, success criteria.

## Step 2: Research (token-efficient)
Load ONLY these files:
- DECISIONS.md (constraints)
- MEMORY/modules.md (existing modules — avoid duplicating)
- CONTEXT.md (stack decisions)

## Step 3: Check HUMAN-TODO.md
Does this feature require human action first?
If yes: tell the human, don't proceed.

## Step 4: Write PRP

Save to `PRPs/{feature-name}.md` using template `PRPs/templates/prp_base.md`.

Must include:
- One-sentence goal
- Verified success criteria (not "it works" — specific test results)
- Files in scope (explicit list)
- Files NOT in scope (Karpathy Rule 3)
- Implementation order
- Edge cases (minimum 3)

## Complete
Say: "PRP written to PRPs/{name}.md — review it, then run /execute-prp PRPs/{name}.md"
