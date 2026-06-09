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
