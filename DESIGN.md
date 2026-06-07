# DESIGN.md — ll-vibekit
> Design principles for all Lab Launchpad products.
> Adapted from: garrytan/gstack (107K★), nexu-io/open-design (60K★)

## Visual language

Dark mode first. Light mode is an afterthought.
Color: one accent (cyan-500). Everything else is neutral.
Type: system font for body, monospace for code. No custom fonts in V1.
Spacing: 4px grid (4, 8, 12, 16, 24, 32, 48, 64).
Border radius: 6px components, 10px cards.

## Component hierarchy

```
Design token (var(--accent), var(--bg-surface))
    └── Primitive (shadcn-svelte button, input)
        └── Compound (AOHITLEntry, AOExpertBadge)
            └── Page section
                └── Route
```

Never hardcode hex colors. Always use CSS custom properties.
Never import from a CDN at runtime. Always install and bundle.

## Mobile design rules (critical)

Touch targets: minimum 48px height on all interactive elements.
Thumb zone: primary actions in bottom 40% of screen.
No horizontal scroll on mobile.
Swipe gestures: right = approve, left = reject (HITL pattern).
Font minimum: 16px body on mobile to prevent iOS auto-zoom.

## Accessibility

All interactive elements: keyboard focusable.
All images: alt text.
Color contrast: 4.5:1 minimum (WCAG AA).
