# Homebrew Official Docs Analysis

**Source:** https://docs.brew.sh/Manpage and https://docs.brew.sh/FAQ  
**Date:** 2025-06-10

---

## 1. Terminology (from official Manpage)

Understanding Homebrew's vocabulary is essential for writing accurate skill instructions.

| Term | Definition |
|------|------------|
| **formula** | A Homebrew package definition that builds from upstream sources |
| **cask** | A Homebrew package definition for pre-compiled binaries (macOS apps) |
| **keg** | Installation destination for a given formula version, e.g. `/opt/homebrew/Cellar/foo/0.1` |
| **rack** | Directory containing one or more versioned kegs, e.g. `/opt/homebrew/Cellar/foo` |
| **Cellar** | Directory containing all named racks, e.g. `/opt/homebrew/Cellar` |
| **Caskroom** | Directory containing all named casks, e.g. `/opt/homebrew/Caskroom` |
| **tap** | A directory (usually a Git repository) of formulae, casks, and/or external commands |
| **bottle** | A pre-built binary keg distributed instead of building from source |
| **keg-only** | A formula installed in the Cellar but NOT symlinked into the prefix |
| **opt prefix** | Symlink to the active version of a keg, e.g. `/opt/homebrew/opt/foo` |
| **prefix** | The path where Homebrew is installed |

## 2. Key Directory Structure

Based on the official `--prefix` documentation and FAQ:

```
$(brew --prefix)/              # e.g. /opt/homebrew (Apple Silicon), /usr/local (Intel)
├── bin/                       # Symlinks to installed binaries
├── lib/                       # Symlinks to installed libraries
├── Cellar/                    # All installed formulae (kegs)
│   └── <formula>/
│       └── <version>/         # The actual files for one version
├── Caskroom/                  # All installed casks
│   └── <cask>/
│       └── <version>/
├── opt/                       # Symlinks to active versions
│   └── <formula> -> Cellar/<formula>/<version>
└── etc/homebrew/brew.env      # Prefix-level environment file
```

System-wide env file: `/etc/homebrew/brew.env`  
User-level env file: `$XDG_CONFIG_HOME/homebrew/brew.env` or `~/.homebrew/brew.env`  
Cache: `~/Library/Caches/Homebrew` (macOS) | `$XDG_CACHE_HOME/Homebrew` (Linux)  
Logs: `~/Library/Logs/Homebrew` (macOS) | `$XDG_CACHE_HOME/Homebrew/Logs` (Linux)

## 3. The Auto-Cleanup Lifecycle

This is a critical and often misunderstood behavior from the official manpage:

**From `install` docs:**
> "Unless `$HOMEBREW_NO_INSTALL_CLEANUP` is set, `brew cleanup` will then be run for the installed formulae or, every 30 days, for all formulae."

**From `cleanup` docs:**
> "Remove stale lock files and outdated downloads for all formulae and casks, and remove old versions of installed formulae. If arguments are specified, only do this for the given formulae and casks. **Removes all downloads more than 120 days old.** This can be adjusted with `$HOMEBREW_CLEANUP_MAX_AGE_DAYS`."

**Key insight:** Auto-cleanup (triggered by install/upgrade/reinstall) only removes cached downloads older than 120 days, governed by `HOMEBREW_CLEANUP_MAX_AGE_DAYS`. Manual `brew cleanup` without `--prune` removes all old formula *versions* and cached downloads older than 120 days. This is why multiple old versions can accumulate!

**From FAQ:**
> "Homebrew automatically uninstalls old versions of each formula that is upgraded with `brew upgrade`, and periodically performs additional cleanup every 30 days."

`HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS=30` triggers a full cleanup of ALL formulae every 30 days. Without this, only the specific formula just installed/upgraded gets cleaned.

## 4. Multi-Version Behavior

From FAQ:
> "When automatic `brew cleanup` is disabled, if you uninstall a formula, it will only remove the latest version you have installed. It will not remove all versions of the formula that you may have installed in the past."

To force-remove all versions: `brew uninstall --force <formula>`

## 5. The No-Sudo Design

From FAQ: Homebrew refuses to work with sudo. The macOS sandbox prevents build scripts from modifying files outside the prefix, which doesn't work as root. Designed for single-user use.

## 6. Default Ownership and Permissions

From FAQ:
- **macOS:** subdirectories/files use `admin` group, permissions `0755`
- **Linux:** current user and group, permissions `0755`  
- Only the installing user can modify/replace files; all users can read and execute
