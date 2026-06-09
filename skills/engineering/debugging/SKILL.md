# Debugging
> Source: addy-skills debugging-and-error-recovery

## When to Use
Something is broken. Error message is unclear. Before writing any fix.

## Steps
1. Reproduce — confirm consistent, not flaky
2. Locate — exact file:line where it fails
3. Isolate — Go / Python / Svelte / DB / infra?
4. Trace — what input/state triggers it?
5. Hypothesize — 3 root causes, ranked by likelihood
6. Verify — add log or test to confirm cause
7. Fix — minimal change only

## Layer Debugging

### Go
```bash
log.Info("debug", "value", x, "tenant", tenantID)
go test ./internal/modules/{module}/... -v -run TestX
```

### Python
```python
logger.debug("debug", value=x, expert_id=self.expert_id)
pytest tests/ -v -k "test_x" -s
```

### Svelte
```typescript
console.log('load:', JSON.stringify(data))
// Check: browser console + terminal (pnpm dev)
```

### DB
```sql
SELECT current_setting('app.tenant_id');  -- verify RLS context
EXPLAIN ANALYZE SELECT ...;               -- check query plan
```

## Before Debugging
Read MEMORY/mistakes.md — has this happened before?

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
