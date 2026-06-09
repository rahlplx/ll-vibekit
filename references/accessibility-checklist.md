# Accessibility Checklist
> Source: addy-skills references/accessibility-checklist.md

## Web (SvelteKit)
- [ ] All interactive elements have visible focus states
- [ ] Color contrast >= 4.5:1 for normal text
- [ ] Images have alt text
- [ ] Forms have labels (not just placeholder text)
- [ ] Keyboard navigation works for all features
- [ ] ARIA roles on custom interactive components

## Mobile (React Native)
- [ ] All touchable elements have accessibilityLabel
- [ ] Minimum touch target: 44x44pt
- [ ] VoiceOver (iOS) + TalkBack (Android) tested
- [ ] Text scales with system font size

## HITL Screen (most critical for mobile)
- [ ] Approve/Reject buttons: large and clearly labeled
- [ ] Content preview readable at font size +2
- [ ] Swipe gesture also accessible via tap buttons
- [ ] Status indicated by shape/label not just color
