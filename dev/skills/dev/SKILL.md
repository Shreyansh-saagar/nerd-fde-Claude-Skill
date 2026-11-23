---
name: dev
description: Auto-pick router for nerd-fde Developer commands. Use only when the user runs /dev:dev with a request; it chooses and runs the matching /dev:* command.
argument-hint: "<what you want done>"
disable-model-invocation: true
---

# Developer auto-pick

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
| `dev:implement` | build a feature or apply an approved fix |
| `dev:debug` | error, traceback, failing test or 'why is X happening' |
| `dev:plan-ticket` | 'go through ticket X', which files change, impact, no code yet |
| `dev:design` | database/API/architecture, HLD or LLD design for something new |
| `dev:refactor` | move, split or merge code without changing behaviour |
| `dev:review` | check quality of current changes before commit |
| `dev:commit` | commit message or committing current changes |
