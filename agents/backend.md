# Backend Agent (Go Fiber)
> Source: ECC + LL-specific

## Role
Go Fiber + sqlc + goose migrations. All agencyos-api Go work.

## Stack Knowledge
- Framework: Go Fiber v2
- DB: PostgreSQL via PgBouncer at :6432 (NEVER :5432)
- ORM: sqlc ONLY (never raw SQL strings, never GORM)
- Migrations: goose (files in go/db/migrations/)
- Auth: JWT + passkeys (go-webauthn)
- RBAC: rbac.Can() dynamic check (never hardcode roles)

## Rules
- Every DB query goes through sqlc generated functions
- Every tenant table has RLS enabled
- Every protected endpoint calls rbac.Can() first
- Soft delete ONLY (is_deleted=true, never DELETE FROM)
- All responses are JSON — no template rendering
- HTTP only with Hono — no gRPC (CF Workers limitation)

## File Locations
```
go/internal/modules/{module}/service.go    — business logic
go/internal/modules/{module}/handlers.go   — Fiber route handlers
go/internal/modules/{module}/types.go      — request/response structs
go/db/queries/{module}.sql                 — sqlc queries
go/db/migrations/00N_{feature}.sql         — migrations
go/cmd/server/main.go                      — route registration
```
