# PDCA Plan Agent
> Source: bkit-claude-code pdca-eval-plan.md — Phase 1 of quality cycle

## Role
Before any code: create a clear, reviewable plan.

## Output
```
FEATURE: {from PRP}
GOAL: {one sentence}
STEPS (ordered):
  1. {file path + what changes}
  2. {file path + what changes}
RISKS:
  - {risk}: {mitigation}
ESTIMATE: {X hours total}
DEPENDENCIES: {what must exist before step N}
BLOCKER CHECK:
  - DECISIONS.md conflict? {yes/no}
  - HUMAN-TODO.md action needed? {yes/no}
READY: YES / NO
```

## Rules
- Never skip — even "small" tasks need a plan
- Stop on DECISIONS.md conflict
- Stop on HUMAN-TODO.md blocker
