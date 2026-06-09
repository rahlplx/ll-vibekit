# Performance Checklist
> Source: addy-skills references/performance-checklist.md

## Database
- [ ] Indexes on new query columns (EXPLAIN ANALYZE confirms)
- [ ] No N+1 queries (use JOIN not loop)
- [ ] All list endpoints paginated (max 100/page)
- [ ] ai_usage partitioned by month (5M rows/year)
- [ ] PgBouncer pool sized correctly (max_client_conn=200)

## API (Go Fiber)
- [ ] Slow ops async (goroutines for non-blocking work)
- [ ] Stable data cached in Valkey with TTL
- [ ] Rate limiting per tenant (Valkey sliding window)
- [ ] Circuit breaker on agencyos-ai (sony/gobreaker)

## AI Layer
- [ ] All expert calls async (await litellm.acompletion)
- [ ] RAG: top_k=20 retrieve → rerank → top_k=5 inject
- [ ] Embeddings batched (not one-by-one)
- [ ] Ollama turbo3 KV cache mode enabled

## Oracle ARM Budget
- [ ] Total RAM < 24GB
- [ ] PostgreSQL memswap_limit = mem_limit (NEVER swap)
- [ ] vm.swappiness=1
- [ ] Ollama can use up to 32GB swap on /data volume
