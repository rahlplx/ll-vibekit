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
