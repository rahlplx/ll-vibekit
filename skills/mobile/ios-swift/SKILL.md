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
