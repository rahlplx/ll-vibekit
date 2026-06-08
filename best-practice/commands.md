# Claude Code Commands Best Practice
> Source: shanraisshan/claude-code-best-practice

## Custom Commands in ll-vibekit
Located in `.claude/commands/`:

| Command | When to Use |
|---------|-------------|
| /route | Start of any session — auto-classifies task |
| /generate-prp | After filling INITIAL.md |
| /execute-prp | After reviewing PRP |

## Claude Code Settings
For hooks to work, add to `~/.claude/settings.json`:
```json
{
  "hooks": {
    "SessionStart": [
      {"command": "bash /path/to/ll-vibekit/hooks/session-start.sh"}
    ]
  }
}
```

## Memory Commands
```
/memory recall    → load WORKING-CONTEXT.md + DISCOVERIES.md
/memory save      → update WORKING-CONTEXT.md with session summary
/memory discover  → add new finding to DISCOVERIES.md
```

## Efficiency Tips
1. Use /route before starting — saves ~2-3 back-and-forth messages
2. Load DECISIONS.md only when making architecture decisions
3. Apply caveman compression when context is 75%+ full
4. Update WORKING-CONTEXT.md at end of every session
