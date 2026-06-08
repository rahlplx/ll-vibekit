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
