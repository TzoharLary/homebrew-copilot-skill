# Homebrew Disk Space Management

A complete guide to understanding, monitoring, and reclaiming disk space used by Homebrew.

---

## Where Homebrew Uses Disk Space

| Location | What's Stored | How to Check Size |
|----------|--------------|-------------------|
| `$(brew --cellar)/` | All installed formula versions | `du -sh $(brew --cellar)` |
| `$(brew --prefix)/Caskroom/` | All installed cask versions (macOS only) | `du -sh $(brew --prefix)/Caskroom` |
| `~/Library/Caches/Homebrew/` | Downloaded bottles and source archives | `du -sh "$(brew --cache)"` |
| `~/Library/Logs/Homebrew/` | Build and install logs | Usually small; `du -sh ~/Library/Logs/Homebrew` |

---

## Step 1: Assessment (No Changes)

Always start here. Never delete without looking first.

```bash
# See which packages use the most disk space
brew info --sizes --installed

# Sort from largest to smallest
brew info --sizes --installed | sort -k2 -h -r

# Check how much the download cache uses
du -sh "$(brew --cache)"

# See formulae that have multiple versions installed
brew list --multiple

# See the full Cellar size
du -sh $(brew --cellar)

# See orphaned dependencies that could be removed
brew autoremove --dry-run
```

---

## Step 2: Preview Cleanup (No Changes)

**Always preview before deleting.** This shows exactly what will be removed and the estimated space savings.

```bash
brew cleanup --dry-run
```

Example output:
```text
Removing: /opt/homebrew/Cellar/git/2.43.0... (5.1MB)
Removing: /Users/username/Library/Caches/Homebrew/downloads/... (38.5MB)
This operation would free approximately 210.4MB of disk space.
```

---

## Step 3: Standard Cleanup

```bash
brew cleanup
brew autoremove
```

**What `brew cleanup` removes:**
- All old formula versions (keeping only the currently installed version)
- Cached download files older than `HOMEBREW_CLEANUP_MAX_AGE_DAYS` days (default: 120)
- Stale lock files

**What `brew cleanup` keeps:**
- The currently active installed version of each formula
- Cached downloads newer than 120 days

> **Why do multiple versions accumulate?** Auto-cleanup (triggered after each install/upgrade) only removes cached downloads older than 120 days. It does NOT remove old formula versions each time. Only manual `brew cleanup` or the periodic 30-day full cleanup removes old installed versions.

---

## Step 4: Deep Cache Cleanup

If standard cleanup isn't enough:

```bash
# Remove cache files older than 7 days (much more aggressive)
brew cleanup --prune=7

# Remove the ENTIRE download cache
brew cleanup --prune=all

# Also remove downloads for the latest versions (not yet installed)
brew cleanup -s
```

---

## Step 5: Nuclear Options

Use these only when you need maximum space reclamation.

```bash
# Delete the ENTIRE cache directory including everything in it
rm -rf "$(brew --cache)"

# Clean orphaned symlinks and empty directories from the prefix
brew cleanup --prune-prefix

# Remove ALL versions of a specific formula (not just the old ones)
brew uninstall --force git
```

> After `rm -rf "$(brew --cache)"`, the next install/upgrade will need to re-download everything. This is fine but may be slow.

---

## Preventing Future Space Accumulation

### More Aggressive Auto-Cleanup
Set in `~/.homebrew/brew.env`:
```text
HOMEBREW_CLEANUP_MAX_AGE_DAYS=7
HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS=7
```
This cleans cached downloads after 7 days (instead of 120) and runs a full cleanup weekly (instead of monthly).

### Weekly Cleanup Habit
```bash
# Add to weekly cron or run manually
brew cleanup && brew autoremove
```

### Audit Periodically
```bash
# Find large packages you might not need
brew info --sizes --installed | sort -rh | head -20
brew leaves -r   # Manually installed packages with no dependents
```

---

## Quick Reference: Cleanup Command Summary

| Command | What it removes |
|---------|-----------------|
| `brew cleanup` | Old formula versions + cache >120 days |
| `brew cleanup --dry-run` | Nothing (preview only) |
| `brew cleanup --prune=N` | Old versions + cache >N days |
| `brew cleanup --prune=all` | Old versions + entire download cache |
| `brew cleanup -s` | Old versions + cache >120 days + latest version downloads |
| `brew autoremove` | Orphaned dependencies |
| `rm -rf "$(brew --cache)"` | Entire cache directory |
