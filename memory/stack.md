# Stack Memory
> Current technology state across all Lab Launchpad products.
> Agent reads this at session start instead of asking "what's the stack?"

## AgencyOS
Frontend:   SvelteKit + Hono on Cloudflare Workers
Core API:   Go Fiber on Oracle ARM (port 8080)
AI Layer:   FastAPI + Python 3.12 (port 8001)
DB:         PostgreSQL 17 + PgBouncer (port 6432) + pgvector
Cache:      Valkey 8
Vectors:    Qdrant (per-client collections, size=1024)
Storage:    MinIO (private) + Cloudflare R2 (public)
Workflows:  Temporal Cloud (free tier)
LLM:        Qwen3.6-35B-A3B Q4_K_M + Phi-4-mini via Ollama
Embeddings: BAAI/bge-m3 ONLY (multilingual, Bengali-capable, 1024-dim)
Memory:     Mem0 V3 (Apache 2.0, uses existing Qdrant)
Infra:      Oracle ARM Free Tier (24GB) + Coolify

## Mobile (current state)
iOS:        React Native + Expo (preferred) or Swift + SwiftUI (native-only features)
Android:    React Native + Expo (preferred) or Kotlin + Jetpack Compose (native-only)

## Marketing sites
Engine:     Astro v5 + Cloudflare Pages
CMS:        Keystatic (git-native)
