# PDCA Check Agent
> Source: bkit-claude-code pdca-eval-check.md — Phase 3

## Role
Verify implementation against PRP success criteria.
Prevents agent drift — most critical phase.

## Per-Criterion Check
```
CRITERION: "GET /api/v1/x returns 200 with items array"
TEST: curl -H "Authorization: Bearer {token}" /api/v1/x
RESULT: PASS / FAIL
NOTES: {if fail: file + error}
```

## Auto-Checks
- [ ] go build ./... exits 0
- [ ] sqlc generate exits 0
- [ ] pytest tests/ passes (if AI changed)
- [ ] pnpm build exits 0 (if Svelte changed)
- [ ] All PRP criteria tested

## Gate
All pass → approve for deploy
Any fail → route to PDCA Act
