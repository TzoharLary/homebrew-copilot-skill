# Homebrew Copilot Skill — Installation Guide

This skill provides expert Homebrew guidance to GitHub Copilot. Once installed, Copilot will automatically use it when you ask questions about `brew` commands, package management, disk space, maintenance workflows, environment variables, and more.

---

## Prerequisites

- **GitHub Copilot** subscription (or active trial)
- **VS Code** (any version) or **VS Code Insiders** with the GitHub Copilot extension installed
- **git** (to clone this repo)

---

## Installation

> **VS Code and VS Code Insiders share the same personal skills directory** (`~/.copilot/skills/`). You only need to install once — it works for both.

### Method 1: Direct Clone (Recommended)

```bash
# Create skills directory if needed
mkdir -p ~/.copilot/skills

# Clone only the skill folder into your personal skills directory
git clone --depth=1 --filter=blob:none --sparse \
  https://github.com/TzoharLary/homebrew-copilot-skill \
  ~/.copilot/skills/homebrew-repo

cd ~/.copilot/skills/homebrew-repo
git sparse-checkout set homebrew

# Move the skill to the right location
mv homebrew ~/.copilot/skills/homebrew
cd .. && rm -rf homebrew-repo
```

### Method 2: Clone Full Repo (Simplest if you have space)

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/homebrew-copilot-skill
cp -r /tmp/homebrew-copilot-skill/homebrew ~/.copilot/skills/homebrew
rm -rf /tmp/homebrew-copilot-skill
```

### Method 3: Manual Download

1. Download the repository as a ZIP: [GitHub → Code → Download ZIP](https://github.com/TzoharLary/homebrew-copilot-skill/archive/refs/heads/main.zip)
2. Extract the ZIP
3. Copy the `homebrew/` folder into `~/.copilot/skills/`:
   ```bash
   mkdir -p ~/.copilot/skills
   cp -r ~/Downloads/homebrew-copilot-skill-main/homebrew ~/.copilot/skills/homebrew
   ```

---

## Verify Installation

1. Open VS Code (or VS Code Insiders)
2. Open GitHub Copilot Chat
3. Ask a Homebrew question:
   ```
   How do I free up disk space used by Homebrew?
   ```
4. Copilot should provide a detailed, step-by-step answer using `brew cleanup`, `brew autoremove`, and `brew info --sizes`

Alternatively, explicitly invoke the skill:
```
Use the homebrew skill to show me the weekly maintenance workflow
```

---

## Updating the Skill

If you used Method 1 or 2, you can't pull directly from the cloned location. To update:

```bash
# Remove old version
rm -rf ~/.copilot/skills/homebrew

# Re-install (Method 1 or 2 from above)
```

Alternatively, if you cloned the full repo to a separate directory and symlinked:
```bash
cd /path/to/homebrew-copilot-skill && git pull
```

---

## Uninstallation

```bash
rm -rf ~/.copilot/skills/homebrew
```

That's it. No other cleanup needed.

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
