# Modules Registry
> All existing modules + their API contracts.
> Agent reads before building to avoid duplicates.

## AgencyOS modules (go/internal/modules/)
content/    POST /api/v1/content/generate → HITLQueue
seo/        POST /api/v1/seo/keyword-cluster → HITLQueue
social/     POST /api/v1/social/hashtags + GET /api/v1/social/schedule
gbp/        POST /api/v1/gbp/review-reply → HITLQueue
analytics/  GET /api/v1/analytics/campaign-insight
crm/        GET /api/v1/clients/{id}/health-score
inbox/      GET /api/v1/inbox/unread + POST /api/v1/inbox/{id}/reply
email/      GET /api/v1/email/threads + POST /api/v1/email/{id}/reply
billing/    GET /api/v1/billing/credits + POST /api/v1/billing/usage
team/       GET /api/v1/team/members + POST /api/v1/team/tasks
hitl/       GET /api/v1/hitl/queue + POST /api/v1/hitl/{id}/approve
employees/  POST /api/v1/employees + GET /api/v1/employees/{id}/activity
workflows/  POST /api/v1/workflows + PATCH /api/v1/workflows/{id}/activate

## A2A endpoints (agencyos-ai)
/a2a/e1    Content Expert
/a2a/e2    SEO Expert
/a2a/e7    GBP Expert
/a2a/e9    Analytics Expert
