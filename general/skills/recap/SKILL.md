---
name: recap
description: Quick recap in chat of what was done - in this session, on a ticket, or over a date range - as short bullets from git history and the conversation. Use when the user runs /general:recap or asks "what did we do", "summarise as 2-4 bullets", or "give me a summary of this phase". For writing the entry into a build log, use /pm:build-log instead.
argument-hint: "[this session | ticket id | date range] [n bullets]"
---

# Recap

Load `core:principles` first. Read only; chat output only.

Scope: $ARGUMENTS (default: this session)

## Sources (only these, never invent)
- This conversation.
- `git log` for the scope, author = the current git user, all branches if a date range.
- Ticket comments and status if a ticket id is given.

## Output
- Default: grouped by day or ticket, 2-4 short bullets each, plain words.
- If the user gives a bullet count or word limit, keep to it exactly.
- End with **Open items** (anything unfinished or untested) if there are any.
- Include commands the user needs again only if asked.
