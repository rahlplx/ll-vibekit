# /route — Auto-Router
Read the user's request and determine exactly what to do.

## Classification Tree (deterministic)

1. Contains "fix", "bug", "error", "broken"?
   → INTENT: fix-bug
   → Load: MEMORY/mistakes.md + relevant module files
   → Route: code-reviewer → backend/frontend/mobile agent

2. Contains "migrate", "table", "column", "database", "SQL"?
   → INTENT: db-change
   → Route: database agent
   → Skill: skills/saas/migration/SKILL.md

3. Contains "expert", "E1"-"E15", "AI agent", "HITL"?
   → INTENT: ai-feature
   → Route: ai-layer agent
   → Load: MEMORY/stack.md

4. Contains "mobile", "android", "iOS", "React Native"?
   → INTENT: mobile-feature
   → Route: mobile agent
   → Load: android/SETUP.md or ios/SETUP.md

5. Contains "deploy", "push", "ship", "production"?
   → INTENT: deploy
   → Check: HUMAN-TODO.md first
   → Route: devops agent

6. Contains "design", "UI", "component", "Svelte"?
   → INTENT: ui-feature
   → Route: frontend agent

7. Everything else?
   → INTENT: build-feature
   → Phase: 2 (plan first)
   → Route: architect → generate-prp
   → Next: /generate-prp INITIAL.md

## Output Format
```
INTENT: [classified type]
SCOPE: [layers affected]
AGENT: [which agent(s) to use]
DECISIONS TO CHECK: [from DECISIONS.md]
HUMAN ACTION NEEDED: [yes/no + what]
PHASE: [plan / implement / deploy]
NEXT COMMAND: [what to run]
```
