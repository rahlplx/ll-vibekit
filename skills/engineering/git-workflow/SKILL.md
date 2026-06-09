# Git Workflow
> Source: addyosmani/agent-skills (48K★), mattpocock/skills (119K★)

## BRANCH NAMING
feature/{ticket}-description
fix/{ticket}-description
chore/{description}

## COMMIT FORMAT
type(scope): description

Types: feat | fix | chore | docs | test | refactor | perf
Examples:
  feat(content): add Bengali voice generation via MPT
  fix(hitl): correct expiry trigger when final_content is NULL
  chore(deps): update pydantic-ai to 0.0.46

## RULES
- One logical change per commit
- Never commit: .env files, node_modules, __pycache__
- Always run pre-commit-check.sh before committing
- Squash before merging to main

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
