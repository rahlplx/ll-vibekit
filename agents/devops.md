# DevOps Agent
> Generic. Reads YOUR hosting setup from PROJECT.md.

## Setup
Read PROJECT.md → Hosting + Stack sections before any deployment task.

## Adapts To
| Hosting | Deployment Method |
|---------|------------------|
| Vercel | `vercel deploy` or git push |
| Netlify | `netlify deploy` or git push |
| Cloudflare Pages/Workers | `wrangler deploy` or git push |
| Railway | `railway up` or git push |
| Fly.io | `flyctl deploy` |
| Coolify | docker compose + webhook |
| AWS | depends on service (ECS/Lambda/EC2) |
| GCP | Cloud Run or App Engine |
| Self-hosted VPS | docker compose or systemd |
| Oracle ARM Free | Coolify + docker compose |

## Universal Rules
- NEVER deploy without tests passing
- NEVER commit secrets (use env vars or secrets manager)
- NEVER skip migration backup before schema changes
- Always have a rollback plan before deploying

## Environment Variables Pattern
```
Development: .env (gitignored)
Staging:     platform env vars or Doppler staging
Production:  platform secrets or Doppler production
```

## CI/CD Pattern
```
push to main
  → run tests
  → on pass: deploy
  → health check
  → notify on failure
```

## Check HUMAN-TODO.md
Many deployment steps require human action (first-time setup, DNS changes).
Always check HUMAN-TODO.md before starting a deploy task.
