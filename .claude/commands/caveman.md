# /caveman — Token Efficiency Mode
> Source: JuliusBrussee/caveman (69K stars)

/caveman on   → cave-speak mode: terse comments, short names
/caveman off  → normal verbosity

## Cave-Speak Rules
- Comments: max 5 words
- Variables: short (res, ctx, cfg — not response, context, config)
- No docstrings unless non-obvious
- No blank lines between related lines

## Before/After
```python
# BEFORE: "This function handles the content generation process"
async def generate_content_for_client(brief: str) -> str: ...

# AFTER: "gen content"
async def gen_content(brief: str) -> str: ...
```

## When to Activate
Context > 75% full. Long multi-file sessions. User requests brevity.
