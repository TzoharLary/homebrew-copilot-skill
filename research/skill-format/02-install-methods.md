# Skill Installation Methods

**Source:** https://code.visualstudio.com/docs/copilot/customization/agent-skills and https://agentskills.io/  
**Date:** 2025-06-10

---

## Installation Locations (Official)

From the VS Code official documentation, agent skills are discovered from the following paths:

### Personal (User-Level) Locations
These apply to all workspaces open by this user.

| Path | Notes |
|------|-------|
| `~/.copilot/skills/<name>/` | Recommended for GitHub Copilot personal skills |
| `~/.claude/skills/<name>/` | For Claude-based agents |
| `~/.agents/skills/<name>/` | Generic path used by many agents |

### Project (Workspace-Level) Locations
These apply only when the workspace folder is open.

| Path | Notes |
|------|-------|
| `.github/skills/<name>/` | GitHub-centric projects |
| `.claude/skills/<name>/` | For Claude-enabled projects |
| `.agents/skills/<name>/` | Generic multi-agent path |

### Custom Locations
Users can configure additional paths in VS Code settings:
```json
"chat.agentSkillsLocations": [
  "~/my-custom-folder/skills"
]
```

---

## VS Code vs. VS Code Insiders — Same Path

**Key finding:** VS Code and VS Code Insiders use the **same personal skill locations** because they are based on the home directory (`~/`), not on the VS Code application directory.

Both `code` and `code-insiders` discover skills from:
- `~/.copilot/skills/<name>/SKILL.md`
- `~/.agents/skills/<name>/SKILL.md`

**No separate installs needed.** Install once in `~/.copilot/skills/` and it works for both.

The only difference: custom `chat.agentSkillsLocations` settings are stored per VS Code installation (in user settings), so if a user has different `settings.json` for regular vs. Insiders, they’d need to configure custom paths in both. But the default home-directory paths are shared.

---

## Installing This Skill — Recommended Methods

### Method 1: Direct Clone (Recommended)
```bash
# Clone into personal skills directory
git clone https://github.com/TzoharLary/homebrew-copilot-skill \
  ~/.copilot/skills/homebrew
```

### Method 2: Manual Copy
```bash
# Create the directory
mkdir -p ~/.copilot/skills/homebrew

# Copy SKILL.md and references
cp -r ~/Downloads/homebrew-copilot-skill/homebrew/* ~/.copilot/skills/homebrew/
```

### Method 3: Git Sparse Checkout (efficient)
```bash
mkdir -p ~/.copilot/skills/homebrew
cd ~/.copilot/skills/homebrew
git init
git sparse-checkout init --cone
git sparse-checkout set homebrew
git remote add origin https://github.com/TzoharLary/homebrew-copilot-skill
git pull origin main
mv homebrew/* . && rmdir homebrew
```

---

## Verifying Installation

From VS Code:
1. Open GitHub Copilot Chat
2. Type `@` — if the skill implements a participant, it will appear
3. Or ask: "Use the homebrew skill to help me upgrade my packages"
4. The skill will be auto-invoked when you ask Homebrew-related questions

To check VS Code discovered the skill:
1. Open VS Code Command Palette (`Cmd+Shift+P`)
2. Run `Preferences: Open User Settings (JSON)`
3. Check `chat.agentSkillsLocations` if you set custom paths

---

## Project Installation vs Personal Installation

### Personal (`~/.copilot/skills/homebrew/`)
- Available in every VS Code window
- Best for: tools you use in all projects
- Homebrew is a developer tool — **personal installation is appropriate**

### Project (`.github/skills/homebrew/`, e.g., inside a repo)
- Available only when that specific workspace folder is open
- Best for: project-specific knowledge (domain models, coding conventions, APIs)
- Not ideal for Homebrew since Homebrew is platform-wide, not project-specific

### Recommendation for This Skill
Use **personal installation** (`~/.copilot/skills/homebrew/`) for Homebrew.
