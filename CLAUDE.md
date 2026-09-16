# Claude Knowledge Bank — Router

This vault is a curated knowledge bank of the best guidance on using and improving Claude (Claude Code, the Claude apps, the API, skills, agents, memory, prompting, workflows). It is built from tutorials the user shares — mostly YouTube videos — and exists for two jobs:

1. **Answer** "how should I…" questions with sourced, specific guidance.
2. **Build** systems based on a tutorial (e.g. "set up the Level 1 second brain from the Nate Herk video in ~/projects/foo").

The structure follows the LLM Wiki pattern — plain markdown files, an index, and routing rules (see [[LLM Wiki]]). Obsidian is only the viewer.

## Where things live

| Path | What's in it | Read it when |
|---|---|---|
| `Home.md` | Master index of every note, grouped by type | Always start here to locate anything |
| `Sources/` | One note per tutorial: TL;DR, chapter-by-chapter notes with timestamp links, caveats, build ideas | Asked what a specific video/creator said; building from a tutorial |
| `Concepts/` | One idea per note, synthesised across all sources | Asked "what is / why / when to use" |
| `Techniques/` | Build-ready playbooks: prerequisites, steps, file layouts, prompts, done-checks | Asked to build or set something up |
| `Tools/` | Hub notes for products and libraries, listing every source that mentions them | Asked about a specific tool |
| `People/` | Creators and people referenced in sources | Asked who someone is or what else they've taught |
| `Templates/` | Note templates — follow them | Creating any note |
| `Ingest Log.md` | Append-only record of every ingest | Checking what's been added and when |
| `.tools/` | `fetch_youtube.py`, `check_links.py` and their venv (hidden from Obsidian) | Ingesting or validating |

## Routing rules

- **User shares a YouTube link** → run the `ingest-youtube` skill (`.claude/skills/ingest-youtube/SKILL.md`). Do the full ingest; don't just summarise in chat.
- **"How do I…" / "what's the best way to…"** → `Home.md` → matching Concepts and Techniques → answer with links to the notes and timestamped source links. If sources disagree, say so.
- **"Build X from <video / technique>"** → read the Technique note(s) and the Source note. If a step needs detail the notes don't have, re-fetch the transcript with `.tools/fetch_youtube.py` rather than guessing.
- **Nothing in the vault covers it** → say so plainly, answer from general knowledge marked as such, and suggest finding a tutorial to ingest.

## Note conventions

- **Filenames are note titles** (Title Case; no `: # ^ [ ] | /`). Link with `[[Note Title]]`. Only link to notes that exist or that are being created in the same ingest. Run `.tools/.venv/bin/python .tools/check_links.py` after writing.
- **Frontmatter** comes from the matching template in `Templates/`. Dates are `YYYY-MM-DD`. Wikilinks inside YAML are quoted: `sources: ["[[Note]]"]`.
- **Provenance is explicit.** Anything a source says gets a timestamp link: `[12:34](https://www.youtube.com/watch?v=VIDEO_ID&t=754s)`. Anything *not* from a source goes under a `## Beyond the source` heading with a link to where it was verified. Never present your own additions as what the creator said.
- **Paraphrase; don't transcribe.** Capture the knowledge in your own words. No quote longer than ~15 words. Raw transcripts are working files and are never saved into the vault.
- **Fix caption errors** in the prose (e.g. "claw.md" → CLAUDE.md) and list the non-obvious ones under `## Transcript notes` in the Source note. Mark anything unresolvable as *(unclear in captions)*.
- **One idea per Concept note.** When a new source adds to an existing concept, update that note (new angle + source link) instead of creating a near-duplicate. Call out disagreements between sources explicitly.
- **Techniques must be buildable**: goal, prerequisites, numbered steps, concrete file/folder layouts or prompts, a "Done when" checklist, and pitfalls.
- **Tags** — use this set; add new ones sparingly and list them here: `topic/second-brain`, `topic/memory`, `topic/retrieval`, `topic/rag`, `topic/knowledge-graph`, `topic/claude-code`, `topic/skills`, `topic/agents`, `topic/automation`, `topic/prompting`, `topic/privacy`, `topic/portability`, `topic/teams`, `topic/context`, `topic/models`, `topic/planning`, `topic/verification`, `topic/loops`, `topic/subagents`, `topic/permissions`, `topic/scheduling`, `topic/mcp`, `topic/design`, `topic/agentic-os`, `topic/cowork`, `topic/managed-agents`, `topic/marketing`, `topic/media`.
