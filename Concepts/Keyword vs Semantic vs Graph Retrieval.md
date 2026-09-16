---
type: concept
aliases: ["Retrieval Styles Compared", "Keyword vs Vector vs Graph Search"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]"]
tags: [topic/retrieval, topic/second-brain, topic/rag, topic/knowledge-graph]
---

# Keyword vs Semantic vs Graph Retrieval

## In one sentence

A second brain can find information in four ways, and they differ in what counts as a match:
- an exact word or a routed path (Level 1)
- a followed link to a page read in full (Level 2)
- a nearby meaning (Level 3)
- a typed relationship between entities (Level 4)

Each suits a different kind of data and question, and one brain can use all four, folder by folder.

## How it works

The video lays out five levels ([[Second Brain Levels]]). Levels 1–4 are four different retrieval styles. As he describes it, Level 5 doesn't add a new way of matching: [[GBrain]] combines wikis, routing, relationships and tools, then keeps them syncing all the time [25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s) (see [[Always-On Brain OS]]).

### 1. Exact keyword / routing lookup — Level 1

- **The question it answers:** can you find a file or fact by an exact word or name? [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)
- **Mechanism:**
  - CLAUDE.md works as a router, with rules like "info about me is in this folder" and "Q1 priorities are in that folder". [04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)
  - Claude won't search your whole project on its own, and you wouldn't want it to because of the time and tokens. [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)
  - If it doesn't know where something lives, it probably won't find it. [05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)
  - The result is mostly exact-word search, depending on how you write the routing. [05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)
- **Human version:** folders you can drill into. To find a slide deck he goes projects → YouTube videos → a dated folder → the deck. [07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s) Because the routing makes sense, his agent can follow the same path. [07:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=463s)
- **Pure keyword search, for contrast:** in his "feedback" demo, the regular search in his YouTube-transcript brain lists only the places where that literal word appears. (It looks like the vault he showed in Obsidian earlier, but he doesn't name the search tool.) [14:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=885s)
- Concept: [[CLAUDE.md as a Router]] · Build: [[Build a Level 1 Second Brain]]

### 2. Wiki link-following — Level 2

- **The question it answers:** can you pull everything on one topic together? [03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)
- **Mechanism:** the wiki has indexes. Asked about agentic workflows, the agent starts at the matching index entry and drills into linked pages. His example path goes to what is most likely his WAT framework (captioned "WATC"), then to the CLAUDE.md system-prompt page. [11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)
- **What the links mean:**
  - This is following a trail and reading each page *in its entirety*. It is not a semantic or knowledge-graph relationship. [12:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=734s)
  - Does a wiki full of links count as a knowledge graph? Not quite, he says: the links don't record *how* pages relate, e.g. "endorsed by". [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)
  - They behave like "see also" backlinks. The effect can be similar, but the two aren't the same. [12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)
- **Wiki vs semantic RAG, from the April video.** [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] asks whether the wiki kills semantic-search RAG: no, but kind of yes, depending on the project's goal and how much context you have [15:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=936s). His comparison chart was one Claude Code made from Karpathy material in his own brain vault [15:45](https://www.youtube.com/watch?v=sboNwYmH3AY&t=945s).
  - *Retrieval and infrastructure:* the wiki reads indexes and follows links instead of running similarity search, which he says gives a deeper grasp of relationships than chunks that merely seem similar [16:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=973s). It needs only markdown, not even Obsidian, against an embedding model, a vector database and a chunking pipeline [16:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=985s). *Reconciling with June:* links beat chunk similarity for relationships, but unlike a graph's edges they carry no types [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s).
  - *Cost:* a wiki costs only tokens; RAG can carry ongoing compute and storage [16:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=996s).
  - *Maintenance:* lint, clean up and add articles, rather than re-embedding when content changes [16:42](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1002s).
  - *Scale:* a pile of files doesn't stretch across an enterprise, where semantic search, a knowledge graph or [[LightRAG]] likely become cheaper [16:51](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1011s). Hundreds of well-indexed pages suit a wiki; millions of documents need a traditional RAG pipeline, at least with April 2026 models [17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s).
- Concept: [[LLM Wiki]] · Build: [[Ingest Sources into an LLM Wiki]]

### 3. Semantic similarity — Level 3

- **The question it answers:** can you find something when you search with different words than you wrote? [03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)
- **Mechanism:** keyword search says "X equals X", while semantic search says X is similar to X, Y and Z. [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) Documents are chunked, each chunk is embedded, and the chunks nearest in meaning come back. [15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s)
- Concept: [[Semantic Search]] · Build: [[Add Semantic Search to One Folder]]

### 4. Typed-relationship graph traversal — Level 4

- **The question it answers:** can you ask about topic X and trace a chain of relationships back to topic A? [03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s)
- **Mechanism:**
  - A knowledge-graph folder stores entities (Jordan is a person, Acme is a company). [23:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1408s)
  - It stores typed edges between them. In the demo, Jordan is linked to Acme by *works at*, Acme to Postpilot by *endorsed by*, and Postpilot to Cadently by *competitor of*. These names are fictional demo data. [23:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1411s)
- **Real example:** a [[LightRAG]] view of his actual brain shows edges like "collaborates with" and "builds". [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s) He follows one chain: the 7-day AI challenge → came from YouTube → connects to AIS Plus onboarding → developed by a named person. [24:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1488s)
- The data is essentially the same as in his Obsidian view, but the graph shows much richer relationships between entities. [24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)
- Concept: [[Knowledge Graphs]] · Build: [[Build a Knowledge Graph Layer]]

## Comparison table

### What each style does

| Style | How it matches | Great at | Where it fails |
|---|---|---|---|
| **Keyword / routing lookup (Level 1)**: [[CLAUDE.md as a Router]] | Exact word, name or path; a routing rule tells the agent which folder to open. "X equals X" [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) | Finding a known file fast; ending the need to re-explain things, because the agent knows where to look and why [05:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=314s) | A CLAUDE.md that grows too big gets messy and ignored [05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s); anything with no routing rule [05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s); searches using different words than the note [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s) |
| **Wiki link-following (Level 2)**: [[LLM Wiki]] | Start at an index, follow "see also"-style links, read each page in full [12:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=734s) | Gathering everything on a topic [03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s); 30+ notes whose contents you keep forgetting [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s); whole-document tasks such as a meeting summary, where he'd rather the agent read a full markdown file than chunks [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s) | Wikis start to degrade at a certain point [11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s); it reads a whole page even when it needs one fact [24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s); links don't say how pages relate [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s) |
| **Semantic similarity (Level 3)**: [[Semantic Search]] | Chunks sit near the query in embedding space. X is "similar to X, Y, and Z" [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) | Lots of text plus one pinpoint answer [18:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1101s); finding notes phrased differently from the query [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s) | Summaries built from a few chunks [16:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=986s); aggregate questions over a table [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s); "not a magic solution" [16:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1007s) |
| **Graph traversal (Level 4)**: [[Knowledge Graphs]] | Entities joined by *typed* relationships, followed as chains [23:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1411s) | Relationship chains [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s); CRM-heavy work across many businesses and clients [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s); single facts without reading a whole page [24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s) | The hard part is feeding it enough data; the software handles building the relationships [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s); overkill if you don't need relationship chains [25:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1516s) |

### What each style takes

| Style | Cost / complexity | Data shape it fits | Example question from the video |
|---|---|---|---|
| **Keyword / routing lookup (Level 1)**: [[CLAUDE.md as a Router]] | Simplest, and where you always start [04:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=260s); a CLAUDE.md plus a few folders is the whole second brain [05:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=347s) | Small, always-true context: about-me, a decisions log, projects [05:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=355s) | "Find the HTML slide deck for my Claude Code features video" [07:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=440s); "what are our Q1 priorities?" [04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s) |
| **Wiki link-following (Level 2)**: [[LLM Wiki]] | Still plain markdown, but ingesting well takes real time and effort; he credits that effort for his wiki's relational feel [23:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1432s) | Many similar documents on a theme, such as YouTube transcripts or meeting transcripts [08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s) | A question about agentic workflows: index → WAT framework → CLAUDE.md system-prompt page [11:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=716s) |
| **Semantic similarity (Level 3)**: [[Semantic Search]] | A semantic-search setup (he names Obsidian, Pinecone or Supabase; demo in Qdrant) [13:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=784s) plus a pipeline of chunking, embedding, search, hybrid, re-ranking [18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s); metadata tuning helps [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s) | A large body of text in one folder (e.g. transcripts); context, projects and decisions stay markdown [17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s) | "Remind me what rule 17 was" [18:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1117s); searching "feedback" [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s) |
| **Graph traversal (Level 4)**: [[Knowledge Graphs]] | Highest: typically the most complex and sometimes the most expensive [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s); open-source software is an option [19:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1178s) | Entity-rich data: people, companies, clients, competitors, projects. It often already exists in your markdown [20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s) | Ask about topic X and trace it back to topic A [03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s); in the demo graph, following Jordan → Acme → Postpilot → Cadently [23:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1411s); tracing the 7-day AI challenge chain [24:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1488s) |

### Why a graph can be lighter than a wiki

- A wiki's drawback in Nate's framing: the agent has to open and read every file it wants. [24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)
- **His example:** the agent is researching AI video production but only needs the ElevenLabs detail. It still reads that whole page first. [24:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1444s)
- A knowledge graph can answer from the entity and its edges without loading the full page, so in that sense it is more lightweight. [24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)
- *The trade-off (drawn from the same video):* lighter to query, heavier to build. Graphs are the most complex level [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s) and need a lot of well-captured data [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s).

### Semantic vs graph: two different "relationships"

- Semantic relationships are *closeness in meaning*. In the Qdrant image demo the images carry no descriptions, yet similar ones sit together; nothing names how they are connected. [13:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=812s) [14:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=862s)
- Graph relationships are *named facts*: who works where, who competes with whom. [23:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1422s)
- Nate treats them as separate needs. If you don't need relationship chains and aren't worried about semantic-style relationships, you probably don't need a knowledge graph. [25:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1516s)

## When to use it — and when not to

**Pick from the pain, not the prestige.** Use the simplest level that meets your needs; without a pain point there's no reason to add architecture. [04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s) Decide the storage by working backwards from the questions you'll ask. [02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s) See [[Design for Retrieval]].

His "Finding your level" checklist ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s)):

| Symptom | Retrieval style to look at |
|---|---|
| You keep re-explaining your setup; you need things found by exact words or file names | Keyword / routing: Level 1 [28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s) |
| 30+ notes and you keep forgetting what's in them | Wiki link-following: Level 2 [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s) |
| The project misses notes you know exist, and routing isn't fixing it | Semantic similarity: Level 3 [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s) |
| You need relationships and want to follow chains of questions | Graph traversal: Level 4 [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s) |

- **Mix styles by folder.** A whole project doesn't sit at one level: one folder can be Level 2, another Level 4, another Level 3. [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s) Not everything needs GraphRAG, and not everything has to be an LLM Wiki. [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s)
- **Chain styles in a lookup order.** His example is a vague question about what he and a colleague discussed last week on one of the quarter's projects (captioned "OTA"; the exact term is unclear in captions). The brain first checks the quarterly-projects file, then the wiki and meeting transcripts, and finally pulls live data from ClickUp. [28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s) Build: [[Tiered Lookup Routing]].
- **Whole-document questions beat chunks.** For a summary or a table-wide maximum, give the agent the full markdown file instead of vector chunks. [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)
- **Before blaming retrieval, check capture.** Often the bigger problem is getting what's in your head into the system, not the system's retrieval. [22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s) See [[Grill Me Interview Skill]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] ([[Nate Herk]]):
  - His main second brain, Herk2, sits almost entirely at Level 2. [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)
  - He has experimented a lot with knowledge graphs but doesn't use them day to day. Routing files and wikis fit his project-based, content-heavy work. [19:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1182s)
  - He says a large CRM with many businesses and clients would probably justify a graph. [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s)
  - He says moving up a level doesn't necessarily mean better. [19:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1158s)
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (April): gives Level 2 a cost, maintenance and scale comparison against semantic RAG that the June video lacks; see the Level 2 section above. [16:36](https://www.youtube.com/watch?v=sboNwYmH3AY&t=996s)
- *Caption notes:*
  - "graph rack" → GraphRAG; "Lightrag" → LightRAG; "a genetic workflow" → agentic workflows.
  - "WATC framework" is most likely his WAT framework (Workflows, Agents, Tools).
  - At [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s) he says he hasn't felt enough pain to move to "level two", but from context he means Level 3.

## Beyond the source

*Not from the video. Each item was checked against the linked page.*

- **Claude Code's own search is Level-1 style pattern matching.**
  - Claude Code's tools reference: on macOS, Linux and WSL, Claude searches with `find` and `grep` through the Bash tool, which run embedded `bfs` and `ugrep`.
  - The dedicated Glob (file-name patterns) and Grep (ripgrep regex) tools are in the default set on Windows.
  - Out of the box, it finds things by pattern, not by meaning. That is why routing rules or an added semantic layer matter. — <https://code.claude.com/docs/en/tools-reference>
- **Keyword and semantic aren't either/or.** Hybrid search runs sparse (keyword-style) and dense (semantic) retrieval together and merges the rankings, e.g. with Reciprocal Rank Fusion. — <https://qdrant.tech/documentation/concepts/hybrid-queries/>
  - Anthropic's contextual-retrieval approach pairs embeddings with BM25, because exact matching catches identifiers and technical terms that embeddings can miss. — <https://www.anthropic.com/news/contextual-retrieval>
- **Semantic and graph aren't either/or either.** [[LightRAG]], the tool in Nate's graph demo, stores both a knowledge graph and vector embeddings. Its query modes:
  - *naive*: traditional chunk-based vector retrieval, with no graph
  - *local*: precise matching of specific entities and their local context
  - *global*: broad themes, reasoning across documents, deeper relationships between entities
  - *hybrid*: local + global
  - *mix*: local, global and naive combined
  - — <https://github.com/HKUDS/LightRAG>
- **Graphs also help with dataset-wide questions.** Microsoft Research reports that baseline vector RAG does poorly on questions that pull together information across a whole dataset (e.g. "top 5 themes"). GraphRAG handles them using pre-summarised clusters in an LLM-built knowledge graph. This adds to Nate's advice: for corpus-wide questions, a graph is an alternative to reading every file. — <https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/>
- **A size rule of thumb for "just read it all".** Anthropic suggests that a knowledge base under roughly 200,000 tokens can go straight into the prompt (with prompt caching) instead of using retrieval. — <https://www.anthropic.com/news/contextual-retrieval>

## Related

- [[Second Brain Levels]] · [[Design for Retrieval]] · [[Tiered Lookup Routing]] · [[Second Brain Pain-Point Audit]]
- Level 1: [[CLAUDE.md as a Router]] · [[Build a Level 1 Second Brain]]
- Level 2: [[LLM Wiki]] · [[Ingest Sources into an LLM Wiki]]
- Level 3: [[Semantic Search]] · [[Add Semantic Search to One Folder]]
- Level 4: [[Knowledge Graphs]] · [[Build a Knowledge Graph Layer]]
- Level 5: [[Always-On Brain OS]]
- Tools: [[Claude Code]] · [[Obsidian]] · [[Qdrant]] · [[LightRAG]] · [[GBrain]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]
- [[Home]]
