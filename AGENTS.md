# AGENTS.md — ll-vibekit Agent Team
> All available agents. Load specific agents based on task routing.
> Sources: ECC (209K★) · addy-skills (48K★) · bkit · gstack

---

## CORE TEAM

| Agent | File | Role | When to Use |
|-------|------|------|-------------|
| Architect | agents/architect.md | System design, PRP generation | Planning |
| Backend | agents/backend.md | API, DB, business logic (any stack) | Go/API/Server |
| Frontend | agents/frontend.md | UI, components (any framework) | Web UI |
| Mobile | agents/mobile.md | React Native + Expo + iOS + Android | Mobile |
| AI Layer | agents/ai-layer.md | LLMs, RAG, agents (any framework) | AI features |
| Database | agents/database.md | Migrations, queries, schema | DB work |
| DevOps | agents/devops.md | Deploy to any hosting platform | Deployment |
| QA | agents/qa-lead.md | Tests, success criteria | Validation |
| Code Reviewer | agents/code-reviewer.md | DECISIONS.md compliance | Review |
| Security | agents/security.md | Security audit | Before shipping |

## QUALITY CYCLE (bkit PDCA)

| Agent | Role |
|-------|------|
| agents/pdca-plan.md | Plan before coding |
| agents/pdca-do.md | Implement to spec |
| agents/pdca-check.md | Verify all criteria |
| agents/pdca-act.md | Fix + update memory |

## SPECIALIST AGENTS

| Agent | Source | Role |
|-------|--------|------|
| agents/pm-lead.md | bkit | Product management |
| agents/pm-prd.md | bkit | PRD creation |
| agents/chief-of-staff.md | ECC | Multi-agent coordination |
| agents/cavecrew-builder.md | caveman | Token-efficient build |
| agents/cavecrew-reviewer.md | caveman | Token-efficient review |

---

## SELF-EVAL REQUIREMENT

Every agent has a Self-Eval Checklist at the bottom of its file.
Before returning any output, the agent must internally verify:
- Output matches user's stated intent
- No DECISIONS.md violations
- Karpathy Rule 3: only touched files in scope
- Success criteria are verifiable commands, not vague statements

## PERFORMANCE TRACKING

Every agent has a Performance section with live stats:
```
scripts/eval-agents.py    → updates all agent stats
/report                   → shows rankings
/harness-health           → scores all agents 0-100
```

## ACTIVATE AN AGENT

```
@agents/architect.md Design the notifications module.
Or: let /route auto-select based on task type.
```

## IMPROVE AN AGENT

If an agent's ship_rate < 70% after 5+ uses:
1. Read its failure_patterns in the Performance section
2. Update its Rules or Steps accordingly
3. Bump version in improvement_log
4. Run: python3 scripts/eval-agents.py to reset stats for next period
