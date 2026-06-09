# ll-vibekit Intelligence Layer

The more you use this harness, the smarter it gets.
Every session, every failure, every shipped feature feeds back into the system.

---

## How It Works

```
Session runs
    │
    ├─ hooks/session-start.sh   → loads context (OTel: trace start)
    │
    ├─ /route → /generate-prp → /execute-prp → PDCA cycle
    │       │           │              │            │
    │     span        span           span        span (per iteration)
    │
    ├─ hooks/session-end.sh     → captures outcome (OTel: trace end)
    │       ├─ writes .telemetry/sessions/{date}-{id}.json
    │       ├─ updates INTELLIGENCE.md summary
    │       └─ triggers eval pipeline
    │
    └─ scripts/eval-session.py  → scores session, updates MEMORY/
            ├─ PRP quality score (0-100)
            ├─ PDCA iteration count
            ├─ Errors encountered
            ├─ New patterns → MEMORY/patterns.md
            └─ New mistakes → MEMORY/mistakes.md
```

---

## Files

```
intelligence/
├── README.md              This file
├── INTELLIGENCE.md        The harness brain — growing knowledge summary
├── schema/
│   ├── session.json       Schema for session telemetry events
│   └── eval.json          Schema for eval results

.telemetry/                (gitignored — local data only)
├── sessions/              One JSON per session
├── prp-evals/             PRP quality scores over time
└── errors/                Error patterns with frequency

scripts/
├── eval-session.py        Score a session, update MEMORY/
├── eval-prp.py            Score a PRP before/after execution
├── intelligence-report.py Generate weekly learning report
└── otel-harness.py        OpenTelemetry span emitter

hooks/
└── session-end.sh         Capture session outcome → .telemetry/

.claude/commands/
├── eval.md                /eval — score current session
├── eval-prp.md            /eval-prp — score a PRP
└── report.md              /report — generate intelligence report
```

---

## What Gets Tracked

| Event | What's captured | Used for |
|-------|----------------|----------|
| Session start | project, task description | session correlation |
| PRP generated | quality score (0-100) | improve PRP templates |
| PRP executed | iterations, errors | identify hard patterns |
| PDCA Check | pass/fail, which criteria failed | identify weak spots |
| Error occurred | type, file, message | update MEMORY/mistakes.md |
| Feature shipped | time taken, PDCA iterations | efficiency trends |
| Pattern discovered | code pattern text | update MEMORY/patterns.md |

---

## Privacy

All telemetry is LOCAL. No data leaves your machine.
.telemetry/ is gitignored — never committed.
INTELLIGENCE.md and MEMORY/ are committed (they're your knowledge, not raw data).
