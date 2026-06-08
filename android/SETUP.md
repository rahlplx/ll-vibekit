# Android Setup — React Native + Expo

## Prerequisites
- Node.js 20+
- Expo CLI: `npm install -g @expo/cli`
- Android Studio (for emulator)
- JDK 17+

## Project Setup
```bash
npx create-expo-app@latest ll-mobile --template
cd ll-mobile
npx expo install expo-router expo-secure-store expo-auth-session
npx expo install react-native-gesture-handler react-native-reanimated
npx expo install expo-notifications expo-linking
```

## Run on Android
```bash
npx expo run:android
# Or: npx expo start → press 'a' for Android
```

## Building for Play Store
```bash
eas build --platform android --profile production
# Requires: eas.json configured, EAS account
```

## Key Files
```
app.json         — Expo config (bundleIdentifier, version, etc.)
eas.json         — EAS Build config
app/             — Expo Router screens
components/      — Shared components
```

## Android-Specific Notes
- Target API 35+ (required by Google Play 2025+)
- Permissions: check AndroidManifest.xml carefully
- Gestures: react-native-gesture-handler required for HITL swipe

## Play Store Requirements (HUMAN-TODO)
See HUMAN-TODO.md — Google Play Console account required (one-time $25).
