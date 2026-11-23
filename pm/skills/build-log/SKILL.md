---
name: build-log
description: Keep a running build log for a feature - add a plain-language entry after each phase or step with what was done, decisions, tests and open items - or produce a recap of recent work. Use when the user runs /pm:build-log, asks to "update the build log", "summarise this phase", or "what did we do on Monday and Tuesday".
argument-hint: "<update | recap> [feature or doc link] [date range]"
---

# Build log

Load `core:principles` first.

Input: $ARGUMENTS (default: update)

## Update
1. Find the log: the doc/artifact the user names, or the one used earlier for this feature.
   If none exists, propose a location (repo docs folder or an artifact) and ask.
2. Read the current log first. Append; never rewrite earlier entries.
3. Add an entry:
   - **Date** and phase/step name.
   - **Done**: 2-5 plain bullets a non-developer can follow.
   - **Decisions** made and why.
   - **Tested**: what and the result; what was not tested.
   - **Open items / known gaps**.
   - **Commands** the user needs (migrations, scripts), if any.
4. Show the entry; write it after approval (or directly if the user set that standing rule
   for this log).

## Recap
- Sources: git log for the date range (author = the user), this conversation, the build log,
  ticket updates.
- Output: per day or per ticket, 2-4 short bullets each. Only what the sources show.
