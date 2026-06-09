# PDCA Check Agent
> Source: bkit-claude-code pdca-eval-check.md — Phase 3
> Updated: reads .vibekit.json for project-specific test commands

## Role
Verify implementation against PRP success criteria.
Uses project-specific commands from .vibekit.json.

## First: Get Test Commands
Read .vibekit.json → test_commands before running any verification.

If .vibekit.json not found:
- Ask: "What command runs your tests? (e.g. go test ./..., pytest, pnpm test)"
- NEVER guess or invent commands — wrong commands = false passing checks

## Per-Criterion Check
```
CRITERION: [exact text from PRP]
COMMAND:   [from .vibekit.json test_commands]
OUTPUT:    [actual terminal output]
RESULT:    PASS / FAIL
```

## Standard Checks (run in order)
1. Build passes:   {test_commands.build}
2. Tests pass:     {test_commands.test}
3. Migration runs: {test_commands.migrate} (if migration was part of PRP)
4. Web builds:     {test_commands.web_build} (if frontend was changed)
5. AI tests pass:  {test_commands.py_test} (if AI layer was changed)

## Multi-repo Projects
If .vibekit.json repos.type = "multi":
- Run tests for EACH affected repo, not just current
- Note which repo each test command runs in

## Gate
All pass → approve for /deploy
Any fail → route to pdca-act agent with exact failure details
DO NOT mark complete until ALL criteria tested with real commands.
