# ll-vibekit
> Lab Launchpad Vibe Kit — Unified AI agent harness for SaaS, iOS, Android, web.

Merged from top GitHub trending repos Jan–Jun 2026. Verified with gitingest.
Works with: Claude Code, Codex, OpenCode, Cursor, Gemini CLI, Roo Code.

## What this is

A cognitive harness — not a boilerplate. Drop it into any project and your AI agent inherits:
- Behavioural guardrails (Karpathy 4 rules + caveman token rules)
- 60+ curated skills across SaaS, mobile, web, AI, DevOps
- 20+ specialist agents (PM, QA, architect, mobile, security)
- PRP system (INITIAL.md → /generate-prp → /execute-prp)
- Self-improving memory (DISCOVERIES.md compounds session to session)
- Android (Kotlin/Jetpack) + iOS (Swift/SwiftUI) starter templates
- Cross-agent: CLAUDE.md + GEMINI.md + CURSOR.md + .roo/rules

## Install (30 seconds)

```bash
# Into any project
git clone https://github.com/rahlplx/ll-vibekit /tmp/ll-vibekit
cp -r /tmp/ll-vibekit/.claude /tmp/ll-vibekit/CLAUDE.md /tmp/ll-vibekit/AGENTS.md .
cp /tmp/ll-vibekit/INITIAL.md /tmp/ll-vibekit/DISCOVERIES.md /tmp/ll-vibekit/HUMAN-TODO.md .
```

## 3-command workflow

```
/generate-prp INITIAL.md    # Describe feature → PRP written
# Review PRP (2 min)
/execute-prp PRPs/name.md   # Implement to spec, hooks validate
```

## Sources (gitingest-verified, Jan–Jun 2026)

| Repo | Stars | What was taken |
|---|---|---|
| affaan-m/ECC | 209K | Harness architecture, agent pattern |
| garrytan/gstack | 107K | SKILL.md.tmpl format, ETHOS.md, DESIGN.md |
| mattpocock/skills | 119K | Engineering skills (TDD, ADR, diagnose, prototype) |
| multica-ai/andrej-karpathy-skills | 169K | Karpathy 4 behavioural rules |
| addyosmani/agent-skills | 48K | 22 production skills, agents, hooks, references |
| JuliusBrussee/caveman | 69K | Token reduction skills, cross-agent GEMINI.md, hooks |
| coleam00/context-engineering-intro | — | PRP system (.claude/commands, INITIAL.md) |
| popup-studio-ai/bkit-claude-code | — | 34 specialist agents (PM/QA/sprint/security) |
| withkynam/vibecode-pro-max-kit | — | Development protocols, process system |
| nexu-io/open-design | 60K | Design skills, CONTEXT.md pattern |
| profullstack/vibe-stack | — | Android+iOS templates, HUMAN-TODO.md, .roo/rules |

## Folder structure

```
ll-vibekit/
├── CLAUDE.md          Root behavioural rules (Karpathy + token)
├── AGENTS.md          Agent team definitions
├── GEMINI.md          Gemini CLI rules (from caveman)
├── CURSOR.md          Cursor rules (from karpathy)
├── ETHOS.md           Philosophy (from gstack)
├── DESIGN.md          Design principles (from gstack)
├── INITIAL.md         Feature request template
├── DISCOVERIES.md     Self-improving session memory
├── HUMAN-TODO.md      Tasks only humans can do
├── DECISIONS.md       Locked technical decisions (for LL products)
├── .claude/
│   ├── commands/      Slash commands
│   └── hooks/         Auto-validators
├── .roo/rules/        Roo Code rules
├── agents/            Specialist agents (PM, QA, mobile, security)
├── skills/
│   ├── engineering/   From mattpocock + addy-skills
│   ├── token/         From caveman
│   ├── saas/          SaaS-specific skills
│   ├── mobile/        iOS + Android skills
│   ├── design/        From open-design
│   └── devops/        Deployment skills
├── process/           From vibecode-pro (development protocols)
├── mobile/
│   ├── android/       Kotlin + Jetpack Compose starter
│   └── ios/           Swift + SwiftUI starter
├── PRPs/
│   ├── templates/     PRP templates
│   └── examples/      Completed PRPs
└── memory/            Persistent context files
```

## Products this covers

- AgencyOS (SvelteKit + Go + FastAPI)
- Kalki AI (RAG platform)
- Any SaaS product
- Android app (Kotlin + Jetpack Compose)
- iOS app (Swift + SwiftUI)
- Marketing site (Astro + Cloudflare Pages)

**Lab Launchpad · Sylhet · 2026**
