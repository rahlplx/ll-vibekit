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
