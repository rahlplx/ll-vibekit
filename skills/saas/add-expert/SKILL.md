# Add AI Expert (E{N})
> LL-specific — adds new expert to agencyos-ai

## Decision First
Simple (no HITL routing)? → Agno in simple_experts.py
Needs HITL + E15 routing? → PydanticAI + new file

## Steps (PydanticAI route)

1. Create output model + expert class
```python
# src/experts/e{N}_{name}.py
class {Name}Output(BaseModel):
    content: str = Field(min_length=10, max_length=5000)
    confidence: confloat(ge=0.0, le=1.0)
```

2. Create system prompt
```markdown
# src/prompts/e{N}_{name}.md
You are {role}. Task: {description}.
Output JSON: {"content": "...", "confidence": 0.X}
```

3. Wire into E15 ROUTING_TABLE
```python
ROUTING_TABLE[("{module}", "{action}")] = "E{N}"
```

4. Register in EXPERT_REGISTRY
```python
EXPERT_REGISTRY["E{N}"] = E{N}{Name}Expert
```

5. Add to A2A registry (a2a_agents table)

## Success
- [ ] Expert returns output with 0.0 <= confidence <= 1.0
- [ ] ROUTING_TABLE routes to E{N}
- [ ] HITL queue shows output under correct module label
- [ ] /a2a/e{N} responds to A2A message/send

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
