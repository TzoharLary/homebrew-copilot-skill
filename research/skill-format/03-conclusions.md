# Skill Format Design Conclusions

**Date:** 2025-06-10  
**Based on:** Files 01-02 in this research directory

These conclusions feed directly into the implementation plan.

---

## Naming Decision: `homebrew`

**Chosen skill name:** `homebrew`

Rationale:
- Lowercase alphanumeric — satisfies the `name` field constraint
- 8 characters — well within the 1-64 char limit
- Maximally clear and discoverable — users typing `@homebrew` or asking about `brew` will trigger it
- The directory name `homebrew/` will match this exactly
- Disambiguation possible in description: no collision with Homebrew the company

## Directory Structure

```
homebrew/                  ← directory name matches name: field exactly
├── SKILL.md               ← frontmatter + body (core skill)
├── references/            ← Level 3 resources (loaded on demand)
│   ├── commands.md        ← Complete command reference
│   ├── workflows.md       ← Step-by-step maintenance workflows
│   ├── env-vars.md        ← All HOMEBREW_* environment variables
│   ├── disk-space.md      ← Disk space management guide
│   ├── platform-guide.md  ← Intel vs ARM vs Linux differences
│   └── troubleshooting.md ← Common problems and solutions
└── README.md              ← Installation instructions (VS Code + Insiders)
```

## Frontmatter Design

```yaml
---
name: homebrew
description: |   # max 1024 chars
  Expert guidance for Homebrew package manager on macOS and Linux.
  USE FOR: installing formulae and casks, brew install, brew upgrade,
  brew cleanup, brew update, brew outdated, brew autoremove, brew doctor,
  brew bundle, brew services, brew pin, brew tap, brew leaves, brew deps,
  disk space management, cache cleanup, environment variables,
  HOMEBREW_* variables, maintenance routines, Brewfile, platform differences
  between Intel Mac/Apple Silicon/Linux, keg-only packages, taps,
  troubleshooting broken installations, services management.
  DO NOT USE FOR: pip, npm, apt, yum, dnf, chocolatey, snap, flatpak,
  or other package managers.
argument-hint: "What do you want to do with Homebrew?"
user-invocable: true
---
```

## SKILL.md Body Structure

The body should provide:
1. Quick-reference key concepts (short — fits in Level 2 load)
2. Platform detection instructions
3. Essential workflows (basic — detailed versions in references/)
4. Explicit pointers to reference files for deep dives

Each section should end with: `For complete details, see references/<file>.md`

## What Goes Where

| Content | File |
|---------|------|
| Core concepts + quick workflows | `SKILL.md` body |
| Every command + every flag | `references/commands.md` |
| Maintenance routine workflows | `references/workflows.md` |
| All env vars with defaults | `references/env-vars.md` |
| Disk space step-by-step workflow | `references/disk-space.md` |
| Platform prefix/cache/behavior diffs | `references/platform-guide.md` |
| brew doctor + link + unlink + migrate | `references/troubleshooting.md` |
| Install instructions for both VS Code | `README.md` |

## Description Field Content

The description (max 1024 chars) must trigger the skill for:
- brew/Homebrew questions
- Package management on Mac
- Disk space management (since Homebrew is a major contributor)
- Maintenance workflows
- Environment variable questions
- Specific common commands: `install`, `upgrade`, `cleanup`, `update`, `doctor`

## `user-invocable` Setting

Set to `true` (the default). Users should be able to explicitly invoke:
```
@homebrew how do I free up disk space?
@homebrew what's the difference between update and upgrade?
```

## README.md Content

The README must cover:
1. What the skill does
2. Prerequisites (GitHub Copilot in VS Code)
3. **Personal installation** (primary path) — works for both VS Code and VS Code Insiders
4. Verification steps
5. Updating the skill
6. Uninstallation
