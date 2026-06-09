# PROJECT.md — AgencyOS
> Copy this to your agencyos-api project root and rename to PROJECT.md
> This is the ready-to-use PROJECT.md for AgencyOS specifically.

## What This Project Is
AgencyOS is an AI-native multi-tenant SaaS platform for social media marketing
agencies. Bangladesh-first (bKash payments, Bengali AI content, Facebook-first),
UK/USA secondary. Core mechanic: AI generates content, humans approve it (HITL).

## Project Type
Multi-tenant SaaS web app + mobile app (in progress)

## Stack
| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | SvelteKit + adapter-cloudflare | Workers, not Pages |
| Edge API | Hono v4 on CF Workers | tRPC + REST /v1/ |
| Core API | Go Fiber v2 | Oracle ARM :8080 |
| AI Layer | FastAPI Python 3.12 | Oracle ARM :8001 |
| Database | PostgreSQL 17 | via PgBouncer :6432 |
| Cache | Valkey 8 | pub/sub + rate limit |
| Vectors | Qdrant | bge-m3 1024-dim |
| Storage | MinIO + CF R2 | private + public |
| Workflows | Temporal Cloud | free tier |
| Mobile | React Native + Expo | in progress |
| Hosting | Oracle ARM 24GB + Coolify | |

## Key Directories
```
agencyos-api/go/internal/modules/   Go business modules
agencyos-api/go/db/migrations/      Database migrations
agencyos-api/go/db/queries/         sqlc SQL queries
agencyos-web/src/routes/(app)/      SvelteKit app routes
agencyos-ai/src/experts/            E1-E15 AI experts
agencyos-ai/src/prompts/            System prompt .md files
agencyos-ai/src/tools/              Web research, video gen tools
```

## Current Modules
| Module | Status | Location |
|--------|--------|----------|
| auth | in-progress | go/internal/modules/auth |
| content + E1 | in-progress | go/internal/modules/content |
| hitl | in-progress | go/internal/modules/hitl |
| social | planned | |
| gbp | planned | |
| billing | planned | |

## Locked Decisions
- Go connects to PgBouncer :6432, NEVER PostgreSQL :5432
- Embedding model: BAAI/bge-m3 ONLY (Bengali-capable, 1024-dim)
- Auth: passkeys PRIMARY + email/password FALLBACK (BD Android compat)
- HITL auto-approve: 0.95 threshold (not 0.90)
- Real-time: Valkey pub/sub (not PG LISTEN/NOTIFY)
- Soft delete: is_deleted=true ONLY (never DELETE FROM)
- BYOK: get_byok_key() before every LiteLLM call
- LangGraph for E15 orchestration; Agno for E8/E10/E12/E13
- Langfuse V2 pinned (V3 has ClickHouse overhead + licence risk)

## Human TODO
- [ ] Submit Meta App Review (pages_manage_posts) — 4-8 week wait — DO TODAY
- [ ] Register SSLCommerz merchant (7-10 days)
- [ ] Revoke exposed GitHub PAT: github.com/settings/tokens
- [ ] Set up Doppler: 3 projects (agencyos-api, agencyos-web, agencyos-ai)
- [ ] Configure Temporal Cloud namespace: cloud.temporal.io
- [ ] Pull Qwen3.6 on Oracle ARM: ollama pull qwen3.6:35b-a3b-q4_k_m

## Active Sprint
Sprint 1: auth module (passkeys + email fallback + JWT) + HITL engine

## Commands
```bash
cd agencyos-api/go && goose up     # run migrations
cd agencyos-api/go && sqlc generate # regenerate types
cd agencyos-api/go && go test ./...  # run tests
cd agencyos-web && pnpm build        # build SvelteKit
cd agencyos-ai && pytest tests/ -x   # run AI tests
```

## Notes for AI Agents
- For Go: use DECISIONS.md in agencyos-api for all architectural questions
- For Python: use bge-m3 embeddings — bge-base-en-v1.5 breaks Bengali RAG
- For Svelte: data loading only in +page.server.ts — never in onMount
- Bengali support is required for all AI content generation (BD market)
