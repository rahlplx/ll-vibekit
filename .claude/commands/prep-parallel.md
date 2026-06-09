# /prep-parallel
> Source: coleam00/context-engineering-intro

Split a PRP into parallel tracks for simultaneous execution.

## When to Use
Feature has independent layers with no mutual dependency.
Example: Go module and Svelte route can build simultaneously.

## Output
```
SEQUENTIAL (must happen first):
  1. Migration
  2. sqlc generate

PARALLEL TRACKS:
  Track B: [backend] Go module files
  Track C: [frontend] Svelte route files
  Track D: [ai-layer] Python expert files

FINAL:
  - Register routes
  - Wire ROUTING_TABLE
  - Run PDCA Check
```

## Next: /execute-parallel
