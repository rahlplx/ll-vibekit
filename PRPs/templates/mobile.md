# PRP Template — Mobile Feature
> Use for: iOS or Android features

---
# PRP: {Feature Name}
> Platform: iOS | Android | Both

## Goal
{One sentence}

## Success Criteria
- [ ] {Screen renders correctly on iPhone 15}
- [ ] {Screen renders correctly on Samsung Galaxy A54 (BD market device)}
- [ ] {Action works: tap X → Y happens}

## What NOT to change
{other screens/components}

## Platform constraints
iOS: minimum iOS 17, HIG guidelines
Android: minimum Android 12, Material You

## Implementation
```
components/{Component}.tsx
app/(tabs)/{screen}.tsx
lib/{service}.ts
```

## Test
- [ ] Tested on physical iOS device
- [ ] Tested on physical Android device (budget tier)
- [ ] Tested in dark mode
- [ ] Touch targets ≥ 48px

## HUMAN-TODO after completion
- [ ] Add to TestFlight / Internal testing track
