---
name: explain
description: Explain code, a concept, a flow or a decision in simple words with a real example - a line of code, a file-by-file flow from frontend to backend, why a rule exists, or what changed. Use when the user runs /general:explain or asks "explain in simple words", "what does this line do", "why do we have X", or "walk me through the flow".
argument-hint: "<code, file:line, concept, flow or decision to explain>"
---

# Explain

Load `core:principles` first. Read only.

Topic: $ARGUMENTS

## Steps
1. Read the actual code, history or docs behind the topic. For "why does X exist", check git
   log/blame and ticket references for the real reason; do not guess.
2. Pick the shape that fits:
   - **A line or function**: what it does, why it is there, what breaks without it.
   - **A flow**: numbered steps, file by file, from where the user clicks to the database and back.
   - **A concept**: plain definition, then how it applies in this project.
   - **A decision or rule**: the problem it solved, the alternative rejected, when to revisit it.
   - **What changed**: file by file, one plain line each.

## Style
- Simple English, short sentences, no jargon without a one-line meaning.
- Always one real example from this project (actual values, actual screen).
- Lead with the one-sentence answer, then the detail.
- Mark anything not verified in the code as an assumption.
- Offer to go deeper on one part rather than explaining everything at once.
