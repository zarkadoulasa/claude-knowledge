---
type: source
title: "Every Level of a Claude Second Brain Explained"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=DTCyvo6cC54
video_id: DTCyvo6cC54
published: 2026-06-17
duration: "30:59"
ingested: 2026-09-15
topics: [second brain, memory, retrieval, RAG, knowledge graphs, portability, privacy, teams]
tags: [source/youtube, topic/second-brain, topic/memory, topic/retrieval, topic/rag, topic/knowledge-graph, topic/claude-code, topic/skills, topic/agents, topic/privacy, topic/portability, topic/teams]
---

# Nate Herk - Every Level of a Claude Second Brain

> **Creator:** [[Nate Herk]] · **Published:** 2026-06-17 · **Length:** 30:59 · [Watch on YouTube](https://www.youtube.com/watch?v=DTCyvo6cC54)

## TL;DR

Nate Herk breaks an AI second brain in [[Claude Code]] into five levels: (1) a CLAUDE.md router over plain folders, (2) an LLM Wiki, (3) semantic/vector search, (4) a knowledge graph of typed relationships, and (5) an always-on, self-syncing brain OS such as [[GBrain]], illustrated with his real Herk2 project and an example project with a folder for each of Levels 1–4. His two core rules are to decide how knowledge goes in by working backwards from the questions you'll ask, and to pick the lowest level that fixes a pain you actually feel. Every step up has a cost: vector chunks lose whole-document context, graphs are complex and can be expensive, and always-on systems risk flooding the brain with context. You can mix levels folder by folder, and he admits almost all of Herk2 sits at Level 2. Along the way he adds a "context vs connections" filter for what to ingest, a tiered lookup for live data, a warning that data processed through Claude goes to Anthropic, and the view that team brains are mostly a change-management problem.

## Key takeaways

- **Design for retrieval, not storage.** Work out how a piece of knowledge will be asked for, then shape how it goes in. His analogy: nobody would make a basketball square when the hoop is round. [02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s), [02:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=166s). See [[Design for Retrieval]].
- **One test for any second brain:** can your agent find it again, and can you? If not, your routing or folder architecture is what's missing. [02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s), [02:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=139s)
- **Pick the lowest level that fixes a pain you actually feel.** Level 5 isn't "best", and if nothing hurts there's no reason to build more architecture. [03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s), [04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s). See [[Second Brain Levels]].
- **CLAUDE.md is a router, not only a system prompt.** It needs explicit "for X, look in folder Y" rules. Claude won't search the whole project on its own, and you wouldn't want to pay the time and token cost if it did. [04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s), [04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s), [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s). See [[CLAUDE.md as a Router]].
- **Nobody has proven a best folder structure yet.** Copying his layout, or anyone else's, misses the point. What matters is routing that makes sense to both you and the AI. [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s), [07:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=422s)
- **Mix levels inside one brain.** Keep context, projects and decisions as markdown, and turn only the folder that needs it (for example, YouTube transcripts) into a vector index or graph. [17:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1060s), [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s), [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)
- **Vector search is not magic.** An agent that only retrieves chunks can miss key parts of a meeting when summarising it, or report the wrong maximum from a table. Have the agent read the full markdown file for whole-document questions, and use vectors for needle-in-a-haystack lookups like "rule 17 of 1,000". [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s), [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s). See [[Keyword vs Semantic vs Graph Retrieval]].
- **Wiki links are not a knowledge graph.** Wiki links work like "see also" backlinks. A graph stores typed relations such as "works at" or "competitor of". [12:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=763s), [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s), [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s). See [[Knowledge Graphs]].
- **The bottleneck may be getting knowledge in, not retrieving it.** Retrieval is sometimes at fault, but sometimes the bigger problem is getting what's in your head into the system at all. Before blaming the AI, check whether your files actually hold that nuance. He uses a Grill Me interview skill to pull it out. [22:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1342s), [22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s), [20:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1258s). See [[Grill Me Interview Skill]].
- **Ingest context; keep connections reachable.** Evergreen knowledge such as decisions and quarterly projects goes into the brain. Data that changes (Slack, email, customer records) stays in its own system, but the brain can reach it. His test: will this still be useful a year from now? [26:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1606s), [27:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1647s), [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s), [28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s). See [[Context vs Connections]].
- **Keep it tool-agnostic.** The brain is just files, so the same one works in [[OpenAI Codex]] and [[Hermes Agent]]. Mirror CLAUDE.md as AGENTS.md and point other agents at the memory file. [01:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=107s), [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s), [11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s). See [[Tool-Agnostic Context Files]].
- **Privacy and teams.** Anything you process through Claude goes to Anthropic, so sensitive or client data may belong with open-source models. A team brain is mainly an adoption problem, and you should solve it only after your personal brain works. [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s), [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s), [30:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1834s)

## The five levels at a glance

| Level | Question it answers | What you add | Strengths | Weaknesses / failure modes | Move up when… |
|---|---|---|---|---|---|
| **1 — Router** · [[CLAUDE.md as a Router]] | Can you find a file or fact by an exact word or name? [03:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=207s) | CLAUDE.md (or AGENTS.md) with routing rules, plus plain folders: context, projects, decision log [04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s), [05:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=355s) | You stop re-explaining, and the agent knows where to look and why [05:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=316s). You can drill down by hand too [07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s) | Gets messy and starts being ignored as it grows; lookups tend to rely on exact words [05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s) | Start here if you keep re-explaining your setup [28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s). Move to Level 2 when you have 30+ notes and keep forgetting what's in them [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s) |
| **2 — LLM Wiki** · [[LLM Wiki]] | Can you pull everything on a topic together? [03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s) | Index-driven wikis per body of material (transcripts, meetings), a references folder, and a memory file / [[Claude Code Auto Memory]] [10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s), [10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s) | Claude builds the pages when it ingests a source [09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s); indexes let it drill down [11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s); good enough for his whole Herk2 project [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s) | Degrades at scale [11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s); links are backlinks, not typed relations [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s); has to read whole pages [24:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1447s) | The brain keeps missing notes you know exist and routing isn't working [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s) |
| **3 — Semantic search** · [[Semantic Search]] | You search with different words than you wrote: meaning, not exact match [03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s) | Embeddings-based search, however you get it (he names Obsidian, Pinecone and Supabase and demos [[Qdrant]]), often for just one folder [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s), [17:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1060s) | Matches by meaning ("feedback" finds test results) [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s); cheap needle-in-a-haystack lookups [18:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1117s) | Chunks miss whole-document context (meeting summaries, max-of-table) [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s); not magic [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s) | You need relationships and to follow chains of questions [29:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1762s) |
| **4 — Knowledge graph** · [[Knowledge Graphs]] | Can you trace relationship chains, following topic X back to topic A? [03:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=221s) | A graph layer of entities and typed relationships next to the wiki, e.g. [[LightRAG]] [23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s), [24:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1458s) | Explicit typed links you can follow [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s); lighter than reading whole pages [24:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1453s) | Most complex and sometimes most expensive [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s); the software builds relationships well, but you have to feed it enough data [20:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1230s) | You run agents unattended (captioned "offline") on lots of data and want several Hermes agents synced [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s) |
| **5 — Always-on brain OS** · [[Always-On Brain OS]] | Can the whole thing run autonomously so you don't have to think about it? [03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s) | A continuously syncing system such as [[GBrain]] (wikis, routing, relationships, tools) plus scheduled jobs [25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s), [25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s) | Constantly syncs, refreshes memories and adds new material [25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s); pairs well with Hermes Agent [25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s) | Risks too much context doing more harm than good, and you lose control over what goes in [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s); in Claude Code you have to manage the crons yourself [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s) | Top level. He doesn't run it himself yet [25:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1558s) |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=0s) Intro

- He opens on three visuals of increasingly structured data. First, context starts forming into nodes and entities [00:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=4s). With more knowledge and relationships, distinct clusters appear [00:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=21s). The last is a full relationship map showing how everything fits together, rather than files that merely link to each other [00:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=34s).
- Why second brains took off: people want to get knowledge out of their heads and into systems, and that data, your IP, is your moat [00:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=47s).
- The hard part is organising it so it works across many AI models and recalls sensibly, instead of hallucinating or burning time and tokens searching everything [00:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=57s).
- The visuals come from his real project, Herk2. Underneath, it's just folders of markdown organised so that both he and his agents understand them [01:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=65s).
- He also uses a separate example project to show what each level looks like if you're starting from scratch or sitting between Levels 2 and 3 [01:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=79s).
- It's framed around Claude Code, but it works with any model [01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s). He uses the same brain with Codex and Hermes Agent [01:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=107s), which works because it's only files and folders [01:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=112s).
- **The job of a second brain**, as he sees it: a place to drop notes, meeting recordings, ClickUp threads and the like [02:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=122s). It then helps him ingest that material into the right places so it can be found later [02:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=126s).
- **The test:** can the agent find it again, and could you [02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)? If not, the routing or folder architecture is missing [02:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=139s).
- **Work backwards from the question.** How data will be accessed and recalled should decide how it goes in [02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s). His basketball analogy: you know the hoop's shape, so you'd never design the ball as a giant square [02:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=166s), [02:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=174s). Start with the end in mind [03:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=180s).
- The end goal is a brain that knows your business, you and your relationships, and recalls things better and faster than you can [03:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=186s), [03:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=196s).

### [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s) The 5 Levels Overview

- Each level answers a different question:
  - **Level 1:** can you find a file or fact by an exact word or name? [03:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=207s)
  - **Level 2:** can you pull everything on one topic together? [03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)
  - **Level 3:** you search with different words than you wrote, so it has to search by meaning rather than exact match (semantic search) [03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)
  - **Level 4:** can you trace relationship chains, asking about topic X and following it back to topic A? [03:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=221s)
  - **Level 5:** make the whole brain autonomous so you don't have to think about it [03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s)
- This isn't a ranking with 5 as best. He has reasons for not sitting at Level 5 himself [03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s).
- The aim is the simplest, lowest level that meets your needs [04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s). If there's no pain point, there's no need to experiment with new architecture [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s), [04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s).

### [04:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=259s) Level 1

- Level 1 is simple and it's where everyone starts. You begin with a CLAUDE.md, or an AGENTS.md if you use Codex [04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s), [04:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=266s).
- CLAUDE.md loads at the start of each session and acts almost like the system prompt for that project [04:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=271s).
- **The key idea is to treat CLAUDE.md as a router** [04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s). Besides the role and what matters, it holds routing rules [04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s). Examples: personal information about him lives in one folder [04:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=285s), and Q1 priorities live in another [04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s).
- A sign routing is missing: Claude asks you for more information even though you know it's in the project's files [04:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=294s). That means you never told it to look there [04:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=297s).
- Claude won't search the entire project automatically, and you wouldn't want it to because of the time and token cost [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s). If it doesn't know something exists somewhere, it probably won't find it [05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s).
- The payoff: once routing is set up properly, you stop re-explaining things, and it knows where to look and why [05:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=316s).
- The downsides: once the file grows too big it gets messy and starts to feel ignored [05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s). Lookups also tend to rely on exact words, depending on how you route [05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s).
- **Demo: the example Level 1 folder** (imagine it as its own Claude project) [05:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=335s).
  - Its CLAUDE.md explains that it auto-loads whenever Claude Code opens in the folder, and gives the AI your identity, working style and a map of where everything is kept [05:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=341s). At this level, that file plus a few folders is the entire second brain [05:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=349s).
  - The "where things live" section is very short. It lists a **context** folder of always-true background to read first [05:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=355s), then **projects** and a **decision log** [05:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=359s).
  - The context folder holds an about-me file you can grow over time [06:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=364s), a stack file, and a second file captioned "conversations" (possibly "conventions"; *unclear in captions*) [06:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=366s).
  - The decision log holds dated decisions, and you can have CLAUDE.md instruct Claude to append a new entry whenever you make a big change to the project, your life or your business [06:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=370s).
  - Projects can be one markdown file or one subfolder per ongoing project or client, organised however you like [06:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=385s). You can also organise by date, e.g. a May folder and a June folder [06:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=395s).
- **No proven standard exists.** It's a question he answers a lot in his community and in comments. Beyond common elements like a context folder and CLAUDE.md, nobody has proven a best way to structure a second brain yet [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s). Don't treat his layout, or any creator's, as the only right way [06:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=417s).
- What matters is proper routing that makes sense both to you and to your AI [07:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=422s).
- **Demo: drilling down in Herk2 without AI** [07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s).
  - He knows his base folders and the drill-down paths [07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s), so finding the HTML slide deck from his "ranking Claude Code features" video is easy [07:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=441s).
  - The path is projects → YouTube videos → a folder for the May 30 "Claude Code top 50 features" video → the tier-list deck, which opens as the slide deck [07:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=447s).
  - Because the structure makes sense and there are routing rules, his agent finds it just as easily [07:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=466s).

### [08:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=491s) Level 2

- Level 2 brings in the **LLM Wiki**, [[Andrej Karpathy]]'s pattern, which Herk has set up for several bodies of material [08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s). He made a separate full video on it [08:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=500s), most likely [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (published 2026-04-05).
- It fits once you have more files that take a different shape and need grouping in a different way [08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s), for example researching everything on one project [08:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=512s). In his setup, all YouTube transcripts live in one wiki and all meeting transcripts in another [08:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=520s).
- **Demo: [[Obsidian]] view of his YouTube-transcripts wiki** [08:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=523s).
  - It has concept pages such as agentic workflows, AI coding market and context window [08:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=529s), which link to related tools, concepts and videos.
  - It also has sections for sources, platforms and context-management techniques [08:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=539s).
  - All of it was created automatically by Claude Code whenever he told it to ingest a transcript into the wiki [09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s).
- This transcript wiki lives inside the main Herk2 project [09:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=560s). The path is a folder captioned "Other Worlds" (*unclear in captions*) → YouTube OS → transcript wiki [09:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=562s), with the same concepts, comparisons, sources and techniques folders seen in Obsidian.
- **Obsidian is only a viewer.** All it does is visualise the markdown files [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s).
  - People get infatuated with the graph view, which is why he opened the video with it [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s). What matters is whether your system can fetch the information and give it to you [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s).
  - If you're a visual person, installing Obsidian is easy [10:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=606s). If the visual layer doesn't help you, skip it. He rarely opens Obsidian, because he knows his brain and OS can find everything [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s).
- **Demo: the example Level 2 folder** has the same shape as Level 1 and builds on top of it [10:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=621s).
  - CLAUDE.md now routes to the wiki as well as to context, projects and decisions. It also routes to a references folder and a memory.md [10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s). In other words, Level 2 mostly means more routing rules [10:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=639s).
  - Context, decisions, projects and references all keep growing, and the idea of memory comes in [10:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=641s).
- **Auto memory:** once Claude Code's auto memory is switched on, Claude maintains and updates that memory file without you doing anything [10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s). The /memory command shows whether auto memory is on or off and lets you switch it on [10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s). See [[Claude Code Auto Memory]].
- **Portability catch:** he wants brains to be tool-agnostic [11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s), but CLAUDE.md and the self-updating memory file are specific to Claude Code [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s).
- **Moving to Codex:**
  - Copy CLAUDE.md into a file called AGENTS.md [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s). Herk2 keeps both side by side as essentially identical files, so each tool reads its own [11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s).
  - For memory, make sure the memory.md file exists and tell Codex to look there for memories [11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s), [11:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=701s). It all comes down to routing. See [[Port a Claude Code Brain to Other Agents]].
- **Limits of wikis:**
  - Past a certain size, wikis start to degrade [11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s).
  - Their strength is the index [11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s). Asked about agentic workflows, the AI starts at that page and drills down [11:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=718s), perhaps into a framework page (captioned "WATC"; most likely his WAT framework, not certain) [12:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=727s) and then into a page about CLAUDE.md as a system prompt [12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s).
  - So there are relationships of a sort, but not semantic or knowledge-graph relationships that carry meaning [12:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=739s). It's trail-following, reading each page in full [12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s).
- **Where he actually sits:** nearly all of Herk2 lives at Level 2, because it works well for him [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s). He hasn't felt enough pain to move up. The captions say "level two" here, but from context he means Level 3 [12:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=760s).
- **Do wiki links make it a knowledge graph?** Not exactly [12:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=763s). Wiki links don't say how two things are related, e.g. "endorsed by" [12:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=769s). They behave like "see also" backlinks [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s). The effect can be similar, but they are still different.

### [13:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=783s) Level 3

- Level 3 is semantic search, however you get it: Obsidian, Pinecone, Supabase or something else [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s), [13:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=795s). See [[Semantic Search]].
- **Demo: [[Qdrant]] cluster of images** [13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s).
  - Every vector point is an image. The payload holds only metadata like file name, URL and author or artist [13:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=806s), with no description of what the image shows. So the images have to be organised by meaning, i.e. similarity.
  - In the graph view, a central psychedelic painting of owls [13:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=826s) sits next to images that share its colours and paint style: similar, but not the same.
  - Expanding further drifts into other styles, like creepy eyes and mushrooms or more fantasy-like images [14:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=846s). The graph grows away from the start as meaning diverges.
  - Qdrant just provides the visualisation on top of its clusters and vector store [14:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=855s), [14:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=858s). The point of the demo is to watch relationships form based on meaning, not keywords.
- **Demo: keyword search vs smart lookup for "feedback"** in his YouTube-transcript brain (apparently the vault he showed in Obsidian earlier; he doesn't name the search tool) [14:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=875s).
  - Regular search matches only the places where the literal word "feedback" appears.
  - The smart lookup [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s) returns notes whose meaning relates to feedback, such as live test results and a Claude Code skills note about evaluations.
  - Keyword search says X equals X; semantic search says X is similar to X, Y and Z [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s).
- **How vector databases work** (he has covered them at length on his channel):
  - Take a document, such as a transcript, and chunk it [15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s).
  - Run each chunk through an embeddings model [15:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=932s), which places it in a space where position encodes meaning. He calls it "three-dimensional", which is a simplification [15:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=936s).
  - A chunk about a company lands in one region and a chunk about finances in another [15:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=944s), so similar vectors cluster together.
- **Why designing for the question matters here** [15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s):
  - **March 5th meeting.** Say the March 5 meeting transcript is vectorised into about 20 chunks [15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s), [16:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=972s). Ask for a summary of that meeting, and the agent searches for chunks similar to "March 5th meeting summary" [16:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=984s). Even when it retrieves the right chunks, it summarises only that handful (he says five) and never sees the whole transcript, so it can miss key information [16:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=991s).
  - Metadata and similar tricks can improve results [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s). Still, the widespread assumption that a vector database always pulls back what you need is false [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s).
  - **Highest-sales table.** Asked which week had the highest sales [16:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1016s), the agent grabs one chunk of the table and concludes week 6 [17:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1024s). In fact weeks 14 and 19 were higher [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s).
  - **Rule of thumb:** when an answer needs full context, chunking won't work [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s). A plain March 5 markdown file that the agent reads end to end gives a more accurate summary [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s).
- **Demo: the example Level 3 folder** looks much like the earlier ones, still with context and decision files. You might make just one unit of your business a vector database, say YouTube transcripts, while context, projects and decisions stay as markdown [17:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1060s).
- **One brain, many styles.** A big brain doesn't have to use one style. Not everything needs GraphRAG, and not everything has to be an LLM Wiki [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s). Decide per folder, based on the type of data and how you use it [18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s).
- The example's **vector index folder** has a "how search works" note [18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s). It covers chunking, embedding, search, hybrid search and re-ranking, all areas you can go very deep on [18:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1098s).
- **Where vectors shine:** very large amounts of text, when you need one specific, similar answer [18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s). Example: store 1,000 rules and ask what rule 17 was [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s). Vector search pulls just that snippet [18:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1117s), instead of spending time and tokens reading the whole 1,000-rule file [18:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1129s).
- **Not sure which to use? Ask your agent.** Describe the data and how you'll use it to your Claude Code agent, and ask whether markdown files or semantic search fits better. It will walk you through the setup [19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s).
- Moving up or down a level isn't automatically better. Identify the pain point in your current setup and where a different level would fix it [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s), [19:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1161s).

### [19:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1167s) Level 4

- Level 4 is knowledge graphs and relationship graphs [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s). They're usually the most complex option, and sometimes the most expensive if you run them on a paid platform [19:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1175s). Open-source software is an alternative [19:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1178s). See [[Knowledge Graphs]].
- **His disclosure:** he has experimented a lot but doesn't use graphs day to day, because routing files and wikis cover his needs [19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s). His work is project-based and content-heavy with no massive CRM of businesses and clients [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s). If he had one, a knowledge graph would probably make sense [20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s).
- If you decide you need a graph, say for all your projects, the data probably already exists in your folders [20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s). Graph software is usually good at building the relationships. The problem you have to solve is feeding it enough data [20:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1230s). See [[Build a Knowledge Graph Layer]].
- **Grill Me brainstorm sessions:**
  - To get that data out of his head, he runs brainstorm sessions with a skill called **Grill Me** [20:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1233s). It originally came from [[Matt Pocock]], and Herk customised it [20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s).
  - His version is in his free Skool community: Classroom → all YouTube resources [20:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1249s).
  - The skill interviews him relentlessly about a topic [20:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1258s) and writes a brainstorm file. It stops only once it knows everything about the topic [21:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1260s).
  - To seed a graph of clients and businesses, run it once per entity: grill me about client A, client B, business A [21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s). Along the way you can feed it files, transcripts and contracts [21:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1276s). See [[Grill Me Interview Skill]].
- **Privacy aside** (added while editing) [21:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1282s):
  - Data you send through Claude models goes to Anthropic, so it isn't private [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s).
  - He's comfortable putting his own business data in. If you aren't, or you're dealing with client data, consider open-source models [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s). Claude Code may not be the place for a brain holding everything about you and your clients.
  - He's aware his data goes to Anthropic when he processes it through Claude [22:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1321s), and says you should be aware of it too. He plans upcoming videos on local AI and open-source models [22:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1331s).
- **The common misconception** [22:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1342s) is that poor retrieval is the problem. Sometimes it is, but sometimes the bigger problem is getting what's in your head into the system at all. Before blaming the AI, ask whether your folders are holistic [22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s) and capture the nuance you carry in your head [22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s).
- **Demo: the example Level 4 folder** keeps the same shape, with a few additions:
  - An AGENTS.md identical to CLAUDE.md. He notes you can simply reference @AGENTS.md inside CLAUDE.md and delete the duplicated content [22:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1379s), because the reference effectively injects that file [23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s).
  - A wiki plus a new **knowledge graph layer** [23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s). The same routing sits over ordinary folders and plain markdown. His phrase: "boring is beautiful" [23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s).
  - The memory file is still there and still growing [23:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1399s). Each level just builds on the last.
- **Demo: the knowledge-graph folder** [23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s):
  - Entities have types, e.g. Jordan is a person and Acme is a company [23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s).
  - Relationships connect them: Jordan works at Acme [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s), Acme is endorsed by Postpilot, and Postpilot is a competitor of Cadently [23:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1418s), [23:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1420s).
  - So the graph records both the entities and how they're related. These are fictional demo entities.
- **Why his wiki is enough for him:** he gets enough of that relationship feel from his LLM Wiki because he has put a lot of effort into ingesting sources properly, with context [23:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1438s).
- **Where graphs are lighter:** a wiki forces the agent to read every file it wants in full. If it only needed the ElevenLabs detail inside an AI-video-production page, it would still read the whole page [24:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1447s). In that sense a knowledge graph can be more lightweight [24:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1453s).
- **Demo: [[LightRAG]] graph of his real business**, the graph from the intro [24:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1458s):
  - It's essentially his entire second brain and business, so parts are blurred [24:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1463s). There's so much data that zooming in slows his computer.
  - The edges carry named relationships such as "collaborates with" and "builds" [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s).
  - Expanding a node shows, for example, that the 7-day AI challenge [24:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1486s) came from YouTube, connects to the AIS Plus onboarding process [24:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1492s), and was developed by Aiden [24:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1494s). You can keep following relationships from node to node.
  - It's roughly the same data as his Obsidian wiki, but Obsidian doesn't give that level of relationship between entities [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s).
- He invites requests for a full breakdown of graph tools like Logseq, Graphiti (*uncertain; captioned "Graphir"*) and others [25:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1508s).
- **Bottom line:** if you don't need relationship chains or meaning-level relationships, you probably don't need a knowledge graph [25:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1519s).

### [25:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1525s) Level 5

- Level 5 is an **always-on brain OS**, for example [[GBrain]], created by [[Garry Tan]], CEO of Y Combinator [25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s). It pairs well with gstack [25:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1535s). See [[Always-On Brain OS]].
- GBrain combines everything covered so far: wikis, routing, relationships and tools. What it adds is the always-on element: it's constantly syncing, refreshing memories and adding new material [25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s).
- GBrain on something like a Hermes Agent would work really well [25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s). You could do it in Claude Code, but you'd have to set up and manage the crons yourself [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s). That's why he doesn't run GBrain yet, though he's experimenting with it on his Hermes agent [25:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1558s).
- In short, it's the same ideas as the earlier levels with an auto-updating, autonomous, always-on feel [26:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1562s).
- **What worries him about it:**
  - He isn't sure where "too much context" begins [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), i.e. the point where the brain does more harm than good [26:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1580s).
  - Today he's in complete control of what his brain ingests [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s). He runs a skill to collect the week's meeting transcripts [26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s), or hands the brain something, works out with it where it belongs, and then they ingest it together (this part is garbled in the captions) [26:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1595s). He likes that control.
- **The four C's.** From his AI OS videos: context, connections, capabilities and cadence [26:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1606s). For a second brain he mainly thinks about the first two, context and connections. See [[Context vs Connections]].
- **Context = what the business has done, locked in.**
  - Demo: his quarterly project files, captioned "OTAs" (*exact term unclear in captions*) [27:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1621s).
  - He can open the Q1 set to see decisions and statuses [27:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1625s), and the Q2 set as well [27:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1631s).
  - These are locked-in decisions about what they're doing that quarter, and he keeps the statuses updated [27:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1636s). His brain can see all of it.
- **Connections = live data that isn't evergreen** [27:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1647s): Slack threads, emails, customer data [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s).
  - Don't ingest this into the brain. It turns into noise, and you'd have to go back every month to delete old material [27:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1657s).
- **His ingest filter:** the brain holds things he won't delete [27:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1665s). The test is whether having this memory will still help a year from now; if not, it's noise [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s), [27:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1671s).
- So when adding data, ask whether it's evergreen, holistic context [27:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1678s) or something that will change next week. For the latter, don't pull it in, but make sure the brain has access to go and fetch it [28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s).
- **Demo: tiered lookup.** He asks what John and he discussed last week about quarterly project ("OTA") number seven [28:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1693s). The brain works through three tiers:
  1. It checks the quarterly project file first.
  2. If the answer isn't there, it searches the wiki and meeting transcripts.
  3. If it still can't find it, it goes to ClickUp and pulls the live conversations between him and John [28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s).

  See [[Tiered Lookup Routing]].
- To him that still counts as a second brain. You can ask a vague question, and it knows where to look and in what order to find real-time data [28:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1717s).
- His self-check: does it understand where the data lives and where to look, and does it give accurate answers [28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s)?

### [28:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1728s) Finding Your Level

- Your whole project doesn't sit at one level. One folder might be Level 2, another Level 4, another Level 3 [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s). See [[Second Brain Pain-Point Audit]].
- **Symptom → level:**
  - You keep re-explaining your setup and need to find things by exact words or file names → **Level 1** [28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s), [29:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1740s).
  - You have 30+ notes and keep forgetting what's in them → **Level 2**: ingest them into a wiki with relationships [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s).
  - The project keeps missing notes you know exist and routing isn't working → **Level 3**, semantic search that doesn't depend on exact words [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s).
  - You want relationships and the ability to follow chains of questions and thoughts → **Level 4**, a knowledge graph [29:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1762s).
  - You run agents unattended (captioned "offline") on lots of data and want several Hermes agents synced → **Level 5**, e.g. GBrain [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s), [29:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1769s).
- **Team second brains** (touched on briefly):
  - Once you have your own brain OS, other people on your team are building theirs too [29:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1783s). That raises the question of how to sync everyone's data into a team second brain [29:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1788s).
  - There are many ways to do it, and choosing between Google Drive, Notion, GitHub or Claude plugins isn't the real issue [29:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1794s).
  - The real issue is getting the team to make the shift so the shared brain is useful rather than noise [30:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1801s). That means process owners updating and syncing their docs [30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s), and people pulling from the brain instead of pinging the same colleagues with questions [30:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1815s).
  - Adoption and change management are the bigger challenge; the technology and rollout matter less [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s).
  - The first hurdle is getting your own brain set up and understanding routing and where data should live. Only once that works for you every day can you tackle the team-wide problem [30:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1834s), [30:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1836s).

### [30:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1841s) Final Thoughts

- The skills and other resources mentioned in the video are in his free Skool community [30:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1842s), along with the slide deck used in this video [30:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1848s).

## Caveats & disagreements

- **He runs Level 2 himself.** Herk2 sits almost entirely at Level 2 [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s). He has experimented with graphs but doesn't use them daily [19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s), and doesn't run GBrain yet [25:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1558s). Beyond Level 2, most of what he shows is demos and example folders rather than daily practice. The exceptions are the smart lookup over his own transcript vault [14:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=875s) and a LightRAG graph built from his real business data [24:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1458s).
- **His situation may not match yours.** His work is project-based and content-heavy with no large CRM. He says a graph would probably make sense if he had one [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s), [20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s).
- **No proven standard structure.** His folders are one workable layout, not a best practice [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s).
- **A higher level isn't a better level.** Every level adds complexity, and the right level is set by pain, not ambition [03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s), [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s).
- **Vector databases aren't magic.** Chunk retrieval can fail on whole-document and aggregate questions. Metadata helps but doesn't remove the limit [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s), [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s).
- **Knowledge graphs cost more.** They're complex and can be expensive, and the hard part is feeding them enough data [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s), [20:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1230s).
- **Always-on risks too much context.** It trades away manual control over what gets ingested [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s). In Claude Code you'd also have to run the scheduling yourself [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s).
- **Privacy.** Data processed through Claude goes to Anthropic, so client or sensitive data may call for open-source or local models [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s).
- **Team brains are an adoption problem,** not a tooling problem [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s).
- **Reading whole files cuts both ways.** At Level 3 he recommends reading a whole markdown file for accuracy [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s). At Level 4 he calls the wiki's whole-page reads heavier than a graph lookup [24:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1447s). Read alongside his rule 17 example [18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s), the two fit together: whole-file reads suit summaries and aggregates, and targeted lookups suit specific facts. (That reconciliation is this note's, not his wording.) See [[Keyword vs Semantic vs Graph Retrieval]].
- **"Relationship" means three different things in the video.** Wiki links are backlinks; semantic neighbours are similar in meaning; graph edges are typed. He separates the first from the other two explicitly [12:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=739s), [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s).
- **The thresholds are rules of thumb.** "30+ notes", "wikis degrade at a certain point" and "too much context" come with no measurements [11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s), [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s).
- **Level 5 has no build walkthrough.** He only describes what it is and when you might want it.

## Build from this

1. **Level 1 starter brain.** Scaffold a new project with a CLAUDE.md containing a "where things live" routing section. Add `context/` (about-me, stack), `projects/` (per project or client, optionally per month) and a `decisions` log, plus a rule that Claude appends dated entries after big changes. See [[Build a Level 1 Second Brain]] and [[CLAUDE.md as a Router]].
2. **Routing gap fixer.** Collect every time Claude asked for information that already existed in the project, and turn each one into a "for X, look in folder Y" rule, until the agent stops asking. See [[Build a Level 1 Second Brain]].
3. **Cross-agent brain.** Make one instruction file work for Claude Code, Codex and Hermes Agent: AGENTS.md mirrored or imported from CLAUDE.md, plus an explicit pointer to the memory file every agent should read. See [[Port a Claude Code Brain to Other Agents]] and [[Tool-Agnostic Context Files]].
4. **Transcript and meeting LLM Wiki.** Build an ingest workflow that turns each YouTube or meeting transcript into source, concept, technique and comparison pages with an index, as in his YouTube OS transcript wiki. This vault uses the same pattern. See [[Ingest Sources into an LLM Wiki]].
5. **Tiered lookup router.** Write CLAUDE.md rules that answer "what did X and I discuss about project N?" in a fixed order: quarterly project files, then wiki and meeting transcripts, then a live ClickUp or Slack connector. See [[Tiered Lookup Routing]].
6. **Semantic search for one folder.** Put only the high-volume folder (e.g. transcripts) into a vector store such as Qdrant, and keep context, projects and decisions as markdown. Add a "how search works" note (chunking, embedding, hybrid search, re-ranking) and a rule to read whole files for summaries and aggregates. See [[Add Semantic Search to One Folder]].
7. **Knowledge graph layer.** Add an entities-and-relationships folder (person, company, typed edges like works-at or competitor-of), or run LightRAG over existing notes, built from data already in the brain. See [[Build a Knowledge Graph Layer]].
8. **Grill Me intake skill.** Create an interview skill that questions you about one client or business at a time, accepts files, transcripts and contracts, and writes a brainstorm file ready for ingest. See [[Grill Me Interview Skill]].
9. **Pain-point audit and ingest gate.** Build a skill that tests the brain with real questions and scores which ones fail and why. It then assigns each folder the lowest level that fixes the failure, and applies the context-vs-connections "useful in a year?" filter before anything is ingested. See [[Second Brain Pain-Point Audit]] and [[Context vs Connections]].

## Resources mentioned

- **His free Skool community** (AI Automation Society): https://www.skool.com/ai-automation-society/about
  - Hosts his customised Grill Me skill under Classroom → all YouTube resources [20:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1249s), the other skills mentioned, and the slide deck for this video [30:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1842s), [30:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1848s).
  - He says all the skills and everything else you need are there. The example project (he shows folders for Levels 1–4) is probably included, but he never says so explicitly.
- **His full LLM Wiki video.** He says he tagged it on screen [08:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=500s), but neither the captions nor the description give the link.
- **Andrej Karpathy's LLM Wiki pattern** [08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s).
- **Grill Me skill**, originally by Matt Pocock [20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s).
- **His AI OS videos**, the source of the four C's framework [26:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1606s).
- **His earlier vector-database videos** on the channel [15:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=917s).
- **Upcoming videos** on local AI and open-source models [22:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1331s).
- **Tools and products named:**
  - Agents and viewers: Claude Code, Codex, Hermes Agent, Obsidian
  - Vector stores and search: Pinecone, Supabase, Qdrant
  - Graph tools: LightRAG, Logseq, Graphiti (uncertain), GraphRAG (as a concept)
  - Always-on brain: GBrain, gstack
  - Live data and team sync: ClickUp, Slack, Google Drive, Notion, GitHub, Claude plugins
  - Example only: ElevenLabs, as a page topic

## Beyond the source

*Not said in the video; added at ingest and verified at the links given.*

- **Where Claude Code auto memory actually lives.** It's stored per project *outside* the repo at `~/.claude/projects/<project>/memory/`. A `MEMORY.md` index sits there, and its first 200 lines or 25KB load every session; topic files are read on demand. Auto memory is on by default and toggled in `/memory`, and the `autoMemoryDirectory` setting can relocate it. The memory.md shown inside his example folders is therefore most likely a project file he routes agents to, not Claude Code's default auto-memory location. The video doesn't say whether he relocated auto memory there with `autoMemoryDirectory`. To share auto memory with Codex, point Codex at the real memory directory, copy it into the project, or set `autoMemoryDirectory`. Source: https://code.claude.com/docs/en/memory
- **CLAUDE.md + AGENTS.md.** Claude Code reads CLAUDE.md, not AGENTS.md. The docs recommend a CLAUDE.md that imports `@AGENTS.md` (or a symlink), which matches his 22:59 tip. Imported files still load into context at launch, and the docs suggest keeping each CLAUDE.md under about 200 lines. Source: https://code.claude.com/docs/en/memory. AGENTS.md itself is an open instructions format for coding agents, including Codex. Source: https://agents.md/
- **Embeddings aren't 3D.** They're high-dimensional; for example, OpenAI's text-embedding-3-small returns 1,536 dimensions and text-embedding-3-large 3,072. "Three-dimensional" works only as a mental picture. Source: https://developers.openai.com/api/docs/guides/embeddings
- **Karpathy's LLM Wiki gist** describes three layers: a curated collection of raw sources, an LLM-maintained wiki, and a schema file such as CLAUDE.md or AGENTS.md. It also defines three operations: ingest, query and lint. Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **"Smart lookup".** The video never names the tool behind it. Smart Lookup is the name of an Obsidian plugin from the Smart Connections family that searches a vault by meaning using a locally prepared embeddings index. It's likely, but not confirmed, that this is what he shows. Source: https://smartconnections.app/smart-lookup/search/
- **LightRAG** (HKUDS) is open source. It extracts entities and relationships from documents, ships a web UI with graph visualisation, and offers naive, local, global, hybrid and mix query modes. Source: https://github.com/HKUDS/LightRAG
- **GBrain** is open source. It keeps markdown in git as the system of record with a Postgres/PGLite index, and combines vector and keyword (BM25) search with an automatically extracted typed graph. Cron-driven enrichment runs in the background. It primarily targets always-on agents like OpenClaw and Hermes, and also works with Claude Code and Codex over MCP. Source: https://github.com/garrytan/gbrain
- **The original Grill Me skill** is in Matt Pocock's skills repo. Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me
- **Other tools named, briefly:**
  - Qdrant describes itself as a vector search and semantic search engine. Source: https://qdrant.tech/documentation/
  - Graphiti is Zep's open-source framework for temporal knowledge graphs. Source: https://github.com/getzep/graphiti
  - gstack is Garry Tan's open-source (MIT) set of Claude Code slash-command skills. Source: https://github.com/garrytan/gstack
  - Hermes Agent is Nous Research's open-source (MIT) agent with a built-in learning loop. Source: https://github.com/NousResearch/hermes-agent
  - Obsidian stores notes as plain Markdown files in a local vault folder, which supports his point that it's only a viewer. Source: https://obsidian.md/help/data-storage
- **Privacy detail.** On Anthropic's consumer plans (Free, Pro, Max, including Claude Code used from those accounts), a user-controlled setting decides whether chats are used for model training. Retention is 5 years if you allow training and 30 days if you don't. Those terms don't apply to Claude for Work (Team and Enterprise), Claude for Government, Claude for Education or API use. Source: https://www.anthropic.com/news/updates-to-our-consumer-terms

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "claw.md", "Claude at MD", "claude.md" | CLAUDE.md |
| "agents.md" | AGENTS.md |
| "{slash} memory" | the /memory command |
| "Hercule", "Herc 2", "PERC 2" | Herk2, his main second-brain project (spelled this way in the video description) |
| "Quadrant" | Qdrant |
| "Pine Cone" | Pinecone |
| "Lightrag" | LightRAG |
| "graph rack" | GraphRAG |
| "Gbrain", "G brain" | GBrain (by Garry Tan) |
| "G stack" | gstack |
| "a genetic workflow" | agentic workflows |
| "WATC framework" | most likely his WAT framework (Workflows, Agents, Tools); likely, not certain |
| "Graphir" | probably Graphiti (uncertain) |
| "school community" | Skool community |
| "cloud code skills" (15:04), "cloud plugins" (29:56) | Claude Code skills; probably Claude plugins |
| "OTAs" | his term for quarterly projects/priorities; the exact term is *unclear in captions* |
| "stack and conversations file" (06:06) | a stack file plus a second file captioned "conversations", possibly "conventions" (*unclear*) |
| "Other Worlds" folder (09:22) | folder name *unclear in captions* |
| "switch over to level two" (12:40) | from context he means Level 3, since he says he sits at Level 2 |
| "has cron to here" (12:49) | garbled example of a typed relation (*unclear*) |
| "three-dimensional space" (15:36) | simplification; real embeddings are high-dimensional (see Beyond the source) |
| "running agents offline" (29:26) | as captioned; likely means agents running unattended |
| "house search works" (18:14) | the example's "how search works" note |
| "how many brains are about this" (26:33) | garbled; from context, working out where a new item belongs before ingesting it (*unclear*) |
| Jordan, Acme, Postpilot, Cadently (23:29) | fictional demo entities, not real companies |
| "AIS Plus", "Aiden" (24:52) | as captioned: probably his paid community (AI Automation Society Plus, linked in the description), and the person he credits with developing the challenge (role not stated) |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Second Brain Levels]] · [[Design for Retrieval]] · [[CLAUDE.md as a Router]] · [[Tool-Agnostic Context Files]] · [[Claude Code Auto Memory]] · [[LLM Wiki]] · [[Semantic Search]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Knowledge Graphs]] · [[Always-On Brain OS]] · [[Context vs Connections]]
- **Techniques:** [[Build a Level 1 Second Brain]] · [[Port a Claude Code Brain to Other Agents]] · [[Ingest Sources into an LLM Wiki]] · [[Tiered Lookup Routing]] · [[Add Semantic Search to One Folder]] · [[Build a Knowledge Graph Layer]] · [[Grill Me Interview Skill]] · [[Second Brain Pain-Point Audit]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]] · [[Hermes Agent]] · [[GBrain]] · [[Obsidian]] · [[Qdrant]] · [[LightRAG]]
- **People:** [[Nate Herk]] · [[Andrej Karpathy]] · [[Garry Tan]] · [[Matt Pocock]]
