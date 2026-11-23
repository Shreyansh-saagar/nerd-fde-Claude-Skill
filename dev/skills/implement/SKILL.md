---
name: implement
description: Implement a feature or bug fix end to end with a plan-first approval gate, HLD/LLD check, SOLID and best practices, and a step-by-step walkthrough at the end. Use when the user runs /dev:implement or asks to build, add or fix something in code and wants the toolkit workflow.
argument-hint: "<what to build or fix, ticket id, extra context>"
---

# Implement a feature or fix

Load `core:principles` first (section 3 holds the full code quality and SOLID rules).
Read the repo's CLAUDE.md "Project rules" if present.

Task: $ARGUMENTS

## 1. Understand (read only)
- If a ticket id is given, read it (Jira connector if available, otherwise ask the user to paste it).
- Trace the real flow end to end: entry point, every file the change touches, every caller of any
  function you will change.
- For a bug: find the root cause, not the symptom. Reproduce it if you can.
- **Check the existing design**: look for HLD/LLD material (architecture or design docs, ADRs,
  specs, README sections, CLAUDE.md). If none exists, infer the current design from the code:
  layers (route, controller, service, repository, UI component, API client), module boundaries,
  data flow. The change must fit that design, not fight it.

## 2. Plan, then stop
Reply with:
- What the change is, in 2-3 plain lines.
- **HLD fit**: which modules/layers are involved and how data flows between them. Say clearly if
  the change alters the architecture (new service, new table, new dependency, new boundary).
- **LLD**: for each file, the functions/components/types added or changed, their inputs and
  outputs, and where new code sits (the file that already owns the concern).
  Size this to the change: one line per file for a small fix, fuller for a feature.
- **Design choices**: which SOLID principle or pattern applies and why, only where it matters
  (e.g. "logic moves into the service, controller stays thin: single responsibility").
- Risks: security, data, backwards compatibility (old saved data, existing users).
- How it will be verified.
- Anything you are unsure about, as a direct question.

Wait for explicit approval. Do not edit before it.

## 3. Build
- Only the approved files and scope. Smallest diff that fixes the root cause.
- Follow the approved HLD/LLD. If it turns out wrong mid-way, stop and say so before changing
  direction.
- **SOLID**, applied where it removes real complexity (see `core:principles` §3):
  one responsibility per unit, extend through existing seams, keep contracts callers rely on,
  small focused interfaces, abstractions only at real boundaries (I/O, network, DB).
- **Best practices**:
  - Reuse existing helpers, types and patterns before writing new ones; no duplication.
  - Clear, intention-revealing names; small functions; early returns over deep nesting.
  - Strong typing where the language supports it; no `any`/untyped escapes without reason.
  - No magic numbers or strings: use the project's constants/config.
  - Errors handled explicitly with useful messages; inputs validated at trust boundaries;
    nothing swallowed silently.
  - Follow the framework's idioms and the project's conventions (markers, naming, file placement).
  - No leftover debug code, commented-out code or unused imports.
- **Self-check before verifying**: re-read your diff against the checklist above and the
  `/dev:review` checks (correctness, scope, security, quality). Fix what you find.

## 4. Verify
- Run the narrowest relevant check (the specific test, a targeted script, an API call) unless the
  project rules say the user verifies themselves.
- Leave one runnable check behind for non-trivial logic, unless the user said no tests.

## 5. Walkthrough (end of every implementation)
Give the user a step-by-step walkthrough, in plain language:
1. **Summary**: what was built or fixed, in 2-3 lines.
2. **How it works now**: numbered flow from where the user acts (click, API call) through each
   layer to the result, naming the file and function at each step.
3. **Changes file by file**: what changed and why, one or two lines each, with `file:line`.
4. **Design notes**: how it fits the HLD/LLD, which principles were applied, anything
   deliberately left simple and when to revisit it.
5. **Evidence**: checks run and their output; what was not tested.
6. **Manual test steps**: numbered, each with the expected result.
7. **Next steps**: follow-ups, open questions, risks.

Do not commit. Offer `/dev:review` and `/dev:commit`.
