# Claude Code (Anthropic) — Skill Discovery Analysis

**Source:** Official documentation at `code.claude.com/docs/en/skills`
**Date:** 2026-03-09
**Method:** Direct reading of official docs (redirected from `docs.anthropic.com/en/docs/claude-code/skills`)

---

## What is Claude Code?

Claude Code is Anthropic's agentic coding tool, available as:
- Terminal CLI (`claude` command)
- VS Code extension
- JetBrains plugin
- Desktop app
- Web interface

All surfaces share the same CLAUDE.md files, settings, and skill discovery mechanism.

---

## Skill Discovery Paths

### Priority Order

When skills share the same name across levels:
**enterprise > personal > project > plugin**

Plugin skills use a `plugin-name:skill-name` namespace (no conflicts possible).

### Path Table

| Level | Path | Scope |
|-------|------|-------|
| Enterprise | Managed settings | All users in organization |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All projects for this user |
| Project | `.claude/skills/<name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |

### Nested Directory Discovery

Claude Code automatically discovers skills from nested `.claude/skills/` directories.
For example, if editing `packages/frontend/`, Claude Code also looks in
`packages/frontend/.claude/skills/`. This supports monorepos.

---

## SKILL.md Format (Full Frontmatter Reference)

From official docs:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | No | Lowercase, numbers, hyphens only, max 64 chars. Defaults to directory name. |
| `description` | Recommended | Claude uses this to decide when to apply the skill. |
| `argument-hint` | No | Hint shown during autocomplete for expected arguments. |
| `disable-model-invocation` | No | `true` = only user can invoke (not Claude auto-invoke). Default: `false`. |
| `user-invocable` | No | `false` = hide from `/` menu. Default: `true`. |
| `allowed-tools` | No | Tools Claude can use without asking permission when skill is active. |
| `model` | No | Model to use when skill is active. |
| `context` | No | Set to `fork` to run in isolated subagent context. |
| `agent` | No | Which subagent type to use when `context: fork`. |
| `hooks` | No | Hooks scoped to this skill's lifecycle. |

**Claude Code extends the Agent Skills standard** with 5 extra fields (`allowed-tools`, `model`, `context`, `agent`, `hooks`).
These are **additive-only**: YAML parsers in other runtimes (Copilot, Codex) silently ignore unknown keys.

---

## Compliance Declaration

From official documentation (verbatim):
> "Claude Code skills follow the Agent Skills open standard, which works across multiple AI tools.
> Claude Code extends the standard with additional features like invocation control, subagent execution,
> and dynamic context injection."

Source: `code.claude.com/docs/en/skills` (introduction section)

---

## Compatibility with Our homebrew SKILL.md

Our current frontmatter:
```yaml
name: homebrew
description: >-
  (600 chars, covers all trigger cases)
argument-hint: "What do you want to do with Homebrew?"
user-invocable: true
version: "1.1.0"         ← after M2, ignored by Claude Code
maintainer: TzoharLary   ← after M2, ignored by Claude Code
```

All 4 original fields are natively supported by Claude Code. The 2 new fields (`version`, `maintainer`) are
unknown to Claude Code and will be silently ignored. ✅

---

## Invocation Model

### Two ways to invoke:
1. **Automatic:** Claude loads skill description into context. When query matches, Claude invokes.
2. **Manual:** User types `/homebrew <argument>`

### Three-tier loading (same as VS Code Copilot):
| Stage | What loads |
|-------|-----------|
| Always | Only `name` and `description` from frontmatter |
| When relevant | Full SKILL.md body |
| On demand | Supporting files referenced from SKILL.md |

### Invocation control:
| Frontmatter | User invoke | Claude auto-invoke |
|-------------|-------------|-------------------|
| (default) | ✅ | ✅ |
| `disable-model-invocation: true` | ✅ | ❌ |
| `user-invocable: false` | ❌ | ✅ |

---

## String Substitutions (Claude Code Only)

Claude Code supports dynamic values in skill content:

| Placeholder | Value |
|-------------|-------|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` | Specific argument by 0-based index |
| `$N` | Shorthand for `$ARGUMENTS[N]` |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's SKILL.md |

These are Claude Code-specific. Other runtimes will treat them as literal text.
Our homebrew skill does not use these substitutions — no compatibility issue.

---

## Installation Verification

From official docs example:
```bash
mkdir -p ~/.claude/skills/explain-code
# then create ~/.claude/skills/explain-code/SKILL.md
```

And invoke:
```
/explain-code src/auth/login.ts
```
Or ask: `How does this code work?` (auto-invoked when description matches)

---

## Conclusion

| Item | Value |
|------|-------|
| Supports SKILL.md? | ✅ Yes — declared Agent Skills compliance |
| Global path | `~/.claude/skills/<name>/SKILL.md` |
| Project path | `.claude/skills/<name>/SKILL.md` |
| Compatible with our frontmatter? | ✅ Full compatibility |
| Auto-discovery? | ✅ Yes |
| Env-var override? | Not documented |
| Extra features beyond standard? | `allowed-tools`, `model`, `context`, `agent`, `hooks` |
