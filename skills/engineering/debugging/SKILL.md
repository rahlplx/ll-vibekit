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
