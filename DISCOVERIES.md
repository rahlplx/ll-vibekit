# DISCOVERIES.md — Accumulated Knowledge
> Auto-updated by agent at end of every session.
> Never delete entries — this is the permanent memory.
> Source: ECC + vibecode-pro-max-kit pattern

---

## Format
Each entry: date, what was discovered, why it matters.

---

## June 2026

**2026-06-09 — ll-vibekit initialized**
Merged 14 repos into unified harness. Key insight: every top repo uses the same
core file naming (CLAUDE.md, AGENTS.md, SKILL.md inside named folders). The
ECC repo (209K stars) has the most comprehensive agent library. gstack has the
best skill template format. addy-skills has the best hooks system.

**2026-06-09 — gitingest token efficiency**
Running gitingest with `max_file_size=30_000` and excluding `*.lock`, `node_modules`,
`dist/`, `*.min.*` reduces digest size by ~60-80%. ECC's 3074 files compress to
~185KB usable digest. For large repos, limit to tree + key files only.

**2026-06-09 — Vibe-stack Android structure**
profullstack/vibe-stack has a real Android app in `android/` (Kotlin MainActivity,
Gradle build). For LL mobile apps: Expo + React Native is the right approach
(single codebase), but the vibe-stack Android folder pattern is useful for
native features that need to bridge to the JS layer.

**2026-06-09 — bkit PDCA quality cycle**
The bkit repo's PDCA agents (Plan → Do → Check → Act) are the best quality
gate pattern found in any vibe coding harness. The `pdca-check.md` agent
explicitly verifies output against the original spec — this is what prevents
the "agent divergence" problem where implementation drifts from intent.

---

## Add New Entries Below

