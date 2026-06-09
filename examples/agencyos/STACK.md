# AgencyOS Stack Reference
> Move AgencyOS-specific content here out of core harness.
> Reference this when working on AgencyOS projects.

## Stack (Locked)
| Layer | Technology |
|-------|-----------|
| Frontend | SvelteKit + adapter-cloudflare (Workers) |
| Edge API | Hono v4 on CF Workers |
| Core API | Go Fiber v2 on Oracle ARM |
| AI Layer | FastAPI + Python 3.12 |
| Database | PostgreSQL 17 via PgBouncer :6432 |
| Cache | Valkey 8 |
| Vectors | Qdrant (bge-m3, 1024-dim) |
| Storage | MinIO + CF R2 |
| Workflows | Temporal Cloud free tier |
| Hosting | Oracle ARM 24GB + Coolify |

## Critical Rules (AgencyOS only)
- Go connects to PgBouncer :6432, NEVER :5432
- Embedding: BAAI/bge-m3 ONLY (multilingual, Bengali-capable)
- Passkeys + email/password fallback (50-60% BD Android lacks passkey support)
- Auto-approve HITL at 0.95 confidence (not 0.90)
- Valkey pub/sub, not PG LISTEN/NOTIFY
- is_deleted soft delete only
- BYOK first: get_byok_key() before any LiteLLM call

## Use This Reference
When working on AgencyOS, point agents to this file:
@examples/agencyos/STACK.md

Or run /setup and fill PROJECT.md from this file.
