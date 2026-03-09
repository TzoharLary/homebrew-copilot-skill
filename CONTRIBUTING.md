# Contributing to homebrew-copilot-skill

Thank you for considering a contribution! This repository contains documentation
and skill content for Homebrew — all changes must be grounded in official sources.

---

## Types of Contributions Welcome

| Type | Examples |
|------|----------|
| **Correctness fix** | A command flag is wrong, an output example is outdated, a default value changed |
| **New runtime path** | Adding or updating install paths for a new AI runtime that supports Agent Skills |
| **New example** | A useful prompt/response pair that demonstrates a real use case |
| **Typo / grammar** | Spelling mistakes, awkward phrasing, broken formatting |

---

## Requirements for All Contributions

### 1. Official sources only

Every factual claim in this repository must be verifiable from official documentation:

- Homebrew commands, flags, and defaults: [docs.brew.sh](https://docs.brew.sh)
- GitHub Copilot skill format: [code.visualstudio.com/docs/copilot/customization/agent-skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- Claude Code skills: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- Codex skills: OpenAI official documentation or verified extension source

**Do not submit:** AI-generated commands you haven't verified, Stack Overflow answers that contradict official docs, or commands from personal experience that aren't in the official documentation.

### 2. One topic per PR

Each pull request should address a single, focused change. This makes review faster
and ensures each change has a clear scope. Examples:

- ✅ "Fix: `brew tab` should be `brew untab`"
- ✅ "Add: Claude Code global path for Apple Silicon"
- ❌ "Various fixes and improvements" (too broad — split into separate PRs)

### 3. Include documentation link in PR description

Every PR must include a link to the official documentation that supports the change.
This is required — not optional. See the PR template for the field.

---

## Pull Request Process

1. **Fork** this repository
2. **Create a branch** with a descriptive name:
   ```bash
   git checkout -b fix/brew-cleanup-default-age
   git checkout -b feat/add-codex-project-path
   ```
3. **Make your changes** and verify them locally
4. **Open a PR** against `main` using the provided PR template
5. A maintainer will review within a few days

---

## What We Will Not Accept

- Commands not present in official Homebrew documentation
- Speculation about future Homebrew behavior
- PRs that restructure the entire skill without prior discussion
- Content about non-Homebrew package managers

If you're unsure whether a change is appropriate, open an issue first to discuss it.

---

## Questions?

Open a [GitHub Issue](https://github.com/TzoharLary/homebrew-copilot-skill/issues) with your question.
