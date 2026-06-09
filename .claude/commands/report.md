# /report — Generate Intelligence Report

## When to Run
Weekly. Or after 5+ sessions to see patterns.

## Usage
```
/report
```
This runs: python3 scripts/intelligence-report.py

## What You Get
- intelligence/report-{date}.md (weekly report)
- Updated stats in intelligence/INTELLIGENCE.md
- Ship rate, avg PDCA iterations, top errors
- Auto-generated harness improvement suggestions

## Example Output
```
Sessions: 12  |  Ship rate: 83%  |  Avg PDCA: 1.8
Top error: go build failed (3x) — add to MEMORY/mistakes.md
Suggestion: migration skill used 8x — consider adding migration checklist
```
