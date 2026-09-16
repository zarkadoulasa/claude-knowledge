---
type: technique
goal: Give one text-heavy folder of a second brain meaning-based (vector) retrieval while context, decisions and projects stay plain markdown
difficulty: intermediate
time_to_build: Half a day for a first folder (estimate, not stated in the source)
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tools: ["[[Claude Code]]", "[[Qdrant]]", "[[Obsidian]]"]
tags: [topic/second-brain, topic/retrieval, topic/rag, topic/claude-code]
---

# Add Semantic Search to One Folder

> Level 3 of [[Second Brain Levels]], applied to one part of the brain only. One folder gets a vector index. Everything else stays as plain markdown that the agent reads in full.

## Goal

Make one large, text-heavy part of the brain searchable by meaning instead of exact words, without converting the whole brain. [[Nate Herk]]'s example is his YouTube transcripts. His context, projects and decisions stay as markdown files ([17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s)). CLAUDE.md then sends each kind of question to the retrieval method that suits it:

- **Summaries:** read the full markdown file.
- **Pinpoint lookups:** use vector search.
- **Aggregates:** use structured data.

In his framework, Level 3 answers one question: can you find something when you search with different words than you wrote? ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)). What makes a brain Level 3 is having semantic search at all. The tool doesn't matter: Obsidian, Pinecone and Supabase are all options ([13:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=786s)).

### Keyword vs semantic: what changes

| | Keyword search (Levels 1–2) | Semantic search (Level 3) |
|---|---|---|
| How it matches | Exact word: "X equals X" ([15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s)) | Meaning: "X is similar to X, Y and Z" ([15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s)) |
| His live demo | Searching "feedback" only returns places where that word appears ([14:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=885s)) | The same query in his "smart lookup" also finds related material, such as live test results and a note on Claude Code skill evaluations ([14:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=898s)) |
| Strong at | Finding a known file, name or phrase | Pulling one specific answer out of a lot of text ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s)), even when your wording differs from what you wrote ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)) |
| Weak at | Synonyms and rephrasings | Summarising a whole document, and aggregates across a table ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s)) |

See [[Keyword vs Semantic vs Graph Retrieval]] and [[Semantic Search]] for the concept.

## Use when

- **The agent keeps missing notes you know exist,** and your routing isn't solving it. That is his signal to look at semantic search ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)).
- **You remember ideas in different words** from the ones you wrote down ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)).
- **The folder is a big pile of text and most questions need one small piece of it.** His example is a thousand stored rules when you only need rule 17. Vector search returns just that snippet. Reading the whole file would waste time and tokens ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s), [18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)).

### Don't use when

- **Nothing hurts yet.** Pick the lowest level that meets your needs. Without a pain point there's no reason to build new architecture ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)). A higher level isn't automatically better ([19:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1156s)).
- **The questions need the whole document.** Examples: summarising one meeting, or finding the highest-sales week in a table. Reading the full markdown file is more accurate for these ([17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)).
- **Wikis and routing already work.** Nate says his main Herk2 project sits pretty much entirely at Level 2, because that works well for him. He hasn't felt enough pain to move up ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)). The captions say "switch over to level two" at [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s), but from context he means Level 3. He does demo a semantic "smart lookup" on his YouTube-transcript brain ([14:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=873s)), though the video doesn't say how that lookup fits inside Herk2. Either way, his broader point stands: different folders of one project can sit at different levels ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).

## Prerequisites

- **A working Level 1–2 brain with CLAUDE.md acting as a router** ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)). See [[Build a Level 1 Second Brain]] and [[CLAUDE.md as a Router]]. His Level 3 example project still has its context and decision files ([17:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1049s)).
- **A clear list of the questions you'll ask this folder.** How data will be recalled should decide how you store it ([02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)). He uses vector chunking as a prime example of why that matters ([15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s)). See [[Design for Retrieval]].
- **Complete source files.** He notes that sometimes the bigger problem isn't retrieval but getting what's in your head into the system ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).
- **A privacy decision.** Anything you process through Claude goes to Anthropic ([21:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1290s)). He raises this in the Level 4 chapter, but it applies to any folder you index and query with a cloud model.
- **A chosen vector store,** plus accounts or API keys if it's hosted (see step 5).

## Steps

1. **Confirm the pain.** Write down 3–5 real lookups that failed, such as a note you know exists or a synonym search that came back empty. These are your baseline and your acceptance tests. His trigger for Level 3 is the agent whiffing on notes you know are there ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)). See [[Second Brain Pain-Point Audit]].

2. **Pick one unit, not the whole brain.** Having a large brain doesn't mean every folder needs the same style. Not everything needs GraphRAG, and not everything has to be an LLM Wiki ([18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s)). Decide per folder, based on the type of data and how you use it ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)). One project can mix Levels 2, 3 and 4 ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)). Good candidates are big text collections such as transcripts, where questions are pinpoint or fuzzy.

3. **Sort the questions you'll ask of that unit into three types.** This decides the routing in step 8.

   | Question type | Example | Best method | Why (from the video) |
   |---|---|---|---|
   | Whole-document or summary | "Summarise the March 5th meeting" | Read the full markdown file | Vector search only sees the chunks it retrieved, so it can miss key parts of the meeting ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)) |
   | Pinpoint or fuzzy wording | "What was rule 17?" / "Where did I talk about feedback?" | Vector (semantic) search | Returns only the relevant snippet from a lot of text ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)) |
   | Aggregate across rows | "Which week had the highest sales?" | Structured data, read or computed in full | A single chunk can show a local maximum (week 6) while weeks 14 and 19 were actually higher ([16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)) |

4. **Ask Claude Code for a fit check before building.** Describe the data and how you'll use it. Ask whether it should stay markdown or get semantic search, and it will walk you through the setup ([18:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1139s), [19:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1149s)). The prompt is below.

5. **Choose a store.** The video names these options. Verified setup details are under *Beyond the source*.

   | Option | What the video says |
   |---|---|
   | [[Obsidian]] | You can add semantic search inside Obsidian ([13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s)). Obsidian itself only visualises your markdown files ([09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)) |
   | Pinecone | Named as a way to get semantic search ([13:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=790s)) |
   | Supabase | Named alongside Pinecone ([13:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=790s)) |
   | [[Qdrant]] | Used for his demo: a collection of images grouped by similarity. Each point's payload holds only metadata such as file name, URL and artist, not a description of the image ([13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s), [13:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=806s)). He describes it as a vector store with cluster visualisation ([14:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=856s)) |

6. **Build the pipeline in a `vector-index/` folder, with a "how search works" doc.** His example project has a vector-index folder whose explainer lists five stages: chunking, embedding, search, hybrid and re-ranking ([18:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1094s)). He adds that semantic search has a lot of nitty-gritty details you can tune.
   - A document such as a transcript is split into chunks.
   - Each chunk goes through an embeddings model, which places it in a space where position reflects meaning ([15:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=928s)).
   - Chunks about similar things end up near each other ([15:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=947s)).
   - Keep the original markdown files in place. Summaries need to read them whole ([17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)).

7. **Add metadata to every chunk.** He names metadata as one lever for improving chunk-based results like the March 5th meeting lookup, without saying which fields to use ([16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s)). This note suggests at least date, source file, title and type. With a date field, the agent can filter a search to that one meeting instead of pulling look-alike chunks from other meetings.

8. **Add routing to CLAUDE.md.** Claude won't search your whole project on its own. You wouldn't want it to, because of the time and token cost ([05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)). If it doesn't know where something lives, it probably won't find it ([05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)). Add the routing block below: summaries read the full file, pinpoint lookups use vector search, aggregates use structured data, and unindexed folders are read directly.

9. **Run the test prompts, including a keyword comparison.** Recreate his demo: run the same query through plain keyword search and through the semantic lookup, and compare the results ([14:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=878s)). Then re-run your failed lookups from step 1.

10. **Keep ingestion deliberate.** Nate stays in full control of what his brain ingests ([26:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1585s)). Some data changes often: Slack threads, emails, customer data. Don't ingest it into the brain, where it becomes noise you have to clean out ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)). Instead, make sure the brain knows where to fetch it ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)). See [[Context vs Connections]] and [[Tiered Lookup Routing]].

## Starter files & prompts

### Folder layout (example)

Adapted from his Level 3 example project ([17:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1049s), [18:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1094s)). The file names are illustrative. The other paths follow the vault's shared starter layout: the base tree in [[Build a Level 1 Second Brain]] plus the `wikis/` folders from [[Ingest Sources into an LLM Wiki]]. If you already keep original transcripts in a wiki's `raw/` folder, index that folder instead of `transcripts/`.

```text
my-brain/
├── CLAUDE.md                     ← router; gains the retrieval-routing block below
├── context/                      ← markdown, NOT indexed (always-true background)
├── decisions.md                  ← markdown, NOT indexed (decision log)
├── projects/                     ← markdown, NOT indexed
├── wikis/                        ← Level 2 wikis if you have them, NOT indexed
├── transcripts/                  ← the ONE unit being upgraded (YouTube + meeting transcripts)
│   ├── 2026-03-05-weekly-meeting.md      (originals stay: source of truth)
│   └── 2026-05-30-top-50-features.md
├── vector-index/
│   ├── how-search-works.md       ← chunking, embedding, search, hybrid, re-ranking
│   ├── index-log.md              ← what was indexed when, embedding model used
│   └── scripts/
│       ├── index.py              ← (re)builds the index from transcripts/
│       └── search.py             ← query + optional date/type filters
└── data/
    └── weekly-sales.csv          ← aggregates live as structured data, not chunks
```

### Fit-check prompt (step 4)

```text
I have a folder `transcripts/` with about <N> markdown transcripts
(one per video/meeting, each several thousand words, each with a date in the filename).

How I will use it:
1. Summaries of one video or meeting ("summarise the March 5th meeting")
2. Pinpoint lookups where my wording won't match the text
   ("where did I talk about getting feedback on skills?")
3. Occasional aggregates ("which month had the most videos about agents?")

These lookups currently fail: <paste 3–5 real failures>.

Should this folder stay plain markdown, get semantic search, or both?
For each of the three question types, tell me which retrieval method gives the most
accurate answer and why. Then propose the smallest setup that fixes the failures.
Do not build anything yet.
```

### Build prompt (steps 5–8)

```text
Build semantic search for `transcripts/` ONLY. Do not index context/, decisions.md,
projects/ or wikis/.

- Store: <Qdrant (local) | Pinecone | Supabase pgvector | Obsidian plugin>.
- The markdown files stay the source of truth; the index is derived and must be rebuildable
  with one documented command.
- Chunk each file and embed each chunk. Store metadata on every chunk:
  source_path, title, date (ISO 8601), type (video|meeting), chunk_index.
- Search: hybrid (semantic + keyword) with a re-ranking step; support filtering by date and type.
- Scripts go in vector-index/scripts/. Write vector-index/how-search-works.md explaining the
  chunking settings, embedding model, hybrid method, re-ranker, metadata fields and how to re-index.
- Append the routing block I paste below to CLAUDE.md.
- Then run the five test prompts from my note and report pass/fail for each.
```

### CLAUDE.md routing block (step 8)

```markdown
## Retrieval routing: transcripts/

This folder has two access paths. Choose by question type:

| If the question is… | Do this |
|---|---|
| A summary / walkthrough of ONE video or meeting | Find the file by date or title and read the WHOLE markdown file. Never summarise from search chunks. |
| A pinpoint lookup, or my wording may not match the text ("where did I…", "what did I say about…") | Run semantic search (`python vector-index/scripts/search.py "<query>"`, add `--after/--before` when a date is known). Open the source file if a snippet is ambiguous and cite source_path. |
| An aggregate ("which / how many / highest / trend across all…") | Do NOT use vector search. Use the structured data in data/ and compute over all rows. |
| Anything about context/, decisions.md, projects/ | Read the markdown directly. These are not indexed. |

If semantic search returns nothing relevant, try an exact keyword search of the folder
before concluding the information doesn't exist.
```

### `vector-index/how-search-works.md` skeleton

```markdown
# How search works (transcripts/)

- Scope: transcripts/ only. Rebuild: `python vector-index/scripts/index.py --rebuild`
- Chunking: <size, overlap, split on headings/speaker turns?>
- Embedding model: <name, dimensions>. Changing it = full re-index.
- Metadata per chunk: source_path, title, date, type, chunk_index
- Search: <dense + keyword hybrid, fusion method>
- Re-ranking: <model / none>, top-k before and after
- Known limits: chunk-based. Don't use for whole-document summaries or aggregates (see CLAUDE.md routing).
```

### Test prompts (step 9)

| # | Prompt | Tests | Pass if |
|---|---|---|---|
| 1 | "Find where I talked about getting input from viewers on my videos." (Notes use words like "feedback" or "comments.") | Synonym / meaning match ([14:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=898s)) | Returns the right transcripts even though your words aren't in them. A plain keyword search for your words misses them. |
| 2 | "Summarise the March 5th meeting." | Whole-document summary ([16:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=975s)) | The agent opens the full file, not chunks. The summary covers the beginning, middle and end of the meeting. |
| 3 | "Which week had the highest sales?" | Aggregate ([16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s)) | The agent uses `data/`, checks every row and returns the true maximum. |
| 4 | "What did we decide about pricing in the March 5th meeting?" | Metadata filter ([16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s)) | Results come only from that date's file, and the answer cites it. |
| 5 | "What are my current project priorities?" | Routing control | The agent reads `projects/` directly and doesn't call vector search. |

## Done when

- [ ] 3–5 documented failed lookups now succeed
- [ ] Only the chosen folder is indexed. `context/`, `decisions.md` and `projects/` are still plain, unindexed markdown
- [ ] Original markdown files are intact, and one documented command rebuilds the index from them
- [ ] Every chunk carries at least `source_path` and `date` metadata
- [ ] `vector-index/how-search-works.md` explains the chunking, embedding, hybrid and re-ranking choices
- [ ] CLAUDE.md routes the three question types (summary, pinpoint, aggregate) plus the unindexed folders
- [ ] All five test prompts pass
- [ ] Your ingest routine indexes new files added to the folder

## Pitfalls

- **Summarising from chunks.** Say a meeting is split into about 20 chunks and you ask for a summary. The agent pulls the few chunks that resemble "March 5th meeting summary" and summarises only those. It never sees the whole transcript and can miss key information ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s), [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=997s)). Route summaries to the full file.
- **Aggregates over chunks.** Asked for the best sales week, the agent grabs one chunk of the table and reports week 6, while weeks 14 and 19 were higher ([16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)). Anything that needs full context shouldn't go through vector chunking ([17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)).
- **Treating a vector database as magic.** People assumed vector stores would always return what you need. He says that's very false ([16:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1007s)).
- **Converting the whole brain.** Level 3 is a per-folder decision. In his example, context, projects and decisions stay as markdown files ([17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s), [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s)).
- **Building without pain.** If no lookups are failing, the extra architecture is cost without benefit ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).
- **No metadata.** He lists metadata among the ways to improve weak chunk results ([16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s)). Without date and source fields (this note's inference), look-alike chunks from other meetings can outrank the one you meant.
- **Mistaking wiki links for semantic relationships.** Following wiki links means walking a trail and reading whole pages. That is not the same as similarity search ([12:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=736s), [12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)).
- **Choosing a tool for its visuals.** The Qdrant cluster view is useful for seeing meaning-based grouping ([14:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=861s)). What matters is whether the system can find the data and hand it back to you ([10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)).
- **Blaming retrieval when the data is thin.** Before blaming the AI, check whether your files actually capture the nuance you have in your head ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)).
- **Indexing data that changes often.** Slack, email and customer data go stale and turn into noise ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)). Route to the live source instead ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)).

## Variations

- **Inside Obsidian, no separate database:** add semantic search through Obsidian ([13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s)). One plugin option is listed under *Beyond the source*.
- **Hosted store:** Pinecone or Supabase ([13:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=790s)).
- **Qdrant:** the vector store behind his cluster demo ([13:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=799s)). It can run locally in Docker and be exposed to Claude Code through an MCP server (both under *Beyond the source*).
- **Rules or policy library:** a large set of numbered rules where questions target single items ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)).
- **Meeting transcripts:** his March 5th example ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s)) points to the same split. Read whole files for summaries and use vector search for pinpoint mentions. Metadata can help tell meetings apart ([16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s)). The split itself is this note's suggestion.

## Beyond the source

*Not from the video. Each item was checked against the linked page on 2026-09-15.*

- **Embeddings aren't three-dimensional.** At [15:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=936s) the video describes the embedding space as three-dimensional, which is a simplification. Real embedding vectors have hundreds to thousands of dimensions. OpenAI's `text-embedding-3-small` defaults to 1536 and `text-embedding-3-large` to 3072. [OpenAI embeddings guide](https://developers.openai.com/api/docs/guides/embeddings)
- **What "hybrid" and "re-ranking" mean in practice.** Qdrant's hybrid queries combine dense vectors (semantic meaning) with sparse vectors (exact word matching). They run sub-queries via `prefetch` and merge the results with Reciprocal Rank Fusion (RRF) or Distribution-Based Score Fusion (DBSF). Multi-stage queries can re-score candidates with a more accurate representation, such as ColBERT-style multi-vectors. [Qdrant: hybrid and multi-stage queries](https://qdrant.tech/documentation/concepts/hybrid-queries/)
- **Pinecone hybrid search.** Pinecone supports hybrid (semantic plus keyword) search using sparse and dense vectors. [Pinecone: hybrid search overview](https://docs.pinecone.io/guides/search/hybrid-search)
- **Evidence that hybrid plus re-ranking helps.** Anthropic's Contextual Retrieval write-up prepends chunk-specific context before embedding and before BM25 indexing. Contextual embeddings cut top-20 retrieval failures by 35%. Adding contextual BM25 made it 49%, and adding re-ranking made it 67%. The write-up also found retrieving the top 20 chunks beat 5 or 10. For knowledge bases under about 200,000 tokens, it suggests skipping retrieval and putting the whole knowledge base in the prompt, using prompt caching. That's another reason to confirm pain before building. [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- **Metadata filters, Qdrant.** Payload filters use `must` / `should` / `must_not` with match and range conditions, including a datetime range on RFC 3339 values. Qdrant recommends creating payload indexes on fields you filter by, ideally before ingesting data. [Qdrant: filtering](https://qdrant.tech/documentation/concepts/filtering/)
- **Metadata filters, Pinecone.** Filters use `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin` and `$exists`, plus `$and`, `$or` and `$not`. The range operators (`$gt`, `$gte`, `$lt`, `$lte`) work on numbers only. Inference, not stated on the page: store dates as numbers (for example Unix timestamps) if you want date-range filters. [Pinecone: filter by metadata](https://docs.pinecone.io/guides/search/filter-by-metadata)
- **Supabase.** Vectors live in Postgres via the pgvector extension: `create extension vector with schema extensions;`, a column type such as `extensions.vector(384)`, and nearest-neighbour ordering with the `<->` operator. [Supabase: pgvector](https://supabase.com/docs/guides/database/extensions/pgvector)
- **Obsidian option.** The Smart Connections community plugin uses a local embedding model for semantic search. It needs no API key and shows related notes while you write. [Smart Connections on GitHub](https://github.com/brianpetro/obsidian-smart-connections)
- **Running Qdrant locally.** Qdrant's quickstart runs it in Docker with `docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant`. The REST API is on port 6333 and gRPC on 6334. [Qdrant quickstart](https://qdrant.tech/documentation/quickstart/)
- **Wiring Qdrant into Claude Code.** The official `mcp-server-qdrant` provides two tools, `qdrant-store` and `qdrant-find` (semantic search). It's configured with `QDRANT_URL` or `QDRANT_LOCAL_PATH`, `COLLECTION_NAME` and `EMBEDDING_MODEL`. The default embedding model is `sentence-transformers/all-MiniLM-L6-v2` via FastEmbed, which runs locally. The README's Claude Code example is `claude mcp add <name> -e QDRANT_URL=... -e COLLECTION_NAME=... -- uvx mcp-server-qdrant`. [mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)
- **`claude mcp add` scopes.** `--scope local` (the default) is only you, in this project. `project` is shared through a `.mcp.json` file at the project root. `user` applies to you across all projects. Everything after `--` is passed to the server command untouched. [Claude Code docs: MCP](https://code.claude.com/docs/en/mcp)
- **Privacy details.** On consumer plans (Free, Pro, Max), Anthropic trains on your data, including Claude Code sessions, only when the model-improvement setting is on. Under commercial terms (Team, Enterprise, API) it doesn't train on your data unless you opt in, for example through the Development Partner Program. Either way, prompts and outputs still leave your machine to be processed. A local embedding model keeps only the indexing step on-device. [Claude Code docs: data usage](https://code.claude.com/docs/en/data-usage)

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]], mainly the Level 3 chapter ([13:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=783s)–[19:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1167s)) and Finding Your Level ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s))

## Related

- Concepts: [[Second Brain Levels]] · [[Semantic Search]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Design for Retrieval]] · [[CLAUDE.md as a Router]] · [[Context vs Connections]] · [[LLM Wiki]]
- Techniques: [[Second Brain Pain-Point Audit]] · [[Build a Level 1 Second Brain]] · [[Ingest Sources into an LLM Wiki]] · [[Tiered Lookup Routing]] · [[Build a Knowledge Graph Layer]]
- Tools: [[Claude Code]] · [[Qdrant]] · [[Obsidian]]
- People: [[Nate Herk]]
- [[Home]]
