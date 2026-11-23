---
name: coverage
description: Run unit, integration and e2e test suites and report results and coverage, overall and per feature, for frontend and backend; optionally write missing tests. Use when the user runs /qa:coverage or asks "run the tests", "what is the coverage", or "write e2e for feature X".
argument-hint: "[frontend | backend | e2e | all] [feature] [write: <feature>]"
---

# Tests and coverage

Load `core:principles` first.

Scope: $ARGUMENTS (default: all suites, report only)

## Run and report
1. Find the test commands in CLAUDE.md "Project rules", package.json, pytest/vitest/playwright config.
   If a suite needs services (DB, docker, browser) that are not running, say so and ask.
2. Run each suite. Capture totals: passed / failed / skipped, duration.
3. Run coverage where configured. Report lines (and branches if available):
   - overall, frontend and backend separately
   - per feature: group files by feature folder/module; list the lowest-covered features
4. For failures: test name, error message, likely cause (test bug vs code bug), verified or suspected.

| Suite | Passed | Failed | Skipped | Coverage |

## Writing tests (only if asked with `write`)
- Read the feature and existing tests first; match the project's test style and fixtures.
- Cover behaviour users rely on: happy path, key edge cases, permissions, error states.
- No snapshot spam, no testing implementation details, no tests that pass without asserting.
- Run the new tests and show them passing; report the coverage change before/after.

Never edit production code to make a test pass without saying so and asking.

## Clean up
Delete coverage output you generated (e.g. `coverage/`, `htmlcov/`, `.coverage`, test-results)
unless the user asked to keep it or it existed before the run. Confirm `git status` matches
what it was before you started.
