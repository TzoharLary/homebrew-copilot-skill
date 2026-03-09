# Homebrew Commands Deep Dive

**Source:** https://docs.brew.sh/Manpage  
**Date:** 2025-06-10

This covers every essential user-facing command with key options and use cases.

---

## Core Package Management

### `brew install <formula|cask>`
- Install a formula or cask
- `--cask` — treat as cask
- `-n, --dry-run` — show what would be installed without doing it
- `--ask` — ask for confirmation before installing (shows download sizes and dependencies)
- `-s, --build-from-source` — compile from source even if a bottle is available
- `--force-bottle` — use a bottle even if normally skipped
- `--ignore-dependencies` — ⚠️ unsupported, causes issues
- `--only-dependencies` — install only dependencies, not the formula itself
- After install: auto-triggers `brew cleanup` for installed formula (unless `HOMEBREW_NO_INSTALL_CLEANUP`)
- If formula already installed but outdated: upgrades it (unless `HOMEBREW_NO_INSTALL_UPGRADE`)

### `brew uninstall <formula|cask>` (aliases: `remove`, `rm`)
- Uninstall a formula or cask
- `-f, --force` — delete ALL installed versions; ignore errors
- `--zap` — remove ALL files associated with a cask (may remove shared files)
- `--ignore-dependencies` — don't fail if formula is a dependency of another

### `brew reinstall <formula|cask>`
- Uninstall then reinstall using the same original options
- Useful when a package is broken or symlinks are wrong

### `brew upgrade [formula|cask]`
- Upgrade all outdated formulae and casks, or specific ones
- `-n, --dry-run` — preview what would be upgraded
- `-g, --greedy` — also upgrade casks with `auto_updates true` or `version :latest`
- `--greedy-latest` — upgrade casks with `version :latest`
- `--greedy-auto-updates` — upgrade casks with `auto_updates true`
- `--formula` / `--cask` — filter by type
- After upgrade: triggers cleanup (unless `HOMEBREW_NO_INSTALL_CLEANUP`)

---

## Information and Discovery

### `brew list` (alias: `ls`)
- List all installed formulae and casks
- `--formula` — only formulae
- `--cask` — only casks
- `--versions` — show version numbers
- `--multiple` — only show formulae with multiple versions installed
- `--pinned` — only show pinned formulae
- `-1` — one entry per line

### `brew outdated [formula|cask]`
- Show installed formulae/casks with newer versions available
- `-q, --quiet` — only names, no version info
- `-v, --verbose` — include version details
- `-g, --greedy` — include casks with `auto_updates true` or `version :latest`
- `--formula` / `--cask` — filter by type

### `brew info <formula|cask>` (alias: `abv`)
- Display info about a formula/cask
- `--installed` — show info for all installed
- `--sizes` — **show disk usage per package** (great for finding large packages)
- `--json` — output JSON (version `v2` covers both formulae and casks)

### `brew search <text>` (alias: `-S`)
- Search formula/cask names; `/regex/` for regex search
- `--formula` / `--cask` — filter by type
- `--desc` — search descriptions too

### `brew desc <formula|cask>`
- Show name and one-line description
- `-s, --search` — search names AND descriptions for text

### `brew leaves`
- List installed formulae that are NOT dependencies of anything else
- `-r, --installed-on-request` — only manually installed leaves
- `-p, --installed-as-dependency` — only dependency-leaves
- **Use case:** find what you explicitly want vs. what came along

### `brew deps <formula|cask>`
- Show dependencies of a formula
- `--tree` — show as a dependency tree
- `--installed` — limit to currently installed deps only
- `--missing` — show only missing dependencies
- `--for-each` — one formula per line format

### `brew uses <formula>`
- Show what formulae depend on this formula (reverse deps)
- `--installed` — only show installed dependents
- `--recursive` — follow dependency chain

---

## Maintenance

### `brew update` (alias: `up`)
- Fetch the newest version of Homebrew and all formulae from GitHub using git
- `--auto-update` — used internally for the pre-command auto-update
- `-f, --force` — always do a full update check
- **Does NOT upgrade your installed packages** — only updates the recipe database

### `brew cleanup [formula|cask]`
- Remove stale lock files, outdated downloads, and old formula versions
- `-n, --dry-run` — **preview only, remove nothing** (always use first!)
- `--prune=<days>` — remove cache files older than N days
- `--prune=all` — remove the entire cache (including downloads for latest versions)
- `-s, --scrub` — scrub cache; removes even downloads of latest versions (but NOT if installed)
  - To delete even installed formula downloads: `rm -rf "$(brew --cache)"`
- `--prune-prefix` — only prune prefix symlinks and directories
- Default: removes all old versions + downloads older than 120 days

### `brew autoremove`
- Remove formulae that were only installed as dependencies and are no longer needed
- `-n, --dry-run` — preview only
- **Use after upgrading or uninstalling to reclaim space**

### `brew doctor` (alias: `dr`)
- Check the system for potential problems
- `--list-checks` — list all available checks
- Non-zero exit code if problems found
- **Always run before reporting issues**

### `brew missing [formula]`
- Check for missing dependencies
- Useful when packages are broken after a partial install or system change

---

## Version Control

### `brew pin <formula>`
- Prevent a formula from being upgraded by `brew upgrade`
- Note: pinned formulae may still be upgraded if they are a dependency of something else

### `brew unpin <formula>`
- Allow a previously pinned formula to be upgraded

### `brew tab <formula>`
- Control whether `brew autoremove` can remove a formula
- `--installed-on-request` — mark as manually installed (prevents autoremove)
- `--no-installed-on-request` — allow autoremove to remove it

---

## Tap Management

### `brew tap [user/repo]`
- With no args: list all installed taps
- `brew tap user/repo` — add a tap from GitHub (clones `https://github.com/user/homebrew-repo`)
- `brew tap user/repo https://custom-url` — add a tap from a custom URL

### `brew untap [tap]`
- Remove a tap
- `-f, --force` — untap even if formulae from this tap are installed

### `brew tap-info [tap]`
- Show details about installed taps
- `--installed` — show info for all installed taps

---

## Brewfile / Bundle

### `brew bundle dump`
- Write all installed casks/formulae/taps to a `Brewfile` in the current directory
- `-g, --global` — write to `~/.homebrew/Brewfile` or `~/.Brewfile`
- `-f, --force` — overwrite existing Brewfile
- `--describe` — add description comments
- `--no-vscode` — exclude VS Code extensions

### `brew bundle install`
- Install everything from a `Brewfile`
- `--upgrade` — also upgrade installed packages
- `--cleanup` — remove anything not in Brewfile

### `brew bundle cleanup`
- Uninstall anything not in the Brewfile
- `-f, --force` — actually perform cleanup (otherwise just shows what would be removed)

### `brew bundle check`
- Check if all Brewfile dependencies are satisfied (exits 0 if all installed)

---

## Services

### `brew services list`
- List all running and registered services

### `brew services start <formula>`
- Start the service AND register it to start at login (or boot)
- Requires `sudo` for system-wide services

### `brew services stop <formula>`
- Stop the service AND unregister from auto-start

### `brew services run <formula>`
- Start the service for current session only (does NOT register for auto-start)

### `brew services restart <formula>`
- Stop and start, maintaining registration

### `brew services cleanup`
- Remove all unused service registrations

---

## Utility Commands

### `brew --prefix [formula]`
- Show Homebrew's install path
- With formula arg: show where that formula would be installed

### `brew --cache [formula]`
- Show the download cache path
- With formula arg: show the specific cache file for that formula

### `brew --cellar [formula]`
- Show the Cellar path (`$(brew --prefix)/Cellar`)

### `brew config` (alias: `--config`)
- Show Homebrew and system configuration (macOS version, CPU arch, prefix, etc.)
- **Include this info when filing a bug report**

### `brew shellenv`
- Print export statements to add Homebrew to `$PATH`, `$MANPATH`, `$INFOPATH`
- Typically used in `.zprofile` or `.bash_profile`: `eval "$(brew shellenv)"`

### `brew link <formula>` (alias: `ln`)
- Symlink installed formula files into the Homebrew prefix
- `-f, --force` — allow keg-only formulae to be linked

### `brew unlink <formula>`
- Remove symlinks for a formula
- Useful for temporarily disabling: `brew unlink formula && commands && brew link formula`

### `brew migrate <formula|cask>`
- Migrate renamed packages to their new names

### `brew home [formula|cask]`
- Open the formula/cask's homepage in a browser
