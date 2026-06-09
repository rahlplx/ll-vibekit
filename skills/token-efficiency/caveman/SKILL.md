# Caveman Token Compression
> Source: JuliusBrussee/caveman (69K★) — 65% token reduction

## When to Use
When token budget is running low (context window ~75% full).
When long-running tasks need to compress output to survive.

## The Caveman Principle
"Why use many token when few token do trick?"

Caveman writes code with short, primitive comments.
No essays. No philosophy. Just the essential.

## Before (normal)
```python
# This function handles the generation of content by calling the AI model
# with the appropriate system prompt and user message, then parsing the
# response and returning an ExpertResult object with the output and confidence
async def execute(self, task: AgentTask) -> ExpertResult:
```

## After (caveman)
```python
# gen content → parse → return result
async def execute(self, task: AgentTask) -> ExpertResult:
```

## Rules for Caveman Mode
1. Comments: one line max, 5 words max
2. Variable names: descriptive but short (res not response, ctx not context)
3. No docstrings unless they carry unique non-obvious information
4. Function bodies: compress blank lines
5. String literals in prompts: remove filler words

## When to Apply
- /caveman activate → applies these rules for the rest of the session
- /caveman off → returns to normal verbosity
- Auto-applies when token budget warning appears

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "JuliusBrussee/caveman + garrytan/gstack"
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
    source: "JuliusBrussee/caveman + garrytan/gstack"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
