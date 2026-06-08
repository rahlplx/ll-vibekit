# ll-vibekit

> **Lab Launchpad Unified Vibe Coding Harness**
> Universal SaaS + Mobile builder for non-technical founders and solo developers.
> Works with: Claude Code · Opencode · Codex CLI · Cursor · Gemini CLI

---

## What This Is

A unified vibe coding harness merging the best of:

| Source | Stars | What We Took |
|--------|-------|--------------|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 209K | Agent library, SOUL.md, RULES.md, WORKING-CONTEXT.md |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 107K | ETHOS.md, SKILL.md template, context-save/restore |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 119K | Engineering skills (tdd, diagnose, prototype) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 169K | 4 behavioral rules (the most important file) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 48K | Hooks system, references, engineering skills |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 69K | Token efficiency skills (65% reduction) |
| [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) | — | PRP system (INITIAL.md → generate-prp → execute-prp) |
| [popup-studio-ai/bkit-claude-code](https://github.com/popup-studio-ai/bkit-claude-code) | — | PDCA agents, QA agents, PM agents |
| [profullstack/vibe-stack](https://github.com/profullstack/vibe-stack) | 10 | HUMAN-TODO.md pattern, Android/iOS structure |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 56K | Best practice docs, changelog pattern |

---

## Products Covered

```
AgencyOS         SvelteKit + Go Fiber + FastAPI + Oracle ARM
Kalki AI         RAG platform
Any SaaS         Stack-agnostic skills work everywhere
Android app      React Native + Expo
iOS app          React Native + Expo (same codebase)
Marketing site   Astro + Cloudflare Pages
```

---

## 3-Command Workflow

```bash
# 1. Describe what you want (plain English)
nano INITIAL.md

# 2. Generate a full implementation plan
/generate-prp INITIAL.md

# 3. Execute the plan
/execute-prp PRPs/your-feature.md
```

---

## Quick Install

```bash
# Clone into your project
git clone https://github.com/rahlplx/ll-vibekit .ll-vibekit
cd .ll-vibekit && bash install.sh

# Or use gitingest to understand this repo first
gitingest https://github.com/rahlplx/ll-vibekit
```

---

## Structure

```
ll-vibekit/
├── CLAUDE.md          Karpathy 4 rules + LL stack rules
├── AGENTS.md          All agent team definitions
├── SOUL.md            Mission and values
├── RULES.md           Explicit non-negotiable rules
├── ETHOS.md           Principles and philosophy
├── CONTEXT.md         Product + stack context
├── WORKING-CONTEXT.md Current session state
├── HUMAN-TODO.md      Tasks only humans can do
├── INITIAL.md         Feature request template
├── agents/            35+ specialist agents
├── skills/            Engineering + SaaS + Mobile + Token efficiency
├── hooks/             Automated triggers and validators
├── PRPs/              Product Requirements Prompts
├── process/           Feature lifecycle management
├── .claude/commands/  Slash commands
├── android/           Android (React Native + Expo)
├── ios/               iOS (React Native + Expo)
├── references/        Checklists and patterns
├── best-practice/     Claude Code best practices
└── docs/              Guides and documentation
```

---

**Lab Launchpad · Bangladesh-first · Self-hosted · BYOK · Open source MIT**
