---
name: design
description: Produce a technical design for a feature (data model, API, flow, edge cases) sized to the need, before any code. Use when the user runs /dev:design or asks for a database design, API design, architecture or "how should we build X".
argument-hint: "<feature or problem to design>"
---

# Technical design

Load `core:principles` first. Read only: no product code in this skill.

Feature: $ARGUMENTS

## Steps
1. Read the existing code, models and migrations this touches. Build on what exists.
2. Ask at most one or two questions, only where the answer changes the design.
3. Size it: a small change gets a short design, a project gets the full one. Prefer POC level
   when the user is still validating the idea.

## Design contents (skip what does not apply)
- **Goal** and non-goals, 2-4 lines.
- **Approaches**: 2-3 options, trade-offs, your pick and why.
- **Data model**: tables/columns, one line per column on its purpose; indexes; migration and
  rollback; what happens to existing rows.
- **API**: endpoints, request/response shape, auth and permission checks.
- **Flow**: frontend to backend to DB, step by step.
- **Edge cases and limits**: size caps, concurrency, partial failure, old data.
- **Security**: who can read/write what; risks called out explicitly.
- **Cost** (if AI calls are involved): number of calls per action, rough token cost.
- **Phases**: small shippable steps.

Offer to save the design as a doc (repo docs folder or an artifact). Implementation only after
explicit approval, via `/dev:implement`.
