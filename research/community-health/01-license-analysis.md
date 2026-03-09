# License Analysis

**Date:** 2026-03-09
**Question:** What license applies to this repository, and is there any conflict with the
content sources used?

---

## Content Sources

All skill content was written based on two official sources (documented in `research/sources.md`):

| Source | License |
|--------|---------|
| `docs.brew.sh` (Homebrew documentation) | [BSD 2-Clause License](https://github.com/Homebrew/homebrew-core/blob/master/LICENSE.txt) |
| `code.visualstudio.com/docs/copilot/customization/agent-skills` | [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `agentskills.io` | Not specified (open standard) |

---

## Content Treatment

The skill content was **not copied verbatim** from any source. The approach taken was:

1. Read official documentation
2. Extract facts, commands, and their behaviors
3. Write new content structured for AI consumption (tables, code blocks, structured sections)
4. Reference the source at the end of each section

Facts (command names, flag behaviors, paths, defaults) are **not copyrightable** under US and
international copyright law — copyright applies to expression, not information. The specific
way a command is described *is* expression, but our descriptions are original.

**Assessment:** The content in this repository is original expression based on factual information
from official sources. It is not a derivative work in the legal sense.

---

## License Choice: MIT

**Reasoning:**

| Criterion | MIT | Apache 2.0 | BSD 2-Clause |
|-----------|-----|------------|--------------|
| Short and readable | ✅ | ❌ (longer) | ✅ |
| Patent grant | ❌ | ✅ | ❌ |
| Compatible with BSD (source docs) | ✅ | ✅ | ✅ |
| Community familiarity | Very high | High | High |
| Appropriate for documentation repos | ✅ | ✅ | ✅ |

**Conclusion:** MIT is the correct choice. No patent concerns exist (this is documentation, not
executable code). MIT is the most commonly recognized permissive license and aligns with the
community expectation for open-source skills.

---

## Attribution

Attribution to Homebrew documentation is already present in the skill content — each section
in `homebrew/SKILL.md` includes a reference to the relevant official page. The research branch
`research/sources.md` documents all sources explicitly.

No additional attribution obligations exist beyond what is already in place.

---

## Decision

| Item | Decision |
|------|----------|
| Repository license | MIT |
| Copyright holder | TzoharLary |
| Copyright year | 2025 (original creation) |
| Content license concern | None — original expression, not verbatim copy |
| Attribution status | Already present in skill content |
