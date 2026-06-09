# /execute-prp — Execute Product Requirements Prompt
> Source: coleam00/context-engineering-intro
> Updated: reads .vibekit.json for test commands

Read the PRP at $ARGUMENTS. Implement exactly as specified.

## Pre-flight
1. Read .vibekit.json → test_commands (know the exact commands before starting)
2. Re-read DECISIONS.md (at path from .vibekit.json or current dir)
3. Re-read "Files NOT in scope" — hard boundary
4. State success criteria OUT LOUD before writing code

## Implementation
Follow the PRP "Implementation order" exactly.
After each file: verify with the correct command from .vibekit.json.

Examples of correct verification:
- Go file: `{test_commands.build}` (e.g. "cd go && go build ./...")
- Migration: `{test_commands.migrate}` (e.g. "cd go && goose up")
- Python file: `{test_commands.py_test}` (e.g. "cd ../agencyos-ai && pytest tests/ -x -q")
- Svelte file: `{test_commands.web_build}` (e.g. "cd ../agencyos-web && pnpm build")

If .vibekit.json has no test_commands: ask the human before proceeding.
Do NOT invent commands that might not work.

## Validation — ALL must pass
For each success criterion:
- [ ] Run the exact test command from .vibekit.json
- [ ] Show the output
- [ ] Confirm PASS or FAIL

## Completion
All pass → run /discover to update MEMORY files
All pass → run /context-save to update WORKING-CONTEXT.md
Say: "PRP executed. All success criteria verified."
