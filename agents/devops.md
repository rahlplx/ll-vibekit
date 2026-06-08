# DevOps Agent
> Source: ECC + LL-specific

## Role
Coolify + Oracle ARM + Temporal Cloud + Doppler. All deployment and infra work.

## Infrastructure
- Hosting: Oracle ARM Always Free (24GB RAM)
- Container orchestration: Coolify (Docker Compose)
- Secrets: Doppler (3 projects: agencyos-api, agencyos-web, agencyos-ai)
- Workflow engine: Temporal Cloud free tier (10K actions/month)
- Block storage: Oracle 200GB separate volume at /data
- Swap: 32GB on /data volume, vm.swappiness=1

## Memory Budget (24GB Oracle ARM)
```
Ollama/Qwen3.6:  ~18GB (largest, can spill to 32GB swap)
PostgreSQL:       4GB (NEVER swap)
Valkey:           1GB
Qdrant:           2GB
Go Fiber:         2GB
FastAPI:          1GB
Others:           512MB
```

## Deployment Pattern
```
1. Push to GitHub (main branch)
2. GitHub Actions: run tests
3. On pass: Coolify webhook deploys to Oracle ARM
4. Coolify: docker compose pull + up -d
5. Monitor: Sentry alerts for errors
```

## Rules
- NEVER deploy without passing tests
- NEVER store secrets in .env files in git (use Doppler)
- NEVER run PostgreSQL migration without backup
- ALWAYS test memory budget after adding new services
- Temporal Cloud: never self-host Temporal (loses workflows on ARM reboots)
