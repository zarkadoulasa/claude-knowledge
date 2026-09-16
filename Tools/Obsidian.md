---
type: tool
category: markdown note app / vault viewer
website: https://obsidian.md/
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tags: [topic/second-brain, topic/retrieval, topic/knowledge-graph, topic/agentic-os, topic/skills]
---

# Obsidian

## What it is

In [[Nate Herk]]'s framing, Obsidian is a **viewer, not the brain itself**. It takes a folder of markdown files and shows them visually; nothing more [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s). The second brain itself is just markdown files, organised so that both he and his agents understand them [01:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=70s). In his setup [[Claude Code]] writes those files, and Obsidian only renders them [09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s).

Other sources take it further. [[Chase AI - The Agentic OS Setup for Claude Code]] also calls Obsidian optional [13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s). But he uses it as the vault for his agentic OS's memory, and as the home of a Claude-built plugin command center whose buttons run skills [25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s). That makes it a control surface, not just a viewer. [[Jay E - The ARMS Framework for a Claude Agentic OS]] never mentions Obsidian. He built his own visual second brain viewer for a similar job and ranks it as his top memory level [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s).

## How sources use it

- [[Nate Herk - Every Level of a Claude Second Brain]]:
  - **Level 2:** the Obsidian view of his YouTube-transcript [[LLM Wiki]] [08:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=523s).
  - **Optional:** install it only if you like visuals; he rarely opens it [10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s), [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s).
  - **Level 3:** a demo comparing keyword search with a "smart lookup" (semantic search) in his YouTube-transcript second brain [14:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=875s).
  - **Level 4:** the contrast between his Obsidian wiki and a [[LightRAG]] graph built from roughly the same data [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s).
- [[Chase AI - The Agentic OS Setup for Claude Code]]:
  - **The vault:** the folder Claude Code is opened in, holding the memory and state of his agentic OS [14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s), [15:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=917s).
  - **A command-center plugin:** buttons inside Obsidian that run skills and automations through headless Claude Code [25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s), [27:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1634s).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]:
  - **A related idea, not Obsidian:** a visual second brain viewer he built for his workspace [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s), [20:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1243s).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (April, two months before his June video): create a vault under Manage Vaults [06:30](https://www.youtube.com/watch?v=sboNwYmH3AY&t=390s) and open that folder where you run Claude Code [06:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=404s). Capture and stance are in the two tables below.
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]: the Codex project is the vault folder itself [10:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=628s). Capture and stance are in the tables below.
- [[Chase AI - The Three-Step Claude Code Agentic OS]]: an interface over markdown; see "Later stances" below.

### Level 2: Obsidian view of his YouTube-transcript wiki

- He keeps separate wikis for different material: all YouTube transcripts in one, all meeting transcripts in another [08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s).
- He opens the transcript wiki in Obsidian [08:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=523s). It has concept pages such as agentic workflows, AI coding market and context window [08:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=529s).
  - Those pages link out to related tools, concepts and videos [08:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=535s).
  - There are also sections for sources, platforms and context-management techniques [08:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=539s).
- **He didn't build any of the structure by hand.** Claude Code created it each time he told it to ingest a transcript into the wiki [09:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=544s). See [[Ingest Sources into an LLM Wiki]].
- **The vault is just a folder inside his main project.** The transcript wiki lives in Herk2 [09:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=557s), under a folder captioned "Other Worlds" (*unclear in captions*), then YouTube OS, then the transcript wiki [09:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=562s).
  - Opened in the file tree, it shows the same folders that appeared in Obsidian [09:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=568s): concepts, comparisons, sources and techniques [09:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=572s).
  - Obsidian just visualises those markdown files [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s). All it adds is a visual view of the same content [09:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=584s).

### It's optional: install it only if the visual layer helps you

- **The visual view is attention-grabbing.** He thinks many people get infatuated with that visual view [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s). He admits that's why he opened the video with the graph visuals: they hook viewers [09:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=597s).
- **What actually matters** is whether your system can fetch the information and hand it back to you [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s).
- **If you're a visual person,** go ahead and install Obsidian; he says setup is very easy [10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s), [10:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=606s).
- **If the visual layer doesn't help you, skip it** [10:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=609s). He rarely opens Obsidian himself [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s). He knows the files live in the project and that his second brain and OS can find them [10:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=616s).

### Level 3: keyword search vs smart lookup

- He lists Obsidian as one route to semantic search, alongside Pinecone and Supabase [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s).
- **The demo.** In his YouTube-transcript second brain he compares the regular search with a "smart lookup" panel [14:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=875s):
  - He searches for "feedback" in the regular search [14:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=885s). It only shows places where that exact word appears [14:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=889s).
  - He runs the same query in smart lookup [14:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=896s). It returns notes whose *meaning* relates to feedback [14:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=898s), such as live test results and a Claude Code skills note about evaluations [15:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=902s).
- He stresses how different keyword matching and semantic similarity matching are [15:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=907s).

| | Regular search | Smart lookup |
|---|---|---|
| Matches on | The literal word you typed [14:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=889s) | Meaning, i.e. similar content [14:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=898s) |
| His summary of the logic | X equals X [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) | X is similar to X, Y and Z [15:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=911s) |
| Result for "feedback" | Only places where that exact word appears [14:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=889s) | Live test results, a Claude Code skills/evaluations note [15:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=902s) |
| Level question it matches | Level 1: find it by an exact word or name [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s) | Level 3: search with different words than you wrote ([[Semantic Search]]) [03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s) |

### Levels 2 and 4: Obsidian links are not typed relationships

- **Links aren't quite a knowledge graph.** He asks whether a wiki full of links counts as one, and answers: not exactly [12:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=763s). The links don't say *how* two things relate; a relation like "endorsed by" is missing [12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s). They behave like "see also" backlinks [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s). The effect can be similar, but it isn't the same thing [12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s).
- **Why a wiki is heavier to read.** An agent working from the wiki reads every file it needs in full [24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s). Even if it only wants the ElevenLabs detail on an AI-video-production page, it reads the whole page [24:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1446s). A graph can be lighter in that respect [24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s).
- **Same data, different depth.** His [[LightRAG]] graph holds roughly the same data as his Obsidian view [24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s). Obsidian doesn't show the same level of relationships between entities [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s).
- **Why the wiki is still enough for him.** He puts a lot of care into ingesting with context, so the wiki already gives him enough sense of how things relate [23:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1432s).

| | Obsidian view of an LLM Wiki | Relationship graph ([[LightRAG]]) |
|---|---|---|
| What a link means | "See also" backlink with no stated relation [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s) | Named relation, e.g. "collaborates with" [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s) |
| How the agent reads | Whole pages [24:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1442s) | Can be more lightweight [24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s) |
| His daily use | The wiki, yes: Herk2 sits almost entirely at Level 2 [12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s). Obsidian itself, hardly ever [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s) | Played with knowledge graphs a lot, but doesn't use them day to day [19:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1185s) |

### Chase AI: Obsidian as the vault, then as a command center

[[Chase AI - The Agentic OS Setup for Claude Code]] uses Obsidian in two ways: for Level 2 (memory and state) and Level 3 (interface) of his [[Agentic OS]].

**The vault (Level 2)**
- **Optional, but easy.** People favour Obsidian because it's free and simple, but anything it does could also be done in an ordinary database [13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s)–[13:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=835s). A coherent file structure matters more than either [14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s).
- **Setup.** Download it and designate a folder as the vault. At install you choose between creating a new vault and opening an existing folder as one [14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s)–[14:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=888s).
- **"Connecting" Claude Code** just means opening a terminal in the vault folder and starting Claude Code there [15:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=917s)–[15:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=942s).
- **Graph as map.** He shows the Obsidian graph of his vault as a picture of how files connect, and calls Obsidian a filing cabinet for everything [16:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1008s)–[17:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1028s).
- **What goes inside.** Karpathy-style raw/, wiki/ and outputs/ folders, an index.md at every level, and a vault CLAUDE.md with structure and navigation sections [17:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1056s)–[22:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1331s). See [[LLM Wiki]] and [[Ingest Sources into an LLM Wiki]].

**The command center (Level 3)**
- **Two interface options.** A custom visual wrapper can be a web app or live inside Obsidian [23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s)–[23:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1418s).
  - His web dashboard runs Claude Code under the hood, connected to the Obsidian vault [23:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1421s). A finished inbox brief opens as a full write-up that can also be opened in Obsidian [25:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1533s)–[25:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1537s).
  - For teammates or clients, button results land in their own Obsidian or the team's [25:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1500s).
- **The Obsidian version.** It is a command center inside Obsidian itself [25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s). It shows token burn [25:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1551s), has buttons that run skills or automations [25:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1553s), and has tabs for audience metrics and research [25:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1557s).
  - He says the value is a one-stop view of things that are hard to see from the terminal, not the visuals [26:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1567s)–[26:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1578s).
- **How he suggests building it.** Obsidian works through plugins, so the command center is an app built as a plugin. Ask Claude Code to turn the web app you already built into an Obsidian plugin, then install and run it [26:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1613s)–[27:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1632s). The web app itself starts from a screenshot of a design you like, your list of skills, the vault connection and the metrics you want [26:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1594s)–[26:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1611s).
- **What a button does.** Clicking a skill button, e.g. a morning brief, runs a *headless* Claude Code session. It's like typing the /morning-brief command in a terminal, but nothing pops up; it uses `claude -p` [27:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1634s)–[27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s).
- **Harder to hand over.** A web version can be shared as a GitHub repo or a zip. The Obsidian command center needs more hands-on setup, which you'd do for each person [29:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1744s)–[29:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1776s).
- **Not shown.** No plugin code, manifest or settings appear in the video. For a buildable version, see [[Build an Agentic OS Dashboard]].

### Related idea: Jay E's visual second brain viewer

[[Jay E - The ARMS Framework for a Claude Agentic OS]] never mentions Obsidian. His "visual second brain" is an app he built himself [11:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=670s), [20:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1243s), but it plays a similar role to Obsidian's graph and search.

- **What it does.** It shows how files and folders in his workspace connect and searches faster [13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s)–[13:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=838s). CLAUDE.md sits at the centre, linked out to his department router files [12:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=743s)–[12:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=752s).
- **How he uses it.** It opens from the centre of his dashboard, and he uses it to show skills and workspace files when explaining his systems [02:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=122s)–[02:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=138s). It finds and previews a skill immediately, where a file explorer is slow [14:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=857s)–[14:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=872s).
- **An audit side effect.** Pointing it at his workspace showed it held about 60,000 files [11:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=670s)–[11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s).
- **Where he ranks it.** It is the top rung of his memory ladder [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s), though he puts his visual dashboard as a whole at only about 20–30% of an agentic OS's value [03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s). See [[Second Brain Levels]] for how that clashes with Nate's view.

### Three stances on the visual layer

| | Nate Herk | Chase AI | Jay E |
|---|---|---|---|
| What the visual tool is | Obsidian, only a viewer over markdown [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s) | Obsidian as the vault, plus a plugin command center with run buttons [25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s) | A self-built second brain viewer, not Obsidian [20:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1243s) |
| Is it needed? | Optional; he rarely opens it [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s) | Optional; a database works too [13:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=829s). The UI is the "cherry on top" [30:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1826s) | His highest memory level [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s) |
| What it's for | Visual people; the hook, not the value [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s) | One-stop visibility, and letting non-technical people run skills by button [24:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1472s) | Explaining systems, seeing connections, quick find and preview [14:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=845s) |

### Web Clipper: capturing into raw/

Nate (April) and Matt both save clips straight into the folder the agent ingests from. See [[Ingest Sources into an LLM Wiki]].

| | [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] | [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] |
|---|---|---|
| Why clip | A copy-pasted page can come through garbled [08:47](https://www.youtube.com/watch?v=sboNwYmH3AY&t=527s) | On YouTube it pulls in the full transcript [09:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=556s) |
| Folder | Change the location from the default "Clippings" to raw [10:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=626s) | Set the note location to raw [13:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=822s). The vault name must match Obsidian's exactly [13:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=782s) |
| Properties | Only a title and source; Claude fills in the rest [09:21](https://www.youtube.com/watch?v=sboNwYmH3AY&t=561s) | Source title, URL, clip date (not publish date) and a web-clip tag [13:23](https://www.youtube.com/watch?v=yke4fLQUsh4&t=803s). No channel name, so the agent adds it while processing [14:57](https://www.youtube.com/watch?v=yke4fLQUsh4&t=897s) |
| Next | Ask Claude Code to ingest the clip [09:27](https://www.youtube.com/watch?v=sboNwYmH3AY&t=567s) | Process raw/ on request, later via an hourly job [29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s) |

### Later stances: working in Obsidian or only viewing it

| | Nate Herk, April | Matt Wolfe, May | Chase AI, May |
|---|---|---|---|
| Role | An optional front end [06:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=363s). He watches the graph fill in during an ingest [11:06](https://www.youtube.com/watch?v=sboNwYmH3AY&t=666s) | His working "visibility layer": he checks results there throughout the build and opens it to tweak the rules [31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s). He likes watching the graph view grow more interconnected [16:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1004s) and shows a far denser vault as what weeks of use bring [32:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1936s) | A nice interface over markdown. Installing it does little by itself [08:06](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=486s) |
| Needed? | No; the markdown files are enough [16:27](https://www.youtube.com/watch?v=sboNwYmH3AY&t=987s) | Assumed. He credits Karpathy with using Obsidian as the front end [08:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=492s) | Recommended as a middle ground short of full RAG [10:57](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=657s) |
| What matters more | Letting Claude Code build the structure; he linked nothing by hand [01:07](https://www.youtube.com/watch?v=sboNwYmH3AY&t=67s) | The instruction file, because it's all just prompts [32:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1922s) | The file structure you set up inside it [08:09](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=489s), one both Claude and you can navigate [12:13](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=733s) |

## Notes

- **Build takeaway.** Design the vault for the agent, not for the graph picture. What matters is whether the system can fetch the information for you [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s); if your agent can't find things, he says you probably lack the right routing or folder architecture [02:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=137s). Obsidian is an optional window onto it. See [[Design for Retrieval]] and [[CLAUDE.md as a Router]]. Counterpoint: Matt enjoys watching the graph get denser [16:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1004s) and shows a dense vault as what weeks of use get you [32:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1936s), while Nate in June treats the graph visuals mainly as a hook [09:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=597s).
- **Obsidian's graph is not a Level 4 graph.** However dense it looks, it's drawn from the same see-also style links he describes [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s), and he says Obsidian doesn't show the entity relationships his LightRAG graph does [25:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1500s). If you need typed relationship chains, that's a separate graph layer ([[Build a Knowledge Graph Layer]]).
- **He doesn't name the smart lookup tool** or show how it was set up, and he doesn't say outright that this screen is Obsidian. He does name Obsidian as one place to do semantic search [13:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=788s). See Beyond the source for the likely candidates.
- **Build takeaway from Chase's command center.** Every button starts an unattended Claude Code run. His inbox-brief button goes through his inbox and writes drafts with nobody watching [24:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1451s)–[24:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1462s). He doesn't talk about permissions. Before wiring up a button, decide which tools that run is allowed to use; the relevant flags are under Beyond the source.
- **"Viewer" vs "control surface" is a real split between sources.** Nate's advice: skip Obsidian unless visuals help you. Chase keeps it optional too, but makes it an interactive front end. Jay E replaces it with a custom viewer. The "Three stances" table above sets these side by side, and [[Second Brain Levels]] covers the clash over whether a visual layer counts as a memory level.
- **Stances drift, so date them.** Nate goes from watching the graph fill in (April) to rarely opening Obsidian (June). Chase goes from recommending it (May) to calling it optional (June). Matt, recording in May, keeps it as his working visibility layer. Timestamps are in the tables above.

## Beyond the source

*Not said in the videos; verified at the links given.*

- **Local, plain-text files.** Obsidian is a free app that keeps notes on your device as plain-text Markdown files. That's why the same folder can serve as Claude Code's project and as an Obsidian vault at once. Source: https://obsidian.md/
- **What Graph view shows.** Graph view is a core plugin: each note is a node, each internal link is a line, and a node grows with the number of notes that reference it. It has a global graph (the whole vault) and a local graph (notes connected to the active note, with adjustable depth). Because lines are untyped internal links, the graph can't show the named relations he describes at Level 4. Source: https://obsidian.md/help/plugins/graph
- **Core Search is keyword-based.** Each word of the query is matched independently within each file. It supports quoted exact phrases, `OR` and `-` exclusion, operators like `file:`, `path:`, `tag:`, `line:` and `section:`, and JavaScript-flavoured regular expressions. The help page documents no semantic mode. If that screen is Obsidian, this would be the regular-search side of his demo. Source: https://obsidian.md/help/plugins/search
- **What probably powers "smart lookup".** The video never names it. Two likely candidates come from the same developer's Smart Plugins family (GitHub: brianpetro). **Smart Lookup** is a community plugin for semantic search: you ask in natural language and it finds notes by meaning when exact words fail. **Smart Connections**, the flagship plugin, surfaces notes semantically related to what you're working on, and it also has a Lookup view for ad hoc semantic searches across the vault. It ships with a local embedding model and needs no API key. Smart Lookup's docs say to use Obsidian search for an exact word, title, tag, syntax or regex, and Lookup for finding notes by meaning, which matches his "feedback" demo. It's likely, but not confirmed, that his panel is one of these. Sources: https://smartconnections.app/smart-lookup/search/ · https://community.obsidian.md/plugins/smart-lookup · https://github.com/brianpetro/obsidian-smart-connections
- **Privacy angle.** Smart Connections describes itself as private and offline by default, with a local embedding model. Smart Lookup's docs say a cloud provider only receives note content you explicitly send. So semantic search inside Obsidian needn't send your vault anywhere. That's relevant to his aside that data he processes through Claude goes to Anthropic [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s). Sources: https://github.com/brianpetro/obsidian-smart-connections · https://smartconnections.app/smart-lookup/search/
- **This vault uses Obsidian the same way.** It follows the LLM Wiki pattern: plain markdown files plus an index and routing rules. Obsidian is only the viewer, and Claude reads and writes the files directly. Source: this vault's `CLAUDE.md` (see [[Home]] and [[LLM Wiki]]).
- **Opening an existing folder as a vault.** Obsidian's vault switcher offers "Create new vault" and "Open folder as vault". The second is the step Chase describes: it points Obsidian at a folder Claude Code already works in, without moving anything. Source: https://obsidian.md/help/manage-vaults
- **Web Clipper basics.** A free, open-source browser extension; Obsidian says it collects no data or usage metrics. Templates can be picked by URL pattern or schema.org type and filled from page variables such as `{{published}}` or `{{selector:…}}`. The variables help page lists no transcript variable. Sources: https://obsidian.md/help/web-clipper · https://obsidian.md/help/web-clipper/templates · https://obsidian.md/help/web-clipper/variables
- **YouTube transcript capture is fragile** (forum reports, not the docs). YouTube's February 2026 redesign broke selector-based transcript templates until users patched them. Later posts say transcripts now arrive through Reader via `{{content}}` (May 2026) or a `{{transcript}}` variable (July 2026). If a clip lacks a transcript, check the clipper version and template before blaming the ingest. https://forum.obsidian.md/t/web-clipper-youtube-video-transcript-for-yts-ui-feb-2026-update/111550
- **How a plugin like Chase's command center is built.** Obsidian's developer docs start from the official sample plugin template, cloned into the vault's `.obsidian/plugins` folder. A plugin consists of `manifest.json` (id, name and other metadata) and a compiled `main.js`, built from `main.ts` with `npm install` and `npm run dev`. You switch it on under Settings → Community plugins. Source: https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin
- **Desktop only.** Every plugin manifest must set `isDesktopOnly`. The docs say it should be true when a plugin relies on NodeJS or Electron APIs. A plugin that launches a local `claude -p` process would need Node's process APIs (this note's inference; the docs don't discuss this case), so it would run in desktop Obsidian only, not on mobile. Source: https://docs.obsidian.md/Reference/Manifest
- **What a headless button run can and can't do.** Source: https://code.claude.com/docs/en/headless
  - A `claude -p` run loads the same context as an interactive session, including CLAUDE.md, skills, hooks and MCP servers from the working directory. The exception is `--bare`, which skips all of that and doesn't use your subscription login (it needs an API key).
  - User-invoked skills work: put `/skill-name` in the prompt string and it expands before the run.
  - `-p` starts in Manual permission mode on every plan. For a button to use tools without prompts, pass `--allowedTools` or a `--permission-mode` such as `acceptEdits`, `dontAsk` or `auto`. With no permission host, anything that would prompt is denied. `--permission-prompts none` (v2.1.259+) also tells Claude not to retry those actions.
  - `--output-format json` returns the result text plus session ID and metadata, which a plugin can render as the write-up.

## Related

- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] · [[Chase AI - The Three-Step Claude Code Agentic OS]]
- **More:** [[Add a Journal and Personal CRM to a Second Brain]] · [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Matt Wolfe]]
- **Concepts:** [[LLM Wiki]] · [[Semantic Search]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[Knowledge Graphs]] · [[Design for Retrieval]] · [[Second Brain Levels]] · [[Agentic OS]]
- **Techniques:** [[Ingest Sources into an LLM Wiki]] · [[Add Semantic Search to One Folder]] · [[Build a Knowledge Graph Layer]] · [[Build an Agentic OS Dashboard]]
- **Tools:** [[Claude Code]] · [[Qdrant]] · [[LightRAG]]
- **People:** [[Nate Herk]] · [[Chase AI]] · [[Jay E]]
- [[Home]]
