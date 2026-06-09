# CRITIQUE.md — What Would Break Using This for AgencyOS

> Simulated walkthrough: Hrittik opens Claude Code, tries to build AgencyOS.
> Every failure mode found. All fixed in this commit.

---

## FAILURE 1 — session-start.sh loads the WRONG files  [CRITICAL]

**What happens:**
Hrittik registers the hook. Claude Code fires session-start.sh.
It runs `cat CLAUDE.md` and `cat WORKING-CONTEXT.md`.
But it loads the ll-vibekit template files, not the AgencyOS project files.
The agent reads empty WORKING-CONTEXT.md with no project context.

**Root cause:**
session-start.sh uses relative paths with no working directory.
It has no idea where the project is.
PROJECT.md (the most important file) is never loaded.

**Fix:** session-start.sh reads `.vibekit.json` for the project root,
loads PROJECT.md from there. See hooks/session-start.sh.

---

## FAILURE 2 — /route is cut off  [CRITICAL]

**What happens:**
Hrittik types `/route "build GBP review reply feature"`.
The route command ends mid-sentence: "4. Contains"
No mobile case. No deploy case. No unknown fallback.
Agent stalls.

**Root cause:** The route.md file was truncated during push.

**Fix:** Complete route.md with all 8 cases including mobile, deploy,
AgencyOS module names (gbp, hitl, inbox, crm), and unknown fallback.

---

## FAILURE 3 — /generate-prp reads wrong DECISIONS.md  [CRITICAL]

**What happens:**
Hrittik runs `/generate-prp INITIAL.md` in agencyos-web.
generate-prp.md says "Load DECISIONS.md".
Claude looks for DECISIONS.md in current directory.
agencyos-web has no DECISIONS.md. The correct one is in agencyos-api.
Agent generates a PRP with wrong or missing constraints.
Hrittik's PRP suggests using WebSockets (banned), port 5432 (wrong), etc.

**Root cause:** generate-prp.md has no path to DECISIONS.md.
It assumes DECISIONS.md is always in the current directory.

**Fix:** .vibekit.json specifies DECISIONS_PATH.
generate-prp.md reads from that path.

---

## FAILURE 4 — PDCA Check has no test commands  [HIGH]

**What happens:**
pdca-check.md says "go build ./... exits 0".
Hrittik is in agencyos-api. Go code is in agencyos-api/go/.
`go build ./...` fails — no Go files in root.
Correct command: `cd go && go build ./...`

Agent reports "all checks passed" because it ran the wrong command.
Broken code ships.

**Root cause:** PDCA Check agents are generic.
They have no knowledge of the project's directory structure or test commands.

**Fix:** .vibekit.json has TEST_COMMANDS. pdca-check.md reads them.

---

## FAILURE 5 — Multi-repo confusion  [HIGH]

**What happens:**
AgencyOS is 4 repos: agencyos-api, agencyos-web, agencyos-ai, agencyos-marketing.
Hrittik runs /generate-prp in agencyos-api for a feature that also needs:
  - a new Svelte route (agencyos-web)
  - a new Python expert (agencyos-ai)

The PRP says "create src/routes/..." but that path is in a different repo.
Agent creates the file in the wrong repo.

**Root cause:** No multi-repo awareness anywhere in the harness.

**Fix:** .vibekit.json has RELATED_REPOS.
generate-prp.md detects cross-repo files and notes the correct repos.

---

## FAILURE 6 — Hooks never activate  [HIGH]

**What happens:**
Hrittik reads hooks/hooks.json. Tries to figure out how to enable it.
No instructions anywhere. No .claude/settings.json.
Hooks never fire. session-start.sh never runs.
All the automation is dead.

**Root cause:** Claude Code requires hooks to be registered in
~/.claude/settings.json. The harness provides hooks.json but no
instructions on how to wire it into Claude Code.

**Fix:** docs/SETUP-HOOKS.md + .claude/settings.json template.

---

## FAILURE 7 — INITIAL.md is AgencyOS-specific  [MEDIUM]

**What happens:**
Someone uses ll-vibekit on a different project (Django app, React Native).
They open INITIAL.md and see:
  "- [ ] AgencyOS (SaaS dashboard)"
  "- [ ] Kalki AI (RAG platform)"
Confusing. They don't know what to put.

**Root cause:** INITIAL.md is hardcoded with Lab Launchpad product names.

**Fix:** Generic INITIAL.md that reads project name from PROJECT.md.

---

## FAILURE 8 — /discover updates wrong MEMORY/ path  [MEDIUM]

**What happens:**
After shipping a feature, Hrittik runs /discover.
discover.md says update `memory/patterns.md` (lowercase).
But the canonical path is `MEMORY/patterns.md` (uppercase).
On Linux (Oracle ARM), these are different directories.
Knowledge is saved to the wrong place and never found again.

**Root cause:** Case inconsistency in discover.md.

**Fix:** Standardize to MEMORY/ (uppercase) everywhere.

---

## FAILURE 9 — No error recovery workflow  [MEDIUM]

**What happens:**
`goose up` fails on migration 003. Hrittik doesn't know:
  - How to see what went wrong
  - How to roll back
  - Whether to retry or fix first

No error recovery skill or guide exists.

**Fix:** skills/engineering/error-recovery/SKILL.md

---

## FAILURE 10 — Mobile stack inconsistency  [LOW]

**What happens:**
agents/mobile.md says "React Native + Expo".
But agencyos-web uses Capacitor (wrapping SvelteKit PWA as mobile app).
Agent gives wrong advice for AgencyOS mobile.

**Root cause:** Mobile strategy changed but harness wasn't updated.

**Fix:** AgencyOS PROJECT.md specifies Capacitor, not RN.
Generic mobile.md stays as RN/Expo (correct for new projects).
AgencyOS-specific mobile notes in examples/agencyos/PROJECT.md.
