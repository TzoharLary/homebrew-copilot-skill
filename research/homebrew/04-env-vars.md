# Homebrew Environment Variables

**Source:** https://docs.brew.sh/Manpage (ENVIRONMENT section)  
**Date:** 2025-06-10

> **Important:** Environment variables must have a value set to be detected. Use `export HOMEBREW_NO_AUTO_UPDATE=1` not just `export HOMEBREW_NO_AUTO_UPDATE`.

---

## Most Commonly Useful Variables

### Cleanup and Versions

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_INSTALL_CLEANUP` | Not set | If set, disables auto-cleanup after install/upgrade/reinstall |
| `HOMEBREW_CLEANUP_MAX_AGE_DAYS` | `120` | Max age (days) for auto-cleanup to remove cached files |
| `HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS` | `30` | Interval (days) for full cleanup of all formulae |
| `HOMEBREW_NO_CLEANUP_FORMULAE` | Not set | Comma-separated list of formulae to exclude from cleanup |
| `HOMEBREW_NO_AUTOREMOVE` | Not set | If set, `brew cleanup` and `brew uninstall` won't auto-remove unused dependents |

### Updates

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_AUTO_UPDATE` | Not set | If set, skip auto-update before install/upgrade/tap. Not recommended for daily use. |
| `HOMEBREW_AUTO_UPDATE_SECS` | `86400` (24h) | How often to run auto-update. `3600` if dev commands used, `300` if `HOMEBREW_NO_INSTALL_FROM_API` set |
| `HOMEBREW_API_AUTO_UPDATE_SECS` | `450` | How often to check API for new formula/cask data |

### Installation Behavior

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_INSTALL_UPGRADE` | Not set | If set, `brew install formula` won't upgrade if already installed but outdated |
| `HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK` | Not set | If set, skip checking for broken/outdated dependents after installing |
| `HOMEBREW_NO_INSTALL_FROM_API` | Not set | If set, use local tap checkouts instead of the API (slower, needed for formula editing) |
| `HOMEBREW_ASK` | Not set | If set, always ask for confirmation before downloading/installing (shows sizes) |

### Cask Behavior

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_CASK_OPTS` | Not set | Append options to all cask commands, e.g. `--appdir=${HOME}/Applications` |
| `HOMEBREW_UPGRADE_GREEDY` | Not set | If set, include `auto_updates true`/`version :latest` casks in upgrades |
| `HOMEBREW_UPGRADE_GREEDY_CASKS` | Not set | Space-separated list of casks to always treat as greedy |

### Network and Downloads

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_CACHE` | `~/Library/Caches/Homebrew` (macOS) | Custom cache directory |
| `HOMEBREW_BOTTLE_DOMAIN` | `https://ghcr.io/v2/homebrew/core` | Mirror for bottle downloads |
| `HOMEBREW_API_DOMAIN` | `https://formulae.brew.sh/api` | Mirror for Homebrew JSON API |
| `HOMEBREW_CURL_RETRIES` | `3` | Number of `curl` retries on failure |
| `HOMEBREW_CURL_VERBOSE` | Not set | If set, enable verbose `curl` output |
| `HOMEBREW_DOWNLOAD_CONCURRENCY` | `auto` | Parallel download connections (`auto` = 2x CPU cores) |
| `HOMEBREW_GITHUB_API_TOKEN` | Not set | Personal access token for GitHub API (increases rate limits) |

### Analytics

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_NO_ANALYTICS` | Not set | If set, disable anonymous usage analytics |

### Logging and Display

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_LOGS` | macOS: `~/Library/Logs/Homebrew` | Directory for log files |
| `HOMEBREW_VERBOSE` | Not set | If set, always `--verbose` |
| `HOMEBREW_DEBUG` | Not set | If set, always `--debug` |
| `HOMEBREW_NO_COLOR` | `$NO_COLOR` | If set, disable colored output |
| `HOMEBREW_NO_EMOJI` | Not set | If set, disable the beer mug emoji |
| `HOMEBREW_DISPLAY_INSTALL_TIMES` | Not set | If set, print install times for each formula |

### Build Environment

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_MAKE_JOBS` | CPU core count | Parallel jobs for `make` during builds |
| `HOMEBREW_TEMP` | macOS: `/private/tmp`, Linux: `/var/tmp` | Temporary directory for builds |
| `HOMEBREW_FORCE_BREWED_CURL` | Not set | Always use Homebrew-installed `curl` (auto-set if system version is too old) |
| `HOMEBREW_FORCE_BREWED_GIT` | Not set | Always use Homebrew-installed `git` (auto-set if system version is too old) |
| `HOMEBREW_FORCE_VENDOR_RUBY` | Not set | Always use Homebrew's vendored Ruby |

### Developer

| Variable | Default | Effect |
|----------|---------|--------|
| `HOMEBREW_DEVELOPER` | Not set | Enable developer mode (warnings become errors) |
| `HOMEBREW_EVAL_ALL` | Not set | Evaluate all formulae/casks by default (needed for caching descriptions) |

---

## Where to Set Environment Variables

Option 1 — Shell profile (set every shell session):
```bash
# ~/.zshrc or ~/.bash_profile
export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_CLEANUP_MAX_AGE_DAYS=30
```

Option 2 — Homebrew env files (preferred for Homebrew-specific settings):
```bash
# ~/.homebrew/brew.env
# Note: does NOT support shell variable expansion or command execution
HOMEBREW_NO_AUTO_UPDATE=1
HOMEBREW_CLEANUP_MAX_AGE_DAYS=30
```

Option 3 — Prefix-level setting:
```bash
# $(brew --prefix)/etc/homebrew/brew.env
# Applies to all users of this Homebrew installation
```

---

## Practical Combinations

### Performance-Optimized Setup (CI/CD)
```bash
export HOMEBREW_NO_AUTO_UPDATE=1        # Skip auto-update (done separately)
export HOMEBREW_NO_INSTALL_CLEANUP=1    # Handle cleanup manually
export HOMEBREW_NO_ANALYTICS=1          # Disable analytics
export HOMEBREW_DOWNLOAD_CONCURRENCY=4  # Fixed concurrency
```

### Developer Setup
```bash
export HOMEBREW_NO_INSTALL_CLEANUP=1          # Keep old versions for rollback
export HOMEBREW_NO_CLEANUP_FORMULAE=python,ruby  # Never clean these
export HOMEBREW_GITHUB_API_TOKEN=<your-token>   # Higher rate limits
```

### Power User Disk-Conscious Setup
```bash
export HOMEBREW_CLEANUP_MAX_AGE_DAYS=7    # Clean downloads > 7 days old
export HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS=7  # Full cleanup every week
```
