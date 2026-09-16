---
type: concept
aliases: ["Work Backwards from the Question", "Retrieval-First Storage Design"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Knowing More - Every Claude Model Explained]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tags: [topic/retrieval, topic/second-brain, topic/rag, topic/context, topic/models, topic/agentic-os]
---

# Design for Retrieval

## In one sentence

Decide how to store knowledge by starting from how you'll ask for it later. The shape of the question sets the shape of the storage: whole files, vector chunks, graph edges, or not ingesting at all.

## How it works

### The principle

- **Work backwards.** Reverse-engineer your storage from the questions you'll ask ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)). How the data will be accessed and recalled should decide how it goes in ([02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)).
- **The hoop analogy.** You already know the hoop's shape and that the ball has to pass through it, so you wouldn't make a square ball ([02:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=166s)). Start with the end in mind ([03:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=180s)). Here the hoop is the future question and the ball is the stored data.
- **The success test.** Can your agent find it again, and could you? If not, the routing or folder layout is wrong ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s), [02:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=139s)).
- **Nate's final check.** Does the system know where the data lives and where to look, and does it give accurate answers ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s))?
- **Decide per dataset, not per vault.** A second brain doesn't have to use one style throughout ([17:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1069s), [17:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1078s)). Choose each folder's structure from the type of data and how you use it ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)). In the Level 3 example, context, projects and decisions stay as markdown and only one unit (e.g. YouTube transcripts) is vectorised ([17:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1056s)). See [[Second Brain Levels]].

### Question shape → storage shape

| Question you'll ask | Example from the video | Store it as | Why |
|---|---|---|---|
| **Whole-document synthesis** (summarise, rank, find the max across everything) | "Summarise the March 5 meeting." "Which week had the highest sales?" | One complete markdown file per unit, read end to end | Chunk retrieval only sees some of the content, so it misses information or picks the wrong maximum ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s), [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)) |
| **Pinpoint lookup in a large text corpus** | "Remind me what rule 17 was" (out of 1,000 rules) | Vector index: chunks plus embeddings | Returns just the snippet. Reading all 1,000 rules wastes time and tokens ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s), [18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s), [18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)) |
| **Fuzzy recall** (your words differ from the note's) | Searching "feedback" should also surface pages on test results and skill evaluations | [[Semantic Search]] layer | Keyword search only returns literal matches ([14:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=887s), [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s), [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s)) |
| **Exact file or name lookup** | Finding the slide deck for a specific dated video | Plain folders plus CLAUDE.md routing rules | Both you and the agent can follow the drill-down ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s), [07:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=464s)) |
| **Relationship chains** (ask about X, trace back to A) | A person works at a company, which is endorsed by another entity that competes with a third (fictional demo data) | [[Knowledge Graphs]]: entities plus typed relationships | Wiki links are just see-also links and don't say how things relate ([03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s), [12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s), [23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s)) |
| **Recent, changing conversations** | What he and a colleague discussed last week about a quarterly project | **Don't ingest.** Check the stable files and wiki first, then fetch from the live tool (ClickUp) | Volatile data becomes noise that needs monthly clean-up ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s), [28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s), [28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s), [28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)) |

For a side-by-side of the three retrieval styles, see [[Keyword vs Semantic vs Graph Retrieval]].

### Worked example 1: meeting summaries need the full file

Nate ties this example directly back to the work-backwards principle ([15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s)).

1. **Store as chunks.** The March 5 meeting transcript goes into the brain as vectorised chunks, around 20 of them ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s)).
2. **Ask for a summary.** The agent searches for chunks similar to "March 5 meeting summary" ([16:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=984s)).
3. **See what breaks.** Even when it retrieves the right chunks, it summarises only those few. It never sees the whole transcript ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [16:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=991s)), so the "summary" can leave out key information ([16:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=998s)).
4. **Tuning helps, but only partly.** Metadata and similar tweaks can improve results. Still, people assumed vector databases were a magic fix that always returns what you need, and Nate calls that very false ([16:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1001s), [16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s)).
5. **Same failure with tables.** Asked for the highest-sales week, the agent may grab one chunk of the table and answer from it. Weeks in other chunks that were higher get missed ([16:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1015s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)).
6. **Fix it.** When a question needs full context, don't chunk. Keep one markdown file for March 5 and have the agent read all of it ([17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s), [17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)). That is more accurate ([17:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1047s)).

### Worked example 2: huge rule sets suit vector search

- Vector retrieval is strong when you have lots of text and need one specific, closely matching answer ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s)).
- **Example:** store 1,000 rules and ask what rule 17 was. The search pulls the relevant chunks and returns a short snippet ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)).
- Making the agent read the whole 1,000-rule file for one answer would waste time and tokens ([18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)).
- Semantic search has further dials: chunking, embedding, hybrid search and re-ranking ([18:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1095s)).

### Worked example 3: the same trade-off between wiki and graph

- **Wiki cost:** a wiki agent reads a whole page even when it needs one detail, e.g. the full AI video production page just to learn about one tool on it ([24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s)).
- **Graph benefit:** for that kind of question a knowledge graph can be lighter ([24:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1453s)).
- **When to skip the graph:** if you never ask relationship-chain questions, you probably don't need one ([25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s)).

### Retrieval failures are often capture failures

- **The common misconception** is that the system is bad at retrieving ([22:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1342s)). Sometimes it is. Often the bigger problem is that the knowledge never got out of your head and into the files ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).
- **Before blaming the AI,** look through your folders and files. Are they complete? Do they hold the nuance you carry in your head ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s))?
- **The software usually isn't the hard part.** Whatever graph software you use will typically do a decent job of building the relationships. The hard part is giving it enough data ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)), and that data probably already exists in your folders ([20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s)).
- **Capture fix: interviews.**
  - Run a Grill Me session per subject (client A, client B, business A) ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)). It questions you relentlessly and doesn't stop until it knows the topic ([20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s), [21:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1262s)).
  - Feed it files, transcripts and contracts along the way ([21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s)).
  - See [[Grill Me Interview Skill]].
- **Ingest quality is itself a retrieval feature.** Nate gets enough of a sense of relationships from his LLM Wiki because he put so much effort into ingesting sources properly and with context ([23:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1427s)).

### What *not* to store is also a design decision

- **Store:** evergreen context you won't delete. His filter is whether the memory will still be useful in a year ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s), [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)).
- **Don't store:** material that will change next week ([27:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1678s)). Make sure the brain can fetch it live instead ([28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)).
- See [[Context vs Connections]] and [[Tiered Lookup Routing]].

### A coherent structure is the agent's map (Chase AI)

*Everything above comes from [[Nate Herk - Every Level of a Claude Second Brain]]. This section and the next two add other sources.*

[[Chase AI - The Agentic OS Setup for Claude Code]] makes the same "can it find it again" argument, but in terms of navigation cost.

- **Structure matters more than the tool.** Obsidian isn't required; a traditional database can do the same job ([13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s)–[13:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=835s)). He claims a coherent file structure alone gets you about 99% of the way ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)–[14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s)). That's his opinion, not a measurement.
- **What good looks like.** You open Claude Code in a folder with a huge number of subfolders and files, ask about any of them, and get a quick, accurate answer ([15:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=953s)–[16:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=978s)).
- **What bad looks like.** One folder with millions of files, no backlinks and no hierarchy. Claude struggles to find answers fast. Slow here also means more tokens, and so more money ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s)–[16:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1000s)).
- **The mental model.** You're building Claude a map with a clear path to every file ([16:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1004s)–[17:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1026s)).
- **An index in every room.** He sees the real value of the [[Andrej Karpathy]]-style raw/wiki/outputs layout as the `index.md` at each level, telling Claude what that level holds ([19:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1168s)–[19:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1183s)). Asked about AI agents, Claude reads the vault's index, heads into `wiki/`, and finds another index there ([19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s)–[20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s)). An index for a one-file folder is overkill, but it pays off once there are thousands of documents ([20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s)–[20:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1251s)). If every room Claude enters explains what's in it, lookups get faster and cheaper ([20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s)–[21:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1265s)).
- **Folder names are arbitrary; the map isn't.** You don't need his folders or Karpathy's, just a map that makes sense for your data ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)–[21:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1290s)). If you're unsure, ask Claude Code to look at the vault and propose a structure ([21:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1292s)–[21:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1304s)).
- **Write the map down.** His vault's CLAUDE.md describes the vault structure and includes a navigation pattern, the path Claude should follow to find things ([21:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1306s)–[22:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1333s)). See [[CLAUDE.md as a Router]].
- **Design for loops too.** Skill and automation outputs should be logged where a self-improving loop can see past runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)). Here retrieval serves the agent's own improvement, not just your questions. See [[Loop Engineering]].

### Saved knowledge has to come back out (Matt Wolfe, Chase AI)

- **The storage graveyard.** [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] says most second brains are just storage ([00:41](https://www.youtube.com/watch?v=yke4fLQUsh4&t=41s)). Everything gets dumped in one place, and unless you keep reviewing and searching it, nothing saved there is ever looked at again ([00:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=53s)).
- **His fix builds retrieval into daily use.** Journal replies must draw on the wiki, past journal entries and the CRM ([22:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1347s), [22:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1367s)). The plan is for the system to resurface relevant ideas when he needs them ([05:33](https://www.youtube.com/watch?v=yke4fLQUsh4&t=333s)). Plain questions run as wiki queries that check the index first and file the reusable part of the answer back into the wiki ([18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s)).
- *This note's reading:* when you list questions in step 1 below, also list what should come back to you *without* being asked, and name the moment it should surface.
- **Chase's May video: the path has to work for both of you.** In [[Chase AI - The Three-Step Claude Code Agentic OS]], the vault must give Claude Code a clear path for where data flows, and give you one too ([16:31](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=991s)). Claude working it out alone isn't enough, because you need to see what's going on ([16:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1001s)). A CLAUDE.md that maps the memory structure makes lookups cheaper for Claude and the vault navigable for you ([12:03](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=723s), [12:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=732s)).

### Agent-first organisation (Jay E)

[[Jay E - The ARMS Framework for a Claude Agentic OS]] ends up somewhere similar, starting from the other side: stop organising for people.

- **Level 1, a flat workspace, is fine while it's small.** With only a few files it mostly works ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)–[11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s)).
- **Scale is what breaks it.** When he pointed his second-brain app at his workspace folder, he found about 60,000 files. That hurts both how fast you can retrieve information and how quickly you use up your plan ([11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s)–[11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)). Once retrieval slows, he moves on to organising the workspace for the agent ([11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)–[11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s)).
- **Don't optimise for a file explorer.** People used to name and folder files neatly so they could find things themselves. Now that agents do the work on files, he says names and file-explorer navigability matter much less ([11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s)–[12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s)).
- **Use router files instead.** At minimum, CLAUDE.md is the central router. It describes his departments so Claude works inside the right set of files for each ([12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s)–[12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)). Each department also has its own router file. `content.md`, for example, just lists that area's skills and reference files ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)–[13:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=785s)). Agents read files very fast, so routers get them to the right one in the fewest steps ([13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)–[13:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=809s)).
- **Humans get a separate layer.** His Level 3 is a visual second brain that shows how files connect and searches faster. It helps visual thinkers and makes it easier to explain systems to others, and it finds a skill far faster than a file explorer ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)–[14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s)).

### Cost is a second design axis

Nate's framing asks *what shape* a question needs. Several of the newer sources add a second question: *what it costs* to answer. That depends partly on the structure and partly on which model does the reading. See [[Choosing a Claude Model]].

- **Match the model to the reading job.** [[Knowing More - Every Claude Model Explained]] recommends Haiku for quick tasks, batch jobs and repetitive work because it's fast and cheap ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)–[06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s)). Its examples include quick summaries and pulling key information out of documents ([01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s)–[01:43](https://www.youtube.com/watch?v=BJauPEH_9OU&t=103s)). Haiku's limit is depth, meaning hard engineering or nuanced analysis ([01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s)–[02:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=124s)). Sonnet covers everything else ([06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s)–[07:00](https://www.youtube.com/watch?v=BJauPEH_9OU&t=420s)). Opus is for hard engineering, financial modelling and decisions that are hard to reverse ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)–[07:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=426s)), and it's expensive and token-hungry ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s)–[04:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=262s)).
- **Let a cheap model do the bulk reading.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] suggests a Haiku subagent that reads hundreds of thousands of tokens of scraped articles and hands the Opus main agent just a short summary. It makes no sense for a heavy, expensive model to read all that for a few facts ([06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=388s)).
- **Navigation costs tokens too.** Chase links a messy structure to extra tokens and money ([16:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=993s)–[16:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1000s)). Jay links file sprawl to using up your plan faster ([11:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=684s)–[11:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=690s)). [[Simon Pittman - Set Up Claude Cowork]] says a context map of a connected tool stops Claude burning tokens looking for things ([31:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1863s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s)). He also runs a routine document task on Sonnet to save credits ([33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s)–[33:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=1996s)).
- **A big context window doesn't remove the choice.** Knowing More describes Sonnet's 1M-token window as roughly 2,000–3,000 pages in one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)–[02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s)). The same video complains that Claude burns through tokens very fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)–[06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)). *This note's reading:* "can it fit" and "should you pay to read it all" are separate questions. When a question needs the whole file (worked example 1), reading the whole file is still the right shape; the model choice decides what that read costs.

**Who should do the reading** *(this note's synthesis; question shapes from the table above)*

| Question shape | Who reads | Why (source) |
|---|---|---|
| Whole-document synthesis across many files | A cheaper model or subagent reads and summarises; the main model reasons over the summaries | Bulk reading on an expensive model is wasteful ([Nate, 32 tricks, 06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)) |
| Pinpoint lookup in a large corpus | Any model; vector search already keeps the read small | Returns a short snippet ([Nate, second brain, 18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)) |
| Exact file lookup through routers or indexes | Any model; the router or index cuts how many files get opened | Fewest steps ([Jay E, 13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)); faster and cheaper ([Chase, 20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s)) |
| Judgement on what was retrieved (hard analysis, hard-to-reverse decisions) | The strongest model | Knowing More's use cases for Opus ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)) |

## When to use it — and when not to

**Use it:**
- before creating any new folder, wiki, vector index or graph layer
- when choosing between plain markdown and semantic search for one dataset. Nate suggests describing the data and its intended use to Claude Code and asking which fits ([19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s))
- when answers are wrong or incomplete. Work out whether the cause is storage shape (chunks for a whole-document question, [16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s)), routing (no rule points there, [04:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=297s)) or capture (the nuance was never written down, [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s))
- when a workspace gets big enough to slow lookups or eat into plan limits. Jay E treats that as the signal to add router files; his workspace had about 60,000 files ([11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s)–[11:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=700s)). Chase AI's answer to the same slowdown is an index at every level ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s), [20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s))
- when choosing which model reads each dataset: a cheap model for bulk or batch reading, a strong one for judgement ([Knowing More, 06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s); [Nate, 32 tricks, 06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s))

**Don't:**
- make vector search the default for everything. It is not a magic solution ([16:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1008s))
- choose an architecture because it looks impressive. What matters is whether the system can hand you the answer ([10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s))
- redesign storage when nothing hurts ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s))

**Apply it in five steps.** The ordering is a synthesis. Steps 1–4 come from Nate's second-brain video; step 5 comes from the later sources.
1. List the real questions you'll ask of this data ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)).
2. Classify each question with the table above: whole-document, pinpoint, fuzzy, exact, relationship or volatile.
3. Store each dataset in the shape its main question needs, folder by folder ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)).
4. Before blaming retrieval, audit whether the files hold the nuance ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)).
5. Make every large folder cheap to navigate, and decide who does the reading.
   - Where an agent has to choose among many files, add an index or router file ([Chase, 20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s); [Jay E, 12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)).
   - Pick the model that does the bulk reading for each dataset ([Knowing More, 06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s); [Nate, 32 tricks, 06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)).

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] by [[Nate Herk]] sets this out as the mindset to adopt before choosing any second-brain level ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)).
  - **Argued from failure cases:** chunked meeting summaries and partial sales tables ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s), [17:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1028s)).
  - **And from success cases:** the 1,000-rules lookup ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)).
  - **Distinctive angle:** retrieval problems often start upstream, at capture ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]] — A coherent structure is Claude's map. Give every level an `index.md` and add a navigation pattern to the vault's CLAUDE.md. Without these, lookups are slow and use a lot of tokens ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s)–[17:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1026s), [19:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1168s)–[22:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1333s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]] — Organise for the agent, not for a file explorer: a CLAUDE.md router plus a router file per department. Human lookup moves to a visual second brain ([11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s)–[14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s)).
- [[Knowing More - Every Claude Model Explained]] — Haiku for quick or batch reading, Sonnet by default, Opus for hard or hard-to-reverse work. That makes cost a design choice alongside question shape ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)–[07:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=426s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] — Have a Haiku subagent do the bulk reading and pass a summary to Opus ([06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=388s)).
- [[Simon Pittman - Set Up Claude Cowork]] — A context map of a connected tool lets Claude find live data first time and saves the tokens it would spend searching ([30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s)).
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] — Storage alone is where saved knowledge dies. Make it resurface through journaling and queries that draw on the wiki ([00:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=53s), [22:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1347s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]] — Memory needs a structure both Claude and you can navigate, written down in CLAUDE.md ([12:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=732s), [16:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1001s)).

## Where sources disagree

**1. Does the structure also have to work for people?**
- [[Nate Herk - Every Level of a Claude Second Brain]]: the test is whether your agent can find something again, *and whether you can* ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s), [02:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=139s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: now that agents work on the files, you don't need to pay as much attention to names or how easy things are to browse in a file explorer. Router files matter more ([11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s)–[12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]] is closer to Jay. The map is for Claude, the folder names are arbitrary, and you ask Claude a question rather than browsing yourself ([16:09](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=969s)–[16:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=978s), [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s)–[21:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1273s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]], Chase's earlier May video, sides firmly with Nate: Claude working it out isn't enough, and you need a clear path too ([16:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1001s)). His emphasis shifted between the two videos.
- *One way to reconcile them (this note's reading):* Jay doesn't drop human findability. He moves it to a visual search layer ([13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)), and his routers are plain markdown a person can read. If you don't have that kind of layer, Nate's two-sided test is the safer default.

**2. Is a good structure enough on its own?**
- Chase: a coherent file structure gets you about 99% of the way; Obsidian or a database are extras ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)–[14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s)). His earlier May video is blunter: 99.9% of people need neither LightRAG nor a vector database ([11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s)).
- Nate: some question shapes need more than folders. Pinpoint lookups in a large corpus suit vector search ([18:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1103s)), and relationship chains suit a graph ([23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s)).
- *Note:* Chase's memory level never gets to semantic search or graphs, so read his 99% as applying to questions you can answer by navigating folders.

**3. When should routing start?**
- Nate's Level 1 already has routing rules in CLAUDE.md, such as where to look for quarter-one priorities ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)–[04:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=289s)).
- Jay starts with a flat workspace and adds router files once retrieval slows down ([10:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=657s)–[11:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=700s)).

**4. Load everything, or route?**
- Knowing More presents the 1M-token window as fitting thousands of pages into one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)–[02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s)).
- Nate: Claude won't search your whole project unprompted, and you wouldn't want it to, because that wastes time and tokens ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=308s)).
- Knowing More's own complaints about token burn and usage limits ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s)–[04:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=262s), [06:03](https://www.youtube.com/watch?v=BJauPEH_9OU&t=363s)–[06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)) back Nate on cost.

## Beyond the source

*Not from the videos. Each item below was checked against the linked page.*

- **Anthropic describes the same chunk failure.** Its Contextual Retrieval write-up notes that chunks often lack context. Its example is a chunk saying revenue grew 3% without naming the company or the period.
  - **Fixes:** prepend context to each chunk before embedding, combine embeddings with BM25 keyword matching, and add re-ranking. Together these cut the top-20-chunk retrieval failure rate by 67% in their tests (5.7% → 1.9%).
  - **Supports the whole-file option:** for knowledge bases under about 200,000 tokens (~500 pages), the post suggests putting the whole knowledge base in the prompt, with prompt caching, and skipping RAG.
  - Source: [Anthropic: Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- **Karpathy's LLM Wiki gist agrees search should wait for scale.** It says an index file is enough at small scale, and proper search becomes worthwhile as the wiki grows. That supports adding semantic search only when scale causes pain. Source: [Karpathy, llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Embeddings are high-dimensional.** The video's "three-dimensional space" is a simplification. OpenAI's text-embedding-3-small defaults to 1536 dimensions and text-embedding-3-large to 3072. Source: [OpenAI embeddings guide](https://developers.openai.com/api/docs/guides/embeddings)
- **Claude Code's own memory follows this principle.** A short `MEMORY.md` index is always loaded (first 200 lines or 25KB), while detailed topic files are read only when needed. The always-needed part is kept small and the rest is fetched on demand. Source: [Claude Code docs: memory](https://code.claude.com/docs/en/memory)
- **Hybrid retrieval appears in the wild.** [[GBrain]] combines vector search, keyword search and reciprocal-rank fusion with a typed knowledge graph, rather than betting on one method. Source: [garrytan/gbrain on GitHub](https://github.com/garrytan/gbrain)
- **Knowing More's model lineup is out of date, but the cost axis still holds.** The video calls Sonnet 4.6 and Opus 4.7 current ([02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s), [03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)).
  - **Current lineup.** Anthropic's models overview now lists Claude Fable 5.1 at $10 input and $50 output per million tokens, the slowest. Then Opus 5 at $5 / $25, Sonnet 5 at $2 / $10, and Haiku 4.5 at $1 / $5, the fastest.
  - **Context windows.** The first three have 1M-token windows; Haiku 4.5 has 200K.
  - **Discounts.** Batch requests cost half. Prompt-cache reads cost 10% of the base input price, or 2.5% on Fable 5.1.
  - **What a bulk read costs.** At base input prices, reading 200,000 tokens of raw material costs about $0.20 on Haiku 4.5 and $1.00 on Opus 5 (arithmetic from the listed prices).
  - **Where to start.** The overview suggests starting with Opus 5 for most workloads, unlike the video's "start with Sonnet" ([03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s)).

  Source: [Claude Platform docs — Models overview](https://platform.claude.com/docs/en/models/overview)
- **Chase's "index at every level" is his own extension.** Karpathy's LLM Wiki gist describes three layers: immutable raw sources, a wiki the LLM writes and maintains, and a schema file such as CLAUDE.md. For navigation, the gist relies on a single `index.md` catalogue that the LLM updates on every ingest, plus an append-only `log.md`. Chase calls the layout raw/wiki/outputs ([20:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1203s)–[20:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1213s)) and puts an index in every folder ([19:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1168s)). Both are reasonable, but the second is his refinement, not the gist's. Source: [Karpathy, llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Related

- **Concepts:** [[Second Brain Levels]], [[Keyword vs Semantic vs Graph Retrieval]], [[Semantic Search]], [[Knowledge Graphs]], [[Context vs Connections]], [[CLAUDE.md as a Router]], [[LLM Wiki]]
- **Techniques:** [[Grill Me Interview Skill]], [[Add Semantic Search to One Folder]], [[Tiered Lookup Routing]], [[Second Brain Pain-Point Audit]]
- **More concepts:** [[Choosing a Claude Model]] · [[Context Window Management]] · [[Agentic OS]] · [[Loop Engineering]] · [[Subagents and Agent Teams]]
- **More techniques:** [[Route Tasks to the Right Claude Model]] · [[Build a Context Map for a Connected Tool]] · [[Keep CLAUDE.md Lean]]
- **Newer techniques:** [[Add a Journal and Personal CRM to a Second Brain]] · [[Bootstrap an LLM Wiki from the Karpathy Gist]]
- **People:** [[Nate Herk]] · [[Chase AI]] · [[Jay E]] · [[Simon Pittman]] · [[Andrej Karpathy]] · [[Matt Wolfe]]
- **Newer sources:** [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] · [[Chase AI - The Three-Step Claude Code Agentic OS]]
- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Knowing More - Every Claude Model Explained]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Simon Pittman - Set Up Claude Cowork]] · [[Home]]
