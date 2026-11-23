---
name: general
description: Auto-pick router for nerd-fde General commands. Use only when the user runs /general:general with a request; it chooses and runs the matching /general:* command.
argument-hint: "<what you want done>"
disable-model-invocation: true
---

# General auto-pick

Request: $ARGUMENTS

1. Pick the single best match from the table. Judge by what the user wants as the outcome,
   not by keywords alone.
2. If the request is empty, list the commands below in one short table and ask what they want.
3. If two commands fit equally and the choice changes what happens (e.g. explain vs fix),
   ask one short question naming both. Otherwise pick.
4. Say in one line which command you picked and why, then invoke it with the Skill tool,
   passing the user's request as args. Follow that skill fully, including its approval gates.
5. If the request belongs to another area (dev / qa / pm / general), say so and use that
   area's command instead.

| Command | Pick when the user wants |
|---|---|
| `general:explain` | explain code, a flow, a concept or a decision simply |
| `general:recap` | what was done in a session, ticket or date range |
| `general:learn` | guided learning of a codebase, library or technique |
