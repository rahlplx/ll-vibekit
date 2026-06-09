# Orchestration Patterns
> Source: addy-skills references/orchestration-patterns.md

## When to Use
Designing multi-agent workflows or complex automation pipelines.

## Pattern 1: Sequential Chain
```
Architect -> Backend -> Frontend -> QA
```
Use when: strict step dependencies.

## Pattern 2: Parallel Tracks
```
Architect -> [Backend || Frontend || AI] -> QA
```
Use when: independent steps. Commands: /prep-parallel + /execute-parallel

## Pattern 3: PDCA Validation Loop
```
Do -> Check -> (fail: Act -> Do again) -> pass -> ship
```
Use when: quality must be verified. Agents: pdca-do, pdca-check, pdca-act

## Pattern 4: A2A Delegation
```
E15 -> E2 (get keywords) -> E1 (write with keywords)
```
Use when: expert needs another expert's output.

## Anti-Patterns
- Circular delegation (A calls B calls A)
- Too many parallel tracks (>5) — context pollution
- Skipping PDCA Check — agent drift undetected

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "mattpocock/skills + addy-skills"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "avg_pdca_when_used > 2.5 OR ship_rate < 70%"

# Populated by eval-session.py after each use
stats:
  times_used: 0
  features_shipped_after_use: 0
  avg_pdca_iterations_when_used: 0.0
  ship_rate_when_used: "0%"
  last_used: "never"

# Auto-populated by scripts/eval-skills.py
failure_patterns: []

# Manual + auto improvement history
improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
    source: "mattpocock/skills + addy-skills"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
