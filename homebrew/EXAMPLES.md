# Homebrew Skill — Example Prompts and Responses

These examples show the kind of questions this skill can answer. Each example includes the
prompt you would type and a representative response from the AI.

---

## Category 1: Disk Space Management

### Example 1 — Full disk assessment and cleanup

**Prompt:**
```
How much disk space is Homebrew using and how do I free it up?
```

**Response:**

First, assess what's using space:

```bash
brew info --sizes --installed    # See size of each installed package
du -sh "$(brew --cache)"         # Size of download cache
brew list --multiple             # Formulae with multiple versions installed
```

Then clean up (always preview first):

```bash
brew cleanup --dry-run           # Preview what would be removed
brew cleanup                     # Remove old versions + cached files >120 days old
brew autoremove --dry-run        # Preview orphaned dependency removal
brew autoremove                  # Remove orphaned dependencies
```

For a more aggressive cleanup:

```bash
brew cleanup --prune=all         # Remove the entire download cache, not just old files
```

> **Note:** `brew cleanup` alone does NOT delete your entire cache — it only removes files older than 120 days. Use `--prune=all` if you want to reclaim all cache space immediately.

---

### Example 2 — Finding the biggest packages

**Prompt:**
```
Which of my installed Homebrew packages take the most space?
```

**Response:**

```bash
brew info --sizes --installed
```

This lists all installed formulae and casks with their on-disk size. Output looks like:

```
gcc: 1.2 GB
llvm: 847 MB
python@3.12: 312 MB
node: 201 MB
git: 44.5 MB
```

To sort by size (largest first):

```bash
brew info --sizes --installed | sort -h -r | head -20
```

If a formula has multiple versions installed (`brew list --multiple`), `brew cleanup` will remove the older ones automatically.

---

## Category 2: Platform and Migration

### Example 3 — Intel Mac to Apple Silicon migration

**Prompt:**
```
I just switched from an Intel Mac to an M3 MacBook Pro. How do I migrate my Homebrew setup?
```

**Response:**

You cannot simply copy your Intel Homebrew installation to Apple Silicon — the prefixes and binary architectures are different:

| Platform | Prefix |
|----------|--------|
| Intel Mac | `/usr/local` |
| Apple Silicon | `/opt/homebrew` |

**Recommended migration steps:**

1. **On the old Intel Mac,** export your installed packages:
   ```bash
   brew bundle dump --force --describe --file=~/Brewfile.backup
   ```
   Copy `Brewfile.backup` to the new Mac (AirDrop, iCloud, USB).

2. **On the new Apple Silicon Mac,** install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   This installs to `/opt/homebrew` automatically.

3. **Restore all packages:**
   ```bash
   brew bundle install --file=~/Brewfile.backup
   ```

4. **Review any failures.** Some formulae may have been renamed, removed, or are macOS-only.

> Expect most packages to be re-downloaded as bottles (pre-built ARM binaries) — this is fast and correct.

---

## Category 3: Cask Management

### Example 4 — Updating auto-updating apps

**Prompt:**
```
I ran brew upgrade but Chrome and Slack didn't update. How do I update them?
```

**Response:**

Apps like Chrome, Slack, VS Code, and Firefox have `auto_updates true` in their cask definition. Homebrew skips them during `brew upgrade` by default, assuming the app updates itself.

To include them:

```bash
brew upgrade --greedy            # Upgrade all casks, including auto-updating ones
brew outdated --greedy           # First check what's outdated (including auto-updating)
```

If you always want `--greedy` behavior without typing it:

```bash
export HOMEBREW_UPGRADE_GREEDY=1
```

Add that to your `~/.zshrc` or `~/.bashrc` to make it permanent.

> **macOS Ventura+ note:** Without "App Management" permission granted to Homebrew in System Settings > Privacy & Security, cask upgrades do an uninstall+reinstall instead of in-place update. This may lose your Dock position. Grant the permission once to avoid this.

---

## Category 4: Brewfile

### Example 5 — Reproducible Homebrew setup across machines

**Prompt:**
```
How do I create a Brewfile so I can restore my exact Homebrew setup on a new machine?
```

**Response:**

A Brewfile records all your formulae, casks, taps, and Mac App Store apps.

**Create a Brewfile from your current setup:**

```bash
brew bundle dump --global --force --describe
```

This writes to `~/.homebrew/Brewfile`. The `--describe` flag adds a comment above each entry explaining what it is.

Example output:
```ruby
tap "homebrew/bundle"
tap "homebrew/cask"

# Git version control system
brew "git"
# Node.js JavaScript runtime
brew "node"

# The Mozilla Firefox browser
cask "firefox"
# Visual Studio Code
cask "visual-studio-code"
```

**Restore on a new machine:**

```bash
# 1. Install Homebrew first
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Copy your Brewfile to ~/.homebrew/Brewfile (or any path)
# 3. Install everything
brew bundle install --global

# Or if the file is in your current directory:
brew bundle install
```

**Check what's missing without installing:**
```bash
brew bundle check --global       # Exits 0 if all deps satisfied, 1 if missing
```

**Tip:** Commit your Brewfile to a dotfiles repo so it's always available:
```bash
cp ~/.homebrew/Brewfile ~/dotfiles/Brewfile
```
