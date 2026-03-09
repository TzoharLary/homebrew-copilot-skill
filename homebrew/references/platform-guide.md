# Homebrew Platform Guide

Differences between macOS Apple Silicon, macOS Intel, and Linux installations.

---

## Identifying Your Platform

```bash
brew --prefix   # /opt/homebrew = Apple Silicon, /usr/local = Intel, /home/linuxbrew... = Linux
brew config     # Full output including OS version, CPU arch, bottles enabled
```

---

## Prefix and Directory Locations

| | macOS Apple Silicon | macOS Intel | Linux |
|---|---|---|---|
| **Prefix** | `/opt/homebrew` | `/usr/local` | `/home/linuxbrew/.linuxbrew` |
| **Cellar** | `/opt/homebrew/Cellar` | `/usr/local/Cellar` | `/home/linuxbrew/.linuxbrew/Cellar` |
| **Caskroom** | `/opt/homebrew/Caskroom` | `/usr/local/Caskroom` | N/A (no casks on Linux) |
| **Cache** | `~/Library/Caches/Homebrew` | `~/Library/Caches/Homebrew` | `~/.cache/Homebrew` |
| **Logs** | `~/Library/Logs/Homebrew` | `~/Library/Logs/Homebrew` | `~/.cache/Homebrew/Logs` |
| **Temp** | `/private/tmp` | `/private/tmp` | `/var/tmp` |

---

## Why Different Prefixes?

From the official FAQ:
> "The prefix `/opt/homebrew` was chosen to allow installations in `/opt/homebrew` for Apple Silicon and `/usr/local` for Rosetta 2 to coexist and use bottles."

- Intel Macs use `/usr/local` because it's an existing standard path that's writable without sudo
- Apple Silicon uses `/opt/homebrew` to allow both ARM and Intel (Rosetta 2) Homebrew to coexist
- Linux uses `/home/linuxbrew/.linuxbrew` so non-admin users can install without system changes

---

## Bottle Availability (Pre-Built Binaries)

From official FAQ:
> "Our pre-built binary packages (bottles) can only be used if you install in the default installation prefix, otherwise they have to be built from source. Building from source takes a long time, is prone to failure, and is not supported."

**Bottles are only available if:**
1. You use the default prefix for your platform
2. You are on a supported macOS version (Apple supports the last 3 Mac OS versions)
3. You are not passing special build options

---

## Running Intel and Apple Silicon Homebrew Together

On Apple Silicon, you can run both:
- Native ARM Homebrew at `/opt/homebrew` (primary)
- Intel/Rosetta Homebrew at `/usr/local` (for compatibility)

To invoke Intel Homebrew explicitly:
```bash
arch -x86_64 /usr/local/bin/brew install formula  # Install Intel version
```

To have both available via shell aliases:
```bash
alias ibrew='arch -x86_64 /usr/local/bin/brew'
alias mbrew='/opt/homebrew/bin/brew'
```

---

## Shell Configuration

### macOS Apple Silicon
```bash
# ~/.zprofile (recommended for login shells)
eval "$(brew shellenv)"
```

### macOS Intel
Usually already in PATH via `/usr/local/bin`. If not:
```bash
# ~/.zprofile or ~/.bash_profile
eval "$(brew shellenv)"
```

### Linux
```bash
# ~/.bashrc or ~/.zshrc
eval "$(brew shellenv)"
```

---

## macOS-Specific Features

### Casks (macOS only)
Casks install `.app` bundles, font files, browser extensions, screen savers, etc.
Linux does not support casks.

```bash
brew install --cask visual-studio-code
brew install --cask font-fira-code
```

### Gatekeeper
When first launching a cask-installed app, macOS Gatekeeper may block it.
- Right-click the app and choose **Open** to bypass the warning once

### macOS Ventura+ App Management Permission
Starting in macOS Ventura, in-place cask upgrades require one of:
- **App Management** permission (System Settings → Privacy & Security → App Management)
- **Full Disk Access** permission

Without this permission, `brew upgrade --cask` will use uninstall+reinstall strategy, which:
- Resets the app's Dock position
- May lose granted app permissions
- Is otherwise functionally equivalent

### GUI App PATH Problem
GUI apps launched from Dock or Spotlight don't inherit your shell PATH. If an app can't find Homebrew-installed tools:

```bash
# Run once, then reboot
sudo launchctl config user path "$(brew --prefix)/bin:${PATH}"
```

---

## Linux-Specific

### No sudo needed (and not allowed)
Homebrew on Linux installs to a user-writable location. Never use sudo with brew.

### Environment variables
- `HOMEBREW_ARCH=native` (default) — sets `-march=native` compiler flag
- `HOMEBREW_CURL_PATH` — path to curl if not system default
- `HOMEBREW_GIT_PATH` — path to git if not system default

### Shell setup is more important on Linux
The Homebrew prefix is NOT in the system PATH by default. `eval "$(brew shellenv)"` in your shell profile is required on Linux.
