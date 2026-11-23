---
name: qa
description: Auto-pick router for nerd-fde QA commands. Use only when the user runs /qa:qa with a request; it chooses and runs the matching /qa:* command.
argument-hint: "<what you want done>"
disable-model-invocation: true
---

# QA auto-pick

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
| `qa:test-steps` | manual steps or test prompts for the user to run |
| `qa:regression` | run many cases across datasets myself, pass/fail table |
| `qa:browser-test` | test flows in the real browser |
| `qa:coverage` | run test suites, coverage numbers, or write tests |
| `qa:verify-fix` | prove a fix with before/after ('are you sure', 'test X again') |
| `qa:security-check` | security test of code or an owned URL |
| `qa:report` | turn test results into a shareable report |
