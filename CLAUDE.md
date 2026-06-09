# CLAUDE.md — ll-vibekit Universal Rules
> Read this FIRST on every session. Every project. Every time.
> Source: karpathy-skills (169K★) + ECC (209K★) + addy-skills (48K★)

---

## YOUR FIRST ACTION ON EVERY SESSION

1. Check if PROJECT.md exists in this project
   - YES → read it. It contains the project context, stack, and current sprint.
   - NO  → run /setup to generate it before doing anything else.

2. Read WORKING-CONTEXT.md if it exists (previous session state).

3. Load MEMORY/ files ONLY when needed:
   - patterns.md → when writing code
   - mistakes.md → when debugging
   - stack.md    → when making architecture decisions
   Never load all MEMORY/ files at once.

---

## KARPATHY'S 4 RULES (169K★ — most-starred CLAUDE.md ever)

### Rule 1: NEVER ASSUME — ASK FIRST
If you are not sure about something, ask before proceeding.
Silent assumptions are the #1 cause of failed agent sessions.

### Rule 2: NO OVER-ENGINEERING
Write the minimal code that solves the task.
No extra abstractions, base classes, or patterns unless the codebase already uses them.

### Rule 3: STAY IN SCOPE
Only modify files directly related to the task.
Do NOT refactor or "improve" code outside the task scope.

### Rule 4: DEFINE VERIFIABLE SUCCESS
Before starting, state what "done" looks like — specifically.
Never finish a task without explicitly verifying success criteria.

---

## WORKFLOW (works for any project)

```
1. /setup          → discover project, generate PROJECT.md (first time only)
2. Fill INITIAL.md → describe the feature in plain English
3. /generate-prp   → research codebase + write implementation plan
4. Review PRP      → human approves (2 min)
5. /execute-prp    → implement to spec
6. PDCA Check      → verify all success criteria
7. /context-save   → update WORKING-CONTEXT.md
```

---

## AGENT ROUTING (auto — run /route first)

| User says | Route to |
|-----------|---------|
| "new feature" / "build" | architect → /generate-prp |
| "fix" / "bug" / "error" | code-reviewer → diagnose skill |
| "mobile" / "iOS" / "Android" | mobile agent |
| "database" / "migration" | database agent |
| "deploy" / "ship" | devops agent → check HUMAN-TODO |
| "review" / "check" | code-reviewer |
| unknown | /route to classify |

---

## TOKEN BUDGET RULES

- Always active: CLAUDE.md + PROJECT.md (~2K tokens)
- Load on demand: MEMORY/patterns.md, specific module files
- Never preload: all agents, all skills, all memory simultaneously
- Context > 75%: activate /caveman for compression

---

## PROJECT-SPECIFIC RULES

All project-specific rules live in PROJECT.md, not here.
If PROJECT.md has a "Locked Decisions" section, those override general advice.
If PROJECT.md has a "Notes for AI Agents" section, treat those as hard rules.
