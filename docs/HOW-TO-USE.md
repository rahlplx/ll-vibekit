# How To Use ll-vibekit

## For Non-Technical Founders (Rahul)

### Build a new feature in 4 steps

**1. Describe it** — open INITIAL.md, fill in plain English
```
What: Weekly analytics report for agencies every Monday
Which product: AgencyOS
Success: Agency receives email with top 5 posts every Monday 9am
```

**2. Generate plan** — run in Claude Code:
```
/generate-prp INITIAL.md
```

**3. Review PRP** (2 minutes) — Claude shows exactly what will change.
Add/remove anything before approving.

**4. Execute**:
```
/execute-prp PRPs/weekly-analytics-report.md
```

Claude builds it. Every file is validated as it's written.
Success criteria are checked automatically at the end.

---

## For Developers (Hrittik)

### Continue a session
```bash
git pull origin main
cat WORKING-CONTEXT.md     # what was left incomplete
/route "continue {feature}" # auto-routes to right agent
```

### Start a new module
```bash
cp INITIAL.md              # describe feature
/generate-prp INITIAL.md   # generates PRP
/execute-prp PRPs/name.md  # implements
```

### Debug production issue
```bash
/route "fix: E1 returns empty output for Bengali clients"
# Loads: MEMORY/mistakes.md + ai-layer agent
# Runs: diagnose skill
```

---

## Token Budget
Context fills up. When it does:
1. /caveman on — compress output
2. /status — see what's left
3. /context-save name — save state
4. New session: /context-restore name
