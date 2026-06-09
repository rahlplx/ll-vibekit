# /harness-health — Full Harness Health Check

## When to Run
Weekly. Before starting a major sprint. After installing into a new project.

## Usage
```
/harness-health
```
This runs: python3 scripts/harness-health.py

## What Gets Checked
- Skills: all have When-to-Use, metadata, eval criteria (score /100)
- Agents: all have Role, performance tracking, self-eval checklist (/100)
- Memory: all MEMORY/ files exist and are filled (not stubs) (/100)
- Project Config: PROJECT.md filled + .vibekit.json configured (/100)
- Commands: all required slash commands exist (/100)
- Telemetry: ship rate + PDCA trends (/100)

## Auto-fix
```
python3 scripts/harness-health.py --fix
```
Runs eval-skills + eval-agents + intelligence-report automatically.

## Scoring
90-100: Excellent  |  75-89: Good  |  60-74: Needs Work  |  <60: Critical
