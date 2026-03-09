# homebrew-copilot-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-quality [GitHub Copilot Agent Skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills) for [Homebrew](https://brew.sh) — the package manager for macOS and Linux. Once installed, Copilot will automatically use expert Homebrew knowledge when answering your questions.

---

## What It Does

This skill teaches GitHub Copilot comprehensive Homebrew knowledge, including:

- **Package management** — installing, upgrading, and removing formulae and casks
- **Correct maintenance order** — `update` → `outdated` → `upgrade` → `cleanup` → `autoremove` → `doctor`
- **Disk space management** — assessment, cleanup workflows, cache nuking, orphan removal
- **Platform awareness** — Intel Mac (`/usr/local`) vs Apple Silicon (`/opt/homebrew`) vs Linux
- **Cask upgrade gotchas** — `--greedy` flag, macOS Ventura App Management permissions
- **Environment variables** — all `HOMEBREW_*` variables with defaults and use cases
- **Brewfile** — backup and restore your Homebrew setup across machines
- **Services** — `brew services` for managing launchd/systemd processes
- **Troubleshooting** — `brew doctor`, broken symlinks, missing deps, renamed formulae

All content is based exclusively on official documentation from [docs.brew.sh](https://docs.brew.sh).

---

## Quick Install

> VS Code and VS Code Insiders share the same skills directory. Install once, works in both.

```bash
mkdir -p ~/.copilot/skills
git clone https://github.com/TzoharLary/homebrew-copilot-skill /tmp/hbc
cp -r /tmp/hbc/homebrew ~/.copilot/skills/homebrew
rm -rf /tmp/hbc
```

Then ask Copilot:
```
How do I free up disk space used by Homebrew?
```

Also works with Codex and Claude Code — see [homebrew/README.md](homebrew/README.md) for all runtime install paths.

---

## Skill Structure

```
homebrew/
├── SKILL.md                     ← core skill (auto-loaded by Copilot)
├── README.md                    ← full install guide
├── EXAMPLES.md                  ← example prompts and responses
└── references/
    ├── commands.md              ← every command with every option
    ├── workflows.md             ← step-by-step maintenance recipes
    ├── env-vars.md              ← all HOMEBREW_* variables
    ├── disk-space.md            ← disk space management
    ├── platform-guide.md        ← Intel / Apple Silicon / Linux differences
    └── troubleshooting.md       ← common problems and fixes
```

---

## Research Branch

All implementation decisions are documented in the [`research/skill-design`](https://github.com/TzoharLary/homebrew-copilot-skill/tree/research/skill-design) branch:

- Official Homebrew manpage analysis
- Platform difference research
- Environment variable reference
- Agent Skills format specification
- Runtime compatibility research (GitHub Copilot, Codex, Claude Code)
- Implementation plan reviewed 5 times before execution

---

## License

[MIT](LICENSE)
