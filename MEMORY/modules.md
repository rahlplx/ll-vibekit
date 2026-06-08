# MEMORY/modules.md — All Existing Modules + API Contracts
> Updated when new modules are added.

## AgencyOS Modules

| Module | Go package | Svelte route | AI Expert | Status |
|--------|-----------|-------------|-----------|--------|
| auth | modules/auth | (auth)/ | None | ✓ Active |
| content | modules/content | (app)/content | E1 | ✓ Active |
| social | modules/social | (app)/social | E3/E8 | ✓ Active |
| seo | modules/seo | (app)/seo | E2 | ✓ Active |
| inbox | modules/inbox | (app)/inbox | E6 | ✓ Active |
| gbp | modules/gbp | (app)/gbp | E7 | ✓ Active |
| crm | modules/crm | (app)/crm | E5 | ✓ Active |
| reports | modules/reports | (app)/reports | E9 | ✓ Active |
| billing | modules/billing | (app)/billing | E10 | ✓ Active |
| hitl | modules/hitl | (app)/content (shared) | E14 | ✓ Core |
| vault | modules/vault | (app)/settings | None | ✓ Active |
| employees | modules/employees | (app)/employees | All | In Progress |
| workflows | modules/workflows | (app)/workflows | All | In Progress |
| a2a | (FastAPI only) | None | All | In Progress |

## Key API Patterns
- All routes: /api/v1/{module}
- Auth: JWT in httpOnly cookie
- Tenant isolation: X-Tenant-ID header from Hono → Go middleware sets RLS
- HITL webhook: PATCH /api/v1/hitl/{id}/review
