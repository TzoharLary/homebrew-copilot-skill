# Homebrew Research Conclusions

**Date:** 2025-06-10  
**Based on:** Files 01-05 in this research directory

The following conclusions directly inform the design of the skill content.

---

## Key Actionable Insights for Skill

### 1. Platform Awareness is Critical
The skill MUST handle three distinct platforms (macOS Intel, macOS Apple Silicon, Linux) transparently. Users often don't know which they're on. The skill should:
- Remind users to use `brew --prefix` or `brew config` to identify their platform
- Present platform-aware commands (e.g., cache paths differ by platform)
- Never assume a specific prefix

### 2. The Cleanup Misunderstanding is Widespread
The biggest confusion is: **auto-cleanup does NOT remove files newer than 120 days**. Users think Homebrew manages disk space aggressively, but it doesn't. The skill should:
- Explain the 120-day default threshold clearly
- Promote `brew cleanup --dry-run` as the first step
- Document the full cleanup workflow from assessment to nuclear options

### 3. The Update vs. Upgrade Distinction is Important
- `brew update` = update Homebrew recipe database (no packages changed)
- `brew upgrade` = actually install newer versions of your packages
- Users frequently confuse these. The skill should always clarify.

### 4. Cask Upgrade Has Gotchas
Three gotchas to cover:
- Apps with `auto_updates true` are excluded from `brew upgrade` by default
- Use `--greedy` to include auto-updating apps
- macOS Ventura+ requires "App Management" or "Full Disk Access" permission for in-place upgrades (otherwise apps lose Dock position/permissions)

### 5. The `brew autoremove` Command is Underused
Many users don't know that uninstalling a formula leaves its dependencies behind. `brew autoremove` recovers this space. The skill should surface it prominently.

### 6. The `brew leaves` Command is Powerful for Auditing
`brew leaves` shows formulae with no dependents. Combined with `brew info --sizes`, it helps users find large packages they may no longer need.

### 7. Brewfile is the Reproducibility Tool
For multi-machine setups or backups, `brew bundle dump` + `brew bundle install` is the official way to reproduce a Homebrew setup. The skill should cover this.

### 8. Services are Not Just `launchctl`
`brew services` wraps launchd and provides a much friendlier interface. Many developers don't know it exists.

### 9. Pinning Formulae Has Trade-offs
Pinned formulae may still be upgraded if they are dependencies of something else. Users need to be aware this is not absolute protection.

## What the Skill Body Should Cover

1. **Concept overview** — Homebrew terminology explained simply
2. **Platform detection** — how to know which platform you're on
3. **Package management workflow** — install, upgrade, uninstall (with cask coverage)
4. **Maintenance routine** — update → outdated → upgrade → cleanup → autoremove → doctor
5. **Disk space management** — the full workflow from assessment to reclamation
6. **Version management** — pin, unpin, multiple versions, tab
7. **Dependency management** — deps, uses, leaves, autoremove, missing
8. **Tap management** — add, remove, list taps
9. **Brewfile** — backup/restore/sync packages
10. **Services** — start/stop/list launchd services
11. **Environment variables** — most important ones with practical use cases
12. **Troubleshooting** — doctor, link, unlink, missing, migrate

## What Goes in References vs. SKILL.md Body

| Content | Location |
|---------|----------|
| Brief context + "how it works" overview | SKILL.md body |
| Complete command reference | `references/commands.md` |
| All env vars with defaults | `references/env-vars.md` |
| Platform-specific differences | `references/platform-guide.md` |
| Disk space workflow | `references/disk-space.md` |
| Maintenance workflows | `references/workflows.md` |
| Common problems | `references/troubleshooting.md` |
