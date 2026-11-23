---
name: learn
description: Guided learning of a codebase, library or technique (e.g. a PyTorch notebook, AG Grid, how a feature works) at the depth the user asks, with optional study notes as a doc. Use when the user runs /general:learn or asks to "help me understand this project", "teach me", or "create a doc explaining this file in detail".
argument-hint: "<topic, project path or file> [depth: overview | detailed | line-by-line] [doc]"
---

# Learn

Load `core:principles` first. Read only, except a notes doc if asked.

Topic: $ARGUMENTS (default depth: overview)

## Steps
1. Read the material first (project, notebook, file, official docs). Run nothing that changes
   the environment; if running code would help (e.g. a notebook cell), ask first, and use a
   virtual environment, never the system Python.
2. Ask what the user already knows if it is unclear; pitch just above that level.
3. Teach in layers:
   - **Big picture**: what it is for and the main parts, in 5-8 lines.
   - **How it fits together**: data or control flow, step by step.
   - **Details** at the requested depth: for line-by-line, explain each block's purpose,
     inputs, outputs and the key idea behind it (e.g. why the learning rate is set this way).
4. After each layer, offer 2-3 check questions or "try this" exercises, and ask whether to go deeper.

## Notes doc (only if asked)
- Sections mirror the layers above, with code snippets and real values from the material.
- Cite sources for library or API facts; flag anything uncertain.
- Confirm where to save it (repo docs folder, artifact or doc) before creating it.
