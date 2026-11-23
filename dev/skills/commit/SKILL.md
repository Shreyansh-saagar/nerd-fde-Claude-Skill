---
name: commit
description: Write a short commit message for the current changes and commit only after the user confirms. Use when the user runs /dev:commit or asks for a commit message or to commit what we did.
argument-hint: "[files to include, ticket id, or 'msg only']"
---

# Commit

Load `core:principles` first.

Input: $ARGUMENTS

## Steps
1. Run `git status`, `git diff --stat` and read the diff. Show the current branch.
2. Flag before anything else: secrets, debug logs, large or generated files, files unrelated to
   the task, being on the main/master branch.
3. Propose:
   - Files to include (only the task's files; never `git add -A` blindly).
   - A commit message of about 10 words, imperative, with the ticket id if known
     (e.g. `GOR-355 show whole numbers on widgets, 2dp in grid`). Follow the repo's existing
     message style from `git log --oneline -10`.
4. If the user said "msg only", stop here.
5. Otherwise ask for confirmation. On yes, commit only those files with
   `git commit <files> -m "<msg>"` so nothing else gets staged.
6. Never push. Offer to push only if asked; pushing needs its own confirmation.
