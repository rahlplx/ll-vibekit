# MEMORY/stack.md — Current Tech Stack
> Updated when stack decisions change. Never stale.

## AgencyOS Stack (LOCKED)
| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | SvelteKit + adapter-cloudflare | Workers (not Pages) |
| Edge API | Hono v4 on CF Workers | tRPC + REST /v1/ |
| Core API | Go Fiber v2 | Oracle ARM :8080 |
| AI API | FastAPI Python 3.12 | Oracle ARM :8001 |
| DB | PostgreSQL 17 | via PgBouncer :6432 |
| Cache | Valkey 8 | pub/sub + rate limit |
| Vectors | Qdrant | bge-m3 1024-dim |
| Storage | MinIO + CF R2 | private + public |
| Workflows | Temporal Cloud | free tier |
| Components | shadcn-svelte | dark theme |
| ORM | sqlc only | never GORM |
| Migrations | goose | SQL files |

## AI Models
| Model | Size | Use Case | Location |
|-------|------|----------|----------|
| Qwen3.6-35B-A3B Q4_K_M | ~18GB | Orchestrator | Oracle ARM Ollama |
| Phi-4-mini 3.8B | ~2.5GB | Fast tasks | Oracle ARM Ollama |
| Qwen3-Coder | varies | BYOK only | Tenant's key |
| BAAI/bge-m3 | 570MB | Embeddings | fastembed |

## Mobile Stack
| Layer | Technology |
|-------|-----------|
| Framework | React Native + Expo SDK 52 |
| Navigation | Expo Router |
| State | Zustand |
| Styling | NativeWind |
| Auth | expo-auth-session |
| Storage | expo-secure-store |
