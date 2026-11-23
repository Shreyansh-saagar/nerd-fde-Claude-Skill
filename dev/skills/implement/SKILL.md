---
name: implement
description: Implement a feature or bug fix end to end with a plan-first approval gate. Use when the user runs /dev:implement or asks to build, add or fix something in code and wants the toolkit workflow.
argument-hint: "<what to build or fix, ticket id, extra context>"
---

# Implement a feature or fix

Load `core:principles` first. Read the repo's CLAUDE.md "Project rules" if present.

Task: $ARGUMENTS

## 1. Understand (read only)
- If a ticket id is given, read it (Jira connector if available, otherwise ask the user to paste it).
- Trace the real flow end to end: entry point, every file the change touches, every caller of any
  function you will change.
- For a bug: find the root cause, not the symptom. Reproduce it if you can.

## 2. Plan, then stop
Reply with:
- What the change is, in 2-3 plain lines.
- Files to change, one line each: what changes and why.
- Risks: security, data, backwards compatibility (old saved data, existing users).
- How it will be verified.
- Anything you are unsure about, as a direct question.

Wait for explicit approval. Do not edit before it.

## 3. Build
- Only the approved files and scope. Smallest diff that fixes the root cause.
- Follow the project's conventions (markers, naming, file placement).
- Errors handled, inputs validated at trust boundaries.
- If the plan turns out wrong mid-way, stop and say so before changing direction.

## 4. Verify
- Run the narrowest relevant check (the specific test, a targeted script, an API call) unless the
  project rules say the user verifies themselves.
- Leave one runnable check behind for non-trivial logic, unless the user said no tests.

## 5. Report
- Changes, file by file, one line each.
- Evidence it works (output), and what was not tested.
- Manual test steps the user can follow.
- Do not commit. Offer `/dev:commit`.
