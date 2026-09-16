---
type: person
role: "Referenced — originator of the LLM Wiki pattern and the LLM Council project"
links: ["https://karpathy.ai/", "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f", "https://x.com/karpathy/status/2039805659525644595", "https://github.com/karpathy/llm-council", "https://en.wikipedia.org/wiki/Andrej_Karpathy"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tags: [topic/second-brain, topic/retrieval, topic/rag, topic/loops, topic/agentic-os, topic/memory, topic/portability]
---

# Andrej Karpathy

## Who

- **In the source:** named by [[Nate Herk]] as the person behind the LLM Wiki pattern he uses at level two of his second brain. Nate calls it "the Karpathy LLM Wiki" and notes he has made a separate full video on it ([08:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=498s), [08:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=500s)).
- **In [[AI LABS - Types of Claude Loops Explained]]:** named as the creator of LLM Council, which [[AI LABS]] say is close to their multi-agent review loop ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)).
- **In [[Chase AI - The Agentic OS Setup for Claude Code]]:** credited by [[Chase AI]] with a viral post about setting up an Obsidian knowledge base that LLMs can find their way around. Chase says it passed 20 million views ([17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s), [17:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1042s)).
- None of these videos says anything else about his background. That is covered under *Beyond the source* below.

## In this vault

- [[Nate Herk - Every Level of a Claude Second Brain]] — referenced as the originator of the LLM Wiki pattern (level two).
- [[AI LABS - Types of Claude Loops Explained]] — referenced; his LLM Council is named as close to their multi-agent review loop.
- [[Chase AI - The Agentic OS Setup for Claude Code]] — referenced; Chase credits him as the source of the raw / wiki / outputs vault structure he teaches (Chase's version differs from Karpathy's own post and gist; see *Beyond the source*).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] — referenced throughout. Nate relays the viral post and gist, then builds the wiki live from the gist.
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] — referenced. [[Matt Wolfe]] credits him with the knowledge-base idea and Obsidian as the front end ([08:06](https://www.youtube.com/watch?v=yke4fLQUsh4&t=486s)), then adds a journal and a CRM on top.
- [[Chase AI - The Three-Step Claude Code Agentic OS]] — referenced. Chase's May video gives the same raw / wiki / output credit as his June one ([09:03](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=543s)).
- This vault is built on the same pattern: plain markdown notes, an index ([[Home]]), and routing rules in the vault's CLAUDE.md. See [[LLM Wiki]].

## Ideas associated with them

### LLM Wiki — how Nate Herk uses it

Everything in this table comes from the video. It shows how one practitioner uses Karpathy's pattern, not what Karpathy himself wrote.

| Aspect | What the video says | When |
|---|---|---|
| Where it fits | Level two, whose question is whether you can pull everything on one topic together. Use it once you have more files that take a different shape and need organising together in a different way | [03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s), [08:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=491s), [08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s) |
| Good uses | Pulling together research on one project. Nate keeps separate wikis for his YouTube transcripts and for his meeting transcripts | [08:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=512s), [08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s) |
| Shape | Concept pages (e.g. agentic workflows, AI coding market, context window) linked to tools, techniques, comparisons and sources | [08:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=529s) |
| Who builds it | Claude Code created the pages itself when told to ingest a transcript | [09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s) |
| Obsidian | Only a viewer for the markdown files. Useful if you think visually, otherwise optional | [09:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=576s), [10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s) |
| How retrieval works | The agent starts at the index, opens the most likely page, then follows links from page to page, reading each one in full | [11:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=713s), [12:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=744s) |
| Not a knowledge graph | Wiki links work like "see also" backlinks. They don't say *how* two things relate (e.g. "is endorsed by") | [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s) |
| Limits | Wikis degrade somewhat as they grow ([11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s)). The agent must read a whole page even when it needs one detail, so a knowledge graph can be lighter for that job | [24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s) |
| Mixing levels | One brain can use a wiki for one folder and a vector index or graph for another. The whole brain doesn't need a single style | [17:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1071s), [18:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1084s) |
| Why Nate stays on it | Careful ingestion gives his wiki enough of a sense of relationships that he hasn't needed a graph | [23:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1427s) |
| When to adopt | You have 30+ notes and keep forgetting what's in them | [29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s) |

Related notes: [[LLM Wiki]] · [[Ingest Sources into an LLM Wiki]] · [[Second Brain Levels]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Knowledge Graphs]]

### raw / wiki / outputs: how Chase AI describes his structure

Everything in this table comes from [[Chase AI - The Agentic OS Setup for Claude Code]]. It is Chase's version of the idea, which differs from Karpathy's own post and gist (see *Beyond the source*).

| Aspect | What the video says | When |
|---|---|---|
| Origin | A common way to lay out an Obsidian vault for Claude Code comes from a Karpathy post | [17:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1033s), [17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s) |
| raw/ | Holds all unstructured data, such as a pile of research articles | [17:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1067s) |
| wiki/ | That research turned into structured, Wikipedia-style articles, so Claude reads one article instead of twenty sources | [17:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1077s) |
| outputs/ | Deliverables built from the wiki, such as a slide deck | [18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s) |
| Label | He calls it Karpathy's Obsidian "RAG", in air quotes | [19:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1152s) |
| Where the value is | An index.md at every level telling Claude what that level holds | [19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s) |
| Walk-through | Asked about AI agents, Claude reads the vault's index, goes into wiki/, reads that folder's index, then opens the article | [19:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1185s) |
| When indexes pay off | An index is pointless for a one-file folder, but it matters after years of use, with thousands of documents and subfolders | [20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s) |
| Folders are optional | The folder names are arbitrary. You don't need raw or outputs, only a map that fits your own data | [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s), [21:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1275s) |
| Getting started | Ask Claude Code to look at your vault and suggest a structure, using Karpathy's setup for inspiration | [21:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1294s) |
| CLAUDE.md | Add a vault CLAUDE.md describing the vault's conventions and folder structure | [21:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1306s) |

Related notes: [[LLM Wiki]] · [[Tiered Lookup Routing]] · [[CLAUDE.md as a Router]] · [[Agentic OS]]

### Idea files: building straight from the gist

Two sources show the gist used as an "idea file": you hand the write-up to an agent and let it build, instead of copying code.

| | [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (Claude Code) | [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] (Codex) |
|---|---|---|
| Input | Pastes the whole gist, plus a wrapper telling Claude to implement this idea file as his second brain and create the CLAUDE.md schema ([07:12](https://www.youtube.com/watch?v=sboNwYmH3AY&t=432s), [07:31](https://www.youtube.com/watch?v=sboNwYmH3AY&t=451s)) | Links the gist and says the vault folder is empty ([11:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=663s)) |
| Why it works | There's no repo to copy: you tell the agent to read the idea and implement it ([05:09](https://www.youtube.com/watch?v=sboNwYmH3AY&t=309s)). Karpathy left it vague so you can customise it ([05:28](https://www.youtube.com/watch?v=sboNwYmH3AY&t=328s)) | The hard part, the architecture, is already worked out in the gist ([10:43](https://www.youtube.com/watch?v=yke4fLQUsh4&t=643s)) |
| What the agent made | raw/ and wiki/, with default analysis, concepts, entities and sources subfolders ([07:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=474s)); his personal wiki is flat instead ([08:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=484s)) | 51 files, which he had pruned back to what the gist calls for: raw/, wiki/, AGENTS.md, index.md, log.md ([11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s), [11:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=713s)) |
| Gist operations covered | Lint health checks, described as Karpathy's but not demonstrated ([15:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=904s)) | Query answers filed back into the wiki as new pages, demonstrated ([18:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1114s)) |
| RAG | Hundreds of well-indexed pages suit a wiki, while millions of documents need a RAG pipeline ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)) | Not discussed |

**The lesson from comparing them.** Because an idea file leaves the implementation open, the same gist gives different scaffolds. Nate keeps and refines what Claude creates, while Matt prunes back to the minimum. Check what the agent built before you ingest anything.

Related notes: [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Ingest Sources into an LLM Wiki]]

### LLM Council: how AI LABS describe it

From [[AI LABS - Types of Claude Loops Explained]]:

- **The problem it answers.** A single review agent has to cover every angle of a review, which is too much for one agent. Spreading the review across several agents covers each one's blind spots ([07:21](https://www.youtube.com/watch?v=8wsM0euQOvc&t=441s), [07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s)).
- **The comparison.** They say the idea is close to Karpathy's LLM Council. They describe it as several agents discussing and arguing over a topic, using the reasoning of several models to reach the right answer ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)). See *Beyond the source* for how the repo actually works.
- **Their version.**
  - Four critic subagents: factual, domain, safety and style ([08:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=481s)).
  - A custom orchestrate command ties them together ([08:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=515s)) and runs them over several rounds of fixes ([08:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=534s)).
  - For agents that talk to each other directly, which is closer to the council, they point to Claude Code agent teams ([09:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=549s)).
  - They chose an orchestrator anyway, because one agent needs to hold the context of earlier rounds ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)).

Related notes: [[Multi-Agent Review and Scoring Loops]] · [[Loop Engineering]] · [[Subagents and Agent Teams]]

## Beyond the source

None of the following comes from any of the videos.

- **Career:** founding member and research scientist at OpenAI (2015–2017). Director of AI at Tesla, leading Autopilot computer vision (2017–2022). Back at OpenAI 2023–2024. PhD from Stanford (2015) under Fei-Fei Li, where he designed and taught CS231n, Stanford's first deep learning course. — [karpathy.ai](https://karpathy.ai/), [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)
- **Eureka Labs:** launched this AI-native education company in July 2024. — [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)
- **Anthropic:** announced on 19 May 2026 that he had joined Anthropic's pre-training team, where he is to start a team using Claude to speed up pre-training research. — [TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)
- **"Vibe coding":** coined the term in February 2025. — [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)
- **The LLM Wiki write-up:** a GitHub gist titled "LLM Wiki", created 4 April 2026. — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
  - He called it an "idea file": a description of the pattern you paste into your own agent so it builds a version for you, instead of sharing code. — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [Lobster Pack write-up](https://www.lobsterpack.com/blog/karpathy-llm-wiki-idea-files/)
  - It has three layers:
    1. curated raw sources;
    2. a markdown wiki that the LLM writes and maintains;
    3. a schema document that defines the wiki's structure and how to keep it up to date.
  - It has three operations: **ingest** (fold a new source into the pages it affects and flag contradictions), **query** (answer by combining wiki pages) and **lint** (find stale or inconsistent content).
  - The point is that knowledge builds up over time, instead of being pulled back out of raw chunks on every query as in classic RAG. — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- *My own comparison, not a claim from either source:* in Nate's setup, CLAUDE.md / AGENTS.md routing rules play roughly the role of the gist's schema layer. See [[CLAUDE.md as a Router]].
- **Checking the gist against the two idea-file builds** (checked 2026-09-15).
  - The gist calls itself an idea file meant to be pasted into your own agent, and says it is deliberately abstract.
  - It names CLAUDE.md (for Claude Code) or AGENTS.md (for Codex) as the schema file. So Nate's CLAUDE.md and Matt's AGENTS.md both follow it.
  - It says good query answers can be filed back into the wiki as new pages, which Matt's agent did ([18:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1114s)).
  - Its own scale note is about 100 sources and hundreds of pages.
  - — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Porting Matt's build to Claude Code.** Claude Code reads CLAUDE.md, not AGENTS.md. Add a CLAUDE.md that imports `@AGENTS.md`, or symlink it. — [Claude Code docs: memory](https://code.claude.com/docs/en/memory)
- **Scale figures.**
  - Nate says Karpathy was working with about 100 articles and "about half a million words" ([02:55](https://www.youtube.com/watch?v=sboNwYmH3AY&t=175s)). Karpathy's post says about 100 articles and about 400K words, so Nate's word count is an overstatement.
  - Nate's quote about not needing "fancy RAG" at this small scale does match the post ([02:43](https://www.youtube.com/watch?v=sboNwYmH3AY&t=163s)).
  - The 95% token cut Nate mentions comes from an unnamed X user, not from Karpathy, and has no primary source ([05:00](https://www.youtube.com/watch?v=sboNwYmH3AY&t=300s)).
  - — [X post via FxTwitter](https://api.fxtwitter.com/karpathy/status/2039805659525644595)
- **The "LLM Knowledge Bases" post on X.**
  - Posted 2 April 2026, two days before the gist. It showed about 21.9 million views when checked on 2026-09-15, which fits Chase's "over 20 million" ([17:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1042s)). Earlier press coverage cited 16M+.
  - The post describes collecting sources in a `raw/` directory, having the LLM compile a markdown wiki, and filing generated outputs (markdown pages, slide decks, charts) back into the wiki.
  - It doesn't name a separate outputs folder, and the gist's third layer is a schema file, not outputs. So Chase's raw / wiki / outputs split and "index.md at every level" are his own adaptation.
  - — [X post](https://x.com/karpathy/status/2039805659525644595) (text and view count read via [FxTwitter](https://api.fxtwitter.com/karpathy/status/2039805659525644595)), [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [Chavez Calva write-up](https://joseluischavezcalva.substack.com/p/karpathys-llm-knowledge-bases)
- *My own comparison:* the gist presents the wiki as knowledge compiled once and kept up to date, in contrast to classic RAG, which works from raw chunks on every query (see the gist bullet above). Chase's "RAG" label ([19:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1152s)) is loose, and he does put it in air quotes.
- **LLM Council.**
  - Repo `karpathy/llm-council`, created 22 November 2025. It is a small web app built on OpenRouter that works in three stages:
    1. Every model answers the question on its own.
    2. Each model ranks the other models' answers, with identities hidden.
    3. A designated chairman model writes the final answer.
  - The README calls it a vibe-coded Saturday hack that he won't support.
  - AI LABS's "agents that talk to each other and argue" ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)) is therefore inaccurate: the models never debate directly. Review is anonymous ranking followed by a chairman's synthesis.
  - — [repo](https://github.com/karpathy/llm-council), [GitHub API (creation date)](https://api.github.com/repos/karpathy/llm-council)

## Related

- [[Home]]
- [[Nate Herk]]
- [[Matt Wolfe]]
- [[Chase AI]]
- [[AI LABS]]
- [[Bootstrap an LLM Wiki from the Karpathy Gist]]
- [[Add a Journal and Personal CRM to a Second Brain]]
- [[LLM Wiki]]
- [[Ingest Sources into an LLM Wiki]]
- [[Multi-Agent Review and Scoring Loops]]
- [[Agentic OS]]
- [[Obsidian]]
- [[Claude Code]]
