# Error Recovery
> For when something breaks mid-implementation.

## When to Use
A command fails, a test breaks, or the agent gets stuck.
Before retrying blindly — recover properly.

## Decision Tree

### Migration failed (goose up error)
```
1. Run: goose status  (see which migration failed and why)
2. Fix the SQL error in the migration file
3. If already partially applied: goose down (rolls back last migration)
4. Fix the issue
5. Run: goose up again
NEVER: delete the migration file and recreate (breaks migration history)
```

### Go build failed
```
1. Read the error output completely (not just the last line)
2. Identify: compilation error? import error? type mismatch?
3. Search MEMORY/mistakes.md for this error type
4. Fix ONLY the reported error — do not touch other files
5. Run: {test_commands.build} again
```

### Python import failed
```
1. Check: is the package in pyproject.toml / requirements.txt?
2. Check: is the import path correct (relative vs absolute)?
3. Check: is __init__.py missing?
4. Run: python -c "import {module}" to test directly
```

### Svelte build failed
```
1. Run: pnpm build 2>&1 | head -50  (first 50 lines usually have the real error)
2. TypeScript errors: check the type mismatch — do not cast with `as any`
3. Missing import: add the import, do not suppress the error
```

### Tests failing after implementation
```
1. Did I touch files outside the PRP scope? (Karpathy Rule 3 violation)
2. Did the implementation match the PRP exactly?
3. Run: git diff to see exactly what changed
4. If unintended changes: revert them, rerun tests
```

### Agent stuck in a loop
```
1. Stop. Type: "Stop. Let's diagnose before continuing."
2. Run /status to see current state
3. Run /review [file] to check the last file written
4. Identify: where did the agent diverge from the PRP?
5. Revert to last known good state: git stash
6. Re-read PRP, restart from the failed step only
```

## NEVER
- Retry the same command 3+ times without understanding the error
- Delete and recreate files to "fix" them
- Continue to next step when current step is failing
- Add error suppression (try/except: pass, || true) to "fix" failures

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "mattpocock/skills + addy-skills"
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
    source: "mattpocock/skills + addy-skills"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
