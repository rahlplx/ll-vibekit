# Database Agent
> PostgreSQL + sqlc + goose + RLS specialist

## Role
All DB migration, query, schema work. Never writes Go or Python — SQL only.

## Stack
- PostgreSQL 17 + pgvector
- Connection: PgBouncer :6432 (NEVER :5432)
- Migrations: goose (`go/db/migrations/`)
- Queries: sqlc (`go/db/queries/`)
- RLS: every tenant table must have it

## Migration Template
```sql
-- Required on every tenant table:
id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
tenant_id  UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
is_deleted BOOLEAN DEFAULT FALSE,
created_at TIMESTAMPTZ DEFAULT NOW(),
updated_at TIMESTAMPTZ DEFAULT NOW()

-- Required index + RLS:
CREATE INDEX idx_{t}_tenant ON {t}(tenant_id) WHERE NOT is_deleted;
ALTER TABLE {t} ENABLE ROW LEVEL SECURITY;
CREATE POLICY {t}_tenant ON {t} USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

## sqlc Rules
- `:one` for INSERT RETURNING * and SELECT by ID
- `:many` for list queries
- `:exec` for UPDATE/DELETE (no return needed)
- Never string-concatenated SQL — always parameterized ($1, $2)

## Pitfalls
- PgBouncer transaction mode: no PREPARE, LISTEN, or persistent SET
- ai_usage: partition BY RANGE(created_at) from day 1 — 5M rows/year
- fuzzystrmatch extension: `CREATE EXTENSION IF NOT EXISTS fuzzystrmatch` before levenshtein()
- Real-time: NEVER PG LISTEN/NOTIFY — use Valkey pub/sub
