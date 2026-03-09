# Security Policy

## Scope

This repository contains:
- Markdown documentation files (skill content and reference guides)
- A Python script (`scripts/validate-skill.py`) that runs locally and reads only local files
- A CI workflow (`.github/workflows/ci.yml`) that runs in an isolated GitHub Actions environment

There is no server, no network service, no database, and no user-facing application.
The attack surface is extremely limited.

---

## Reporting a Security Issue

If you believe you've found a security issue in this repository — for example, a malicious
payload in the skill content, or a vulnerability in the validation script — please
[open a GitHub Issue](https://github.com/TzoharLary/homebrew-copilot-skill/issues) and
describe what you found.

For a documentation repository of this size, a private disclosure channel would be
disproportionate overhead. Issues will be triaged and addressed promptly.

---

## Supported Versions

Only the latest version on the `main` branch is maintained.

| Version | Supported |
|---------|-----------|
| Latest (`main`) | ✅ |
| Older tags | ❌ |
