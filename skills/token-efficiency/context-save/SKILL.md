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

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "JuliusBrussee/caveman + garrytan/gstack"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "avg_pdca_when_used > 2.5 OR ship_rate < 70%"

# Populated by eval-session.py after each use
stats:
  times_used: 0
  features_shipped_after_use: 0
  avg_pdca_iterations_when_used: 0.0
  ship_rate_when_used: "0%"
  last_used: "never"

# Auto-populated by scripts/eval-skills.py
failure_patterns: []

# Manual + auto improvement history
improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
    source: "JuliusBrussee/caveman + garrytan/gstack"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
