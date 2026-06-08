# PRP: [Feature Name]
> Generated from: [source file]
> Date: [date]

---

## Goal
[One sentence — what will work after this is done?]

## Success Criteria (Verifiable — Karpathy Rule 4)
All must be explicitly checked before calling complete.
- [ ] [Specific: "GET /api/v1/X returns Y with status 200"]
- [ ] [Specific: "Migration runs: goose up exits 0"]
- [ ] [Specific: "Svelte route /app/X renders without errors"]
- [ ] [Specific: "Mobile screen shows X on both iOS and Android"]

## Files in Scope (Karpathy Rule 3)
Modify ONLY these files:
- [ ] `path/to/file1` — reason
- [ ] `path/to/file2` — reason

## Files NOT in Scope
Leave exactly as found:
- `path/to/excluded` — not touching
- `path/to/excluded` — not touching

## DECISIONS.md Compliance
- [ ] DB port: 6432 (PgBouncer), not 5432
- [ ] Embedding: bge-m3 if AI involved
- [ ] RLS on any new DB table
- [ ] Soft delete: is_deleted only
- [ ] Valkey for real-time, not PG LISTEN/NOTIFY

## Implementation Order
1. [first step — usually migration if DB involved]
2. [second step]
3. [etc.]

## Edge Cases
1. [What if X is null/empty?]
2. [What if concurrent requests conflict?]
3. [What if the external service is down?]
