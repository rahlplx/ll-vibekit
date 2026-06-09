# Testing Patterns
> Source: addy-skills references/testing-patterns.md

## Go Tests
```go
func TestHITLQueue(t *testing.T) {
    tests := []struct{
        name    string
        input   CreateHITLInput
        wantErr bool
    }{
        {"valid", CreateHITLInput{...}, false},
        {"no tenant", CreateHITLInput{}, true},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            _, err := hitl.Create(ctx, tt.input)
            if tt.wantErr { require.Error(t, err) } else { require.NoError(t, err) }
        })
    }
}
```

## Python Tests
```python
@pytest.mark.asyncio
async def test_e1_confidence_bounds():
    result = await E1ContentExpert().execute(mock_task)
    assert 0.0 <= result.confidence <= 1.0
    assert len(result.output) > 0

async def test_rag_quality():
    scores = evaluate(bengali_dataset, metrics=[faithfulness, context_precision])
    assert scores["faithfulness"] >= 0.75
```

## Svelte Tests (Playwright)
```typescript
test('HITL entry shows approve/reject', async ({ page }) => {
    await page.goto('/app/content')
    await expect(page.getByTestId('hitl-queue')).toBeVisible()
    await page.getByTestId('approve-btn').first().click()
    await expect(page.getByText('Approved')).toBeVisible()
})
```

## Mobile Tests (Detox)
```typescript
it('swipe right approves', async () => {
    await element(by.id('hitl-card')).swipe('right', 'slow', 0.75)
    await expect(element(by.text('Approved'))).toBeVisible()
})
```
