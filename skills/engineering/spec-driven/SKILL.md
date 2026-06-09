# Spec-Driven Development
> Source: addyosmani/agent-skills (48K★), coleam00/context-engineering-intro

## WHEN TO USE
Any new feature. Always write the spec before writing code.

## STEPS
1. Write INITIAL.md describing the feature
2. Run /generate-prp INITIAL.md
3. Review PRP — approve or request changes
4. Run /execute-prp PRPs/name.md
5. Verify all success criteria
6. Update DISCOVERIES.md

## THE KEY RULE
Never implement without an approved PRP.
"We'll figure it out as we go" = context drift = wrong product.

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
