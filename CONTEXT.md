# CONTEXT.md — Product and Stack Context
> Read this before any task. Updated when products change.

---

## Lab Launchpad Products

### AgencyOS (primary)
AI-native social media management SaaS for marketing agencies.
Bangladesh-first (bKash payments, Bengali AI, Facebook-first), UK/USA secondary.
Stack: SvelteKit + Hono (CF Workers) + Go Fiber (Oracle ARM) + FastAPI + PostgreSQL + Qdrant

### Kalki AI
BYOK RAG platform for enterprises. Stack: TBD. Self-hosted first.

### Mobile (React Native + Expo)
Cross-platform mobile app. Same codebase for Android and iOS.
See android/SETUP.md and ios/SETUP.md.

---

## Default Tech Decisions

When building anything new, these are the defaults unless specified otherwise:

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend web | SvelteKit (adapter-cloudflare) | CF Workers SSR at edge |
| Frontend mobile | React Native + Expo | One codebase → iOS + Android |
| Edge API | Hono v4 on CF Workers | auth, tRPC, webhooks |
| Core API | Go Fiber v2 on Oracle ARM | all module logic + DB |
| AI layer | FastAPI + Python 3.12 | AI ecosystem native |
| Database | PostgreSQL 17 + PgBouncer (:6432) | multi-tenant RLS |
| Cache/Queue | Valkey 8 | pub/sub + rate limiting |
| Vector DB | Qdrant (bge-m3 1024-dim embeddings) | per-client collections |
| Object storage | MinIO (private) + CF R2 (public) | self-hosted first |
| Workflows | Temporal Cloud free tier | survives ARM reboots |
| Secrets | Doppler | never in .env files |

---

## Critical Constraints

- Oracle ARM Always Free: 24GB RAM — never exceed this
- Ollama/Qwen3.6: ~18GB — largest single service
- PostgreSQL connects via PgBouncer :6432, NOT :5432 directly
- Valkey pub/sub for real-time, NOT PG LISTEN/NOTIFY
- Bengali support required for all AI outputs (use BAAI/bge-m3)
- Passkeys + email/password fallback mandatory (BD Android compat)
