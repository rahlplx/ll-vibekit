# Context Restore
> Companion to context-save. Source: gstack pattern.

## When to Use
Start of new session to resume from where you left off.
After Claude Code compacts context mid-session.

## Usage
```
/context-restore {session-name}
```

## What Gets Loaded
1. WORKING-CONTEXT.md — what was in progress
2. DISCOVERIES.md — last 5 entries
3. MEMORY/stack.md — tech stack decisions
4. MEMORY/modules.md — existing modules

## Load Only What Task Needs
- Continuing a feature: + MEMORY/patterns.md + that module file
- Debugging: + MEMORY/mistakes.md + broken file
- Never load all MEMORY/ files at once

## Manual Restore (no command)
Read WORKING-CONTEXT.md and tell me:
1. What was being built
2. What is left to do
3. The last file modified
Then continue from that point.
