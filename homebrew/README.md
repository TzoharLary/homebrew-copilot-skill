# Homebrew Copilot Skill — Installation Guide

This skill provides expert Homebrew guidance to GitHub Copilot, Codex, and Claude Code. Once installed, your AI assistant will automatically use it when you ask questions about `brew` commands, package management, disk space, maintenance workflows, environment variables, and more.

---

## Runtime Compatibility

| Runtime | Extension / App | Supported |
|---------|----------------|-----------|
| **GitHub Copilot** | `github.copilot-chat` (VS Code) | ✅ Full support |
| **Codex** | `openai.chatgpt` (VS Code) | ✅ Full support |
| **Claude Code** | `claude.ai/code` | ✅ Full support |
| Google Cloud Code | `googlecloudtools.cloudcode` | ❌ Not supported¹ |

> ¹ Google Cloud Code is a GCP infrastructure tool (GKE/Cloud Run). Its AI assistance (Gemini Code Assist) uses its own context system and does not implement the Agent Skills standard.

---

## Prerequisites

- **git** (to clone this repo)
- One of the supported runtimes above

---

## Installation

### GitHub Copilot (VS Code / VS Code Insiders)

> VS Code and VS Code Insiders share the same personal skills directory. Install once, works in both.

**Method 1: Direct Clone (Recommended)**

```bash
mkdir -p ~/.copilot/skills
git clone --depth=1 --filter=blob:none --sparse \
  https://github.com/TzoharLary/homebrew-copilot-skill \
  ~/.copilot/skills/homebrew-repo

cd ~/.copilot/skills/homebrew-repo
git sparse-checkout set homebrew
mv homebrew ~/.copilot/skills/homebrew
cd .. && rm -rf homebrew-repo
```

**Method 2: Clone Full Repo (Simplest)**

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew
rm -rf /tmp/hbc
```

**Method 3: Manual Download**

1. Download: [GitHub → Code → Download ZIP](https://github.com/TzoharLary/homebrew-copilot-skill/archive/refs/heads/main.zip)
2. Extract and copy:
   ```bash
   mkdir -p ~/.copilot/skills
   cp -r ~/Downloads/homebrew-copilot-skill-main/homebrew ~/.copilot/skills/homebrew
   ```

---

### Codex (`openai.chatgpt` VS Code extension)

```bash
# Global (all projects)
mkdir -p ~/.codex/skills
cp -r /tmp/hbc/homebrew ~/.codex/skills/homebrew

# Project-local (current repo only)
mkdir -p .codex/skills
cp -r /tmp/hbc/homebrew .codex/skills/homebrew
```

---

### Claude Code

```bash
# Global (all projects) — personal skills
mkdir -p ~/.claude/skills
cp -r /tmp/hbc/homebrew ~/.claude/skills/homebrew

# Project-local (current repo only)
mkdir -p .claude/skills
cp -r /tmp/hbc/homebrew .claude/skills/homebrew
```

---

## Verify Installation

Open your AI assistant's chat and ask:

```
How do I free up disk space used by Homebrew?
```

You should get a detailed, step-by-step answer using `brew cleanup`, `brew autoremove`, and `brew info --sizes`.

To explicitly invoke the skill by name:

```
Use the homebrew skill to show me the weekly maintenance workflow
```

---

## Usage Examples

See [EXAMPLES.md](EXAMPLES.md) for prompt/response pairs showing the skill in action.

Quick examples:

- `How much disk space is Homebrew using and how do I free it up?`
- `I switched from an Intel Mac to an M3. How do I migrate my Homebrew setup?`
- `How do I update apps like Chrome that Homebrew usually skips?`
- `Create a Brewfile that I can use to restore my setup on a new machine`

---

## Updating the Skill

```bash
# Remove old version and re-install
rm -rf ~/.copilot/skills/homebrew
# (then repeat the install commands above)
```

For Codex/Claude Code, replace `~/.copilot/skills/homebrew` with the appropriate path.

---

## Uninstallation

```bash
# GitHub Copilot
rm -rf ~/.copilot/skills/homebrew

# Codex (global)
rm -rf ~/.codex/skills/homebrew

# Claude Code (global)
rm -rf ~/.claude/skills/homebrew
```

---

## What This Skill Covers

- Installing, upgrading, and removing formulae and casks
- The correct `update` → `upgrade` → `cleanup` → `autoremove` → `doctor` order
- Disk space management: assessment, cleanup, orphan removal, cache nuking
- Platform differences (Intel Mac / Apple Silicon / Linux)
- Cask upgrade gotchas: `--greedy`, macOS Ventura permissions
- Environment variable reference (`HOMEBREW_*`)
- Brewfile backup and restore across machines
- `brew services` for launchd service management
- Pinning, version management, keg-only formulae
- Tap management
- Troubleshooting: `brew doctor`, `brew link`, `brew missing`, `brew migrate`
