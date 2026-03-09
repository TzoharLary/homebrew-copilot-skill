# Homebrew Environment Variables Reference

All `HOMEBREW_*` environment variables from the official Homebrew manpage.

> **Important:** Variables must have a value to be active. Use `export HOMEBREW_NO_AUTO_UPDATE=1`, not just `export HOMEBREW_NO_AUTO_UPDATE`.

---

## Cleanup and Version Management

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_INSTALL_CLEANUP` | not set | If set, disables auto-cleanup after install/upgrade/reinstall |
| `HOMEBREW_CLEANUP_MAX_AGE_DAYS` | `120` | Max age (days) for cached files before auto-cleanup removes them |
| `HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS` | `30` | How often (days) to run a full cleanup of ALL formulae |
| `HOMEBREW_NO_CLEANUP_FORMULAE` | not set | Comma-separated list of formulae to exclude from cleanup |
| `HOMEBREW_NO_AUTOREMOVE` | not set | If set, prevents auto-removal of unused deps during cleanup/uninstall |

---

## Auto-Update Behavior

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_AUTO_UPDATE` | not set | Skip auto-update check before install/upgrade/tap commands |
| `HOMEBREW_AUTO_UPDATE_SECS` | `86400` (24h) | Minimum seconds between auto-updates. Set to `3600` if dev commands used |
| `HOMEBREW_API_AUTO_UPDATE_SECS` | `450` | How often to check the API for new formula/cask metadata |

---

## Installation Behavior

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_INSTALL_UPGRADE` | not set | `brew install formula` won't upgrade if already installed but outdated |
| `HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK` | not set | Skip checking for broken/outdated dependents after installing |
| `HOMEBREW_NO_INSTALL_FROM_API` | not set | Use local tap checkouts instead of API (slower; needed only for formula editing) |
| `HOMEBREW_ASK` | not set | If set, always ask for confirmation before downloading/installing (shows sizes) |

---

## Cask Behavior

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_CASK_OPTS` | not set | Options appended to all cask commands; e.g. `--appdir=${HOME}/Applications` |
| `HOMEBREW_UPGRADE_GREEDY` | not set | If set, include `auto_updates true`/`version :latest` casks in all upgrades |
| `HOMEBREW_UPGRADE_GREEDY_CASKS` | not set | Space-separated list of specific casks to always treat as greedy |

---

## Network and Downloads

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_CACHE` | `~/Library/Caches/Homebrew` (macOS) | Custom cache directory for downloaded bottles and sources |
| `HOMEBREW_BOTTLE_DOMAIN` | `https://ghcr.io/v2/homebrew/core` | Mirror URL for bottle downloads |
| `HOMEBREW_API_DOMAIN` | `https://formulae.brew.sh/api` | Mirror URL for Homebrew JSON API |
| `HOMEBREW_CURL_RETRIES` | `3` | Number of curl retries on failure |
| `HOMEBREW_CURL_VERBOSE` | not set | If set, enable verbose curl output for debugging |
| `HOMEBREW_DOWNLOAD_CONCURRENCY` | `auto` | Parallel download connections (`auto` = 2× CPU cores) |
| `HOMEBREW_GITHUB_API_TOKEN` | not set | Personal access token for GitHub API (higher rate limits; avoids failures during mass installs) |

---

## Analytics

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_ANALYTICS` | not set | Disable anonymous analytics about install/upgrade/fail events |

---

## Logging and Display

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_LOGS` | `~/Library/Logs/Homebrew` (macOS) | Directory for log files |
| `HOMEBREW_VERBOSE` | not set | If set, always enable verbose output (equivalent to always passing `--verbose`) |
| `HOMEBREW_DEBUG` | not set | If set, always enable debug output |
| `HOMEBREW_NO_COLOR` | `$NO_COLOR` | If set, disable colored output |
| `HOMEBREW_NO_EMOJI` | not set | If set, disable emoji in output |
| `HOMEBREW_DISPLAY_INSTALL_TIMES` | not set | If set, print how long each formula took to install |

---

## Build Environment

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_MAKE_JOBS` | CPU core count | Number of parallel jobs for `make` during source builds |
| `HOMEBREW_TEMP` | `/private/tmp` (macOS), `/var/tmp` (Linux) | Temporary directory for builds |
| `HOMEBREW_FORCE_BREWED_CURL` | not set | Always use Homebrew's curl (auto-set if system curl is too old) |
| `HOMEBREW_FORCE_BREWED_GIT` | not set | Always use Homebrew's git (auto-set if system git is too old) |
| `HOMEBREW_FORCE_VENDOR_RUBY` | not set | Always use Homebrew's vendored Ruby |

---

## Linux-Specific

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_ARCH` | `native` | Pass value to compiler `-march` option during builds |
| `HOMEBREW_CURL_PATH` | system curl | Path to the curl executable |
| `HOMEBREW_GIT_PATH` | system git | Path to the git executable |

---

## Setting Variables

### Option 1: Shell Profile (applies to all shell sessions)
```bash
# ~/.zshrc or ~/.bash_profile
export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_CLEANUP_MAX_AGE_DAYS=30
export HOMEBREW_NO_ANALYTICS=1
```

### Option 2: Homebrew-Specific Env File (recommended)
```bash
# ~/.homebrew/brew.env
# Simple KEY=VALUE format (no shell expansion, no subcommands)
HOMEBREW_NO_AUTO_UPDATE=1
HOMEBREW_CLEANUP_MAX_AGE_DAYS=30
HOMEBREW_NO_ANALYTICS=1
```

### Option 3: Per-Invocation Override
```bash
HOMEBREW_NO_AUTO_UPDATE=1 brew install git
```

---

## Recommended Configurations

### Disk-Conscious Developer
```
HOMEBREW_CLEANUP_MAX_AGE_DAYS=7
HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS=7
HOMEBREW_NO_ANALYTICS=1
HOMEBREW_GITHUB_API_TOKEN=<your-token>
```

### CI/CD Pipeline
```
HOMEBREW_NO_AUTO_UPDATE=1
HOMEBREW_NO_INSTALL_CLEANUP=1
HOMEBREW_NO_ANALYTICS=1
HOMEBREW_DOWNLOAD_CONCURRENCY=4
```

### Multi-Version Developer (needs rollback capability)
```
HOMEBREW_NO_INSTALL_CLEANUP=1
HOMEBREW_NO_CLEANUP_FORMULAE=python,ruby,node
HOMEBREW_GITHUB_API_TOKEN=<your-token>
```
