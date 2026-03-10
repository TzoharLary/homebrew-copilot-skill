<div align="center">

# 🍺 homebrew-copilot-skill

**Expert Homebrew knowledge, automatically loaded into your AI assistant**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-brightgreen.svg)](https://agentskills.io/)

[![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-supported-0078d7?logo=github&logoColor=white)](homebrew/README.md#github-copilot)
[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-d45f00)](homebrew/README.md#claude-code)
[![OpenAI Codex](https://img.shields.io/badge/OpenAI_Codex-supported-10a37f?logo=openai&logoColor=white)](homebrew/README.md#codex)

[📦 Install](homebrew/README.md) · [💬 Examples](homebrew/EXAMPLES.md) · [🤝 Contribute](CONTRIBUTING.md) · [📋 Changelog](CHANGELOG.md)

</div>

---

## The Problem

Without this skill, your AI assistant gives generic — sometimes wrong — Homebrew advice:

> ❌ `brew update && brew upgrade` — *skips cleanup, autoremove, and doctor; leaves disk full over time*
> ❌ `brew upgrade` silently **skips Chrome, Slack, and VS Code** because they self-update
> ❌ Gives Intel paths (`/usr/local`) to someone on Apple Silicon (`/opt/homebrew`)

## The Fix

This skill teaches your AI assistant accurate Homebrew expertise sourced directly from [docs.brew.sh](https://docs.brew.sh). Install once — it loads automatically on every Homebrew-related question.

> [!NOTE]
> An **Agent Skill** is a knowledge module that AI tools (Copilot, Claude Code, Codex) auto-load as context. No prompts needed after install — it works silently in the background.

---

## What You Can Ask

| 💬 Prompt | 🎯 What You Get |
|-----------|----------------|
| *"How do I free up disk space?"* | Cleanup workflow with `--dry-run` preview, `brew cleanup`, `brew autoremove` |
| *"What's the correct maintenance order?"* | `update → outdated → upgrade → cleanup → autoremove → doctor` |
| *"I just switched to an M3 Mac — how do I migrate?"* | Brewfile export + ARM Homebrew install + restore steps |
| *"Why doesn't `brew upgrade` update Chrome or Slack?"* | `--greedy` flag explained + macOS Ventura App Management fix |
| *"Create a Brewfile to back up my packages"* | Full `brew bundle dump` and restore workflow |

→ See [EXAMPLES.md](homebrew/EXAMPLES.md) for complete prompt/response pairs.

---

## Quick Install

**GitHub Copilot** (VS Code / VS Code Insiders):

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew && rm -rf /tmp/hbc
```

Then restart VS Code, open Copilot Chat, and ask: *"How do I free up disk space used by Homebrew?"*

Using **Claude Code** or **OpenAI Codex**? → [Full install guide for all runtimes](homebrew/README.md)

---

## What's Covered

<details>
<summary><b>13 topics in SKILL.md + 6 deep-reference files — click to expand</b></summary>
<br>

**Core topics (`homebrew/SKILL.md`):**

| Topic | Details |
|-------|---------|
| Platform identification | Intel `/usr/local` · Apple Silicon `/opt/homebrew` · Linux |
| Maintenance workflow | `update → upgrade → cleanup → autoremove → doctor` — in the right order |
| Disk space management | Assessment, cleanup, orphan removal, full cache nuke |
| Cask management | `--greedy` flag · macOS Ventura App Management permissions |
| Version control | `brew pin` / `brew unpin` · keg-only formulae |
| Dependency management | `brew deps`, `brew uses`, `brew leaves` |
| Brewfile | Backup and restore your full setup across machines |
| Services | `brew services` for launchd/systemd daemon management |
| Environment variables | All `HOMEBREW_*` vars with defaults and use cases |
| Troubleshooting | `brew doctor`, broken symlinks, renamed formulae |
| + 3 more | Commands, search, taps |

**Deep-reference files (`homebrew/references/`):**

| File | Contents |
|------|----------|
| `commands.md` | Every command with every option |
| `workflows.md` | Step-by-step maintenance recipes |
| `env-vars.md` | All `HOMEBREW_*` variables with defaults |
| `disk-space.md` | Complete disk space management guide |
| `platform-guide.md` | Intel / Apple Silicon / Linux differences |
| `troubleshooting.md` | Common problems and fixes |

</details>

---

## Repository Layout

```
homebrew/
├── SKILL.md        ← knowledge module (auto-loaded by your AI tool)
├── README.md       ← full install guide for all runtimes
├── EXAMPLES.md     ← real prompt/response examples
└── references/     ← deep-dive guides by topic (6 files)
```

---

## License

[MIT](LICENSE) — Content based on official [Homebrew documentation](https://docs.brew.sh).
