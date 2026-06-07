# Mistakes Log
> Anti-patterns. What went wrong. Never repeat these.

## gRPC between Hono and Go
WHAT: tried to use gRPC for Hono (CF Workers) → Go (Oracle ARM)
WHY WRONG: CF Workers V8 isolates have no TCP socket. gRPC impossible.
CORRECT: HTTP fetch() with X-Internal-Secret header.

## bge-base-en-v1.5 for embeddings
WHAT: used English-only embedding model
WHY WRONG: Bengali text → near-random vectors → retrieval quality zero
CORRECT: BAAI/bge-m3 ALWAYS. 1024-dim. Multilingual.

## Auto-approve at 0.90 confidence
WHAT: set auto-approve threshold to 0.90
WHY WRONG: LLMs are overconfident. 0.90 lets too many bad outputs through.
CORRECT: 0.95 threshold. Research-backed.

## PG LISTEN/NOTIFY for real-time
WHAT: used PostgreSQL LISTEN/NOTIFY for events
WHY WRONG: PgBouncer transaction mode reassigns connections. LISTEN requires persistent connection.
CORRECT: Valkey pub/sub → SSE to browser.

## Turborepo monorepo
WHAT: tried to use Turborepo @agencyos/shared cross-repo imports
WHY WRONG: CF Workers build fails on cross-repo imports at build time.
CORRECT: Separate repos + generate types from Go OpenAPI spec.
