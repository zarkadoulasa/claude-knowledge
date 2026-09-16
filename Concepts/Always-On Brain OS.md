---
type: concept
aliases: ["Autonomous Second Brain", "Brain OS"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]"]
tags: [topic/second-brain, topic/memory, topic/automation, topic/agents, topic/teams, topic/scheduling, topic/agentic-os, topic/cowork, topic/managed-agents]
---

# Always-On Brain OS

## In one sentence

Level 5 of [[Second Brain Levels]] is a second brain that runs itself: it constantly syncs, refreshes memories and adds new material on its own, so you don't even have to think about it ([03:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=229s), [25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)).

## How it works

### What Level 5 is

- The Level 5 goal is to make the whole second brain so autonomous that it needs no thought from you ([03:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=229s)).
- Nate's name for this level is the "always-on Brain OS", and his example is [[GBrain]] ([25:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1525s)). It was built by [[Garry Tan]], whom he introduces as CEO of Y Combinator, and he says it pairs really well with gstack (also a Tan project; see Beyond the source) ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s), [25:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1534s)).
- **Ingredients.** GBrain is basically everything from the lower levels put together: wikis, routing, relationships and tools ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)). What it adds is an **always-on element** that constantly syncs, refreshes memories and pulls in new material ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)).
- **Not a different architecture.** Nate stresses that it closely resembles Levels 1–4. The difference is the auto-updating, autonomous, always-running feel ([26:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1562s)).

| Layer | Where it comes from | What Level 5 changes |
|---|---|---|
| Routing ([[CLAUDE.md as a Router]]) | Level 1 | Included in the bundle ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)) |
| Wikis ([[LLM Wiki]]) | Level 2 | Included ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)) |
| Relationships ([[Knowledge Graphs]]) | Level 4 | Included ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)) |
| Tools | Not tied to one level in the video | Included ([25:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1537s)) |
| Syncing and memory refresh | New at Level 5 | Runs continuously without you ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) |

### The harness matters: Hermes Agent vs Claude Code

- Nate thinks adding GBrain to an agent like [[Hermes Agent]] would work really well ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)).
- You can still do it in [[Claude Code]], but you'd have to create and manage the scheduled (cron) jobs yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)).
- That is why Nate doesn't run GBrain today. He has been experimenting with it on his Hermes agent ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).
- One background fact makes cross-agent setups workable: a second brain is just files and folders, and Nate already uses his with [[OpenAI Codex]] and Hermes Agent as well as Claude Code ([01:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=106s)). See [[Tool-Agnostic Context Files]] and [[Port a Claude Code Brain to Other Agents]].

### "Always-on" means different things in different sources

*Everything above comes from [[Nate Herk - Every Level of a Claude Second Brain]]. The sources below also talk about always-on or 24/7 setups, but they mean different things. Check which one a creator means before copying their setup.*

| Source | What stays on | What it gets you | Does memory refresh itself? *(this note's reading)* |
|---|---|---|---|
| [[Nate Herk - Every Level of a Claude Second Brain]] | A brain that keeps syncing and refreshing memories ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) | Knowledge that stays current without you | Yes. That's what Level 5 is |
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | A Hermes agent on its own cloud computer ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)) | Scheduled routines that run while your own computer is off | No. Skill and memory files are synced over from your machine ([17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)) |
| [[Simon Pittman - Set Up Claude Cowork]] | A desktop Mac that stays awake ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)–[41:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=2517s), [44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)–[44:25](https://www.youtube.com/watch?v=pl90LATQlHI&t=2665s)) | Cowork scheduled tasks, plus Dispatch requests sent from his phone | No. His `memory.md` is written during sessions because his instructions say so ([14:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=895s)–[15:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=916s)) |
| [[Nate Herk - 32 Tricks to Level Up Claude Code]] | Claude Code on a VPS ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)–[12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s)) | Sessions that keep running with your laptop closed | No |
| [[Anthropic - What Is Claude Managed Agents]] | Hosted agents with a memory store ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)–[02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s)) | Recurring runs that remember what they found last time | Partly. Each run writes its own findings, limited to its job |

Only Nate's Level 5 describes a brain that looks after itself. The others are about **cadence and availability**, the scheduling side covered in [[Routines and Scheduled Tasks]]. Level 5 would still need that infrastructure to run on.

### Jay E: routines on a dedicated Hermes cloud computer

- **Routines come after skills and memory.** Only once you've mastered those do you have the confidence to let the agent work without watching it. Routines are simply scheduled tasks ([14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s)–[14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s)). In his words, a routine is a prompt Claude sends itself at a set time ([15:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=913s)–[15:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=919s)).
- **Local routines stop when the computer is off.** That's why he keeps only a few in the desktop app ([15:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=956s)–[16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)).
- **Most of his schedules live on Hermes.** He wants routines that run with his computer off. He names OpenClaw, and Grok Bot as a newer but expensive option, and uses [[Hermes Agent]] himself ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)–[16:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=989s)). Hermes is always on because most people give it its own computer. His runs on a cloud machine, and most of his scheduled tasks are loaded there ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)).
- **The step most people miss.** A Hermes agent on another computer can't see the skills and context you built up with Claude Code. His fix is [[Syncthing]], a free open-source sync tool. You install it on both machines and point it at the Claude Code workspace, so the skills and memory files you choose are shared ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)). The build is [[Sync a Workspace to an Always-On Cloud Agent]].
- **His Level 3: one platform on a VPS.** This isn't his own setup; he describes users he knows who are trying it. Rent a VPS, install Claude Code on it and keep all files and context there. Routines then run around the clock on a single platform, with no sync tool ([17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s)–[18:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1101s)). He expected Anthropic and OpenAI to offer something like this, but not yet, because of file storage and security concerns ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)–[18:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1112s)). *Partly dated; see Beyond the source.*
- *This note's reading:* a Syncthing-shared workspace is one concrete way to meet Nate's Level 5 signal of several Hermes agents staying in sync with one brain ([29:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1765s)). Jay doesn't add automatic memory refresh on top of that.

### Simon Pittman: a desktop kept awake for Cowork

- **What a scheduled task draws on.** It runs on a timer, using the instructions, connectors and context you've set up ("contacts" in the captions) ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)–[41:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2503s)).
- **His hardware conclusion.** He says the computer must be on and online, which argues for a desktop you leave running ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)–[41:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=2517s)). The new-task form has an option to stop the computer sleeping, which he'd avoid on a laptop ([43:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2602s)–[43:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=2614s)).
- **Dispatch pushed him further.** In a post-filming update he shows Dispatch, which lets you control Claude on the desktop from your phone ([43:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=2629s)–[44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)). That's why he's committing to an always-on Mac in his studio plus a second Mac for travel ([44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)–[44:25](https://www.youtube.com/watch?v=pl90LATQlHI&t=2665s)). In the demo he asks from his phone what's on his calendar today; the desktop does the work and reports back ([45:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=2714s)–[45:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=2739s)).
- **The permissions that come with it.** One browser setting lets Claude act in Chrome without asking, even on sites you haven't approved ([44:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2670s)–[44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s)). Computer-use settings include a list of apps Claude may not use ([44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s)–[45:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=2702s)). See [[Permissions and Approval Gates]].
- **Terminology flag.** Simon's "always-on" means availability: a machine awake for scheduled tasks, phone requests and computer use. It isn't Nate's self-refreshing memory, and nothing in his setup curates the brain while he's away. *(This note's reading.)*

### Chase AI: scheduling a skill is the easy part

- **Automations come from skills.** [[Chase AI]] builds automations on top of skills. Once a skill is getting repeated over and over, turn it into an automation where that makes sense ([10:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=657s)–[11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)).
- **Two ways to schedule.** He calls this very easy. You can just ask Claude Code whether a skill can become an automation. Or, in the Claude desktop app's Routines page, name the routine, set its instructions to run the skill, and pick a schedule ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s)).
- **Loops come next.** The third layer is loop engineering: adding a self-improvement loop to an automation, tied to memory and state ([11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s)–[12:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=735s)). For that to work, skill and automation outputs have to be logged in one place where the loop can see past runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)). See [[Loop Engineering]].
- **How this compares.** *Where sources disagree* sets this against Nate's view that in Claude Code you'd manage the crons yourself.

### Anthropic's Managed Agents: memory stores hosted for you

- **What it is.** [[Anthropic - What Is Claude Managed Agents]] introduces a set of APIs for building and deploying agents at scale. Claude works inside an isolated container with filesystem access, bash and web search ([00:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=2s)–[00:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=29s)).
- **Memory across runs.** The pricing agent checks its memory store for last week's findings before it starts, and stores what changed when it finishes ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)–[02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s)). So the next Monday's report leads with changes instead of repeating static prices ([02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s)–[02:30](https://www.youtube.com/watch?v=NLWiIj47IdI&t=150s)).
- **Memory across incidents.** A coordinator agent checks past incidents in the store and spots a repeat DNS issue. The next similar alert starts from that context instead of from scratch ([03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)–[03:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=206s)).
- **What the video lists, and leaves out.** Memory is one of the building blocks it lists for a fully managed, stateful agent ([03:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=212s)–[03:43](https://www.youtube.com/watch?v=NLWiIj47IdI&t=223s)). The video doesn't show what triggers the weekly run.
- *This note's reading:* this is a first-party way to run agents that keep memory between unattended runs, without a Hermes machine or crons of your own. But it's an API product for developers, not a drop-in replacement for a personal markdown brain. See [[Claude Managed Agents]] and [[Agent Memory Patterns]].

### Nate Herk's 32 tricks: what "set up the crons yourself" looks like

- **`/loop`.** In [[Nate Herk - 32 Tricks to Level Up Claude Code]], `/loop` re-runs a prompt in the same session at an interval until you close the session ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s)–[12:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=728s)).
- **Desktop scheduled tasks.** He says loops last only 3 days, so longer schedules belong in desktop scheduled tasks. Each run of those is a separate session without the earlier conversation's context ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)–[12:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=755s)). *The 3-day figure is out of date; see Beyond the source.*
- **A VPS.** For always-on sessions, host Claude Code on a VPS. It keeps running with your laptop closed, and you can reach it over SSH or through Telegram ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)–[12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s)).
- **Remote Control.** It lets you steer a local session from your phone while the code stays on your machine ([12:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=774s)–[13:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=789s)). *Execution does stay local, but the conversation is stored by Anthropic while connected; see Beyond the source.*
- *This note's reading:* none of these refresh a brain by themselves. They give you cadence, and you still have to write the job that curates memory.

## When to use it — and when not to

### Signals that point to Level 5

From Nate's "finding your level" checklist ([29:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1765s)), consider Level 5 if:

- you run agents "offline" (as captioned; he most likely means agents running unattended);
- you have a very large amount of data; and
- you want several Hermes agents to share and stay in sync with one brain.

### Picking a route by what you actually need

*This table combines the sources above. Each row names the source that proposes the route. Current platform limits are under Beyond the source, and the build steps are in [[Schedule Recurring Claude Tasks]] and [[Sync a Workspace to an Always-On Cloud Agent]].*

| You need | Route a source proposes | Source |
|---|---|---|
| A skill that runs on a timer and can use local files | Desktop Routines page: name it, "run this skill", set a schedule | Chase [11:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=690s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s); Jay E [14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s) |
| Schedules that fire with your computer off and still see your Claude Code skills | Hermes on a cloud computer, with the workspace shared through Syncthing | Jay E [16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s) |
| One always-running Claude Code with every file in one place | Claude Code on a VPS | Jay E [17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s); Nate (32 tricks) [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s) |
| Handing your desktop tasks while you're away from it | Dispatch, with the desktop kept awake | Simon [44:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=2652s)–[45:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=2739s) |
| Steering a running local session from your phone | Remote Control | Nate (32 tricks) [12:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=774s) |
| An agent in your product that remembers across unattended runs | Managed Agents with a memory store | Anthropic [02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s) |
| A brain that syncs and refreshes its own memories | GBrain, ideally on Hermes | Nate (second brain) [25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)–[25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s) |

### Reasons to hold back

- **Level 5 isn't "best".** Nate says outright that the top level isn't automatically the goal. He has specific reasons for not sitting there himself ([03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s)). Choose the lowest level that meets your needs, and don't build more if nothing hurts ([04:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=242s), [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)). See [[Second Brain Pain-Point Audit]].
- **Too much context.** What worries him about always-on ingestion is the question of when you have too much context ([26:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1570s), [26:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1576s)). At some point extra material starts doing more harm than good ([26:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1576s)).

### Nate's counter-approach: stay in control of ingestion

Rather than letting a background process decide what goes in, Nate keeps full control over what his second brain ingests ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)):

1. He runs a skill that collects all of the week's meeting transcripts ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)).
2. He works through the material with Claude to decide where it belongs in the brain ([26:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1591s)). His exact wording here is *(unclear in captions)*.
3. They ingest it together ([26:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1591s)). He says he likes having that control ([26:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1596s)).

See [[Ingest Sources into an LLM Wiki]] for the ingest mechanics.

He decides what belongs in the brain by splitting data into **context** and **connections**. These are the first two of his "four C's": context, connections, capabilities and cadence. For a second brain he mainly thinks about the first two ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s)). Full detail is in [[Context vs Connections]].

- **Context** is evergreen, locked-in material, such as the quarter's projects with their decisions and statuses ([27:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1621s), [27:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1634s)). His term for these quarterly projects is captioned "OTAs"; the exact term is *(unclear in captions)*.
- **Connections** are live data that keeps changing: Slack threads, emails, customer data ([27:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1645s)). He doesn't ingest these. They become noise you'd have to prune every month ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)).
- **His test** is whether he would still want that memory in the brain a year from now. If not, it is noise ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)).
- **Access instead of ingestion.** Volatile data stays out of the brain, but the brain must still be able to reach it ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)). Ask about last week's conversation with a colleague on one quarterly project, and the brain looks in three places in order ([28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)):
  1. the project file;
  2. the wiki and meeting transcripts;
  3. finally ClickUp, where it pulls the live conversation ([28:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1706s)).

  He still counts that as a second brain, because it knows where the data lives and in what order to look ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s)). See [[Tiered Lookup Routing]].

| | Always-on Brain OS (Level 5) | Nate's controlled ingestion |
|---|---|---|
| Who decides what enters the brain | A background process that keeps syncing and adding ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) | Nate, working through each week's material with Claude ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)) |
| Cadence | Continuous ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) | He runs a skill over the week's transcripts ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)) |
| Volatile data (Slack, email, customers) | Not addressed in the video | Kept out; fetched live when a question needs it ([27:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1645s), [28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)) |
| Infrastructure | An always-on agent like Hermes, or cron jobs you manage yourself in Claude Code ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s), [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)) | A skill run on demand ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)) |
| Main risk he names | Too much context doing more harm than good ([26:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1576s)) | (none stated) |

### Adjacent question: team-wide brains

Syncing several agents raises a related question Nate only touches on: how a whole team keeps its second brains in sync ([29:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1780s)).

- He doesn't think the choice of Google Drive, Notion, GitHub or plugins is the hard part ([29:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1794s)).
- The real work is adoption and change management: process owners keeping their docs current, and colleagues pulling from the brain instead of pinging the same people ([30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s), [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)).
- Get your own brain working day to day before trying to solve it for the team ([30:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1826s)).

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]] describes Level 5 as the self-maintaining version of everything below it, with GBrain as the example ([25:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1525s)). He is deliberately not there yet, for two reasons. In Claude Code you'd have to run the scheduling yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). And he is wary of automatic ingestion flooding the brain with context ([26:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1576s)). His alternative is hands-on weekly ingestion plus live access to volatile data ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s), [28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)). He is experimenting with GBrain on Hermes Agent ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]] — Routines are the third ARMS layer. He runs most of his around the clock on a Hermes agent with its own cloud computer and shares his Claude Code skills and memory with it through Syncthing. He sees Claude Code on a VPS as the next step ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[18:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1101s)).
- [[Simon Pittman - Set Up Claude Cowork]] — For him "always-on" means a desktop kept awake for Cowork scheduled tasks, plus Dispatch requests sent from his phone ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s), [44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]] — Turning a skill into a scheduled automation is easy, either with a prompt or on the desktop Routines page. Self-improving loops then need past runs logged somewhere they can see ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s), [22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)).
- [[Anthropic - What Is Claude Managed Agents]] — Hosted agents read a memory store before each run and write what changed afterwards ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)–[02:30](https://www.youtube.com/watch?v=NLWiIj47IdI&t=150s), [03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)–[03:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=206s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] — The Claude Code building blocks: `/loop`, desktop scheduled tasks, a VPS and Remote Control ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s)–[13:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=789s)).

## Where sources disagree

**1. How hard is scheduling in Claude Code?**
- [[Nate Herk - Every Level of a Claude Second Brain]]: in Claude Code you'd have to create and manage the cron jobs yourself. That's part of why he tries GBrain on Hermes instead ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)–[25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: turning a skill into an automation is very easy, with a single prompt or the desktop Routines page ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s)).
- *One way to reconcile them (this note's reading):* they're describing different jobs. Scheduling one skill is quick. A brain that keeps syncing and deduplicating itself, as GBrain does, is a system you still have to design and look after. The platform limits that put conditions on "easy" are under Beyond the source.

**2. Do you need a separate machine to run things with your computer off?**
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: yes. Local routines stop when the computer is off, so he runs Hermes on a cloud machine. He expected a hosted Claude Code option only later ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)–[16:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=989s), [18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)–[18:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1112s)).
- [[Simon Pittman - Set Up Claude Cowork]]: keep a desktop awake so Cowork scheduled tasks run ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)–[41:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=2517s)).
- [[Anthropic - What Is Claude Managed Agents]]: demonstrates Anthropic-hosted agents with persistent memory ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)).
- Current Anthropic docs have moved past both creators' framing. See Beyond the source.

**3. Is writing memory automatically a risk or a feature?**
- [[Nate Herk - Every Level of a Claude Second Brain]] worries that always-on ingestion ends in too much context ([26:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1576s)).
- [[Anthropic - What Is Claude Managed Agents]] has agents write to memory on every run, but only the findings of their job. The pricing agent stores what changed ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s)). The incident coordinator reads past incidents from the store; the video implies, but doesn't show, that incidents get written there ([03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s)–[03:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=206s)).
- *This note's reading:* narrow memory writes tied to one job sit between Nate's hand-curated ingestion and a brain that swallows everything.

**4. Terminology, not substance.** "Always-on" means self-refreshing memory for Nate ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)), a dedicated agent computer for Jay ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)), an awake desktop for Simon ([44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)) and a VPS session in Nate's tricks video ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)). See the table under *How it works*.

## Beyond the source

*Not from the videos. Each item was checked at the link given.*

- **GBrain** (MIT) is Garry Tan's memory layer for the AI agents you already use. Knowledge lives as markdown files in a git "brain repo". GBrain syncs that repo into Postgres for retrieval, using embedded PGLite by default and Postgres with pgvector for larger or shared brains. It also builds a "self-wiring" knowledge graph with typed edges such as `works_at`. Its "dream cycle" is a cron-driven overnight pass. It deduplicates people pages, fixes citations, scores salience, finds contradictions and preps the next day's tasks. It can also pull in Gmail, Calendar and Contacts, and meeting data via webhooks. The README lists Claude Code, Codex, OpenClaw, Hermes and Cursor among supported harnesses. So Claude Code support isn't the blocker; the scheduling is what Nate says you'd have to manage yourself. [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain)
- **gstack** (MIT) is Garry Tan's Claude Code setup. It turns Claude Code into a virtual engineering team. Its README counts twenty-three specialists and eight power tools, all slash commands written in Markdown. The specialists are roles such as CEO, eng manager, designer and QA lead. Its skills include `/setup-gbrain`, which connects GBrain through local PGLite, Supabase or a remote MCP endpoint, and `/sync-gbrain`. The GBrain README also lists a gstack repo as an example source a brain can index. *My inference:* those hooks are the concrete link behind "pairs well with gstack". [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Hermes Agent has scheduling built in.** Nous Research's Hermes Agent schedules tasks from plain phrases like "every monday 9am" or from cron expressions. Jobs only fire while the Hermes gateway daemon is running, and each one runs in a fresh, isolated session with no chat history. By default a cron job runs detached from any repo, so no AGENTS.md or CLAUDE.md is loaded. The prompt, or the skills attached to the job, must supply whatever it needs. *My inference:* the built-in scheduler is why Hermes suits an always-on brain. A job that maintains a markdown brain still has to be pointed at the brain's folder explicitly. [Hermes Agent docs — Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- **What "set up the crons yourself" means in Claude Code today.** `/loop` and the in-session cron tools are tied to the session. They only fire while Claude Code is running and stop when the session exits; `--resume` can restore some of them. Recurring tasks expire after 7 days. For durable schedules the docs point to three options:
  - **Desktop scheduled tasks** run on your machine, which must be on, and can use local files.
  - **Cloud Routines** run on Anthropic-managed infrastructure against a fresh repo clone, with no local files and a minimum interval of one hour.
  - **GitHub Actions** schedules.

  *My inference:* for a local markdown brain, Desktop scheduled tasks are the closest fit for a GBrain-style nightly refresh. [Claude Code docs — Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
- **The desktop Routines page creates both local and cloud schedules.** The Desktop docs say the Routines page creates local scheduled tasks and remote routines.
  - **Local tasks** can use your files and tools, but fire only while the app is open and the computer is awake. If the computer sleeps through a run, it's skipped. On wake, Desktop starts one catch-up run for the most recent miss in the last seven days.
  - **Staying awake.** A **Keep computer awake** setting is under Settings → Desktop app → General. Closing a laptop lid still puts it to sleep.
  - **Permission stalls.** A task in Manual permission mode stalls until you approve any tool it doesn't have permission for.
  - **Remote routines** run in the cloud with the computer off, but against a fresh clone with no local files, and at most once an hour.

  *My inference:* Chase's "easy" holds for setup. Jay is right that local routines need the machine on. His expectation that a hosted option is still to come is out of date for cloud routines, though his VPS point about keeping local files and context in one place still stands. [Claude Code docs — Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
- **`/loop` tasks expire after 7 days, not 3.** The docs say recurring tasks expire seven days after they're created, and unexpired ones come back when you resume with `--resume` or `--continue`, except a self-paced `/loop` (no interval), which you have to start again. The 3-day figure in [[Nate Herk - 32 Tricks to Level Up Claude Code]] ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)) is out of date. [Claude Code docs — Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
- **Cowork scheduled tasks now run remotely.** The Claude Help Center says Cowork scheduled tasks run remotely, so they keep to schedule while the computer is asleep or the desktop app is closed. A task that needs local files or apps runs only locally. Scheduled tasks are available on all paid plans (Pro, Max, Team, Enterprise). *My inference:* Simon's advice to keep a desktop on ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)) now matters only for local-file tasks, Dispatch and computer use. [Claude Help Center — Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- **Remote Control's data path.** Execution and filesystem access stay on your machine, but all traffic goes through the Anthropic API, and while connected the session transcript (messages, responses, tool activity) is stored on Anthropic servers. So Nate's "code never leaves your machine" ([13:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=784s)) holds for execution, not for the conversation. [Claude Code docs — Remote Control](https://code.claude.com/docs/en/remote-control)
- **Dispatch still needs an awake desktop.** Per the Help Center, Dispatch runs tasks on your desktop using your local files, connectors, plugins and apps. The computer must be awake and the Claude Desktop app open, and setup includes a keep-awake toggle. It's in limited beta for some Pro and Max plans. So Simon's always-on Mac is still the right setup for Dispatch. [Claude Help Center — Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- **How Managed Agents memory stores work.**
  - **What a store is.** A workspace-scoped collection of text documents, mounted as a directory in the session sandbox and read and written with the agent's file tools.
  - **Versioning.** Every change creates an immutable version. Versions are kept for 30 days, and a live memory's recent versions are always kept.
  - **Access and risk.** Stores attach read-write by default. The docs warn that a prompt injection could plant malicious memories, and recommend `read_only` for reference stores.
  - **Limits.** Up to 10,000 memories per store, each up to 100 kB.
  - **Upkeep.** The docs suggest deleting stale memories, or running a *dreaming* session that consolidates content into a new output store.
  - **Beta headers.** Memory store endpoints use the `agent-memory-2026-07-22` header. The rest of Managed Agents uses `managed-agents-2026-04-01`.

  *My inference:* dreaming is the closest first-party counterpart to GBrain's overnight dream cycle described above. [Claude Platform docs — Using agent memory](https://platform.claude.com/docs/en/managed-agents/memory)
- **Syncthing** syncs files continuously between two or more computers. It's open source, has no central server that stores your data, and encrypts connections with TLS. *My inference, from Claude Code's memory docs:* auto memory lives outside the project, at `~/.claude/projects/<project>/memory/`. Syncing only the workspace folder, as Jay does, won't bring that memory over to a Hermes machine unless you sync that folder too. [syncthing.net](https://syncthing.net/), [Claude Code docs — memory](https://code.claude.com/docs/en/memory)

## Related

- [[Second Brain Levels]] covers the full ladder; this note is Level 5.
- [[Context vs Connections]] is the filter for what should enter the brain at all.
- [[Tiered Lookup Routing]] explains fetching volatile data live instead of ingesting it.
- [[Knowledge Graphs]] (Level 4) and [[LLM Wiki]] (Level 2) are the layers Level 5 bundles.
- [[Claude Code Auto Memory]] is the built-in, lighter form of self-updating memory.
- [[Ingest Sources into an LLM Wiki]] covers the controlled, hands-on ingestion Nate prefers.
- [[Port a Claude Code Brain to Other Agents]] covers sharing one brain across harnesses.
- [[Second Brain Pain-Point Audit]] helps check whether you actually need Level 5.
- [[Routines and Scheduled Tasks]] covers the cadence side: what runs when, and where.
- [[Agentic OS]] covers where routines sit in Jay E's ARMS framework and Chase AI's four levels.
- [[Agent Memory Patterns]] covers other ways agents carry memory between runs.
- [[Permissions and Approval Gates]] covers what an unattended agent may do without asking.
- Techniques: [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Build an Event-Triggered Managed Agent]] · [[Set Up Claude Cowork]]
- Tools and people: [[GBrain]], [[Hermes Agent]], [[Claude Code]], [[OpenAI Codex]], [[Garry Tan]], [[Nate Herk]], [[Syncthing]], [[OpenClaw]], [[Claude Cowork]], [[Claude Managed Agents]], [[Jay E]], [[Simon Pittman]], [[Chase AI]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Simon Pittman - Set Up Claude Cowork]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Anthropic - What Is Claude Managed Agents]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]]
- [[Home]]
