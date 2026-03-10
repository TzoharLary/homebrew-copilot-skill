# Homebrew Skill — Install Guide

<div align="center">

**Choose your runtime below. Each section is self-contained.**

<br>

<a href="#github-copilot"><img src="https://img.shields.io/badge/GitHub_Copilot-0078d7?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Copilot"></a>&nbsp;
<a href="#openai-codex"><img src="https://img.shields.io/badge/OpenAI_Codex-10a37f?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI Codex"></a>&nbsp;
<a href="#claude-code"><img src="https://img.shields.io/badge/Claude_Code-d45f00?style=for-the-badge" alt="Claude Code"></a>

</div>

&nbsp;

## Runtime Support

| Runtime | Extension / App | Scope | Status |
| --- | --- | --- | --- |
| **GitHub Copilot** | `github.copilot-chat` | Global + Project-local | ✅ Supported |
| **OpenAI Codex** | `openai.chatgpt` | Global + Project-local *(prefer global)* | ✅ Supported |
| **Claude Code** | `claude.ai/code` | Global + Project-local *(prefer global)* | ✅ Supported |
| Google Cloud Code | `googlecloudtools.cloudcode` | — | ❌ Not supported¹ |

> ¹ Google Cloud Code is a GCP infrastructure tool. Its AI (Gemini Code Assist) doesn't implement the Agent Skills protocol.

&nbsp;

---

## GitHub Copilot

<details>
<summary><strong>📦 Install &nbsp;·&nbsp; ✅ Verify &nbsp;·&nbsp; 🔄 Update &nbsp;·&nbsp; 🗑️ Uninstall</strong></summary>

&nbsp;

The `github.copilot-chat` extension supports both global and project-local skills. VS Code and VS Code Insiders share the same skills directory — install once and it works in both.

### Install

**Global** *(recommended — Homebrew is a system-wide tool)*

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew
rm -rf /tmp/hbc
```

**Project-local** *(active only in this repository)*

```bash
mkdir -p .github/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew .github/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Restart VS Code → open Copilot Chat (`⌘⇧I` / `Ctrl+Shift+I`)
2. Ask: **"How do I free up disk space used by Homebrew?"**
3. **Expected:** a step-by-step answer mentioning `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`

> [!TIP]
> If those commands appear in the response → the skill is active.

### Update

```bash
rm -rf ~/.copilot/skills/homebrew     # global
# rm -rf .github/skills/homebrew    # project-local
# Re-run the install commands above
```

### Uninstall

```bash
rm -rf ~/.copilot/skills/homebrew     # global
rm -rf .github/skills/homebrew        # project-local (if installed)
```

</details>

&nbsp;

## OpenAI Codex

<details>
<summary><strong>📦 Install &nbsp;·&nbsp; ✅ Verify &nbsp;·&nbsp; 🔄 Update &nbsp;·&nbsp; 🗑️ Uninstall</strong></summary>

&nbsp;

The `openai.chatgpt` extension supports both global and project-local skills.

### Install

**Global** *(recommended — Homebrew is a system-wide tool)*

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.codex/skills/homebrew
rm -rf /tmp/hbc
```

**Project-local** *(active only in this repository)*

```bash
mkdir -p .codex/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew .codex/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Open the Codex chat panel in VS Code
2. Ask: **"How do I free up disk space used by Homebrew?"**
3. **Expected:** a step-by-step answer mentioning `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`

> [!TIP]
> If those commands appear in the response → the skill is active.

### Update

```bash
rm -rf ~/.codex/skills/homebrew     # global
# rm -rf .codex/skills/homebrew    # project-local
# Re-run the install commands above
```

### Uninstall

```bash
rm -rf ~/.codex/skills/homebrew     # global
rm -rf .codex/skills/homebrew       # project-local (if installed)
```

</details>

&nbsp;

## Claude Code

<details>
<summary><strong>📦 Install &nbsp;·&nbsp; ✅ Verify &nbsp;·&nbsp; 🔄 Update &nbsp;·&nbsp; 🗑️ Uninstall</strong></summary>

&nbsp;

Claude Code supports both global and project-local skills.

### Install

**Global** *(recommended — Homebrew is a system-wide tool)*

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.claude/skills/homebrew
rm -rf /tmp/hbc
```

**Project-local** *(active only in this repository)*

```bash
mkdir -p .claude/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew .claude/skills/homebrew
rm -rf /tmp/hbc
```

### Verify

1. Open Claude Code and start a new conversation
2. Ask: **"How do I free up disk space used by Homebrew?"**
3. **Expected:** a step-by-step answer mentioning `brew cleanup --dry-run`, `brew cleanup`, and `brew autoremove`

> [!TIP]
> If those commands appear in the response → the skill is active.

### Update

```bash
rm -rf ~/.claude/skills/homebrew    # global
# rm -rf .claude/skills/homebrew   # project-local
# Re-run the install commands above
```

### Uninstall

```bash
rm -rf ~/.claude/skills/homebrew    # global
rm -rf .claude/skills/homebrew      # project-local (if installed)
```

</details>

&nbsp;

---

## What's Inside

This skill covers 13 Homebrew topics across 7 source files:

- Installing, upgrading, and removing formulae and casks
- Correct maintenance order: `update → upgrade → cleanup → autoremove → doctor`
- Disk space: assessment, cleanup, orphan removal, cache nuke
- Platform differences: Intel `/usr/local` · Apple Silicon `/opt/homebrew` · Linux
- Cask gotchas: `--greedy` · macOS Ventura App Management
- Environment variables (`HOMEBREW_*`)
- Brewfile backup and restore
- `brew services` for daemon management
- Version pinning and keg-only formulae
- Tap management
- Troubleshooting: `brew doctor` · `brew link` · `brew missing`

&nbsp;

## Try It

After installing, try these prompts:

- *"How much disk space is Homebrew using and how do I free it up?"*
- *"I switched from an Intel Mac to M3. How do I migrate?"*
- *"How do I update apps like Chrome that Homebrew usually skips?"*
- *"Create a Brewfile I can use to restore my setup on a new machine"*

→ See [EXAMPLES.md](EXAMPLES.md) for complete prompt / response pairs.

&nbsp;

<div align="center">
<sub><a href="../README.md">← Back to main README</a></sub>
</div>
