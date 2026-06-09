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

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "mattpocock/skills + addy-skills"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "avg_pdca_when_used > 2.5 OR ship_rate < 70%"

# Populated by eval-session.py after each use
stats:
  times_used: 0
  features_shipped_after_use: 0
  avg_pdca_iterations_when_used: 0.0
  ship_rate_when_used: "0%"
  last_used: "never"

# Auto-populated by scripts/eval-skills.py
failure_patterns: []

# Manual + auto improvement history
improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
    source: "mattpocock/skills + addy-skills"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
