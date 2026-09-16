---
type: tool
category: graph-based RAG framework
website: https://github.com/HKUDS/LightRAG
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]"]
tags: [topic/knowledge-graph, topic/rag, topic/retrieval, topic/second-brain]
---

# LightRAG

## What it is

In [[Nate Herk - Every Level of a Claude Second Brain]], LightRAG is the relationship-graph tool [[Nate Herk]] runs over his real business data. He points to it as the graph behind the opening visuals [24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s) and uses it for the Level 4 demo. Its edges carry named relationships such as "collaborates with" and "builds" [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s). It's his example of a [[Knowledge Graphs|knowledge graph]] layer, as opposed to a wiki of backlinks.

## How sources use it

- [[Nate Herk - Every Level of a Claude Second Brain]]:
  - **Intro:** the hook visuals of relationship mapping [00:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=26s), [00:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=34s).
  - **Level 4:** a live demo over essentially his entire second brain and business [24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s), [24:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1461s).
  - **Comparison:** the same data viewed as an Obsidian wiki [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (April 2026): named, not demoed, as an enterprise-scale alternative to a file wiki.
  - A wiki of plain files doesn't scale across an enterprise, where semantic search, a knowledge graph or LightRAG gets cheaper [16:51](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1011s), [17:05](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1025s). Hundreds of well-indexed pages are fine as a wiki; at millions of documents, move to a traditional RAG pipeline [17:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1033s).

### Opening visuals

- **Three stages of structure.** The video opens on three visuals of increasingly structured data [00:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=4s):
  1. Context starting to form, with relationships, nodes and entities appearing [00:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=8s).
  2. More knowledge and relationships, producing distinct clusters whose nodes visibly relate to each other [00:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=15s), [00:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=21s).
  3. Relationships taken further, so you see how everything fits together rather than files that merely link to each other [00:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=26s), [00:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=31s). He calls this relationship mapping [00:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=34s).
- **It's his real data.** It all comes from his actual project, Herk2 [01:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=62s).
- **Which visual is LightRAG.** At Level 4 he says the LightRAG graph is the example from the start of the video [24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s). He doesn't say which of the three opening visuals it is.

### Level 4 demo: LightRAG over his business

- **Real data, so some of it is blurred.** It's essentially his entire second brain and business [24:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1461s).
- **Too much data slows it down.** Zooming in bogs down his computer [24:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1466s). He admits he probably shouldn't have loaded that much data into the demo [24:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1471s).
- **Edges carry named relationships** [24:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1469s), such as "collaborates with" and "builds" [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s), [24:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1476s). Opening up the node circles shows how things are related [24:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1481s).
- **Worked chain.** Starting from his 7-day AI challenge [24:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1486s):
  - it came from YouTube [24:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1488s);
  - it connects to the onboarding process for AIS Plus (as captioned) [24:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1492s);
  - it was developed by Aiden (name as captioned) [24:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1494s).
  - You can keep following relationships from node to node like this [24:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1496s).
- **Same data, richer relationships.** It's roughly the same data he views in Obsidian [24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s), but Obsidian doesn't give that level of relationship between entities [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s).

### Wiki vs LightRAG graph over the same data

| | LLM Wiki viewed in [[Obsidian]] (his Level 2) | LightRAG graph (Level 4) |
|---|---|---|
| What a link means | "See also" backlinks that don't say how things relate [12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s), [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s) | Named relations such as "collaborates with", "builds", "developed by" [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s), [24:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1494s) |
| How the agent navigates | Follows a trail through the index and reads each page in full [12:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=744s), [24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s) | Can be more lightweight: no need to read a whole page for one detail [24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s) |
| Example cost | Needs only the ElevenLabs detail but still reads the whole AI-video-production page [24:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1446s) | Follows the relevant relationship chain [24:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1496s) |
| His daily use | The wiki, yes: nearly all of Herk2 sits at Level 2 [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s). The Obsidian view itself, hardly ever [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s) | He has played with knowledge graphs a lot but doesn't use them day to day [19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s) |
| Why | Careful ingestion with context gives him enough sense of how things relate [23:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1432s) | Worth it when you need relationship chains [25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s) |

### When a graph tool like LightRAG is worth it

- **The question Level 4 answers:** can you ask about topic X and trace the chain back to topic A [03:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=221s)?
- **The costs.** Knowledge and relationship graphs are usually the most complex option [19:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1172s). They can also be the most expensive if you run them on certain platforms [19:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1175s). Open-source software is the alternative [19:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1178s).
- **Fit depends on your work.** His is project-based and content-heavy, with no big CRM [19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s). If he managed many businesses and clients, he thinks a graph would probably make sense [20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s).
- **Symptom that points here:** you want relationships and the ability to follow chains of questions and thoughts [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s).
- **Skip it** if you don't need relationship chains or meaning-level relationships [25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s).
- **Don't graph everything.** Not everything needs GraphRAG; choose per folder, based on the data and how you use it [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s), [18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s). See [[Second Brain Pain-Point Audit]].

### Feeding it: data is the bottleneck, not the software

- **You probably have the data already.** If you decide a graph is needed, say for all your projects, the data probably already sits in your folders [20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s).
- **The software is the easy part.** Graph tools are usually good at building the relationships [20:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1224s). The problem you have to solve is giving them enough data [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s).
- **Use Grill Me to fill gaps.** Run interview sessions with the Grill Me skill [20:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1237s), one per client or business [21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s), and feed in files, transcripts and contracts [21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s). See [[Grill Me Interview Skill]].
- **Check your files before blaming retrieval.** Make sure your folders actually capture the nuance in your head [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s), [22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s).
- **Privacy.** In an aside added while editing, he notes that data you send through Claude models goes to Anthropic, so it isn't private [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s). He's comfortable doing that with his own business data [21:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1297s). If you don't want to send client data, consider open-source models, and maybe keep that all-knowing brain out of Claude Code [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s).

## Notes

- **Tool vs hand-built folder.** His example Level 4 project adds a markdown **knowledge-graph folder** next to the wiki [23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s), [23:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1406s). It holds typed entities and relationships, e.g. Jordan (a person) works at Acme (a company) [23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s), [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s), Acme is endorsed by Postpilot, and Postpilot is a competitor of Cadently [23:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1418s). These are fictional demo entities. LightRAG is the tool-driven version of that idea, applied to real data. See [[Build a Knowledge Graph Layer]].
- **No setup shown.** Neither video shows how LightRAG was installed, configured or fed, or which model built the graph. Use the verified details below for a build.
- **Other graph tools named, not compared.** He mentions Logseq and a tool captioned "Graphir" (probably Graphiti, *uncertain*) [25:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1508s). He doesn't compare them with LightRAG.
- **Scale caution.** His own demo lagged under the volume of data [24:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1466s). Together with his advice to choose a structure folder by folder [18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s), that suggests starting a graph on one bounded folder.

## Beyond the source

*Not said in either video; verified at the links given.*

- **What it is.** LightRAG ("Simple and Fast Retrieval-Augmented Generation") is an MIT-licensed open-source project from HKUDS, the Data Intelligence Lab at the University of Hong Kong. Sources: https://github.com/HKUDS/LightRAG · https://github.com/HKUDS
- **Paper.** Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao and Chao Huang, *LightRAG: Simple and Fast Retrieval-Augmented Generation*, arXiv 2410.05779, first submitted October 2024. The README lists it as an EMNLP 2025 paper. Sources: https://arxiv.org/abs/2410.05779 · https://github.com/HKUDS/LightRAG
- **How indexing works** (per the paper):
  - An LLM extracts entities (nodes) and relationships (edges) from text chunks.
  - Each node and edge gets a text profile stored as key-value pairs. Relation edges can get several index keys, including broader themes drawn from the entities they connect.
  - Duplicate entities and relations found in different chunks are merged.
  - New documents are indexed the same way, and their nodes and edges are merged into the existing graph instead of rebuilding the index.
  - This extraction and profiling is presumably where the named edges in his demo come from. That's an inference; the video doesn't explain it.
  - Source: https://arxiv.org/html/2410.05779
- **How retrieval works.** It retrieves at two levels: low-level (specific entities and their direct relationships) and high-level (broader themes spanning many entities). The README offers query modes `naive` (plain chunk retrieval), `local`, `global`, `hybrid` (merges local and global results) and `mix` (merges local, global and naive results; the default mode). Sources: https://arxiv.org/html/2410.05779 · https://github.com/HKUDS/LightRAG
- **Server and web UI.** Install with `pip install "lightrag-hku[api]"` (or `uv tool install "lightrag-hku[api]"`). The LightRAG Server's web UI at `/webui` provides document management, knowledge-graph exploration and query debugging. Source: https://github.com/HKUDS/LightRAG
- **Storage backends.** Supported backends include PostgreSQL (recommended for production), MongoDB, Neo4j, Milvus, OpenSearch and [[Qdrant]], with in-memory defaults meant only for testing. Source: https://github.com/HKUDS/LightRAG
- **Local models and privacy.** The README gives guidance for local deployment, naming Qwen3-30B-A3B-Instruct as a reasonable minimum model for the extraction step. So a graph can be built without sending your data to a hosted model, which addresses his privacy aside [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s). The server also exposes Ollama-compatible API routes for chat clients. Source: https://github.com/HKUDS/LightRAG

## Related

- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]
- **Concepts:** [[Knowledge Graphs]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[LLM Wiki]] · [[Second Brain Levels]] · [[Design for Retrieval]]
- **Techniques:** [[Build a Knowledge Graph Layer]] · [[Grill Me Interview Skill]] · [[Second Brain Pain-Point Audit]]
- **Tools:** [[Obsidian]] · [[Qdrant]] · [[Claude Code]]
- **People:** [[Nate Herk]]
- [[Home]]
