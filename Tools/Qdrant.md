---
type: tool
category: vector database
website: https://qdrant.tech/
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tags: [topic/retrieval, topic/rag, topic/second-brain]
---

# Qdrant

## What it is

In the video, Qdrant is a vector store that groups points into clusters [14:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=858s). [[Nate Herk]] uses it only as a **visual demo** of Level 3 semantic search: you watch images group by similarity [13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s), [14:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=862s). He doesn't present it as part of his own stack. The examples he gives for where you might get semantic search are Obsidian, Pinecone and Supabase [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s). Qdrant stands in for vector databases generally, so the guidance below applies to any vector store.

## How sources use it

- [[Nate Herk - Every Level of a Claude Second Brain]]:
  - **Level 3 demo:** a cluster of image vectors organised by similarity [13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s). The takeaway is that relationships form on *meaning*, not keywords [14:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=862s), [14:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=869s).
  - **Around the demo:** how vector databases work, where they fail, and how to scope one to a single folder [15:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=917s), [17:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1060s).

### The image-cluster demo

- **Setup.** Each vector point in the collection is one image [13:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=803s).
  - Each point's payload holds metadata such as the file name, URL, and the author or artist [13:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=806s).
  - Nothing in it describes what the image shows [13:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=814s). So the images can't be organised by text; they have to be grouped by meaning, i.e. by similarity [13:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=817s).
- **Walking the graph.**
  - He opens the graph visualisation [13:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=821s). A central image of owls in a trippy, psychedelic style [13:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=826s) sits next to neighbours with similar colours and paint [13:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=833s).
  - Those neighbours are similar but not the same; they only share traits [13:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=836s).
  - Expanding further drifts into other styles [14:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=842s): creepy eyes and mushrooms, then more fantasy-like images [14:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=846s), [14:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=847s).
  - The more relationships and meanings you build out, the further the graph moves from where it started [14:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=851s).
- **His framing.** Qdrant mainly supplies the visualisation here [14:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=855s), on top of its clusters and vector store [14:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=858s). He picked it because you can watch relationships form based on meaning [14:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=862s). That's the core of semantic search: searching by meaning instead of matching keywords [14:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=869s).

### What a vector database does (his explanation)

He has covered vector databases at length on his channel, so this is a quick version [15:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=917s):

1. Take a document, such as a YouTube transcript, and split it into chunks [15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s).
2. Run each chunk through an embeddings model [15:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=932s). The model places the chunk in a space where position encodes meaning. He calls it "three-dimensional", which is a simplification (see Beyond the source) [15:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=936s).
3. A chunk about a company lands in one region and a chunk about finances in another [15:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=941s). Similar vectors end up near each other [15:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=947s).

### When vector search fits and when it fails

He brings this back to designing for the questions you'll ask [15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s).

| Question | Vector search? | Why (per the video) |
|---|---|---|
| "What was rule 17?" out of 1,000 stored rules | **Good fit** | It pulls just the matching snippet [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s), [18:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1117s), instead of spending time and tokens reading all 1,000 rules [18:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1129s) |
| Searching with words you never wrote ("feedback") | **Good fit** | Matches on meaning, not the literal word [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s), [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) |
| "Summarise the March 5 meeting" (transcript stored as ~20 chunks) | **Poor fit** | It fetches chunks similar to "March 5th meeting summary" [16:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=980s). Even with the right chunks, it summarises only that handful (he says five) and never sees the whole transcript [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=991s) |
| "Which week had the highest sales?" | **Poor fit** | It grabs one chunk of the table and answers week 6 [17:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1024s). Weeks 14 and 19 were actually higher [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s) |

- **Rule of thumb.** If the answer needs full context, chunking won't do [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s). Keep a plain markdown file, such as the March 5 meeting, and have the agent read all of it; that's more accurate [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s).
- **Where vectors shine:** large amounts of text where you need one specific answer that closely matches the query [18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s).
- **Metadata helps, but vectors aren't magic.** Metadata and similar tweaks can improve results [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s). Still, the belief that a vector database always returns what you need is false [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s).

### How to scope a vector store in a second brain

- **Vectorise one folder, not the whole brain.** For example, only YouTube transcripts go into a vector database, while context, projects and decisions stay as markdown files [17:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1060s). Not every part of the brain needs the same style [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s). Decide per folder, based on the data and how you use it [18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s). See [[Add Semantic Search to One Folder]].
- **Document the search pipeline inside the folder.** His example Level 3 project has a vector index folder with a "how search works" note [18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s). It covers chunking, embedding, search, hybrid search and re-ranking; he adds that semantic search has plenty of detail you can go very deep on [18:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1095s).
- **Ask your agent first.** Describe the data and how you'll use it to your Claude Code agent. Ask whether plain markdown or semantic search fits better; it will walk you through the setup [19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s), [19:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1144s).
- **When to add one.** Consider semantic search when the brain keeps missing notes you know exist and routing isn't fixing it [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s), [29:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1755s). If nothing hurts, don't add architecture [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s).

## Notes

- **No Qdrant build in the video.** There's no setup walkthrough, no named embedding model and no ingestion pipeline. The demo is only there to build intuition. For a build, pair the scoping rules above with the verified setup details below.
- **His own brain doesn't use a vector store day to day.** His main project sits at Level 2 [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s).
- **Similarity isn't a typed relationship.** Semantic search says X is similar to Y and Z [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s), while knowledge-graph edges name the relation, such as a person who works at a company [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s) ([[Knowledge Graphs]], [[LightRAG]]). See [[Keyword vs Semantic vs Graph Retrieval]].

## Beyond the source

*Not said in the video; verified at the links given.*

- **What Qdrant is.** An open-source (Apache License 2.0) vector similarity search engine and vector database, written in Rust. It's aimed at neural-network or semantic matching and has extended filtering (keyword, full-text, numeric-range and geo filters, combinable with logical operators). Source: https://github.com/qdrant/qdrant
- **Run it locally.** After `docker pull qdrant/qdrant`, start it with `docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant`. The REST API is at `localhost:6333`, the Web UI at `localhost:6333/dashboard`, and gRPC at `localhost:6334`; data is stored in `./qdrant_storage`. The README warns that a plain Docker run is an insecure deployment with no authentication, open on all network interfaces, so read the security docs before exposing it. Sources: https://qdrant.tech/documentation/quickstart/ · https://github.com/qdrant/qdrant
- **The tools his demo appears to use.** Qdrant's Web UI has visualisation and graph exploration tools; it reduces n-dimensional vectors to 2D points shown with their payloads. Qdrant's article on distance-based exploration projects vectors to 2D with UMAP and clusters them with KMeans, noting an interactive version of the plot is available in the Web UI. It also describes its Graph Exploration Tool, which can start from one point and keep adding the most similar neighbours. The article's demos use the Midjourney Styles dataset, one of Qdrant's default datasets for experimenting. His demo (art-style images, a similarity graph expanding outward from one image) looks similar, but the video doesn't name the dataset and the article doesn't list its payload fields, so the match is unconfirmed. Sources: https://qdrant.tech/articles/distance-based-exploration/ · https://qdrant.tech/articles/web-ui-gsoc/
- **Payloads.** A payload is any JSON stored alongside a vector, and it can be used to filter searches. Creating indexes on the payload fields you filter on makes filtered search more efficient. This is one concrete way to act on his point that metadata can improve results [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s); for example, you could filter chunks by date or source file before ranking by similarity. Source: https://qdrant.tech/documentation/manage-data/payload/
- **Hybrid search.** Qdrant supports hybrid queries that combine dense and sparse vectors through prefetch and a fusion method such as Reciprocal Rank Fusion (RRF). This covers the "hybrid" item in his example folder's how-search-works note [18:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1095s). Source: https://qdrant.tech/documentation/search/hybrid-queries/
- **Embeddings aren't 3D.** They're high-dimensional; Qdrant's docs cite a standard OpenAI embedding of 1,536 dimensions and OpenAI's text-embedding-3-large at up to 3,072. High-dimensional data can't be plotted directly, so 2D or 3D pictures, including Qdrant's Web UI visualisation, rely on dimensionality reduction. Sources: https://qdrant.tech/documentation/manage-data/vectors/ · https://qdrant.tech/articles/distance-based-exploration/
- **Works with [[LightRAG]].** Qdrant is one of LightRAG's supported vector storage backends, so the two can be combined. Source: https://github.com/HKUDS/LightRAG
- **Privacy implication** (reasoning from the facts above, not a claim from the video). Because Qdrant is open source and runs locally in Docker, the vector index can stay on your own infrastructure. Whether your text leaves your machine still depends on which embedding model you call. That's relevant to his aside about data sent to Anthropic [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s). Source for self-hosting: https://qdrant.tech/documentation/quickstart/

## Related

- **Source:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **Concepts:** [[Semantic Search]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Design for Retrieval]] · [[Second Brain Levels]] · [[Knowledge Graphs]]
- **Techniques:** [[Add Semantic Search to One Folder]] · [[Second Brain Pain-Point Audit]]
- **Tools:** [[LightRAG]] · [[Obsidian]] · [[Claude Code]]
- **People:** [[Nate Herk]]
- [[Home]]
