---
type: source
title: "The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)"
creator: "[[Jay E]]"
channel: "Jay E | RoboNuggets"
url: https://www.youtube.com/watch?v=8NSyI-npJCU
video_id: 8NSyI-npJCU
published: 2026-08-21
duration: "21:38"
ingested: 2026-09-15
topics: [agentic OS, ARMS framework, skills, reference files, headless claude -p, memory, router files, visual second brain, routines, cloud scheduling, workspace sync, connectors, micro-apps, dashboards]
tags: [source/youtube, topic/agentic-os, topic/skills, topic/memory, topic/second-brain, topic/context, topic/scheduling, topic/automation, topic/mcp, topic/claude-code, topic/agents, topic/portability]
---

# Jay E - The ARMS Framework for a Claude Agentic OS

> **Creator:** [[Jay E]] · **Published:** 2026-08-21 · **Length:** 21:38 · [Watch on YouTube](https://www.youtube.com/watch?v=8NSyI-npJCU)

## TL;DR

Jay E (RoboNuggets) opens with the dashboard he uses as the "command center" of his [[Claude Code]] agentic OS, then says the dashboard is only about 20–30% of the value. The rest is how the workspace underneath is organised, which he frames as the **ARMS framework: Applications, Routines, Memory, Skills**. He says to learn it bottom-up and gives each element three levels:

- **Skills:** Anthropic's pre-built skills and skill-creator, then skill folders where SKILL.md routes to reference files, then headless `claude -p` runs from a dashboard button.
- **Memory:** a flat workspace, then router files built for the agent (a CLAUDE.md router plus one router per department), then a visual second brain.
- **Routines:** local desktop-app routines, then cloud scheduling on an always-on [[Hermes Agent]] that gets his skills and memory via [[Syncthing]], then Claude Code on a VPS.
- **Applications:** the connectors directory, then a skill that finds connectors for him, then connectors and micro-apps he builds himself.

It tours a finished setup rather than building one: every starter prompt is shown only on screen. Part of the routines advice is dated; current behaviour is under Caveats and Beyond the source.

## Key takeaways

- **The dashboard is the smaller part.** He rates the visual interface at 20–30% of the value. About 70% lies in how context and the workspace are organised [03:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=213s), [03:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=219s), [03:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=224s). See [[Agentic OS]] and [[Build an Agentic OS Dashboard]].
- **ARMS, learned bottom-up.** Go skills → memory → routines → applications [04:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=257s), [04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s), [04:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=275s). Skills and memory give you the confidence to let the agent run unmonitored [14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s).
- **Prompted twice → make a skill.** Skills are shortcuts to your SOPs [05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s), [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s). Build your own, because your work is custom [06:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=360s). See [[Agent Skills]], [[Workflow Audit into Skills]] and [[Build vs Install Third-Party Skills]].
- **A skill is a folder.** In strong skills, SKILL.md routes to reference files such as a brand HTML file with fonts and palettes. Visual references suit design skills [06:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=406s), [07:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=457s), [07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s), [08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s). See [[Build a Reference-Rich Skill]].
- **Run skills headlessly.** `claude -p` sends a one-shot prompt (here just `/cleanup`) with a chosen model and effort. That lets skills sit in dashboards and team apps [09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s), [09:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=589s), [09:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=598s), [10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s).
- **Reorganise memory when retrieval slows.** His workspace held about 60,000 files. He says that hurts retrieval speed and plan usage [11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s), [11:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=684s), [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s).
- **Route for the agent.** CLAUDE.md routes to departments, and each department's router file lists its skills and references [12:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=741s), [12:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=748s), [12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s). He says human-friendly naming matters much less now [12:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=722s). The vault disagrees (see Caveats). See [[CLAUDE.md as a Router]].
- **A routine is a prompt Claude sends itself on a schedule** [15:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=913s). Because his routine uses a custom voice skill, he's 70–80% confident its drafts match his tone and need only minor edits [15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s). See [[Routines and Scheduled Tasks]] and [[Schedule Recurring Claude Tasks]].
- **Always-on agents need your context.** Hermes on its own cloud machine can't see your Claude Code skills and memory. He syncs the workspace to it with Syncthing [17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s), [17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s), [17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s). See [[Sync a Workspace to an Always-On Cloud Agent]].
- **Let the agent find connectors; build what's missing.** Check for an official connector, then community CLIs, APIs or MCPs, with a safety scan before setup [19:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1152s), [19:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1163s), [19:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1188s). Build your own where none exist [19:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1195s). See [[Connecting Claude to External Tools]].

## ARMS at a glance

Rows follow his learning order.

| Element (order) | Level 1 | Level 2 | Level 3 | Move up when… | Vault notes |
|---|---|---|---|---|---|
| **Skills** (1st) | Anthropic's pre-built skills (Claude desktop app → Customize → Skills), plus skill-creator for your own [05:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=342s), [05:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=346s), [05:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=352s) | Skill folders where SKILL.md routes to rich reference files (his /robo brand design system) [06:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=406s), [07:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=457s), [07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s) | Trigger skills outside chat: a dashboard "skills deck" runs them via `claude -p` with a chosen model and effort [09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s), [09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s), [10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s) | You've made a few skills [06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s); a skill needs to do complex work [08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s); you want it without opening a session [09:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=560s) | [[Agent Skills]] · [[Build a Reference-Rich Skill]] · [[Build an Agentic OS Dashboard]] |
| **Memory** (2nd) | A workspace full of files (his "Robo" folder) [10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s), [10:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=648s) | Workspace organised for an agent: CLAUDE.md router + per-department routers such as content.md [11:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=697s), [12:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=741s), [12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s) | Visual second brain showing connections, with fast search and preview [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s), [13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s), [14:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=867s) | The agent struggles to find things, retrieval slows, usage burns [11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s), [11:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=684s), [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s); you need to see or explain the system [14:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=846s) | [[Second Brain Levels]] · [[CLAUDE.md as a Router]] · [[Build a Level 1 Second Brain]] |
| **Routines** (3rd) | Local routines from the desktop app's Routines sidebar, drafted in natural language [14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s), [14:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=896s) | Cloud scheduling on an always-on agent: Hermes on a cloud computer, synced via Syncthing [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s), [16:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=988s), [16:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1008s), [17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s) | Claude Code (or Codex) on a VPS holding all files and context [17:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1069s), [17:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1078s), [18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s) | Local routines only run while the computer is on [16:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=961s); you want one platform and no sync tool [18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s), [18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s) | [[Routines and Scheduled Tasks]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] |
| **Applications** (4th) | Connectors directory (desktop app → Customize → Connectors) [18:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1122s), [18:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1126s) | Claude Code finds and connects apps via a search-connectors skill: official first, then community CLIs, APIs or MCPs [18:59](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1139s), [19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s), [19:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1163s) | Build your own connectors (CLI Printing Press) and applications (dashboard, micro-apps) [19:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1195s), [20:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1201s), [20:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1224s) | Browsing yourself is inefficient [18:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1134s); no agent connector exists [20:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1213s) | [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[Build an Agentic OS Dashboard]] |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=0s) Intro

- **The pitch.** Claude 5-generation models are much more capable, but most people's agent and OS setups haven't caught up [00:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=0s), [00:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=4s). He promises faster, cheaper systems and more productivity [00:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=11s), [00:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=17s). There are four parts, and he claims they'll put you ahead of 99% of agent users [00:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=24s).
- **Background:** a decade with brands, a data-science master's, and he now runs an AI business and a large AI community [00:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=29s), [00:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=34s).

### [00:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=43s) My Agentic OS

- **What it is.** The "virtual command center" gives him one view summarising the apps he uses daily [00:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=43s), [00:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=49s). The widgets:
  - calendar events and chosen time zones [00:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=53s)
  - an email summary that includes messages Claude flags as needing him [00:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=56s)
  - quick links to micro-apps he built [01:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=62s)
  - custom widgets such as YouTube stats [01:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=66s)
  - a view of which routines and scheduled tasks fire when [01:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=71s)
  - a **skills deck** that runs selected skills from the dashboard, choosing the model and effort for each run [01:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=76s), [01:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=82s)
- **Widgets are flexible.** They can be resized and moved, and Claude Code builds new ones well on request [01:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=89s), [01:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=93s).
- **Artifacts ring.** He asks Claude Code for artifacts constantly, so he had it build a finder for past ones [01:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=100s), [01:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=105s). Demo: search a client name (captioned "THRO", *unclear*) and open an HTML file made on 5 August [01:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=110s), [01:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=116s).
- **Second brain at the centre.** Clicking the centre opens his second brain. Visualising systems helps him explain them and show his skills and files [02:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=122s), [02:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=128s), [02:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=133s).
- **Client service.** Dashboards like this are a sellable AI-consulting service [02:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=147s), [02:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=151s). He shows mockups for an Australian financial services firm and a company captioned "Beto Green" (*unclear*) [02:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=154s), [02:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=159s). With your own foundations in place, customising per client is easy [02:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=161s), [02:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=165s).
- *(Community promotion 02:50–03:22 omitted; see Caveats.)*
- **The 20–30% claim.** It is his daily homepage [03:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=204s), [03:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=209s). But he puts the interface at only about 20–30% of the value [03:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=213s). The other ~70% is underneath: organising context and workspace so Claude Code works for you, not against you [03:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=219s), [03:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=224s), [03:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=229s).

### [03:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=234s) The framework

- **His framing, not a standard.** There are many ways to organise an OS; ARMS is how he thinks about it and teaches it [03:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=233s), [03:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=238s). The mnemonic is giving Claude, your AI employee, its own arms and workspace [04:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=242s), [04:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=244s).
- **The four elements:** the applications you use, the routines (scheduled tasks) you run, your memory system, and your agent's skills [04:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=257s), [04:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=260s), [04:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=264s).
- **Learn bottom-up.** Skills first, then memory [04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s), [04:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=271s). Only once you're confident, schedule routines and build apps or connectors [04:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=275s), [04:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=278s), [04:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=283s).
- **Three levels per element,** so you can skip what you know [04:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=286s), [04:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=289s). The goal is an OS like his, customised to you [05:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=301s), [05:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=306s).
- **The PDF guide.** His 9-page guide can be read, or sent to Claude Code so the agent walks you through setup [05:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=311s), [05:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=315s).

### [05:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=309s) Part 1 - Skills

- **What skills are:** shortcuts to your standard operating procedures [05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s), [05:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=328s).
- **The trigger:** once you've asked Claude to do the same job a second time, it's a good skill candidate [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s), [05:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=336s). See [[Workflow Audit into Skills]] and [[Build a Skill from a Successful Run]].

**Level 1: pre-built skills and skill-creator**

- Most people start with Anthropic's pre-built skills, browsable in the Claude desktop app under Customize → Skills [05:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=342s), [05:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=345s), [05:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=348s).
- skill-creator is one of the most popular [05:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=352s), [05:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=356s). He advises making your own skills, because everyone's work is custom and the habit gets refined results faster [06:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=360s), [06:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=364s), [06:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=367s).
- **Demo: /cleanup.**
  - He pasted a whole X post with a tip for speeding up a computer and invoked skill-creator [06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s), [06:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=380s), [06:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=384s).
  - Claude Code built a skill he could test [06:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=386s).
  - He calls it effective, and suggests it if Claude Code or Codex are clogging your machine [06:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=390s), [06:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=392s).
  - He opens its SKILL.md on screen later [07:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=424s) but never explains what commands it runs (see Caveats).

**Level 2: skills with reference files**

- **A skill isn't only its markdown file.** Once you've made a few, you see that the most powerful skills pull from rich references [06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s), [06:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=406s), [06:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=410s).
- **Thin skill:** /cleanup is just one SKILL.md, a markdown file of instructions for running the command [07:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=420s), [07:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=424s), [07:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=426s), [07:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=430s).
- **Thick skill:** his /robo skill folder holds several files [07:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=436s), [07:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=440s). Its SKILL.md tells Claude how to use the skill and acts as a **router** to the reference files beside it [07:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=447s), [07:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=457s), [07:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=459s).
- **Why:** /robo is the design system for his videos and company assets [07:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=466s), [07:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=468s). A brand HTML file guides fonts and colour palettes [07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s), [07:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=478s), [08:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=480s). Visual references work especially well for design skills [08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s).
- **Rule:** for complex tasks, enrich the skill with files rather than housing everything in SKILL.md [08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s), [08:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=493s).
- **Demo: the PDF guide.** He made it with /robo [08:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=500s), [08:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=507s), using a one-line request for a PDF guide on setting up an agentic OS [08:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=510s), [08:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=512s). He answered Claude's clarifying questions [08:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=516s) and got a polished result in one or two prompts, because the skill is so well referenced [08:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=522s), [08:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=526s).
- **On-screen starter prompt.** It has Claude find "thick" skills that stuff everything into SKILL.md and restructure them around richer references [08:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=531s), [08:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=535s), [09:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=540s). The prompt text isn't in the transcript. See [[Build a Reference-Rich Skill]] and [[Skill Improvement Loop]].

**Level 3: triggering skills outside chat**

- It's sometimes useful to run skills with no chat session [09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s), [09:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=548s).
- **Use case.** /cleanup sits in his skills deck, so he needn't open Claude Code in a terminal and type the command [09:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=552s), [09:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=556s), [09:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=560s). He runs it whenever the device slows [09:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=566s). Each run leaves a report summarising what the skill did [09:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=570s), [09:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=572s), [09:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=576s).
- **Mechanism.** Headless runs use `claude -p` [09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s), [09:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=584s), [09:47](https://www.youtube.com/watch?v=8NSyI-npJCU&t=587s). It spins up a quick session that sends a one-shot prompt with your chosen model and effort [09:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=589s), [09:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=594s). His example sent only `/cleanup` [09:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=598s), [10:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=602s).
- **Why it matters.** Skills can be built into dashboards or internal team and company apps [10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s), [10:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=608s), [10:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=610s). That needs no extra tooling beyond knowing `claude -p` exists, in Claude Code or Codex [10:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=614s), [10:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=619s), [10:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=624s). An on-screen prompt starts the integration [10:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=627s).
- Permission flags he doesn't mention are under Beyond the source.

### [10:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=635s) Part 2 - Memory

- The more you use Claude Code, the more context and files pile up [10:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=637s), [10:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=640s).

**Level 1: a workspace full of files**

- A folder of files; his OS workspace is called Robo [10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s), [10:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=648s), [10:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=652s).
- Fine with few files [10:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=657s), but it becomes a problem once the agent struggles to find things [11:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=661s), [11:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=666s).
- **The 60,000-file moment.** Pointing his second brain viewer at Robo revealed about 60,000 files [11:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=670s), [11:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=674s), [11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s). He argues that slows retrieval and burns plan usage faster [11:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=681s), [11:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=684s), [11:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=688s).

**Level 2: a workspace organised for the agent**

- **When to move up:** once memory retrieval slows [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s), [11:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=697s).
- **Agent-first stance.**
  - Many people who lived through the arrival of Windows and Mac learned to tidy folders and rename files so *they* could navigate [11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s), [11:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=708s), [11:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=714s).
  - Now agents operate on the files, so names and file-explorer navigability matter much less, he says [12:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=722s), [12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s), [12:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=729s).
  - The vault disagrees; see Caveats.
- **Router files are the minimum** [12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s), [12:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=739s):
  - **CLAUDE.md is the central router** at the centre of his graph [12:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=741s), [12:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=745s). It describes his departments, so content work stays within one set of files and community work within another [12:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=748s), [12:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=753s), [12:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=757s).
  - **Each department has its own router.** content.md is just a list of skills and reference files, so content lookups go straight to the right place [12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s), [12:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=769s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s), [12:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=777s).
- **Why routers beat folder tidying:** agents parse files very fast, and routers get them there in the fewest steps [13:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=785s), [13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s), [13:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=801s), [13:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=807s). An on-screen prompt sets them up [13:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=810s), [13:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=814s).
- See [[CLAUDE.md as a Router]], [[Build a Level 1 Second Brain]], [[Tiered Lookup Routing]] and [[Keep CLAUDE.md Lean]].

**Level 3: a visual second brain**

- **What it adds:** a view of how files and folders connect, plus faster search [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s), [13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s), [13:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=834s). It's what he has used throughout to show skills and how CLAUDE.md links to departments [13:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=838s), [14:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=841s).
- **Who it's for:** visual people, and explaining systems without walking someone through a file explorer [14:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=846s), [14:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=850s), [14:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=853s).
- **Demo.** The cleanup skill is slow to find in a file explorer, but instant to find and preview in the second brain [14:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=859s), [14:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=862s), [14:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=867s), [14:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=871s).
- He never names the viewer software. Compare [[Second Brain Levels]].

### [14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s) Part 3 - Routines

- **Why third:** only after mastering skills and memory do you trust the agent to work unmonitored [14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s), [14:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=880s), [14:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=884s). Routines are just scheduled tasks [14:47](https://www.youtube.com/watch?v=8NSyI-npJCU&t=887s).

**Level 1: local routines in the desktop app**

- Built into Claude Code: open Routines in the desktop app's left sidebar and draft routines in natural language [14:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=891s), [14:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=896s), [14:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=898s), [15:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=901s).
- **What a routine is:** a prompt Claude sends itself at the time you set [15:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=913s), [15:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=917s).
- **Example: "YouTube to Substack daily" at 8:00 a.m.** [15:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=905s), [15:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=909s)
  - It turns any new channel video into a newsletter draft in his voice [15:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=921s), [15:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=923s), [15:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=927s).
  - The output lands as an artifact in his OS with several drafts to review; for example, for his "6 New Rules of Claude Code" video [15:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=929s), [15:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=932s), [15:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=936s), [15:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=940s).
  - Because it uses a custom skill, he's 70–80% confident the draft is on-voice and needs only minor edits [15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s), [15:47](https://www.youtube.com/watch?v=8NSyI-npJCU&t=947s), [15:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=951s).
- **The limitation.** He keeps only a few local routines, because they run only while the computer is on [15:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=956s), [16:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=961s), [16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s). See Beyond the source for current options.

**Level 2: cloud scheduling on an always-on agent**

- **Most of his routines live here:** in the cloud, so they run with his computer off [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s), [16:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=972s), [16:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=976s).
- **Options he names:** OpenClaw (probably popularised the idea) [16:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=980s); "Grockbot", likely xAI's Grok Bot, new but pricey [16:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=981s), [16:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=985s); and Hermes, which he uses [16:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=988s).
- **Why Hermes.** It's always on because most users give it its own computer; his is in the cloud [16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s), [16:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1004s), [16:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1008s). Most scheduled tasks on his firing board run in Hermes [16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s), [16:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1017s).
- **The step most people miss.** Hermes on its own computer can't reach the skills and context built up in Claude Code [17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s), [17:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1023s), [17:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1026s).
  - His fix, and his suggestion for beginners, is Syncthing: free, open-source software that syncs files between computers [17:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1030s), [17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s), [17:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1038s).
  - Point it at the Claude Code workspace, install it on Hermes's computer, and sync the skills and memory files you choose [17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s), [17:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1049s), [17:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1053s).
  - One on-screen prompt starts it [17:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1059s).
- See [[Sync a Workspace to an Always-On Cloud Agent]], [[Port a Claude Code Brain to Other Agents]] and [[Tool-Agnostic Context Files]].

**Level 3: Claude Code on a VPS**

- **Coming soon by default, he thinks** [17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s), [17:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1066s).
- **The setup.** Some users rent a VPS (a computer in the cloud) and install Claude Code there, so all files and context live on it [17:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1069s), [17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s), [17:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1078s), [18:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1082s).
- **Best of both:** routines that run 24/7 [18:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1085s), [18:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1087s); one platform, Claude Code or Codex [18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s), [18:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1094s); no sync tool [18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s).
- **His prediction.** Anthropic and OpenAI will likely offer this, but file storage and security concerns put it in the near future rather than now [18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s), [18:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1106s), [18:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1108s). See [[Always-On Brain OS]], and Beyond the source for what exists today.

### [18:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1113s) Part 4 - Apps

- Real work with agents means connecting to your apps [18:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1115s), [18:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1118s).
- **Level 1: the directory.** In the Claude Code desktop app, browse Customize → Connectors [18:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1122s), [18:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1126s), [18:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1128s).
- **Level 2: let Claude Code find connectors.** Browsing yourself is inefficient, he says; have Claude Code search for and connect apps instead [18:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1134s), [18:59](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1139s), [19:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1143s).
  - **His search-connectors skill** checks the web for an official connector [19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s), [19:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1152s). Failing that, it looks for community ones [19:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1156s) in the three usual formats: CLIs, APIs and MCPs [19:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1160s), [19:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1163s), [19:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1165s).
  - **Demo: Adobe Premiere.** It checked for an official Adobe connector and community options, then recommended an open-source GitHub repo [19:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1172s), [19:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1176s), [19:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1180s).
  - **Safety step.** He then asks Claude Code, in the same session, to check the repo is safe and set it up [19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s), [19:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1188s), [19:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1190s). No method is shown.
  - See [[Connecting Claude to External Tools]] and [[Permissions and Approval Gates]].
- **Level 3: build your own connectors and apps** [19:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1193s), [19:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1197s).
  - **Connectors.** He uses CLI Printing Press by Matt Van Horn, whom he calls a Lyft co-founder [20:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1201s), [20:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1203s). He covers it in a separate video [20:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1207s). He made connectors for MyFitnessPal and Skool, which had none [20:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1211s), [20:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1215s), [20:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1217s).
  - **Apps.** The dashboard itself [20:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1224s), plus micro-apps he uses almost daily [20:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1230s):
    - a masonry-grid gallery of all his image and video generations [20:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1234s), [20:38](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1238s)
    - the second brain [20:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1243s)
    - a landing pad for the Excalidraw-style illustration artifacts Claude makes [20:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1246s), [20:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1249s), [20:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1251s)
  - He encourages building apps yourself to see what agentic platforms can do [20:59](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1259s), [21:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1262s).

### [21:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1266s) Wrap up

- That's the whole ARMS framework [21:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1266s). Send his PDF, which holds every prompt, to Claude Code to build a similar OS for yourself or a client [21:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1273s), [21:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1276s), [21:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1279s).

## Caveats & disagreements

### Limits of this video

- **Title hype.** ARMS is his own framework, one of many ways to organise an OS [03:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=233s), [03:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=238s). Nothing in it is specific to Claude 5 models. The "99%" lines are claims, not evidence [00:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=26s), [04:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=254s).
- **Result, not build.** Every starter prompt is on screen only: skill refactor [09:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=540s), `claude -p` integration [10:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=627s), routers [13:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=814s), Syncthing [17:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1059s). He says they're in his PDF [21:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1273s). He opens the /cleanup SKILL.md, the brand HTML and the content.md router on screen [07:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=426s), [07:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=475s), [12:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=769s), but the narration never walks through their text or any routine prompt; the only concrete command spoken is `/cleanup` via `claude -p` [09:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=598s).
- **Unreviewed commands.** The /cleanup skill came from a social media post [06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s) and is called effective without explaining what it runs [06:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=390s). Review commands like that line by line before running them, especially behind a one-click button [09:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=556s). See [[Permissions and Approval Gates]] and [[Configure Safe Autonomy Permissions]].
- **Thin safety step.** The connector safety scan is a single sentence with no criteria [19:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1188s).
- **Unmeasured numbers:** the 20–30% vs 70% value split [03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s), the 60,000-file cost to retrieval and usage [11:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=681s), and 70–80% confidence in routine drafts [15:47](https://www.youtube.com/watch?v=8NSyI-npJCU&t=947s).
- **Dated routines framing.** He says desktop routines stop when the computer is off [16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s), so cloud scheduling needs an outside agent [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s), and Anthropic hosting is still to come [18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s). Current docs say the desktop Routines page creates both Local tasks and Cloud routines, and Cloud routines run with the computer off. His VPS argument still partly holds, because cloud routines start from a fresh repo clone with no persistent local workspace (see Beyond the source). [[Claude Managed Agents]] is another hosted Anthropic option that partly meets his prediction, though it's a developer API and doesn't sync your workspace.
- **Loose credit.** Matt Van Horn co-founded Zimride, which later became Lyft [20:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1205s).
- **Promotion omitted:** a paid-community pitch (02:50–03:22), a course plug (16:31), and the description's gated guide, product plug and affiliate links.

### Conflicts with existing vault notes

- **Agent-first naming vs "could you find it too?".**
  - **Jay:** agents operate on the files, so naming and file-explorer navigability matter much less, and router files do the work [12:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=722s), [12:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=734s). Humans find things through his visual second brain [14:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=867s).
  - **Nate:** [[CLAUDE.md as a Router]] and [[Design for Retrieval]] use the test from [[Nate Herk - Every Level of a Claude Second Brain]]: can the agent find it, *and could you* [02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s). He wants routing that makes sense to both [07:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=422s).
  - **Where that leaves it.** Both put routers first; they split on whether the folder layout itself must serve humans. *Inference (not either creator's words):* Jay's approach relies on the viewer app existing and staying current.
- **A competing memory ladder.**
  - **The ladders.** Jay goes flat workspace → routers once retrieval slows [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s) → visual second brain [13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s). [[Second Brain Levels]] (Nate) starts every brain with a router at Level 1 [04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s), then adds wiki, semantic, graph and always-on tiers that Jay's ladder lacks.
  - **On visuals.** Jay makes the visual layer the top memory level [13:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=830s), [14:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=846s). Nate calls graph views the hook, not the value, and Obsidian only a viewer [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s), [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s), [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s). Jay's own 20–30% estimate for the interface narrows the gap [03:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=213s).
- **[[Always-On Brain OS]].** Jay treats cloud scheduling as needing an external agent [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s). Nate says that in Claude Code you'd manage the crons yourself [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s). That note's Beyond the source already records Cloud Routines, and today's docs confirm them.
- **[[Port a Claude Code Brain to Other Agents]]: a refinement.**
  - **Jay adds** the cross-machine step: Syncthing to a cloud Hermes computer [17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s).
  - **He omits** (each checked under Beyond the source):
    - Hermes reads AGENTS.md before CLAUDE.md.
    - Claude Code auto memory lives outside the workspace, so folder sync doesn't carry it.
    - Hermes cron jobs need a working directory to load the router.
- **[[Hermes Agent]].** Not a disagreement: Nate is experimenting with Hermes, while Jay runs most of his scheduled tasks on it [16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s).
- **[[Context vs Connections]]: terminology only.** Nate's "connections" are volatile data kept reachable; Jay's connectors (CLI, API, MCP) are how you reach them [19:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1163s). Cross-link the notes, but keep the two terms distinct.

### How other sources compare

- **Agreement: [[Chase AI - The Agentic OS Setup for Claude Code]].** Chase also puts the value under the hood, about 90% in his first two levels [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s). He also wires dashboard buttons to headless `claude -p` skill runs [27:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1644s), [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s).
- **Tension: [[Ras Mic - How AI Agents and Claude Skills Work]].** Jay starts people on pre-built skills [05:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=342s) and installs a community connector repo after a scan [19:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1180s), [19:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1188s). Ras Mic doesn't install others' skills: he mines them for ideas, calls downloads an easy attack route, and says skills need your own successful run [12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s). Jay's pre-built skills are Anthropic's own and his community item is a connector, but the trust question is the same. See [[Build vs Install Third-Party Skills]].
- **Compatible on CLAUDE.md size.** Ras Mic warns that CLAUDE.md/AGENTS.md content costs tokens every turn [04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s), [04:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=264s). Jay's CLAUDE.md only names departments and pushes detail into department routers and skills [12:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=748s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s). See [[Keep CLAUDE.md Lean]].
- **Agreement: [[AI LABS - Claude Design Skills for Beautiful Sites]].** Jay's point that visual references work especially well in design skills [08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s) matches the reference-grounded skills AI LABS favour, such as web-design-engineer's design references ([04:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=274s)) and tastemaker's script-based extraction of exact design details ([10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)). See [[Escaping the Default AI Design Look]].
- **Same scheduling end point.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] also moves from desktop scheduled tasks [12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s) to VPS hosting for always-on sessions [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s), matching Jay's Routines Level 3 [17:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1069s).

## Build from this

1. **ARMS self-audit skill.** Score a workspace's skills, routers, routines and connectors against the three levels in the table, then output the next upgrade for each, bottom-up [04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s). See [[Agentic OS]] and [[Second Brain Pain-Point Audit]].
2. **Prompted-twice capture.** Log repeated requests. On the second repeat [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s), turn the successful run into a skill with skill-creator [05:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=352s). See [[Workflow Audit into Skills]] and [[Build a Skill from a Successful Run]].
3. **Thick-skill refactor.** Split stuffed SKILL.md files into a short router plus reference files [08:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=531s), and re-test each one. See [[Build a Reference-Rich Skill]] and [[Skill Improvement Loop]].
4. **Brand design-system skill.** A SKILL.md routing to a brand HTML file (fonts, palettes) and other visual references, so on-brand assets take one or two prompts [07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s), [08:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=522s). See [[Build a Reference-Rich Skill]].
5. **Skills deck.** A dashboard widget over an allowlist of skills: pick model and effort, run `claude -p "/skill-name"`, and save each run's report [01:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=76s), [09:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=570s), [09:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=589s). Add explicit permission flags and a spend cap (Beyond the source). See [[Build an Agentic OS Dashboard]] and [[Configure Safe Autonomy Permissions]].
6. **Department routers.** CLAUDE.md names departments. Each department file lists its skills and references, and a link check confirms the paths exist [12:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=748s), [12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s). See [[Build a Level 1 Second Brain]], [[Tiered Lookup Routing]] and [[Keep CLAUDE.md Lean]].
7. **Workspace bloat check.** Count files by folder and type to spot generated or vendor folders slowing agent search, the kind of thing his 60,000-file moment revealed [11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s). See [[Design for Retrieval]].
8. **Voice-matched content routine.** Daily drafts of a newsletter from each new video using a voice skill, saved as a reviewable artifact [15:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=905s), [15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s). Pick local or cloud using Beyond the source. See [[Schedule Recurring Claude Tasks]].
9. **Hermes + Syncthing bridge.** Sync chosen folders (skills, routers, a relocated memory folder) to an always-on Hermes machine [17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s). Ignore secrets and build output, and set each cron job's working directory. See [[Sync a Workspace to an Always-On Cloud Agent]] and [[Port a Claude Code Brain to Other Agents]].
10. **Search-connectors skill with a real gate.** Official first, then community CLI, API or MCP [19:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1152s), [19:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1163s). Before setup, run a documented review (install scripts, network calls, credentials, maintenance) and require approval [19:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1188s). See [[Connecting Claude to External Tools]] and [[Permissions and Approval Gates]].
11. **Artifacts ring.** Index HTML, PDF and image artifacts by client, project and date, with search and preview [01:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=100s), [01:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=110s). See [[Build an Agentic OS Dashboard]].

## Resources mentioned

- **His 9-page PDF guide** with all the on-screen prompts, linked from the description [05:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=311s), [21:13](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1273s)
- **His separate CLI Printing Press video** [20:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1207s) and **other Hermes tutorials** on his channel [16:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=989s); neither is linked in the captions
- **His earlier video "6 New Rules of Claude Code"**, the routine example [15:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=934s)
- **Tools and products named:**
  - Agents: Claude Code (desktop app, `claude -p`, Routines), OpenAI Codex, Hermes Agent, OpenClaw, Grok Bot
  - Claude desktop app: Customize → Skills and Customize → Connectors; Anthropic's skill-creator
  - Sync and connectors: Syncthing; CLI Printing Press (Matt Van Horn)
  - Example apps: Adobe Premiere, MyFitnessPal, Skool, Substack, X, GitHub; Excalidraw-style illustrations

## Beyond the source

*Not said in the video. Added at ingest and checked at the links given.*

- **Routines today (corrects his Level 1/2 framing).**
  - **Where:** the desktop app's Code tab → Routines → New routine, then choose **Local** or **Cloud**.
  - **Local** tasks use your files. They fire only while the app is open and the computer is awake: missed runs are skipped, and one catch-up run happens on wake. There's a Keep computer awake setting, and permission mode is set per task.
  - **Cloud** routines run on Anthropic infrastructure with the computer off, and can also fire on API calls or GitHub events.
    - Each run uses a fresh clone of your selected repos: no local files, a one-hour minimum interval, no permission prompts.
    - All your connectors are included by default, and their tools (including writes) are usable without asking, so trim them.
    - Research preview; Pro, Max, Team and Enterprise plans.
  - Sources: [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Routines](https://code.claude.com/docs/en/routines)
- **`claude -p` for a skills deck.**
  - **Skills work:** put `/skill-name` in the prompt and Claude Code expands it. Set the model with `--model` and effort with `--effort` (`low`–`max`, model-dependent).
  - **Permissions:** `-p` starts in Manual mode, so pass `--allowedTools` or `--permission-mode`, plus `--permission-prompts none` for unattended runs.
  - **Caps:** `--max-turns` and `--max-budget-usd`. `--output-format json` adds an estimated `total_cost_usd`.
  - **Trust:** without `--bare`, a run loads that folder's hooks and `.mcp.json` servers with no trust dialog, so only point it at trusted folders.
  - **Don't use `--bare`:** it skips skill discovery and CLAUDE.md.
  - Sources: [Headless docs](https://code.claude.com/docs/en/headless), [CLI reference](https://code.claude.com/docs/en/cli-reference)
- **Reference-rich skills are the documented pattern.**
  - Keep SKILL.md under 500 lines and move detail into supporting files. SKILL.md should say what each file holds, so Claude loads files only when needed.
  - Anthropic's skill-creator builds, edits, evaluates and benchmarks skills, and tunes descriptions for triggering. It organises resources into `scripts/`, `references/` and `assets/`.
  - Sources: [Skills docs](https://code.claude.com/docs/en/skills), [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- **Connectors and trust.**
  - The unified directory opens via Customize → Connectors → "+" → Browse connectors. It lists verified and community MCP servers, and one catalog serves Claude.ai, Desktop, mobile, Cowork and Claude Code.
  - Verified means Anthropic tested a connector for quality and compatibility, but that isn't a security audit. Community connectors are only screened before listing.
  - Claude Code's MCP docs say to verify you trust each server before connecting, and flag prompt-injection risk from servers that fetch external content.
  - Sources: [Directory help article](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory), [Connectors directory docs](https://claude.com/docs/connectors/directory), [Connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities), [MCP docs](https://code.claude.com/docs/en/mcp)
- **Hermes cron and your router.**
  - Jobs run in isolated sessions and need the gateway daemon running.
  - By default they ignore AGENTS.md and CLAUDE.md. Setting `workdir` injects context files from that folder, and jobs can also preload skills.
  - Hermes loads one project context-file type, and AGENTS.md comes before CLAUDE.md.
  - Sources: [Hermes cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron), [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- **Syncthing and memory.**
  - Syncthing is open-source, continuous file sync between two or more computers, with all traffic secured by TLS. Exclusions go in a root `.stignore`, which never syncs itself; `#include` can share patterns. Use it to keep `.env` files, credentials, caches and build output off the remote machine.
  - Claude Code auto memory lives at `~/.claude/projects/<project>/memory/` unless `autoMemoryDirectory` moves it, so workspace sync alone won't carry it.
  - Sources: [syncthing.net](https://syncthing.net/), [Ignoring files](https://docs.syncthing.net/users/ignoring.html), [Claude Code memory](https://code.claude.com/docs/en/memory#auto-memory)
- **CLI Printing Press.**
  - It generates an agent-first Go CLI and an MCP server from an OpenAPI spec, a website URL or a HAR capture of browser traffic. It's driven by Claude Code skills such as `/printing-press <app-name>` and is MIT-licensed.
  - Matt Van Horn co-founded Zimride, which renamed itself Lyft in 2013.
  - Sources: [GitHub](https://github.com/mvanhorn/cli-printing-press), [Matt Van Horn](https://en.wikipedia.org/wiki/Matt_Van_Horn), [Zimride](https://en.wikipedia.org/wiki/Zimride)
- **Grok Bot.** xAI launched it on 11 August 2026: always-on agents with their own cloud computers. It launched in beta, available through SuperGrok Heavy, Cursor Ultra ($200/month) or Cursor Teams Premium ($120 per seat per month), which fits his remark about a high price point. Source: [Unite.AI](https://www.unite.ai/xai-launches-grok-bot-always-on-ai-teammates-with-their-own-cloud-computers/)
- **OpenClaw.** An open-source (MIT), self-hosted personal AI assistant with a local gateway and messaging-app channels. Source: [GitHub](https://github.com/openclaw/openclaw)

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Aentic OS" (00:13, 02:22, 15:30) | Agentic OS |
| "Cloud Code", "cloud code" | Claude Code |
| "claw.md", "cloud.md" (12:25, 12:28, 14:01) | CLAUDE.md |
| "Entropic" (05:43, 05:50, 18:24) | Anthropic |
| "Codeex" (06:32, 10:18, 18:14) | Codex (OpenAI Codex) |
| "Cloud Desktop app" (05:46) | Claude desktop app |
| "Claude P" (09:47), "cloud hyphen P" (10:24) | `claude -p` (print / headless mode) |
| "/cleup" (10:02) | /cleanup |
| "skill.mmd" (07:37) | SKILL.md |
| "Robbernuggets" (02:57) | RoboNuggets |
| "Grockbot" (16:21) | likely xAI's Grok Bot |
| "Sync Thing" (17:15) | Syncthing |
| "Matt VH", described as Lyft's co-founder (20:05) | Matt Van Horn (co-founded Zimride, which became Lyft) |
| "my fitness pal" (20:15) | MyFitnessPal |
| "school" (20:17) | Skool (likely) |
| "excal illustrations" (20:46) | Excalidraw-style illustrations (likely) |
| "six new rules of cloud code" (15:34) | his earlier video "6 New Rules of Claude Code" (likely) |
| "THRO" (01:52), "Beto Green" (02:39) | client names, *unclear in captions* |
| "Robo" folder (10:52) vs "/robo" skill (07:20) | two things: his workspace folder and his brand design-system skill |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Agentic OS]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[CLAUDE.md as a Router]] · [[Design for Retrieval]] · [[Second Brain Levels]] · [[Always-On Brain OS]] · [[Tool-Agnostic Context Files]] · [[Context vs Connections]] · [[Routines and Scheduled Tasks]] · [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[LLM Wiki]] · [[Escaping the Default AI Design Look]]
- **Techniques:** [[Build an Agentic OS Dashboard]] · [[Workflow Audit into Skills]] · [[Build a Skill from a Successful Run]] · [[Build a Reference-Rich Skill]] · [[Skill Improvement Loop]] · [[Build a Level 1 Second Brain]] · [[Keep CLAUDE.md Lean]] · [[Tiered Lookup Routing]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Port a Claude Code Brain to Other Agents]] · [[Configure Safe Autonomy Permissions]] · [[Ingest Sources into an LLM Wiki]] · [[Second Brain Pain-Point Audit]]
- **Tools:** [[Claude Code]] · [[Hermes Agent]] · [[Syncthing]] · [[OpenClaw]] · [[OpenAI Codex]] · [[Obsidian]] · [[Claude Managed Agents]]
- **People:** [[Jay E]] · [[Nate Herk]] · [[Chase AI]] · [[Ras Mic]]
- **Other sources:** [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Nate Herk - Every Level of a Claude Second Brain]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[AI LABS - Types of Claude Loops Explained]] · [[Simon Pittman - Set Up Claude Cowork]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Anthropic - What Is Claude Managed Agents]] · [[AI LABS - Claude Design Skills for Beautiful Sites]]
