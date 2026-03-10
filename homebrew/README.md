# Homebrew Skill — Installation Guide

Expert Homebrew guidance for your AI assistant. Each runtime section below is fully self-contained — find your tool and follow it straight through.

---

## Choose Your Runtime

<div align="center">

| ⬇️ [GitHub Copilot](#github-copilot) | ⬇️ [Codex](#codex) | ⬇️ [Claude Code](#claude-code) |
|:------------------------------------:|:-------------------:|:------------------------------:|
| VS Code · VS Code Insiders | `openai.chatgpt` extension | `claude.ai/code` desktop app |

</div>

---

## Runtime Support

| Runtime | Extension / App | Status |
|---------|----------------|--------|
| **GitHub Copilot** | `github.copilot-chat` (VS Code) | ✅ Supported |
| **Codex** | `openai.chatgpt` (VS Code) | ✅ Supported |
| **Claude Code** | `claude.ai/code` | ✅ Supported |
| Google Cloud Code | `googlecloudtools.cloudcode` | ❌ Not supported¹ |

> ¹ Google Cloud Code is a GCP infrastructure tool (GKE/Cloud Run). Its AI assistance (Gemini Code Assist) does not implement the Agent Skills protocol.

---

## GitHub Copilot

Applies to: **VS Code** and **VS Code Insiders** — they share the same skills directory, so install once and it works in both.

### Install

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Restart VS Code and open Copilot Chat (`⌘⇧I` on Mac · `Ctrl+Shift+I` on Windows/Linux)
2. Ask:
   ```
   How do I free up disk space used by Homebrew?
   ```
3. ✅ **Expected:** A step-by-step answer that mentions `brew info --sizes --installed`, `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`. If those commands appear — the skill is active.

### Update

```bash
rm -rf ~/.copilot/skills/homebrew
# Re-run the Install commands above
```

### Uninstall

```bash
rm -rf ~/.copilot/skills/homebrew
```

---

## Codex

Applies to: the **`openai.chatgpt`** extension in VS Code. Skills can be global (all projects) or project-local.

### Install

**Global — recommended for a system-wide tool like Homebrew:**

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.codex/skills/homebrew
rm -rf /tmp/hbc
```

**Project-local — active only in the current repository:**

```bash
mkdir -p .codex/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew .codex/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Open the Codex chat panel in VS Code
2. Ask:
   ```
   How do I free up disk space used by Homebrew?
   ```
3. ✅ **Expected:** A step-by-step answer that mentions `brew info --sizes --installed`, `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`. If those commands appear — the skill is active.

### Update

```bash
rm -rf ~/.codex/skills/homebrew     # global
# rm -rf .codex/skills/homebrew    # project-local
# Re-run the Install commands above
```

### Uninstall

```bash
rm -rf ~/.codex/skills/homebrew     # global
rm -rf .codex/skills/homebrew       # project-local (if installed)
```

---

## Claude Code

Applies to: the **Claude Code** desktop app (`claude.ai/code`). Skills can be global (all projects) or project-local.

### Install

**Global — recommended for a system-wide tool like Homebrew:**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.claude/skills/homebrew
rm -rf /tmp/hbc
```

**Project-local — active only in the current repository:**

```bash
mkdir -p .claude/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew .claude/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Open Claude Code and start a new conversation
2. Ask:
   ```
   How do I free up disk space used by Homebrew?
   ```
3. ✅ **Expected:** A step-by-step answer that mentions `brew info --sizes --installed`, `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`. If those commands appear — the skill is active.

### Update

```bash
rm -rf ~/.claude/skills/homebrew    # global
# rm -rf .claude/skills/homebrew   # project-local
# Re-run the Install commands above
```

### Uninstall

```bash
rm -rf ~/.claude/skills/homebrew    # global
rm -rf .claude/skills/homebrew      # project-local (if installed)
```

---

## What This Skill Covers

- Installing, upgrading, and removing formulae and casks
- The correct `update` → `upgrade` → `cleanup` → `autoremove` → `doctor` order
- Disk space management: assessment, cleanup, orphan removal, cache nuking
- Platform differences (Intel Mac / Apple Silicon / Linux)
- Cask upgrade gotchas: `--greedy`, macOS Ventura App Management permissions
- Environment variable reference (`HOMEBREW_*`)
- Brewfile backup and restore across machines
- `brew services` for launchd service management
- Pinning, version management, keg-only formulae
- Tap management
- Troubleshooting: `brew doctor`, `brew link`, `brew missing`, `brew migrate`

---

## Usage Examples

→ See [EXAMPLES.md](EXAMPLES.md) for complete prompt/response pairs.

Quick prompts to try after installing:

- `How much disk space is Homebrew using and how do I free it up?`
- `I switched from an Intel Mac to an M3. How do I migrate my Homebrew setup?`
- `How do I update apps like Chrome that Homebrew usually skips?`
- `Create a Brewfile that I can use to restore my setup on a new machine`
