# Official Agent Skills Format Specification

**Source:** https://code.visualstudio.com/docs/copilot/customization/agent-skills  
**Date:** 2025-06-10

---

## What is an Agent Skill?

From the official VS Code docs:
> "An agent skill is a collection of resources that together provide instructions, context, and references to help AI agents perform a specific task."

Skills provide **general knowledge, terminology, best practices, and step-by-step instructions** — NOT runtime access to real-time data or system commands. They are read by the AI when it determines the skill is relevant, then used to generate better responses.

## Open Standard

Agent Skills is an **open standard** originally developed by Anthropic, now community-maintained at `agentskills.io`. It works across:
- GitHub Copilot (VS Code)
- GitHub Copilot CLI
- GitHub Copilot coding agent
- Claude (Anthropic)
- And many other AI systems

---

## The SKILL.md File Format

Every skill consists of a directory with at minimum a `SKILL.md` file. The file has two sections:

### 1. YAML Frontmatter (between `---` markers)

```yaml
---
name: my-skill-name
description: A clear description of what this skill helps with...
argument-hint: Optional hint shown to user about what argument to supply
user-invocable: true
disable-model-invocation: false
---
```

#### Frontmatter Field Reference

| Field | Required | Type | Constraints | Notes |
|-------|----------|------|-------------|-------|
| `name` | **Yes** | string | 1–64 chars, lowercase, alphanumeric + hyphens ONLY | **Must exactly match the parent directory name** |
| `description` | **Yes** | string | Max 1024 characters | Used by AI to decide when to use the skill. The most important field for discoverability. |
| `argument-hint` | No | string | — | Shown in UI as a hint for what argument the user should provide when invoking |
| `user-invocable` | No | boolean | Default: `true` | Whether users can invoke the skill directly with `@skill-name argument` |
| `disable-model-invocation` | No | boolean | Default: `false` | If `true`, AI cannot auto-invoke (only explicit user invocations) |

**Critical constraint:** The directory name MUST exactly match the `name:` field. `my-skill/SKILL.md` must have `name: my-skill`.

### 2. Skill Body (after the frontmatter)

The body is standard Markdown. From the official docs:
> "It can contain procedural instructions for how to use a tool, best practices for accomplishing a task, or any information that helps the agent behave better."

Best practices for the body:
- Use headers to organize content into scannable sections
- Include code examples with language fencing (` ```bash `)
- Be explicit about when to use which command/approach
- Reference other files in the skill directory for detailed information
- The body is the full "knowledge" the AI gets when the skill is loaded

---

## Three-Level Loading Architecture

From the official VS Code docs, skills are loaded in three stages for efficiency:

### Level 1: Discovery (always loaded)
- Only the `name` and `description` frontmatter fields are read
- Agent uses these to determine whether the skill is relevant to the current query
- **`description` quality is critical** — this is what determines if the skill is used

### Level 2: Instructions (loaded when relevant)
- The full SKILL.md body is loaded
- Happens when the AI determines the skill is relevant based on the description match
- The body provides the full procedural instructions and best practices

### Level 3: Resources (loaded on demand)
- Additional files referenced in the SKILL.md body
- Scripts, extended references, examples, templates
- Only accessed when the AI decides it needs them for the specific query

**Design implication:** Put the most commonly needed info in the SKILL.md body. Put extended reference data in separate files. The AI will request the files it needs.

---

## Additional Files in a Skill

A skill directory can contain any number of supporting files:
- Markdown reference files (commands, workflows, examples)
- Shell scripts or other executable resources
- Configuration templates
- Diagrams or visual aids

These files are referenced from the SKILL.md body. The AI loads them only when needed (Level 3).

---

## Description Field Strategy

The `description` field (max 1024 chars) determines when the skill is auto-invoked. Strategies:

1. **Include all trigger keywords** — list the scenarios where this skill helps
2. **Cover entry points** — what questions or tasks would a user phrase as?
3. **Cover both explicit and implicit use** — "USE FOR: X" and "DO NOT USE FOR: Y"
4. **Include the domain name** — e.g., "Homebrew", "brew", "package manager"
5. **Each listed scenario = one more chance of auto-invocation**

Example structure:
```
Expert guidance for Homebrew package manager on macOS and Linux. 
USE FOR: installing packages, upgrading formulae, managing casks, 
cleanup and disk space, maintenance workflows, environment variables, 
brew commands, tap management, Brewfile, services.
DO NOT USE FOR: Linux apt/yum, Windows Chocolatey, pip/npm packages.
```
