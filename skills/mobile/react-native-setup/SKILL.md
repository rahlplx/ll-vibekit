# React Native + Expo Setup
> Cross-platform mobile (iOS + Android) from one codebase

## WHEN TO USE
Any Lab Launchpad mobile app.

## STACK
- Framework: React Native + Expo SDK
- Navigation: Expo Router (file-based, same as Next.js)
- UI: NativeWind (Tailwind for RN) + Expo UI
- State: Zustand
- API: tRPC or REST (same as web)
- Auth: expo-auth-session for passkeys, expo-local-authentication for biometrics
- Push: Expo Notifications
- OTA updates: Expo Updates

## INIT
```bash
npx create-expo-app@latest {name} --template tabs
cd {name}
npx expo install expo-router nativewind zustand
```

## STRUCTURE
```
app/                    Expo Router pages
  (tabs)/              Tab navigation
  (auth)/              Auth screens
components/            Reusable components
lib/                   Utilities, API client
assets/                Images, fonts
```

## RULES
- Test on real device early. Simulator lies about performance.
- iOS: TestFlight for internal testing before App Store submission.
- Android: Internal testing track on Play Console first.

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
