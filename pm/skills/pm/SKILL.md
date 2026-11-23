---
name: pm
description: Auto-pick router for claude-toolkit PM commands. Use only when the user runs /pm:pm with a request; it chooses and runs the matching /pm:* command.
argument-hint: "<what you want done>"
disable-model-invocation: true
---

# PM auto-pick

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
| `pm:triage` | what the real problem is, valid/duplicate/done/out of scope, priority |
| `pm:plan-feature` | phased product plan for a feature or epic |
| `pm:estimate` | size, file count, effort or AI running cost |
| `pm:jira-comment` | draft (and on approval post) a ticket comment |
| `pm:stakeholder-note` | explanation or update for seniors, DevOps, PM or client |
| `pm:build-log` | add an entry to a feature's build log |
