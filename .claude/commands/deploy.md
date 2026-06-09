# /deploy — Deploy to Production

## Pre-flight
- [ ] All tests pass locally (go test, pytest, pnpm build)
- [ ] WORKING-CONTEXT.md updated
- [ ] No blocking items in HUMAN-TODO.md
- [ ] Migrations ran: goose up
- [ ] Secrets in Doppler (not in .env files)

## Deploy
```bash
git add -A
git commit -m "feat: {feature} — PRP #{n} complete"
git push origin main
# GitHub Actions runs tests → Coolify deploys on pass
```

## Verify
```bash
curl https://agencyos.app/health
# {"status":"ok","version":"1.x.x"}
```

## Post-Deploy (first 30 min)
- Monitor Sentry for new errors
- Verify Evolution API still connected (WhatsApp can drop on redeploy)
- Check HITL queue still processes
