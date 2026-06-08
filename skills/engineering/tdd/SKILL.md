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
