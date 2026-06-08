# MEMORY/mistakes.md — Anti-Patterns Never To Repeat
> Add entries when something goes wrong.

## DB Mistakes

### gRPC from Hono (CF Workers)
- **Wrong:** Using gRPC for Hono→Go communication
- **Why wrong:** CF Workers V8 isolates have no TCP socket
- **Correct:** HTTP fetch() + X-Internal-Secret header

### bge-base-en-v1.5 for embeddings
- **Wrong:** Using English-only embedding model
- **Why wrong:** Bengali content produces near-random vectors
- **Correct:** BAAI/bge-m3 (multilingual, 1024-dim)

### Passing port 5432 in Go
- **Wrong:** Go Fiber connecting directly to PostgreSQL :5432
- **Why wrong:** PgBouncer in transaction mode, not direct
- **Correct:** Always connect to PgBouncer :6432

### navigator.gpu without adapter check
- **Wrong:** `if (navigator.gpu)` — always truthy even without GPU
- **Correct:** `await navigator.gpu?.requestAdapter()` — actually tests

## Agent Mistakes

### Auto-approve at 0.90 confidence
- **Wrong:** Using 0.90 threshold
- **Why wrong:** Models are overconfident. 0.90 lets too many bad outputs through
- **Correct:** 0.95 threshold

### LangGraph for simple Agno tasks
- **Wrong:** Using LangGraph for single-expert no-HITL calls (E8, E10, E13)
- **Why wrong:** 10,000× overhead vs Agno for simple calls
- **Correct:** Agno for E8/E10/E12/E13, LangGraph for E15 + HITL only

## Context Mistakes

### Loading entire DECISIONS.md for every task
- **Wrong:** Pre-loading all context files every session
- **Why wrong:** Wastes ~50% of context budget on irrelevant content
- **Correct:** Load only files relevant to the current task (CLAUDE.md says which)
