---
name: browser-test
description: Test a web app flow in the real browser (Claude in Chrome or the built-in browser) and report what works, what breaks, with screenshots or GIF on request. Use when the user runs /qa:browser-test or asks to "test this in the browser", "check every flow on UI", or "use claude-in-chrome".
argument-hint: "<URL or environment, flows to check>"
---

# Browser test

Load `core:principles` first. Load the browser skill for the tool you use
(chrome-browser / claude-in-chrome, or built-in-browser) before the first browser call.

Target: $ARGUMENTS

## Before starting
- Confirm URL/environment and the flows to cover. List them back as a checklist.
- The user logs in themselves. Never type passwords or secrets unless the user gives them for
  this test; never save them.
- Open a new tab; do not reuse the user's tabs unless asked.
- Avoid actions that trigger native dialogs (delete confirms, alerts). Warn first if needed.
- On shared environments (dev/prod): no destructive actions without asking. Create test
  items with a clear prefix (e.g. `QA-test-`) and say what you created.

## Run
- One flow at a time. For each: steps taken, expected, actual, PASS/FAIL.
- Check the console and network for errors on each failed step.
- Record a GIF if the user asked for one or a failure needs showing.
- After 2-3 failed attempts at the same browser action, stop and ask.

## Report
- Checklist with PASS / FAIL / BLOCKED per flow.
- Each failure: steps to reproduce, what was seen, console/network error if any.
- Test data created, so the user can clean it up.
