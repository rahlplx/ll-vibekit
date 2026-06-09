# CI/CD
> Source: addy-skills ci-cd-and-automation

## Pipeline
```
git push main
    → GitHub Actions: go test + pytest + pnpm build
    → all pass → Coolify webhook → Oracle ARM deploy
    → health check: curl /health
    → Sentry release notify
```

## GitHub Actions Template
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Go
        run: cd go && go test ./...
      - name: Python
        run: cd ai && pytest tests/ -x -q
      - name: Svelte
        run: cd web && pnpm install && pnpm build
```

## Rules
- NEVER deploy without all tests passing
- Feature branches: test only (no deploy)
- Main: test + deploy on pass
- Rollback: Coolify one-click to previous container
