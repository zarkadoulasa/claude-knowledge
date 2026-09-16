---
type: concept
aliases: ["Karpathy LLM Wiki", "Karpathy Obsidian RAG"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tags: [topic/second-brain, topic/retrieval, topic/claude-code, topic/memory]
---

# LLM Wiki

## In one sentence

An LLM Wiki is a folder of plain markdown pages that the agent writes and updates as you feed it sources, and answers questions by starting at an index, following see-also links and reading whole pages; it is **Level 2** in [[Nate Herk]]'s five-level model ([[Second Brain Levels]]) and the level his main project runs at ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)).

## How it works

### Where it sits in the levels

- Level 2's question is whether the system can **gather everything on one topic in one place** ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)). Level 1 asks something narrower: can you find a file by an exact word or name.
- He credits the pattern to [[Andrej Karpathy]] and mentions he has a separate full video on it ([08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s)).
- Level 2 keeps the Level 1 shape and adds to it. The [[CLAUDE.md as a Router|CLAUDE.md router]] still sends Claude to the context, projects and decisions folders. It now also points to the wiki, a references folder and a memory.md file ([10:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=620s)–[10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). In practice, Level 2 means more routing rules in the same CLAUDE.md.
- memory.md comes from turning on Claude Code's auto memory (toggled with the /memory command), so Claude writes that file itself ([10:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=647s)–[10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s)). To keep the brain usable from other tools, copy CLAUDE.md to AGENTS.md and tell Codex to read memory.md for memories ([11:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=678s)–[11:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=701s)). Where Claude Code really stores auto memory is covered under Beyond the source. Details are in [[Claude Code Auto Memory]] and [[Port a Claude Code Brain to Other Agents]].

### Separate wikis for different kinds of material

- A wiki starts to make sense once you have **more files, the files take different shapes, and you want them grouped differently** ([08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s)).
- His examples: collecting all the research on one project ([08:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=511s)), one wiki for all his YouTube video transcripts ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)), and another for his meeting transcripts ([08:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=520s)). Each body of material gets **its own wiki**.
- The transcript wiki is not a separate vault. It sits inside his main Herk2 project, a few folders down (under a folder captioned "Other Worlds", then "YouTube OS", then the transcript wiki) ([09:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=555s)–[09:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=566s)). Because it all lives in that one project, he relies on his second brain to find it instead of opening Obsidian ([10:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=614s)).

### Ingest: the agent writes the pages

When he tells [[Claude Code]] to ingest a YouTube transcript, it creates these pages on its own ([09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s)). The page types he points to in his transcript wiki:

| Page type | What he names on screen | Timestamp |
|---|---|---|
| Concepts | agentic workflows, AI coding market, context window | [08:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=527s) |
| Sources | named as a section; no examples given | [08:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=539s) |
| Platforms | named as a section; no examples given | [09:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=540s) |
| Techniques | context management techniques | [09:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=540s) |
| Comparisons | named as a section; no examples given | [09:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=572s) |

The pages link back to related tools, concepts and videos ([08:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=535s)). He stays in charge of what gets ingested. He runs a skill that gathers the week's meeting transcripts, asks Claude to help him work out how the material fits (this sentence is garbled in the captions), and then they ingest it together ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)–[26:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1596s)). The step-by-step workflow is in [[Ingest Sources into an LLM Wiki]].

### Retrieval: start at the index, drill down

- A wiki's main strength is its **index** ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)). For a question about agentic workflows, the agent opens the index, goes to that page, and reads it to see what else is relevant ([11:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=716s)).
- From there it follows links to further pages, such as a page captioned "WATC framework" (most likely his WAT framework; not certain from the captions, see Beyond the source) and then a page on the CLAUDE.md system prompt ([12:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=727s)–[12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s)).
- He describes this as **following a trail and reading each page in full** ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)). There are some relationships along the trail, but he says they carry less meaning than semantic or knowledge-graph relationships ([12:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=734s)).
- The wiki is one stop in a wider lookup order. In his [[Tiered Lookup Routing]] example, a question about a recent conversation sends the agent first to the file of quarterly projects (captioned "OTA"; the exact term is unclear in the captions), then to the wiki and meeting transcripts, and only then to the live system, ClickUp ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s)–[28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)).

### Links are see-also, not typed relationships

- He takes on the obvious objection: if the wiki has links, isn't it a knowledge graph? Not quite ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)).
- Wiki links don't say how two pages relate. There's no label such as "endorsed by" ([12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s)). They work like see-also references or backlinks ([12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)). The effect can be similar, but they are still a little different ([12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)).
- He says his wiki still gives him enough of a feel for these relationships, **because he has put a lot of effort into ingesting sources properly and giving them context** ([23:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1427s)–[23:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1438s)).
- A graph tool like [[LightRAG]] shows named relationships such as "collaborates with" and "builds" ([24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s)). He says it holds much the same data as his Obsidian view, but the wiki doesn't give the same level of relationships between entities ([24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)). See [[Knowledge Graphs]].

### Obsidian is only a viewer

- The graph screens of his wiki are [[Obsidian]], which does nothing except render the markdown files as a visual map ([09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)).
- People get drawn in by the visual graph ([09:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=589s)). What matters is whether the system can find the information and hand it back ([10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)).
- If you think visually, installing it is easy ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s)). If the view doesn't help you, skip it. He rarely opens Obsidian because his agent can already find everything ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).

### How it compares with the levels either side (as described in the video)

| | LLM Wiki (L2) | Semantic search (L3) | Knowledge graph (L4) |
|---|---|---|---|
| How the agent finds things | Index, then follows links through the trail ([11:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=716s)) | Matches by meaning, not exact words ([14:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=869s)) | Follows chains of entities and relationships ([23:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1408s)) |
| What it reads | Entire pages ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)) | Chunks that look similar ([16:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=982s)) | Can be lighter, because it doesn't have to read whole files ([24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)) |
| Links / relationships | Untyped see-also links ([12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)) | Nearness in embedding space ([15:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=947s)) | Typed, e.g. works at, competitor of ([23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s)) |

The full comparison is in [[Keyword vs Semantic vs Graph Retrieval]].

### Chase's version: raw / wiki / outputs with an index in every folder

[[Chase AI - The Agentic OS Setup for Claude Code]] teaches the same pattern as part of his agentic OS. It is the core of his Level 2, "memory and state" ([02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)); see [[Agentic OS]]. His Level 2 is not the same thing as Nate's Level 2 ([[Second Brain Levels]]).

- **Where he says it comes from.** He credits a viral Karpathy tweet about building an Obsidian knowledge base that LLMs can read quickly. He puts it at over 20 million views ([17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s)–[17:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1049s)). The existing sections of this note rely on Karpathy's later gist instead (see Beyond the source).
- **Three folders, split by stage of processing:**

  | Folder | What goes in it | Timestamp |
  |---|---|---|
  | `raw/` | Unstructured material, e.g. a pile of articles from researching AI agents | [17:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1067s)–[18:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1091s) |
  | `wiki/` | The same research turned into structured, Wikipedia-style articles, so Claude reads one tidy page instead of 20 source documents | [17:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1077s)–[18:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1110s) |
  | `outputs/` | Deliverables built from the wiki, e.g. a slide deck | [18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s)–[19:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1141s) |

- **The index files matter more than the folders.** He says the real strength is an index.md at *every* level telling Claude Code what that level holds ([19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s)–[19:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1183s)). His walk-through: asked about AI agents, Claude reads the vault's root index.md, which lists raw, wiki and outputs. It picks wiki/, reads the index.md there, then opens the article ([19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s)–[20:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1225s)). That is the same index-first drill-down Nate describes above, repeated in every folder.
- **Why an index in every folder.** It's overkill for a folder with one file. After years of use, with thousands of documents and subfolders, it makes navigation much easier ([20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s)–[20:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1249s)). If each "room" Claude walks into has a spot that explains it, lookups get faster and cheaper ([20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s)–[21:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1265s)).
- **The folder names are arbitrary.** You don't need raw or outputs or any of the Karpathy layout. You need a map that fits your own data ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)–[21:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1286s)). If you're unsure, ask Claude Code to look at your vault and suggest a structure, using Karpathy's setup as inspiration ([21:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1292s)–[21:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1301s)).
- **A vault CLAUDE.md on top.** His vault's CLAUDE.md sets out the vault conventions. It describes the folder structure, and his real vault has more than three folders: content, notes, runs, inbox, ops, projects. It also has a navigation pattern section giving the path to follow when looking something up ([21:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1307s)–[22:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1331s)). That is the [[CLAUDE.md as a Router]] idea, plus explicit navigation steps.
- **Why he bothers.** Without structure, say one folder of millions of files with no backlinks or hierarchy, Claude is slow to find answers, and slow here means more tokens and more cost ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s)–[16:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1002s)). His mental model is a map with a clear path to every file ([16:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1004s)–[17:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1026s)). He goes as far as saying a coherent file structure alone, with no database and no Obsidian, gets you about 99% of the way ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)–[14:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=857s)). That's an opinion; he gives no measurement.
- **It also stores state for loops.** Outputs from skills and automations should be logged in the same place, so a self-improving loop can see what past runs did ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)). See [[Loop Engineering]].
- **How to build it:** the "One vault split by stage" variation in [[Ingest Sources into an LLM Wiki]].

### Building it from the idea file (April–May 2026 sources)

The setup steps are in [[Bootstrap an LLM Wiki from the Karpathy Gist]].

- **Idea files.** There is no repo to copy: you ask Claude Code to read Karpathy's deliberately vague idea and implement it, and the result follows the vault's purpose ([[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]], [05:28](https://www.youtube.com/watch?v=sboNwYmH3AY&t=328s)). Codex over-built [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]'s first attempt to 51 files before he pruned it ([11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s)).
- **Flat or subfoldered.** Nate keeps his personal wiki flat and his YouTube wiki in subfolders, matching each one's purpose ([08:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=484s)).
- **Hot cache.** His personal wiki has hot.md, roughly 500 words or characters (he isn't sure which) of the latest material; a reference wiki doesn't need one ([14:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=884s)). See [[Agent Memory Patterns]].
- **Lint.** Nate passes on Karpathy's checks: inconsistent data, gaps filled by web search, and new article candidates, run daily or weekly ([15:08](https://www.youtube.com/watch?v=sboNwYmH3AY&t=908s)).
- **Tokens.** A wiki needs only markdown and tokens; RAG needs embeddings, a vector database and chunking ([16:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=985s)). The token savings are claimed, not measured ([04:53](https://www.youtube.com/watch?v=sboNwYmH3AY&t=293s), [14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s)). Where a wiki stops scaling is under "Newer disagreements".
- **Answers filed back, no orphans.** Matt's agent saves reusable answers as pages linked to their sources ([18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s)), and his schema links every new page to its source page ([21:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1268s)).
- **A hub with layers.** Matt adds a journal and a CRM that read the wiki; how a chat starts decides which one handles it ([23:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1424s)). See [[Add a Journal and Personal CRM to a Second Brain]].
- **Shared by other projects.** Nate's April assistant reaches a separate wiki vault through its CLAUDE.md: hot cache, then index, then sub-index, and only when needed ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s)). By June his transcript wiki sits inside the Herk2 project ([09:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=555s)).
- **Chase, May.** [[Chase AI - The Three-Step Claude Code Agentic OS]] restates raw as staging for conversations and research ([09:21](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=561s)) and output for deliverables such as slide decks ([10:07](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=607s)), allows one folder per domain instead ([10:35](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=635s)), and treats a CLAUDE.md that maps the memory as the must-have ([11:50](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=710s)).

### Where sources disagree

*The "Karpathy's gist" parts of the left column are not from a video. They summarise the gist items under Beyond the source, where each one is linked. Only the cells with timestamps are what Nate or Chase said.*

| Question | Karpathy's gist and Nate (earlier sections, Beyond the source) | [[Chase AI - The Agentic OS Setup for Claude Code]] |
|---|---|---|
| **Is it RAG?** | The gist presents the wiki as knowledge compiled once and kept current, as opposed to RAG, which works from raw documents again on every query. Nate treats meaning-based chunk retrieval as a separate level, [[Semantic Search]] ([13:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=784s)) | He calls it the Karpathy Obsidian "RAG", with air quotes, as a new kind of RAG ([19:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1155s)–[19:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1160s)) |
| **The three layers** | Raw sources, the wiki, and a schema file (CLAUDE.md or AGENTS.md) | raw/, wiki/, outputs/ ([19:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1144s)). The CLAUDE.md comes later as an extra ([21:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1306s)) |
| **Indexes** | One index.md catalogue per wiki, plus an append-only log.md. Nate's agent starts at "the index" ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)) | An index.md in every folder at every level ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)). No ingest log is mentioned; his logging is for skill and automation runs ([22:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1356s)) |
| **Answers and deliverables** | The gist's query step files good answers back into the wiki as new pages | Deliverables go to a separate outputs/ folder ([18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s)). He doesn't say whether they feed back into wiki/ |
| **How to split a wiki** | Nate keeps one wiki per kind of material, e.g. YouTube transcripts vs meeting transcripts ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)) | One vault split by stage of processing: unstructured, then structured, then outputs ([19:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1148s)) |
| **How far structure gets you** | Nate says wikis start to degrade at some scale ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)) and keeps Levels 3–4 for specific pains | Structure alone gets you about 99% of the way ([14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s)), and nested indexes pay off more as files pile up over years ([20:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1236s)) |
| **Obsidian** | Nate calls it only a viewer and rarely opens it ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)) | Also optional, since a database works too ([13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s)–[13:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=835s)), but he uses it as the vault and shows its graph as Claude's map ([16:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1008s)) |
| **Is there one right layout?** | Nate: no structure is proven best; use routing that makes sense to you and your AI ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)) | They agree: the folders are arbitrary, so build a map for your own data ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)) |

**What to take from the "RAG" label.** Nothing in Chase's walk-through uses embeddings. Claude reads index files and opens whole pages ([19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s)). So in this vault's terms his setup is an LLM Wiki with nested indexes, not RAG. If you want chunk-and-embed retrieval, that's [[Semantic Search]].

**Newer disagreements**

| Question | One side | Other side |
|---|---|---|
| **Where the wiki stops** | Nate, April: hundreds of well-indexed pages are fine, millions of documents need RAG ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)); June: wikis degrade at some point ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)) | Chase: 99.9% of people need no vector database ([11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s)) |
| **Who controls ingest** | Nate ingests by hand, wary of too much context ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)) | Matt runs an unattended hourly ingest ([29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s)) |
| **Obsidian's role** | Nate, June: rarely opens it ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)) | Matt edits the schema there, calling it his "visibility layer" ([31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s)) |

## When to use it — and when not to

**Signs it fits**
- You have **30 or more notes and keep forgetting what's in them**. That is his rule-of-thumb trigger for Level 2 ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)–[29:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1748s)).
- One area keeps growing: research on a single project, or a steady stream of video or meeting transcripts ([08:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=511s)).
- Answers need the **whole document**. When asked to summarise one meeting, reading that meeting's full markdown file gives a more accurate result than retrieving a handful of vector chunks ([17:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1038s)–[17:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1046s)). Reading whole pages is exactly what a wiki does.
- The main part of your work is projects and content, not a big CRM full of clients and businesses. That describes his situation, and a wiki has been enough for it ([19:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1193s)–[20:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1206s)).

**Signs you have outgrown it, or never needed it**
- **Growth.** He says that at a certain point wikis start to degrade a little ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)).
- **Whole-page reads get heavy.** The agent reads every page it opens. If it only needed the ElevenLabs detail, it still reads the entire AI-video-production page ([24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s)–[24:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1449s)). He makes the same point about Level 3: pulling "rule 17" from 1,000 rules by vector search beats reading the whole file ([18:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1111s)–[18:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1127s)).
- **Routing misses notes you know exist.** Look at [[Semantic Search]] ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)).
- **You need to follow chains of relationships.** Look at [[Knowledge Graphs]] ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)).
- **No pain, no upgrade.** Choose the lowest level that meets your needs, and don't build a new architecture without a real pain point ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)–[04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).

**Mix levels by folder.** A project doesn't need one style everywhere. Not every folder needs GraphRAG, and not every folder needs to be a wiki. Structure each folder around its data and how you use it ([17:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1073s)–[18:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1087s), [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)). His Level 4 example project still keeps a wiki next to the new graph layer ([23:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1389s)). If you aren't sure, describe your data and how you'll use it to Claude Code and ask whether plain markdown or semantic search fits better ([19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s)). The per-folder diagnosis is in [[Second Brain Pain-Point Audit]].

**Check capture before blaming retrieval.** Sometimes retrieval really is the problem. But sometimes the bigger problem is that the knowledge never made it out of your head into the files. Before blaming the AI, check whether your folders hold the full nuance you carry around ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s)). See [[Grill Me Interview Skill]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] — He runs pretty much his whole Herk2 project at Level 2 because it keeps working well for him ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)–[12:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=754s)). He hasn't hit a pain big enough to move up ([12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s); he says "level two" in that sentence, but from context he means moving up to Level three). He has experimented with knowledge graphs but doesn't use them day to day, because routing files and wikis cover his needs ([19:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1183s)–[19:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1192s)). His view of the wiki: pages that were ingested carefully and given context convey enough of the relationships ([23:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1427s)). The costs are whole-page reads and degradation as the wiki grows ([24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s), [11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)). The whole thing is just markdown files organised so both he and his agents understand them ([01:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=70s)), so any harness can use it, including Codex and [[Hermes Agent]] ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)–[01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: He treats the wiki as the memory-and-state layer of an [[Agentic OS]], not as one retrieval level among several ([02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)). For him the work is done by the index files; the raw/wiki/outputs folders are just one choice among many ([19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s), [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)). He says a coherent structure alone gets you about 99% of the way, with no database or Obsidian needed ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)), and he never discusses when a wiki stops scaling. What he adds: an outputs/ stage for deliverables ([18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s)), a navigation-pattern section in the vault CLAUDE.md ([22:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1327s)), and logging skill and automation runs next to the knowledge so loops can learn from past runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)). He uses "RAG" loosely for the setup ([19:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1155s)); see "Where sources disagree".
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]], [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] and [[Chase AI - The Three-Step Claude Code Agentic OS]]: see "Building it from the idea file" and "Newer disagreements". Chase's May video is an earlier, shorter take on his June layout.

## Beyond the source

*None of this comes from the videos. Each item was checked against the linked page.*

- **Origin.** Karpathy published the pattern as a GitHub gist titled "LLM Wiki" on 2026-04-04. It is an "idea file": prose meant to be pasted into an agent so the agent builds a wiki for its user. It describes a pattern, not a product. Verified: [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), whose page shows it was created on 2026-04-04 and calls itself an idea file. [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/) also dates it to April 2026.
- **The three layers in Karpathy's description.** Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

  | Layer | What it is | Who changes it |
  |---|---|---|
  | Raw sources | Articles, papers, images and other source documents; never modified | Human curates; LLM only reads |
  | The wiki | LLM-written markdown pages: summaries, entity pages, concept pages, cross-references | LLM writes and maintains all of it |
  | The schema | An instruction file (the gist names CLAUDE.md for Claude Code or AGENTS.md for Codex) that sets the wiki's structure, conventions and ingest/query workflows | Human and LLM refine it over time |

- **The three operations.** Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
  - *Ingest*: read a new source, discuss the takeaways, write a summary page, update the index and the related entity and concept pages, and add an entry to the log. One source can touch 10–15 pages. Karpathy prefers ingesting one source at a time and staying involved, but says batch ingest with less supervision also works.
  - *Query*: search the wiki, answer with citations, and optionally **file a good answer back into the wiki as a new page** so explorations build up over time. Nate's June video doesn't mention this; [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] shows it working ([18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s)).
  - *Lint*: a periodic health check for contradictions, stale claims, orphan pages, missing cross-references and gaps. Nate's June video doesn't cover lint; his April video passes on Karpathy's version ([15:08](https://www.youtube.com/watch?v=sboNwYmH3AY&t=908s)).
- **The two special files.** Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
  - `index.md` is a catalogue of every page by category with one-line summaries. It is updated on each ingest and is where retrieval starts. This is the "index" Nate describes the agent reading first.
  - `log.md` is an append-only, time-ordered record of ingests, queries and lint passes.
- **The scale guidance lines up with Nate's point that wikis degrade past a certain point.** The gist says the index-file approach works well at moderate scale, roughly 100 sources and hundreds of pages, without embedding-based RAG. As the wiki grows it suggests adding proper search (it names qmd, a local hybrid BM25/vector search with LLM re-ranking). That is effectively a step toward Level 3 ([[Add Semantic Search to One Folder]]). Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **Not in the gist.** Neither the gist nor Karpathy's post says anything about flat vs nested folders or a hot cache. So the liking for flat layouts Nate credits to Karpathy ([08:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=490s)) is unverified, and hot.md is Nate's own addition as far as these sources show. Karpathy's post gives about 100 articles and about 400K words; Nate says half a million ([02:58](https://www.youtube.com/watch?v=sboNwYmH3AY&t=178s)). Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [FxTwitter readout](https://api.fxtwitter.com/karpathy/status/2039805659525644595).
- **The contrast with RAG.** The gist presents the wiki as knowledge that is compiled once and then kept current, while RAG re-derives answers from raw documents on every query. Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **A difference in emphasis on Obsidian.** Karpathy makes Obsidian central to the experience: Obsidian is the IDE, the LLM the programmer, the wiki the codebase. He keeps the agent open next to Obsidian, browses the results (including the graph view) as the edits land, and recommends Obsidian Web Clipper for capturing sources. Nate treats Obsidian as optional and seldom opens it. Both agree the substance is plain markdown, which the gist describes as a git repo of markdown files. Verified: [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **The "WATC framework" caption.** It most likely refers to his WAT framework, commonly expanded as Workflows, Agents, Tools in write-ups about his teaching. His own Skool post names the framework as how he builds automations ([Skool post](https://www.skool.com/ai-automation-society/new-video-master-95-of-claude-code-in-36-mins-as-a-beginner)). The captions alone can't confirm it.
- **Where auto memory actually lives.** In the video, memory.md sits inside his example project folder ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). By default, Claude Code keeps auto memory per project *outside* the repo, in `~/.claude/projects/<project>/memory/`. That folder holds a `MEMORY.md` index, and its first 200 lines or 25KB load at the start of every session. It is machine-local. A different folder can be set with the `autoMemoryDirectory` setting. The docs also say auto memory is on by default, so the /memory toggle he shows is only needed if it has been switched off. So before you point Codex or another agent at "the memory file", check where it really is. Either route to that folder or keep a memory file inside the project yourself. Verified: [Claude Code memory docs](https://code.claude.com/docs/en/memory). See [[Claude Code Auto Memory]].
- **This vault is itself an LLM Wiki.** Its `CLAUDE.md` says the vault follows the pattern. Verified in the vault's own `CLAUDE.md` and [[Home]]. Mapped to Karpathy's layers:

  | Karpathy's layer / file | In this vault |
  |---|---|
  | Schema | `CLAUDE.md` (routing rules, note conventions, tag set) plus `Templates/` |
  | Wiki pages | `Sources/`, `Concepts/`, `Techniques/`, `Tools/`, `People/` |
  | `index.md` | [[Home]] |
  | `log.md` | `Ingest Log.md` (append-only) |
  | Ingest | the `ingest-youtube` skill |
  | Lint | partly: `.tools/check_links.py` checks links (no contradiction or staleness pass yet) |
  | Raw sources | transcripts are fetched as working files and **deliberately not kept** in the vault. That differs from the gist's persistent, unmodified raw layer; a transcript is re-fetched when a build needs more detail |

- **Build note.** The gist deliberately stays abstract. For a concrete folder layout, schema rules and ingest prompts to hand Claude, use [[Ingest Sources into an LLM Wiki]]. The other route, which Nate and Matt both take, is to hand the gist itself to the agent and check what it builds: [[Bootstrap an LLM Wiki from the Karpathy Gist]]. Only Matt prunes, telling Codex to strip its 51 files back ([11:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=698s)); Nate keeps Claude's default subfolders and plans to revisit them once content arrives ([07:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=474s)).
- **Post vs gist: why Chase's layout differs from the table above.** Before the gist, Karpathy described the idea in an April 2026 "LLM Knowledge Bases" post on X. Coverage of that post describes:
  - raw data collected into a `raw/` directory
  - an LLM-compiled markdown wiki with index files summarising the documents, plus concept articles with backlinks
  - outputs such as Marp slide decks and matplotlib charts
  - query outputs filed back into the wiki, so each exploration adds up
  - no embeddings or vector search needed at personal-knowledge-base scale

  So Chase's raw / wiki / outputs split matches the *post*, while the raw / wiki / schema split above comes from the *gist*. The post, like the gist, treats this as an alternative to embedding-based retrieval, which is why "RAG" is a loose label for it. The coverage doesn't describe a separate outputs folder or an index in every folder; both look like Chase's own additions. Chase says the post had over 20 million views ([17:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1042s)); that matches the post's count of about 21.9 million on 2026-09-15 ([FxTwitter API readout](https://api.fxtwitter.com/karpathy/status/2039805659525644595)). The 16+ million in an April 2026 write-up was an early count ([Starmorph guide](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide)). Verified: [DAIR.AI Academy summary of the post](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy). The [original post](https://x.com/karpathy/status/2039805659525644595) needs an X account to open directly.

## Related

- [[Second Brain Levels]] · [[CLAUDE.md as a Router]] (Level 1, below) · [[Semantic Search]] (Level 3, above) · [[Knowledge Graphs]] (Level 4)
- [[Design for Retrieval]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Context vs Connections]] · [[Tool-Agnostic Context Files]] · [[Claude Code Auto Memory]]
- Agentic OS context: [[Agentic OS]] · [[Loop Engineering]]
- Techniques: [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Ingest Sources into an LLM Wiki]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Tiered Lookup Routing]] · [[Second Brain Pain-Point Audit]] · [[Grill Me Interview Skill]]
- Tools: [[Obsidian]] · [[Claude Code]] · [[OpenAI Codex]] · [[LightRAG]]
- People: [[Andrej Karpathy]] · [[Nate Herk]] · [[Chase AI]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] · [[Chase AI - The Three-Step Claude Code Agentic OS]]
- People: [[Matt Wolfe]]
- [[Home]]
