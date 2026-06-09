# NEXT_PLAN.md — What Happens Now

> ll-vibekit v1.0 is complete. Here's what to do with it.
> Priority order: human-critical → dev sprint → harness usage.

---

## TODAY (Rahul — human-only, cannot be delegated to agents)

From HUMAN-TODO.md:

**1. Submit Meta App Review** — this is the CRITICAL PATH blocker
   - URL: https://developers.facebook.com/apps
   - Permissions needed: pages_manage_posts, instagram_content_publish
   - Wait time: 4-8 weeks — every day you delay = 4-8 weeks later you ship social module
   - Do this BEFORE anything else today

**2. Revoke exposed GitHub PAT**
   - URL: https://github.com/settings/tokens
   - Security incident — do immediately

**3. Register SSLCommerz merchant** (7-10 days)
   - URL: https://merchants.sslcommerz.com
   - Blocks: billing module, paid plan signup

---

## THIS WEEK (Hrittik — Sprint 1)

### Day 1-2: Oracle ARM Setup
```bash
# On Oracle ARM server:
bash agencyos-api/scripts/setup-oracle-arm.sh
ollama pull qwen3.6:35b-a3b-q4_k_m   # 18GB download
cd agencyos-api/go && goose up         # run all 3 migrations
```

### Day 3-5: Auth Module
Using: ll-vibekit `skills/saas/auth-flow/SKILL.md`

1. Implement passkey registration/login (go-webauthn)
2. Implement email+password fallback (mandatory)
3. JWT issuance + httpOnly cookie
4. SvelteKit login page + passkey UI

Success: agency can create account and log in.

### Day 6-7: HITL Engine
Using: ll-vibekit `skills/saas/hitl-flow/SKILL.md`

1. LangGraph E15 graph with interrupt()
2. HITLQueue table (migration 001 already has it)
3. SSE stream: Valkey pub/sub → /api/stream
4. SvelteKit HITL queue component with badge counter

Success: placeholder HITL entry appears in queue, approve works.

---

## NEXT WEEK (Hrittik — Sprint 2)

### E1 Content Expert + Content Module

Using ll-vibekit harness:
```
nano agencyos-api/INITIAL.md
# Fill: "Build E1 content expert that generates Bengali captions
#        for BD restaurant clients with HITL approval"

/generate-prp agencyos-api/INITIAL.md
# Review PRP
/execute-prp PRPs/e1-content-expert.md
```

This replaces manually writing all the Go + Python + Svelte files.
The harness generates the PRP, you review it (5 min), it implements.

### Langfuse V2 Observability
Add to docker-compose.prod.yml and wire LiteLLM callbacks.
After this: every E1 call visible in Langfuse dashboard with tokens + confidence.

---

## HOW TO USE ll-vibekit GOING FORWARD

### For every new feature:
```
1. Open agencyos-api/INITIAL.md
2. Describe feature in plain English
3. Claude Code: /generate-prp INITIAL.md
4. Review PRP (2 min)
5. Claude Code: /execute-prp PRPs/feature-name.md
6. PDCA Check runs automatically
7. Claude Code: update WORKING-CONTEXT.md
```

### For every session start:
```
Claude Code reads:
  CLAUDE.md           (Karpathy rules)
  WORKING-CONTEXT.md  (where we left off)
  DECISIONS.md        (locked decisions)
That's all. Don't load everything.
```

### For debugging:
```
/route "fix: {error description}"
Loads: MEMORY/mistakes.md + relevant module
Runs: diagnose skill
```

### For mobile features (when ready):
```
/route "mobile: HITL approval screen for React Native"
Loads: android/SETUP.md + agents/mobile.md
Uses: skills/mobile/react-native-expo/SKILL.md
```

---

## HARNESS SYNC PLAN

ll-vibekit is a separate repo. To keep it in sync with AgencyOS decisions:

**When to update ll-vibekit:**
- New mistake discovered → MEMORY/mistakes.md
- New code pattern confirmed → MEMORY/patterns.md
- New module ships → MEMORY/modules.md
- New feature completed → process/features/completed/

**How to update:**
```bash
cd ll-vibekit
# Edit the relevant MEMORY/ file
git add -A && git commit -m "memory: update after {feature} ships"
git push
```

**Monthly:**
Run `scripts/batch-digest.py` to refresh gitingest digests of source repos.
Check if any source repos have new patterns worth extracting.

---

## 60-DAY MILESTONE TARGETS

| Week | Target | Success Metric |
|------|--------|----------------|
| 1-2 | Auth + HITL working | Agency logs in, approves test content |
| 3-4 | E1 + Content module | Agency generates + approves captions |
| 5-6 | Social scheduling | Post scheduled to Facebook |
| 7-8 | GBP reviews | E7 drafts replies (after Meta App Review) |
| 9-10 | Beta launch | 5 agencies onboarded |
| 11-12 | Billing live | First ৳ paid |

---

## REPO STATUS

| Repo | State | Next Action |
|------|-------|-------------|
| rahlplx/ll-vibekit | ✅ Complete (124 files) | Use for all future dev |
| rahlplx/agencyos-api | ✅ Architecture complete | Hrittik: auth module |
| rahlplx/agencyos-web | ✅ Architecture complete | Hrittik: login page |
| rahlplx/agencyos-ai | ✅ Architecture complete | Hrittik: E1 expert |
| rahlplx/agencyos-marketing | ✅ Basic setup | Later |

---

## IMMEDIATE COMMAND FOR HRITTIK

```bash
# Clone the harness into each repo
git clone https://github.com/rahlplx/ll-vibekit .vibekit

# Start Claude Code in agencyos-api
claude --context .vibekit/CLAUDE.md --context DECISIONS.md

# First task:
/route "build auth module: passkeys + email fallback + JWT"
```
