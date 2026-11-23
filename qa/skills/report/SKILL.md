---
name: report
description: Turn test results from this session (regression, browser, coverage, security, fix verification) into a shareable QA report. Use when the user runs /qa:report or asks to "create a report", "save results in an artifact", or "update the report with latest results".
argument-hint: "[audience: me | seniors | devops | client] [format: artifact | doc | markdown]"
---

# QA report

Load `core:principles` first.

Options: $ARGUMENTS (default: audience seniors, format artifact)

## Rules
- Only results actually run in this session or given by the user. Never invent numbers.
- If results are stale (code changed after the run), say so or offer to re-run first.
- Updating an existing report: read it first, keep earlier sections, add a dated update.
- Publishing or sharing anywhere: confirm with the user first. No secrets, tokens, real
  customer data or internal URLs beyond what the audience needs.
- Client-facing: British English, professional, no timeline or scope promises.

## Structure
1. **Summary**: 3-5 bullets: what was tested, overall result, key risks.
2. **Scope**: build/branch/commit, environment, datasets, what was excluded.
3. **Results**: table per test type with PASS / FAIL / BLOCKED.
4. **Issues found**: severity, steps to reproduce, status (open / fixed in this session).
5. **Fixes verified**: before/after evidence.
6. **Not tested / limitations**.
7. **Appendix** (on request): commands or SQL run, each with a one-line description.

Plain language for seniors and clients; include commands and file references for DevOps and devs.
