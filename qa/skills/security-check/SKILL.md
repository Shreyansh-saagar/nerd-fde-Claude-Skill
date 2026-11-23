---
name: security-check
description: Non-destructive security check of code changes or a web app the user owns (headers, auth, tokens, cookies, input validation, secrets, dependencies) with verified findings only. Use when the user runs /qa:security-check or asks for a security test or security review of their app or URL.
argument-hint: "<code | URL the user owns or is authorised to test> [focus area]"
---

# Security check

Load `core:principles` first.

Target: $ARGUMENTS

## Rules of engagement
- Only targets the user owns or is authorised to test. If unclear, ask before starting.
- Non-destructive only: no DoS, brute force, data deletion, or exploiting beyond proof.
  Low request volume. No scanning third-party hosts.
- Never print secrets or tokens found; refer to them by location and recommend rotation.

## Code checks
- Auth and permissions on every route touched; ownership checks on IDs (IDOR).
- Token handling: storage, expiry, refresh, scope (e.g. shared links cannot gain owner rights).
- Input validation, SQL/NoSQL injection, unsafe deserialisation, path traversal, XSS.
- Secrets in code or logs; verbose error messages; CORS configuration.
- Dependencies: run the project's audit tool (npm audit, pip-audit) if available.

## Live URL checks (read-only requests)
- Security headers: CSP, HSTS, X-Content-Type-Options, frame-ancestors/X-Frame-Options,
  Referrer-Policy; server version disclosure.
- Cookies: Secure, HttpOnly, SameSite.
- Auth endpoints: error messages, rate-limit presence (observe, do not hammer).
- Exposed docs, debug or admin endpoints.

## Report
Findings ranked Critical / High / Medium / Low. Each: what, where (`file:line` or URL), evidence,
impact in plain words, fix. Mark verified vs suspected. List what was not checked.
Offer `/qa:report` to write it up for seniors or DevOps.
