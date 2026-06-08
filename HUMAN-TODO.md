# HUMAN-TODO.md — Tasks Only Humans Can Do
> Source: profullstack/vibe-stack pattern.
> The agent reads this and NEVER attempts items on this list.
> It redirects the human instead.

---

## CRITICAL PATH (time-sensitive)

- [ ] **Submit Meta App Review** — pages_manage_posts + instagram_content_publish
  - URL: https://developers.facebook.com/apps
  - Wait time: 4-8 weeks — DO THIS TODAY
  - Without this: social posting module cannot go live

- [ ] **Register SSLCommerz merchant account**
  - URL: https://merchants.sslcommerz.com
  - Wait time: 7-10 business days
  - Without this: BD payments cannot process

---

## INFRASTRUCTURE

- [ ] **Set up Doppler** — 3 projects: agencyos-api, agencyos-web, agencyos-ai
  - URL: https://doppler.com

- [ ] **Configure Temporal Cloud namespace**
  - URL: https://cloud.temporal.io
  - Free tier: 10K actions/month (sufficient for beta)

- [ ] **Revoke exposed GitHub PAT**
  - URL: https://github.com/settings/tokens
  - SECURITY: do immediately

- [ ] **Oracle ARM: pull Qwen3.6 model**
  ```bash
  ssh oracle-arm
  ollama pull qwen3.6:35b-a3b-q4_k_m
  ```

- [ ] **Oracle ARM: run migrations**
  ```bash
  cd agencyos-api/go && goose up
  ```

---

## APP STORE / PLATFORM REGISTRATIONS

- [ ] **Google Play Console** — create developer account (one-time $25)
  - URL: https://play.google.com/console

- [ ] **Apple Developer Program** — create account ($99/year)
  - URL: https://developer.apple.com/programs

- [ ] **App Store Connect** — create app listing after Apple account

---

## BUSINESS / LEGAL

- [ ] **SSLCommerz merchant** — for BD bKash/card payments
- [ ] **Stripe account** — for international payments  
- [ ] **SR Creative Hub UK registration** — for UK client invoicing
- [ ] **Evolution API number** — WhatsApp Business number for each client

---

## AGENT INSTRUCTIONS

When the human asks about any of the above:
1. Read the specific item
2. Tell the human what needs to be done
3. Provide the exact URL
4. Tell them the wait time if applicable
5. Do NOT attempt to do it yourself
