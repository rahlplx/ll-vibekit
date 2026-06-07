# SaaS Auth Flow
> Standard auth implementation for Lab Launchpad SaaS products

## WHEN TO USE
Building auth for any LL SaaS product.

## PATTERN
1. Passkeys (WebAuthn) — PRIMARY
2. Email + password — MANDATORY FALLBACK (50-60% BD Android lacks passkey support)
3. TOTP — mandatory for owner + admin roles on email/password path

## IMPLEMENTATION
```
Registration: passkey preferred → email+password as backup
Login: try passkey → "Use email instead" link always visible
MFA: TOTP on email+password path for privileged roles
JWT: 15min access + 7d refresh, httpOnly cookie
Session: stored in DB, deleted on logout/expiry
```

## NEVER
- Passkey-only (locks out BD Android users)
- Store plain passwords (bcrypt minimum)
- JWT in localStorage (XSS risk)
