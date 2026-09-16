---
type: technique
goal: "Add a Level 2 LLM Wiki to a Claude Code second brain: one agent-maintained markdown wiki per data type, routed from CLAUDE.md, fed through an ingest step you control, and kept healthy with lint checks."
difficulty: intermediate
time_to_build: "About 1–2 hours to scaffold the folders, router and ingest skill (estimate, not from the video), then a few minutes per ingest"
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]"]
tools: ["[[Claude Code]]", "[[Obsidian]]", "[[OpenAI Codex]]"]
tags: [topic/second-brain, topic/retrieval, topic/claude-code, topic/skills, topic/memory]
---

# Ingest Sources into an LLM Wiki

## Goal

Build Level 2 of [[Nate Herk]]'s [[Second Brain Levels]]. You add a wiki folder, with an index and pages the agent writes itself, to a project that already has a Level 1 router. Then you ingest sources into it one controlled batch at a time. The payoff: when you ask about anything a source covered, Claude opens the wiki's index, drills down to the right pages and reads them. It doesn't ask you for more information, and it doesn't search the whole project.

- Level 2's question is whether the system can **pull everything on one topic together** ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)).
- It keeps the Level 1 shape and builds on top of it ([10:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=621s)).
- He credits the pattern to [[Andrej Karpathy]] ([08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s)). For the idea itself, see [[LLM Wiki]].
- Starting from an empty folder? Scaffold the wiki with [[Bootstrap an LLM Wiki from the Karpathy Gist]] first, then use this note for ingest discipline.

## Use when

| Signal | What the video says | Timestamp |
|---|---|---|
| You have 30+ notes and keep forgetting what's in them | His rule of thumb for moving to Level 2 | [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s) |
| Files are piling up, take different shapes, and need grouping differently | This is when a wiki starts to make sense | [08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s) |
| A steady stream of one kind of material | Research on one project; his YouTube transcripts; his meeting transcripts | [08:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=511s), [08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s), [08:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=520s) |
| Answers need the **whole document** (e.g. "summarise the March 5th meeting") | A handful of vector chunks misses content. Reading the full markdown file is more accurate | [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [17:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1038s) |
| Your work is mostly projects and content rather than a big multi-client CRM | His own situation, where routing files and wikis have been enough | [19:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1195s) |
| A wiki works and nothing hurts enough to add search | He runs pretty much all of Herk2 at Level 2 and hasn't felt enough pain to move up. The captions say "switch over to level two" there, but from context he means Level 3 | [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s), [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s) |

**Hold off, or pick a different build, when:**
- **Nothing hurts yet.** Pick the lowest level that meets your needs. Without a pain point, don't build a new architecture ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).
- **You need one small fact from a huge body of text**, like rule 17 out of 1,000 rules. He calls that a good use case for vector search, because reading the whole file would waste time and tokens ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)–[18:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1127s)). See [[Add Semantic Search to One Folder]].
- **You need to follow chains of relationships** ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)). See [[Build a Knowledge Graph Layer]].
- **The data is volatile**, e.g. Slack threads, emails, customer data. Don't ingest it; make it reachable instead ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)–[28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)). See [[Tiered Lookup Routing]].

## Prerequisites

- **A Level 1 brain.** That means a CLAUDE.md router plus context, projects and decisions folders. At Level 2 the router still points to all three ([10:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=631s)). See [[Build a Level 1 Second Brain]] and [[CLAUDE.md as a Router]].
- **[[Claude Code]], or any agent harness.** A brain is just files and folders, so he also uses his with Codex and [[Hermes Agent]] ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)–[01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).
- **The questions you'll ask.** How data will be recalled should decide how it goes in ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s), [02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)).
- **A privacy decision.** Ingesting through Claude sends the material to Anthropic. For client data you may prefer open-source models ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- **Optional: [[Obsidian]]**, if a visual view helps you ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s)).

## Steps

1. **Write the questions before the folders.** List 5–10 questions you'll actually ask this wiki. He says to work backwards from the question, because how data is recalled should shape how it's stored ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)–[02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)).
2. **One wiki per data type.** He keeps separate wikis for YouTube transcripts and for meeting transcripts ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)–[08:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=520s)). Research on a single project is another good fit ([08:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=511s)).
3. **Check that markdown suits this folder.**
   - Questions that need a whole document fit markdown ([17:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1038s)). Pulling one fact out of a huge body fits vectors ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)).
   - A project can mix both. You might make one unit a vector database and keep context, projects and decisions as markdown ([17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s), [17:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1071s)).
   - If unsure, describe the data and how you'll use it to Claude Code, and ask which fits ([19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s)).
4. **Put the wiki inside the main project.** His transcript wiki sits a few folders down inside Herk2, where the main brain can reach it. The path is captioned "Other Worlds", then "YouTube OS", then the transcript wiki ([09:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=557s)–[09:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=566s)). Scaffold the tree under *Starter files* below.
5. **Decide the page types.**
   - His YouTube wiki has: concepts (e.g. agentic workflows, AI coding market, context window), sources, platforms, techniques (e.g. context management) and comparisons ([08:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=529s), [08:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=539s), [09:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=572s)).
   - The pages link back to related tools, concepts and videos ([08:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=535s)).
   - For a meetings wiki, adapt the types. This note suggests meetings, people and topics.
6. **Update the CLAUDE.md router.**
   - Add routes to the wiki, a references folder and the memory file. Keep the context, projects and decisions routes ([10:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=628s)–[10:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=633s)). The video doesn't say what goes in references.
   - In practice, Level 2 is just more routing rules in the same file ([10:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=637s)).
   - Keep ingest procedures out of the router (this note's advice). His reason to keep it lean: when CLAUDE.md grows too big it gets messy and feels ignored ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)). A starter block is below.
7. **Turn on auto memory (optional).** Toggle it with the /memory command. Claude then writes and updates the memory file itself ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s), [10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s)). See [[Claude Code Auto Memory]]. The video shows memory.md inside the project, but Claude Code stores auto memory elsewhere (see *Beyond the source*).
8. **Keep it usable from other tools.**
   - CLAUDE.md and the auto-updated memory file are specific to Claude Code ([11:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=668s)).
   - For Codex, copy CLAUDE.md to AGENTS.md and tell Codex to look in memory.md for memories ([11:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=679s), [11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)).
   - Or reference AGENTS.md from inside CLAUDE.md so its content is pulled in ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)).
   - See [[Port a Claude Code Brain to Other Agents]] and [[Tool-Agnostic Context Files]].
9. **Create the ingest skill** (outline below) so every ingest follows the same page, index and log rules.
10. **Ingest.** He just tells Claude Code to ingest a YouTube transcript into the wiki. Claude Code then creates the concept, source, platform and technique pages and links them together ([09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s)).
11. **Stay in control of what goes in.**
    - He decides what his brain ingests ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
    - He runs a skill that gathers the week's meeting transcripts ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)). He works through the material with Claude (the captions read "how many brains are about this", *unclear in captions*; probably which brains or wikis it belongs to) ([26:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1591s)–[26:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1593s)). Then they ingest it together ([26:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1595s)).
    - Why: different kinds of data need different treatment ([26:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1597s)), and he worries about the point where more context starts doing more damage than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)).
12. **Filter with the one-year test.**
    - Ingest material you won't delete and will still want in a year ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)–[27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)).
    - Volatile data (Slack threads, emails, customer data) turns into noise you have to clear out every month ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)). Leave it out, but make sure the brain can go and fetch it ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)).
    - See [[Context vs Connections]].
13. **Test retrieval.**
    - Ask your target questions and watch the path. Claude should open the index, go to the matching page, then follow links onward ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)–[12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s)).
    - Run the human test too. He finds a slide deck by clicking through project, YouTube videos and the dated video folder. His agent finds it the same way because the routing makes sense ([07:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=433s)–[07:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=463s)).
    - The core check: can your agent find it again, and could you ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s))?
14. **(Optional) Open the folder in Obsidian.** Obsidian only visualises the markdown files ([09:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=576s)). Install it if the view helps you; he rarely opens it ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s), [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).
15. **Maintain it.** Run the lint checks below. He says wikis start to degrade at a certain point ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)), and every page the agent opens is read in full ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)), so watch page size and index length.

## Starter files & prompts

*Everything in this section is an original starting point written for this vault. The video shows the shape of his wiki (page types, index, routing) but doesn't give the text of his files, prompts or ingest skill. Where something mirrors what he describes, the timestamp is in the Steps above.*

### Folder tree

This extends the base tree in [[Build a Level 1 Second Brain]], so the Level 1 paths (`context/`, `projects/priorities.md`, `decisions.md`) stay the same.

```text
my-brain/
├── CLAUDE.md                 # Level 1 router + Level 2 wiki routes
├── AGENTS.md                 # optional: same router for Codex
├── context/                  # always-true background; read first
├── projects/                 # includes priorities.md
├── decisions.md              # dated decisions, appended
├── references/               # docs/specs you point Claude at
├── memory/
│   └── MEMORY.md             # optional portable memory index (see Beyond the source)
├── inbox/                    # raw material waiting to be ingested
└── wikis/
    ├── youtube/
    │   ├── index.md          # catalogue: one line per page, grouped by type
    │   ├── log.md            # append-only record of ingests and lint passes
    │   ├── raw/              # optional: original transcripts, never edited
    │   ├── sources/          # one page per video
    │   ├── concepts/
    │   ├── techniques/
    │   ├── platforms/        # tools and products
    │   └── comparisons/
    └── meetings/
        ├── index.md
        ├── log.md
        ├── meetings/         # one page per meeting, read whole
        ├── people/
        └── topics/
```

### CLAUDE.md routing block

```markdown
## Where things live
| When you need…                                   | Look in                    | How |
|--------------------------------------------------|----------------------------|-----|
| Background on me, how I work, my stack           | `context/`                 | Read first |
| Active projects and clients                      | `projects/`                | One folder per project |
| This quarter's priorities                        | `projects/priorities.md`   | Then the project files it links to |
| Past decisions and why                           | `decisions.md`             | Append new decisions with a date |
| Anything learned from YouTube videos             | `wikis/youtube/index.md`   | Open the index, then only matching pages; follow their "How it connects" links if needed |
| What was said or decided in a meeting            | `wikis/meetings/index.md`  | Find the meeting page by date and people; read it whole |
| External docs and specs                          | `references/`              | |
| Remembered preferences and corrections           | `memory/MEMORY.md`         | |

## Wiki rules
- Answer wiki questions from the wiki's index first. Search the whole project only if the index has no match, and tell me you did.
- Name the wiki pages you used.
- Only write to a wiki through `/wiki-ingest`.
- Don't ingest volatile data (chat threads, email, customer records, task statuses). Fetch it live instead.
```

### Ingest skill outline

Save as `.claude/skills/wiki-ingest/SKILL.md`. The format was checked against the Claude Code docs; see *Beyond the source*.

```markdown
---
name: wiki-ingest
description: Ingest a source (transcript, article, meeting notes) into one of the wikis under wikis/. Use when I say "ingest" and point at a file or paste text.
disable-model-invocation: true
---

Ingest $ARGUMENTS.

1. Route: decide which wiki this belongs in (youtube, meetings, ...). If it fits several or none, ask me.
2. Filter: would I still want this in a year? Flag volatile parts (statuses, chat threads,
   customer records, "this week" details) and leave them out.
3. Read the entire source. Then read that wiki's index.md.
4. Propose a plan and WAIT for my OK:
   - the source page you'll create
   - existing pages you'll update, and what you'll add to each
   - new pages you'll create (only when no existing page fits)
   - what you're deliberately skipping, and why
5. Write the source page first, then the concept / technique / platform / comparison pages,
   using the page format below. Every point links back to its source page.
6. Update index.md: one line per new page, in the right section, with a one-line summary.
7. Append to log.md: date, source, pages created, pages updated.
8. Lint only the pages you touched: broken links, missing index lines, orphans,
   contradictions with existing pages (report these; don't silently overwrite).
9. Report: 3–5 takeaways, pages created and updated, anything skipped.

## Page format
(paste the page and source formats from this note)
```

### Page format

Wiki links alone don't say *how* two pages relate ([12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s)). So this format (a suggestion, not from the video) writes the relationship word next to each link:

```markdown
---
type: concept             # source | concept | technique | platform | comparison
title: Context Window
sources: [sources/2026-05-30-top-50-features.md]
created: 2026-06-01
updated: 2026-06-14
---

# Context Window

**In one line:** what it is, in plain words.

## What the sources say
- A point, paraphrased (source page + timestamp or section)

## How it connects
- part of: concepts/agentic-workflows.md
- contrasts with: concepts/long-term-memory.md
- managed by: techniques/context-management.md

## Open questions / contradictions
```

Source page:

```markdown
---
type: source
title: <video or meeting title>
origin: <URL or file path>
date: 2026-06-17
ingested: 2026-06-18
---

# <title>

## Summary            (3–5 sentences)
## Key points         (each with a timestamp or section reference)
## Pages this source touched
```

Index:

```markdown
# YouTube wiki — index
_Updated 2026-06-18 · 42 pages · 12 sources_

## Concepts
- concepts/context-window.md — what fills the window and how to manage it (4 sources)

## Techniques
- techniques/context-management.md — ways to keep sessions lean (2 sources)
```

### Lint and maintenance checks

| Check | How to spot it | Why it matters |
|---|---|---|
| Orphan pages | Page has no incoming links and isn't in the index | If nothing points to it, the agent can't find it again ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)) |
| Index drift | A page file with no index line, or an index line pointing at a missing file | The index is where every lookup starts ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)) |
| Broken links | Link target doesn't exist | Retrieval works by following a trail of links ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)) |
| Duplicates | Near-identical titles or one-liners ("Context Window" / "Context Windows") | Knowledge gets split across pages |
| Contradictions | Two pages disagree on the same claim | Report and ask; don't let the latest ingest overwrite silently |
| Volatile content | Statuses, "this week", pasted chat or email | Noise you'll have to delete later ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)) |
| Sprawling pages | A page now covers several topics | Every open reads the whole page ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)), so split it |
| Index too big to scan | The index no longer fits comfortably in one read | Likely one form of the degradation he mentions ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)); he doesn't spell out the cause. Consider [[Add Semantic Search to One Folder]] |
| Log gaps | A source page with no log entry | Breaks the audit trail |

Lint prompt: *"Lint wikis/youtube. Run every check in the lint table. Fix index drift and broken links yourself. List orphans, duplicates, contradictions, volatile content and sprawling pages for me to decide on. Append the pass to log.md."*

[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] adds two checks from Karpathy that grow the wiki: fill gaps by web search, and suggest new article candidates, run daily or weekly ([15:11](https://www.youtube.com/watch?v=sboNwYmH3AY&t=911s)).

### Test prompts

| Prompt | Pass if |
|---|---|
| "Using the YouTube wiki, what do my sources say about context windows? List the files you opened, in order." | Opens `index.md` first, then a few pages. No project-wide search |
| "Which videos compared two coding agents?" | Lands on a comparisons page, then its source pages |
| "Summarise the meeting on 2026-06-10." | Finds the meeting page by date and reads it whole |
| A question the wiki can't answer | Says it isn't in the wiki and doesn't invent an answer |
| Same first prompt in Codex (with AGENTS.md) | Opens the same pages |

## Done when

- [ ] Each data type has its own `wikis/<name>/` folder with `index.md`, `log.md` and page-type folders
- [ ] CLAUDE.md routes to each wiki index, references and memory, and still routes to context, projects and decisions
- [ ] The ingest skill proposes a plan and waits before writing anything
- [ ] At least three sources are ingested, each with a source page, index lines and a log entry
- [ ] A second source on the same topic updates the existing concept page instead of creating a duplicate
- [ ] Test prompts show Claude going index → page → linked page without being told where to look
- [ ] You can find a page yourself by drilling through the folders ([07:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=433s))
- [ ] A lint pass reports no broken links and no index drift
- [ ] If you use other agents, AGENTS.md mirrors the routes and says where memory lives

## Pitfalls

- **Whole-page reads at scale.**
  - The wiki reads every page it opens in full. If it only needed one detail (his example is ElevenLabs), it still reads the entire AI-video-production page ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)–[24:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1447s)).
  - The same waste of time and tokens is his argument for vectors in the rule-17 example ([18:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1127s)). He also says wikis start to degrade at a certain point ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)).
  - Mitigation (this note's suggestion): keep pages to one topic and write informative index one-liners so fewer pages get opened.
  - If a folder keeps missing notes you know exist, his pointer is semantic search ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)), and one folder can switch style without the rest ([17:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1071s)).
- **Treating links as typed relationships.**
  - Wiki links are like see-also references or backlinks. They don't carry labels like "endorsed by" ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)–[12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)).
  - His wiki feels relational only because he put time and effort into ingesting with context ([23:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1432s)–[23:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1435s)).
  - A graph tool such as [[LightRAG]] holds much the same data but records named relationships ([24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)). If your questions follow chains, see [[Build a Knowledge Graph Layer]].
- **Ingesting noise.** Volatile data turns into noise and needs monthly deletes ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)). He is wary of too much context doing more damage than good, which is why he controls ingestion by hand ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)–[26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
- **A wiki the router doesn't mention is invisible.** Claude won't search your whole project by itself. If it doesn't know something lives somewhere, it probably won't find it ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)).
- **Router bloat.** An oversized CLAUDE.md gets messy and feels ignored ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)). Keep procedures in the skill and only routes in the router.
- **One wiki for everything.** He separates wikis by data type ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)–[08:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=520s)).
- **Chunking what should be read whole.** Summarising a meeting from vector chunks only covers the chunks retrieved ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s)). Keep meetings as whole markdown pages ([17:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1038s)).
- **Blaming retrieval for a capture problem.** Often the knowledge never left your head. Before blaming the AI, check whether the folders hold the nuance you carry around ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)). The [[Grill Me Interview Skill]] interviews you and writes up a brainstorm file, and you can feed it transcripts and contracts ([20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s), [21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s)).
- **Making Obsidian the goal.** The graph view hooks people. What matters is whether the system can get the information back to you ([09:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=589s)–[10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)).
- **Copying someone else's layout as "the right way".** There's no proven standard. What counts is routing that makes sense to you and to your AI ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s), [07:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=423s)).
- **Privacy.** Everything ingested through Claude is processed by Anthropic ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- **Claude-only memory.** The auto-updated memory file is a Claude Code feature. Other agents have to be told where it is ([11:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=668s), [11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)).

## Variations

- **Meetings wiki with a weekly batch.** A skill gathers the week's transcripts, then you and Claude ingest them together ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)–[26:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1595s)).
- **Project research wiki** ([08:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=511s)).
- **A wiki alongside higher levels.** His Level 4 example keeps its wiki next to the new knowledge-graph folder, with the same plain-markdown routing; he calls boring beautiful ([23:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1389s)–[23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s)). One folder could also be a vector index instead ([17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s)).
- **Always-on ingestion (Level 5).** [[GBrain]] keeps syncing and refreshing memories on its own ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)). In Claude Code you'd have to set up the cron jobs yourself, which is one reason he doesn't run it ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). See [[Always-On Brain OS]].
- **Team wiki.** The harder part is adoption: process owners keeping docs current, and teammates using the wiki instead of pinging the same people ([30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s)–[30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)). Get your own brain working first ([30:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1826s)).
- **File answers back into the wiki.** Neither Nate video shows this. [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] shows it: the agent answers from the index, then saves the reusable part as a page linked to its sources and updates index.md and log.md ([18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s)). To keep step 11's control, have it propose the page and wait (vault suggestion).
- **Raw inbox with a processed queue** (Matt), **YouTube channel batch** and **external wiki vault** (Nate, April). See below.
- **One vault split by stage, with an index.md in every folder.** This is the layout in [[Chase AI - The Agentic OS Setup for Claude Code]]. Details are below.

### Variation in depth: raw / wiki / outputs with nested indexes (Chase AI)

**What the video describes**

- **Set up the vault.** Obsidian is free. You designate a folder as the vault, choosing either to create a new vault or to open an existing folder as one ([14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s)–[14:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=888s)). To "connect" Claude Code, go to that folder in the terminal and start Claude Code there ([15:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=917s)–[15:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=942s)). Obsidian itself is optional ([13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s)).
- **Three stage folders.** He credits the layout to Karpathy ([17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s)):
  - raw/ holds unstructured data ([17:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1067s)).
  - wiki/ holds that data turned into structured, Wikipedia-style articles ([17:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1077s)–[18:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1096s)).
  - outputs/ holds deliverables made from the wiki, such as a slide deck ([18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s)–[18:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1134s)).
- **An index.md at every level.** He calls this the real power ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)). Claude reads the root index, picks a folder, reads that folder's index, then opens the file ([19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s)–[20:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1225s)). The payoff grows as years of files build up ([20:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1236s)–[20:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1249s)).
- **Folder names are yours to choose.** Ask Claude Code to review the vault and propose a structure, using Karpathy's setup as inspiration ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)–[21:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1301s)).
- **A vault CLAUDE.md** with conventions: a vault structure section and a navigation pattern section that sets the path to follow when finding things ([21:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1307s)–[22:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1331s)). His own top-level folders are content, notes, runs, inbox, ops and projects ([22:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1322s)).
- **Log runs in the same vault.** Skill and automation outputs should be logged there, so self-improving loops can read past runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)).

**How it differs from the main build above**

| | Main build (Nate + Karpathy's gist; gist details under Beyond the source) | Chase's variation |
|---|---|---|
| Split | One wiki per data type under `wikis/` | One vault split by processing stage: `raw/` → `wiki/` → `outputs/` |
| Indexes | One `index.md` per wiki | An `index.md` in every folder, at every depth |
| Router | CLAUDE.md "Where things live" table | Vault CLAUDE.md with "Vault structure" and "Navigation pattern" sections |
| Log | `log.md` per wiki (ingest audit trail) | Run logs for skills and automations, meant for loops; no ingest log mentioned |
| Deliverables | Not covered (the gist files good answers back as wiki pages) | Their own `outputs/` folder |
| Volatile data | Kept out; fetched live (step 12) | He suggests a copy of all of a domain's data, e.g. all your sales data ([15:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=910s)). This conflicts with step 12, so apply the one-year filter anyway |

**Starter files**

*Vault starter content written for this note. The video shows the idea and his CLAUDE.md headings, not the text of his files.*

```text
vault/
├── CLAUDE.md             # vault conventions: structure + navigation pattern
├── index.md              # one line per top-level folder
├── raw/
│   ├── index.md          # one line per source or source batch
│   └── 2026-09-ai-agents/
├── wiki/
│   ├── index.md          # one line per article
│   └── ai-agents.md
├── outputs/
│   ├── index.md          # one line per deliverable
│   └── 2026-09-15-ai-agents-deck/
└── runs/                 # optional: one log per skill or automation run
    └── index.md
```

Vault CLAUDE.md sections:

```markdown
## Vault structure
- raw/: sources exactly as they arrived (articles, transcripts, research dumps). Never edit these.
- wiki/: one article per topic, synthesised from raw/. Each article lists the raw/ files it drew on.
- outputs/: finished deliverables built from wiki/ articles, one dated folder each.
- runs/: one short log per skill or automation run (date, skill, output path, what went wrong).
Every folder contains an index.md with one line per file or subfolder.

## Navigation pattern
1. Start at ./index.md and choose the folder that fits the question.
2. Read that folder's index.md. Go deeper only by following an index line.
3. For "what do we know about X", use wiki/. Open raw/ only to check a claim, or when wiki/ has nothing.
4. For "what did we produce", use outputs/. For "how did the last run go", use runs/.
5. If no index line matches, tell me before searching the whole vault.

## Index upkeep
- Whenever you add, rename, move or delete a file, update the index.md in that folder, and in its parent if a folder changed, in the same turn.
```

Folder index template:

```markdown
# wiki/ index
_Structured articles built from raw/. Updated 2026-09-15._

| File | Covers | Built from |
|---|---|---|
| ai-agents.md | What agents are, loop patterns, tool use | raw/2026-09-ai-agents/ |
```

Prompts to hand Claude Code:

1. *Structure:* "Look through this vault and propose a folder structure. Use a raw / wiki / outputs split as a starting point, and change it to fit what's actually here. Show the tree with a one-line purpose per folder. Wait for my OK before moving anything."
2. *Indexes:* "Write an index.md in every folder that lacks one, following the template in CLAUDE.md. Then list folders where you couldn't tell what a file is for."
3. *Test:* "Where would you find what we know about AI agents? List every file you read, in order." It passes if the order is root `index.md` → `wiki/index.md` → the article.

**Done when**

- [ ] Every folder has an `index.md`, and every file appears in its folder's index
- [ ] CLAUDE.md has "Vault structure" and "Navigation pattern" sections that match the real tree
- [ ] The test prompt reaches the right page through indexes alone, with no vault-wide search
- [ ] Moving one file updates both affected indexes in the same turn

**Pitfalls specific to this variation**

- **More indexes means more drift.** This is this note's warning, not his. Add an index check to the lint pass above: flag any folder without `index.md`, any index line pointing at a missing file, and any file with no index line.
- **Treating "99% of the way" as proven.** He gives no evidence or measurement for it ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)). Nate's degradation warning and the Level 3–4 options still apply ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)).
- **Deliverables that never feed back.** If an output contains new synthesis, also update the wiki article it came from (the gist's query operation; see Beyond the source).
- **The "RAG" label.** He says "RAG" in air quotes ([19:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1155s)), but no embeddings are involved. See "Where sources disagree" in [[LLM Wiki]].

### Variation in depth: raw inbox with a processed queue and no orphans (Matt Wolfe)

[[Matt Wolfe - Second Brain Wiki with Journal and CRM]] builds this in Codex with an AGENTS.md schema. For Claude Code, import that file from CLAUDE.md; see [[Bootstrap an LLM Wiki from the Karpathy Gist]].

- **Clips wait in raw/ until you ask** ([14:20](https://www.youtube.com/watch?v=yke4fLQUsh4&t=860s)). The generated ingest reads each source, creates or updates pages, updates index.md and appends to log.md ([20:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1202s)).
- **A processed queue.** A new last step moves each source into raw/processed/, so whatever is still in raw/ is the queue ([20:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1218s)).
- **Provenance on the source, no orphans.** The channel name goes in the original source page's frontmatter ([20:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1259s)), and every generated or updated page is cross-linked to that source page, so orphans are prevented at write time rather than caught by lint ([21:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1268s)).
- **Reprocess after rule changes** ([28:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1727s)), then schedule it. His hourly run has no review step ([29:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1778s)), unlike step 11's plan-and-wait.

*Vault starter content:* add to the skill outline "5b. Link every page you created or updated to this source's page." and "10. Move the file to `inbox/processed/`; never delete it." If you schedule it, keep the one-year filter in the scheduled prompt.

### Variation: batch-ingest a YouTube channel (Nate Herk, April)

- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] told Claude Code to fetch his recent transcripts and organise everything ([01:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=62s)); 36 videos took about 14 minutes ([11:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=714s)). He doesn't show how the transcripts were fetched.
- The index groups tools, techniques, concepts, sources, people and comparisons ([04:06](https://www.youtube.com/watch?v=sboNwYmH3AY&t=246s)). Each source page has tags, the video link, the raw file, a summary, takeaways and backlinks ([00:22](https://www.youtube.com/watch?v=sboNwYmH3AY&t=22s)). After the batch, each new video is a one-line ingest request that gets logged ([04:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=275s)).

### Variation: route other projects to an external wiki vault (Nate Herk, April)

- The wiki is its own vault, and its CLAUDE.md lets any project crawl it ([13:23](https://www.youtube.com/watch?v=sboNwYmH3AY&t=803s)). His assistant's CLAUDE.md sends it to the hot cache, the index, then a domain sub-index, and only when needed ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s)).
- By June his transcript wiki sits inside Herk2 ([09:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=555s)), as in step 4. Vault reading: nest a wiki that one project uses; keep a separate vault when several share it. Starter block: [[Bootstrap an LLM Wiki from the Karpathy Gist]].

## Beyond the source

*None of this comes from the videos. Each item was checked at the linked page.*

- **Karpathy's three operations.** Verified: [Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
  - *Ingest:* the LLM reads a new source and discusses the key points with you. It writes a summary, updates the index, revises the related entity and concept pages, and appends to the log. One source can touch 10–15 pages. You can stay involved one source at a time or batch-ingest with less oversight. Steps 10–11 and the skill outline follow the hands-on style.
  - *Query:* search the relevant pages and answer with citations. Good answers can be filed back into the wiki as new pages.
  - *Lint:* a periodic health check for contradictions, stale claims, orphan pages, missing cross-references and gaps. The lint table above puts this into practice.
- **`index.md` and `log.md`.** The gist describes `index.md` as a catalogue of every page by category with one-line summaries, updated on each ingest and used for retrieval. `log.md` is an append-only, time-ordered record of ingests, queries and lint passes. Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **The raw layer.** In the gist, raw sources are kept as they are: the LLM reads them but never edits them. That is the optional `raw/` folder above. Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **Scale.** The gist says the index file is enough at moderate size, about 100 sources and hundreds of pages. Beyond that it recommends proper search and names qmd, a local hybrid BM25/vector search tool with CLI and MCP interfaces. That matches Nate's warning that wikis degrade. Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **Where auto memory actually lives.** Verified: [Claude Code memory docs](https://code.claude.com/docs/en/memory).
  - The video shows a memory.md inside his example project ([10:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=633s)). Claude Code's own auto memory is stored **outside the repo**, at `~/.claude/projects/<project>/memory/`. There, a `MEMORY.md` index loads into every session (the first 200 lines or 25KB), and topic files are read when needed.
  - It is on by default, toggled from `/memory`, and stays on your machine.
  - So the memory.md in his example is one of two things, and the video doesn't show which. It could be an ordinary file kept current through instructions, for example by asking Claude to update it. Or it could be auto memory moved into the project with the `autoMemoryDirectory` setting (an absolute path or one starting with `~/`). Either way, an in-project memory file (`memory/MEMORY.md` in the starter above) is what lets Codex or other agents see the same memories. See [[Claude Code Auto Memory]].
- **Importing AGENTS.md.** Claude Code reads CLAUDE.md, not AGENTS.md. A CLAUDE.md containing `@AGENTS.md` loads that file at session start, and a symlink also works. Imported files still take up context at launch. Verified: [memory docs](https://code.claude.com/docs/en/memory).
- **Keep CLAUDE.md short.** The docs suggest staying under about 200 lines per CLAUDE.md, because longer files cost context and are followed less reliably. The docs also say multi-step procedures belong in a skill rather than CLAUDE.md, and a skill's full content loads only when it is invoked. That supports keeping the ingest procedure in a skill. Verified: [memory docs](https://code.claude.com/docs/en/memory).
- **Skill format.** Verified: [Claude Code skills docs](https://code.claude.com/docs/en/skills).
  - Project skills live at `.claude/skills/<name>/SKILL.md` and run as `/<name>`.
  - `description` helps Claude decide when to load the skill.
  - `disable-model-invocation: true` means only you can trigger it, which suits a skill that writes many files.
  - `$ARGUMENTS` receives whatever you type after the command.
- **Obsidian needs no conversion.** Obsidian stores notes as plain-text Markdown files in a vault, which is just a local folder. You can point it straight at the brain folder. Verified: [Obsidian help: data storage](https://obsidian.md/help/data-storage).
- **A working example in this vault.** Verified: the file itself, `.claude/skills/ingest-youtube/SKILL.md`.
  - The skill that builds this knowledge bank is a real ingest skill for an LLM Wiki.
  - It fetches metadata and the transcript into a scratch folder, outside the vault. It checks whether the video was already ingested, reads the whole transcript and `Home.md`, and fixes every note title before writing so links resolve.
  - It writes notes from `Templates/`, then checks timestamp accuracy and provenance and runs `.tools/check_links.py` for broken links. Then it updates `Home.md` (the index) and appends to `Ingest Log.md` (the log).
  - It differs from the starter above in two ways. It keeps raw transcripts out of the vault; the vault's `CLAUDE.md` says to re-fetch one when a detail is needed. And for long videos it gives each group of notes to a separate agent, fact-checks each note against the transcript, then runs a completeness pass.
- **Karpathy's original post already had outputs.** Coverage of his April 2026 "LLM Knowledge Bases" post on X describes these parts:
  - raw data collected into a `raw/` directory
  - a markdown wiki the LLM compiles from it, with index files that summarise the documents
  - outputs such as Marp slide decks and matplotlib charts
  
  Query outputs get filed back into the wiki so each exploration adds up, and the coverage says embeddings or vector search aren't needed at personal-knowledge-base scale. So Chase's `outputs/` stage follows the post rather than the later gist. The coverage doesn't say outputs got their own folder or that every folder had an index; those details look like Chase's own additions. The view count he gives (over 20 million) matches the post's roughly 21.9 million on 2026-09-15 ([FxTwitter API readout](https://api.fxtwitter.com/karpathy/status/2039805659525644595)); an April 2026 write-up's 16+ million was an early count ([Starmorph guide](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide)). Verified: [DAIR.AI Academy summary of the post](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy). The [post itself](https://x.com/karpathy/status/2039805659525644595) needs an X account to open directly.
- **Opening an existing folder as a vault.** Obsidian's vault switcher has two options: "Create new vault" and "Open folder as vault". The second lets you point Obsidian at an existing Claude Code project without moving any files. Verified: [Obsidian help: Manage vaults](https://obsidian.md/help/manage-vaults).

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]]. The main sections for this note are the Level 2 chapter ([08:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=491s)–[13:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=782s)), ingest control and context vs connections ([26:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1570s)–[28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s)), and finding your level ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]. Used for the channel batch, the external-vault routing and lint ([01:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=62s)–[04:43](https://www.youtube.com/watch?v=sboNwYmH3AY&t=283s), [13:23](https://www.youtube.com/watch?v=sboNwYmH3AY&t=803s)–[15:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=925s)).
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]. Used for filing answers back and the raw-inbox variation ([18:13](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1093s)–[21:23](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1283s), [28:22](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1702s)–[31:30](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1890s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]. Used for the raw / wiki / outputs variation. The relevant parts are Obsidian vault setup ([14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s)–[15:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=947s)) and the Karpathy structure, nested indexes, vault CLAUDE.md and run logging ([17:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1033s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)).

## Related

- Concepts: [[LLM Wiki]] · [[Second Brain Levels]] · [[Design for Retrieval]] · [[CLAUDE.md as a Router]] · [[Claude Code Auto Memory]] · [[Tool-Agnostic Context Files]] · [[Context vs Connections]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Semantic Search]] · [[Knowledge Graphs]] · [[Always-On Brain OS]] · [[Agentic OS]] · [[Loop Engineering]]
- Techniques: [[Bootstrap an LLM Wiki from the Karpathy Gist]] (setup from scratch) · [[Build a Level 1 Second Brain]] (the level before) · [[Tiered Lookup Routing]] · [[Port a Claude Code Brain to Other Agents]] · [[Add Semantic Search to One Folder]] (the level after) · [[Build a Knowledge Graph Layer]] · [[Grill Me Interview Skill]] · [[Second Brain Pain-Point Audit]]
- Tools: [[Claude Code]] · [[Obsidian]] · [[OpenAI Codex]] · [[Hermes Agent]] · [[GBrain]] · [[LightRAG]]
- People: [[Nate Herk]] · [[Andrej Karpathy]] · [[Chase AI]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]
- [[Home]]
