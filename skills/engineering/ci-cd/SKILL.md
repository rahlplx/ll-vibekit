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

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "mattpocock/skills + addy-skills"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "avg_pdca_when_used > 2.5 OR ship_rate < 70%"

# Populated by eval-session.py after each use
stats:
  times_used: 0
  features_shipped_after_use: 0
  avg_pdca_iterations_when_used: 0.0
  ship_rate_when_used: "0%"
  last_used: "never"

# Auto-populated by scripts/eval-skills.py
failure_patterns: []

# Manual + auto improvement history
improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
    source: "mattpocock/skills + addy-skills"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
