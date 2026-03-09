# Homebrew Disk Space Management

**Source:** https://docs.brew.sh/Manpage and https://docs.brew.sh/FAQ  
**Date:** 2025-06-10

---

## Understanding Where Disk Space Goes

Homebrew uses disk space in several distinct areas:

| Location | What is stored | How to check |
|----------|---------------|--------------|
| `$(brew --cellar)/` | All installed formula versions | `du -sh $(brew --cellar)` |
| `$(brew --prefix)/Caskroom/` | All installed cask versions | `du -sh $(brew --prefix)/Caskroom` |
| `~/Library/Caches/Homebrew/` | Downloaded bottles and source archives | `du -sh "$(brew --cache)"` |
| `~/Library/Logs/Homebrew/` | Build and install logs | Usually small |

### Finding the Largest Packages

From the `info --sizes` option in the official manpage:
```bash
brew info --sizes            # Show size of all installed formulae
brew info --sizes --cask     # Show size of installed casks
brew info --sizes --installed # Show only installed packages with sizes
```

---

## The Cleanup Command — Official Behavior

From official manpage:

> " Remove stale lock files and outdated downloads for all formulae and casks, and remove old versions of installed formulae. [...] Removes all downloads more than 120 days old."

### `brew cleanup` (basic)
What it removes:
1. Old formula versions (any version that is NOT the currently active installed version)
2. Cached downloads older than `HOMEBREW_CLEANUP_MAX_AGE_DAYS` (default: 120 days)
3. Stale lock files

What it keeps:
1. The currently installed version of each formula
2. Cached downloads newer than 120 days

### `brew cleanup --dry-run` ⭐ Always Use First!
Preview exactly what would be removed WITHOUT actually removing anything.

```bash
brew cleanup --dry-run
# Shows:
# Removing: /usr/local/Cellar/git/2.39.0... (5.6MB)
# Removing: /usr/local/Cellar/node/18.12.0... (152MB)
# This operation would free approximately 234MB of disk space.
```

### `brew cleanup --prune=<days>`
Remove cache files older than N days (instead of the default 120):
```bash
brew cleanup --prune=30   # Remove cache files older than 30 days
brew cleanup --prune=7    # Aggressive: remove cache files older than 7 days
brew cleanup --prune=0    # Remove ALL cache files (same as --prune=all)
```

### `brew cleanup --prune=all`
Remove the **entire cache** — all download archives including recent ones.
- ⚠️ Downloads will need to re-download next time if you reinstall or reinstall
- Downloaded binaries for currently installed formulae are NOT deleted

### `brew cleanup -s` (scrub)
Scrub the cache, including downloads for the latest versions:
- Note: downloads for **installed** formulae are still NOT deleted
- To also delete those: `rm -rf "$(brew --cache)"` (nuclear option)

---

## Orphaned Dependencies: `brew autoremove`

From official manpage:
> "Uninstall formulae that were only installed as a dependency of another formula and are now no longer needed."

```bash
brew autoremove --dry-run    # Preview what would be removed
brew autoremove              # Actually remove orphans
```

**When to use:** After uninstalling formulae. Each formula you remove may leave behind its dependencies, which `autoremove` will clean up.

**Protection:** Use `brew tab --installed-on-request <formula>` to mark a dependency as manually installed, protecting it from autoremove.

---

## Keeping Old Versions

From FAQ:
> "To disable automatic `brew cleanup`: `export HOMEBREW_NO_INSTALL_CLEANUP=1`"
> "To disable automatic `brew cleanup` only for formulae foo and bar: `export HOMEBREW_NO_CLEANUP_FORMULAE=foo,bar`"

Pinning a version:
```bash
brew pin <formula>       # Prevent upgrades
brew unpin <formula>     # Allow upgrades again
brew list --pinned       # See what's pinned
```

---

## Complete Disk Reclamation Workflow

The recommended sequence from safest to most aggressive:

### Step 1: Assess (no changes)
```bash
brew info --sizes --installed     # See largest packages
du -sh "$(brew --cache)"          # Check cache size
brew list --versions              # See formulae with multiple versions
brew list --multiple              # Show ONLY formulae with multiple versions
```

### Step 2: Preview cleanup (no changes)
```bash
brew cleanup --dry-run
brew autoremove --dry-run
```

### Step 3: Standard cleanup
```bash
brew cleanup          # Remove old versions + old cache files
brew autoremove       # Remove orphaned dependencies
```

### Step 4: Deep cache cleanup (if needed)
```bash
brew cleanup --prune=all    # Remove entire download cache
```

### Step 5: Nuclear option (if needed)
```bash
rm -rf "$(brew --cache)"    # Delete everything in the cache including installed formula downloads
brew cleanup --prune-prefix # Clean orphaned symlinks from prefix
```

### Step 6: Force-remove all versions of a specific formula
```bash
brew uninstall --force <formula>   # Remove ALL versions of a formula
```

---

## Preventing Space Accumulation

### Aggressive auto-cleanup settings
```bash
# In ~/.homebrew/brew.env or shell profile:
HOMEBREW_CLEANUP_MAX_AGE_DAYS=7       # Clean files older than 7 days (not 120)
HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS=7 # Full cleanup every 7 days (not 30)
```

### Regular maintenance routine
```bash
# Weekly maintenance script:
brew update
brew upgrade
brew cleanup
brew autoremove
brew doctor
```
