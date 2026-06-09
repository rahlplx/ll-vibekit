# Caveman — Token Reduction
> Source: juliusbrussee/caveman (69K★)
> Reduces tokens by 65% in agent communication

## WHEN TO USE
Always. This is the default communication style for agents.

## THE CAVEMAN RULE
Short words. Simple sentences. No filler.

❌ "In order to facilitate the implementation of the requested functionality..."
✅ "To build this..."

❌ "It is important to note that the following considerations should be taken into account..."
✅ "Note:"

❌ "Please be advised that at this juncture, the system will proceed to..."
✅ "Now:"

## APPLY TO
- Agent responses
- CLAUDE.md rules (write them in caveman style)
- PRP descriptions
- Comments in code

## DON'T APPLY TO
- User-facing content (caption copy, email body, etc.)
- Documentation for human readers
- API response messages

## STATS
Average reduction: 65% fewer tokens
Measured on: real Claude Code sessions (juliusbrussee benchmarks)

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "JuliusBrussee/caveman"
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
    source: "JuliusBrussee/caveman"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
