# API Design
> Source: addy-skills api-and-interface-design

## When to Use
Before writing any handler code for a new endpoint.

## URL Design
```
Noun-based:  /api/v1/posts (not /createPost)
Plural:      /api/v1/posts (not /post)
Nested:      /api/v1/clients/{id}/posts
Actions:     /api/v1/posts/{id}/publish (verbs only when needed)
```

## HTTP Methods
```
GET    /resource       → list (paginated)
GET    /resource/{id}  → single
POST   /resource       → create
PATCH  /resource/{id}  → partial update
DELETE /resource/{id}  → soft delete (is_deleted=true)
```

## Response Format
```json
{"items": [...], "total": 42, "page": 1, "per_page": 20}   // list
{"id": "...", "tenant_id": "...", "...": "..."}              // single
{"error": "message", "code": "MACHINE_CODE"}                 // error
```

## AgencyOS Rules
- All endpoints: JWT auth required (except /auth/*)
- All lists: paginated, default 20, max 100
- All tenant resources: tenancy middleware sets RLS before handler
- Error codes: defined in internal/errors/codes.go

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
