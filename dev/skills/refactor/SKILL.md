---
name: refactor
description: Restructure named code without changing behaviour (e.g. move logic from a controller to a service, merge duplicate endpoints). Use when the user runs /dev:refactor or asks to move, split, merge or clean up specific code.
argument-hint: "<what to restructure and why>"
---

# Refactor

Load `core:principles` first.

Request: $ARGUMENTS

## Rules
- Behaviour stays identical: same inputs, outputs, errors, side effects and API contract.
- Only the code the user named. No renames, style sweeps or "while I'm here" changes.
- Apply SOLID only where it serves the stated goal (e.g. single responsibility when moving logic
  out of a controller). No new interfaces with one implementation.

## Steps
1. Read the target code and every caller. Note existing tests covering it. Check the existing
   design (layers, module boundaries, design docs) so the new structure fits the HLD.
2. Plan: what moves where, new file/function names, callers updated. Wait for approval.
3. If there is no test covering the behaviour, propose a small characterisation test first.
4. Refactor in small steps. Keep imports and public names stable unless approved.
5. Verify: run the covering tests, or show before/after output for the same input.

## Report
Files changed with one line each, proof behaviour is unchanged, anything left as-is on purpose.
