# MEMORY/patterns.md — Code Patterns Agents Must Follow
> Add entries when a new correct pattern is confirmed in production.
> Never remove — prevents recurring mistakes.

---

## Go Fiber: Handler structure
```go
func (h *Handler) CreateX(c *fiber.Ctx) error {
    var req CreateXRequest
    if err := c.BodyParser(&req); err != nil { return fiber.ErrBadRequest }
    if err := validate.Struct(&req); err != nil { return fiber.NewError(400, err.Error()) }
    if !h.rbac.Can(c.Context(), userID, tenantID, "module:create") { return fiber.ErrForbidden }
    result, err := h.service.CreateX(c.Context(), req)
    if err != nil { return err }
    return c.JSON(result)
}
```

## Go: Tenant context
```go
tenantID := tenancy.FromCtx(c.Context())
// Sets SET LOCAL app.tenant_id = '...' for RLS — never pass as parameter
```

## sqlc: Query naming
```sql
-- name: CreateX :one        → returns row
-- name: ListX :many         → returns slice
-- name: UpdateX :exec        → no return
-- Always RETURNING * on INSERT to get generated id/created_at
```

## SvelteKit: Server load (CORRECT)
```typescript
// +page.server.ts — ALWAYS load here, NEVER in onMount
export const load: PageServerLoad = async ({ locals }) => {
    return { data: await api.getX(locals.tenantId) }
}
```

## SvelteKit: SSE (ONE connection in root layout)
```typescript
const es = new EventSource('/api/stream')
es.onmessage = ({ data }) => { const msg = JSON.parse(data); ... }
// NEVER create multiple EventSource connections
```

## Python: 5-step expert pattern
```python
async def execute(self, task: AgentTask) -> ExpertResult:
    byok = await get_byok_key(task.tenant_id, "openai")
    system = self.load_prompt(f"e{n}_{name}")
    memory = await get_client_memory(task.tenant_id, task.payload.get("brief",""))
    context = await retrieve(task.client_id, task.payload.get("brief",""))
    full_system = system
    if memory: full_system += f"\nAGENCY PREFERENCES:\n{memory}"
    if context: full_system += f"\nCLIENT KNOWLEDGE:\n{context}"
    result = await self._agent.run(user_prompt, deps=TenantDeps(...))
    return ExpertResult(expert_id=self.expert_id, output=result.data.output,
                        confidence=result.data.confidence)
```

## Python: Temporal activity
```python
@activity.defn
async def my_activity(inp: MyInput) -> MyOutput:
    # Must be idempotent (may retry), async, no global state
    pass
result = await workflow.execute_activity(
    my_activity, inp,
    start_to_close_timeout=timedelta(minutes=5),
    retry_policy=RetryPolicy(maximum_attempts=3),
)
```

## PostgreSQL: RLS on every tenant table
```sql
ALTER TABLE t ENABLE ROW LEVEL SECURITY;
CREATE POLICY t_tenant ON t
    USING (tenant_id = current_setting('app.tenant_id')::uuid);
CREATE INDEX idx_t_tenant ON t(tenant_id) WHERE NOT is_deleted;
```

## React Native: HITL swipe
```typescript
// Swipe right (translateX > 100) = approve
// Swipe left (translateX < -100) = reject
// Use react-native-gesture-handler PanGestureHandler
```

## Token loading order (cheapest to most expensive)
1. CLAUDE.md + RULES.md (~1K) — always
2. DECISIONS.md (~3K) — architecture decisions only
3. MEMORY/stack.md (~1K) — new features only
4. One module file (~3K) — what task touches
5. One agent file (~1K) — relevant specialist
