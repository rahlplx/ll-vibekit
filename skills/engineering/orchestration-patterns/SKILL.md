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
