# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

---

## [1.1.0] — 2026-03-10

### Added

- `LICENSE` — MIT license (copyright 2025 TzoharLary)
- `CONTRIBUTING.md` — contribution guidelines (official sources required, one topic per PR)
- `CHANGELOG.md` — this file, Keep a Changelog format
- `SECURITY.md` — security policy and reporting instructions
- `.github/ISSUE_TEMPLATE/bug_report.yml` — structured bug report form
- `.github/ISSUE_TEMPLATE/skill_improvement.yml` — structured improvement suggestion form
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist requiring official source links
- `.github/workflows/ci.yml` — CI pipeline: frontmatter validation, markdownlint, link check
- `scripts/validate-skill.py` — validates SKILL.md has all required frontmatter fields
- `.markdownlint.yaml` — markdownlint config (MD013/MD033 disabled)
- `homebrew/EXAMPLES.md` — 5 prompt/response examples in 4 categories
- `homebrew/SKILL.md` frontmatter: `version: "1.1.0"`, `maintainer: TzoharLary`
- `research/skill-runtimes/` — research on Codex, Claude Code, and Google Cloud Code support
- `research/community-health/` — license analysis and community files analysis
- `research/implementation-plan/plan-v2.md` — full implementation plan with 5 review cycles

### Changed

- `homebrew/README.md` — expanded with multi-runtime install table (GitHub Copilot, Codex, Claude Code), install instructions for each runtime, usage examples section
- Root `README.md` — MIT badge, link to LICENSE, note about multi-runtime support, updated skill structure

---

## [1.0.0] — 2025-06-10

### Added

- Initial `homebrew/SKILL.md` with 13 sections covering all core Homebrew topics
- `homebrew/references/` directory with 6 deep-reference files:
  - `commands.md` — complete command reference with all flags
  - `workflows.md` — step-by-step maintenance recipes
  - `env-vars.md` — all `HOMEBREW_*` environment variables
  - `disk-space.md` — disk space management guide
  - `platform-guide.md` — Intel / Apple Silicon / Linux differences
  - `troubleshooting.md` — common problems and fixes
- `homebrew/README.md` — basic installation guide for GitHub Copilot (VS Code)
- Root `README.md` with project overview and quick install command
- `research/skill-design` branch with full implementation research and sources

---

[Unreleased]: https://github.com/TzoharLary/homebrew-copilot-skill/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/TzoharLary/homebrew-copilot-skill/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/TzoharLary/homebrew-copilot-skill/releases/tag/v1.0.0
