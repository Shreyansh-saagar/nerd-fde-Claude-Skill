---
name: verify-fix
description: Prove a fix works by reproducing the bug without the fix and showing it gone with the fix (before/after), then checking nearby behaviour. Use when the user runs /qa:verify-fix or asks "is it really fixed", "stash and test again", "are you sure", or "test ABC-123 again".
argument-hint: "<bug or ticket id; optional: environment, inputs>"
---

# Verify a fix (before / after)

Load `core:principles` first.

Bug: $ARGUMENTS

## Steps
1. State the bug's exact reproduction: input, steps, wrong result, expected result.
2. **Before**: get a state without the fix.
   - Uncommitted fix: `git stash push -- <fix files>` (tell the user first), or
   - Committed fix: check out the parent commit in a temporary worktree, or
   - Deployed env: compare against an environment without the fix.
   Reproduce the bug and capture the output. If it does not reproduce, stop and say so:
   the test is not proving anything.
3. **After**: restore the fix (`git stash pop`, confirm the files are back), run the same
   reproduction, capture the output.
4. Run 2-4 nearby cases to check nothing else broke.
5. Always restore the working tree to how it was. Confirm with `git status`.

## Report
| Step | Without fix | With fix |
- Verdict: FIXED / NOT FIXED / PARTIAL / CANNOT REPRODUCE.
- Nearby checks with results.
- Anything not tested.
