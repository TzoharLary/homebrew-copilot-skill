# Homebrew Complete Command Reference

All commands from the official Homebrew manpage (`docs.brew.sh/Manpage`).

---

## Core Package Management

### `brew install <formula|cask>`
| Option | Effect |
|--------|--------|
| `--cask` | Treat argument as cask |
| `-n, --dry-run` | Show what would be installed without doing it |
| `--ask` | Ask for confirmation (shows download sizes) |
| `-s, --build-from-source` | Compile from source even if bottle available |
| `--force-bottle` | Use a bottle even if normally skipped |
| `--only-dependencies` | Install only dependencies, not the formula itself |
| `--ignore-dependencies` | ⚠️ Unsupported flag — causes issues |

*After install:* Auto-triggers `brew cleanup` for the installed formula unless `HOMEBREW_NO_INSTALL_CLEANUP` is set. If formula is already installed but outdated, upgrades it unless `HOMEBREW_NO_INSTALL_UPGRADE` is set.

### `brew uninstall <formula|cask>` *(aliases: `remove`, `rm`)*
| Option | Effect |
|--------|--------|
| `-f, --force` | Delete ALL installed versions; ignore errors |
| `--zap` | Remove ALL files associated with cask (may remove shared files) |
| `--ignore-dependencies` | Don't fail if this is a dependency of another formula |

### `brew reinstall <formula|cask>`
Uninstall then reinstall using the same original options. Useful when symlinks are broken.

### `brew upgrade [formula|cask]`
| Option | Effect |
|--------|--------|
| `-n, --dry-run` | Preview what would be upgraded |
| `-g, --greedy` | Also upgrade casks with `auto_updates true` or `version :latest` |
| `--greedy-latest` | Upgrade casks with `version :latest` only |
| `--greedy-auto-updates` | Upgrade casks with `auto_updates true` only |
| `--formula` / `--cask` | Filter by type |

---

## Discovery and Information

### `brew list` *(alias: `ls`)*
| Option | Effect |
|--------|--------|
| `--formula` / `--cask` | Filter by type |
| `--versions` | Show version numbers |
| `--multiple` | Only formulae with multiple versions installed |
| `--pinned` | Only pinned formulae |
| `-1` | One entry per line |

### `brew outdated [formula|cask]`
| Option | Effect |
|--------|--------|
| `-q, --quiet` | Names only, no version info |
| `-v, --verbose` | Include version details |
| `-g, --greedy` | Include auto-updating casks |
| `--formula` / `--cask` | Filter by type |

### `brew info <formula|cask>` *(alias: `abv`)*
| Option | Effect |
|--------|--------|
| `--sizes` | Show disk usage per package |
| `--installed` | Show info for all installed packages |
| `--json=v2` | JSON output covering formulae and casks |

### `brew search <text>` *(alias: `-S`)*
| Option | Effect |
|--------|--------|
| `--formula` / `--cask` | Filter by type |
| `--desc` | Search descriptions too |
| `/regex/` syntax | Use regex search, e.g. `brew search /^py/` |

### `brew leaves`
| Option | Effect |
|--------|--------|
| `-r, --installed-on-request` | Only manually installed packages |
| `-p, --installed-as-dependency` | Only packages installed as dependency |

### `brew deps <formula|cask>`
| Option | Effect |
|--------|--------|
| `--tree` | Show as dependency tree |
| `--installed` | Limit to currently installed deps |
| `--missing` | Show only missing dependencies |
| `--for-each` | One formula per line format |

### `brew uses <formula>`
| Option | Effect |
|--------|--------|
| `--installed` | Only show installed dependents |
| `--recursive` | Follow full dependency chain |

---

## Maintenance

### `brew update` *(alias: `up`)*
Update Homebrew's formula database. Does NOT upgrade package versions.

| Option | Effect |
|--------|--------|
| `-f, --force` | Always do a full update check |

### `brew cleanup [formula|cask]`
Remove old versions and stale cache files. Default removes files >120 days old.

| Option | Effect |
|--------|--------|
| `-n, --dry-run` | **Preview only — always run this first** |
| `--prune=<days>` | Remove cache files older than N days |
| `--prune=all` | Remove the entire download cache |
| `-s, --scrub` | Also remove downloads of latest versions (not installed) |
| `--prune-prefix` | Only clean orphaned symlinks from prefix |

### `brew autoremove`
Remove formulae installed only as dependencies that nothing needs anymore.

| Option | Effect |
|--------|--------|
| `-n, --dry-run` | Preview only |

### `brew doctor` *(alias: `dr`)*
Check for system problems. Always run before reporting an issue.

| Option | Effect |
|--------|--------|
| `--list-checks` | List all available health checks |

### `brew missing [formula]`
Check for missing dependencies.

---

## Version Control

### `brew pin <formula>`
Prevent formula from being upgraded by `brew upgrade`. Note: may still upgrade if a dependency.

### `brew unpin <formula>`
Allow pinned formula to be upgraded.

### `brew tab <formula>`
Control autoremove behavior.

| Option | Effect |
|--------|--------|
| `--installed-on-request` | Mark as manually installed (protect from autoremove) |
| `--no-installed-on-request` | Allow autoremove to remove it |

---

## Tap Management

### `brew tap [user/repo]`
No args: list all taps. With args: add a tap from GitHub (`https://github.com/user/homebrew-repo`).

### `brew untap [tap]`
| Option | Effect |
|--------|--------|
| `-f, --force` | Untap even if formulae from this tap are installed |

### `brew tap-info [tap]`
| Option | Effect |
|--------|--------|
| `--installed` | Show info for all installed taps |

---

## Bundle / Brewfile

### `brew bundle dump`
| Option | Effect |
|--------|--------|
| `-g, --global` | Write to `~/.homebrew/Brewfile` or `~/.Brewfile` |
| `-f, --force` | Overwrite existing Brewfile |
| `--describe` | Add description comments for each entry |
| `--no-vscode` | Exclude VS Code extensions |

### `brew bundle install`
| Option | Effect |
|--------|--------|
| `--upgrade` | Also upgrade installed packages |
| `--cleanup` | Remove anything not in the Brewfile |

### `brew bundle cleanup`
| Option | Effect |
|--------|--------|
| `-f, --force` | Actually remove (otherwise just lists what would be removed) |

### `brew bundle check`
Exit 0 if all Brewfile deps satisfied. Great for CI checks.

---

## Services

### `brew services list`
List all running and registered services.

### `brew services start <formula>`
Start service AND register to start at login (macOS) or boot (Linux).

### `brew services stop <formula>`
Stop service AND unregister from auto-start.

### `brew services run <formula>`
Start for current session only — does NOT register for auto-start.

### `brew services restart <formula>`
Stop and start, maintaining registration.

### `brew services cleanup`
Remove all unused service registrations.

---

## Utility

### `brew --prefix [formula]`
Show Homebrew's install path. With formula arg: show where that formula would be installed.

### `brew --cache [formula]`
Show download cache path. With formula arg: show cache file for that formula.

### `brew --cellar [formula]`
Show Cellar path.

### `brew config` *(alias: `--config`)*
Show Homebrew and system configuration. Include in bug reports.

### `brew shellenv`
Print export statements for `$PATH`, `$MANPATH`, `$INFOPATH`. Use in shell profile:
```bash
eval "$(brew shellenv)"
```

### `brew link <formula>` *(alias: `ln`)*
| Option | Effect |
|--------|--------|
| `-f, --force` | Allow keg-only formulae to be linked |
| `-n, --dry-run` | Preview |

### `brew unlink <formula>`
Remove symlinks. Useful for temporarily disabling a formula.

### `brew migrate <formula|cask>`
Migrate renamed packages to their new names.

### `brew home [formula|cask]`
Open the formula/cask's homepage in a browser.
