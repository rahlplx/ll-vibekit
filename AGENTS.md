# AGENTS.md — ll-vibekit Agent Team
> All available agents. Load specific agents based on task routing.
> Sources: ECC (209K★) · addy-skills (48K★) · bkit · gstack

---

## CORE TEAM

| Agent | File | Role | When to Use |
|-------|------|------|-------------|
| Architect | agents/architect.md | System design, PRP generation, DECISIONS.md compliance | Planning new features |
| Backend | agents/backend.md | Go Fiber + sqlc + migrations (LL stack) | Go/API work |
| Frontend | agents/frontend.md | SvelteKit + shadcn-svelte + Tailwind (LL stack) | Svelte/UI work |
| Mobile | agents/mobile.md | React Native + Expo + iOS + Android | Mobile features |
| AI Layer | agents/ai-layer.md | FastAPI + PydanticAI + LangGraph + Agno + RAG | AI/expert work |
| Database | agents/database.md | PostgreSQL + sqlc + goose + RLS | DB migrations |
| DevOps | agents/devops.md | Coolify + Oracle ARM + Temporal Cloud | Deploy/infra |
| QA | agents/qa.md | Tests, success criteria verification | Validation |
| Code Reviewer | agents/code-reviewer.md | Review code vs DECISIONS.md | Code review |
| Security | agents/security.md | Security audit, OWASP, SQL injection | Security review |

## QUALITY CYCLE (bkit PDCA pattern)

| Agent | Role |
|-------|------|
| agents/pdca-plan.md | Plan the sprint, write specs |
| agents/pdca-do.md | Execute the implementation |
| agents/pdca-check.md | Verify output vs success criteria |
| agents/pdca-act.md | Fix gaps, update memory |

## SPECIALIST AGENTS

| Agent | Source | Role |
|-------|--------|------|
| agents/pm-lead.md | bkit | Product management, roadmap |
| agents/pm-prd.md | bkit | Write PRDs from feature requests |
| agents/chief-of-staff.md | ECC | Cross-team coordination |
| agents/cavecrew-builder.md | caveman | Token-efficient implementation |
| agents/cavecrew-reviewer.md | caveman | Token-efficient review |

---

## HOW TO ACTIVATE AN AGENT

In Claude Code or Opencode, add to your request:
```
@agents/architect.md Please review this PRP before I execute it.
@agents/mobile.md Add push notification support to the React Native app.
```

Or let the router in CLAUDE.md select automatically based on task type.
