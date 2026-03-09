# Homebrew Maintenance Workflows

Step-by-step recipes for common Homebrew maintenance scenarios.

---

## Daily Quick Check

```bash
brew outdated        # Are there updates?
```

If there are updates:
```bash
brew upgrade         # Install them
brew cleanup         # Clean up old versions
```

---

## Weekly Maintenance Routine

Run in this exact order:

```bash
# Step 1: Refresh the formula database
brew update

# Step 2: See what has updates
brew outdated

# Step 3: Upgrade everything (or specific packages)
brew upgrade
# OR:
brew upgrade git node python   # Only specific packages

# Step 4: Also upgrade auto-updating apps (Chrome, VS Code, Slack, etc.)
brew upgrade --greedy

# Step 5: Preview what cleanup would remove (safety check)
brew cleanup --dry-run

# Step 6: Remove old versions and stale cache
brew cleanup

# Step 7: Preview orphan removal
brew autoremove --dry-run

# Step 8: Remove orphaned dependencies
brew autoremove

# Step 9: Health check
brew doctor
```

---

## New Machine Setup from Brewfile

On the old machine:
```bash
# Create a complete inventory of your Homebrew setup
brew bundle dump --global --force --describe
# Creates/updates ~/.homebrew/Brewfile with all formulae, casks, taps
# The --describe flag adds comments explaining each package

# View what was captured
cat ~/.homebrew/Brewfile
```

Transfer `~/.homebrew/Brewfile` to the new machine (via iCloud, airdrop, git, etc.), then:

```bash
# On the new machine — verify Homebrew is installed first:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install everything from the Brewfile
brew bundle install --global

# Check if anything failed
brew bundle check --global
```

---

## Rolling Back After a Bad Upgrade

If `brew upgrade formula` breaks something:

```bash
# 1. Check what versions are installed
brew list --versions formula

# 2. Install the previous version (if still in Cellar)
brew switch formula <old-version>   # (deprecated in newer Homebrew, use below)

# 3. Modern approach: uninstall current, reinstall specific version
brew uninstall formula
brew install formula@<major-version>   # e.g., brew install python@3.11

# 4. Pin it to prevent re-upgrading
brew pin formula
```

> **Note:** After `brew cleanup` runs, old versions are deleted and can't be rolled back. If you need rollback capability, set `HOMEBREW_NO_INSTALL_CLEANUP=1` or use `brew pin` before upgrading.

---

## CI/CD Pipeline Setup

For Homebrew in CI environments, prevent interactive prompts and auto-behavior:

```bash
# Recommended CI environment variables
export HOMEBREW_NO_AUTO_UPDATE=1        # Don't update on every command
export HOMEBREW_NO_INSTALL_CLEANUP=1    # Don't cleanup (manage separately)
export HOMEBREW_NO_ANALYTICS=1          # Disable analytics
export NONINTERACTIVE=1                 # Suppress prompts (install script)

# Install specific packages
brew install git node python

# Or from a Brewfile
brew bundle install --file=./Brewfile
```

For reproducible builds, commit your `Brewfile`:
```bash
brew bundle dump --file=./Brewfile --force
# Add to source control
git add Brewfile && git commit -m "Add Brewfile"
```

---

## Selective Formula Maintenance (Skip Pinned)

```bash
# See what's pinned
brew list --pinned

# Upgrade everything EXCEPT pinned formulae
brew upgrade   # Pinned formulae are automatically skipped

# Upgrade a specific pinned formula intentionally
brew unpin formula && brew upgrade formula && brew pin formula
```

---

## Audit Your Installation

```bash
# Large package finder
brew info --sizes --installed | sort -h   # Sort by size (smallest first)
brew info --sizes --installed | sort -rh  # Sort by size (largest first)

# See manually installed packages (leaves with no dependents)
brew leaves -r

# See packages you may not need anymore
brew leaves -r | while read f; do brew info "$f" | head -3; echo '---'; done

# Find formulae with multiple installed versions
brew list --multiple

# Check for missing deps
brew missing
```

---

## Post-macOS Upgrade Recovery

After upgrading macOS, some formulae may break (especially those with compiled C extensions):

```bash
# Check for problems first
brew doctor

# Reinstall all formulae (recompiles/re-links)
brew reinstall $(brew list --formula)

# If that fails for specific ones:
brew reinstall python
brew reinstall node

# Re-check
brew doctor
brew missing
```
