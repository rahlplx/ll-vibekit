# Add AI Employee
> Creates a rentable AI employee persona

## Steps

1. Create employee via API
```json
POST /api/v1/employees
{
  "name": "Mira",
  "role_label": "Social Media Manager",
  "expert_id": "E1",
  "persona_prompt": "You are Mira, creative and energetic...",
  "focus_module": "social",
  "schedule_cron": "0 9 * * 1,3,5",
  "schedule_tz": "Asia/Dhaka",
  "auto_approve_threshold": 0.95,
  "subscription_amount": 999.00
}
```

2. Temporal ScheduledWorkflow auto-starts
```
workflow_id = "employee-{id}-scheduled"
Fires on schedule_cron, calls AIEmployeeScheduledWorkflow
```

3. Persona injected into expert system prompt
```
{persona_prompt}

{base_expert_system_prompt}

AGENCY PREFERENCES: {mem0_memory}
CLIENT KNOWLEDGE: {rag_context}
```

## Success
- [ ] Employee shows in /app/employees
- [ ] Activity log updates after scheduled run
- [ ] HITL shows tasks under employee name
- [ ] Subscription charge appears in billing

## BD Naming Convention
South Asian names: Mira, Raj, Zara, Arjun, Priya, Karim

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
