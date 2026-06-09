# Android Kotlin + Jetpack Compose
> Native Android when React Native is insufficient

## WHEN TO USE
Android-specific features: background services, exact alarms,
NFC, complex Bluetooth, device admin features.

## STACK
- Language: Kotlin
- UI: Jetpack Compose
- Architecture: MVVM + UiState
- DI: Hilt
- Network: Retrofit + OkHttp
- Local DB: Room
- Auth: CredentialManager (passkeys), BiometricPrompt

## STRUCTURE
```
app/src/main/
  java/com/{org}/{app}/
    ui/           Composables + ViewModels
    data/         Repository + DAO
    domain/       Use cases
    di/           Hilt modules
  res/            Layout, strings, icons
```

## PLAY STORE CHECKLIST
- [ ] Target SDK: latest stable
- [ ] Permissions: request only what's needed
- [ ] Dark theme support
- [ ] Edge-to-edge display
- [ ] Screenshots for phone + tablet

## SOURCE
profullstack/vibe-stack (Android Kotlin starter code)

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "vibe-stack + ll-vibekit"
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
    source: "vibe-stack + ll-vibekit"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
