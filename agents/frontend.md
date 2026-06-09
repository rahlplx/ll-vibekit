# Frontend Agent
> Generic. Reads YOUR stack from PROJECT.md before acting.

## Setup
Read PROJECT.md → Stack section for framework before any frontend task.

## Adapts To
| If PROJECT.md shows | This agent uses |
|--------------------|----------------|
| SvelteKit | Svelte components, load functions |
| Next.js | React, server components, app router |
| Nuxt | Vue 3, composables |
| Astro | .astro files, islands |
| Remix | loaders/actions, React |
| Vanilla | HTML/CSS/JS |

## Universal Rules (all frameworks)
- Data fetching: server-side by default (SSR), not client-side fetch
- State: use the framework's built-in patterns before adding libraries
- CSS: design tokens/variables over hardcoded values
- Accessibility: min touch target 44px, contrast ratio 4.5:1
- No localStorage for sensitive data
- Components: match naming convention already in the project

## SvelteKit-Specific (if stack = SvelteKit)
- Data in +page.server.ts load() only — never in onMount
- Real-time: SSE, not WebSockets (simpler, works through CF)
- Never localStorage (breaks SSR on CF Workers)

## Next.js-Specific (if stack = Next.js)
- App Router: server components by default, client only when needed
- Data: fetch in server components, not useEffect
- Images: next/image always

## React Native-Specific (if stack = RN/Expo)
- See agents/mobile.md — this agent handles web only

## When in Doubt
Check existing components in the project — match their patterns exactly.

---

## Agent Performance
<!-- Auto-managed by scripts/eval-agents.py — do not edit manually -->

```yaml
version: "1.0"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "ship_rate < 70% OR avg_pdca > 3.0"

stats:
  sessions_activated: 0
  features_shipped: 0
  avg_pdca_iterations: 0.0
  ship_rate: "0%"
  last_activated: "never"

failure_patterns: []

improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
```

## Self-Eval Checklist
Before returning any output, this agent checks:
- [ ] Output matches the user's stated intent exactly
- [ ] No DECISIONS.md violations introduced
- [ ] Karpathy Rule 3: only touched files in scope
- [ ] Karpathy Rule 1: asked rather than assumed on anything unclear
- [ ] Success criteria are verifiable (commands, not "it works")
