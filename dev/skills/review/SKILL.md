---
name: review
description: Review current uncommitted changes or a branch against toolkit standards (scope, SOLID, code quality, security, tests) and report findings without editing. Use when the user runs /dev:review or asks to check code quality of what we changed before committing.
argument-hint: "[base branch, commit or file paths; default: uncommitted changes]"
---

# Review changes

Load `core:principles` first. Read only: report, do not fix.

Target: $ARGUMENTS (empty means uncommitted changes: `git diff` + `git diff --staged` + untracked files)

## Check, in this order
1. **Correctness**: logic errors, missed callers, broken edge cases (empty, null, large, mixed
   types), old saved data still working.
2. **Scope**: anything changed that the task did not ask for.
3. **Security**: secrets in code, missing auth/permission checks, unvalidated input,
   injection, unsafe logging of user data.
4. **Quality**: duplication of existing helpers, wrong file placement, dead code, debug leftovers,
   swallowed errors, project conventions (markers, naming).
5. **SOLID**: only flag violations that cause real harm (mixed concerns, leaky contracts,
   god objects); not theoretical ones.
6. **Tests**: is the changed logic covered; do existing tests still make sense.

## Report
- Verdict: ready / needs changes.
- Findings ranked most severe first: `file:line`, problem, why it matters, suggested fix.
- Mark each finding as verified (you traced it) or suspected.
- No findings in a category: say so in one line.

Offer to fix the findings via `/dev:implement` after approval.
