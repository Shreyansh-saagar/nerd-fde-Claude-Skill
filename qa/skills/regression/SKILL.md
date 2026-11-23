---
name: regression
description: Run a regression check myself across a graded set of cases (simple to complex) and datasets, and report pass/fail per case. Use when the user runs /qa:regression or asks to "do a regression test", "run the golden dataset", or "test this on different datasets".
argument-hint: "<feature or fix to cover; optional: number of cases, datasets, environment>"
---

# Regression run

Load `core:principles` first.

Scope: $ARGUMENTS

## 1. Plan, then confirm
- Find the project's regression set or datasets in CLAUDE.md "Project rules" or docs.
- Propose: environment (local/dev), datasets, and a case list graded simple to complex
  (default 10-15 cases). Include cases around the change and 2-3 unrelated smoke cases.
- State how each case is checked (API call, UI via browser, test command, SQL check).
- State the cost: number of cases, and whether sub-agents or browser automation are used.
- Wait for the user to confirm or trim the list. Skip areas the user excludes (e.g. auth).

## 2. Run
- Run cases one by one. Capture the actual output for each.
- Never mark a case passed without seeing the result. If a case cannot run, mark it BLOCKED
  with the reason; do not guess.
- Do not fix anything during the run. Note failures and continue.
- Read only on shared environments: no data deletion or destructive actions without asking.

## 3. Report
| # | Case | Dataset | Expected | Actual | Result |
- Result is PASS / FAIL / BLOCKED.
- Summary: totals, then each FAIL with a one-line suspected cause.
- What was not covered.
- Offer `/qa:report` to save it, and `/dev:debug` for failures.
