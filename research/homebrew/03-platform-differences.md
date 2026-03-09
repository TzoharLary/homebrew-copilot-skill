# Homebrew Platform Differences

**Source:** https://docs.brew.sh/Manpage and https://docs.brew.sh/FAQ  
**Date:** 2025-06-10

---

## Installation Prefixes

From the official `--prefix` documentation:

| Platform | Default Prefix | Notes |
|----------|---------------|-------|
| **macOS Apple Silicon** (ARM) | `/opt/homebrew` | Current default for M1/M2/M3/M4 Macs |
| **macOS Intel** (x86_64) | `/usr/local` | Legacy Macs, still supported |
| **Linux** | `/home/linuxbrew/.linuxbrew` | Allows non-admin users to benefit |

From FAQ:
> "The prefix `/opt/homebrew` was chosen to allow installations in `/opt/homebrew` for Apple Silicon and `/usr/local` for Rosetta 2 to coexist and use bottles."

## Running Both Intel and Apple Silicon on the Same Mac

On Apple Silicon Macs, it is possible to run both:
- Native ARM Homebrew at `/opt/homebrew` (default)
- Intel (Rosetta 2) Homebrew at `/usr/local` for compatibility

This is an advanced use case. Users typically only need the native ARM installation. The prefixes are intentionally different so both can coexist.

## Bottle Availability

From FAQ:
> "Our pre-built binary packages (bottles) can only be used if you install in the default installation prefix, otherwise they have to be built from source. Building from source takes a long time, is prone to failure, and is not supported."

**Key implication:** Always use the default prefix for each platform to get pre-built bottles. If you install Homebrew in a non-default prefix, every formula must be compiled from source.

Bottle availability depends on:
1. Using the default prefix for your platform
2. Being on a supported macOS version (bottles are generated only for supported versions)
3. Not passing options like `--build-from-source` or formula-specific options

## Cache Locations

From the `HOMEBREW_CACHE` environment variable documentation:

| Platform | Default Cache Path |
|----------|-------------------|
| macOS | `~/Library/Caches/Homebrew` |
| Linux | `$XDG_CACHE_HOME/Homebrew` or `~/.cache/Homebrew` |

## Log Locations

| Platform | Default Log Path |
|----------|-----------------|
| macOS | `~/Library/Logs/Homebrew` |
| Linux | `$XDG_CACHE_HOME/Homebrew/Logs` or `~/.cache/Homebrew/Logs` |

## Temp Directory

From `HOMEBREW_TEMP` documentation:

| Platform | Default Temp Path |
|----------|------------------|
| macOS | `/private/tmp` |
| Linux | `/var/tmp` |

## Cellar and Caskroom

The Cellar and Caskroom locations respect the prefix:

- **Apple Silicon macOS:** `/opt/homebrew/Cellar/` and `/opt/homebrew/Caskroom/`
- **Intel macOS:** `/usr/local/Cellar/` and `/usr/local/Caskroom/`
- **Linux:** `/home/linuxbrew/.linuxbrew/Cellar/` (no Caskroom on Linux; casks are macOS-only)

## Environment File Locations

Brew reads environment files in this order (later overrides earlier, unless `HOMEBREW_SYSTEM_ENV_TAKES_PRIORITY`):

1. `/etc/homebrew/brew.env` — system-wide
2. `$(brew --prefix)/etc/homebrew/brew.env` — prefix-specific
3. `$XDG_CONFIG_HOME/homebrew/brew.env` or `~/.homebrew/brew.env` — user-specific

## Linux-Specific Environment Variables

From the manpage:
- `HOMEBREW_ARCH` — Linux only: pass value to compiler `-march` option (default: `native`)
- `HOMEBREW_CURL_PATH` — Linux only: path to `curl` executable
- `HOMEBREW_GIT_PATH` — Linux only: path to `git` executable

## macOS-Specific Behaviors

### Casks (macOS only)
Casks are macOS-specific. They install `.app` bundles, font files, browser extensions, etc. Linux does not have casks.

### Gatekeeper
When installing casks, macOS Gatekeeper may block apps from "unidentified developers." From FAQ:
> "You can allow individual apps to be exempt from this feature. Right-click the app and choose Open."

### App Management Permission (macOS Ventura+)
From FAQ:
> "Starting in macOS Ventura, in-place upgrades [for casks] are only allowed when the updater application has certain permissions granted. Either 'App Management' or 'Full Disk Access' permission will suffice."

This affects `brew upgrade --cask` behavior. Without the permission, macOS uses uninstall/reinstall strategy, which may lose Dock position and app permissions.

### `sudo launchctl` for GUI App PATH
From FAQ:
> "GUI apps on macOS don't have Homebrew's prefix in their PATH by default. You can fix this by running `sudo launchctl config user path "$(brew --prefix)/bin:${PATH}"` and then rebooting."

## Detecting Your Platform

Use these commands to identify your setup:

```bash
# Show the prefix (tells you which platform you're on)
brew --prefix   # /usr/local = Intel, /opt/homebrew = Apple Silicon

# Or from brew config — shows all platform details
brew config
```

## Shell Configuration Differences

For Apple Silicon, Homebrew is typically added to the shell in `.zprofile`:
```bash
eval "$(brew shellenv)"
```

For Intel Mac, Homebrew is usually already in PATH via `/usr/local/bin`.

For Linux, add to `~/.bashrc` or `~/.zshrc`:
```bash
eval "$(brew shellenv)"
```
