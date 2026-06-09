# Memory Best Practice
> Source: shanraisshan/claude-code-best-practice claude-memory.md

## Four Memory Types

1. **Session Memory** (WORKING-CONTEXT.md)
   Updated end of every session. Lives forever.
   Read: start of every session.

2. **Accumulated Knowledge** (DISCOVERIES.md)
   Grows over time. Never shrinks.
   Read: when debugging recurring issues.

3. **Structured Knowledge** (MEMORY/)
   Precise technical facts organized by type.
   Read: load only the file relevant to current task.

4. **Semantic Memory** (Mem0 V3)
   Per-tenant agency preferences. Auto-extracted from HITL edits.
   Read: automatically before every expert LLM call.

## Anti-Patterns
- Loading ALL memory files every session (wastes tokens)
- Not updating WORKING-CONTEXT.md (lost context next session)
- Storing one-off facts in structured MEMORY/ (use DISCOVERIES.md)

## End-of-Session Ritual
1. Update WORKING-CONTEXT.md with what was done
2. Add to DISCOVERIES.md if anything new learned
3. git commit with descriptive message
