# AGENTS.md — ll-vibekit Agent Team
> Merged from: addyosmani/agent-skills (48K★), garrytan/gstack (107K★), caveman (69K★), bkit (34 agents)
> Load relevant agents for each task. Not all agents for every task.

---

## CORE TEAM (always available)

**Architect** — designs solutions, checks DECISIONS.md, writes PRPs, validates scope
**Reviewer** — code review against decisions, karpathy rules, project patterns  
**QA Lead** — defines success criteria, runs tests, blocks completion if criteria unmet

---

## SPECIALIST AGENTS

**Frontend Dev** — SvelteKit, React, React Native, Expo, Astro, shadcn, Tailwind
**Backend Dev (Go)** — Go Fiber, sqlc, PgBouncer, Temporal, REST
**Backend Dev (Python)** — FastAPI, PydanticAI, LangGraph, Agno, LiteLLM
**Mobile Dev (iOS)** — Swift, SwiftUI, Xcode, App Store guidelines
**Mobile Dev (Android)** — Kotlin, Jetpack Compose, Gradle, Play Store guidelines
**Database** — PostgreSQL, migrations, RLS, sqlc queries, Qdrant
**DevOps** — Coolify, Docker, Oracle ARM, Cloudflare, GitHub Actions
**Security** — OWASP, auth, vault, GDPR, rate limiting, injection prevention
**AI Layer** — RAG, embeddings, HITL, expert panel, Mem0, Temporal workflows
**Product Manager** — PRDs, user stories, acceptance criteria, backlog, sprint planning
**Designer** — UI/UX, design tokens, component library, dark theme, mobile-first
**Sprint Master** — task breakdown, estimation, velocity, retrospectives

---

## AGENT USAGE PATTERN
```
# In .claude/agents/{agent-name}.md
# Claude Code auto-loads on /agent {name} command
# Or reference in prompt: "Act as the Mobile Dev agent"
```

---

## SOURCES
- PM/QA/Sprint agents: popup-studio-ai/bkit-claude-code
- Code-reviewer, security-auditor: addyosmani/agent-skills  
- CEO/Designer persona: garrytan/gstack
- CaveCreW (builder/investigator/reviewer): juliusbrussee/caveman
- Cross-model agent patterns: shanraisshan/claude-code-best-practice
