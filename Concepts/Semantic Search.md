---
type: concept
aliases: ["Vector Search", "Embeddings Search"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tags: [topic/retrieval, topic/rag, topic/second-brain]
---

# Semantic Search

## In one sentence

Semantic search finds things by meaning, not by exact words. Text is cut into chunks, each chunk becomes an embedding vector, and a query brings back the chunks whose vectors sit closest to it. It is Level 3 of [[Second Brain Levels]]: useful for one big folder of text, but a poor fit for anything that needs the whole document.

## How it works

### Matching by meaning instead of by the word

- The Level 3 question is: can I find a note when I search with different words than the ones I wrote? [03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)
- Nate's short version: keyword search asks whether "X equals X", while semantic search asks whether X is *similar to* X, Y and Z. [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s)
- **The "feedback" demo.** In his YouTube-transcript second brain he searches for "feedback" twice ([14:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=873s)). It looks like the vault he showed in Obsidian earlier, but he doesn't name the app or the search tool on screen:
  - The regular search only lists places where the literal word "feedback" appears. [14:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=885s)
  - A panel called "smart lookup" returns notes whose *meaning* is about feedback even without the word: live test results, and a note on Claude Code skills that covered evaluations. [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s)
- Between his two demos (the Qdrant one below, then this "feedback" one) he gives the core idea: semantic search stops matching keywords and searches by meaning. [14:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=868s)

### The pipeline (as Nate describes it)

1. Take a document, for example a YouTube transcript, and split it into chunks. [15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s)
2. Run each chunk through an embeddings model. [15:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=932s)
3. The model places each chunk in a space where position stands for meaning. He calls it a "three-dimensional space", which is a simplification (see *Beyond the source*). [15:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=933s)
4. A chunk about a company lands in one region and a chunk about finances in another, so similar chunks end up as neighbouring vectors. [15:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=941s)
5. At question time the agent searches with a phrase and pulls back the chunks most similar to it (see his March 5 meeting example below). [16:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=980s)

He frames all of this as the vector-database idea, which he says he has covered at length on his channel. [15:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=917s)

In his Level 3 example project, a vector-index folder holds a doc on how search works (captioned "house search works"; the exact filename is unclear). It lists the stages as **chunking, embedding, search, hybrid, re-ranking**. He adds that semantic search has plenty of fine detail to dig into, but he doesn't explain the stages in this video. [18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s)

### Seeing it: the Qdrant image-cluster demo

- He opens a Qdrant collection where every vector point is an image. [13:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=797s)
- Each point's payload holds only metadata: file name, URL, the author or artist. Nothing describes what the image shows. [13:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=806s)
- So the only way to organise the images is by meaning, or similarity, in the vectors themselves. [13:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=817s)
- In the graph view he starts from a psychedelic-style owl painting. Its neighbours share its colours and painterly look but are different images. [13:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=824s)
- Expanding outward drifts into related but different styles: one with eerie eyes and mushrooms, another more fantasy-like. [14:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=841s)
- He says Qdrant is a vector store with clustering. He picked the demo because it makes the meaning-based relationships visible. [14:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=856s)

### Where you can run it

He names doing semantic search inside Obsidian, or with Pinecone or Supabase. However you get it working, that capability is what defines Level 3. [13:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=784s) Qdrant appears as the visual demo above. [13:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=797s)

## When to use it — and when not to

### What it is good at

- **Lots of text plus a narrow, specific answer.** Vector retrieval shines when there is a large volume of text and you want one very specific, closely matching piece. [18:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1101s)
- **Worked example: 1,000 stored rules.** Asking "what was rule 17?" suits vector search. It pulls the matching chunks and returns a short snippet. [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s) Having the agent read a markdown file of all 1,000 rules to find one would waste time and tokens. [18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)
- **The pain that points here.** Your project keeps missing notes you *know* exist, and fixing the routing hasn't helped. Semantic search doesn't depend on matching the exact word. [29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)

### Failure mode 1: summarising something from a few fragments

This is why he says to think first about how the data will be used and what you'll ask of it ([15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s); see [[Design for Retrieval]]).

- Say a March 5 meeting transcript is stored as vectorised chunks, around 20 of them. [15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s)
- You ask the agent to summarise that meeting. It searches for something like "March 5 meeting summary" and pulls the chunks most similar to that phrase. [16:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=980s)
- Even when it pulls the right chunks, it summarises only that handful (he says five). It never sees the full transcript, so the summary may miss key information. [16:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=986s)
- Metadata and similar tweaks can improve results. [16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s) Still, he calls the belief that a vector database always returns what you need a false assumption. [16:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1007s)
- **Better fit:** keep the meeting as a markdown file and let the agent read the whole thing before summarising. That will be more accurate. [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)

### Failure mode 2: questions that add up across a table

- Take a sales table and ask which week had the highest sales. [16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s)
- The agent searches for "highest sales", grabs one chunk of rows, sees that week 6 is highest *within that chunk*, and answers week 6. [16:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1018s)
- The full table shows weeks 14 and 19 were both higher. [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)
- **Rule:** when the answer needs the full context, chunked vector retrieval is the wrong tool. [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)

### Use it per folder, not for the whole brain

- His Level 3 example project still has the same context and decision files as the lower levels. [17:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1049s)
- You might turn just one unit of the business into a vector database, for example the YouTube transcripts. [17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s) Context, projects and decisions stay as markdown files. [17:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1066s)
- A large second brain doesn't need a single retrieval style. [17:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1071s) Not everything needs GraphRAG, and not everything has to be an [[LLM Wiki]]. [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s) Choose how to structure each folder based on its data and how you use it. [18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)
- The same point comes back in "Finding your level": one project can have folders at different levels. [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)

### Let Claude Code make the call

- Tell your Claude Code agent what the data is and how you plan to use it. Then ask whether it's better kept as markdown files for now or put behind semantic search. [18:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1139s) He says it will walk you through how to set it up. [19:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1148s)
- The same prompt as a fill-in template (his suggestion paraphrased, with placeholders added): *"I have this data: [describe it]. Here's how I want to use it: [describe]. For now, is it better kept as markdown files, or should it go behind semantic search? What makes more sense?"* Build steps: [[Add Semantic Search to One Folder]].
- Moving up a level is not automatically better. Find the actual pain point first, and change levels only if that fixes it. [19:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1158s) See [[Second Brain Pain-Point Audit]].

### Quick decision table (from the video's examples)

| Question type | Semantic search? | Why | Timestamp |
|---|---|---|---|
| "Remind me what rule 17 was" (1 of 1,000) | Yes | A small, specific snippet from a big pile of text | [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s) |
| "Find notes about feedback" without knowing the wording | Yes | Matches meaning, not the literal word | [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s) |
| "Summarise the March 5 meeting" | No: read the markdown | Only a few chunks come back, not the whole meeting | [16:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=986s) |
| "Which week had the highest sales?" | No | Needs every row; one chunk gives a wrong maximum | [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s) |
| Your own context, decisions, projects | No: keep as markdown | He keeps these as plain markdown even when one folder moves to vectors | [17:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1066s) |

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] ([[Nate Herk]]): semantic search is a per-folder upgrade, not a default.
  - He says his own main second brain, Herk2, sits almost entirely at Level 2. [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)
  - He hasn't felt enough pain to move up. The captions say "level two" there, but from context he means Level 3. [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s)
  - He separates wiki links, which give only a loose sense of relationship, from semantic or knowledge-graph relationships, which carry more meaning. [12:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=734s)
  - His warning: vector databases are not magic [16:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1007s), and chunked retrieval is the wrong tool when the answer needs full context, like a summary or a table-wide maximum. [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)
- *Caption fixes used in this note:* "Quadrant" → Qdrant; "Pine Cone" → Pinecone; "graph rack" → GraphRAG; "PERC 2" → Herk2; "cloud code skills" → Claude Code skills. The "house search works" doc name is *(unclear in captions)*, probably "how search works".

## Beyond the source

*Not from the video. Each item was checked against the linked page.*

- **Embeddings are high-dimensional, not 3-D.**
  - OpenAI's embeddings guide gives vector lengths of 1,536 for `text-embedding-3-small` and 3,072 for `text-embedding-3-large`. The distance between two vectors measures how related they are. — <https://developers.openai.com/api/docs/guides/embeddings>
  - Any picture of vectors on a screen is a stand-in for that space. Qdrant describes two options. One projects the vectors to 2-D with UMAP, which keeps relative distances. The other is a graph where points are nodes and similarities are edges, which is the kind of view Nate opens. — <https://qdrant.tech/articles/distance-based-exploration/>
- **Hybrid search.** Hybrid search combines dense vectors (semantic meaning) with sparse vectors (keyword-style matching) and merges the two ranked lists. Qdrant calls Reciprocal Rank Fusion (RRF) the safe default when you have neither an evaluation set nor strong score priors. — <https://qdrant.tech/documentation/concepts/hybrid-queries/>
  - Anthropic pairs embeddings with BM25 keyword matching because exact matching catches identifiers and technical terms that semantic models can miss. That covers lookups like "rule 17". — <https://www.anthropic.com/news/contextual-retrieval>
- **Re-ranking.** Retrieval runs in stages. A smaller, cheaper representation gathers a long list of candidates, then a larger, more accurate one re-scores them and keeps the best. Qdrant's examples include full-precision vectors and ColBERT-style multi-vectors. — <https://qdrant.tech/documentation/concepts/hybrid-queries/>
  - In Anthropic's contextual-retrieval write-up, the top 150 chunks were re-ranked down to 20 before being sent to the model. — <https://www.anthropic.com/news/contextual-retrieval>
- **Chunks losing their context (related to failure mode 1 and the metadata tip).**
  - Anthropic's "contextual retrieval" adds a short, chunk-specific context to each chunk before embedding it and indexing it for BM25.
  - Reported cuts in retrieval failures: 35% with contextual embeddings, 49% when contextual BM25 is added, 67% when re-ranking is added on top.
  - This improves *which* chunks come back. It does not show the model the whole meeting, so Nate's advice to read the full markdown for summaries still holds. — <https://www.anthropic.com/news/contextual-retrieval>
- **When to skip vectors entirely.** The same Anthropic article suggests that a knowledge base under roughly 200,000 tokens can go straight into the prompt (with prompt caching) instead of using RAG. This matches Nate's "just read the markdown file" instinct for smaller data. — <https://www.anthropic.com/news/contextual-retrieval>
- **Aggregate questions are a known weakness.** Microsoft Research reports that baseline vector RAG does poorly on questions that need information pulled together across a dataset (e.g. "top 5 themes"). GraphRAG tackles these with pre-summarised graph clusters. Nate's example is a numeric table; Microsoft's is about themes. The underlying limitation is the same. — <https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/>
- **What Obsidian's "smart lookup" probably is.** Obsidian's core Search plugin matches words, exact phrases and regex patterns, with no meaning-based mode. — <https://obsidian.md/help/plugins/search>
  - The Smart Plugins family, whose flagship is Smart Connections, includes **Smart Lookup**. You type an idea, topic or question, and it returns a ranked list of notes or note sections by meaning. A local embedding model builds the index, and no API key is needed. — <https://smartconnections.app/smart-lookup/search/>, <https://github.com/brianpetro/obsidian-smart-connections>
  - If that screen is Obsidian, the panel in Nate's demo is probably Smart Lookup. The video names neither the app nor the plugin.
- **Supabase option.** Semantic search on Supabase runs on the `pgvector` Postgres extension, which stores embeddings and runs similarity search. — <https://supabase.com/docs/guides/database/extensions/pgvector>
- **Qdrant's graph view.** Qdrant's Web UI graph-exploration tool shows points as nodes linked by similarity edges, and you can expand outward from one point. That matches what Nate does in his image demo, though he doesn't name the feature. — <https://qdrant.tech/articles/distance-based-exploration/>

## Related

- [[Second Brain Levels]]: semantic search is Level 3
- [[Keyword vs Semantic vs Graph Retrieval]]: side-by-side comparison with keyword, wiki and graph retrieval
- [[Design for Retrieval]]: decide storage from the questions you'll ask
- [[Add Semantic Search to One Folder]]: build playbook
- [[LLM Wiki]] · [[Knowledge Graphs]] · [[Tiered Lookup Routing]]
- [[Second Brain Pain-Point Audit]]
- Tools: [[Qdrant]] · [[Obsidian]] · [[Claude Code]] · [[LightRAG]]
- Source: [[Nate Herk - Every Level of a Claude Second Brain]]
- [[Home]]
