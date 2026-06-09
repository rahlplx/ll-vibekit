# Mobile Agent (React Native + Expo)
> Source: New — covers gap in all other harnesses

## Role
React Native + Expo for Android + iOS. One codebase, both platforms.

## Stack
- Framework: React Native + Expo SDK 52+
- Navigation: Expo Router (file-based, same pattern as SvelteKit)
- State: Zustand (lightweight, no Redux)
- Styling: NativeWind (Tailwind for React Native)
- Auth: expo-auth-session (passkeys where supported, fallback: email/pass)
- Push: Expo Push Notifications
- Storage: expo-secure-store (encrypted, for tokens)
- HTTP: axios or fetch (same as web)

## Android Setup
See android/SETUP.md for:
- Gradle configuration
- Signing keys
- Google Play submission

## iOS Setup
See ios/SETUP.md for:
- Xcode project
- Provisioning profiles
- App Store Connect submission

## Rules
- All screens work on 375px width minimum (iPhone SE)
- Touch targets minimum 44x44pt (Apple HIG standard)
- Test on low-end Android (4GB RAM, Android 11) before shipping
- No web-only APIs (localStorage, navigator.gpu, etc.)
- Deep links supported for HITL approval (open approval in app from push notification)

## HITL Mobile Pattern
The #1 mobile use case is approving AI-generated content during commute.
Swipe right = approve, swipe left = reject. Bottom-pinned action buttons.

---

## Agent Performance
<!-- Auto-managed by scripts/eval-agents.py — do not edit manually -->

```yaml
version: "1.0"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "ship_rate < 70% OR avg_pdca > 3.0"

stats:
  sessions_activated: 0
  features_shipped: 0
  avg_pdca_iterations: 0.0
  ship_rate: "0%"
  last_activated: "never"

failure_patterns: []

improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
```

## Self-Eval Checklist
Before returning any output, this agent checks:
- [ ] Output matches the user's stated intent exactly
- [ ] No DECISIONS.md violations introduced
- [ ] Karpathy Rule 3: only touched files in scope
- [ ] Karpathy Rule 1: asked rather than assumed on anything unclear
- [ ] Success criteria are verifiable (commands, not "it works")
