# Google Cloud Code — Agent Skills Support Analysis

**Source:** Official documentation at `cloud.google.com/code/docs/vscode/overview`
and `cloud.google.com/gemini/docs/codeassist/overview`
**Date:** 2026-03-09
**Method:** Direct reading of official documentation pages

---

## What is Google Cloud Code?

Cloud Code is a VS Code (and JetBrains) extension for Google Cloud infrastructure development.
Its primary function is streamlining development for:

- Google Kubernetes Engine (GKE) applications
- Cloud Run services
- Compute Engine VM management
- Secret Manager
- Cloud APIs and client libraries
- Apigee API development
- Container image creation (buildpacks, Skaffold)

---

## What is Gemini Code Assist?

Gemini Code Assist is a **separate** Google AI coding assistant plugin that integrates with
Cloud Code (and can be used independently). It provides:
- Code completions and generation
- Conversational AI chat
- Agentic mode (MCP server support)
- Code review suggestions

**Important:** Gemini Code Assist is now a separate plugin from Cloud Code (split occurred
at some point before the 2026-03-03 documentation update).

---

## Does Either Support SKILL.md / Agent Skills?

### Cloud Code

Searched official documentation for:
- "skill" → No results in context of agent skills or SKILL.md
- "SKILL.md" → Not mentioned
- "agent skills" → Not mentioned
- Discovery paths (`~/.copilot`, `~/.claude`, `~/.codex`) → Not mentioned

**Result: No skill discovery mechanism exists in Cloud Code.**

### Gemini Code Assist

Searched documentation for same keywords.

Gemini Code Assist provides:
- Chat via the Gemini panel in VS Code
- Agentic mode with MCP server support (for tool use)
- Code customization via private codebases (Enterprise tier only)

There is no SKILL.md loading, no skills directory, no Agent Skills open standard implementation.

**Result: Gemini Code Assist does not implement the Agent Skills protocol.**

---

## Why the Confusion May Arise

1. "Cloud Code" is an AI coding tool → users assume it must work like Claude Code / Copilot
2. Google has a product called "Gemini Code Assist" which sounds like a coding agent
3. Users familiar with agents skills may expect all AI coding extensions to implement the standard

**Reality:** Google Cloud Code is a **GCP infrastructure tool**, not a general-purpose AI agent.
Gemini Code Assist is an AI assistant, but it uses its own context loading system (not Agent Skills).

---

## Evidence Summary

| What we checked | Result |
|----------------|--------|
| `cloud.google.com/code/docs/vscode/overview` | No mention of SKILL.md, skills directories, or Agent Skills |
| `cloud.google.com/gemini/docs/codeassist/overview` | No mention of SKILL.md or skill loading |
| Extension features listed | GKE, Cloud Run, Compute Engine, Secret Manager, Apigee |
| AI feature description | "AI-powered chat", "code completions", "MCP servers" — not skills |

---

## Conclusion

| Item | Value |
|------|-------|
| Supports SKILL.md? | ❌ No |
| Skill discovery paths | ❌ None |
| Agent Skills compliance? | ❌ Not implemented |
| Include in install table? | ❌ No — would be false documentation |
| Mention in README? | ✅ Yes — one-line note explaining why it is not listed |

**Decision:** Google Cloud Code will not appear in the skill installation table.
A brief explanatory note will be included in `homebrew/README.md`:
> "Google Cloud Code uses Gemini Code Assist, which does not implement the Agent Skills protocol
> and is therefore not listed above."
