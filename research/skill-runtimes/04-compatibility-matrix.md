# Runtime Compatibility Matrix

**Date:** 2026-03-09
**Based on:** Files 01–03 in this directory

---

## Full Cross-Runtime Table

| Runtime | Global path | Project path | Agent Skills standard | Frontmatter compatible | Auto-discovery | Source verified |
|---------|------------|--------------|----------------------|----------------------|----------------|-----------------|
| **GitHub Copilot** (VS Code) | `~/.copilot/skills/<name>/` | `.copilot/skills/<name>/` or `.github/skills/<name>/` | ✅ Primary implementation | ✅ Full | ✅ | `code.visualstudio.com/docs/copilot/customization/agent-skills` |
| **Claude Code** | `~/.claude/skills/<name>/` | `.claude/skills/<name>/` | ✅ Declared compliance | ✅ Full | ✅ | `code.claude.com/docs/en/skills` |
| **Codex** (openai.chatgpt) | `~/.codex/skills/<name>/` | `.codex/skills/<name>/` | ✅ Compatible | ✅ Full | ✅ | Extension source code `extension.js` |
| **Google Cloud Code** | ❌ None | ❌ None | ❌ Not implemented | N/A | ❌ | `cloud.google.com/code/docs/vscode/overview` |

---

## Install Table for `homebrew/README.md`

This is the exact table to use in the README:

```markdown
| AI Runtime | Global (all projects) | Project-level |
|---|---|---|
| **GitHub Copilot** (VS Code) | `~/.copilot/skills/homebrew/` | `.copilot/skills/homebrew/` |
| **Claude Code** (Anthropic) | `~/.claude/skills/homebrew/` | `.claude/skills/homebrew/` |
| **Codex** (OpenAI VS Code) | `~/.codex/skills/homebrew/` | `.codex/skills/homebrew/` |
```

Followed by:
```markdown
> **Note:** Google Cloud Code uses Gemini Code Assist, which does not implement
> the Agent Skills protocol and is therefore not listed above.
```

---

## Frontmatter Compatibility Details

### Fields recognized by each runtime

| Field | GitHub Copilot | Claude Code | Codex |
|-------|---------------|-------------|-------|
| `name` | ✅ Required | Optional (defaults to dir name) | ✅ Read |
| `description` | ✅ Required | Recommended | ✅ Read |
| `argument-hint` | ✅ | ✅ | Ignored |
| `user-invocable` | ✅ | ✅ | Ignored |
| `disable-model-invocation` | ✅ | ✅ | Ignored |
| `version` | Ignored | Ignored | Ignored |
| `maintainer` | Ignored | Ignored | Ignored |
| `allowed-tools` | ❌ Unknown | ✅ Claude-specific | Ignored |
| `model` | ❌ Unknown | ✅ Claude-specific | Ignored |
| `context` | ❌ Unknown | ✅ Claude-specific | Ignored |

**Key conclusion:** Our homebrew SKILL.md frontmatter (`name`, `description`, `argument-hint`, `user-invocable`, `version`, `maintainer`) is safe across all three supported runtimes. Unknown fields are silently ignored in all cases.

---

## Recommended Installation Level for This Skill

| Runtime | Recommended level | Reason |
|---------|------------------|--------|
| GitHub Copilot | Personal (`~/.copilot/skills/`) | Homebrew is system-wide, not project-specific |
| Claude Code | Personal (`~/.claude/skills/`) | Same reasoning |
| Codex | Personal (`~/.codex/skills/`) | Same reasoning |

Project-level installation (`.copilot/skills/`, `.claude/skills/`, `.codex/skills/`) is
valid but suboptimal for a system-wide tool like Homebrew. Reserve project-level installation
for skills that are specific to a particular codebase.
