---
type: source
title: "Andrej Karpathy Just 10x’d Everyone’s Claude Code"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=sboNwYmH3AY
video_id: sboNwYmH3AY
published: 2026-04-05
duration: "17:46"
ingested: 2026-09-15
topics: [LLM Wiki, Karpathy gist bootstrap, idea files, Obsidian Web Clipper, ingest, hot cache, lint, cross-project wiki routing, wiki vs RAG]
tags: [source/youtube, topic/second-brain, topic/memory, topic/retrieval, topic/rag, topic/claude-code, topic/context]
---

# Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian

> **Creator:** [[Nate Herk]] · **Published:** 2026-04-05 · **Length:** 17:46 · [Watch on YouTube](https://www.youtube.com/watch?v=sboNwYmH3AY)

## TL;DR

A live setup of [[Andrej Karpathy]]'s LLM Wiki, published the day after Karpathy's gist went up (dates under Beyond the source).

- **Setup.** In an empty [[Obsidian]] vault, Nate pastes the whole gist and a short wrapper prompt into [[Claude Code]]. It creates raw/, wiki/ (analysis, concepts, entities, sources), CLAUDE.md, an index and a log.
- **First ingest.** He clips the AI 2027 article into raw/ with Obsidian Web Clipper. Claude asks what to emphasise, then writes 23 linked pages in about 10 minutes.
- **His real wikis.** A YouTube-transcript wiki built in one batch from 36 videos, and a personal "Herk Brain". His assistant project, Herk2, reads Herk Brain through a wiki path in its CLAUDE.md.
- **Close.** He covers lint and shows a wiki-vs-RAG chart Claude made: markdown wins at hundreds of pages, not at millions of documents.

This is almost certainly the "separate full video" mentioned in [[Nate Herk - Every Level of a Claude Second Brain]]. This vault uses the same pattern.

## Key takeaways

- **The gist is the install.** You don't clone a repo. Hand the deliberately vague gist to Claude Code and let it build a version for you [05:09](https://www.youtube.com/watch?v=sboNwYmH3AY&t=309s). See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **Say what the vault is for before the first ingest.** A second brain and a research dump get set up differently [09:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=575s). See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **One source becomes many linked pages.** Nate calls this the agent's own chunking [10:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=610s). Expect it to be slow and to ask questions. See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **Other projects can use a wiki.** Their CLAUDE.md gives the vault path, a read order and "don't read unless needed" [14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s). See [[CLAUDE.md as a Router]] and [[Tiered Lookup Routing]].
- **A hot cache helps an assistant's brain, not a reference wiki** [14:57](https://www.youtube.com/watch?v=sboNwYmH3AY&t=897s). See [[Agent Memory Patterns]].
- **Wiki vs RAG depends on scale.** Hundreds of well-indexed pages suit a wiki; millions of documents need RAG. He frames this as his April 2026 view [17:22](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1042s). See [[Keyword vs Semantic vs Graph Retrieval]].

## Nate's two wikis and the demo vault

| | YouTube Transcripts wiki | Herk Brain | Demo vault (built live) |
|---|---|---|---|
| Material | 36 recent video transcripts [00:00](https://www.youtube.com/watch?v=sboNwYmH3AY&t=0s) | Personal life, Uppit AI, employees, Q2 initiatives [01:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=73s); meeting recordings, ClickUp summaries [13:38](https://www.youtube.com/watch?v=sboNwYmH3AY&t=818s) | AI 2027 article [08:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=515s) |
| Build | One "grab my transcripts and organise" batch, ~14 min [11:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=714s) | Not shown | Gist + wrapper scaffold, then clip; the ingest alone ~10 min [11:45](https://www.youtube.com/watch?v=sboNwYmH3AY&t=705s) |
| Shape | Subfolders; index groups tools, techniques, concepts, sources, people, comparisons [04:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=242s) | Flat, no subfolders [08:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=484s) | Default analysis/concepts/entities/sources [07:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=474s) |
| hot.md | No [14:34](https://www.youtube.com/watch?v=sboNwYmH3AY&t=874s) | Yes [14:40](https://www.youtube.com/watch?v=sboNwYmH3AY&t=880s) | — |
| Queried from | In place, or turned into a website [13:15](https://www.youtube.com/watch?v=sboNwYmH3AY&t=795s) | Herk2, via a wiki path in its CLAUDE.md [13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s) | Not shown |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=sboNwYmH3AY&t=0s) What We're Building

- Opens on an Obsidian graph of 36 videos and claims a roughly 5-minute setup [00:08](https://www.youtube.com/watch?v=sboNwYmH3AY&t=8s).
- **A source page** (his "$10,000 agentic workflows" video) has tags, the video link, the raw file, a summary and takeaways [00:19](https://www.youtube.com/watch?v=sboNwYmH3AY&t=19s).
- **Its backlinks** go to tools (Perplexity, VS Code, Nano Banana, n8n) and techniques (WAT framework, bypass permissions mode, human review checkpoint) [00:31](https://www.youtube.com/watch?v=sboNwYmH3AY&t=31s).
- **Patterns emerge** as the wiki fills: across tools, skills and MCP servers, all queryable [00:47](https://www.youtube.com/watch?v=sboNwYmH3AY&t=47s).
- **No manual linking.** One instruction to fetch and organise the transcripts built it [01:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=62s).
- **Merge or separate.** Wikis can be combined or kept apart, then plugged into whichever agents need them [01:32](https://www.youtube.com/watch?v=sboNwYmH3AY&t=92s).

### [01:40](https://www.youtube.com/watch?v=sboNwYmH3AY&t=100s) Karpathy's LLM Wiki Idea

- Karpathy's X post on LLM knowledge bases took off within days [01:41](https://www.youtube.com/watch?v=sboNwYmH3AY&t=101s).
- **Stages, as Nate relays them:** ingest (drop in source documents such as PDFs and Claude Code does the rest) [02:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=123s), Obsidian as the "IDE", then Q&A over the wiki [02:32](https://www.youtube.com/watch?v=sboNwYmH3AY&t=152s).
- **Obsidian's role.** Nate says it only renders markdown [02:12](https://www.youtube.com/watch?v=sboNwYmH3AY&t=132s).
- **No fancy RAG needed.** Karpathy expected to need it, but LLM-maintained index files and short summaries were enough at small scale [02:43](https://www.youtube.com/watch?v=sboNwYmH3AY&t=163s).
- **Scale.** Nate says "half a million words" [02:55](https://www.youtube.com/watch?v=sboNwYmH3AY&t=175s). The post says about 400K (see Beyond the source).
- **Gaps.** The agent can spot gaps in a topic and research to fill them [03:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=190s).

### [03:12](https://www.youtube.com/watch?v=sboNwYmH3AY&t=192s) Why It Matters & How It Works

- **Why:** chats forget; a wiki compounds [03:17](https://www.youtube.com/watch?v=sboNwYmH3AY&t=197s). No vector database or embeddings, just markdown in a folder [03:38](https://www.youtube.com/watch?v=sboNwYmH3AY&t=218s).
- **Layout:** raw/ holds your material. wiki/ holds pages the LLM writes, plus an index and a log [03:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=224s).
- **The log** records each operation. After the first big batch, every new video is a one-line ingest request [04:27](https://www.youtube.com/watch?v=sboNwYmH3AY&t=267s).
- **CLAUDE.md** explains how the project works, how to search it and how to update it [04:43](https://www.youtube.com/watch?v=sboNwYmH3AY&t=283s).
- **Token claim:** an unnamed X user turned 383 files and 100+ meeting transcripts into a wiki and reportedly cut query tokens by 95% [04:53](https://www.youtube.com/watch?v=sboNwYmH3AY&t=293s).
- **Kept vague on purpose.** Karpathy left the idea loose so you can adapt it, and Nate's two vaults came out differently [05:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=326s).

### [05:39](https://www.youtube.com/watch?v=sboNwYmH3AY&t=339s) Setting Up Obsidian & Claude Code

1. **Optional:** install Obsidian (free) [06:01](https://www.youtube.com/watch?v=sboNwYmH3AY&t=361s). Then Manage Vaults → create "demo vault" [06:30](https://www.youtube.com/watch?v=sboNwYmH3AY&t=390s).
2. **Open the folder** where you run Claude Code (he uses VS Code). It holds only .obsidian and welcome.md [06:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=404s).
3. **Run claude in the terminal.** He prefers it for the status line [06:56](https://www.youtube.com/watch?v=sboNwYmH3AY&t=416s).
4. **Paste the entire gist** [07:12](https://www.youtube.com/watch?v=sboNwYmH3AY&t=432s).
5. **Add a wrapper prompt** before sending. It makes Claude his LLM Wiki agent, tells it to implement the idea file as his second brain, guide him step by step and create the CLAUDE.md schema. The rest of the wrapper is on screen only [07:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=446s).
6. **Check the scaffold.** Claude creates raw/ and wiki/ with four default subfolders; revisit those once content arrives [07:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=474s). It reports CLAUDE.md, index and log, and asks for a first source in raw/ [08:24](https://www.youtube.com/watch?v=sboNwYmH3AY&t=504s).

- **Flat vs nested.** His personal wiki is flat, which he says Karpathy sometimes prefers [08:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=490s). Subfolders suit the YouTube wiki better [08:19](https://www.youtube.com/watch?v=sboNwYmH3AY&t=499s).

### [08:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=515s) Ingesting Your First Article

- **Capture.** A copy-paste can come through messy [08:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=524s), so use the Obsidian Web Clipper extension [08:56](https://www.youtube.com/watch?v=sboNwYmH3AY&t=536s):
  - Set the folder to raw and click Add to Obsidian [09:07](https://www.youtube.com/watch?v=sboNwYmH3AY&t=547s). The note arrives with only a title and source [09:18](https://www.youtube.com/watch?v=sboNwYmH3AY&t=558s).
  - In the extension's options, change Location from "Clippings" to raw [10:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=613s).
- **Prompt (paraphrased).** Say the AI 2027 article is now in raw and ask Claude to ingest it [09:27](https://www.youtube.com/watch?v=sboNwYmH3AY&t=567s).
- **Page count.** The agent writes 5, 10 or more linked pages, not one file [10:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=602s).
- **Questions before writing.** Claude returns key takeaways and asks about emphasis, focus, granularity and plan [10:29](https://www.youtube.com/watch?v=sboNwYmH3AY&t=629s). His answer: be extremely thorough; this vault is his AI-research dump, so keep it queryable and connected [10:41](https://www.youtube.com/watch?v=sboNwYmH3AY&t=641s).
- **Live graph.** The graph view fills as Claude writes about 25 planned pages [11:20](https://www.youtube.com/watch?v=sboNwYmH3AY&t=680s). One hub gathers people (Eli, Thomas, Daniel) and links to AI governance, OpenBrain and superhuman coder [11:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=695s).
- **Result: 23 pages.** Source, 6 people, 5 organisations, 1 AI-systems page, technical/alignment/geopolitical concept pages and an analysis. Follow-up questions come after [11:59](https://www.youtube.com/watch?v=sboNwYmH3AY&t=719s).
- **Click-through.** Source → OpenAI → model spec → an LLM-psychology page, all from one article [12:37](https://www.youtube.com/watch?v=sboNwYmH3AY&t=757s).

### [13:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=782s) Querying & Connecting Projects

- **Query in place, or from another project.** Point it at the folder; it reads the index and the vault's CLAUDE.md [13:23](https://www.youtube.com/watch?v=sboNwYmH3AY&t=803s).
- **Herk2's wiki path.** For facts about him or the business it doesn't already have, Herk2 goes to the Herk Brain vault and reads, in order, the hot cache, the index and the domain sub-index, or searches [13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s). It lists tasks that don't need the wiki [14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s).
- **Token saving.** Replacing Herk2's in-project context files with the wiki cut tokens, though he gives no numbers [14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s).
- **hot.md.** Roughly 500 words or characters (he's unsure which) of the latest input or discussion. It spares the assistant from crawling pages [14:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=884s).
- **Lint (Karpathy's health checks).** Find inconsistent data, fill gaps with web searches, suggest new article candidates [15:06](https://www.youtube.com/watch?v=sboNwYmH3AY&t=906s). Run daily or weekly [15:19](https://www.youtube.com/watch?v=sboNwYmH3AY&t=919s). It may ask you for more info or articles [15:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=925s).

### [15:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=936s) LLM Wiki vs Traditional RAG

- **Does it kill semantic RAG?** "No, but kind of yes." It depends on the goal and how much context you have [15:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=936s).
- **The chart.** Claude made it inside Herk Brain, from his notes on Karpathy's idea [15:45](https://www.youtube.com/watch?v=sboNwYmH3AY&t=945s):

| Axis | LLM Wiki | Semantic-search RAG |
|---|---|---|
| Retrieval | Reads indexes, follows real links [16:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=973s) | Similarity search over chunks |
| Infrastructure | Markdown only; Obsidian optional [16:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=985s) | Embedding model, vector DB, chunking pipeline |
| Cost | Tokens only [16:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=996s) | Ongoing compute and storage |
| Maintenance | Lint, clean up, add articles [16:42](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1002s) | Re-embed on change |
| Fits | Hundreds of well-indexed pages [17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s) | Millions of documents |

- **The wiki's weakness.** It doesn't scale to enterprise size, where semantic search, a knowledge graph or [[LightRAG]] become cheaper [16:51](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1011s).

### [17:20](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1040s) Final Thoughts

- He points to his executive-assistant video [17:32](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1052s).

## Caveats & disagreements

- **Hype and unmeasured claims.**
  - "5 minutes" covers only the scaffold; the first ingest took about 10 minutes.
  - He repeats praise from X without evidence [03:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=205s).
  - The 95% token cut is secondhand, and the Herk2 saving comes with no numbers. Treat both as hypotheses.
- **Misquotes and unverified attributions.**
  - Karpathy's post says about 400K words, not half a million (see Beyond the source).
  - "Karpathy likes it flat" appears in neither the post nor the gist. The tree in [[Ingest Sources into an LLM Wiki]] assumes subfolders, so read "flat" as Nate's own experience.
- **Thin spots.**
  - hot.md: he's unsure of its size and never shows how it gets updated. It isn't in the gist.
  - The chart is Claude summarising his notes, not research, and "millions of documents" is vague.
  - The wrapper prompt, Herk2's wiki-path wording and the full chart are mostly on screen only.
  - Querying, lint and cross-project reads are described, not demonstrated.
- **Versus his June video, [[Nate Herk - Every Level of a Claude Second Brain]]:**
  - **Where the wiki lives.** Here, Herk Brain is a separate vault that Herk2 points at. In June, the transcript wiki sits inside Herk2 ([09:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=560s)).
  - **Obsidian.** Here he watches the graph to judge hubs [11:06](https://www.youtube.com/watch?v=sboNwYmH3AY&t=666s). In June he rarely opens Obsidian ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).
  - **Scale.** June says only that wikis degrade at some point ([11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s)). This video gives a scale boundary.
  - **Live data.** Here ClickUp summaries go into the brain. June says live data stays in its own system ([27:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1657s)); summaries may count as distilled context. See [[Context vs Connections]].
- **Versus [[LLM Wiki]].** That note's lint summary and paste-the-gist route draw on this video; its "no lint" remark applies only to the June video.
- **Batch then single ingests.** Nate batches first, then ingests one source at a time [04:27](https://www.youtube.com/watch?v=sboNwYmH3AY&t=267s). That fits the gist, which prefers one at a time but allows batches (see Beyond the source).
- **Other creators.**
  - [[Chase AI - The Agentic OS Setup for Claude Code]] designs raw/wiki/outputs with an index per folder. Nate uses the gist's single index plus a log.
  - [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] runs the same gist bootstrap in [[OpenAI Codex]] and prunes an over-built result.
  - [[Build a Level 1 Second Brain]] teaches the context files Nate moved beyond. It's an earlier stage, not a contradiction.
- **Links in the description.** It carries community funnels and affiliate links; none are part of the method.

## Build from this

1. **Gist bootstrap.** Give Claude Code, in an empty vault, the gist, a wrapper prompt and the vault's purpose. Review what it generates. See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
2. **Clip-to-ingest loop.** Set Web Clipper's Location to raw. Answer the emphasis and granularity questions, and log each run. See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
3. **Router block for an external vault.** Write the vault path, read order (hot.md → index → sub-index → search) and a "tasks that don't need the wiki" list. Measure tokens before and after. See [[Tiered Lookup Routing]].
4. **Hot cache.** Keep a short hot.md of recent inputs, read first. Decide who rewrites it and when. See [[Agent Memory Patterns]].
5. **Scale tripwire.** Past a few hundred pages, or once the index no longer fits in one read, add search to that folder only. See [[Add Semantic Search to One Folder]].
6. **Journal and CRM.** Layer them on a working wiki. See [[Add a Journal and Personal CRM to a Second Brain]].

## Resources mentioned

- Karpathy's LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f [05:39](https://www.youtube.com/watch?v=sboNwYmH3AY&t=339s)
- Karpathy's "LLM Knowledge Bases" X post: https://x.com/karpathy/status/2039805659525644595 [01:41](https://www.youtube.com/watch?v=sboNwYmH3AY&t=101s)
- Obsidian: https://obsidian.md · Obsidian Web Clipper extension [08:56](https://www.youtube.com/watch?v=sboNwYmH3AY&t=536s)
- AI 2027 (demo article): https://ai-2027.com/
- His executive-assistant video (not linked in the captions)

## Beyond the source

*Not said in the video. Verified 2026-09-15.*

- **Karpathy's post (2 April 2026)** — [X post](https://x.com/karpathy/status/2039805659525644595), via [FxTwitter](https://api.fxtwitter.com/karpathy/status/2039805659525644595):
  - Says about 100 articles and about 400K words.
  - Uses Obsidian Web Clipper for capture.
  - Files query outputs back into the wiki.
  - Its lint list matches Nate's. Nothing on flat vs nested folders.
- **The gist**, first published 4 April 2026 — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [revisions](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/revisions):
  - Index-first works at roughly 100 sources and hundreds of pages. Add search as the wiki grows; it suggests qmd.
  - Its sample ingest talks through key takeaways with you before writing, and one source might touch 10–15 pages. It prefers one source at a time but allows batch ingest.
  - It calls itself intentionally abstract and leaves directory structure to you. It says nothing about flat vs nested, and has no hot cache.
  - Its lint list also covers orphan pages and stale claims.
- **Web Clipper default folder.** Its default template saves to "Clippings". — [obsidian-clipper source](https://github.com/obsidianmd/obsidian-clipper/blob/main/src/managers/template-manager.ts)
- **The 95% figure** appears, unattributed, in a May 2026 (post-video) [MindStudio post](https://www.mindstudio.ai/blog/karpathy-llm-wiki-pattern-cut-claude-token-usage-95-percent); no primary source was found *(unverified)*.
- **AI 2027** is by Daniel Kokotajlo, Eli Lifland, Thomas Larsen and Romeo Dean; OpenBrain is its fictional AI company. — [about page](https://ai-2027.com/about)
- **This vault uses the same pattern** (see [[LLM Wiki]]):
  - Sources/Concepts/Techniques are the wiki.
  - Home.md is the index; Ingest Log.md is the log; CLAUDE.md is the schema.
  - `.tools/check_links.py` is a partial lint.

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Cloud Code", "claw.md", "Andre Karpathy" | Claude Code, CLAUDE.md, Andrej Karpathy |
| "hot cash", "pre-wreck", "Up-to-AI" | hot cache (hot.md), prereq, Uppit AI |
| "Herc Brain", "Herc 2" | Herk Brain (personal wiki vault), Herk2 (assistant project); spellings likely |
| "N and" (00:41), "light rag", "click-up" | n8n (likely), LightRAG, ClickUp |
| "open brain"; "Eli, Thomas, Daniel" (11:35) | OpenBrain, the fictional company in AI 2027; likely authors Eli Lifland, Thomas Larsen, Daniel Kokotajlo |
| "half a million words" (02:55) | Nate's misstatement; post says ~400K |
| "wiki graph" (17:10) | probably "the wiki" approach (*unclear in captions*) |
| Terminal vs VS Code sentence (06:56) | self-contradictory; most likely the CLI in VS Code's terminal (*unclear*) |
| "LLM psychology model" (12:55) | demo page title; exact name *unclear in captions* |

## Related

- **Concepts:** [[LLM Wiki]] · [[Agent Memory Patterns]] · [[CLAUDE.md as a Router]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Second Brain Levels]] · [[Design for Retrieval]] · [[Context vs Connections]]
- **Techniques:** [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Ingest Sources into an LLM Wiki]] · [[Tiered Lookup Routing]] · [[Add Semantic Search to One Folder]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Build a Level 1 Second Brain]]
- **Tools and people:** [[Claude Code]] · [[Obsidian]] · [[OpenAI Codex]] · [[LightRAG]] · [[Nate Herk]] · [[Andrej Karpathy]] · [[Chase AI]] · [[Matt Wolfe]]
- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Chase AI - The Three-Step Claude Code Agentic OS]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]
