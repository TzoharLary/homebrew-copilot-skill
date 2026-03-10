<div align="center">

# 🍺 homebrew-copilot-skill

**Expert Homebrew knowledge for your AI coding assistant**

<br>

<a href="homebrew/README.md#github-copilot"><img src="https://img.shields.io/badge/GitHub_Copilot-install-0078d7?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Copilot"></a>
&nbsp;
<a href="homebrew/README.md#openai-codex"><img src="https://img.shields.io/badge/OpenAI_Codex-install-10a37f?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI Codex"></a>
&nbsp;
<a href="homebrew/README.md#claude-code"><img src="https://img.shields.io/badge/Claude_Code-install-d45f00?style=for-the-badge" alt="Claude Code"></a>

<br>

<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2e7d32?style=flat-square" alt="MIT License"></a>
&nbsp;
<a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-1.1.0-2e7d32?style=flat-square" alt="v1.1.0"></a>
&nbsp;
<a href="https://agentskills.io"><img src="https://img.shields.io/badge/agent_skills-compatible-2e7d32?style=flat-square" alt="Agent Skills compatible"></a>

<br><br>

[📦 Install](homebrew/README.md) · [💬 Examples](homebrew/EXAMPLES.md) · [🤝 Contribute](CONTRIBUTING.md) · [📋 Changelog](CHANGELOG.md)

</div>

&nbsp;

## What It Does

This skill gives your AI assistant **expert-level Homebrew knowledge** — maintenance order, disk cleanup, cask gotchas, platform paths, environment variables, and more. All sourced from [docs.brew.sh](https://docs.brew.sh). Install once — it loads automatically every time you ask a Homebrew question.

> [!TIP]
> **Try asking:** *"I switched to an M3 Mac. How do I migrate my Homebrew setup?"*
>
> Your AI will walk you through Brewfile export → clean ARM install at `/opt/homebrew` → selective restore — not a generic "just reinstall" answer.

&nbsp;

## What You Can Ask

🧹 *"How do I free up disk space used by Homebrew?"* — full cleanup workflow with `--dry-run` preview

🔄 *"What's the correct maintenance order?"* — `update → outdated → upgrade → cleanup → autoremove → doctor`

💻 *"Intel vs Apple Silicon — what's different?"* — paths, Rosetta, migration steps

🍺 *"Why doesn't `brew upgrade` update Chrome?"* — `--greedy` flag + macOS Ventura permissions

📦 *"Create a Brewfile to back up my packages"* — `brew bundle dump` + restore workflow

⚙️ *"What environment variables does Homebrew use?"* — full `HOMEBREW_*` reference

→ See [EXAMPLES.md](homebrew/EXAMPLES.md) for complete prompt / response pairs.

&nbsp;

## Quick Install

```bash
# GitHub Copilot (VS Code / VS Code Insiders)
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew && rm -rf /tmp/hbc
```

Using **Codex** or **Claude Code**? → [Install guide for all runtimes](homebrew/README.md)

&nbsp;

## What's Covered

<details>
<summary><strong>13 topics &nbsp;·&nbsp; 6 reference files</strong></summary>

&nbsp;

| Topic | Details |
|-------|----------|
| Platform identification | Intel `/usr/local` · Apple Silicon `/opt/homebrew` · Linux |
| Maintenance workflow | `update → upgrade → cleanup → autoremove → doctor` |
| Disk space | Assessment, cleanup, orphan removal, cache nuke |
| Cask management | `--greedy` · macOS Ventura App Management |
| Version control | `brew pin` / `brew unpin` · keg-only formulae |
| Dependencies | `brew deps` · `brew uses` · `brew leaves` |
| Brewfile | Backup + restore across machines |
| Services | `brew services` for launchd/systemd |
| Environment variables | All `HOMEBREW_*` vars with defaults |
| Troubleshooting | `brew doctor` · broken symlinks · renamed formulae |
| + 3 more | Commands, search, taps |

**Reference files** in `homebrew/references/`:
`commands.md` · `workflows.md` · `env-vars.md` · `disk-space.md` · `platform-guide.md` · `troubleshooting.md`

</details>

&nbsp;

## Repository Layout

```
homebrew/
├── SKILL.md        ← knowledge module (auto-loaded by your AI tool)
├── README.md       ← install guide for all runtimes
├── EXAMPLES.md     ← real prompt / response pairs
└── references/     ← 6 deep-dive guides
```

&nbsp;

<div align="center">
<sub>MIT License · Content sourced from <a href="https://docs.brew.sh">docs.brew.sh</a></sub>
</div>
