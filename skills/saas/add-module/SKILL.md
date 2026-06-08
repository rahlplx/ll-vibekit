# Add Full-Stack Module
> LL-specific skill for AgencyOS

## When to Use
When adding a completely new feature domain to AgencyOS.
Creates: DB migration + Go module + Svelte route.

## Steps
1. Read DECISIONS.md — confirm approach is compliant
2. Create migration: `go/db/migrations/00N_{module}.sql`
   - tenant_id FK to workspaces(id)
   - RLS policy
   - is_deleted soft delete
3. Run `goose up` — confirm migration succeeds
4. Create sqlc queries: `go/db/queries/{module}.sql`
5. Run `sqlc generate` — confirm types generated
6. Create Go module: `go/internal/modules/{module}/`
   - service.go (business logic)
   - handlers.go (Fiber routes)
   - types.go (request/response structs)
7. Register routes in `go/cmd/server/main.go`
8. Create Svelte route: `src/routes/(app)/{module}/`
   - +page.svelte (UI)
   - +page.server.ts (data loading via API)
9. Add RBAC permission in `go/db/migrations/001_initial.sql`
10. Verify success criteria

## Success Criteria
- [ ] Migration runs: `goose up` exits 0
- [ ] Go builds: `go build ./...` exits 0
- [ ] Route accessible at /app/{module}
- [ ] API returns correct JSON at /api/v1/{module}
