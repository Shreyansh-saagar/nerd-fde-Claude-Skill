---
name: estimate
description: Estimate effort, size, number of files touched, or running cost (e.g. AI calls and token cost per action) for a ticket or feature, with stated assumptions and ranges. Use when the user runs /pm:estimate or asks "how big is this", "how many files", "how long", or "what will one call cost".
argument-hint: "<ticket, feature or flow; optional: effort | files | cost>"
---

# Estimate

Load `core:principles` first. Read only.

Target: $ARGUMENTS

## Rules
- Ground every number in something checked: files found in the code, measured token counts,
  current published prices. Never invent figures; if a number is a guess, label it.
- Give ranges (low / likely / high), not a single point.
- State assumptions explicitly; the estimate is only as good as they are.
- No timeline commitments on the user's behalf in anything client-facing.

## Effort / size
- Map the work: files and areas to change (use a quick code trace; `/dev:plan-ticket` for depth).
- Size: S / M / L with file count, plus test and QA effort, plus unknowns that could grow it.

## Running cost (AI features)
- Count AI calls per user action, including retries and tool-use rounds.
- Per call: input tokens (system + tools + context + history), output tokens, cache hits.
- Look up current model prices (claude-api skill or official pricing page); cite the source.
- Scenarios: min / typical / max (e.g. short question, typical, long history with large data).

## Reply
Summary line first, then a table of the breakdown, then assumptions and risks to the estimate.
