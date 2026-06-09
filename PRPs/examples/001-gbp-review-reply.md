# PRP: GBP Review Reply Auto-Draft
> Completed example — use as reference when writing new PRPs.
> Status: COMPLETED

## Goal
E7 automatically drafts replies to unanswered GBP reviews, queueing in HITL.

## Success Criteria (all verified)
- [x] GET /api/v1/gbp/reviews returns unanswered reviews
- [x] E7 generates draft reply with confidence >= 0.70
- [x] HITL queue shows draft under "GBP Reviews" label
- [x] Approve posts reply to Google via GBP API
- [x] Review marked 'replied' after approval
- [x] Mobile: visible in /hitl screen with swipe gesture

## Files In Scope
- go/db/migrations/004_gbp_reviews.sql
- go/db/queries/gbp.sql
- go/internal/modules/gbp/service.go
- go/internal/modules/gbp/handlers.go
- src/experts/e7_gbp.py
- src/prompts/e7_gbp.md
- agencyos-web/src/routes/(app)/gbp/+page.svelte

## Files NOT In Scope
- billing module
- auth module
- E1 content expert

## DECISIONS.md Compliance
- [x] RLS on gbp_reviews table
- [x] Valkey pub/sub for HITL notification
- [x] is_deleted soft delete
- [x] 0.95 auto-approve threshold

## Implementation Order (executed)
1. Migration 004_gbp_reviews.sql — goose up
2. sqlc generate
3. Go GBP service + handlers
4. Register /api/v1/gbp routes
5. E7 expert + src/prompts/e7_gbp.md
6. ROUTING_TABLE: ("gbp","review_reply") = "E7"
7. Svelte route /app/gbp

## Edge Cases Handled
1. GBP API rate limit: Temporal exponential backoff retry
2. No unanswered reviews: empty array + "All caught up!" in UI
3. Bengali review: E7 detects language, replies in same language

## Learned
- GBP API requires Meta App Review approval (4-8 weeks)
- Bengali: must explicitly prompt E7 to reply in Bengali
- Rate limit: 200 requests/day per GBP token
