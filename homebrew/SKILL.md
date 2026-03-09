---
name: homebrew
description: >-
  Expert Homebrew guidance for macOS and Linux.
  USE FOR: brew install, brew upgrade, brew cleanup, brew update,
  brew outdated, brew autoremove, brew doctor, brew bundle, brew services,
  brew pin, brew tap, brew leaves, brew deps, brew info --sizes,
  disk space reclamation, cache cleanup, HOMEBREW_* environment variables,
  maintenance routines, Brewfile backup and restore, platform differences
  between Intel Mac / Apple Silicon / Linux, keg-only formulae, tap management,
  troubleshooting broken installations, launchd services, auto-update behavior,
  cask upgrades, --greedy flag, --dry-run preview workflows,
  orphaned dependency removal, formula version pinning.
  DO NOT USE FOR: pip, npm, yarn, apt, yum, dnf, chocolatey, snap, flatpak.
argument-hint: "What do you want to do with Homebrew?"
user-invocable: true
version: "1.1.0"
maintainer: TzoharLary
---

# Homebrew Expert Skill

This skill provides expert guidance for the [Homebrew](https://brew.sh) package manager on macOS and Linux. All guidance is based on official Homebrew documentation (`docs.brew.sh`).

---

## Platform Identification

Homebrew installs to a different prefix depending on your platform:

| Platform | Prefix |
|----------|--------|
| macOS Apple Silicon (M1/M2/M3/M4) | `/opt/homebrew` |
| macOS Intel | `/usr/local` |
| Linux | `/home/linuxbrew/.linuxbrew` |

```bash
brew --prefix          # Shows your prefix (tells you which platform)
brew config            # Full system/Homebrew configuration info
```

> **Always use the default prefix** for your platform. Non-default prefixes require every formula to be compiled from source (slow, error-prone, unsupported).

For complete platform details, see `references/platform-guide.md`.

---

## Core Concepts

| Term | Meaning |
|------|---------|
| **formula** | A package definition that builds from source |
| **cask** | A package for pre-compiled macOS apps (e.g., Chrome, VS Code) |
| **keg** | One installed version of a formula, e.g. `$(brew --cellar)/git/2.44.0` |
| **Cellar** | Directory containing all installed formula versions |
| **Caskroom** | Directory containing all installed casks (macOS only) |
| **tap** | A Git repo of additional formulae/casks |
| **bottle** | A pre-built binary keg (faster than building from source) |
| **keg-only** | Installed but NOT symlinked into the prefix |

---

## Essential Daily Commands

```bash
# Install a formula
brew install git

# Install a macOS app (cask)
brew install --cask visual-studio-code

# Search for packages
brew search node                # Search by name
brew search --desc "database"   # Search by description

# Get info about a package
brew info git
brew info --cask firefox

# List installed packages
brew list                    # All formulae and casks
brew list --formula          # Only formulae
brew list --cask             # Only casks
brew list --versions         # With version numbers

# Remove a package
brew uninstall git
brew uninstall --cask firefox
brew uninstall --force git   # Remove ALL versions of git
```

For the complete command reference with all flags, see `references/commands.md`.

---

## Maintenance Workflow (The Correct Order)

```bash
brew update       # 1. UPDATE the recipe database (no packages changed yet)
brew outdated     # 2. CHECK what has newer versions available
brew upgrade      # 3. UPGRADE all outdated formulae
brew cleanup      # 4. CLEAN old versions and stale cache
brew autoremove   # 5. REMOVE orphaned dependencies
brew doctor       # 6. CHECK for any system problems
```

> **`update` vs `upgrade`:** `brew update` only refreshes Homebrew's formula database. `brew upgrade` actually installs newer package versions. You must run both.

For step-by-step daily/weekly routines, see `references/workflows.md`.

---

## Disk Space Management

Homebrew accumulates disk space in three main areas:
1. Old formula versions in `$(brew --cellar)/`
2. Downloaded archives in `~/Library/Caches/Homebrew` (macOS)
3. Orphaned dependencies no longer needed by anything

### Quick Disk Assessment
```bash
brew info --sizes --installed    # See size of each installed package
du -sh "$(brew --cache)"         # Size of download cache
brew list --multiple             # Formulae with multiple versions installed
```

### Cleanup Workflow (always dry-run first!)
```bash
brew cleanup --dry-run           # Preview what would be removed
brew cleanup                     # Remove old versions + cache >120 days old
brew autoremove --dry-run        # Preview orphan removal
brew autoremove                  # Remove orphaned dependencies
brew cleanup --prune=all         # Also delete entire download cache
```

> **Auto-cleanup does NOT aggressively clean.** It only removes cached files older than 120 days (`HOMEBREW_CLEANUP_MAX_AGE_DAYS=120`). Manual `brew cleanup` removes all old formula versions.

For the complete disk management workflow, see `references/disk-space.md`.

---

## Managing Casks

```bash
brew upgrade               # Upgrades casks (except auto-updating apps)
brew upgrade --greedy      # Also upgrades apps that self-update (Chrome, etc.)
brew outdated --greedy     # Check all outdated including auto-updating casks
```

> Apps like Chrome, Slack, VS Code have `auto_updates true` in their cask definition. They are excluded from `brew upgrade` by default. Use `--greedy` to include them.

> **macOS Ventura+ note:** Without "App Management" or "Full Disk Access" permission, in-place cask upgrades are replaced by uninstall+reinstall (may lose Dock position and app permissions). Grant the permission in System Settings > Privacy & Security.

---

## Version Control (pin/unpin)

```bash
brew pin git               # Prevent git from being upgraded
brew unpin git             # Allow upgrades again
brew list --pinned         # Show all pinned formulae
```

> **Warning:** Pinned formulae may still be upgraded if they are a required dependency of another formula you're upgrading. Pinning is not absolute.

```bash
# Protect a dependency from autoremove:
brew tab --installed-on-request wget    # Mark as manually installed
```

---

## Dependency Management

```bash
brew deps git                    # List what git depends on
brew deps --tree git             # Show dependency tree
brew uses --installed git        # Show what currently installed formulae use git
brew leaves                      # Formulae with no dependents (installed for their own sake)
brew leaves -r                   # Only manually-installed leaves
```

For reverse-deps and orphan management, see `references/commands.md`.

---

## Tap Management

```bash
brew tap                         # List installed taps
brew tap user/repo               # Add a tap from GitHub
brew untap user/repo             # Remove a tap
brew tap-info --installed        # Show info about all taps
```

---

## Brewfile (Backup and Restore)

```bash
brew bundle dump                  # Save all installedformula/casks to ./Brewfile
brew bundle dump --global         # Save to ~/.homebrew/Brewfile
brew bundle dump --force --describe # Overwrite + add description comments
brew bundle install               # Install everything in Brewfile
brew bundle check                 # Check all deps are satisfied (exit 0 if OK)
brew bundle cleanup               # View packages NOT in Brewfile
brew bundle cleanup -f            # Remove packages NOT in Brewfile
```

For new machine setup workflow with Brewfile, see `references/workflows.md`.

---

## Services (launchd)

```bash
brew services list                # List all services and their status
brew services start postgresql    # Start + register to start at login
brew services stop postgresql     # Stop + unregister from auto-start
brew services run postgresql      # Start for this session only (no auto-start)
brew services restart postgresql  # Stop and start
brew services cleanup             # Remove unused service registrations
```

---

## Key Environment Variables

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_AUTO_UPDATE=1` | not set | Skip auto-update before each command |
| `HOMEBREW_NO_INSTALL_CLEANUP=1` | not set | Disable auto-cleanup after install/upgrade |
| `HOMEBREW_CLEANUP_MAX_AGE_DAYS` | `120` | Age threshold for cache cleanup |
| `HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS` | `30` | Interval for full cleanup of all formulae |
| `HOMEBREW_NO_CLEANUP_FORMULAE` | not set | Comma-separated formulae to exclude from cleanup |
| `HOMEBREW_UPGRADE_GREEDY=1` | not set | Always include auto-updating casks in upgrades |
| `HOMEBREW_NO_ANALYTICS=1` | not set | Disable anonymous usage analytics |
| `HOMEBREW_GITHUB_API_TOKEN` | not set | GitHub token for higher API rate limits |

For the complete reference with all variables and their defaults, see `references/env-vars.md`.

---

## Troubleshooting

```bash
brew doctor              # Check for common problems (always run this first)
brew missing             # Check for missing dependencies
brew link <formula>      # Re-create symlinks for a formula
brew link -f <formula>   # Force-link a keg-only formula
brew unlink <formula>    # Remove symlinks (temporarily disable)
brew reinstall <formula> # Uninstall and reinstall (fixes broken installs)
brew migrate <formula>   # Handle renamed formulae
```

> If GUI apps can't find Homebrew binaries, run once:
> `sudo launchctl config user path "$(brew --prefix)/bin:${PATH}"`
> Then restart or log out and back in.

For detailed troubleshooting patterns, see `references/troubleshooting.md`.
