---
type: tool
category: Always-on memory system for AI agents (open source)
website: https://github.com/garrytan/gbrain
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tags: [topic/second-brain, topic/memory, topic/automation, topic/retrieval, topic/knowledge-graph, topic/agents]
---

# GBrain

## What it is

GBrain is [[Nate Herk]]'s example of a Level 5 second brain, the "always-on Brain OS" ([25:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1526s)). It was created by [[Garry Tan]] ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s), [25:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1532s)). It bundles everything from the lower levels and keeps itself updated. Technical details from the repo are under *Beyond the source*.

## How sources use it

### [[Nate Herk - Every Level of a Claude Second Brain]]

#### What GBrain is, per the video

- **What Level 5 means.** The second brain becomes so autonomous that you don't have to think about it ([03:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=229s)). His name for this level is the always-on Brain OS, and GBrain is his example ([25:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1526s)).
- **Who made it.** Garry Tan, whom he introduces as CEO of Y Combinator ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s)). He says it pairs really well with gstack ([25:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1534s)). The video doesn't say who makes gstack; see *Beyond the source*.
- **What's inside.** It's essentially the idea of everything covered at the earlier levels ([25:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1535s)): wikis, routing, relationships and tools ([25:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1539s)).
- **What sets it apart.** An always-on element ([25:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1541s)). It keeps syncing, refreshing memories and adding more material ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s), [25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s)).
- **Not a new architecture.** It's very similar to everything else he covered. The difference is the auto-updating, autonomous, always-on feel ([26:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1562s), [26:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1565s)).

**How GBrain's ingredients map onto his levels**

| Ingredient he names | Level where it first appears | Concept note |
|---|---|---|
| Routing | Level 1 | [[CLAUDE.md as a Router]] |
| Wikis | Level 2 | [[LLM Wiki]] |
| Relationships | Level 4 | [[Knowledge Graphs]] |
| Tools | Not tied to a level in the video | n/a |
| Continuous sync and memory refresh | New at Level 5 | [[Always-On Brain OS]] |

Semantic search (Level 3) isn't in his list of GBrain ingredients. *Beyond the source* covers what the repo actually implements.

#### Where to run it

| Harness | What he says | Where |
|---|---|---|
| [[Hermes Agent]] | Adding GBrain to something like Hermes Agent would be really good. He has been playing with GBrain on his Hermes agent | [25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s), [25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s), [25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s) |
| [[Claude Code]] | Possible, but you'd have to handle the cron jobs and set everything up yourself | [25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s), [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s), [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s) |

That setup burden is part of why he doesn't currently run GBrain ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).

#### When GBrain is the right level

- **The signal.** Look at Level 5 when your agents run on their own (captioned "offline") ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)), you have a lot of data, and you want several Hermes agents synced together ([29:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1767s), [29:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1769s)). That points to something like GBrain ([29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)).
- **Not the goal by default.**
  - Level 5 isn't "the best", and he has arguments for not sitting there himself ([03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s), [03:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=237s)).
  - Find the lowest level that fits your needs ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)). With no pain point, don't build new architecture ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).
- **His own brain runs almost entirely at Level 2** ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)).
- See [[Second Brain Levels]] and [[Second Brain Pain-Point Audit]].

#### His reservations about always-on brains

- **Too much context.** An always-on brain raises a question that scares him a little ([26:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1572s)). When does the brain have so much context that it does more damage than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1580s))?
- **Manual control of ingestion.** He stays in complete control of what his brain ingests ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)). A skill collects the week's meeting transcripts ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)). He also hands Claude material, asks for help working out where it fits, and they ingest it together ([26:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1591s)). Part of that captioned request is garbled.
- **Context vs connections.**
  - Of his "four C's" (context, connections, capabilities, cadence), a second brain is mainly about the first two ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s), [26:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1604s), [26:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1607s)).
  - Connections are data that isn't evergreen, like Slack threads, emails and customer data ([27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s), [27:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1647s), [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)). Ingesting them just adds noise you'd be deleting every month ([27:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1657s), [27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s)).
  - His test: will this memory still be useful a year from now ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s))?
  - Anything that fails the test shouldn't be pulled in. The brain should be able to go fetch it instead ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)).
  - See [[Context vs Connections]] and [[Tiered Lookup Routing]].

## Notes

- **Implication (my reading, not stated by him).** An always-on sync that keeps adding material is exactly where his noise and too-much-context worries bite. If you adopt GBrain, decide deliberately what it may ingest, e.g. evergreen context only. Leave fast-changing sources as live lookups.
- **What the video doesn't cover.** No GBrain demo, install, configuration or architecture. He only describes what it is and where he'd run it.
- **Caption fixes.** "Gbrain" and "G brain" → GBrain; "G stack" → gstack; "cloud code" → Claude Code.

## Beyond the source

*Not from the video. Each item was checked on 2026-09-15 at the linked page. Repo details can change, so re-check before building.*

- **Repo and basics.**
  - The code is at github.com/garrytan/gbrain. Its GitHub description calls it Garry's opinionated OpenClaw/Hermes Agent brain.
  - The README pitches it as a memory you control for the agent you already use.
  - It's MIT-licensed and installs with Bun (`bun install -g github:garrytan/gbrain`).

  <https://github.com/garrytan/gbrain>
- **Storage.** Knowledge lives as markdown files in a regular git "brain repo", which is the system of record. That repo is synced into PGLite (local) or Postgres with pgvector (larger or shared deployments). <https://github.com/garrytan/gbrain>
- **Retrieval.** Search is hybrid: vector search on pgvector, BM25 keyword search and reciprocal-rank fusion, plus a self-wiring knowledge graph with typed edges. <https://github.com/garrytan/gbrain>
  - Semantic search is optional. Without an embedding-provider API key GBrain runs keyword-only, and adding a key enables embeddings.
  - My mapping onto Nate's ladder: keyword (Level 1), semantic (Level 3) and graph (Level 4) retrieval in one package, over a markdown store like Level 2. See [[Keyword vs Semantic vs Graph Retrieval]].
- **The always-on part.** The README describes an overnight "dream cycle" that enriches the brain while you sleep. It argues that a 24/7 background process that ingests, enriches and consolidates is easier than keeping a chat agent working hard. The README calls a server-hosted OpenClaw or Hermes agent with 24/7 crons, continuous ingestion and the dream cycle "GBrain as intended". It also flags this as the highest-cost path: a deployed server plus API token usage. That matches the always-on element Nate describes and his view that Hermes is a good home for it (my mapping). Laptop agents like Claude Code and Codex connect over MCP or a plugin instead. <https://github.com/garrytan/gbrain>
- **Agents it names.** OpenClaw, Hermes, Claude Code and Codex, among others. It exposes a CLI and MCP for connecting agents. <https://github.com/garrytan/gbrain>
- **The gstack pairing.** gstack is Garry Tan's open-source toolkit that turns Claude Code into a virtual engineering team of specialist roles. Its README has a GBrain section ("persistent knowledge for your coding agent") with a `/setup-gbrain` command. That's the pairing Nate mentions. <https://github.com/garrytan/gstack>
- **Garry Tan's title.** He is President and CEO of Y Combinator; the video says "CEO". <https://www.ycombinator.com/library/JZ-garry-tan-president-and-ceo-of-y-combinator>
- **If you run it from Claude Code.** Claude Code has three schedulers: cloud Routines (minimum interval one hour), Desktop scheduled tasks (the machine must stay on) and session-scoped `/loop` (recurring tasks expire after 7 days). Pick one to drive GBrain's maintenance jobs. <https://code.claude.com/docs/en/scheduled-tasks>

## Related

- **Concepts:** [[Always-On Brain OS]], [[Second Brain Levels]], [[Context vs Connections]], [[Knowledge Graphs]], [[Semantic Search]], [[Keyword vs Semantic vs Graph Retrieval]], [[LLM Wiki]]
- **Techniques:** [[Second Brain Pain-Point Audit]], [[Tiered Lookup Routing]], [[Build a Knowledge Graph Layer]]
- **Tools:** [[Hermes Agent]], [[Claude Code]], [[OpenAI Codex]]
- **People:** [[Garry Tan]], [[Nate Herk]]
- **Source:** [[Nate Herk - Every Level of a Claude Second Brain]]
- [[Home]]
