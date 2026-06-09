# Test-Driven Development
> Source: mattpocock/skills (119K★)

## When to Use
When implementing any new function, endpoint, or module.
Write the test first. Then write the implementation.

## Steps
1. Write the test that describes the expected behavior
2. Run the test — confirm it FAILS (red)
3. Write the minimal implementation to make it pass
4. Run the test — confirm it PASSES (green)
5. Refactor if needed, keeping tests green

## For Go (agencyos-api)
```go
// Test first
func TestCreateHITLEntry(t *testing.T) {
    entry, err := hitl.Create(ctx, CreateHITLInput{...})
    require.NoError(t, err)
    assert.Equal(t, "pending", entry.Status)
}
// Then implement hitl.Create()
```

## For Python (agencyos-ai)
```python
# pytest
async def test_e1_expert_returns_confidence():
    result = await E1ContentExpert().execute(task)
    assert 0.0 <= result.confidence <= 1.0
    assert len(result.output) > 0
```

## For Svelte (agencyos-web)
```typescript
// Playwright
test('HITL queue shows pending items', async ({ page }) => {
    await page.goto('/app/content')
    await expect(page.getByTestId('hitl-queue')).toBeVisible()
})
```

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "mattpocock/skills + addy-skills"
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
    source: "mattpocock/skills + addy-skills"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
