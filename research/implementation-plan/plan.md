# Implementation Plan: Homebrew Copilot Skill

**Created:** 2025-06-10  
**Status:** Approved after 5 review cycles (see bottom of this file)  
**Based on:** All research in `research/homebrew/` and `research/skill-format/`

---

## Plan Overview

### What We're Building

A production-quality GitHub Copilot Agent Skill named `homebrew` that helps users:
- Manage Homebrew formulae and casks
- Maintain their Homebrew installation (update, upgrade, cleanup)
- Manage disk space (the #1 pain point)
- Understand platform differences (Intel / Apple Silicon / Linux)
- Configure Homebrew via environment variables

### Skill Identity

| Property | Value |
|----------|-------|
| Name | `homebrew` |
| Directory | `homebrew/` (must match name exactly) |
| Visibility | Public GitHub repo |
| License | MIT |
| Target platforms | macOS (Intel + Apple Silicon) + Linux |

---

## File Structure to Build

```
homebrew/                         ← On main branch, root-level
├── SKILL.md                      ← Core skill file (frontmatter + body)
├── README.md                     ← Install guide
└── references/
    ├── commands.md               ← Complete command reference
    ├── workflows.md              ← Maintenance routine workflows
    ├── env-vars.md               ← All HOMEBREW_* env vars with defaults
    ├── disk-space.md             ← Disk space management
    ├── platform-guide.md         ← Platform differences
    └── troubleshooting.md        ← Common problems & brew doctor
```

Also update:
- `README.md` at repo root (full skill description + install guide)

---

## SKILL.md Spec

### Frontmatter

```yaml
---
name: homebrew
description: >-
  Expert Homebrew guidance for macOS and Linux. 
  USE FOR: brew install, brew upgrade, brew cleanup, brew update, 
  brew outdated, brew autoremove, brew doctor, brew bundle, brew services, 
  brew pin, brew tap, brew leaves, brew deps, brew info --sizes, 
  disk space management, cache cleanup, HOMEBREW_* environment variables, 
  maintenance routines, Brewfile, platform differences between Intel Mac / 
  Apple Silicon / Linux, keg-only formulae, taps, troubleshooting broken 
  installations, services management, auto-update behavior, cask upgrades, 
  --greedy flag, --dry-run workflows. 
  DO NOT USE FOR: pip, npm, apt, yum, dnf, chocolatey, snap, flatpak.
argument-hint: "What do you want to do with Homebrew?"
user-invocable: true
---
```

**Character count target:** ~600 chars (well within 1024 limit, leaves room for expansion)

### Body Sections (with approximate heading structure)

```
## Platform Identification
## Core Concepts
## Essential Daily Commands
## Maintenance Workflow
## Disk Space Management
## Managing Casks
## Version Control (pin/unpin/tab)
## Dependency Management
## Tap Management
## Brewfile
## Services
## Environment Variables
## Troubleshooting
```

Each section:
- Provides brief but complete guidance for common tasks
- Ends with pointer to detailed reference file when applicable
- Includes working bash code examples

---

## Reference Files Spec

### `references/commands.md`
Comprehensive command table. Sections:
- Core package management (install/uninstall/reinstall/upgrade)
- Update and maintenance (update/cleanup/autoremove/doctor/missing)
- Discovery (list/outdated/info/search/leaves/deps/uses)
- Version control (pin/unpin/tab)
- Tap management (tap/untap/tap-info)
- Bundle/Brewfile
- Services
- Utility (--prefix/--cache/--cellar/config/shellenv/link/unlink)

### `references/workflows.md`
Step-by-step recipes:
- Daily maintenance routine
- Weekly maintenance routine
- New machine setup with Brewfile
- CI/CD configuration
- Rolling back a formula

### `references/env-vars.md`
Complete env var reference with:
- Variable name
- Default value
- Effect
- Example usage
Sections: Cleanup/Versions | Updates | Installation | Cask Behavior | Network | Analytics | Logging | Build Environment | Developer

### `references/disk-space.md`
Detailed disk management guide:
- Understanding where disk space goes
- How to find the largest packages
- Step-by-step cleanup workflow (assessment → preview → cleanup → deep clean → nuclear)
- Preventing future accumulation

### `references/platform-guide.md`
Platform-specific guide:
- Prefix table (Intel/ARM/Linux)
- Cache and log locations
- Bottle availability implications
- macOS Ventura cask upgrade permissions
- Running both Intel and ARM Homebrew
- Shell configuration per platform
- cask availability (macOS only)
- `brew config` output interpretation

### `references/troubleshooting.md`
- `brew doctor` output interpretation
- `brew link`/`unlink` for keg-only formulae
- `brew missing` for missing dependencies
- `brew migrate` for renamed formulae
- Common error messages and fixes
- When to run `brew cleanup --prune-prefix`
- PATH issues for GUI apps (sudo launchctl)

---

## Root README.md Spec

Sections:
1. Badge: Homebrew | GitHub Copilot | Open Standard Agent Skills
2. Description: 3-sentence human-friendly overview
3. What it helps with: bullet list
4. Prerequisites: GitHub Copilot + VS Code
5. Installation (Personal — works for VS Code AND VS Code Insiders):
   - Method 1: Direct clone (recommended)
   - Method 2: Sparse checkout  
   - Method 3: Download and copy
6. Verification steps
7. Updating the skill
8. Uninstallation
9. License

---

## Deployment Plan

```
main branch:
  └─ homebrew/
      ├─ SKILL.md
      ├─ README.md
      └─ references/
          ├─ commands.md
          ├─ workflows.md
          ├─ env-vars.md
          ├─ disk-space.md
          ├─ platform-guide.md
          └─ troubleshooting.md
  README.md  (repo root, updated)
```

---

## Review Cycle 1 — Completeness Check

**Reviewer perspective:** Does the plan cover everything a Homebrew user might ask?

**Missing from initial draft, now added:**
- [x] `brew upgrade --greedy` for auto-updating casks — mentioned in workflows
- [x] `brew bundle dump --describe` for documented Brewfiles
- [x] `brew tab` for protecting specific dependencies — added to commands spec
- [x] `brew link -f` for keg-only formulae — added to troubleshooting spec
- [x] macOS Gatekeeper note for new casks — added to platform-guide spec
- [x] `sudo launchctl config user path` for GUI app PATH — added to troubleshooting
- [x] `brew list --multiple` for finding multi-version formulae — now in disk-space.md
- [x] `brew info --sizes` — confirmed in disk-space and commands

**Verdict:** Completeness check passed with 8 additions.

---

## Review Cycle 2 — Structure and Readability

**Reviewer perspective:** Will an AI agent be able to use this skill effectively?

**Issues found and resolved:**
- [x] SKILL.md body was overloaded — resolved by distributing to references/
- [x] Description lacked DO NOT USE FOR section — added (apt, yum, etc.)
- [x] `argument-hint` was missing from initial frontmatter — added
- [x] References need consistent format so AI can parse them uniformly — each reference file will use tables for quick scanning
- [x] Need to be explicit about where each reference is: SKILL.md body should state "For complete details see references/disk-space.md" in each section

**Verdict:** Structure check passed with 5 improvements.

---

## Review Cycle 3 — Accuracy and Currency

**Reviewer perspective:** Is all information from official sources? Is anything wrong?

**Checks performed:**
- [x] All commands verified against `docs.brew.sh/Manpage` — confirmed
- [x] Platform prefixes verified against FAQ — confirmed
- [x] Auto-cleanup behavior (120-day threshold) — confirmed from manpage
- [x] Periodic full cleanup (30 days) — confirmed from manpage
- [x] `brew cleanup --prune=all` behavior — confirmed
- [x] Cask `auto_updates true` exclusion from `brew upgrade` — confirmed from manpage
- [x] `--greedy` flag required for auto-updating casks — confirmed
- [x] macOS Ventura App Management permission for in-place cask upgrades — confirmed from FAQ
- [x] No sudo for Homebrew — confirmed from FAQ
- [x] `brew services` on macOS wraps launchd — confirmed from manpage
- [x] `brew info --sizes` flag exists — confirmed from manpage OPTIONS section

**Verdict:** All facts verified against official docs. No corrections needed.

---

## Review Cycle 4 — Installation UX

**Reviewer perspective:** Are the install instructions foolproof for both VS Code and VS Code Insiders?

**Checks performed:**
- [x] VS Code and VS Code Insiders use the same `~/.copilot/skills/` path — confirmed (home directory based, not app-directory based)
- [x] `git clone` method — requires git (always available on macOS dev machines)
- [x] Sparse checkout method — more complex but worth including for users who want just the skill
- [x] Manual copy method — fallback for non-git environments
- [x] Verification step — needs to tell user exactly what they should see
- [x] Update instructions — `git pull` in the skills directory
- [x] Uninstall — `rm -rf ~/.copilot/skills/homebrew`

**Issues found and resolved:**
- [x] Initial clone command was cloning to wrong path — corrected: clone directly to `~/.copilot/skills/homebrew` (with the directory name at the end)
- [x] Need to mention `mkdir -p ~/.copilot/skills` before cloning if it doesn't exist
- [x] Should mention that the repo root contains `homebrew/` subdirectory, so users cloning the whole repo must install from the subdirectory

**Verdict:** Installation UX issues resolved. 3 corrections made.

---

## Review Cycle 5 — Final Production Readiness

**Reviewer perspective:** Is this ready to ship to main?

**Final checks:**
- [x] Skill name `homebrew` satisfies: 8 chars, all lowercase, alphanumeric only — PASS
- [x] Directory name `homebrew/` exactly matches `name: homebrew` — PASS
- [x] Description covers all major entry points (install, upgrade, cleanup, disk, env vars, casks, troubleshooting) — PASS
- [x] 6 reference files cover all skill content areas — PASS
- [x] README install instructions cover VS Code + VS Code Insiders + updated the fact they're the same path — PASS
- [x] No sudo instructions (Homebrew never uses sudo) — PASS
- [x] Platform-aware content (Intel/ARM/Linux) throughout — PASS
- [x] Official sources only — PASS
- [x] Practical code examples in every section — PASS
- [x] `--dry-run` safety check emphasized for destructive operations — PASS

**VERDICT: APPROVED FOR IMPLEMENTATION ON MAIN BRANCH** ✅

---

## Implementation Order

Push to main in this sequence (single commit preferred):

1. `homebrew/SKILL.md`
2. `homebrew/references/commands.md`
3. `homebrew/references/workflows.md`
4. `homebrew/references/env-vars.md`
5. `homebrew/references/disk-space.md`
6. `homebrew/references/platform-guide.md`
7. `homebrew/references/troubleshooting.md`
8. `homebrew/README.md`
9. `/README.md` (update root)
