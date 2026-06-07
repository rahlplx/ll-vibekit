# PRP Template — Full Stack Feature
> Use for: features touching Go + Svelte + Python

---
# PRP: {Feature Name}
> Generated: {date}
> Repos: agencyos-api + agencyos-web [+ agencyos-ai]

## Goal
{One sentence}

## Success Criteria
- [ ] {Testable: endpoint returns X with status Y}
- [ ] {Testable: UI shows Z on /route}
- [ ] {Testable: AI expert generates non-empty output}

## What NOT to change
- {file/module} — not in scope

## DECISIONS.md compliance
- [ ] DB port 6432 (PgBouncer)
- [ ] Embeddings: bge-m3
- [ ] Auth fallback: passkeys + email/password
- [ ] Soft delete: is_deleted=true
- [ ] RBAC: rbac.Can() check

## Database (if new tables)
```sql
-- Migration go/db/migrations/00N_{feature}.sql
```

## API (Go Fiber)
```
{METHOD} /api/v1/{route} → {handler}
```

## UI (SvelteKit)
```
src/routes/(app)/{route}/+page.svelte
```

## AI (if expert involved)
```
Expert: E{N}
ROUTING_TABLE: ({module}, {action}) → "E{N}"
```

## Implementation order
1. Migration
2. sqlc queries
3. Go module
4. Svelte route
5. Tests

## Edge cases
1. {case}
2. {case}
3. {case}
