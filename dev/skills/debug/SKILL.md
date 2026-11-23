---
name: debug
description: Find the root cause of an error, traceback, failing test or wrong behaviour and explain it simply before any fix. Use when the user runs /dev:debug or pastes a stack trace, console log or screenshot of an error and asks why.
argument-hint: "<error, log, screenshot or symptom>"
---

# Debug

Load `core:principles` first.

Problem: $ARGUMENTS

If the user pasted only a log with no question, assume they want: cause, then proposed fix.

## Steps
1. Read the error fully. Note the exact message, file, line and the first frame in project code.
2. Form 1-3 hypotheses. For each, name the evidence that would confirm or kill it.
3. Check them cheapest first: read the code path, check config, run a targeted command, add a
   temporary log only if needed (and say you will remove it).
4. Confirm the root cause with evidence. If you cannot reproduce it, say so plainly.

## Reply
- **Cause** in simple words, 1-3 bullets.
- **Evidence**: the line, output or behaviour that proves it.
- **Fix**: files and what changes, smallest correct option first. Note other callers affected.
- **How to verify** the fix.

Do not apply the fix until the user approves. Then follow `/dev:implement` steps 3-5.
Never print secrets from logs or config; refer to them by name.
