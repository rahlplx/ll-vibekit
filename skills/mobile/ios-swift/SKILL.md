# iOS Swift + SwiftUI
> Native iOS when React Native is insufficient

## WHEN TO USE
iOS-specific features: ARKit, HealthKit, Apple Pay, complex animations,
background processing, widgets.

## STACK
- Language: Swift 6
- UI: SwiftUI
- Data: SwiftData or Core Data
- Networking: URLSession + async/await
- Auth: AuthenticationServices (passkeys), LocalAuthentication

## STRUCTURE
```
Sources/
  App/                 @main entry
  Features/           Feature modules
  Core/               Shared utilities
  Services/           API, auth, storage
Tests/
```

## APP STORE CHECKLIST
- [ ] Privacy manifest (PrivacyInfo.xcprivacy)
- [ ] Required capabilities declared
- [ ] Screenshots for all device sizes
- [ ] App Review guidelines read
- [ ] Human Interface Guidelines followed

## SOURCE
profullstack/vibe-stack (iOS Swift starter code)
