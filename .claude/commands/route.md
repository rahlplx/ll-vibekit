# /route — Auto-Router
Read the user's request and PROJECT.md, then determine exactly what to do.

## Step 0: Always do first
1. Check if PROJECT.md exists. If not: run /setup first.
2. Read PROJECT.md Stack section to know the project's framework.
3. Check HUMAN-TODO.md — does this task require human action first?

## Classification Tree

### Fix / Debug (highest priority)
Keywords: "fix", "bug", "error", "broken", "failing", "crash", "wrong"
→ INTENT: fix-bug
→ Load: MEMORY/mistakes.md (check if seen before)
→ Route: code-reviewer → diagnose skill
→ Then: backend or frontend agent depending on where the error is

### Database / Migration
Keywords: "migration", "table", "column", "schema", "index", "seed", "db"
→ INTENT: db-change
→ Route: database agent
→ Skill: skills/saas/migration/SKILL.md
→ Commands: read .vibekit.json test_commands.migrate

### AI / Expert / LLM
Keywords: "expert", "E1" through "E15", "HITL", "llm", "prompt", "rag",
          "embedding", "vector", "ai agent", "langchain", "pydantic"
→ INTENT: ai-feature
→ Route: ai-layer agent
→ Skill: skills/saas/add-expert/SKILL.md (if new expert)
→ Check: PROJECT.md AI section for current AI stack

### Mobile
Keywords: "mobile", "ios", "android", "react native", "expo", "capacitor",
          "app store", "push notification", "swipe"
→ INTENT: mobile-feature
→ Route: mobile agent
→ Also load: agents/mobile-android.md or agents/mobile-ios.md
→ Skill: skills/mobile/react-native-expo/SKILL.md

### Deploy / Ship
Keywords: "deploy", "ship", "push to prod", "release", "go live"
→ INTENT: deploy
→ FIRST: check HUMAN-TODO.md — any blockers?
→ Route: devops agent
→ Command: /deploy
→ Read: .vibekit.json test_commands for CI/CD steps

### Frontend / UI
Keywords: "ui", "component", "page", "route", "svelte", "react", "vue",
          "button", "form", "layout", "design", "style"
→ INTENT: ui-feature
→ Route: frontend agent
→ Check: PROJECT.md Frontend section for framework

### New Feature (full-stack)
Keywords: "build", "add", "create", "implement", "new module", "new feature"
→ INTENT: build-feature
→ Phase: plan first (PDCA Plan)
→ Route: architect → /generate-prp
→ NEXT: /generate-prp INITIAL.md

### Review / Check
Keywords: "review", "check", "validate", "is this correct", "does this look right"
→ INTENT: review
→ Route: code-reviewer
→ Command: /review [file]

### Status / What's next
Keywords: "status", "where are we", "what's left", "catch me up", "what next"
→ INTENT: status
→ Command: /status
→ Load: WORKING-CONTEXT.md + process/features/active/

### Unknown / Unclear
→ Ask one clarifying question: "Is this a bug fix, new feature, or something else?"
→ Do NOT proceed until intent is clear
→ Karpathy Rule 1: never assume

## Output Format
```
INTENT:   {classified type}
REPOS:    {which repos are affected — from PROJECT.md related repos}
AGENT:    {which specialist agent to activate}
SKILL:    {which skill file to load, if applicable}
COMMANDS: {test/build commands from .vibekit.json}
BLOCKERS: {anything in HUMAN-TODO.md blocking this}
PHASE:    {plan | implement | verify | deploy}
NEXT:     {exact command or action to run}
```
