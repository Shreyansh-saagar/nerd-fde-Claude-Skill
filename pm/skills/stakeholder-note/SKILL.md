---
name: stakeholder-note
description: Write a short explanation or update for seniors, DevOps, PMs or clients - how something works, what was fixed, what decision is needed - pitched to that audience. Use when the user runs /pm:stakeholder-note or asks to "explain this to my seniors", "write it up for DevOps", or "draft an update for the client".
argument-hint: "<audience: seniors | devops | pm | client> <topic>"
---

# Stakeholder note

Load `core:principles` first.

Input: $ARGUMENTS

## Pitch by audience
- **Seniors / PM**: what it is, why it matters, status, risks, decision needed. Light technical
  detail; one simple diagram or flow if it helps.
- **DevOps**: exact config, env vars by name (never values), headers, commands, rollout and
  rollback steps, owner of each action.
- **Client**: plain language, British English, outcomes not internals, no speculative timelines
  or scope commitments, no internal names of other clients.

## Structure
1. **One-line summary**.
2. **Context**: 2-3 lines.
3. **What happened / how it works**: short bullets or numbered flow, with a real example.
4. **Impact and risks**.
5. **Ask**: the decision or action needed, from whom.

## Rules
- Only verified facts; mark assumptions.
- No secrets, credentials, real customer data.
- Format: chat text by default; artifact or doc if the user asks or it will be shared.
  Confirm before publishing or sending anywhere.
