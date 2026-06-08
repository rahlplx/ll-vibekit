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
