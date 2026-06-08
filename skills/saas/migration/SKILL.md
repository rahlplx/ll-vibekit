# Database Migration
> LL-specific skill — PostgreSQL + goose + RLS

## When to Use
When adding new tables or columns to the database.

## Template
```sql
-- go/db/migrations/00N_{description}.sql

-- ALWAYS: fuzzystrmatch for text operations
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

-- Main table
CREATE TABLE {table_name} (
    id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id       UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
    -- your columns here --
    is_deleted      BOOLEAN DEFAULT FALSE,   -- ALWAYS soft delete
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Index on tenant (always)
CREATE INDEX idx_{table}_tenant ON {table_name}(tenant_id) WHERE NOT is_deleted;

-- RLS (ALWAYS on tenant tables)
ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY;
CREATE POLICY {table}_tenant_isolation ON {table_name}
    USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

## Rules
- NEVER use port 5432 — Go connects via PgBouncer at 6432
- ALWAYS add is_deleted
- ALWAYS add RLS policy
- ALWAYS add tenant_id FK
- NEVER use PG LISTEN/NOTIFY (Valkey pub/sub instead)
