# Codex (OpenAI) — Skill Discovery Analysis

**Source:** Source code analysis of `openai.chatgpt-26.5304.20706-darwin-x64` (`out/extension.js`)
**Date:** 2026-03-09
**Method:** Direct inspection of minified extension.js on local installation at
`~/.vscode-insiders/extensions/openai.chatgpt-26.5304.20706-darwin-x64/`

---

## Extension Identity

| Property | Value |
|----------|-------|
| Extension ID | `openai.chatgpt` |
| Display name | Codex – OpenAI's coding agent |
| Version | `26.5304.20706` |
| Description | "Codex is a coding agent that works with you everywhere you code" |

The extension contributes a `chatSessions` entry of type `"openai-codex"`.

---

## Skill Discovery Paths

### Global (Personal) Path

From `extension.js`:
```javascript
process.env.CODEX_HOME ?? path.join(homedir(), ".codex")
```
Then skills are stored under: `<codexHome>/skills/<skill-name>/`

**Result:**

| Condition | Path |
|-----------|------|
| `CODEX_HOME` not set (default) | `~/.codex/skills/<name>/SKILL.md` |
| `CODEX_HOME=/custom/path` | `/custom/path/skills/<name>/SKILL.md` |

### Project (Workspace) Path

From `extension.js` install logic:
```javascript
let m = r ? c.join(r, ".codex", "skills") : c.join(a, "skills")
```
Where `r` is `installRoot` (the project directory when installing a project-level skill).

**Result:** `.codex/skills/<name>/SKILL.md` (relative to project root)

---

## How Codex Reads SKILL.md

From `extension.js` (skill loading function):
```javascript
let l = u ? r.join(a, "SKILL.md") : a;
if (!await Ao(l, n)) return null;
let d = await de.readFile(l, n);
let m = Khe(d);  // frontmatter parser
```

- Each skill is a directory; `SKILL.md` is the entrypoint
- Frontmatter is parsed from SKILL.md
- Fields read: `description`, `shortDescription`, `name`
  (mapped via `h2 = {name:"name", description:"description", short_description:"shortDescription", "short-description":"shortDescription"}`)

---

## Frontmatter Field Mapping

| SKILL.md field | Codex internal property |
|----------------|------------------------|
| `name` | `name` |
| `description` | `description` |
| `short-description` | `shortDescription` (alias) |
| `short_description` | `shortDescription` (alias) |

Our `argument-hint` and `user-invocable` fields are **not used by Codex** but are silently ignored.

---

## Curated Skills Repository

Codex ships with a curated skills catalog:
- URL: `https://github.com/openai/skills.git`
- Branch: `main`
- Cached locally at: `<codexHome>/vendor_imports/skills/`
- Users can install from the catalog via the VS Code command `openSkills`

---

## Commands Available

| Command ID | Description |
|------------|-------------|
| `forceReloadSkills` | Force-reload all skills from disk |
| `openSkills` | Open the skills catalog/directory |

---

## Verification of Path

The following grep on `extension.js` confirms the path structure:
```
".codex" && t[e+1]==="skills"  → path segment check
"skills/changed"  → event emitted when skills change
```

The path `.codex/skills/<name>` is explicitly validated in candidate path resolution:
```javascript
a.startsWith(".codex/") && i.add(o.resolve(c, s))
a.startsWith("skills/") && i.add(o.resolve(r, a.slice(7)))
```

---

## Conclusion

| Item | Value |
|------|-------|
| Supports SKILL.md? | ✅ Yes |
| Global path | `~/.codex/skills/<name>/SKILL.md` |
| Project path | `.codex/skills/<name>/SKILL.md` |
| Compatible with our frontmatter? | ✅ Yes (extra fields silently ignored) |
| Auto-discovery? | ✅ Yes |
| Env-var override? | ✅ `CODEX_HOME` |
