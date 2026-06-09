# /track — Emit Telemetry Span

## What It Does
Records a span in the current session's OTel trace.
Called automatically by hooks, or manually during a session.

## Usage
```
/track agent architect
/track skill skills/saas/migration
/track prp-generated feature-name
/track pdca-iteration
/track feature-shipped
/track error go-build-failed 'cd go && go build failed with...'
/track pattern 'Always run goose up before sqlc generate'
```

## Under the Hood
Reads current session ID from .telemetry/.current-session
Calls: python3 scripts/otel-harness.py span {session_id} {type} {data}

## Auto-tracked
When hooks are enabled, these are tracked automatically:
- Session start/end
- File writes (sdd-cache-post.sh)
- Large outputs (simplify-ignore.sh triggers)
Manual /track for: agent use, skill use, pattern discoveries
