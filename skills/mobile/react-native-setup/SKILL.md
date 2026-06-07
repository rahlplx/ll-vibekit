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
