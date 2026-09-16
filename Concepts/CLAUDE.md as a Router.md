---
type: concept
aliases: ["Router File", "AGENTS.md router", "Department router files", "Cowork global instructions"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Nate Herk - Build Skills Instead of Agents]]"]
tags: [topic/second-brain, topic/claude-code, topic/retrieval, topic/context, topic/agentic-os, topic/cowork]
---

# CLAUDE.md as a Router

## In one sentence

The CLAUDE.md file loads into every session anyway, so use it as more than a role brief: make it a routing table that tells the agent which folder holds which kind of knowledge. Then the agent goes straight to the right place instead of asking you, guessing, or searching everything.

## How it works

### What the file is

- Every second brain starts at Level 1 with a CLAUDE.md, or an AGENTS.md if you work in Codex, plus ordinary folders and files ([04:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=260s), [04:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=265s)).
- It loads when a session opens in that project and works roughly like the system prompt for that project ([04:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=271s)). *(An analogy; Beyond the source covers how it actually loads.)*
- The key move is to treat it as a **router** ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)). It still covers the basics, like your role and what matters ([04:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=281s)), but it also holds **routing rules** ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)). For example, personal information lives in one folder ([04:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=285s)) and first-quarter priorities live in another ([04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s)).

### Why routing is needed

- **The symptom:** you ask Claude to do something and it asks you for background, even though you know the files are in the project ([04:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=291s)). That usually means you never told it where to look ([05:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=300s)).
- **Why it happens:** Claude won't search your whole codebase on its own ([05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)). You wouldn't want it to either, because that wastes time and tokens ([05:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=307s)). If it doesn't know something exists somewhere, it probably won't find it ([05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)).
- The intro makes the same point. Having data isn't the hard part. The hard part is organizing it so the AI can recall it properly, instead of hallucinating or spending time and tokens reading everything ([00:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=51s), [00:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=57s)).
- **His test for a second brain:** can your agent find the thing again, and could you ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s))? If not, your routing or folder architecture is missing ([02:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=137s)).
- **Design backwards from the question.** How you'll access and recall data should decide how you file it ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s), [02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)). His analogy: you wouldn't make a square basketball when you know the hoop is round ([02:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=166s)). See [[Design for Retrieval]].
- **Repair the route, not just the answer.** When an agent says it can't find a file he knows exists, [[Nate Herk - Build Skills Instead of Agents]] doesn't just hand over the path and move on ([05:13](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=313s)). He has it backtrack and show where it searched and why it missed ([05:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=317s)). Then it updates the routing or the skill so the next run starts in the right place ([05:22](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=322s)).

  *Vault starter content (not from the video):*

  ```text
  You couldn't find <file>; it's at <path>. Before carrying on:
  1. List what you checked, in order, and which rule or index sent you there.
  2. Say why that route missed this file.
  3. Propose the smallest change to CLAUDE.md, an index or the skill that would
     have sent you here first. Show the diff and wait for my OK.
  ```

### The payoff

- With the router set up properly, you stop re-explaining things. The agent knows where to look and why ([05:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=314s), [05:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=318s)).

### His Level 1 example project

| Piece | What it does in the demo |
|---|---|
| `CLAUDE.md` | Its header explains that it loads automatically whenever Claude Code opens in the folder, and that it's the single file describing you, your working style and where your things are ([05:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=339s), [05:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=343s)). At Level 1, this file plus a few folders is the whole second brain ([05:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=347s)). |
| "Where things live" section | A very short list of routes ([05:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=353s)) |
| Context folder | Background about you and how you work that is always true. The router says to read it first ([05:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=355s)). It holds an about-me file you can expand ([06:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=364s)), a stack file, and a second file captioned "conversations" (possibly "conventions"; *unclear in captions*) ([06:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=366s)). |
| Decisions | A decision log. CLAUDE.md can tell Claude to append each big decision with its date ([06:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=368s), [06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)). |
| Projects | One markdown file or subfolder per ongoing project or client ([06:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=379s), [06:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=382s)). You can also organize by date, e.g. a May folder and a June folder ([06:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=389s), [06:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=392s)). |

Approximate shape (exact file names weren't readable in the captions):

```text
level-1-project/
├── CLAUDE.md          # who you are, how you work, where things live
├── context/           # always-true background; read first
│   ├── about-me.md
│   ├── stack.md
│   └── conversations.md   # name unclear in captions
├── decisions          # dated decision log Claude appends to
└── projects/          # one file or folder per project/client
```

### How the router grows at higher levels

- **Level 2.** Same shape, with more routes. The router still points to context, projects and decisions, and now also to a wiki, references and a memory file ([10:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=621s), [10:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=629s), [10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). At this level the change is mostly a few more routing rules inside CLAUDE.md ([10:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=637s)). See [[Claude Code Auto Memory]].
- **The wiki index works as a second-tier router.** Wikis have indexes ([11:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=713s)). A question about agentic workflows starts at that index entry ([11:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=716s)). From there the agent drills down ([12:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=721s)), for example to his framework page (captioned "WATC", most likely his WAT framework: Workflows, Agents, Tools) ([12:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=727s)), then to the page on CLAUDE.md as a system prompt ([12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s)). It follows a trail and reads each page in full ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)). He adds that these links behave like "see also" backlinks rather than knowledge-graph relationships that say how things are related ([12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s)), and that wikis start to degrade once they grow large ([11:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=708s)). See [[LLM Wiki]].
- **Level 4.** The "where things live" routing to plain folders and markdown is unchanged; he calls it "boring is beautiful" ([23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s), [23:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1393s), [23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s)). The Level 4 example also shows CLAUDE.md pulling in AGENTS.md with an @ reference instead of duplicating it ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)). See [[Tool-Agnostic Context Files]].
- **Different folders can use different retrieval styles.** One business unit, such as YouTube transcripts, can become a vector database while context, projects and decisions stay markdown ([17:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1056s), [17:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1064s)). A second brain doesn't need a single style throughout ([17:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1071s)). The router decides which style each question reaches.
- **Routing can set a lookup order.** Suppose he asks what he and a colleague discussed last week about quarterly project number seven. (He calls quarterly projects something captioned "OTAs"; the exact term is *unclear in captions*.) The brain checks the quarterly-projects file first ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s)), then the wiki and meeting transcripts ([28:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1701s)), and only then pulls live data from ClickUp ([28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)). He still counts that as a second brain, because it knows where to look and in what order ([28:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1713s), [28:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1717s)). His check: does the system understand where your data lives and where to look ([28:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1724s))? See [[Tiered Lookup Routing]].
- **Routing to a vault outside the project.** In [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] (April 2026) the wiki is a separate vault. Its own CLAUDE.md explains how the project works and how to search and update it ([04:43](https://www.youtube.com/watch?v=sboNwYmH3AY&t=283s)), so another project can be pointed at it ([13:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=805s)).
  - **The route.** His executive-assistant project, Herk2, has a wiki-path section. For facts about him or the business it doesn't already have, it goes to the Herk Brain vault and reads the hot cache, the index and the domain sub-index, or searches ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s), [14:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=843s)).
  - **A negative route.** Don't read the wiki unless the task needs it, followed by a list of tasks that don't ([14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s)).
  - **The result.** Replacing in-project context files with this lookup cut the tokens the project pulled in, though he gives no figures ([14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s)).
- **Trigger-word modes.** [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] routes by how a chat starts, not only by topic. His router is an AGENTS.md for Codex ([21:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1309s)).
  - **The modes.** A plain question runs the wiki query operation. A chat opening with "journal" becomes a journal entry. Saying the information is for the CRM updates the CRM ([23:46](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1426s), [23:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1435s)).
  - **What each mode names.** The journal and CRM modes each get their own folder and index ([22:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1325s), [23:26](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1406s)).
  - **Other tools.** He says Claude Code or Cowork also works ([32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s)). In Claude Code that needs the AGENTS.md bridge under Beyond the source.

### The human drill-down test

To judge a structure, pretend you can't ask the AI and have to find a file yourself in Herk2 ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s), [07:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=433s)). For him it's easy because he knows his base folders and how they drill down ([07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s)).

1. Goal: the HTML slide deck from his video ranking Claude Code features ([07:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=441s)).
2. It's a project, so open projects ([07:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=447s)).
3. Inside projects, open the YouTube videos project ([07:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=450s)).
4. Open the dated folder for the May 30 "top 50 Claude Code features" video ([07:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=454s)).
5. Open the tier-list deck ([07:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=459s)).

The structure makes sense and has routing rules, so his agent can find the deck as easily as he can ([07:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=463s)).

Not every source accepts this test. [[Jay E - The ARMS Framework for a Claude Agentic OS]] argues that human-friendly names and file-explorer navigation matter less once agents work through router files ([12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s)). See "Where sources disagree" below.

## When to use it — and when not to

**Use it:**
- Always. Level 1 is where every second brain starts ([04:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=260s)).
- Look at Level 1 if you keep re-explaining your setup and need to find things by exact words or file names ([28:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1739s)). Level 1 asks one question: can you find the file by an exact word or name ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s))?

**Its limits:**
- If the file grows too big it gets messy, and its instructions start to feel ignored ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)). [[Nate Herk - 32 Tricks to Level Up Claude Code]] puts a number on it: he keeps his to 150–200 lines at most and routes the rest out ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), [07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)). The audit is [[Keep CLAUDE.md Lean]].
- Not everyone thinks you need one: Ras Mic and the Coding Sloth dissent. See "Where sources disagree".
- Depending on how you route, retrieval is mostly exact-word matching ([05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)).
- If you have 30 or more notes and keep forgetting what's in them, look at Level 2, the wiki ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)).
- If the project keeps missing notes you know exist and routing isn't fixing it, consider semantic search, which doesn't need exact words ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)). See [[Semantic Search]] and [[Keyword vs Semantic vs Graph Retrieval]].

**Don't over-engineer the structure:**
- No proven standard layout exists yet, beyond common pieces like a context folder and CLAUDE.md ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s), [06:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=408s)).
- Don't treat his layout, or any creator's, as the one right way ([06:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=415s)). What matters is whether the routing is in place and makes sense to both you and your AI ([07:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=423s), [07:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=426s)).
- Pick the simplest level that meets your needs ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)). Without real pain there's no reason to build more ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s), [04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)). See [[Second Brain Levels]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: the router is the foundation of every level, and each higher level adds routes rather than replacing it ([10:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=637s), [23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s)). He runs almost all of Herk2 at Level 2, a router plus wikis ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)), because he hasn't felt enough pain to move up. He says "level two" at [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s), but in context he means Level 3.
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: a lean, routed cheat sheet that you keep updating.
  - **Bootstrap.** His first tip is to run `/init` on any existing project. Claude Code scans the folders and writes a CLAUDE.md mapping the architecture, conventions and key files, so you stop re-explaining the project ([00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s), [00:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=23s)). For a new project, have Claude help draft it from the goal, tech stack, rules and key folders ([00:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=42s)).
  - **Keep it current.** After a discovery or a new skill, have Claude log the new patterns, gotchas and conventions ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)). When a challenged output comes back better, tell Claude to update the skill or CLAUDE.md ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - **Cap it.** He calls the file basically the system prompt, loaded into every conversation and eating context ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s), [07:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=420s)). So he keeps his to 150–200 lines at most and trims past that ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).
  - **Route out.** Link to separate files for style guides, business context and reference docs ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s), [07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s)). The always-loaded file doesn't need a project's exact status, only where to find it ([07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s)).
  - `/clear` isn't starting from scratch, because CLAUDE.md and your files are still there ([02:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=164s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the strongest dissent in the vault.
  - **Most people don't need one.** On [[Greg Isenberg]]'s podcast he says 95% of people don't need an AGENTS.md or CLAUDE.md ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). The models are already good ([02:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=129s)), and Claude Code can read the codebase instead of being told it uses React ([02:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=147s), [02:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=152s)).
  - **His exception:** proprietary information, or a method specific to you, that has to be in every conversation ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). More generally, things the agent won't know on its own ([32:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1971s)).
  - **Cost.** The file sits in context on every back-and-forth ([03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s)). A 1,000-line file of about 7,000 tokens is paid on every run and should probably be a skill ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s), [04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s)). Skills put only their name and description in context ([03:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=217s)). In his demo a 944-token skill costs 53 tokens until used ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s), [30:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1857s)). He counted with OpenAI's tokenizer ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)).
  - **Don't list your stack.** Lines like React plus Convex are unnecessary because the code itself is now the context ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). Don't state defaults like using a dollar sign, but do state a non-default currency ([32:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1956s), [32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)).
  - He ends by calling these files a farce you don't need ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).
  - He describes his own agent setup in [[OpenClaw]] terms rather than Claude Code ([24:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1446s), [26:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1594s)), and his CLAUDE.md examples are software projects.
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: a quirk rulebook, helpful but not make-or-break.
  - **On `/init`.** It scans the codebase into CLAUDE.md, which he calls Claude's permanent memory for the project ([03:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=194s), [03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)). The vault separates that file from Claude-written [[Claude Code Auto Memory]]. He grades `/init` a C or D ([04:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=242s)), and a month later still calls it mid ([04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s)). An experimental version behind an environment flag interviews you and recommends skills and hooks, which he thinks has potential ([03:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=233s), [03:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=236s)).
  - **Why the file matters anyway.** He rates the file itself higher: after months you learn the models' habits, and CLAUDE.md is where you counter them ([04:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=253s), [04:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=258s)).
  - **What's in his:** a quick project description and current status ([04:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=267s)), a working-philosophy section he's testing ([04:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=275s)), a rule against ALL-CAPS user-facing text ([04:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=277s)), and the language to use for pull requests ([04:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=290s)).
  - **Keep it flexible.** He says you could survive without one, and skills can give similar or better results ([04:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=293s), [04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s)).
  - **AGENTS.md.** He's annoyed that Claude doesn't use AGENTS.md like other agents do. His workaround is to import it inside CLAUDE.md instead of symlinking ([03:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=201s), [03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)). See [[Tool-Agnostic Context Files]].
- [[Chase AI - The Agentic OS Setup for Claude Code]]: routing pushed down into every folder.
  - **The problem.** One folder with a huge number of files and no hierarchy makes Claude slow, and that costs more tokens ([16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s)). His mental model is building a map for Claude Code ([16:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1004s)).
  - **An index.md at every level.** He says the power of the Karpathy-style raw/wiki/outputs layout is that each level has an `index.md` saying what it contains ([19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s), [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)). Claude reads the vault index, goes to `wiki/`, reads that index, then the article ([19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s)). An index for a one-file folder is overkill, but it pays off with thousands of documents ([20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s), [20:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1245s)).
  - **Folder names don't matter much.** The map does, and yours will be unique to you ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s), [21:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1278s)).
  - **A vault CLAUDE.md on top.** It covers the vault's conventions: the structure (his folders include content, notes, runs, inbox, ops and projects) and a **navigation pattern** saying which path to follow to find something ([21:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1312s), [22:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1321s), [22:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1327s)).
  - Claude Code can suggest a structure for your vault ([21:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1294s)).
  - This goes deeper than this note's router plus wiki index, which has only two tiers. See [[LLM Wiki]].
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: routers as the memory upgrade for a workspace that has grown.
  - **Level 1 is just files.** His first memory level is a workspace full of files ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)). Trouble starts as files pile up. His folder turned out to hold about 60,000 files, which slows retrieval and drains plan usage ([11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s), [11:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=690s)).
  - **Level 2 is routers.** Once you see slowdowns, organise the workspace for the agent ([11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s), [11:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=700s)). The minimum is router files ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)). CLAUDE.md is the central router: it describes his departments so Claude works inside the right set of files ([12:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=745s), [12:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=750s)). Each department then has its own router, such as `content.md`, which is just a list of skills and reference files ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s)).
  - **Why routers work.** Agents parse files very quickly, so routers get them to the right place in the fewest steps ([13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)).
  - **Name for the agent.** Now that agents operate on the files, he says human-friendly names and file-explorer navigation matter less ([11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s), [12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s)).
  - His setup prompt appears only on screen ([13:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=814s)).
  - See [[Agentic OS]].
- [[Simon Pittman - Set Up Claude Cowork]]: the same idea in [[Claude Cowork]], as global instructions plus required reading.
  - **Global instructions.** He calls writing them the most important and most easily missed setup step ([08:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=492s)). He recommends a Cowork-specific set on the Cowork tab of Settings ([08:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=521s), [08:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=525s)). They're rules read at the start of every conversation, like a manual for a new assistant ([08:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=531s)). In effect they're a CLAUDE.md that can sit at system level or in any folder ([09:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=541s), [12:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=728s)).
  - **Drafting them.** His brief to Claude includes safety rules (never delete, send or publish without checking first) and an honesty rule to flag overcomplication ([10:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=617s), [10:25](https://www.youtube.com/watch?v=pl90LATQlHI&t=625s)). Claude writes a CLAUDE.md at the workspace root, and he pastes its contents into the settings box ([10:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=641s), [11:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=710s)).
  - **Required reading.** He adds an About Me folder with `about-me.md`, `writing-rules.md` and `memory.md` ([12:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=776s)). Claude updates the global instructions to read all three at every session start ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)), with the list moved to the top ([18:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=1127s)).
  - **Context map.** A `my-context-map.md` describing his Notion workspace is also referenced ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s)). With it, Claude found the right database immediately ([30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)).
  - **Projects.** Each project gets its own CLAUDE.md and memory file under `projects/` ([35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s)).
  - **Check it.** Start a new task and ask how Claude is meant to work with you ([19:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1175s)).
  - See [[Set Up Claude Cowork]] and [[Build a Context Map for a Connected Tool]].
- [[AI LABS - Types of Claude Loops Explained]]: CLAUDE.md as a place for behavioural safety rules, not routes. While a stateless loop works unattended toward pre-written tests ([03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)), they add one line telling the agent to save every working version of the app ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)), so it can roll back to the last working state instead of undoing changes from memory ([03:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=224s)). See [[Tests-First Goal Loop]] and [[Loop Engineering]]; Beyond the source covers why a commit or hook is sturdier.
- [[Chase AI - The Three-Step Claude Code Agentic OS]] (May 2026, before his four-level video): the one thing his Obsidian memory layer must have is a proper vault CLAUDE.md ([11:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=678s)).
  - **Job 1, purpose.** Tell Claude what the system is for, how to behave and what to care about on any prompt ([11:32](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=692s)). He says the file is effectively appended to every prompt ([11:45](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=705s)); Beyond the source gives the precise loading behaviour.
  - **Job 2, a memory map.** Spell out how memory is structured, so Claude sticks to it and finds things with fewer tokens ([11:55](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=715s), [12:03](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=723s)). His top level is archive, content, ops, personal, projects, raw and wiki ([12:17](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=737s)). The template appears only on screen ([11:25](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=685s)).
  - **For you too.** The map should make the vault navigable by you as well as Claude ([12:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=732s)).

### At a glance: what each source keeps in the always-loaded file

| Source | Always loaded | Routed out or loaded on demand |
|---|---|---|
| [[Nate Herk - Every Level of a Claude Second Brain]] | Role, how you work, "where things live" routes | context/, decisions, projects/, wikis |
| [[Nate Herk - 32 Tricks to Level Up Claude Code]] | Architecture, conventions, key files, gotchas; 150–200 lines at most | Style guides, business context, reference docs, project status |
| [[Ras Mic - How AI Agents and Claude Skills Work]] | Ideally nothing, or only proprietary facts needed every turn | Everything else as skills |
| [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] | Project description, status, coding style, habit-countering rules | Workflows as skills |
| [[Chase AI - The Agentic OS Setup for Claude Code]] | Vault structure and a navigation pattern | An index.md in every folder |
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | Departments | One router file per department listing its skills and references |
| [[Simon Pittman - Set Up Claude Cowork]] | Global instructions with tone and safety rules, plus required reading (about me, writing rules, memory, context map) | Per-project CLAUDE.md and memory; outputs/ |
| [[AI LABS - Types of Claude Loops Explained]] | A save-every-working-version rule for unattended runs | — |
| [[Chase AI - The Three-Step Claude Code Agentic OS]] | The vault's purpose and a map of how memory is structured | raw/, wiki/ and his other top-level folders |
| [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] | A wiki-path section: which external vault, what order, and when not to read it | hot.md, the vault index and domain sub-indexes |
| [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] (AGENTS.md) | Ingest and query operations plus journal and CRM modes keyed to how a chat starts | Wiki, journal and CRM indexes; log.md |

## Where sources disagree

### Do you need a CLAUDE.md at all?

- **Yes, it's the foundation:**
  - [[Nate Herk - Every Level of a Claude Second Brain]] starts every level with one ([04:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=260s)).
  - [[Nate Herk - 32 Tricks to Level Up Claude Code]] makes running `/init` his first tip ([00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s)).
  - [[Jay E - The ARMS Framework for a Claude Agentic OS]] calls router files the minimum ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)).
  - [[Simon Pittman - Set Up Claude Cowork]] calls the equivalent Cowork global instructions the most important step ([08:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=492s)).
- **Mostly no:**
  - [[Ras Mic - How AI Agents and Claude Skills Work]] says 95% of people don't need one ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)) and calls the files a farce ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] says it isn't make-or-break, and skills can match or beat it ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s)).
- **Reading them together** *(vault synthesis, not a claim from any source)*:
  - Ras Mic's own exception covers information specific to you that the model needs every turn ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). His examples are software projects, where the code is the context ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
  - A routing table for a knowledge vault tells the agent something it can't infer from any file, so it arguably falls inside that exception. A CLAUDE.md that restates a code repo's stack doesn't.
  - Both camps agree a bloated file costs you ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s) vs [04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)).

### Is `/init` worth running?

- **Yes, on every project:** [[Nate Herk - 32 Tricks to Level Up Claude Code]] says the generated cheat sheet means you stop re-explaining the project ([00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s), [00:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=35s)).
- **It's mid:** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] grades `/init` a C or D and a month later still calls it mid ([04:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=242s), [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s)). He sees more promise in the experimental version that interviews you ([03:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=233s)).
- *Vault reading:* `/init` analyses a codebase, so it suits code repos better than a personal second brain, whose router is usually simpler to write by hand. [[Build a Level 1 Second Brain]] makes the same point under Beyond the source. The interview flag is covered below.

### Should the always-loaded file hold the tech stack and project status?

- **Yes:**
  - [[Nate Herk - 32 Tricks to Level Up Claude Code]] has Claude draft a new CLAUDE.md from the goal, tech stack and rules ([00:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=42s)).
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] keeps current status in his ([04:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=267s)).
  - Nate Herk's Level 1 layout has a stack file, but it sits in the routed `context/` folder, not in CLAUDE.md itself ([06:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=366s)).
- **No:**
  - [[Ras Mic - How AI Agents and Claude Skills Work]] says stack lines are unnecessary because the code already shows them ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
  - On status, [[Nate Herk - 32 Tricks to Level Up Claude Code]] himself says the always-loaded file needs to know where a project's status lives, not what it is ([07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s)). That puts him against the Coding Sloth here.

### Load context at startup, or route to it on demand?

- **Route:**
  - [[Nate Herk - 32 Tricks to Level Up Claude Code]] points to separate files ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)).
  - [[Jay E - The ARMS Framework for a Claude Agentic OS]] uses department routers ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)).
  - [[Chase AI - The Agentic OS Setup for Claude Code]] puts an index.md at every level ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s)).
- **Read it every session:**
  - [[Simon Pittman - Set Up Claude Cowork]] makes about-me, writing-rules and memory required reading at the start of every session ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s), [18:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=1127s)).
  - His weekly-briefer scheduled task also reads the About Me files before doing any research ([42:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2538s)).
  - His context map joins them: he asks for global instructions that reference it so it is always looked at ([29:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1796s)).
- **Vault note (inference):** required reading that includes a memory file Claude appends to after each session ([15:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=935s)) grows into the bloat the other sources warn about. Keep required reading short; see [[Keep CLAUDE.md Lean]].

### Does the structure also need to make sense to a human?

- **Yes:**
  - [[Nate Herk - Every Level of a Claude Second Brain]] tests whether both the agent and you can find things again ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)). He finds a file by hand as a check ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s)).
  - [[Chase AI - The Three-Step Claude Code Agentic OS]], Chase's earlier video, is firm that Claude working it out isn't enough; you need a clear path too ([16:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1001s)).
- **Much less:** [[Jay E - The ARMS Framework for a Claude Agentic OS]] says that with agents operating on the files, you needn't pay as much attention to names or file-explorer navigability. Build router files for the agent instead ([12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s), [13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)).
- **In between:** [[Chase AI - The Agentic OS Setup for Claude Code]] calls folder names somewhat arbitrary, but says the map has to make sense and will be unique to you ([21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s), [21:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1278s)).

### Where should corrections go?

- **Into CLAUDE.md:**
  - [[Nate Herk - 32 Tricks to Level Up Claude Code]] logs new patterns and gotchas there ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)), or into the relevant skill ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] treats the file as the place to counter observed habits ([04:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=258s)).
- **Into the skill:** [[Ras Mic - How AI Agents and Claude Skills Work]] fixes the failure, then has the agent update the skill so it doesn't happen again ([22:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1329s)). He keeps AGENTS.md for proprietary facts only ([18:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1130s)).
- Beyond the source adds a third destination: auto memory.

### Will Claude go looking on its own?

- **No:** [[Nate Herk - Every Level of a Claude Second Brain]] says Claude won't search the whole codebase unprompted, so it needs routes ([05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)).
- **Too much:** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] says a vague prompt makes Claude read everything to work out what you want ([14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s)).
- **Same conclusion either way:** name the files and sources you want used ([14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)).

## Beyond the source

*Not from the videos. The first group below was checked 2026-09-15 against the Claude Code memory docs: <https://code.claude.com/docs/en/memory>. Items added with the September 2026 batch are marked with their own links.*

- **It isn't literally the system prompt.** The docs say CLAUDE.md content arrives as a user message after the system prompt. Claude reads it and tries to follow it, but compliance isn't guaranteed, especially with vague or conflicting instructions. The system-prompt comparison is a useful analogy, not the mechanism. Anything that must happen every time belongs in a hook. <https://code.claude.com/docs/en/memory#troubleshoot-memory-issues>
- **Where CLAUDE.md files load from:**
  - Managed policy (organization-wide)
  - User: `~/.claude/CLAUDE.md`
  - Project: `./CLAUDE.md` or `./.claude/CLAUDE.md`
  - Local, personal and gitignored: `./CLAUDE.local.md`

  Files in the working directory and every directory above it load at launch. They are concatenated rather than overriding each other, ordered from the filesystem root down. CLAUDE.md files in **subdirectories** load on demand when Claude reads files there, so a large folder can have its own nested router. <https://code.claude.com/docs/en/memory#how-claude-md-files-load>
- **Keep it small.** The docs suggest under 200 lines per CLAUDE.md, because longer files use more context and reduce adherence. For growing instructions they suggest path-scoped rules in `.claude/rules/` (with `paths:` frontmatter), and skills for multi-step procedures. This matches his warning that a big router gets messy and ignored. <https://code.claude.com/docs/en/memory#write-effective-instructions>
- **`@path` imports load everything at launch.** Writing `@path/to/file` expands that file into context at session start. Paths resolve relative to the importing file, imports can nest up to four hops, and the first external import in a project file (one that resolves outside the working directory) triggers a one-time approval dialog. Imports don't save context. **For a router, this means an `@` in front of a route loads the target every session.** To point at a folder or file without loading it, write the path with no `@`, or put it in backticks (import parsing skips code spans). <https://code.claude.com/docs/en/memory#import-additional-files>
- **What belongs in it.** The docs describe CLAUDE.md as the place for anything you'd otherwise re-explain. Add to it when Claude repeats a mistake or you type the same clarification again. Their specificity advice is essentially routing: write "API handlers live in `src/api/handlers/`" rather than "keep files organized." <https://code.claude.com/docs/en/memory#when-to-add-to-claude-md>
- **Check and bootstrap it:**
  - `/context` lists which memory files actually loaded.
  - `/init` generates a starter CLAUDE.md.
  - The project-root CLAUDE.md is re-read from disk after `/compact`.
  - Block-level HTML comments are stripped before injection, so notes for human maintainers cost no tokens.

  <https://code.claude.com/docs/en/memory#set-up-a-project-claude-md>, <https://code.claude.com/docs/en/memory#how-claude-md-files-load>, <https://code.claude.com/docs/en/memory#instructions-seem-lost-after-%2Fcompact>
- **Example routing block.** This is my illustration of the docs' "be specific about paths" advice applied to his Level 1 layout. It is not a file shown in the video. The paths have no `@`, so nothing loads until Claude opens a file:

  ```markdown
  ## Where things live
  - About me, how I work, my tools → `context/` (read first when you need background)
  - Decisions and why we made them → `decisions.md` (append new ones with the date)
  - Active projects and clients → `projects/<name>/`
  - Topic knowledge → `wikis/<name>/index.md`, then follow its links
  - If a route doesn't have it, say so and ask; don't search the whole tree
  ```

  <https://code.claude.com/docs/en/memory#write-effective-instructions>

**Added with the September 2026 batch.** Each item was checked 2026-09-15 at the linked page.

- **The interview-style `/init` the Coding Sloth mentions is documented.** With `CLAUDE_CODE_NEW_INIT=1`, `/init` asks which of CLAUDE.md files, skills and hooks to set up, explores the codebase with a subagent, asks follow-up questions, and shows a reviewable proposal before writing. If a CLAUDE.md already exists, `/init` suggests improvements instead of overwriting it. [Claude Code docs: set up a project CLAUDE.md](https://code.claude.com/docs/en/memory#set-up-a-project-claude-md)
- **AGENTS.md.** Claude Code reads CLAUDE.md, not AGENTS.md. The docs recommend a CLAUDE.md that imports `@AGENTS.md` (Claude-specific lines below it), or a symlink if you have nothing to add; the import is the Coding Sloth's workaround. With the new-init flag set, `/init` also reads AGENTS.md, and `/import` (v2.1.213 or later) appends a one-time copy of another agent's instruction files. [Claude Code docs: AGENTS.md](https://code.claude.com/docs/en/memory#agents-md)
- **What to keep and what to move.** Keep facts Claude needs every session (build commands, conventions, project layout, "always do X" rules). Move multi-step procedures, or anything that matters for one part of the codebase, into a skill or a path-scoped rule. The `/doctor` checkup (v2.1.206 or later) proposes trims: it cuts what Claude can derive from the codebase (directory layouts, dependency lists, architecture overviews) and keeps pitfalls, rationale and conventions that differ from tool defaults, which backs Ras Mic's point for code repos. *Our reading:* a knowledge vault's routes can't be derived from code, so this doesn't argue against a vault router. [Claude Code docs: when to add to CLAUDE.md](https://code.claude.com/docs/en/memory#when-to-add-to-claude-md), [troubleshoot memory issues](https://code.claude.com/docs/en/memory#troubleshoot-memory-issues)
- **"Added at every turn," precisely.** Ras Mic's wording overstates the mechanism, but his cost point holds. CLAUDE.md loads once at session start and stays in context; Claude Code sends the whole conversation, that file included, with every request, and prompt caching lowers the cost of re-reading it. The costs guide notes that workflow-specific CLAUDE.md instructions cost tokens even during unrelated work, and recommends moving them into skills. [Claude Code docs: move instructions from CLAUDE.md to skills](https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills), [why usage climbs in a long session](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)
- **Skill metadata cost.** Before a skill is invoked only its description sits in context (`description` plus `when_to_use` is cut off at 1,536 characters); once invoked, its body stays in the conversation. Ras Mic's figures came from OpenAI's tokenizer. For Claude, use `/context` or Anthropic's free, rate-limited count-tokens endpoint with the model you run: Opus 4.7 and later, and the Fable models, count roughly 30% more tokens for the same text than earlier models. [Claude Code docs: skills](https://code.claude.com/docs/en/skills), [Claude API docs: token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- **Cowork's equivalents.** The Help Center puts global instructions under Settings > Cowork > Edit, applying to every Cowork session. A selected local folder can carry folder instructions, which Claude may update itself. In cloud sessions Cowork shares memory with chat, which Simon doesn't mention. Cowork needs a paid plan (Pro, Max, Team or Enterprise). *Our observation:* instructions that live only in the settings box aren't a file Claude Code or Codex can read in the folder, so keep a file copy as the source of truth. See [[Tool-Agnostic Context Files]]. [Claude Help Center: get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- **Safety lines in CLAUDE.md are requests, not guarantees.** The docs use settings such as `permissions.deny`, or a PreToolUse hook, for enforcement and keep CLAUDE.md for behavioural guidance. Checkpoints capture edits from Claude's file-editing tools before each prompt, but don't track bash-command changes, usually don't restore subagent edits, and don't replace version control. So for the AI LABS rule, a git commit after each passing test run (a hook can make it) is the reliable version. [Claude Code docs: deploy organization-wide CLAUDE.md](https://code.claude.com/docs/en/memory#deploy-organization-wide-claude-md), [CLAUDE.md vs auto memory](https://code.claude.com/docs/en/memory#claude-md-vs-auto-memory), [checkpointing limitations](https://code.claude.com/docs/en/checkpointing#limitations)
- **Auto memory in the corrections debate.** Auto memory saves corrections you give Claude as `feedback` notes, and skips anything CLAUDE.md already says. Asking Claude to remember something sends it to auto memory. Asking it to add something to CLAUDE.md edits the file. See [[Claude Code Auto Memory]]. [Claude Code docs: auto memory](https://code.claude.com/docs/en/memory#auto-memory)
- **Chase's "appended to every prompt" ([11:45](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=705s))** has the same precision problem as Ras Mic's wording above. CLAUDE.md loads at session start as a user message after the system prompt and stays in context; it isn't re-added per prompt. After `/compact` the project-root file is re-read from disk and re-injected. [Claude Code docs: write effective instructions](https://code.claude.com/docs/en/memory#write-effective-instructions), [instructions seem lost after /compact](https://code.claude.com/docs/en/memory#instructions-seem-lost-after-%2Fcompact)
- **Routing to a vault outside the working directory.** Claude Code loads CLAUDE.md from the working directory and its parents at launch, and from subdirectories on demand, so a separate vault like Nate's Herk Brain isn't loaded just because a route names it. `--add-dir` grants access to another directory, but its CLAUDE.md loads only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`. An external `@` import needs one-time approval and then loads every launch, which defeats a "don't read unless needed" rule. *Our reading:* use a plain path plus `--add-dir`. [Claude Code docs: load from additional directories](https://code.claude.com/docs/en/memory#load-from-additional-directories), [import additional files](https://code.claude.com/docs/en/memory#import-additional-files)

## Related

- [[Second Brain Levels]], where the router is Level 1 and the base of every level above it
- [[Design for Retrieval]]
- [[Tool-Agnostic Context Files]], on keeping a CLAUDE.md router and an AGENTS.md router in sync
- [[Claude Code Auto Memory]]
- [[LLM Wiki]] and [[Tiered Lookup Routing]]
- [[Keyword vs Semantic vs Graph Retrieval]]
- [[Build a Level 1 Second Brain]]
- [[Keep CLAUDE.md Lean]], the line-by-line audit that applies the size, routing and correction-loop advice above
- [[Agent Skills]] and [[Context Window Management]], on always-loaded versus on-demand context
- [[Agentic OS]], for department routers and folder indexes in a larger workspace
- [[Set Up Claude Cowork]] and [[Build a Context Map for a Connected Tool]], for the Cowork version
- [[Tests-First Goal Loop]] and [[Loop Engineering]], for CLAUDE.md safety lines in unattended runs
- [[Claude Code]], [[Claude Cowork]], [[OpenAI Codex]], [[OpenClaw]]
- [[Bootstrap an LLM Wiki from the Karpathy Gist]], [[Add a Journal and Personal CRM to a Second Brain]] and [[Audit Skill Descriptions and Triggers]], for external-vault routes, trigger-word modes and repairing missed routes
- People: [[Nate Herk]], [[Ras Mic]], [[Greg Isenberg]], [[The Coding Sloth]], [[Chase AI]], [[Jay E]], [[Simon Pittman]], [[AI LABS]], [[Matt Wolfe]]
- Newer sources: [[Chase AI - The Three-Step Claude Code Agentic OS]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] · [[Nate Herk - Build Skills Instead of Agents]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Simon Pittman - Set Up Claude Cowork]] · [[AI LABS - Types of Claude Loops Explained]]
- [[Home]]
