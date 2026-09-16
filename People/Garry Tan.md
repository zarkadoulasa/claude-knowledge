---
type: person
role: "Referenced — CEO of Y Combinator; creator of GBrain (and gstack)"
links: ["https://www.ycombinator.com/people/garry-tan", "https://github.com/garrytan", "https://github.com/garrytan/gbrain", "https://github.com/garrytan/gstack"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tags: [topic/second-brain, topic/memory, topic/knowledge-graph, topic/agents, topic/claude-code]
---

# Garry Tan

## Who

- **In the source:** introduced as the CEO of Y Combinator who created [[GBrain]] ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s)). [[Nate Herk]] adds that GBrain pairs very well with gstack ([25:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1534s)). The video doesn't say who made gstack; see *Beyond the source*.
- GBrain is Nate's example of a level-five, always-on second brain ([25:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1526s)).

## In this vault

- [[Nate Herk - Every Level of a Claude Second Brain]] — referenced as the creator of GBrain, the level-five example.

## Ideas associated with them

### GBrain as the level-five "always-on Brain OS"

Everything in this table comes from the video.

| Aspect | What the video says | When |
|---|---|---|
| What level five is | A second brain autonomous enough that you stop thinking about maintaining it | [03:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=229s) |
| Level label | The always-on Brain OS, with GBrain as the example | [25:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1526s) |
| What GBrain bundles | Everything from the lower levels: wikis, routing, relationships and tools | [25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s) |
| What sets it apart | It is always on: it keeps syncing, refreshing memories and adding new material | [25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s) |
| Suggested host | Adding it to something like [[Hermes Agent]] would work really well | [25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s) |
| In [[Claude Code]] | Possible, but you'd have to set up and manage the scheduled (cron) jobs yourself | [25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s) |
| Nate's own status | He doesn't run GBrain day to day. He is experimenting with it on his Hermes agent | [25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s) |
| How different it really is | Much like the lower levels. What it adds is automatic updating and autonomy | [26:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1562s) |
| Nate's reservation | He worries an always-on brain takes in so much context it does more harm than good. He prefers to decide himself what gets ingested | [26:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1570s), [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s) |
| When to pick it | You run agents "offline" (as captioned; probably meaning unattended), you have a lot of data, and you want several Hermes agents synced to one brain | [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s) |

Related notes: [[Always-On Brain OS]] · [[GBrain]] · [[Second Brain Levels]] · [[Context vs Connections]] · [[Second Brain Pain-Point Audit]]

## Beyond the source

None of the following comes from the video.

- **Role and background:** President and CEO of Y Combinator, and a General Partner. He was a YC partner earlier (2011–2015). He co-founded Initialized Capital and Posterous (YC S08, later acquired by Twitter), was an early designer and engineering manager at Palantir, and studied computer systems engineering at Stanford. — [YC profile](https://www.ycombinator.com/people/garry-tan)
- **GBrain** is open source under the MIT licence. Its tagline is about giving the agent you already use a memory that you control. — [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain)
  - **Storage:** markdown git repos as the system of record, plus Postgres (PGLite by default for personal brains, or Postgres with pgvector for shared or large ones).
  - **Retrieval:** hybrid, combining vector and keyword (BM25) search with reranking. Each page write adds typed edges to a knowledge graph, and answers come with citations.
  - **Background work:** a cron-driven "dream cycle" runs overnight, while you sleep. It de-duplicates people pages, fixes citations, scores salience, finds contradictions and preps the next day's tasks. That scheduled upkeep is the kind of always-on behaviour Nate describes.
  - **Agents:** built for OpenClaw and Hermes Agent, and also works with Claude Code, Codex, Cursor and other MCP clients.
- **gstack** is Garry Tan's open-source (MIT) Claude Code setup: 23 "specialists" plus eight "power tools", all as markdown slash commands. The specialists map to roles such as CEO/founder, eng manager, designer, QA lead, security officer, release engineer and technical writer. — [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
  - **The GBrain link:** the gstack README connects GBrain through a `/setup-gbrain` command, backed by Supabase, local PGLite or a remote MCP brain, so the coding agent keeps a persistent knowledge base (`/sync-gbrain` keeps code indexed). This is the pairing Nate mentions. — [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- GitHub profile: [github.com/garrytan](https://github.com/garrytan)

## Related

- [[Home]]
- [[Nate Herk]]
- [[GBrain]]
- [[Hermes Agent]]
- [[Always-On Brain OS]]
- [[Knowledge Graphs]]
