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
