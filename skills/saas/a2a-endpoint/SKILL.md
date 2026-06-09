# Add A2A Endpoint
> Expose an expert via Agent-to-Agent Protocol v1.0

## When to Use
When an expert needs to be callable from external agents,
partner integrations, or cross-expert delegation.

## Steps

1. Add to EXPERT_SKILLS in src/a2a/server.py
```python
EXPERT_SKILLS["e{N}"] = [
    {"id": "{skill_id}", "name": "{Skill Name}", "description": "...", "tags": [...]},
]
```

2. Add Agent Card to a2a_agents table
```sql
INSERT INTO a2a_agents (expert_id, agent_name, endpoint_path, skills)
VALUES ('E{N}', '{Name} Expert', '/a2a/e{N}', '[...]'::jsonb);
```

3. Test
```bash
curl -X POST http://localhost:8001/a2a/e{N} \
  -H "Content-Type: application/json" \
  -H "X-AgencyOS-Tenant: {tenant_id}" \
  -d '{"jsonrpc":"2.0","method":"message/send","params":{"message":{"role":"user","parts":[{"type":"text","text":"test"}]},"skill":"{skill_id}"}}'
```

## Success
- [ ] GET /a2a/e{N}/agent-card returns valid JSON
- [ ] POST /a2a/e{N} returns artifact
- [ ] POST with message/stream returns SSE

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
