# Diagnose
> Source: mattpocock/skills (119K★)

## When to Use
When a bug or unexpected behavior appears and the root cause is unclear.
Before writing any fix, run this skill to understand what's actually happening.

## Steps
1. Read the error message or description of unexpected behavior completely
2. Identify which layer the problem is in (Go, Python, Svelte, DB, infra)
3. Find the exact file and line where the issue originates
4. Trace backwards: what input causes this? What state leads to this?
5. List 3 possible root causes, ranked by likelihood
6. Confirm the most likely cause before proposing a fix
7. State the fix in one sentence before writing code

## Output Format
```
ROOT CAUSE: [one sentence, confirmed]
EVIDENCE: [file:line or log snippet]
FIX: [one sentence description]
IMPACT: [which other files/services this fix touches]
```

## Rules
- Never propose a fix before identifying root cause
- If unsure between two causes, ask the human for more info
- Check MEMORY/mistakes.md — has this bug happened before?
