# Homebrew Troubleshooting Guide

Diagnose and fix common Homebrew problems.

---

## Step 1: Always Start with `brew doctor`

```bash
brew doctor
```

`brew doctor` checks dozens of potential problems and explains each one. **Run this first before reporting any issue or trying other fixes.** Annotated output structure:

```text
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry and just ignore them. Thanks!

Warning: A newer Command Line Tools release is available.
...
Warning: Homebrew/homebrew-core is not synced correctly.
```

If `brew doctor` outputs `Your system is ready to brew.` — no action needed.

```bash
brew doctor --list-checks    # See all available health checks
```

---

## Common Problems and Fixes

### Formula Not Found in PATH
**Symptom:** Installed a formula but the command isn't found

```bash
# Check if the formula is linked
brew list formula
brew info formula    # Shows where it's installed

# Re-link the formula
brew unlink formula
brew link formula

# Check if formula is keg-only (see its info)
brew info formula | grep -i keg-only
```

For keg-only formulae (designed NOT to be in PATH to avoid conflicts):
```bash
# Option 1: Force link (use carefully)
brew link --force formula

# Option 2: Add to PATH for this session
export PATH="$(brew --prefix)/opt/formula/bin:$PATH"

# Option 3: Add permanently to shell profile
echo 'export PATH="$(brew --prefix)/opt/formula/bin:$PATH"' >> ~/.zshrc
```

---

### Missing Dependencies
**Symptom:** Formula fails to run due to missing libraries

```bash
brew missing             # Check all installed formulae for missing deps
brew missing formula     # Check a specific formula
brew reinstall formula   # Reinstall to fix broken linkage
```

---

### Formula Renamed or Deprecated
**Symptom:** `brew install foo` says formula was renamed or deprecated

```bash
brew migrate formula     # Migrate to the new name automatically
brew info formula        # Check current status and new name
```

---

### Checksum Mismatch
**Symptom:** `Error: SHA256 mismatch` during install

```bash
# Clear cached file and retry
brew cleanup formula
brew install formula
```

---

### Broken Symlinks After macOS Upgrade
**Symptom:** Commands don't work after macOS upgrade

```bash
brew doctor
brew link formula           # Re-link specific formula
brew reinstall formula      # Full reinstall if link doesn't work
brew reinstall $(brew list --formula)  # Reinstall all formulae (nuclear)
```

---

### Old Formula Database / Update Failure
**Symptom:** `brew update` fails or returns confusing errors

```bash
# Check git status of Homebrew
cd $(brew --repo) && git status

# Force fresh update
brew update --force

# If still broken, check doctor
brew doctor
```

---

### GUI App Can't Find Homebrew Tools
**Symptom:** An app opened from the Dock can't find binaries installed via Homebrew

```bash
# macOS only: Set the PATH for GUI apps system-wide (requires reboot)
sudo launchctl config user path "$(brew --prefix)/bin:${PATH}"
# Then restart your Mac
```

---

### Permission Errors
**Symptom:** Permission denied errors during install

```bash
# Check prefix ownership
ls -la $(brew --prefix)

# Fix ownership (replace USERNAME with your username)
sudo chown -R $(whoami) $(brew --prefix)

# More targeted fix (directories only)
sudo chown -R $(whoami) $(brew --prefix)/{bin,etc,include,lib,opt,sbin,share,var}
```

> **Never use `sudo brew install`.** Homebrew is designed to work without sudo.

---

### Tap Not Found or Outdated
**Symptom:** Formula from a third-party tap can't be found

```bash
brew tap                     # List all installed taps
brew tap-info user/name      # Show tap details including formula count
brew untap user/name && brew tap user/name  # Re-clone the tap
```

---

### `brew cleanup --prune-prefix`

If `brew doctor` reports orphaned symlinks:

```bash
brew cleanup --prune-prefix    # Remove symlinks with no target
```

This targets orphaned files in the Homebrew prefix (dead symlinks, empty dirs) without touching cached downloads or installed formulae.

---

## Diagnostics Info for Bug Reports

When filing an issue with `homebrew/core`, always include:

```bash
brew config                  # System info
brew doctor                  # Current warnings
brew info formula            # Info about the affected formula
brew --env                   # Full Homebrew environment
```
