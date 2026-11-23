---
name: test-steps
description: Write manual test steps (and test prompts or inputs) the user will run themselves to check a fix or feature. Use when the user runs /qa:test-steps or asks "how do I test this manually", "steps to reproduce on UI", or "give me prompts to check X is fixed".
argument-hint: "<fix, feature or ticket id; optional: UI | API | swagger>"
---

# Manual test steps

Load `core:principles` first. Read only: the user runs the steps, you do not.

Target: $ARGUMENTS

## Steps
1. Work out exactly what changed (current diff, ticket or the last fix in this chat).
2. Pick the surface: UI by default; API/Swagger/curl if asked or if there is no UI.
3. Use the project's test data and environments from CLAUDE.md "Project rules" when present.

## Reply format
- **Setup**: branch, rebuild/restart needed, data to load, account/role.
- **Happy path**: numbered steps, each with the **expected result** on the same line.
- **Edge cases**: 2-5 cases most likely to break (empty, huge, mixed types, permissions,
  old saved data, refresh/back navigation).
- **Regression**: 1-3 nearby things that should still work.
- **Test inputs**: exact prompts, values or files to use, copy-paste ready.
- **To reproduce the original bug** (for fixes): steps that failed before the fix.

Keep it short. No percentages, scores or extra commentary unless asked.
