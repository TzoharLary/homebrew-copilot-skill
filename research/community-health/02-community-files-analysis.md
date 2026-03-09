# Community Files Analysis

**Date:** 2026-03-09
**Question:** What community health files should this repository have, and what should they contain?

---

## GitHub Community Standards

GitHub evaluates a repository's "community health" and surfaces it on the repository Insights page.
Having all recommended files makes the repo more discoverable and marks it as well-maintained.

**Required files GitHub checks for:**

| File | Effect if present |
|------|------------------|
| `CONTRIBUTING.md` | Contributors know how to help |
| `LICENSE` | Repo is clearly open source |
| `CODE_OF_CONDUCT.md` | Community expectations are set |
| `SECURITY.md` | Security issue reporting is defined |
| `ISSUE_TEMPLATE` (directory) | Issues are structured and triageable |
| `PULL_REQUEST_TEMPLATE.md` | PRs are consistent and complete |

**Decision:** This repository is small and documentation-focused. A full Code of Conduct would be
disproportionate. We will include: CONTRIBUTING, CHANGELOG, SECURITY, ISSUE_TEMPLATE (2 templates),
and PULL_REQUEST_TEMPLATE.

---

## CONTRIBUTING.md Analysis

**Purpose:** Guide contributors on what kinds of contributions are accepted and how to make them.

**What contributions are appropriate for this repo:**
1. Correcting outdated or incorrect Homebrew commands
2. Adding new runtime installation paths (Codex, Claude Code, future runtimes)
3. Adding or improving usage examples
4. Fixing typos or grammar

**What contributions are NOT appropriate:**
1. Hallucinated commands (no AI-only knowledge, must cite official sources)
2. Opinion-based additions without documentation backing
3. Large restructuring PRs without prior discussion

**Key policies:**
- Official sources only (docs.brew.sh, runtime vendor docs)
- One topic per PR (keeps review focused)
- Include a link to the source documentation in the PR description

**Structure:**
1. Welcome note
2. Types of contributions (with guidance)
3. Requirements (official sources, one topic per PR)
4. PR process (fork → branch → PR)
5. Source reference standard

---

## CHANGELOG.md Analysis

**Format:** [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) standard.

**Why:** Widely adopted, machine-readable, human-friendly. `[Unreleased]` section at top
makes it easy to accumulate changes before tagging.

**Sections to use:** `Added`, `Changed`, `Fixed`, `Removed`, `Deprecated`, `Security`

**Initial state:**
- `[Unreleased]` — empty (all released in 1.1.0)
- `[1.0.0] — 2025-06-10` — original release (SKILL.md + references + homebrew/README.md)
- `[1.1.0] — 2026-03-10` — all changes from this improvement plan

---

## SECURITY.md Analysis

**Context:** This repository contains:
- Markdown documentation files
- A Python script (`scripts/validate-skill.py`) that runs locally, reads only local files
- A CI workflow that runs in an isolated GitHub Actions environment

**Attack surface:** Extremely low. The Python script uses `pathlib` and `yaml.safe_load` — no
network access, no shell execution, no user input from external sources.

**Policy decision:** Direct to GitHub Issues for any concerns. For a documentation repo of this
size, a private disclosure channel would be disproportionate overhead.

---

## Issue Templates Analysis

**Why YAML form format (not markdown):** YAML form templates render as guided forms in GitHub's
issue creation UI. Users fill in labeled fields rather than editing a markdown template. This
produces better-structured issues.

**Template 1: Bug Report**
- Targeting: incorrect or outdated command/output in the skill
- Fields: affected section, command observed, expected behavior, official doc link (URL)

**Template 2: Skill Improvement**
- Targeting: adding new content (runtime paths, examples, commands)
- Fields: improvement type (select), description, official source URL, example prompt/response (optional)

---

## Pull Request Template Analysis

**Goal:** Ensure every PR includes:
- What it changes
- Why
- A link to the official documentation source
- Confirmation that the change was tested locally

**Format:** Short checklist with a brief description area above it.
Checklist items (5–6 lines) are enough for this size of project.

---

## Summary

| File | Location | Priority |
|------|----------|----------|
| `CONTRIBUTING.md` | root | 🟠 High |
| `CHANGELOG.md` | root | 🟡 Medium |
| `SECURITY.md` | root | 🟡 Medium |
| `bug_report.yml` | `.github/ISSUE_TEMPLATE/` | 🟠 High |
| `skill_improvement.yml` | `.github/ISSUE_TEMPLATE/` | 🟠 High |
| `PULL_REQUEST_TEMPLATE.md` | `.github/` | 🟠 High |
