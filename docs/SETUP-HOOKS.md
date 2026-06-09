# How to Enable Hooks in Claude Code

Hooks are the automation layer of ll-vibekit.
Without registering them, session-start.sh and other hooks never fire.

## Step 1: Create or edit ~/.claude/settings.json

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "bash /path/to/ll-vibekit/hooks/session-start.sh"
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash /path/to/ll-vibekit/hooks/sdd-cache-pre.sh "$CLAUDE_TOOL_INPUT""
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash /path/to/ll-vibekit/hooks/sdd-cache-post.sh "$CLAUDE_TOOL_INPUT""
          }
        ]
      }
    ]
  }
}
```

Replace `/path/to/ll-vibekit` with the actual path where you cloned ll-vibekit.

## Step 2: Verify hooks work

Open Claude Code in your project. You should see:
```
=== ll-vibekit session start ===
--- PROJECT.md ---
...your project context...
=== Context loaded. Run /route to begin. ===
```

If you don't see this: check that the path in settings.json is correct.

## Step 3: Project-level hooks (optional)

The install.sh script copies hooks to ll-vibekit-hooks/ in your project.
You can reference these for project-specific validation:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [{"type": "command", "command": "bash ll-vibekit-hooks/sdd-cache-pre.sh"}]
      }
    ]
  }
}
```

## Opencode (alternative to Claude Code)

Opencode uses `opencode.json` instead of settings.json.
ll-vibekit includes opencode.json in the repo root for AgencyOS repos.

## Which hooks do what

| Hook | When | What |
|------|------|------|
| session-start.sh | Every session open | Loads PROJECT.md + CLAUDE.md + WORKING-CONTEXT.md |
| sdd-cache-pre.sh | Before file write | Warns on migrations, AI files — reminds of conventions |
| sdd-cache-post.sh | After file write | Logs modified files to WORKING-CONTEXT.md |
| simplify-ignore.sh | On large files | Warns if output > 300 lines (over-engineering check) |
