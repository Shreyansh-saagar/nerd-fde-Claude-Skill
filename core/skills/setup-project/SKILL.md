---
name: setup-project
description: Draft a "Project rules" section in the current repo's CLAUDE.md so nerd-fde commands know this project's conventions. Use when the user runs /core:setup-project or asks to "set up project rules" for the toolkit.
argument-hint: "[extra notes about this project]"
---

# Set up project rules

Load `core:principles` first.

User notes: $ARGUMENTS

## Steps

1. Inspect the repo (read only): README, CLAUDE.md, package/dependency files, Makefile, docker
   files, CI config, test config, folder layout. Run `git branch -a` and `git log --oneline -15`.
2. Draft the section below. Fill only what you verified; mark guesses with `(confirm)`.
   Leave a line out rather than invent it.
3. Show the draft. Ask what to change. Do not write yet.
4. After explicit approval, add or replace the `## Project rules` section in CLAUDE.md
   (create CLAUDE.md if missing). Touch nothing else in the file.

## Template

```markdown
## Project rules

### Stack
- Frontend: ...
- Backend: ...
- Database / migrations: ...

### Commands
- Run: ...
- Tests (unit / integration / e2e): ...
- Lint / type check: ...
- Ports: ...

### Conventions
- File and naming conventions: ...
- Change markers (e.g. comment prefix on every change): ...
- Where new helpers and types go: ...

### Scope policy
- e.g. UI requests are frontend only; never touch X without asking

### Testing
- Test datasets / fixtures: ...
- Regression set: ...
- Environments (local / dev / prod URLs): ...

### Workflow
- Ticket prefix (e.g. ABC-123) and tracker: ...
- Branching and PR target: ...
- Do not auto-run: ... (e.g. build after every edit)
```
