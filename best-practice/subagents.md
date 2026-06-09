# Sub-Agents Best Practice
> Source: shanraisshan/claude-code-best-practice claude-subagents.md

## In-Context Sub-Agents (Claude Code)
```
@agents/architect.md @agents/backend.md
Design the notifications module.
```

## Parallel Sub-Agents (ctx_eng pattern)
```
/prep-parallel PRPs/feature.md   → splits into parallel sub-tasks
/execute-parallel                 → runs concurrently
```

## AgencyOS Expert Sub-Agents (A2A)
```python
# E1 calls E2 for keywords via A2A
result = await a2a_client.send_message(
    expert_id="e2", skill="keyword_cluster",
    message={"brief": brief}
)
```

## Anti-Patterns
- Activating all agents at once (token budget)
- Sub-agents modifying DECISIONS.md (architect only)
- Sub-agents updating HUMAN-TODO.md (human only)
