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
