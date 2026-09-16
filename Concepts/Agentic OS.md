---
type: concept
aliases: ["AI Operating System", "ARMS Framework"]
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Nate Herk - Build Skills Instead of Agents]]"]
tags: [topic/agentic-os, topic/skills, topic/memory, topic/automation, topic/scheduling, topic/claude-code, topic/teams, topic/agents, topic/design]
---

# Agentic OS

## In one sentence

An agentic OS is a workspace where an agent harness, usually [[Claude Code]], runs your written-down procedures (skills), draws on organised memory, runs jobs on a schedule and reaches your apps, often with a dashboard on top. Both creators who teach it say the dashboard is the smallest part of the value.

- [[Chase AI - The Agentic OS Setup for Claude Code]] says the value isn't a dashboard or a Jarvis-style interface ([00:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=4s)). It is the parts you can't see: loop engineering, skill architecture, state management and a second brain, bundled into one product customised for you ([00:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=14s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]] calls his dashboard the command center of the OS ([00:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=43s)). He says a big part of the OS is how your context and workspace are organised, so that Claude Code works for you rather than against you ([03:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=224s)).

## How it works

### Jay E: the ARMS framework

- **The acronym.** ARMS stands for Applications, Routines, Memory, Skills ([04:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=257s)). He pictures it as giving Claude, your AI employee, its own arms and its own workspace ([04:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=244s)).
- **Learn it bottom-up.** Start with skills, then build a memory system ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)). Only once you are confident there should you schedule routines and build apps or connectors ([04:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=276s)). Each element has three levels ([04:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=289s)).
- **Why routines come third.** Mastering skills and memory is what gives you the confidence to let the agent work while nobody is watching ([14:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=878s)).

| Element (in learning order) | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| **Skills** | Anthropic's pre-built skills under Customize → Skills, including skill-creator ([05:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=338s)) | A skill folder where SKILL.md routes to reference files, such as a brand HTML page ([06:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=402s), [07:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=457s)) | Skills run headlessly with `claude -p`, triggered from a dashboard or an internal app ([09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s), [10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s)) |
| **Memory** | A workspace folder full of files ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)) | Router files: CLAUDE.md routes by department, and each department has its own router file ([12:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=743s), [12:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=765s)) | A visual second brain that shows how files connect and searches faster ([13:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=823s)) |
| **Routines** | Local routines from the desktop app's Routines sidebar ([14:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=893s)) | Cloud scheduled tasks on an always-on agent; he uses [[Hermes Agent]] ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)) | Claude Code installed on a VPS that holds all files and context ([17:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1071s)) |
| **Applications** | The connector directory under Customize → Connectors ([18:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1126s)) | Claude Code finds and connects apps itself ([18:59](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1139s)) | You build your own connectors and apps ([19:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1195s)) |

His trigger for moving memory up a level was scale. When he pointed his second brain at the workspace, it had about 60,000 files ([11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s)). He says that much clutter slows retrieval and eats plan usage ([11:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=684s)).

### Chase: four stacked levels

| Level | What it covers | Timestamps |
|---|---|---|
| **1 · Backbone** | Everything you do in Claude Code becomes a skill or an automation. Sub-phases: workflow audit, skill creation, automation, loop engineering | [01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s), [04:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=271s) |
| **2 · Memory and state** | A store the OS draws on ([[Obsidian]] or an ordinary database), used together with skills so loops can improve themselves. A coherent file structure does most of the work | [02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s), [02:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=133s), [14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s) |
| **3 · Interface** | A custom UI that goes beyond the terminal and the desktop app, which he calls great but limited | [02:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=173s), [03:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=184s) |
| **4 · Distribution** | Teammates or clients use your Level 1–2 work as buttons or voice commands, without running Claude Code themselves | [03:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=190s), [03:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=202s) |

- **Levels 1 and 2 need no UI.** They work in a plain Claude Code terminal, the Codex CLI or the Codex desktop app ([03:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=222s)). See [[OpenAI Codex]].
- **The levels are modular.** The backbone doesn't need any higher level ([13:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=780s)), and the levels stack on top of one another ([13:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=785s)).
- **Loops depend on memory.** Skill and automation outputs have to be logged in one place, so a loop can see what past runs did and improve on them ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)). See [[Loop Engineering]].

### Chase's earlier version: three steps

[[Chase AI - The Three-Step Claude Code Agentic OS]] (May 2026) is the first cut of the same framework. He pitches it as a pipeline: daily workflows become skills, skills become automations, automations become architecture, and memory and observability wrap the whole thing ([00:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=18s)).

| Step | What it covers | Closest June level *(this note's mapping)* |
|---|---|---|
| **1 · Architecture** | Split personal and business work into domains, then tasks, then skills, then a few automations ([01:53](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=113s)). He calls it the real value, worth doing even if you stop there ([03:19](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=199s)) | Level 1, without session mining or loops |
| **2 · Memory** | An Obsidian vault with a Karpathy-style raw, wiki and output layout, or one folder per domain ([09:03](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=543s), [10:34](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=634s)), plus a proper CLAUDE.md, the one piece he says you must add ([11:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=678s)) | Level 2 |
| **3 · Observability** | Buttons that run skills through `claude -p` ([13:45](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=825s)), and panels for what the terminal can't show ([15:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=914s)) | Levels 3 and 4 together |

- **Observability is for you as well as Claude.** Closing his memory recap, he says it isn't enough for Claude to know where things are; you need to see what's going on, which is his lead-in to step 3 ([16:42](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1002s)). His panels track the 5-hour and weekly usage windows and routines used today ([14:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=894s)), plus recent vault changes and forecasts ([15:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=901s)). Memory makes that tracking possible, because work done in a vacuum never shows what's working ([12:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=761s)).
- **What changed by June** *(this note's comparison)*: distribution became its own level rather than a payoff of step 1's codified skills and step 3's buttons, and session mining and self-improvement loops joined Level 1. The core claim stayed: the value is the architecture, not the dashboard ([01:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=74s)).

### The dashboard is the smallest part

- **Jay E:** the visual interface is roughly 20–30% of the value ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s)). The other ~70% is what sits underneath ([03:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=219s)). He still uses the dashboard as his daily homepage ([03:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=211s)).
- **Chase:** Levels 1–2 hold about 90% of the value ([02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s)). Levels 3–4 are the "cherry on top" ([30:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1824s)), which leaves roughly a tenth for the UI and distribution *(this note's arithmetic)*. He likes the dashboards, but says the backbone is where the power is ([12:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=770s)).
- **Chase, three-step version:** buttons pay off mainly for teammates and clients. If you already work well in the terminal, VS Code or the desktop app, they add little ([14:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=840s), [14:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=858s)).
- **What each thinks the UI is for.**
  - Jay E: visualising systems so he can explain them to others ([02:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=129s)), which suits people who think visually ([14:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=846s)).
  - Chase: one place to see things that are hard to see from the terminal ([26:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1565s)), and a way in for people put off by the terminal and even the desktop app ([29:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1789s)).

### Headless Claude Code is the backend for buttons

- **Jay E:**
  - He runs skills without opening a chat by using `claude -p` ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)). It starts a short session that sends one prompt with the model and effort level you chose ([09:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=589s)).
  - In his cleanup example, the only prompt sent was the `/cleanup` command ([09:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=598s)), and the run produced a summary report ([09:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=570s)).
  - The same trick puts skills inside dashboards or internal team apps ([10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s)). You only need to know the feature exists, not any extra tooling ([10:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=614s)).
- **Chase:**
  - Clicking a button calls a headless Claude Code, much like typing `/morning-brief` in a terminal but with no window ([27:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1634s)–[27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s)).
  - Billing: he says Anthropic announced that `claude -p` would draw on a separate credit, then walked it back, so for now it still uses his Max plan ([27:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1671s)–[28:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1693s)). The current status is under *Beyond the source*.
- **Building one:** the steps, security and a starter server are in [[Build an Agentic OS Dashboard]].

### Packaging an OS for other people

- **Jay E: the consulting angle.**
  - For people doing AI consulting, he says building a dashboard like this for a client is a service you can package and sell. He shows design mockups, one of them for a financial services firm ([02:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=147s)).
  - Once your own foundations exist, adapting them for each client is easy ([02:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=161s)).
- **Chase's Level 4: distribution.**
  - Give someone a web app wired to your skills and they are one click away from what Claude Code can do, because the power sits in the skills and automations ([28:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1719s), [28:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1726s)).
  - Results can land in the person's own Obsidian vault or a shared team vault ([24:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1498s)).
  - A web version is easy to hand over as a GitHub repo or a zip ([29:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1741s)). An Obsidian command center has to be set up for each person ([29:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1761s)).
  - For client work, voice or a few buttons goes a long way ([30:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1806s)). He thinks this "dashboard effect" on non-technical people deserves study ([30:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1814s)).

### How the frameworks line up *(this note's synthesis)*

Neither creator compares his framework with the others. The mapping below is this note's reading, and "Level N" means something different in each column.

| Job in the system | Jay E: ARMS | Chase: four levels | Chase: three steps (May) | Nate Herk: four C's | Nate Herk: [[Second Brain Levels]] |
|---|---|---|---|---|---|
| Codified ways of doing work | Skills | Level 1 (skills) | Step 1, architecture (domains, tasks, skills) | Capabilities | Not covered |
| What the agent knows | Memory | Level 2 (memory and state) | Step 2, memory (vault plus CLAUDE.md) | Context | Levels 1–4 (router, wiki, semantic search, graph) |
| Work that runs without you | Routines | Level 1 (automations, loops) | Step 1: selected automations, local or remote, no loops ([05:58](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=358s)) | Cadence | Level 5 (always-on brain OS) |
| Reaching live apps and data | Applications, Levels 1–2 (connectors) | Not a level; his dashboard pulls calendar data ([23:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1439s)) | Not a step | Connections | Not a level; see [[Context vs Connections]] |
| Custom interface | Applications, Level 3; the dashboard is one such app ([20:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1226s)) | Level 3 | Step 3, observability | None | None |
| Other people using it | Client builds, not an element ([02:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=147s)) | Level 4 | Step 1's codified skills make it handable, even packaged and sold to clients ([07:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=421s)); step 3 adds buttons for teammates and clients ([14:27](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=867s)) | None | None |

The Nate Herk columns come from [[Nate Herk - Every Level of a Claude Second Brain]]. He names context, connections, capabilities and cadence ([26:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1601s)), but a second brain mostly uses the first two ([26:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1606s)). His five-level questions are at [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)–[03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s).

What the table shows *(synthesis)*:

- Only Chase makes self-improvement loops and distribution explicit steps.
- Only Jay E treats connectors as their own element.
- Nate's retrieval ladder goes much deeper on memory than either OS framework. Jay E's memory stops at a visual second brain, and Chase's Level 2 is file structure plus index files.

## When to use it — and when not to

**Use it when:**
- **You repeat work with Claude.** Jay E's rule is to make a skill once you've prompted for the same task twice ([05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s)). Chase suggests breaking your use into domains and listing the recurring tasks under each ([06:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=370s)). See [[Workflow Audit into Skills]] and [[Agent Skills]].
- **You want jobs to run unattended,** on a schedule or at a click. See [[Routines and Scheduled Tasks]].
- **Other people need the results but won't use a terminal** (Chase's Level 4).

**Don't:**
- **Start with the dashboard.** Jay E teaches bottom-up ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)). Chase says to put almost all your time into Levels 1–2 ([30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)).
- **Build before you can list your recurring outputs.** Chase says most people can't ([05:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=306s)), so run the audit first.
- **Automate a workflow you haven't proven by hand.** Chase wants a task done manually and confirmed before it becomes a skill ([07:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=440s)). Jay E schedules only once he trusts the skills and memory ([14:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=878s)).

## Where sources disagree

- **When automation comes in.**
  - Chase puts automations and loops inside Level 1, before memory ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s)), and says turning a skill into an automation is easy ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)). He still ties loops to the state logged in Level 2 ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)).
  - His earlier three-step video also puts automations in step 1, but only for tasks that naturally recur: a morning trend scan yes, deep research no ([05:40](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=340s)).
  - Jay E puts routines third, after skills and memory ([14:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=878s)).
  - Neither video settles it for Nate Herk. His repo's build order is under *Beyond the source*.
- **Where scheduled work runs.**
  - Jay E's view:
    - He keeps few local routines because they run only while the computer is on ([16:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=963s)).
    - Most of his scheduled tasks run on Hermes on a cloud machine ([16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s)), with the workspace synced to it through [[Syncthing]] ([17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)).
    - He expects Anthropic-hosted persistent Claude Code only in the near future ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)).
  - Chase shows only Desktop Routines ([11:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=690s)).
  - Chase's earlier video names local and remote automations, and leaves the choice between them to Claude Code ([04:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=241s)–[04:05](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=245s)).
  - How today's docs change this picture is under *Beyond the source*. See also [[Sync a Workspace to an Always-On Cloud Agent]].
- **How memory should be organised.**
  - Jay E optimises for the agent: router files matter more than names humans find easy to browse ([12:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=722s)).
  - Chase says a coherent file structure gets you most of the way ([14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s)), with an index.md at every level ([19:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1168s)) and folder names that are arbitrary ([21:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1268s)).
  - Details in [[Agent Memory Patterns]].
- **What belongs in the store.**
  - Chase suggests putting at least a copy of a domain's data, such as all your sales data, into the vault ([15:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=910s)).
  - Nate Herk keeps fast-changing data out and reaches it live ([27:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1653s)). See [[Context vs Connections]].
- **How much the interface is worth.**
  - Jay E puts the dashboard at 20–30% of the value ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s)), and Chase calls the UI levels the cherry on top ([30:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1824s)).
  - [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] calls his third level, a design OS, the most powerful of his three design systems ([11:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=711s)).
  - *Vault reading:* his design OS generates images across providers and searches a local asset library ([13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s), [15:05](https://www.youtube.com/watch?v=NAumQObJEwM&t=905s)), so it is closer to an ARMS application than a dashboard. He also ranks it against other design systems, not against skills and memory.

## Perspectives from sources

- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: four elements, each with three levels, learned bottom-up. He uses a cloud agent plus file sync for always-on routines, and treats the dashboard as a sellable client service ([03:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=235s), [02:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=147s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: four stacked levels, with 90% of the value in the first two ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s), [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s)). Mining past sessions ([07:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=457s)) and a Claude-led interview ([09:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=542s)) produce a list of tasks to turn into skills. Buttons run `claude -p` ([27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s)), and distribution is its own level ([28:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1717s)).
- [[Nate Herk - Every Level of a Claude Second Brain]]: the four C's model of an AI OS, of which a second brain is mainly context and connections ([26:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1601s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]]: the May version in three steps, with a spoken brain dump building the architecture ([05:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=312s)). See *Chase's earlier version* above.
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: a design module inside his own Claude Code OS, next to memory systems and chats ([13:35](https://www.youtube.com/watch?v=NAumQObJEwM&t=815s)). The wider OS has a dashboard showing usage and spend, and reviews his chats locally every day to suggest new skills ([14:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=884s), [14:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=889s)). See [[Workflow Audit into Skills]] and [[Build an Agentic OS Dashboard]].
- [[Nate Herk - Build Skills Instead of Agents]]: the model is the processor, the agent runtime the operating system, and skills the apps ([00:56](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=56s)). Skills in his own AI OS reuse the same renderers, templates and scripts on every run ([02:08](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=128s)).

## Beyond the source

*Not said in any of the videos. Checked at the linked pages on 2026-09-15.*

- **Nate Herk's four C's, as his repo defines them.**
  - **Context** knows your business.
  - **Connections** reach your stuff. The repo's test is getting tomorrow's calendar and due tasks as live data, without pasting anything in.
  - **Capabilities** know how to do the work. The test is a short phrase that triggers a multi-step workflow producing an artifact.
  - **Cadence** runs without being asked.
  - **Build order:** context can't be skipped, connections and capabilities can be built in parallel, and cadence comes last because you shouldn't automate a workflow that doesn't work by hand. That matches Jay E's routines-after-skills-and-memory order more closely than Chase's Level 1 automations.
  - Sources: [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS), [README](https://raw.githubusercontent.com/nateherkai/AIS-OS/main/README.md)
- **Scheduling options today.**
  - **Local** Desktop tasks: the desktop app's Routines page creates them. They use your local files, but fire only while the app is open and the computer awake.
  - **Cloud** routines: they run on Anthropic-managed infrastructure with the computer off, from a fresh clone of the selected repos with no local files. The minimum interval is one hour and there are no permission prompts during a run. They can also be started by an HTTP POST to a per-routine endpoint with a bearer token, or by GitHub events.
  - Routines are in research preview on Pro, Max, Team and Enterprise plans.
  - **What this means for the videos:** Jay E's claim that Anthropic-hosted always-on Claude Code is still to come ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)) is dated, because cloud routines already run with the computer off. His underlying point still holds. A cloud routine starts from a fresh clone with no local files, so persistent local files still need his Syncthing or VPS approach.
  - Sources: [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Routines](https://code.claude.com/docs/en/routines)
- **What `claude -p` needs behind a button.**
  - **Skills work:** putting `/skill-name` in the prompt runs that skill.
  - **Model and effort:** set them with `--model` (aliases include `haiku`, `sonnet`, `opus`, `fable`) and `--effort`.
  - **Permissions:** runs start in Manual mode, so pre-approve tools with `--allowedTools` or set `--permission-mode`.
  - **Avoid `--bare` for this:** it skips skills and CLAUDE.md, and it doesn't use a subscription login.
  - **Trust:** without `--bare`, a run loads the folder's hooks and `.mcp.json` servers with no trust dialog.
  - Sources: [Headless docs](https://code.claude.com/docs/en/headless), [CLI reference](https://code.claude.com/docs/en/cli-reference)
- **`claude -p` billing status.**
  - **Announced:** Anthropic planned to move Agent SDK and `claude -p` usage to a separate monthly credit from 2026-06-15.
  - **Paused:** that change was paused. This usage still draws on subscription limits, and Anthropic says it will give details before any future change.
  - Source: [Claude Help Center](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) (pause notice dated 2026-06-16)

## Related

- **Build it:** [[Build an Agentic OS Dashboard]], [[Workflow Audit into Skills]], [[Build a Reference-Rich Skill]], [[Schedule Recurring Claude Tasks]], [[Sync a Workspace to an Always-On Cloud Agent]], [[Configure Safe Autonomy Permissions]], [[Second Brain Pain-Point Audit]]
- **Pieces of the OS:** [[Agent Skills]], [[Agent Memory Patterns]], [[Routines and Scheduled Tasks]], [[Connecting Claude to External Tools]], [[Loop Engineering]], [[Permissions and Approval Gates]], [[CLAUDE.md as a Router]]
- **Neighbouring frameworks:** [[Second Brain Levels]], [[Context vs Connections]], [[Always-On Brain OS]], [[Tool-Agnostic Context Files]]
- **Tools and people:** [[Claude Code]], [[Obsidian]], [[Hermes Agent]], [[Syncthing]], [[OpenClaw]], [[OpenAI Codex]], [[Jay E]], [[Chase AI]], [[Nate Herk]], [[Jack Roberts]]
