---
type: concept
aliases: ["Running Claude Unattended", "Automations"]
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/scheduling, topic/automation, topic/loops, topic/agents, topic/claude-code, topic/cowork, topic/managed-agents, topic/agentic-os]
---

# Routines and Scheduled Tasks

## In one sentence

A routine is Claude working without you typing the next prompt. It can run on a timer, until a condition holds, or when an event arrives. [[Jay E - The ARMS Framework for a Claude Agentic OS]] boils it down to a prompt Claude sends itself at a time you choose ([15:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=913s)). He adds routines only once skills and memory are solid. [[Chase AI - The Agentic OS Setup for Claude Code]] also wants a working skill first, but automates it as soon as it keeps repeating, and saves memory for the loops that improve those automations (see Where sources disagree).

## How it works

### The landscape

The first six videos name about nine ways to keep Claude working while you're away, and a later source adds a tenth that runs outside Claude. This table is the vault's summary. Each cell says which source described the mechanism. Current product limits are listed under Beyond the source (labels B1–B9), because several of the videos are already out of date.

| Mechanism | What starts each run | What the sources say | Checked details |
|---|---|---|---|
| `/loop` (inside a session) | A time interval in an open Claude Code session | [[Nate Herk - 32 Tricks to Level Up Claude Code]]: re-runs a prompt in the same session, for example every five minutes, until you close that session ([12:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=723s)). Uses: deploys, PRs, error logs, builds ([12:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=728s)), plus one-off reminders in plain language ([12:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=736s)). [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] calls it an AI cron job ([18:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1087s)) | B1 |
| `/goal` | The previous turn ending, until a condition is met | Coding Sloth: set a goal such as every test passing with no type errors, and Claude keeps working until it gets there or needs you ([19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s), [19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s)) | B2 |
| Desktop scheduled tasks (Claude Code desktop app, local routines) | A schedule, on your own machine | Nate: the longer-term option, but every run is its own session without the conversation's context ([12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s), [12:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=751s)). Jay: you draft them in plain language from the Routines sidebar ([14:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=896s)), but they only run while the computer is on ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)). Chase: give it a name, tell it to run a skill, set a schedule ([11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s)) | B3 |
| Cowork scheduled tasks | A schedule, set up in [[Claude Cowork]] | [[Simon Pittman - Set Up Claude Cowork]]: tasks run on a timer using your instructions, connectors and context ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)). He says the computer must stay on and online ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)) | B5 |
| Cloud routines | A schedule, an API call or a GitHub event, on Anthropic's cloud | None of the first six videos demonstrates these. [[Chase AI - The Three-Step Claude Code Agentic OS]] names remote automations but doesn't say which kind or show one ([04:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=241s)). Jay expects Anthropic-hosted, always-running Claude Code only "in the near future" ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)). Coding Sloth mentions automations that fire when certain things happen ([18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s)) | B4 |
| Headless runs (`claude -p`), including on a VPS | A script, a dashboard button or a server's own scheduler | Jay runs skills from his dashboard as one-shot headless sessions ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)). Chase's dashboard buttons do the same ([27:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1644s)). Nate hosts Claude Code on a VPS so it keeps running with the laptop shut, reachable over SSH or Telegram ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)–[12:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=767s)). Jay's third routines level is Claude Code on a VPS that holds all files and context ([17:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1074s)–[18:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1089s)) | B7 |
| Remote Control and Dispatch | You, from a phone or browser | Nate: keep steering a local session from your phone ([12:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=774s)–[13:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=784s)). Coding Sloth: move sessions between phone, web and terminal ([11:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=693s)). Simon: Dispatch controls the desktop app from the phone ([44:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=2652s)); his demo asks for today's calendar ([45:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=2717s)) | B6 |
| An always-on agent with its own computer | That agent's own scheduler | Jay: most of his scheduled tasks live on [[Hermes Agent]] running on a cloud computer ([16:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1006s)–[16:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1017s)). [[Syncthing]] gives it his Claude Code skills and memory files ([17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)). See [[Sync a Workspace to an Always-On Cloud Agent]] | B9 |
| Event-triggered sessions ([[Claude Managed Agents]]) | Your own application reacting to something | [[Anthropic - What Is Claude Managed Agents]]: your app fires off sessions ([00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s)). Dragging a Kanban card starts one ([00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s)), and so does a monitoring alert ([02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s)). A third agent has a pricing report ready before stand-up ([01:41](https://www.youtube.com/watch?v=NLWiIj47IdI&t=101s)) | B8 |
| Codex app automations (outside Claude) | A schedule, in OpenAI's Codex app | [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]: an hourly job, set to run locally in his vault project rather than in a worktree, processes anything new in raw/ ([29:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1764s)–[29:43](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1783s)). He says Claude Code or Cowork would also work for the build ([32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s)) | B10 |

### Three questions that sort them (vault framing)

The questions below are the vault's framing, not any one creator's. They match the trigger/judge/memory dials in [[Loop Engineering]].

1. **Where does it run?** Options are your open session, your own machine, a machine you rent, or a provider's cloud. The answer decides whether a sleeping laptop matters. It also decides whether the run can see local files.
2. **What starts it?** An interval, a finish condition, a calendar schedule, an event, or you from your phone.
3. **What carries over between runs?** Often nothing:
   - Nate points out that each scheduled desktop run is a fresh session ([12:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=751s)).
   - Chase wants every run's output logged where later loops can look back at it ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1377s)).
   - Anthropic's pricing agent checks last week's findings in a memory store before starting, and stores what changed afterwards ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s)–[02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s)).
   - Jay's whole Syncthing setup exists so the remote agent can see the skills and memory built up locally ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s)).
   - Matt Wolfe's hourly ingest needs no memory store. Files still in raw/ are the queue, and processed clips move to a processed folder ([29:06](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1746s), [29:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1778s)).

See [[Agent Memory Patterns]].

### Routines come after the skill works

- **Jay's order.** Learn bottom-up. Skills come first, then your memory system, and only once you're confident do you schedule routines or build apps ([04:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=271s)–[04:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=279s)). Routines are the third layer because mastering skills and memory is what gives you the confidence to leave the agent unwatched ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)–[14:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=884s)).
- **Why the skill matters.** His daily routine calls a custom skill, so he is 70–80% confident the draft sounds like him and needs only small edits ([15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s)–[15:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=951s)).
- **Chase's order.** His level one pairs skills with automations, and memory and state are level two ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s)–[02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)). Once a task is a skill and keeps repeating, ask why it isn't an automation yet ([11:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=663s)–[11:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=681s)). The next step is a self-improvement loop on top of that automation, which he says ties into memory and state ([11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s)–[12:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=735s)). He calls skills plus automations the backbone ([12:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=751s)). He puts that backbone, together with memory, at about 90% of an agentic OS's value ([02:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=163s)). See [[Workflow Audit into Skills]] and [[Agentic OS]].
- **Only what naturally recurs.** In his earlier three-step video, Chase says not everything needs automating ([03:37](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=217s)): a morning trend scan (a daily scan of AI and competitors on YouTube and GitHub, written into his vault ([03:50](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=230s))) is an easy win, deep research isn't ([05:40](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=340s)). Each automation runs locally or remotely, and he leaves that choice to Claude Code ([04:05](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=245s)). *Vault reading:* the deciding question is whether the job needs files on your machine (B3, B4).
- **Simon's order.** Scheduled tasks are the last of his seven steps ([41:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2487s)), after global instructions, context files, connectors, skills and plugins. His weekly briefer reads his About Me files before it researches anything ([42:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2538s)).

### Not the same as the Always-On Brain OS

"Always-on" means two different things in this vault. Keep them apart.

- **[[Always-On Brain OS]]** (Level 5 in [[Nate Herk - Every Level of a Claude Second Brain]]) is about *memory*: a brain that keeps itself current. Nate's example, [[GBrain]], keeps syncing, refreshing memories and adding material on its own ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)). Scheduling is just the plumbing. Nate notes you could run it in Claude Code but would have to handle the crons yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). Whether a brain should take in material automatically is a separate question; see [[Context vs Connections]].
- **This note** is about the *runner* being available:
  - Simon's always-on Mac on his desk exists for Dispatch and scheduled tasks ([44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)).
  - Jay's Hermes is always on because it has its own cloud computer ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[16:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1012s)).
  - A routine can maintain a brain, but a routine that drafts a newsletter isn't a brain OS.

## When to use it — and when not to

The pairings below are the vault's synthesis. Product limits behind them are under Beyond the source.

| You want to… | Reach for | Grounding |
|---|---|---|
| Watch a deploy, PR or build while you keep working | `/loop` | Nate [12:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=723s), [12:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=728s); B1 |
| Keep going until a checkable finish line | `/goal` with a condition Claude can prove in its output | Coding Sloth [19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s); B2; [[Tests-First Goal Loop]] |
| Run a skill on a schedule that needs files on your computer | Desktop scheduled task on a machine that stays awake | Jay [16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s); Chase [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s); B3 |
| Process whatever lands in a drop folder | A local scheduled job whose prompt only touches unprocessed files | Matt Wolfe [29:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1778s); B3, B10 |
| Get a weekly brief from email, calendar and Notion | Cowork scheduled task | Simon [42:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2521s)–[42:28](https://www.youtube.com/watch?v=pl90LATQlHI&t=2548s); B5 |
| Run a repository job with the laptop closed | Cloud routine | B4 (not covered in the videos) |
| Keep a persistent workspace working around the clock | An agent on its own cloud machine, or Claude Code on a VPS | Jay [16:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1006s), [17:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1074s); Nate [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s); [[Sync a Workspace to an Always-On Cloud Agent]] |
| Start an agent when something happens in your product | Event-triggered Managed Agents session | Anthropic [00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s), [02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s); B8; [[Build an Event-Triggered Managed Agent]] |
| Nudge work that's already running | Remote Control or Dispatch | Nate [12:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=774s); Simon [45:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=2706s); B6 |

**Hold off when:**

- **The skill isn't dialled in yet.** Jay only lets an agent work unmonitored once skills and memory are mastered ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)–[14:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=884s)). *Vault reasoning:* scheduling a mediocre skill just produces mediocre output more often. Chase only automates where it makes sense ([11:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=681s)).
- **The run would send, delete or publish without review.**
  - Simon's standing rule is that Claude checks with him before deleting, sending or publishing anything ([10:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=617s)).
  - He trained Cowork to leave emails as drafts ([26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s)–[26:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1596s)).
  - In his Dispatch update he notes that letting Claude work in your browser means it acts in Chrome without asking, even on sites you haven't approved ([44:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2670s)–[44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s)).
  - See [[Permissions and Approval Gates]]. Anthropic's incident demo shows the same instinct: a permission policy holds the Slack post until a person approves it ([03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)).
- **Your token budget is tight.** Coding Sloth rates `/goal` a tier lower on cheaper plans ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).
- **The work has to last for days.** Don't use a session-bound `/loop` for that (B1).

## Where sources disagree

1. **Does the computer have to stay on?**
   - *Simon:* yes, for Cowork scheduled tasks. That's his argument for a desktop you leave switched on ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)–[41:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=2517s)). He advises against the keep-awake option on a laptop ([43:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=2606s)–[43:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2610s)).
   - *Jay:* local routines only run while the computer is on ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)). That's why most of his jobs run on Hermes ([16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s)).
   - *Current docs (B3–B5):*
     - Claude Code desktop tasks still need the app open and the machine awake.
     - Cowork scheduled tasks now run remotely unless they need local files.
     - Cloud routines need no machine at all.
2. **Is `/loop` a daily scheduler?**
   - *Coding Sloth:* loops are his routines. They keep personal projects moving while he's away, for example by picking an open GitHub issue each day and leaving a PR ([18:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1092s)–[18:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1114s)).
   - *Nate:* `/loop` lives inside a session and lasts three days, so anything longer belongs in desktop scheduled tasks ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)–[12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s)).
   - *Docs (B1):* seven days, and tied to the session. Nate's framing is closer. Daily unattended jobs fit a routine better.
3. **Is scheduling in Claude Code hard?**
   - *Nate, in his second-brain video:* you'd have to handle the crons yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)).
   - *Chase:* it's very easy. Ask Claude Code to turn the skill into an automation, or use the desktop Routines page ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)–[11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s)).
   - *Jay:* first-level routines come out of the box and are simple to set up ([14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s), [16:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=961s)).
   - *Vault reading:* creating the schedule itself is now easy. Nate's remark was about the extra setup a self-maintaining brain like GBrain needs around its crons, not about the scheduler.
4. **Will Anthropic host always-on agents?**
   - *Jay:* predicts a persistent cloud workspace later, not now, because of file storage and security ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)–[18:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1110s)).
   - *Anthropic's video:* already shows hosted sessions in isolated containers ([00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s)), with a memory store that carries findings from one week to the next ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)–[02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s)).
   - *Docs (B4, B8):* cloud routines and scheduled deployments exist. But a routine starts from a fresh repository clone each time, so Jay's point about a persistent local workspace still partly holds.
5. **Do automations wait for a memory system?**
   - *Jay:* yes. Skills first, then memory, then routines ([04:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=271s)–[04:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=279s)).
   - *Chase:* no. Automations sit in level one beside skills, and memory and state are level two ([01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s)–[02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s)). He brings memory in for loops that look at past runs to improve future ones ([02:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=133s)–[02:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=161s)).
   - *Vault reading:* both want a working skill first. A plain scheduled skill can run before a memory layer exists, but a routine meant to improve itself needs somewhere to log and read its past runs.
6. **How far should an unattended job be trusted?**
   - *Simon and Anthropic:* hold anything that sends, deletes or publishes for a person ([10:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=617s), [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)).
   - *Matt Wolfe:* his hourly job writes wiki pages, then commits and pushes to the main branch, and mentions no review step ([31:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1881s)).
   - *Vault reading:* a push to a private backup repo is easy to undo, so skipping review there is reasonable. Still have the run confirm processing finished before it commits.

## Perspectives from sources

- **[[Nate Herk - 32 Tricks to Level Up Claude Code]]** covers four ways to run unattended:
  - `/loop` for polling inside a session, plus plain-language reminders ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s), [12:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=736s));
  - desktop scheduled tasks for longer schedules, each run starting a fresh session ([12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s));
  - a VPS for sessions that survive a closed laptop ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s));
  - Remote Control from your phone ([12:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=774s)).

  He also sets a sound notification so he knows when one of many sessions needs him ([08:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=514s)–[08:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=535s)).
- **[[Simon Pittman - Set Up Claude Cowork]]** calls scheduled tasks his favourite feature ([41:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2490s)).
  - He shows a Tuesday weekly briefer and a 9:30 weekday inbox triage ([42:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2521s), [42:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=2554s)–[42:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=2566s)).
  - He says to decide where outputs land ([42:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=2577s)).
  - He adds Dispatch and computer use in a post-filming update ([43:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=2629s)).
  - He pictures a morning triage turning 30–40 minutes of busywork into five ([45:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=2746s)–[46:04](https://www.youtube.com/watch?v=pl90LATQlHI&t=2764s)).
- **[[Jay E - The ARMS Framework for a Claude Agentic OS]]** makes routines the third ARMS layer ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)). His three levels are:
  1. local desktop routines ([14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s));
  2. cloud scheduling on an always-on agent ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s));
  3. Claude Code on a VPS ([17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s)).

  He also runs skills headlessly from his dashboard ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)).
- **[[Chase AI - The Agentic OS Setup for Claude Code]]** turns skills into automations in two ways: by asking Claude Code, or through desktop Routines ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s), [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s)). He logs runs so loops can improve them ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)). His dashboard buttons call headless Claude Code ([27:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1644s)).
- **[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]** runs three loop automations ([18:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1106s)–[18:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1133s)): a daily issue-to-PR worker, a security and bug sweep, and feature brainstorming.
  - He thinks event-triggered automations are worth trying ([18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s)–[19:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1145s)).
  - He rates `/goal` by how many tokens your plan allows ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).
  - He rates Remote Control highly only if you're often out ([11:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=713s)).
- **[[Anthropic - What Is Claude Managed Agents]]** shows three runs started by your app rather than a person:
  - an event-started coding session ([00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s)), with parallel tickets in separate containers ([01:31](https://www.youtube.com/watch?v=NLWiIj47IdI&t=91s));
  - a recurring pricing report that reports week-over-week changes from memory ([01:41](https://www.youtube.com/watch?v=NLWiIj47IdI&t=101s), [02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s));
  - an alert-triggered triage that waits for human approval before posting ([02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s), [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)).
- **[[Nate Herk - Every Level of a Claude Second Brain]]** thinks adding GBrain's always-on layer to a Hermes agent would work well. In Claude Code you'd have to set up the crons yourself, which is why he isn't running GBrain there and is trying it on his Hermes agent instead ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)–[26:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1561s)).
- **[[Chase AI - The Three-Step Claude Code Agentic OS]]** automates only naturally recurring skills (see above), and his dashboard counts routines used today ([14:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=894s)).
- **[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]** puts ingestion on autopilot ([28:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1704s)). After reprocessing every raw file under updated rules ([28:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1727s)), he schedules an hourly Codex automation on the strongest model at high reasoning ([29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s), [29:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1789s)). He then adds a commit and push to a private GitHub repo to each run, as an hourly backup ([31:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1881s)–[31:39](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1899s)).
- **[[Nate Herk - Claude as a One-Person Marketing Team]]** sketches a weekly loop without building it: connect Claude to performance data, review what it made and what did well, and make more of the winners ([30:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=1845s)). Separately, he suggests automations that sweep and update his generation-log sheet ([37:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=2238s)), weekly research that scrapes creatives for ideas ([37:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=2247s)), and an angle-performance tab for analytics ([37:40](https://www.youtube.com/watch?v=yCACmFTiCto&t=2260s)). *Vault reading:* that sheet could be the loop's run log; whether to store the metrics there or fetch them live at review time is the question in [[Context vs Connections]].

## Beyond the source

*Not from the videos. Checked on 2026-09-15 at the linked pages. Several of these features are in research preview or beta, so recheck limits before relying on them.*

**Anthropic's own comparison of Claude Code scheduling options:**

| | Cloud routine | Desktop scheduled task | `/loop` |
|---|---|---|---|
| Runs on | Anthropic-managed cloud | Your machine | Your machine |
| Machine must be on | No | Yes | Yes |
| Open session needed | No | No | Yes |
| Local files | No (fresh clone) | Yes | Yes |
| Permission prompts | None; runs autonomously | Set per task | Inherited from the session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

Source: [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)

- **B1 — `/loop` and in-session tasks.**
  - Tasks belong to the current conversation. They fire only while Claude Code is running and idle, and closing the terminal stops them.
  - Recurring tasks expire seven days after creation. Nate's "three days" is out of date.
  - `--resume` or `--continue` restores unexpired tasks, but not a self-paced `/loop`.
  - A session holds up to 50 tasks. Recurring tasks can fire up to 30 minutes late (deliberate jitter), and missed fires aren't caught up.
  - [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
- **B2 — `/goal`.**
  - After each turn, a small fast model (Haiku by default on the Claude API) judges the condition against the conversation. The judge doesn't run commands itself.
  - The goal clears when it's met, when it's judged impossible, or when an error you have to fix occurs.
  - It doesn't change the permission mode; the docs suggest auto mode for unattended turns. It also works with `claude -p`.
  - [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)
- **B3 — Desktop scheduled tasks.**
  - Create one from the Code tab: Routines, New routine, Local.
  - Runs happen only while the app is open and the computer is awake. A run that falls during sleep is skipped. On wake, Desktop starts one catch-up run for the most recent miss within the last seven days.
  - "Keep computer awake" stops idle sleep, but closing the lid still sleeps the machine.
  - Each task has its own permission mode. A task in Manual mode stalls until you approve a prompt.
  - The prompt is stored at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`.
  - [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
- **B4 — Cloud routines.**
  - Research preview on Pro, Max, Team and Enterprise. Create them at claude.ai/code/routines, from Desktop (Routines, then Cloud) or with `/schedule` in the CLI.
  - Triggers: a schedule (minimum one hour), an HTTP API call, or GitHub pull-request and release events.
  - Each run clones the repositories fresh and pushes to `claude/`-prefixed branches. There are no permission prompts during a run, and every connected connector is included unless you remove it.
  - There is a daily cap on runs. A green run status only means the session ran without an infrastructure error, not that the task succeeded.
  - [Automate work with routines](https://code.claude.com/docs/en/routines)
- **B5 — Cowork scheduled tasks.**
  - Cadences are hourly, daily, weekly, weekdays or manual.
  - Tasks run remotely even while the computer sleeps or the app is closed. They can use connectors, skills, plugins and files saved to your Claude account, but can't be tied to a folder on your computer.
  - Tasks that need local files or apps run locally instead. The article doesn't say what happens to those while the computer sleeps, so assume they need it awake (inference, not stated).
  - So Simon's always-on-desktop advice now applies mainly to local-file tasks and Dispatch.
  - [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- **B6 — Remote Control, Dispatch and Channels.**
  - **Remote Control** connects claude.ai/code or the Claude app to a session running on your machine. It needs a claude.ai subscription login (Pro, Max, Team or Enterprise), not an API key, and on Team and Enterprise an Owner must switch it on first.
    - Execution and file access stay local, but the transcript is stored on Anthropic's servers while connected. So "code never leaves your machine" is true of execution, not of the conversation.
    - Closing the terminal takes the session offline. On a remote server, run it inside `tmux` or `screen`.
    - [Remote Control](https://code.claude.com/docs/en/remote-control)
  - **Dispatch** is in limited beta for Pro and Max. It needs the desktop app open and the computer awake, and it can use local files, connectors, plugins and computer use. [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
  - **Channels** are the documented way to reach a running Claude Code session from Telegram, as Nate describes. They're a research preview, with Telegram, Discord and iMessage plugins that push messages into an open session. A pairing step and sender allowlist limit who can send. Events only arrive while the session is open. [Channels](https://code.claude.com/docs/en/channels)
- **B7 — Headless runs and servers.**
  - `claude -p` starts in Manual permission mode on every plan. Pass `--permission-mode` (for example `auto` or `dontAsk`) or `--allowedTools` for unattended work. A `/skill-name` inside the prompt is expanded. [Headless](https://code.claude.com/docs/en/headless)
  - The docs reserve `bypassPermissions` for isolated containers and VMs. [Permission modes](https://code.claude.com/docs/en/permission-modes)
  - `claude setup-token` creates a one-year subscription token for machines without a browser. That token can't start Remote Control or use claude.ai connectors. [Authentication](https://code.claude.com/docs/en/authentication)
- **B8 — Managed Agents scheduled deployments.**
  - The Deployments API (beta header `managed-agents-2026-04-01`) runs an agent on a cron expression with an IANA timezone, down to the minute.
  - Runs get jitter of up to 15% of the interval between runs, at least 5 seconds and at most 9 minutes. An organisation can have up to 1,000 deployments.
  - Every attempt is recorded as a deployment run. Unpausing doesn't backfill missed runs. You can set an optional budget per run.
  - [Scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)
  - Pricing at launch (8 April 2026): standard token rates plus $0.08 per active session-hour. [Launch post](https://claude.com/blog/claude-managed-agents)
- **B9 — Hermes Agent cron.**
  - The scheduler lives in the Hermes gateway daemon, which checks for due jobs every 60 seconds. Jobs run in fresh, isolated sessions.
  - `--workdir` loads `AGENTS.md` or `CLAUDE.md` from that folder, and `--skill` attaches skills.
  - Output is saved under `~/.hermes/cron/output/`.
  - [Hermes cron docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- **B10 — Codex app automations.**
  - OpenAI's current docs call these scheduled tasks, and the old Codex automations page redirects there.
  - Keep the computer on and the app running when a task needs local files. Web-based scheduled tasks run on OpenAI's infrastructure without the desktop app, using uploaded files and connected tools.
  - In a Git repository a task can run in a worktree, which keeps its changes apart from your active work, or locally, which changes your main checkout directly. Matt chose local.
  - Tasks run unattended with your default sandbox settings: read-only blocks edits, and full access runs without approval checks.
  - [Scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app)

## Related

- **Build it:** [[Schedule Recurring Claude Tasks]], [[Sync a Workspace to an Always-On Cloud Agent]], [[Build an Event-Triggered Managed Agent]], [[Build an Agentic OS Dashboard]], [[Tests-First Goal Loop]], [[Configure Safe Autonomy Permissions]]
- **Concepts:** [[Loop Engineering]], [[Always-On Brain OS]], [[Agentic OS]], [[Agent Skills]], [[Agent Memory Patterns]], [[Permissions and Approval Gates]], [[Context vs Connections]]
- **Upstream work:** [[Workflow Audit into Skills]], [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]]
- **Tools:** [[Claude Code]], [[Claude Cowork]], [[Claude Managed Agents]], [[Hermes Agent]], [[Syncthing]], [[OpenClaw]], [[OpenAI Codex]]
- **People:** [[Nate Herk]], [[Simon Pittman]], [[Jay E]], [[Chase AI]], [[The Coding Sloth]], [[Matt Wolfe]]
- **Sources:** [[Nate Herk - 32 Tricks to Level Up Claude Code]], [[Simon Pittman - Set Up Claude Cowork]], [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[Chase AI - The Agentic OS Setup for Claude Code]], [[The Coding Sloth - 1000 Hours of Claude Code Lessons]], [[Anthropic - What Is Claude Managed Agents]], [[Nate Herk - Every Level of a Claude Second Brain]], [[Chase AI - The Three-Step Claude Code Agentic OS]], [[Matt Wolfe - Second Brain Wiki with Journal and CRM]], [[Nate Herk - Claude as a One-Person Marketing Team]]
- [[Home]]
