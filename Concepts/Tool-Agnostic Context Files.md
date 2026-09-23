---
type: concept
aliases: ["Portable Second Brain", "AGENTS.md and CLAUDE.md", "Portable Skills"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[LYKN - Website Overview]]"]
tags: [topic/portability, topic/second-brain, topic/claude-code, topic/agents, topic/skills, topic/context, topic/managed-agents]
---

# Tool-Agnostic Context Files

## In one sentence

A second brain is just markdown files and folders, so any agent harness can use it. You only have to bridge the few pieces that belong to one tool: the name of the instruction file, and where that tool keeps its own memory.

Newer sources take the idea two steps further. Skills can live as one copy that several agents read, and the whole workspace can be synced to an agent running on another computer. One source also asks whether most people need the instruction file at all (see Where sources disagree).

## How it works

### Why a file-based brain is portable

- The video talks mostly about Claude Code, but the approach works with any AI model. He uses the same second brain with Codex ([01:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=107s)) and with Hermes Agent ([01:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=108s)), because it's only files and folders that any harness can read ([01:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=99s), [01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).
- His main project, Herk2, is essentially a set of folders and markdown files arranged so that both he and his agents understand them ([01:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=68s), [01:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=70s)).
- **Why it matters:** your data is your moat and your IP ([00:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=47s)). Part of the goal is organizing it so you can use it with many different AI models ([00:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=51s)).
- **The viewer is optional too.** Obsidian only visualizes the markdown files ([09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)). Install it if a visual view helps you ([10:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=603s)), but you don't need it ([10:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=609s)). He rarely opens it, because his system can find everything in the files directly ([10:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=614s)).

### Which pieces are tool-specific

He points out that some parts are particular to Claude Code: the CLAUDE.md file name, and a memory file that Claude Code keeps updated on its own ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s), [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s)).

| Piece | In Claude Code | In another harness | Bridge shown in the sources |
|---|---|---|---|
| Instruction / router file | CLAUDE.md, loaded each session ([04:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=271s)) | Codex starts from AGENTS.md ([04:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=265s)) | Copy it ([11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s)), or import it with @ ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)) |
| Memory | Auto memory, written by Claude Code itself ([10:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=650s)) | Uses the same file only if its router points there | Tell the other agent where the memory file is ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)) |
| Always-on syncing (Level 5) | Possible, but you set up the cron jobs yourself ([25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s)) | He is trying GBrain with Hermes Agent instead ([25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s), [25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s)) | See [[Always-On Brain OS]] |
| Skills | In the Unlazy install, Claude Code finds the skill through its `.claude` folder, which holds only a shortcut ([10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s)) | Codex reads the `.agents` folder ([09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s)) | One real copy in `.agents`, linked into `.claude` ([10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)). See Bridge 4 |
| Account-level skills in Claude's apps | Skills are added once in Claude settings ([01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s)) | Claude Design uses the same set. AI LABS says the skills also work in Claude Code and Codex ([00:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=56s), [01:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=63s)) | No separate install for Claude Design; other agents install separately (see Beyond the source) |
| Files on another computer | The Claude Code workspace lives on your machine | A Hermes agent on its own cloud computer can't reach those skills and that context ([17:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1023s)) | Sync the workspace with Syncthing ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)), or run Claude Code or Codex on a VPS so there is nothing to sync ([18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)) |

The first three rows come from [[Nate Herk - Every Level of a Claude Second Brain]]. The skills row comes from [[AI LABS - The Unlazy Skill for Lazy Agents]], the account-level row from [[AI LABS - Claude Design Skills for Beautiful Sites]], and the last row from [[Jay E - The ARMS Framework for a Claude Agentic OS]].

### Bridge 1: duplicate the router (his Herk2 setup)

- To move the brain to Codex, start with the router: copy CLAUDE.md to a file named AGENTS.md ([11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s), [11:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=679s), [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s)).
- Herk2 has both files side by side ([11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s)). Their contents are essentially identical, so Codex reads one and Claude Code reads the other ([11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s), [11:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=690s)).

### Bridge 2: keep one source and import it (his Level 4 example)

- The Level 4 example project also has an AGENTS.md identical to its CLAUDE.md ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s)).
- He points out a cleaner option. Inside CLAUDE.md, reference AGENTS.md with an @ reference and delete the duplicated body, because the reference injects AGENTS.md's contents ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s), [23:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1381s), [23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s)).
- **A second source picks the same bridge.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] comes at it from coding projects. His complaint is that other agents keep their project memory in AGENTS.md and Claude is the only one that doesn't ([03:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=201s)–[03:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=206s)). Since CLAUDE.md can import other files, he imports AGENTS.md there, which saves him from keeping a symlink ([03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)–[03:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=221s)). He would still prefer Claude to support AGENTS.md directly ([03:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=222s)).

### Bridge 3: route other agents to the memory

- Claude Code maintains auto memory by itself ([11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s)). Make sure the memory file exists ([11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s)) and tell Codex to look there for memories ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)). In his words, it comes down to "all about the routing" ([11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)).
- For where Claude Code actually stores auto memory, see Beyond the source below and [[Claude Code Auto Memory]].

### Bridge 4: one copy of each skill, linked into every agent

All from [[AI LABS - The Unlazy Skill for Lazy Agents]]:

- **The claim.** Unlazy is presented as working with Claude Code, Codex and other popular agents ([01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s)).
- **The install.** Copy the command from the repo's install section and run it in a terminal inside your project ([09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s)–[09:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=557s)).
  - The installer first asks which agent you use. Codex needs nothing extra, because the skill goes into the `.agents` folder Codex already reads ([09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s)–[09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s)).
  - Claude Code has to be picked from the menu, and you can tick several agents in one pass ([09:34](https://www.youtube.com/watch?v=c47uqR7XB_c&t=574s)–[09:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=578s)).
  - Then you choose the scope: this project only, or everything you build. They chose project scope so they could test on one app first ([09:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=580s)–[09:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=589s)).
- **The result.** The project gains a `.agents` folder and a `.claude` folder, but they aren't two copies. The skill lives in `.agents`, and `.claude` holds a shortcut so Claude Code can use the skill without a duplicate ([10:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=601s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- **Why it counts as a bridge** (my reading, not their framing). It's Bridge 2 applied to skills: one real file, plus a pointer wherever each tool looks. It also changes how edits travel. AI LABS later edited the skill itself to run subagents in parallel ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)), and with one copy that edit reaches every agent linked to it.

### Account-level skills across Claude's apps

All from [[AI LABS - Claude Design Skills for Beautiful Sites]]:

- You don't add skills inside Claude Design. The skills in your Claude setup are the ones Claude Design can use, so you add a skill once from Claude settings ([00:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=52s)–[01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s)).
- They demo in Claude Design but say the same skills would work in Claude Code, Codex or any other agent, with the same result ([01:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=63s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s)). They use Emil Kowalski's design skills themselves in both Claude Code and Claude Design ([01:17](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=77s)–[01:22](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=82s)).
- **Caution.** "Same result" is stated, not compared on screen. Each surface also installs skills differently (see Beyond the source). [[Nate Herk - Build Skills Instead of Agents]] disputes it: only the process carries over, because models read skills differently and no skill makes a weaker model match a stronger one ([06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)).

### Beyond one machine: syncing skills and memory

All from [[Jay E - The ARMS Framework for a Claude Agentic OS]]:

- **His setup.** Hermes runs on its own computer in the cloud, and most of his scheduled tasks live there ([16:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1008s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)).
- **The step he says most people miss.** An agent on its own computer can't reach the skills and context you've built up in Claude Code ([17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s)).
- **His fix.** Syncthing, free open-source software that syncs files between computers ([17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)–[17:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1043s)). Point it at the Claude Code workspace, install it on the Hermes computer too, and share the files you choose, including skills and memory files ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)).
- **The next stage he describes.** He knows some users who install Claude Code on a VPS, so the files and context already live where the routines run. You can use Codex there too, and you no longer need a sync tool ([17:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1070s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)).
- **How this fits** (vault framing). Bridges 1–4 decide what each agent reads. Syncing decides whether the files are on that agent's computer at all. Full build: [[Sync a Workspace to an Always-On Cloud Agent]].

### Related portability points in the video

- **Privacy.** Running all your data through Claude models means it goes to Anthropic, so it isn't private ([21:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1290s)). He is comfortable sending his own business data ([21:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1297s)). If you aren't, for example with client data, consider open-source models ([21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)). Claude Code may then not be the right home for a brain that holds everything ([21:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1309s)). He plans videos on local and open-source AI ([22:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1331s)).
- **Level 5 fits other harnesses.** GBrain would pair well with Hermes Agent ([25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s)). In Claude Code you'd have to handle the cron jobs yourself, which is why he doesn't run GBrain there today ([25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s), [25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)). Wanting to keep several Hermes agents in sync is one sign you need Level 5 ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)).
- **Team brains.** For a shared brain, the storage choice (Google Drive, Notion, GitHub, or what the captions call "cloud plugins", likely Claude plugins) matters less than adoption and change management ([29:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1794s), [30:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1819s)). Get your own brain working first ([30:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1826s), [30:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1834s)).

## When to use it — and when not to

- **Use it** whenever you run, or may later run, more than one harness on the same knowledge. He works in Herk2 from Claude Code, Codex and Hermes Agent ([01:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=107s), [01:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=108s)).
- **Bridge 1 (copy)** is what Herk2 uses, with the two files kept essentially identical ([11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s), [11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s)). **Bridge 2 (import)** lets you delete the duplicated body, so the instructions live in one place ([23:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1381s)).
- **Watch the tool-specific parts.** The places he flags as needing extra work are all features of one tool rather than plain files: auto memory ([11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s)) and always-on cron jobs ([25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s)).
- **Skip the bridges** if only one harness ever reads the brain. His general rule is not to build extra structure without a real pain point ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s), [04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)), and he presents the AGENTS.md copy as the step for when you want to move the brain over to Codex ([11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s)). The plain files-and-folders structure is worth having either way.
- **Use Bridge 4 (one skill copy, linked into each agent)** whenever more than one agent should run the same skill. The Unlazy installer builds this layout for you when you tick several agents ([09:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=578s)), and you avoid duplicate skill folders ([10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- **Use account-level skills** for work inside Claude's own apps. AI LABS adds a skill once in settings and uses it in Claude Design ([01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s)).
- **Sync files to another computer** only when an agent really runs somewhere else, like Jay E's always-on Hermes ([16:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1008s), [17:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1023s)). If everything can run on one server, his VPS route needs no sync at all ([18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)).
- **Keep whatever you bridge small.** Ras Mic's case against large context files (next section) applies to every copy or import you make.

## Where sources disagree

### Do most people need AGENTS.md or CLAUDE.md at all?

| Source | Position | Where |
|---|---|---|
| [[Nate Herk - Every Level of a Claude Second Brain]] | A brain starts from its router file (CLAUDE.md, or AGENTS.md for Codex), and porting that file is the main job | [04:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=265s), [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s), [22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s) |
| [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] | Wants Claude to read AGENTS.md the way other agents do. Until then he imports it into CLAUDE.md | [03:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=206s)–[03:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=222s) |
| [[Ras Mic - How AI Agents and Claude Skills Work]] | About 95% of people don't need either file. Keep one only for proprietary company information, or a method of yours the model must see in every conversation | [02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s), [03:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=182s)–[03:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=196s), [18:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1128s) |

**Ras Mic's reasons:**

- **The model already knows a lot.** In a codebase the agent can read the code, so telling Claude Code the project uses React adds nothing ([02:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=147s)–[02:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=153s)). Stack lists such as React plus Convex are unnecessary because the code itself is now context ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s)–[19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
- **The file costs tokens all the time.** It comes along on every exchange with the agent ([03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s)). His example is a 1,000-line file of about 7,000 tokens, spent on every run ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)–[04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s)).
- **Procedures belong in skills.** A report format or code-structure rules should be a skill, because only a skill's name and description sit in context until it's needed ([03:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=212s)–[03:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=219s), [05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s)–[05:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=350s)).
  - In his demo a whole skill measured 944 tokens, and its name plus description 53 ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s), [30:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1857s)).
  - He counted with OpenAI's tokenizer ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)), so the numbers are approximate for Claude.
- **His closing verdict.** He calls these files a farce you don't need ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).

**How the positions fit together** (vault synthesis, not any source's words):

- **Portability only matters for files you keep.** On Ras Mic's rule the file you bridge is short, and Bridge 2 still costs just one import line.
- **His exception covers what the agent can't discover.** A router saying where your non-code knowledge lives fits that exception better than a stack list in a codebase. His critique hits coding projects hardest.
- **Moving procedures into skills makes Bridge 4 matter more, not less.** But he doesn't install other people's skills, partly because a download is an easy way to attack someone ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)). That cuts against one-command, multi-agent installs like Unlazy's. See [[Build vs Install Third-Party Skills]].
- **The Claude Code docs back his direction** on file size and skills. What they say about how the file loads is under Beyond the source.

### Plain files, or a platform memory store?

- [[Nate Herk - Every Level of a Claude Second Brain]]: the brain is only files and folders, so any harness can read it ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).
- [[Anthropic - What Is Claude Managed Agents]]: the demo agent reads from and writes to a memory store held by the platform ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)). It checks last week's findings before a run and stores what changed afterwards ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s)–[02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)).
- **How they fit** (vault synthesis): store memories are path-addressed text, so they can join a file-based brain, but only through an export step (see Beyond the source).
- [[LYKN - Website Overview]]: a third option, a hosted personal vault that other vendors' tools connect to over MCP, OAuth or REST. ChatGPT, Claude and Cursor then share one context, and each connection can be revoked ([terms](https://lykn.io/terms)). It's portable across tools but held on someone else's platform, and it offers data export. See [[LYKN]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: a file-based brain is tool-agnostic by design ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)). He shows both the copy approach ([11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s)) and the import approach ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)). He sees portability as a routing problem: every agent just needs to be told where things are, memory included ([11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: Claude is the odd one out for not reading AGENTS.md ([03:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=206s)). Importing it into CLAUDE.md beats keeping a symlink ([03:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=219s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: takes the one-source idea to skills. The real copy lives in `.agents`, which Codex reads, and `.claude` holds only a shortcut for Claude Code ([09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s), [10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]: skills added in Claude settings are the ones Claude Design uses ([00:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=56s)). They're said to work the same in Claude Code and Codex ([01:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=63s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s)), though the video doesn't test that.
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: portability across computers. A remote Hermes agent needs Claude Code's skills and context ([17:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1023s)). He syncs them with Syncthing ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)), or sidesteps the problem by running Claude Code on a VPS ([17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the skeptic. Most people don't need AGENTS.md or CLAUDE.md ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)), and skills are what matter ([32:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1976s)).

## Beyond the source

*Not from the video. Checked 2026-09-15.*

- **Claude Code reads CLAUDE.md, not AGENTS.md.** For a repo that already has AGENTS.md, the official advice is a CLAUDE.md that starts with `@AGENTS.md`, with any Claude-only instructions below it. Claude loads the imported file first, then the rest. If you have no Claude-only content, a symlink also works: `ln -s AGENTS.md CLAUDE.md`. On Windows, symlinks need Administrator rights or Developer Mode, so use the import there. Confirm it worked with `/context`, which lists loaded memory files. <https://code.claude.com/docs/en/memory#agents-md>
- **How the import behaves:** `@` paths resolve relative to the importing file, nest up to four hops, and load at session start. <https://code.claude.com/docs/en/memory#import-additional-files>
- **Claude Code's `/import` command** (v2.1.213 or later) appends a *one-time copy* of files like AGENTS.md into CLAUDE.md. Like Bridge 1, that copy can drift out of date. <https://code.claude.com/docs/en/memory#agents-md>
- **Codex reads AGENTS.md.**
  - In the Codex home directory (`~/.codex`, or `CODEX_HOME`), it reads `AGENTS.override.md` if present, otherwise `AGENTS.md`.
  - It then walks from the project root down to the current directory. In each folder it checks `AGENTS.override.md`, then `AGENTS.md`, then any fallback names listed in `project_doc_fallback_filenames` in `~/.codex/config.toml`.
  - The files are concatenated from the root down, so files nearer the working directory come later and win.
  - The combined size is capped by `project_doc_max_bytes`, 32 KiB by default.
  - The Codex AGENTS.md guide doesn't describe any `@file` import syntax. **Keep the real content in AGENTS.md itself** and let CLAUDE.md import it, not the other way round.

  <https://developers.openai.com/codex/guides/agents-md> (now redirects to <https://learn.chatgpt.com/docs/agent-configuration/agents-md>)
- **Hermes Agent loads only one project context file *type* per session, and the first match wins:** `.hermes.md`/`HERMES.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. (Inside a git repo it can merge a chain of AGENTS.md files from the root down, and it picks up context files in subdirectories as it navigates.) A global `SOUL.md` from `HERMES_HOME` is loaded separately. With both AGENTS.md and CLAUDE.md in a project, Hermes reads AGENTS.md, which is another reason to make AGENTS.md the real file. The context-files docs don't mention `@` import expansion. <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>
- **Each harness keeps its own memory.**
  - Hermes Agent writes `MEMORY.md` and `USER.md` itself, through its memory tool, into `~/.hermes/memories/`. <https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what>
  - Claude Code's auto memory lives in `~/.claude/projects/<project>/memory/`, outside the repo, and stays on that machine. <https://code.claude.com/docs/en/memory#storage-location>

  Neither agent reads the other's memory automatically, and cloning or syncing the vault carries neither. This is why Bridge 3 matters.
- **Claude Managed Agents memory stores live on the platform, not in your files.** A store is a workspace-scoped set of text documents, mounted as a directory inside the session sandbox. Each memory has a path and can be listed, read, edited or created (seeded) through the API or the Claude Console, which is how you export to or import from a file-based brain. Past versions may be deleted after 30 days unless exported. <https://platform.claude.com/docs/en/managed-agents/memory>
- **A layout that combines the above.** This is my synthesis from the docs, not a layout shown in the video. The import step is the one he demonstrates at Level 4. The folder paths match the vault's shared starter layout (base tree in [[Build a Level 1 Second Brain]], memory and wikis from [[Ingest Sources into an LLM Wiki]]).

  ```text
  my-brain/
  ├── AGENTS.md          # canonical router: role, priorities, "where things live"
  ├── CLAUDE.md          # line 1: @AGENTS.md, then Claude-only notes (or a symlink)
  ├── decisions.md       # dated decision log, as in the Level 1 build
  ├── memory/
  │   └── MEMORY.md      # in-repo memory index any agent can read; routed from AGENTS.md
  ├── context/
  ├── projects/
  └── wikis/
  ```

  Sources: <https://code.claude.com/docs/en/memory#agents-md>, <https://developers.openai.com/codex/guides/agents-md>, <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>

### Skills, sync and context cost (added with the newer sources)

*Not from the videos. Checked 2026-09-15.*

- **Skills share one open format.** An Agent Skill is a folder with a `SKILL.md`. Anthropic developed the format and released it as an open standard. Its client list includes Claude Code, Codex, Hermes Agent, OpenClaw, Cursor and Gemini CLI. Agents load only each skill's name and description at startup, and read the rest when a task matches. <https://agentskills.io/>
- **But each tool looks in its own folder.** Per-tool detail and a link script are in [[Port a Claude Code Brain to Other Agents]].
  - **Claude Code** reads `.claude/skills/<name>/SKILL.md` in the project and `~/.claude/skills/` for personal skills. Its docs list no `.agents/skills` location. A skill entry may be a symlink, and Claude Code loads the target once even if several locations point to it. <https://code.claude.com/docs/en/skills>
  - **Codex** scans `.agents/skills` from the working directory up to the repo root, plus `$HOME/.agents/skills`, and follows symlinked skill folders. <https://learn.chatgpt.com/docs/build-skills>
  - **Hermes Agent** uses `~/.hermes/skills/`. You can add shared folders such as `~/.agents/skills` under `skills.external_dirs`, and a local skill wins over an external one with the same name. <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>

  Together this explains the Unlazy layout: the real copy sits where Codex looks, with a link where Claude Code looks.
- **The installer behind Bridge 4.** Unlazy's README gives `npx skills add Leonxlnx/unlazy` as the install command. <https://github.com/Leonxlnx/unlazy>
  - That CLI offers symlinks to one canonical copy (recommended) or separate copies with `--copy`. <https://github.com/vercel-labs/skills>
  - An open bug (#1355) reports project-scope installs for Claude Code that put the skill in `.agents/skills/` without creating the `.claude/skills/` link, so check the link. <https://github.com/vercel-labs/skills/issues/1355>
  - The Windows symlink caveat above presumably applies to skill links too (my inference).
- **Account-level skills.** On claude.ai you add skills under Customize > Skills, with code execution and file creation turned on. <https://support.claude.com/en/articles/12512180-use-skills-in-claude>
  - Claude Code loads account-enabled skills automatically in Cowork and cloud sessions.
  - Local sessions need a one-time download: `CLAUDE_CODE_SYNC_SKILLS=1 claude -p "..."`, which puts the skills in `~/.claude/skills/synced/`. <https://code.claude.com/docs/en/skills>
  - Claude Design's getting-started article doesn't mention skills, so the claim that settings skills show up there rests on the AI LABS video. <https://support.claude.com/en/articles/14604416-get-started-with-claude-design>
- **Syncthing** is free, open-source, continuous file sync between your own devices, with no central server holding the data. <https://syncthing.net/> Syncing a workspace doesn't carry Claude Code's auto memory, which is machine-local and stored outside the project (see the memory bullet above). <https://code.claude.com/docs/en/memory#storage-location>
- **What the Claude Code docs say about context-file cost** (relevant to Ras Mic's argument):
  - CLAUDE.md files load into the context window at the start of every session and use tokens alongside the conversation.
  - The docs suggest under 200 lines per file, and say multi-step procedures belong in skills or path-scoped rules.
  - Imports don't reduce context, because imported files load at launch too. So Bridge 2 organizes a file but doesn't shrink it.

  <https://code.claude.com/docs/en/memory>

## Related

- [[CLAUDE.md as a Router]]
- [[Keep CLAUDE.md Lean]]
- [[Claude Code Auto Memory]]
- [[Port a Claude Code Brain to Other Agents]], the build steps for this concept
- [[Sync a Workspace to an Always-On Cloud Agent]], the cross-machine build
- [[Agent Skills]] and [[Build vs Install Third-Party Skills]]
- [[Always-On Brain OS]] and [[Second Brain Levels]]
- [[Agentic OS]] and [[Routines and Scheduled Tasks]]
- [[Context vs Connections]]
- [[LYKN]], a commercial cross-tool memory layer
- [[Context Window Management]]
- [[Claude Code]], [[OpenAI Codex]], [[Hermes Agent]], [[GBrain]], [[Obsidian]]
- [[Unlazy]], [[Claude Design]], [[Syncthing]]
- Source: [[Nate Herk - Every Level of a Claude Second Brain]]
- Sources: [[The Coding Sloth - 1000 Hours of Claude Code Lessons]], [[AI LABS - The Unlazy Skill for Lazy Agents]], [[AI LABS - Claude Design Skills for Beautiful Sites]], [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[Ras Mic - How AI Agents and Claude Skills Work]], [[Anthropic - What Is Claude Managed Agents]]
- [[Claude Managed Agents]]
- People: [[Nate Herk]], [[The Coding Sloth]], [[AI LABS]], [[Jay E]], [[Ras Mic]]
- [[Home]]
