---
type: concept
aliases: ["Relationship Graph", "GraphRAG"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tags: [topic/second-brain, topic/knowledge-graph, topic/retrieval, topic/rag, topic/privacy]
---

# Knowledge Graphs

## In one sentence

A knowledge graph stores your information as **entities** (people, companies, products, programmes) joined by **typed, named relationships** ("works at", "endorsed by", "competitor of"). An agent can then follow a chain of connections from one thing to another. It is Level 4 of [[Second Brain Levels]] ([19:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1168s), [23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s)).

## How it works

### The question a graph answers

- Each level of the ladder answers a different question. At Level 4 the question is: can you ask about topic X and trace the connections all the way back to topic A? ([03:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=221s))
- The video opens on three views of data that get richer step by step. The last view goes past files that just link back to each other and shows how everything fits together. Nate calls this *relationship mapping* ([00:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=26s)).
- In his "finding your level" checklist, a graph is the answer when you want relationships and the ability to follow chains of questions and thoughts ([29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s)).

### Entities plus typed relationships (demo)

In the Level 4 example project, Nate adds a knowledge-graph folder next to everything from the lower levels ([23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)). The entities and relationships below are **fictional demo data**:

| Entity A | Relationship | Entity B | Timestamp |
|---|---|---|---|
| Jordan (person) | works at | Acme (company) | [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s) |
| Acme | is endorsed by | Postpilot | [23:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1418s) |
| Postpilot | is a competitor of | Cadently | [23:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1420s) |

The point is that the folder records more than which entities exist. It also records how each one relates to the others ([23:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1422s)).

### Graph edges vs wiki backlinks

A common objection: "My wiki already has links, so isn't that a knowledge graph?" Nate says not exactly ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)).

| | [[LLM Wiki]] links (Level 2) | Knowledge graph (Level 4) |
|---|---|---|
| What a link means | A plain "see also" or backlink. It says two pages are connected, not how ([12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)) | A named relationship, such as one thing being endorsed by another ([12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s)). A second example relation he gives is *(unclear in captions)* |
| How the agent moves | Starts at the wiki index and drills down page by page ([11:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=713s), [12:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=721s)). It follows a trail and reads each page in full ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)) | Follows relationships from entity to entity ([24:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1496s)) |
| Kind of relationship | Some relationships, but not the meaning-carrying kind you get from semantic or graph systems ([12:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=734s)) | Relationships with explicit meaning |
| Retrieval cost | Has to read every file it opens. If the agent is looking at an "AI video production" page and only needs the ElevenLabs detail, it still reads the whole file ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s), [24:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1444s)) | Can be lighter in that respect ([24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)) |
| Net effect | The two are similar and can achieve a similar effect, but they are not the same ([12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)) | |

### Where the graph sits in the brain

- The Level 4 example keeps everything from the levels below it. It has the CLAUDE.md router (plus an identical AGENTS.md), the "where things live" routing to context, projects and decisions, the wiki, and a growing memory file. The graph is one extra layer on top ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s), [23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s)). Nate sums up the plain-folders-and-markdown base as "boring is beautiful" ([23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s)). See [[CLAUDE.md as a Router]] and [[Tool-Agnostic Context Files]].
- You don't need a graph for everything. Having a second brain doesn't mean every folder needs GraphRAG. Choose a structure per folder based on the data and how you'll use it ([18:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1082s)). One folder might be Level 2 while another is Level 4 ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).

### A real graph: LightRAG over his business data

- The graph at the start of the video is [[LightRAG]] running over what he says is essentially his whole business second brain. Parts of it are blurred ([24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s)). With that much data, zooming in slows his computer down ([24:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1466s)).
- The edges carry labels such as *collaborates with* and *builds* ([24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s)).
- Expanding one node, his 7-day AI challenge, shows that it was *provided from* YouTube. It also *connects to* the onboarding process of AIS Plus (as captioned) and was *developed by* a named person ([24:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1486s), [24:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1492s)).
- This is roughly the same data he views as a wiki in [[Obsidian]], but Obsidian doesn't show that level of relationship between entities ([24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)).

### Getting data into a graph is the real problem

- If you decide you need a graph, say for all your projects, the data **probably already exists** in your files ([20:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1210s), [20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s)).
- Whatever graph software you pick is usually good at processing that material and building the relationships ([20:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1224s)). What you have to solve is **giving it enough data** ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).
- His fix is brainstorm sessions with a skill called Grill Me. It originally came from [[Matt Pocock]] and he has customised it ([20:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1237s), [20:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1240s)). He shares his version in his free [Skool community](https://www.skool.com/ai-automation-society/about) ([20:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1246s)). The skill interviews you relentlessly on one topic, writes a brainstorm file, and only stops once it knows everything ([20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s)). See [[Grill Me Interview Skill]].
- For a client or business graph, run it once per entity ("grill me about client A", then client B, then business A). You can feed it files, transcripts and contracts along the way ([21:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1265s), [21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s)).
- Before blaming the AI's retrieval, check whether your folders actually hold all the nuance that is in your head. Retrieval is sometimes the problem, but sometimes the bigger one is getting knowledge out of your head and into the system ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s), [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)).
- **Privacy caveat.** Interviewing Claude about clients means that data is sent to Anthropic when Claude processes it. Nate accepts that for his own business data. If you can't, for example with client data, he suggests open-source models, or not keeping the everything-brain in [[Claude Code]] ([21:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1286s), [21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)).

### Tooling named in the video

- Graphs are usually the most complex level and sometimes the most expensive, depending on the platform. Open-source software is always an option ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s), [19:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1177s)).
- [[LightRAG]] is his live example ([24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s)). He names Logseq and a tool captioned "Graphir" as other options, and offers a deeper video if viewers want one ([25:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1505s)). "Graphir" is probably Graphiti, but that is uncertain.

## When to use it — and when not to

| Signal in your situation | What it points to |
|---|---|
| You need to follow relationship chains, going from X through connected entities back to A ([29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s)) | A knowledge graph |
| CRM-heavy work: many businesses and clients to keep track of ([19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s)) | A graph would probably make much more sense ([20:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1205s)) |
| Project-based, content-heavy work like Nate's ([19:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1195s)) | Routing files and wikis were enough for Nate's needs ([19:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1189s)) |
| You don't need relationship chains or semantic-style relationships ([25:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1516s)) | Skip the graph |
| Your current setup causes no real pain ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)) | Don't build a new architecture |

- **Nate's own position:** he has experimented with graphs a lot but doesn't use them day to day. He found ways to meet his needs with routing files and wikis ([19:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1183s), [19:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1189s)). He runs essentially all of Herk2 at Level 2 ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)). He puts a lot of care into ingesting wiki material with context, and that gives him enough of a relationship feel ([23:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1425s), [23:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1435s)).
- **Higher isn't automatically better.** Look for the lowest level that fixes an actual pain point ([04:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=242s), [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s)).
- **Work backwards from the questions you'll ask.** How data will be retrieved should decide how you store it ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)). If your real questions are about who connects to what, that is the case for a graph. See [[Design for Retrieval]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] frames graphs as Level 4: typed relationships between entities that let an agent trace chains, which wiki backlinks can't fully do ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s), [23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)). He is openly lukewarm about using them himself. Graphs are the most complex and sometimes costly level, and he thinks a business managing a big CRM of companies and clients would get more from one than his own project-based, content-heavy work does ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s), [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s)). His most practical advice is that the bottleneck is feeding the graph enough knowledge, not the graph software ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).

## Beyond the source

*Not from the video. Each item was checked at the link given.*

- **GraphRAG.** Microsoft Research's GraphRAG uses an LLM to pull entities and relationships out of raw text. It then groups them into a hierarchy of communities using the Leiden algorithm and writes summaries for each community. Query modes: global search answers whole-corpus questions from the community summaries. Local search fans out from specific entities to their neighbours. DRIFT search does the same but adds community-level context. Basic search is a plain top-k vector-search fallback. Sources: [GraphRAG docs](https://microsoft.github.io/graphrag/), [Microsoft Research project page](https://www.microsoft.com/en-us/research/project/graphrag/). The term is also used generically for any graph-based RAG, as in [this survey](https://arxiv.org/abs/2501.13958). *My reading:* when Nate mentions GraphRAG ([18:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1082s); captioned "graph rack") he means the general idea, not necessarily Microsoft's library.
- **LightRAG.** An open-source (MIT) graph-based RAG framework from HKUDS. It keeps a knowledge graph and vector embeddings side by side and ships a web UI for inserting, querying and visualising the graph, which fits the view shown in the video. *My inference:* because it combines both, it can cover Level 3 ([[Semantic Search]]) and Level 4 in one tool. [github.com/HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- **Graphiti** (the likely match for "Graphir"). An open-source (Apache-2.0) framework from Zep for building temporal context graphs for AI agents. It tracks how facts change over time rather than storing one static snapshot. [github.com/getzep/graphiti](https://github.com/getzep/graphiti)
- **Logseq.** A privacy-first, open-source (AGPL-3.0) platform for knowledge management and collaboration ([github.com/logseq/logseq](https://github.com/logseq/logseq)). It has bidirectional links and a graph view ([Bellingcat toolkit entry](https://bellingcat.gitbook.io/toolkit/more/all-tools/logseq)). Its own guide describes page links, embeds and block references, and every link automatically works in both directions. None of these are named or typed relationships ([Logseq blog](https://blog.logseq.com/how-to-get-started-with-networked-thinking-and-logseq/)). *My inference:* out of the box that is closer to the wiki-backlink style above than to typed graph edges. Check whether it gives you the typed relationships you need before using it for Level 4.
- **GBrain builds typed edges too.** The README describes a "self-wiring" knowledge graph. Every page write pulls entity references out of the markdown and wikilinks and writes edges with no LLM calls. Typed links include `works_at`, `invested_in`, `founded` and `advises`. So the Level 5 option also includes a Level 4 graph layer (see [[Always-On Brain OS]]). [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain)

## Related

- [[Second Brain Levels]] covers the full five-level ladder; this note is Level 4.
- [[LLM Wiki]] is Level 2, where links are backlinks rather than typed edges.
- [[Semantic Search]] is Level 3, retrieval by meaning.
- [[Keyword vs Semantic vs Graph Retrieval]] compares all three retrieval styles side by side.
- [[Build a Knowledge Graph Layer]] is the build playbook for adding this layer.
- [[Grill Me Interview Skill]] is how to get enough data into the graph.
- [[Design for Retrieval]] is about starting from the questions you'll ask.
- [[Always-On Brain OS]] is Level 5.
- [[Second Brain Pain-Point Audit]] helps decide whether you need this level at all.
- Tools and people: [[LightRAG]], [[Obsidian]], [[Claude Code]], [[Matt Pocock]], [[Nate Herk]]
- Source: [[Nate Herk - Every Level of a Claude Second Brain]]
- [[Home]]
