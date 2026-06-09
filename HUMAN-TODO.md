# HUMAN-TODO.md — Tasks Only Humans Can Do
> Source: profullstack/vibe-stack pattern.
> Agents read this and REDIRECT to the human instead of attempting these tasks.
> Fill with YOUR project's human-only tasks.

---

## HOW AGENTS USE THIS FILE

When a user asks Claude to do something on this list:
1. Read the item
2. Tell the human what needs to be done
3. Provide the URL or exact steps
4. Do NOT attempt to do it — stop and wait for human action

---

## TEMPLATE CATEGORIES

### Platform / API Registrations
- [ ] {platform}: create developer account
  - URL: {url}
  - Required for: {what feature}

### Infrastructure
- [ ] Set up secrets manager ({Doppler / Vault / AWS Secrets})
- [ ] Configure production hosting
- [ ] Set up CI/CD webhooks

### Business / Legal
- [ ] Register payment processor merchant account
- [ ] App Store submission (Apple Developer Program)
- [ ] Google Play Console setup

### Security
- [ ] Rotate any exposed credentials
- [ ] Review OAuth app permissions
- [ ] Set up monitoring alerts

---

## YOUR PROJECT ITEMS

<!-- Add your project-specific human-only tasks below -->
<!-- Format: - [ ] {task}: {why + URL + wait time} -->

{YOUR_HUMAN_TASKS_HERE}

---

## COMMON PATTERNS

### OAuth API Review (e.g. Meta, Google, Twitter)
Submit immediately — reviews take 4-8 weeks.
Every day you delay = a day later your feature ships.

### Payment Processor (Stripe, PayPal, local providers)
Register before billing module is built — approval takes 7-14 days.

### App Store
Build the app first, then submit. But create developer account early.
Apple: $99/year, 1-2 day review after submission.
Google Play: $25 one-time, 3-7 day review.
