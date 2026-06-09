# HITL Flow — Human In The Loop
> Core AgencyOS pattern for AI-generated content approval

## WHEN TO USE
Every AI output that touches client deliverables.

## THE FLOW
```
Expert generates → validate confidence → LangGraph interrupt() → HITLQueue
     → SSE to browser → human reviews/edits → approve/reject
     → graph resumes → downstream action
```

## RULES
- Auto-approve threshold: 0.95 (never 0.90 — models are overconfident)
- Expiry: expires_at = NOW() + 72 hours
- Mobile: swipe right = approve, swipe left = reject
- Edit distance tracked (levenshtein trigger, needs fuzzystrmatch)
- NEVER execute actions without HITL approval

## AGENT NOTE
HITL is not a feature. It is the product.

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "ll-vibekit (LL-specific)"
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
    source: "ll-vibekit (LL-specific)"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
