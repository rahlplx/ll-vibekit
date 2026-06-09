# Code Review
> Source: addyosmani/agent-skills (48K★)

## WHEN TO USE
Before every merge. After every /execute-prp.

## CHECKLIST
- [ ] Does it do what the PRP specified?
- [ ] Are success criteria all verifiable?
- [ ] DECISIONS.md: any violations?
- [ ] Karpathy Rule 2: any over-engineering?
- [ ] Karpathy Rule 3: any out-of-scope changes?
- [ ] Tests exist for the new code?
- [ ] Error handling for edge cases?
- [ ] No hardcoded secrets or credentials?

## OUTPUT
PASS — list what looks good  
FAIL — specific violations with line references

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
