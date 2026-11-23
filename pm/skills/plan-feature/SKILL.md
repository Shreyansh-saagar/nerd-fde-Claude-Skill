---
name: plan-feature
description: Turn a feature idea or epic into a phased delivery plan with scope, non-goals, phases, risks and a tracking artifact, at product level rather than code level. Use when the user runs /pm:plan-feature or asks to brainstorm a feature, "create a phase plan", or plan a new epic.
argument-hint: "<feature or epic, ticket id, links to docs or prototype>"
---

# Plan a feature

Load `core:principles` first. Planning only; no code.
If the superpowers brainstorming skill is available and the idea is still fuzzy, use it first.

Feature: $ARGUMENTS

## Steps
1. Read the inputs: ticket, docs, prototype, related code areas (briefly, to know what exists).
2. Ask open questions one at a time, only where the answer changes the plan: who it is for,
   what success looks like, what must not happen.
3. Propose 2-3 delivery approaches (e.g. POC first vs full build) with trade-offs and a pick.

## Plan contents
- **Goal** and success measure, 2-3 lines.
- **In scope / out of scope / anti-goals**.
- **Users and permissions** affected (owner, shared read, shared full access).
- **Phases**: each small and shippable, with what the user can see at the end of it and how
  it will be tested.
- **Dependencies and risks**: data migration, old saved data, performance limits, AI cost,
  security.
- **Open decisions**: who decides, by when.

Offer to save it as an artifact or doc with a "Build log" section that is updated after every
phase (see `/pm:build-log`). If updating an existing plan, never overwrite earlier versions
without asking; add a new dated version instead.
Hand off: `/dev:design` for the technical design, `/pm:estimate` for sizing.
