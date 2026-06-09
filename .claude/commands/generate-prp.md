# /generate-prp — Generate Product Requirements Prompt
> Source: coleam00/context-engineering-intro
> Updated: reads .vibekit.json for project-specific paths

Read the feature request in $ARGUMENTS (default: INITIAL.md).
DO NOT write any code. Write the PRP only.

## Step 1: Load Project Config
Read .vibekit.json if it exists:
- project_name → for PRP header
- test_commands → for success criteria commands
- repos.related → for cross-repo file paths
- context_files.decisions → exact path to DECISIONS.md

If no .vibekit.json: look for DECISIONS.md in current directory.

## Step 2: Read Feature Request
Read $ARGUMENTS completely.
Understand: what is being built, which layers change, what success looks like.

## Step 3: Research Codebase (token-efficient)
Load ONLY what's needed for this feature:
- DECISIONS.md (from .vibekit.json path, or current dir)
- MEMORY/modules.md (does this module already exist?)
- PROJECT.md Stack section (correct framework for this project)
For cross-repo features: note which repos need changes.

## Step 4: Check HUMAN-TODO.md
Does this feature require human action first?
(e.g. Meta App Review for social features, payment setup for billing)
If yes: STOP. Tell the human what's needed. Do not proceed.

## Step 5: Write PRP to PRPs/{feature-name}.md

Required sections:
- Goal (one sentence)
- Repos affected (from .vibekit.json related repos)
- Success criteria (verifiable — use .vibekit.json test_commands for exact commands)
- Files in scope (exact paths)
- Files NOT in scope (Karpathy Rule 3)
- DECISIONS.md compliance checklist
- Implementation order
- Edge cases (minimum 3)

For multi-repo projects (.vibekit.json repos.type = "multi"):
- Clearly label each file with its repo name
- Note the correct working directory for each test command

## Complete
Say: "PRP written to PRPs/{name}.md — review it, then run /execute-prp PRPs/{name}.md"
