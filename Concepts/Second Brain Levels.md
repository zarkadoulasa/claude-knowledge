---
type: concept
aliases: ["Five Levels of a Second Brain", "AI Second Brain"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]"]
tags: [topic/second-brain, topic/retrieval, topic/memory, topic/rag, topic/knowledge-graph, topic/claude-code, topic/agents, topic/agentic-os]
---

# Second Brain Levels

## In one sentence

An AI second brain can be built at five levels (router file, LLM wiki, semantic search, knowledge graph, always-on brain OS). Each level answers a harder retrieval question. The goal is the **lowest level that fixes a pain you actually have**, not the top of the ladder.

These five levels are [[Nate Herk]]'s. Two other sources use "levels" for different ladders. [[Jay E]] has a three-rung memory ladder and [[Chase AI]] has four agentic OS levels, so the same level number means different things. See "Other level frameworks" below.

## How it works

### What a second brain is for

- **The job:** a place to drop notes, meeting recordings and ClickUp threads. It ingests them, files them in the right spot and finds them again later ([01:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=115s), [02:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=122s)).
- **The test:** can your agent find it again, *and could you*? If not, your routing or folder layout is wrong ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s), [02:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=139s)).
- **Why it matters:** your data is your moat and your IP ([00:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=47s)). The hard part is organising it so different AI models can recall it accurately, without hallucinating or spending time and tokens searching everything ([00:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=52s)).
- **The goal:** a brain that knows your business, you and your relationships well enough to recall things faster and better than you can ([03:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=186s)).
- **It is just files and folders.** Nate uses the same brain from Claude Code, OpenAI Codex and Hermes Agent, because any agent harness can read it ([01:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=102s)). See [[Tool-Agnostic Context Files]].
- **Design rule behind every level:** work backwards from the questions you will ask. How data will be retrieved decides how it should be stored ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)). See [[Design for Retrieval]].

### The five levels at a glance

The question for each level comes from the overview at [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s).

| Level | Question it answers | Mechanism | Concept note |
|---|---|---|---|
| **1 · Router** | Can you find a file or fact by an exact word or name? ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)) | CLAUDE.md / AGENTS.md with routing rules, plus plain folders of markdown | [[CLAUDE.md as a Router]] |
| **2 · LLM Wiki** | Can you pull everything on one topic together? ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)) | Ingested, indexed, interlinked wiki pages. Auto memory. | [[LLM Wiki]], [[Claude Code Auto Memory]] |
| **3 · Semantic search** | You search with different words than you wrote. Can it still match on meaning? ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)) | Chunk, embed and store in a vector index, then search by similarity | [[Semantic Search]] |
| **4 · Knowledge graph** | Can you ask about topic X and trace a relationship chain back to topic A? ([03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s)) | Entities plus typed relationships | [[Knowledge Graphs]] |
| **5 · Always-on brain OS** | Can the whole thing run so you don't have to think about it? ([03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s)) | Continuous sync and memory refresh on schedules (e.g. [[GBrain]]) | [[Always-On Brain OS]] |

Each level builds on the one before rather than replacing it ([10:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=624s), [23:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1401s)). The Level 3 example still has its context and decision files ([17:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1049s)), and the Level 4 example still has the routing, wiki, plain markdown and memory ([23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s)).

Nate's shorthand for keyword vs semantic search: keyword search asks whether X equals X, and semantic search asks whether X is similar to X, Y and Z ([15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s)). See [[Keyword vs Semantic vs Graph Retrieval]].

---

### Level 1: CLAUDE.md as a router

**Mechanism**
- This is where everyone starts ([04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s)). You write a CLAUDE.md, or an AGENTS.md if you use Codex or a similar agent ([04:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=266s)). It loads every session and works almost like that project's system prompt ([04:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=271s)).
- The key move is treating that file as a **router** ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)). It still sets a role and priorities, but it also holds routing rules like "personal info lives in this folder" or "Q1 priorities live in that folder" ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)).
- The example Level 1 project has these parts:
  - a CLAUDE.md with a short "where things live" section ([05:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=353s))
  - a context folder for always-true background: an about-me file, a stack file, and a second file captioned "conversations" (possibly "conventions") *(unclear in captions)* ([06:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=366s))
  - a decision log that Claude appends dated decisions to ([06:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=370s))
  - a projects folder with files or sub-folders per project or client ([06:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=379s)), which can also be grouped by month ([06:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=389s))

**What you get**
- You stop re-explaining yourself. The agent knows where to look and why ([05:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=314s)).
- You can navigate it too. Nate finds a slide deck in his Herk2 project by drilling from projects to YouTube videos to the dated video folder, without asking AI ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s)). His agent can find it for the same reason ([07:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=464s)).

**Failure modes**
- **Missing route.** Claude asks you for information you know is somewhere in the project. That usually means no rule points to it. Claude won't search the whole project on its own, and you wouldn't want it to burn the time and tokens ([04:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=297s), [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)).
- **Bloat.** As the file grows it gets messy and starts to feel ignored ([05:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=319s)).
- **Exact-word dependence.** Retrieval mostly relies on exact words, depending on how you route ([05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)).
- **Copying someone else's layout.** No folder structure has been proven best yet ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)). Don't treat Nate's layout, or anyone's, as the only right one ([06:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=415s)). What matters is proper routing that makes sense to you and to your AI ([07:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=422s)).

**Signal to move up:** you have more files in different shapes that need grouping differently ([08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s)), or 30+ notes whose contents you keep forgetting ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)). Check first that the problem isn't just a missing route.

**Build it:** [[Build a Level 1 Second Brain]]

---

### Level 2: LLM Wiki

**Mechanism**
- Level 2 brings in Andrej Karpathy's [[LLM Wiki]] pattern ([08:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=491s), [08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s)). It fits when you have more files, in different shapes, that need grouping differently ([08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s)).
- Good uses include research on one project ([08:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=512s)). Nate keeps separate wikis for his YouTube transcripts and his meeting transcripts ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)).
- Claude Code generated the concept, source and technique pages when told to ingest a transcript ([09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s)). See [[Ingest Sources into an LLM Wiki]].
- A wiki can sit inside the main brain. His transcript wiki lives inside Herk2, under a YouTube OS area ([09:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=557s)).
- The folder has the same shape as Level 1. CLAUDE.md now also routes to the wiki, a references folder and a memory file ([10:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=628s), [10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)).
- Turn on Claude Code auto memory and the AI writes and updates memory itself. The /memory command shows whether it is on ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s), [10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s)). See [[Claude Code Auto Memory]].
- **How retrieval works:** wiki indexes give the agent an entry page, and it drills down from there ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)). An example trail runs from agentic workflows to what is most likely his WAT framework (captioned "WATC") to the CLAUDE.md system prompt ([12:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=727s)).
  - This is following a trail and reading whole pages. It is not semantic or knowledge-graph relationships ([12:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=736s), [12:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=744s)).
- **Wiki links are not a knowledge graph.** They work like see-also links or backlinks. They don't say *how* two things relate (e.g. "endorsed by"), even if the effect can be similar ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s), [12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)).
- **Obsidian is only a viewer** for the markdown ([09:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=576s)).
  - People get hooked on the graph view ([09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s)), but what matters is whether the system can fetch the answer ([10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)).
  - Nate rarely opens [[Obsidian]] ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).

**Portability**
- CLAUDE.md and auto memory are the Claude-specific parts of the brain ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s)).
- For Codex, copy CLAUDE.md to AGENTS.md ([11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s)), keep the memory file, and tell Codex where to find it ([11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s)).
- See [[Port a Claude Code Brain to Other Agents]].

**Failure modes**
- At some scale, wikis start to degrade ([11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s)).
  - [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]], his April 2026 video, is more specific. Hundreds of pages with good indexes are fine ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)); millions of documents call for a traditional RAG pipeline ([17:14](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1034s)). A file-based wiki doesn't scale across an enterprise, where it gets costlier than semantic search, a knowledge graph or LightRAG ([16:53](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1013s)). He frames this as a view for current models ([17:17](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1037s)).
- The agent must read whole files. Even when it needs one detail, such as a single tool on an AI video production page, it reads the entire page first ([24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s)).

**Signal to move up:** the agent keeps missing notes you know exist and better routing isn't fixing it ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)), or you need one detail out of a large body of text without reading it all ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s)).

**Where Nate sits:** almost all of Herk2 is at Level 2, because it works well for him ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)). He hasn't felt enough pain to move up ([12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s)). The captions say "level two" there, but from context he means Level 3.

---

### Level 3: Semantic search

**Mechanism**
- Search by meaning instead of exact words. You can do this in Obsidian, Pinecone, Supabase or elsewhere ([13:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=784s), [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s)).
- **Image demo in [[Qdrant]]:** each vector point is an image ([13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s)). The payload holds details like file name, URL and author or artist, but no description of what the image shows ([13:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=806s)). Still, similar-looking images cluster together, similar but not identical ([13:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=838s)).
- **Search demo:** in his YouTube-transcript brain, a normal search for "feedback" returns only literal matches ([14:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=887s)). A "smart lookup" also returns pages that *mean* feedback, like live test results and a page on skill evaluations ([14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s)).
- **How it works:** split a document into chunks and run each chunk through an embeddings model ([15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s)). The model places the chunk in a space where position reflects meaning. Nate describes it as three-dimensional, which is a simplification ([15:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=936s)).
- **Mix it in per folder:** keep context, projects and decisions as markdown and vectorise only one unit, such as YouTube transcripts ([17:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1056s)).
- The example project's vector index folder explains the pipeline: chunking, embedding, search, hybrid search and re-ranking ([18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s), [18:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1095s)).

**What you get**
- Pinpoint answers from large bodies of text ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s)). For example, "what was rule 17?" out of 1,000 rules returns just that snippet ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)). Reading the whole file would waste time and tokens ([18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)).

**Failure modes**
- **Whole-document questions.** Store the March 5 meeting as chunks, then ask for a summary. The agent retrieves only chunks similar to the query and summarises just those, so it can miss key information ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s), [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=998s)).
- **Aggregates.** Ask for the highest-sales week and the agent may answer from a partial table chunk. Later weeks that were higher get missed ([16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)).
- **Vector databases aren't magic.** Metadata helps, but it doesn't remove the problem ([16:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1001s), [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s)).
- For full-context tasks, a single markdown file read end to end is more accurate ([17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s), [17:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1047s)).

**Deciding:** describe your data and how you'll use it to Claude Code, and ask whether it should stay as markdown or get semantic search ([19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s)).

**Signal to move up:** you need to follow relationships and chains of questions between entities ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)). If you don't, a graph is probably unnecessary ([25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s)).

**Build it:** [[Add Semantic Search to One Folder]]

---

### Level 4: Knowledge graph

**Mechanism**
- The Level 4 example project keeps routing, the wiki, plain markdown ("boring is beautiful") and memory, then adds a knowledge-graph layer ([23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s), [23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s), [23:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1398s)).
- It also has an AGENTS.md identical to CLAUDE.md. Nate notes you can reference AGENTS.md from CLAUDE.md instead of keeping a duplicate ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s), [22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)).
- **Entities and typed relationships:** a person works at a company, that company is endorsed by another entity, and that entity competes with a third. The example names are fictional demo data ([23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s), [23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s)).
- **His real graph in [[LightRAG]]** covers his business ([24:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1458s)). Its edges have names like "collaborates with" and "builds" ([24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s)).
  - Example: his 7-day AI challenge is linked to where it came from, the onboarding it feeds and the person who developed it ([24:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1486s)).
  - The underlying data is roughly the same as in his Obsidian wiki, but the relationships are much richer ([24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)).

**What you get**
- You can follow relationship chains ([24:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1496s)).
- It can be lighter than a wiki because the agent doesn't have to read whole files ([24:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1453s)).

**Costs and failure modes**
- Usually the most complex level and sometimes the most expensive, though open-source options exist ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s), [19:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1178s)).
- Nate has experimented a lot but doesn't use graphs day to day. Routing files and wikis cover his needs ([19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s), [19:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1189s)).
  - His work is project-based and content-heavy ([19:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1195s)). With a big CRM across many businesses and clients, a graph would probably make sense ([20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s)).
    - **A personal CRM may not need one.** [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] keeps his CRM as flat markdown: one file per person plus an alphabetical index with short bios ([23:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1392s), [23:26](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1406s)). It answers "where did I meet this person?" from those files ([25:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1549s)). *This note's reading:* Nate's threshold is many businesses and clients, which a one-person contact list doesn't reach.
- **The hard part is data, not software.** The data you need probably already exists in your folders ([20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s)). Graph tools are good at building relationships; you have to feed them enough material ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).
  - Nate generates that material with brainstorm interviews using a customised Grill Me skill from [[Matt Pocock]] ([20:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1237s), [20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s)). See [[Grill Me Interview Skill]].
- **Retrieval failures are often capture failures.** Before blaming the AI, check whether your files hold the nuance that's in your head ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s), [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)).
- **Privacy caveat.** Data processed through Claude models goes to Anthropic. Nate accepts that for his own business data ([21:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1297s)), but for client data you may prefer open-source models and a brain outside Claude Code ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- Other graph tools he mentions: Logseq, and probably Graphiti (captioned "Graphir", *uncertain*) ([25:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1508s)).
- If you don't need relationship chains or meaning-based relationships, you probably don't need a graph ([25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s)).

**Signal to move up:** agents run unattended (captioned "offline"), there's a lot of data, and several agents (his example is Hermes agents) need to stay in sync ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)).

**Build it:** [[Build a Knowledge Graph Layer]]

---

### Level 5: Always-on brain OS

**Mechanism**
- The always-on brain OS ([25:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1526s)). The example is [[GBrain]] by [[Garry Tan]], CEO of Y Combinator ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s)), which he says pairs well with gstack ([25:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1535s)).
- It bundles everything from the lower levels: wikis, routing, relationships and tools ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)). On top, it keeps syncing and refreshing memories and adding material ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)).
- It pairs well with [[Hermes Agent]] ([25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s)). In [[Claude Code]] you would have to set up the cron jobs yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). That is part of why Nate doesn't run GBrain yet, though he is experimenting with it on Hermes ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).
- Otherwise it resembles the lower levels. The difference is that it updates itself and runs autonomously ([26:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1565s)).

**Risks and Nate's counter-position**
- **Too much context.** When does extra context start doing more harm than good ([26:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1573s))?
- **He prefers manual control of ingest** ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)). For example, a skill pulls the week's meeting transcripts, then he decides with the agent what to ingest ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)).
- **Context vs connections.** His "four C's" are context, connections, capabilities and cadence. For a second brain he focuses on the first two ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s), [26:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1609s)). See [[Context vs Connections]].
  - **Ingest context:** durable, locked-in material. Example: quarterly projects with their decisions and statuses, captioned "OTAs" (the exact term is *unclear in captions*) ([27:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1621s), [27:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1636s)).
  - **Don't ingest connections:** fast-changing data like Slack threads, email and customer data ([27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s), [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)). Ingesting it adds noise and means monthly clean-ups ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s), [27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)).
  - **His filter:** would this memory still be useful in a year? ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s))
  - **Keep connections reachable:** make sure the brain can fetch them live ([28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)).
- **Tiered lookup.** Nate's example is a vague question about what he and a colleague recently said about a quarterly project ([28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)). The brain checks sources in order:
  1. the quarterly-project file ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s))
  2. the wiki and meeting transcripts ([28:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1702s))
  3. the live ClickUp conversation as a last resort ([28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s))

  That still counts as a second brain, because it knows where to look and in what order ([28:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1713s)). See [[Tiered Lookup Routing]].

**Signal to adopt it:** see the Level 4 signal above, and weigh it against the context-overload risk and the scheduling work it adds in Claude Code ([26:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1573s), [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). To check your own symptoms, run the [[Second Brain Pain-Point Audit]].

---

### Choosing your level

- **It is not a ranking.** Level 5 isn't "best" ([03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s)). Pick the simplest level that fits your needs ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)).
- **No pain, no new architecture.** Without a pain point there's no reason to experiment with a new setup ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s), [04:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=255s)). Moving up doesn't automatically mean better. Find the pain point and the level that fixes it ([19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s), [19:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1161s)).
- **Mix levels per folder.** A brain doesn't have to be one style throughout. Not everything needs GraphRAG, and not everything needs to be an LLM Wiki ([17:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1069s), [17:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1078s)). Choose per folder, based on the data and how you use it ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)). One folder can be Level 2, another Level 4, another Level 3 ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).
- **Nate's own position:** Herk2 runs almost entirely at Level 2 ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)). No knowledge graph day to day ([19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s)) and no GBrain yet ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).
- **His overall test:** does the brain know where your data lives and where to look, and does it return accurate answers ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s))?

#### Finding Your Level diagnostic

This is the symptom-to-level mapping from [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s). To run it on your own setup, see [[Second Brain Pain-Point Audit]].

| If your pain is… | Look at | Timestamp |
|---|---|---|
| You keep re-explaining your setup and need to find things by exact words or file names | Level 1: [[CLAUDE.md as a Router]] | [28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s) |
| You have 30+ notes and keep forgetting what's in them | Level 2: [[LLM Wiki]] (ingest them into a linked wiki) | [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s) |
| The agent misses notes you know exist, and routing isn't fixing it | Level 3: [[Semantic Search]] (no exact-word match needed) | [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s) |
| You need relationships, and to follow chains of questions and thoughts | Level 4: [[Knowledge Graphs]] | [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s) |
| Agents run unattended (captioned "offline"), there's a lot of data, and several Hermes agents need to stay in sync | Level 5: [[Always-On Brain OS]] such as [[GBrain]] | [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s) |

#### Team brains

- Nate touches on this only briefly ([29:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1780s)).
- **The tool isn't the main question.** Google Drive, Notion, GitHub or plugins matter less than keeping shared content useful rather than noise ([29:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1799s)).
- **The harder parts are adoption and change management:** process owners keep their docs updated, and colleagues look things up there instead of pinging people ([30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)).
- **Get your own brain working first.** Only then tackle the team-wide version ([30:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1828s), [30:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1834s)).

## When to use it — and when not to

**Use the framework:**
- as a diagnostic when retrieval hurts: re-explaining, forgotten notes, missed files, or questions that need relationships
- when deciding how to structure a *new* folder or data type ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s))

**Don't use it:**
- as a ladder to climb for its own sake or for the visuals. The graph views that open the video are the hook, not the value ([09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s), [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s))
- to force one level onto the whole vault ([17:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1078s))
- to justify ingesting volatile data. Route to live sources instead ([28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s))
- when nothing is broken ([04:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=255s))

**Cheapest fixes first:** before moving up, check routing (Level 1 symptoms) and capture quality ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)). A higher level won't fix files that never held the knowledge.

## Other level frameworks

Two more sources also use "levels", but they level different things. Everything above is Nate Herk's five-level retrieval model. Always say whose "Level 2" you mean.

| Framework | What it levels | Levels |
|---|---|---|
| [[Nate Herk - Every Level of a Claude Second Brain]] | How the brain *retrieves* | 1 router · 2 LLM wiki · 3 semantic search · 4 knowledge graph · 5 always-on ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)) |
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | The *memory* element of his ARMS agentic OS (Applications, Routines, Memory, Skills) ([04:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=259s)) | 1 flat workspace · 2 router files · 3 visual second brain ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s), [11:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=697s), [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)) |
| [[Chase AI - The Agentic OS Setup for Claude Code]] | The *whole agentic OS* | 1 skills, automations and loops · 2 memory and state · 3 interface · 4 distribution ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s)–[03:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=190s)) |

Both of the other frameworks are covered more broadly in [[Agentic OS]].

### Jay E's memory ladder

- **Where memory sits.** It is one of four ARMS elements. He says to learn them bottom-up: skills first, then memory, then routines and applications ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)–[04:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=283s)). Each element gets three levels ([04:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=289s)).
- **Level 1: a workspace with a bunch of files.** His is a folder called Robo ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)–[10:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=654s)). With only a few files this works fine ([10:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=657s)).
  - **When it breaks:** files build up until the agent struggles to find things ([11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s)). When he pointed his second-brain viewer at the folder, he found about 60,000 files ([11:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=670s)–[11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s)). He says that slows retrieval and eats into your plan's usage faster ([11:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=681s)–[11:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=690s)); he doesn't measure it.
  - **Trigger to move up:** you notice memory retrieval slowing down ([11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)).
- **Level 2: a workspace organised for the agent** ([11:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=697s)).
  - Tidy, human-friendly file names and folder navigation in a file explorer matter much less now that agents operate on the files ([12:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=722s)–[12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s)).
  - The minimum is router files ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)). CLAUDE.md is the central router. It describes his departments (content, community and so on) so Claude works inside the right set of files for each ([12:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=745s)–[12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)).
  - Each department has its own router file. For example, content.md is just a list of content skills and reference files ([12:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=765s)–[13:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=783s)).
  - The goal is the fewest steps to the right file ([13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)–[13:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=809s)). His setup prompt is on screen only, not spoken ([13:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=812s)). This two-tier router is a variant of [[CLAUDE.md as a Router]].
- **Level 3: a visual second brain** ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)).
  - It shows how files and folders connect and lets you search faster ([13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s)–[13:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=838s)).
  - He values it for visual people and for explaining systems to others ([14:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=845s)–[14:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=857s)). It also finds and previews a skill immediately, where a file explorer is slow ([14:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=857s)–[14:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=872s)).
  - It is an app he built himself ([20:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1243s)), with CLAUDE.md at the centre ([12:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=743s)). He doesn't name any tool behind it. See [[Obsidian]] for the comparison.

### Chase's agentic OS levels

- **Level 1, the backbone:** everything you do in Claude Code turned into skills or automations, plus loop engineering ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s)). See [[Workflow Audit into Skills]] and [[Loop Engineering]].
- **Level 2, memory and state.** This is a store of information the OS can draw on, in Obsidian or a standard database ([02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)–[02:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=138s)). It works together with the Level 1 skills and automations so loops can improve themselves ([02:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=140s)–[02:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=161s)). What he puts in it:
  - a coherent file structure, which he claims gets you about 99% of the way without a database or Obsidian ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s))
  - Karpathy-style raw/, wiki/ and outputs/ folders with an index.md at every level ([17:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1056s), [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s))
  - a vault CLAUDE.md with the structure and a navigation pattern ([21:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1307s)–[22:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1331s))
  - logged runs that loops can read ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s))

  Details are in [[LLM Wiki]] and [[Ingest Sources into an LLM Wiki]].
- **Level 3, interface:** a custom visual wrapper, as a web app or inside Obsidian ([23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s)–[23:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1418s)). **Level 4, distribution:** handing that interface to teammates and clients ([28:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1717s)). See [[Build an Agentic OS Dashboard]].
- **Where he says the value is:** Levels 1–2 hold about 90% of it ([02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s)), and both work in a plain Claude Code terminal or Codex ([03:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=224s)). Levels 3–4 are the cherry on top ([30:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1826s)).

### Rough correspondence between the three

*This comparison is drawn by this note. Each cell cites what its source actually says.*

| Nate's retrieval level | Closest in Jay E's memory ladder | Closest in Chase's agentic OS |
|---|---|---|
| Nothing below Level 1; Nate says everyone starts with a router ([04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s)) | Level 1, flat workspace ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)) | His failure case: one folder of millions of files with no hierarchy ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s)) |
| Level 1, CLAUDE.md as a router ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)) | Level 2, CLAUDE.md plus department routers ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)) | Part of Level 2: vault CLAUDE.md with a navigation pattern ([22:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1327s)) |
| Level 2, LLM Wiki ([08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s)) | No equivalent | Part of Level 2: raw/wiki/outputs with nested indexes ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)) |
| Levels 3–4, semantic search and knowledge graph | No equivalent | No equivalent; he says structure gets you 99% of the way ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)) |
| Level 5, always-on: the brain keeps itself synced ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) | Scheduling is a separate element, Routines, not memory ([14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s)) | Scheduling sits in Level 1 as automations ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s)), not in memory |
| Not a level: a visual view is optional ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s)) | Level 3, visual second brain ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)) | Not a memory feature: Level 3 is the interface ([23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s)) |

### Where these frameworks clash

- **Same numbers, different meanings.**
  - "Level 1" means a router (Nate), skills and automations (Chase), or a flat workspace (Jay E).
  - "Level 2" means an LLM wiki (Nate), memory and state as a whole (Chase), or router files (Jay E).
  - Chase's Level 2 roughly covers Nate's Levels 1–2 combined.
- **When to add a router.**
  - Nate treats a router as the starting point for everyone ([04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s)).
  - Jay E adds routers only once retrieval slows as files pile up ([11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)).
- **Is a visual second brain the top of the ladder, or optional?**
  - **Nate:** the graph visuals are the hook, not the value ([09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s)–[10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)). Install [[Obsidian]] only if visuals help you; he rarely opens it ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s), [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).
  - **Jay E:** a visual second brain is his *highest* memory level ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)). He also says his visual dashboard as a whole (the viewer opens from it) captures only about 20–30% of an agentic OS's value ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s)), and what he credits the viewer with helps the human: explaining, seeing connections, finding and previewing files ([13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s)–[14:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=872s)).
  - **Chase:** sits between them. Obsidian isn't required ([13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s)), but he shows its graph as the map ([16:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1008s)). He says the point of a UI is one-stop visibility, not the visuals ([26:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1567s)).
  - **Reconciling them** (this note's reading): no source claims the visual layer improves what the agent retrieves. Treat it as optional for agent retrieval, and worth building when humans need to see or explain the system.
- **Should humans be able to navigate the folders too?**
  - Nate's test is whether the agent can find it *and you could* ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)). He shows himself drilling through folders by hand ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s)).
  - Jay E says human-friendly names and file-explorer navigation matter much less now ([12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s)). He gives humans the visual viewer instead.
- **How high you need to go.**
  - Chase's "structure gets you 99% of the way" ([14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s)) and Jay E's three-rung ladder both stop before semantic search and graphs.
  - Nate keeps those levels for specific pains: one fact buried in a huge text ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)), or following relationship chains ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)).
  - All three agree on starting simple and moving up only when something hurts.

### Newer sources on how far up to go

- **Chase, earlier and blunter.** In [[Chase AI - The Three-Step Claude Code Agentic OS]] (May 2026) he says 99.9% of people need neither [[LightRAG]] nor a vector database, because Claude Code handles plain markdown in an Obsidian vault fine ([11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s)). That writes off Levels 3–4 for almost everyone, where Nate keeps them for specific pains ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s), [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)). Yet his own research domain lists LightRAG work among his tasks ([02:22](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=142s)).
- **Nate's April scale line** (under Level 2 failure modes) sits between them ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)).
- **A CRM isn't automatically graph territory.** Matt Wolfe's markdown CRM handles personal recall (see Level 4). He also rates the wiki and journal as the parts most useful to most people, and says a CRM may not be what you need ([02:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=156s)).
- *Reconciling them (this note's reading):* the split is mostly about scale and question shape. Personal brains rarely hit Nate's Level 3–4 triggers, which is Chase's point. Large corpora and relationship-chain questions still do.

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] by [[Nate Herk]] is the source of the five-level framework.
  - **Stance:** pragmatic minimalism. The lowest level that solves real pain, mixed per folder ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).
  - **Evidence:** he runs his real Herk2 project at Level 2 ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)).
  - **Scepticism toward Level 5:** too much auto-ingested context can hurt, and he prefers controlling what goes in ([26:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1573s), [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
  - **Credits:** the LLM Wiki pattern to [[Andrej Karpathy]] ([08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s)), GBrain to [[Garry Tan]] ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s)), and Grill Me to [[Matt Pocock]] ([20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s)).
  - **Resources:** his customised Grill Me skill ([20:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1246s)), his other skills and resources from the video ([30:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1842s)) and the slide deck ([30:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1848s)) are shared in his free [Skool community](https://www.skool.com/ai-automation-society/about).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]] by [[Jay E]] offers a simpler three-rung memory ladder inside his ARMS agentic OS.
  - **Stance:** organise the workspace for the agent. Once a flat workspace slows down, add router files, then a visual second brain ([11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s), [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)).
  - **Evidence:** his own workspace of about 60,000 files ([11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s)). The claimed effect on speed and plan usage is not measured.
  - **Gaps compared with Nate:** no wiki, semantic-search or graph tiers. He ranks the visual layer higher than Nate does ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]] by [[Chase AI]] makes memory and state Level 2 of a four-level agentic OS ([02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)).
  - **Stance:** a coherent file structure with index files at every level and a vault CLAUDE.md does most of the work ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s), [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)). Memory also has to hold logs of skill and automation runs so loops can improve ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)).
  - **Gaps compared with Nate:** he doesn't cover semantic search, graphs or auto memory. The "90%" and "99%" figures are opinions ([02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]], his earlier May video, makes memory step 2 of three ([07:32](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=452s)) and sets the ceiling lower: no LightRAG or vector database for 99.9% of people ([11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s)).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] is Nate's April Level 2 build. It adds a rough scale limit for wikis ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)).
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] stays at Level 2 and adds journal and CRM folders to the same markdown vault ([21:43](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1303s)).

## Beyond the source

*Not from the videos. Each item below was checked against the linked page.*

- **Auto memory lives outside the project by default.** The video shows a memory file inside the example project folder. Claude Code actually stores auto memory per project at `~/.claude/projects/<project>/memory/`, in a `MEMORY.md` index plus topic files.
  - Only the first 200 lines (or 25KB) of `MEMORY.md` load at session start. Topic files are read on demand.
  - Auto memory is **on by default**. The `/memory` toggle saves `autoMemoryEnabled`, and an `autoMemoryDirectory` setting can relocate it.
  - For the Codex port, point AGENTS.md at the real memory directory, or relocate/copy the memory into the project.
  - Source: [Claude Code docs: memory](https://code.claude.com/docs/en/memory)
- **Official way to share instructions with AGENTS.md.** Claude Code reads CLAUDE.md, not AGENTS.md. The docs suggest a CLAUDE.md that imports it with `@AGENTS.md`, or a symlink. Imported files still load into context at launch.
  - The docs also recommend keeping each CLAUDE.md under about 200 lines, which matches Nate's warning about router bloat.
  - Source: [Claude Code docs: memory](https://code.claude.com/docs/en/memory)
- **AGENTS.md is an open format** read by OpenAI Codex and many other coding agents. That is why it works as the portable twin of CLAUDE.md. Source: [agents.md](https://agents.md/)
- **Karpathy's gist anticipates the Level 2 → 3 step.** It describes raw sources, an LLM-maintained wiki and a schema file, with an `index.md` and an append-only `log.md`. It notes that an index file is enough at small scale, but a growing wiki needs proper search (it points to a local hybrid BM25/vector tool). Source: [Karpathy, llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Karpathy's own scale figures.** Nate relays Karpathy's post as about 100 articles and half a million words ([02:55](https://www.youtube.com/watch?v=sboNwYmH3AY&t=175s)). The post says roughly 100 articles and 400K words. The gist places the index-only approach at moderate scale, about 100 sources and hundreds of pages, which fits Nate's "hundreds of pages" line. Sources: [VentureBeat on Karpathy's post](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an), [Karpathy on X](https://x.com/karpathy/status/2039805659525644595), [Karpathy, llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Embeddings have far more than three dimensions.** The "three-dimensional space" is a mental model. Real embeddings are high-dimensional: OpenAI's text-embedding-3-small defaults to 1536 dimensions and text-embedding-3-large to 3072. Source: [OpenAI embeddings guide](https://developers.openai.com/api/docs/guides/embeddings)
- **GBrain spans Levels 3–5 in one package.** It is MIT-licensed and keeps knowledge as markdown in git, synced into Postgres.
  - Search combines vector search, keyword search and reciprocal-rank fusion, plus a typed knowledge graph.
  - A background "dream cycle" runs enrichment jobs such as de-duplication and contradiction checks.
  - It connects to Claude Code, Codex, Hermes and OpenClaw over MCP.
  - Source: [garrytan/gbrain on GitHub](https://github.com/garrytan/gbrain)
- **Grill Me** is published in Matt Pocock's public skills repo as "a relentless interview to sharpen a plan or design". In the current repo it hands off to a separate `grilling` skill. That skill maps decisions as a design tree and keeps asking until every branch is explored. Nate's customised version isn't public in that repo. Sources: [mattpocock/skills: grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me), [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)

## Related

- **Principles:** [[Design for Retrieval]], [[Keyword vs Semantic vs Graph Retrieval]], [[Context vs Connections]]
- **Level concepts:** [[CLAUDE.md as a Router]], [[LLM Wiki]], [[Claude Code Auto Memory]], [[Semantic Search]], [[Knowledge Graphs]], [[Always-On Brain OS]], [[Tool-Agnostic Context Files]]
- **Techniques:** [[Second Brain Pain-Point Audit]], [[Build a Level 1 Second Brain]], [[Ingest Sources into an LLM Wiki]], [[Add Semantic Search to One Folder]], [[Build a Knowledge Graph Layer]], [[Grill Me Interview Skill]], [[Tiered Lookup Routing]], [[Port a Claude Code Brain to Other Agents]]
- **Tools:** [[Claude Code]], [[OpenAI Codex]], [[Hermes Agent]], [[Obsidian]], [[Qdrant]], [[LightRAG]], [[GBrain]]
- **Other level frameworks:** [[Agentic OS]] · [[Workflow Audit into Skills]] · [[Loop Engineering]] · [[Build an Agentic OS Dashboard]]
- **Newer builds:** [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Add a Journal and Personal CRM to a Second Brain]]
- **People:** [[Nate Herk]] · [[Jay E]] · [[Chase AI]] · [[Matt Wolfe]]
- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Chase AI - The Three-Step Claude Code Agentic OS]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] · [[Home]]
