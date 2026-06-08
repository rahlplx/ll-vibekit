# Context Save + Restore
> Source: garrytan/gstack (107K★)

## When to Use
Before ending a long session so context survives to next session.
Before Claude Code compacts context automatically.

## Save (run at session end)
```
/context-save {session-name}
```
This saves to WORKING-CONTEXT.md:
- Current task and progress
- Decisions made this session
- Files modified
- What's left to do
- Any open questions

## Restore (run at session start)
```
/context-restore {session-name}
```
This loads:
- WORKING-CONTEXT.md (session state)
- DISCOVERIES.md (accumulated knowledge)
- MEMORY/stack.md (tech decisions)
- MEMORY/modules.md (existing modules)

## Manual Save Format
When updating WORKING-CONTEXT.md manually:
```markdown
## Session: {date} {task-name}
### Completed
- [x] specific thing done
### In Progress
- [ ] thing started but not done
### Next Session Must
- start from: {file:line}
- check: {specific thing to verify}
### Decisions Made
- chose X over Y because Z
```
