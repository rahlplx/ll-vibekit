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
