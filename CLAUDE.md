# CLAUDE.md — ll-vibekit Master Rules
> Read this FIRST before any task. Every session, every time.
> Sources: karpathy-skills (169K★) + ECC (209K★) + addy-skills (48K★)

---

## IDENTITY
You are operating within ll-vibekit, Lab Launchpad's unified vibe coding harness.
Your job: convert plain English feature requests into production-grade software.
Current products: AgencyOS, Kalki AI, mobile apps (Android + iOS).

---

## KARPATHY'S 4 RULES (169K stars — most starred CLAUDE.md in history)

### Rule 1: NEVER ASSUME — ASK FIRST
If you are not sure about something, ask before proceeding.
Do NOT make silent assumptions and charge ahead.
A wrong assumption builds the wrong thing. Asking costs 5 seconds.

### Rule 2: NO OVER-ENGINEERING
Write the minimal code that solves the task. 50 lines, not 500.
Do NOT create abstractions, base classes, factories, or registries
unless explicitly asked or the pattern already exists in this codebase.

### Rule 3: STAY IN SCOPE
Only modify files/functions directly related to the task.
Do NOT refactor unrelated code while implementing a feature.
Do NOT "improve" code outside the task scope.

### Rule 4: DEFINE VERIFIABLE SUCCESS
Before starting, state what "done" looks like:
- Which test passes?
- Which endpoint returns what?
- Which file was created/modified?
Never finish without confirming success criteria are met.

---

## WORKFLOW (3 commands)

```
1. User fills INITIAL.md in plain English
2. Agent runs: /generate-prp INITIAL.md
3. Human approves PRP
4. Agent runs: /execute-prp PRPs/feature-name.md
5. Agent verifies all success criteria
6. Agent updates WORKING-CONTEXT.md + DISCOVERIES.md
```

---

## CONTEXT FILES (load selectively, not all at once)

| Task | Load These |
|------|-----------|
| Any task | CLAUDE.md + RULES.md (always) |
| AgencyOS | + agencyos-api/DECISIONS.md |
| New feature | + CONTEXT.md + MEMORY/modules.md |
| Mobile | + android/SETUP.md OR ios/SETUP.md |
| AI/expert | + MEMORY/stack.md |
| Debug | + MEMORY/mistakes.md |

**Token rule (caveman):** Never load all files. Load only what the current task needs.

---

## AGENT ROUTING

| User request contains | Route to |
|----------------------|----------|
| "new module" or "new feature" | architect → backend → frontend → qa |
| "fix" or "bug" or "broken" | code-reviewer → backend/frontend |
| "mobile" or "android" or "iOS" | mobile agent |
| "AI expert" or "E1" or "expert" | ai-layer agent |
| "deploy" or "push" or "ship" | devops agent |
| "design" or "UI" or "component" | frontend agent |
| "database" or "migration" or "sql" | database agent |
| "plan" or "PRP" or "INITIAL" | architect → generate-prp |

---

## HARNESS VERSION
ll-vibekit v1.0 — June 2026
Source repos: ECC · gstack · mattpocock · karpathy · addy · caveman · ctx_eng · bkit · vibe-stack · shanraisshan
