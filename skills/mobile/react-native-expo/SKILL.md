# React Native + Expo App
> LL-specific mobile skill

## When to Use
When building or extending the LL mobile app for Android/iOS.

## Setup
```bash
npx create-expo-app@latest my-app --template
cd my-app
npx expo install expo-router react-native-safe-area-context
```

## File Structure (Expo Router)
```
app/
├── (auth)/
│   ├── login.tsx        ← login screen
│   └── register.tsx     ← registration
├── (app)/
│   ├── _layout.tsx      ← tab navigation
│   ├── index.tsx        ← home/dashboard
│   ├── hitl/
│   │   └── index.tsx    ← HITL queue (primary mobile use case)
│   └── employees/
│       └── index.tsx    ← AI employees
└── _layout.tsx          ← root layout
```

## HITL Mobile Pattern (most important screen)
```typescript
// Swipe right = approve, swipe left = reject
import { PanGestureHandler } from 'react-native-gesture-handler';
// See android/SETUP.md for gesture handler installation
```

## Auth on Mobile
1. Try passkeys (expo-passkeys) — newer Android/iOS
2. Fallback to email/password — for older devices
3. Store JWT in expo-secure-store (encrypted)

## Rules
- Minimum touch target: 44×44pt (Apple HIG)
- Test on Android 11 (low-end, 4GB RAM) before shipping
- Use expo-push-notifications for HITL alerts
- Deep links: handle /hitl/{id} to open specific approval

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
