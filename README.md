# ll-vibekit

> **Lab Launchpad Unified Vibe Coding Harness**
> Universal SaaS + Mobile builder. For non-technical founders and solo developers.
> Works with: Claude Code · Opencode · Codex CLI · Cursor · Gemini CLI

---

## What This Is

A unified vibe coding harness merging the best of 14 trending repos (gitingested + analyzed):

| Source | Stars | What We Extracted |
|--------|-------|-------------------|
| affaan-m/ECC | 209K | Agent library, SOUL.md, RULES.md, WORKING-CONTEXT.md |
| garrytan/gstack | 107K | ETHOS.md, SKILL.md template, context-save/restore |
| mattpocock/skills | 119K | Engineering skills (tdd, diagnose, prototype) |
| multica-ai/andrej-karpathy-skills | 169K | 4 behavioral rules — the most important file |
| addyosmani/agent-skills | 48K | Hooks system, references checklists |
| JuliusBrussee/caveman | 69K | Token efficiency (65% reduction) |
| coleam00/context-engineering-intro | — | PRP system: INITIAL.md → generate-prp → execute-prp |
| popup-studio-ai/bkit-claude-code | — | PDCA quality cycle, QA + PM agents |
| profullstack/vibe-stack | — | HUMAN-TODO.md, Android/iOS structure |
| shanraisshan/claude-code-best-practice | 56K | Best practice docs |
| InsForge/InsForge | 2K | Backend infra patterns |
| withkynam/vibecode-pro-max-kit | — | Feature lifecycle process/ system |
| sickn33/antigravity-awesome-skills | 39K | Skills library patterns |
| rtk-ai/rtk | 59K | Token efficiency docs |

---

## Products Covered

```
AgencyOS         SvelteKit + Go Fiber + FastAPI + Oracle ARM
Kalki AI         RAG platform
Any SaaS         Stack-agnostic skills work everywhere
Android app      React Native + Expo
iOS app          React Native + Expo (same codebase)
Marketing sites  Astro + Cloudflare Pages
```

---

## 3-Command Workflow

```bash
# 1. Describe what you want in plain English
nano INITIAL.md

# 2. Generate full implementation plan
/generate-prp INITIAL.md

# 3. Execute the plan
/execute-prp PRPs/your-feature.md
```

---

## Quick Install

```bash
# Install gitingest to understand any repo before using it
pip install gitingest

# Clone harness
git clone https://github.com/rahlplx/ll-vibekit .ll-vibekit
cd .ll-vibekit && bash install.sh

# Or understand this repo first
gitingest https://github.com/rahlplx/ll-vibekit
```

---

## Structure (109 files)

```
ll-vibekit/
├── CLAUDE.md              Karpathy 4 rules + LL rules (read FIRST always)
├── AGENTS.md              All agent team definitions + routing table
├── SOUL.md                Mission and values
├── RULES.md               10 explicit non-negotiable rules
├── ETHOS.md               Principles and philosophy
├── CONTEXT.md             Products + stack reference
├── WORKING-CONTEXT.md     Current session state (updated each session)
├── DISCOVERIES.md         Accumulated knowledge (grows over time)
├── HUMAN-TODO.md          Tasks ONLY humans can do (agents skip these)
├── INITIAL.md             Feature request template (start here)
├── SKILL.md.tmpl          Template for creating new skills
├── install.sh             One-command install
├── .mcp.json              MCP server config
│
├── agents/ (19 files)
│   ├── architect.md       System design + PRP generation
│   ├── backend.md         Go Fiber + sqlc
│   ├── frontend.md        SvelteKit + shadcn-svelte
│   ├── mobile.md          React Native + Expo
│   ├── mobile-android.md  Android-specific
│   ├── mobile-ios.md      iOS-specific
│   ├── ai-layer.md        FastAPI + PydanticAI + LangGraph + Agno
│   ├── database.md        PostgreSQL + sqlc + goose
│   ├── devops.md          Coolify + Oracle ARM + Temporal
│   ├── qa-lead.md         Quality assurance
│   ├── code-reviewer.md   DECISIONS.md compliance review
│   ├── security.md        OWASP security audit
│   ├── chief-of-staff.md  Multi-agent coordination (ECC)
│   ├── pm-lead.md         Product management (bkit)
│   ├── pm-prd.md          PRD creation (bkit)
│   ├── pdca-plan.md       PDCA Phase 1: Plan
│   ├── pdca-do.md         PDCA Phase 2: Do
│   ├── pdca-check.md      PDCA Phase 3: Check (prevents agent drift)
│   ├── pdca-act.md        PDCA Phase 4: Act + memory update
│   └── cavecrew-builder.md Token-efficient implementation (caveman)
│
├── skills/
│   ├── engineering/       diagnose, tdd, api-design, debugging, ci-cd, code-review
│   ├── saas/              add-module, migration, auth-flow, hitl-flow, add-expert, a2a-endpoint, ai-employee
│   ├── mobile/            react-native-expo, react-native-setup, android-kotlin, ios-swift
│   └── token-efficiency/  caveman, context-save
│
├── hooks/ (5 files)
│   ├── hooks.json         Claude Code hook registrations
│   ├── session-start.sh   Auto-load context at session start
│   ├── sdd-cache-pre.sh   Validate before file writes
│   ├── sdd-cache-post.sh  Log after file writes
│   └── simplify-ignore.sh Warn on over-engineering (>300 lines)
│
├── .claude/commands/ (10 files)
│   ├── route.md           AUTO-ROUTER: classifies task, picks agent+skill
│   ├── generate-prp.md    INITIAL.md → PRP
│   ├── execute-prp.md     PRP → code
│   ├── caveman.md         Token efficiency mode on/off
│   ├── deploy.md          Deploy to Coolify + Oracle ARM
│   ├── status.md          Project status summary
│   ├── discover.md        Update DISCOVERIES.md
│   └── review.md          DECISIONS.md compliance check
│
├── PRPs/
│   ├── templates/         full-stack, mobile, prp_base
│   └── examples/          001-gbp-review-reply, 002-weekly-analytics-report
│
├── MEMORY/
│   ├── stack.md           Current tech stack (never stale)
│   ├── patterns.md        Code patterns agents must follow
│   ├── mistakes.md        Anti-patterns never to repeat
│   └── modules.md         All modules + API contracts
│
├── process/               Feature lifecycle (vibecode-pro pattern)
│   ├── features/backlog/  Ideas not started
│   ├── features/active/   Currently building
│   └── features/completed/ Shipped features
│
├── android/SETUP.md       Android setup (React Native + Expo)
├── ios/SETUP.md           iOS setup (React Native + Expo)
│
├── references/            Performance, accessibility, security, testing checklists
├── best-practice/         Commands, memory, MCP, subagents
└── docs/                  HOW-TO-USE, PRODUCTS, SKILLS-REGISTRY, CONTRIBUTING, GITINGEST
```

---

**Lab Launchpad · Bangladesh-first · BYOK · Self-hosted · MIT**
