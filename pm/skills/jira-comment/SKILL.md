---
name: jira-comment
description: Draft a Jira comment for a ticket (status update, why something happens, out of scope, question for the PM, done summary) and post it only after explicit approval. Use when the user runs /pm:jira-comment or asks to write or post a comment on a ticket.
argument-hint: "<ticket id> <what the comment should say or its purpose>"
---

# Jira comment

Load `core:principles` first.

Input: $ARGUMENTS

## Steps
1. Read the ticket and its recent comments (Jira connector) so the comment fits the thread
   and does not repeat what is already said.
2. If the comment explains behaviour or a fix, check the facts in the code or test results first.
3. Draft the comment:
   - First line: the point (done / question / why it happens / out of scope).
   - Then 2-5 short bullets with plain-language detail and real examples
     (e.g. "£1,747,936.45 now shows as £1,747,937").
   - Questions numbered, so the reader can answer by number.
   - Mentions (@name) only for people the user names.
   - Professional and concise; British English; no em-dashes; no timeline or scope promises.
   - No secrets, internal URLs, credentials or customer data.
4. Show the draft and stop.
5. Post only after the user explicitly says to post it. Post exactly the approved text.
   Never edit, delete or transition the ticket unless separately asked and confirmed.
