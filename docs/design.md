# nerd-fde: design

Date: 2026-11-23
Owner: Shreyansh Saagar

## Intent

Bundle my recurring Claude Code work into reusable commands so I stop retyping the same
instructions and guardrails in every chat. Personal use, works across all my projects
(not tied to any one repo). May be shared with teammates later.

Built from an analysis of ~1,300 of my prompts (Jul to Nov 2026): roughly 40% dev,
30% QA, 15% PM, 15% general.

## Goals

- Named commands per area: `/dev:implement <context>`, `/qa:regression`, `/pm:jira-comment GOR-351`.
- An auto-pick command per area (`/dev:dev <what I want>`) that chooses the right command.
- My guardrails applied every time without retyping them.
- Hard blocks for the few actions that must never happen silently.

## Non-goals

- No project-specific rules inside the toolkit (those live in each repo's CLAUDE.md).
- No MCP servers, no external services, no paid anything.
- Not a replacement for superpowers, ponytail or mattpocock skills; commands may invoke them.

## Anti-goals (failure even if it "works")

- Commands that trigger when I meant a different skill.
- A hook that blocks normal work, or that blocks when it crashes.
- Long skill files that burn context on every use.
- Any skill that edits code, commits, pushes or writes to Jira/Slack without my explicit go-ahead.

## Approaches considered

| Approach | Trade-off | Verdict |
|---|---|---|
| A. Local marketplace, 5 plugins (core, dev, qa, pm, general) | Gives `dev:` prefixes, bundles hooks, versioned in git | **Chosen** |
| B. Plain skills in `~/.claude/skills/` | Simplest, but no prefixes, hooks set by hand | Rejected |
| C. One single plugin | One install, but `/toolkit:dev-implement` loses grouping | Rejected |

## Layout

```
~/nerd-fde/
  .claude-plugin/marketplace.json
  docs/design.md
  README.md
  core/     skills: principles, setup-project   hooks: hooks.json + guard.py
  dev/      skills: dev, implement, debug, plan-ticket, design, refactor, review, commit
  qa/       skills: qa, test-steps, regression, browser-test, coverage, verify-fix, security-check, report
  pm/       skills: pm, triage, plan-feature, estimate, jira-comment, stakeholder-note, build-log
  general/  skills: general, explain, recap, learn
```

Each plugin: `<plugin>/.claude-plugin/plugin.json` + `<plugin>/skills/<name>/SKILL.md`.
Skill frontmatter used: `name`, `description`, `argument-hint`, `allowed-tools` where a
skill must stay read-only. Arguments arrive as `$ARGUMENTS`.

## Guardrails

### Soft rules (core:principles, every skill reads it)

1. Plan first; no file edits until an explicit go-ahead ("do it"). "Can we..." is discussion.
2. Fix scope only; no extra refactors, guards or audits unless asked.
3. Minimal code; reuse what exists; SOLID only where it reduces real complexity.
4. Production code gets error handling and input validation.
5. Never output secrets; flag them and recommend rotation.
6. Security-sensitive code (auth, payments, data access): call out risks before the solution.
7. QA: before/after proof, honest pass/fail with output, no "should work".
8. Confirm before any external write (Jira, Slack, Drive, git push).
9. Plain language; distinguish verified facts from assumptions.
10. Obey the repo's CLAUDE.md "Project rules" section; it overrides toolkit defaults.

### Hard blocks (core hook, PreToolUse on Bash and Read)

- Ask: `git commit`, `git push`.
- Deny: `git push --force` / `-f`, `rm -rf` on `/`, `~` or broad paths, reading `.env*`, `*.pem`, `*.key`, `id_rsa*`.
- Fails open: any error inside the hook lets the command through.
- "Unapproved edits" cannot be detected by a script, so it stays a soft rule.

## Project rules

Each repo's CLAUDE.md gets a "Project rules" section (e.g. comment markers, frontend-only
policy, test datasets, ports). `/core:setup-project` drafts it.

## Delivery phases

0. Folder, git init, this doc.
1. Marketplace + 5 empty plugins; user installs; verify in `/plugin`.
2. core: principles, setup-project, hook + hook tests.
3. dev skills.  4. qa skills.  5. pm skills.  6. general skills.
7. Auto-pick skills + real trial on one small task; tune.
8. README; optional private GitHub push (ask first).

Pause after each phase for user trial.

## Left to the builder

Exact wording of skills, hook matching details, test fixtures.
