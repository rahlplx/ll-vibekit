# /eval — Score Current Session

## When to Run
At the end of every session before closing Claude Code.
Or after a feature ships to capture the outcome.

## What It Does
1. Reads .telemetry/sessions/ for current session data
2. Scores the session 0-100 based on:
   - Was a PRP generated? (+20)
   - Did the feature ship? (+30)
   - How many PDCA iterations? (+30 for 1, +10 for 2-4)
   - Were errors resolved cleanly? (+20)
3. Updates MEMORY/ files with new patterns and mistakes
4. Updates intelligence/INTELLIGENCE.md

## Usage
```
/eval
```
This runs: python3 scripts/eval-session.py

## Output
```
Score: 85/100
  - PRP generated: +20
  - Feature shipped: +30
  - PDCA passed in 2 iterations: +20
  - 1 error resolved cleanly: +15
Updated MEMORY/patterns.md (+1 pattern)
Updated intelligence/INTELLIGENCE.md
```
