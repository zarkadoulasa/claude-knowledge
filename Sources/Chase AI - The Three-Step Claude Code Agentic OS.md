---
type: source
title: "Stop Using Claude Code Without an Agentic OS"
creator: "[[Chase AI]]"
channel: "Chase AI"
url: https://www.youtube.com/watch?v=Bgxsx8slDEA
video_id: Bgxsx8slDEA
published: 2026-05-05
duration: "17:29"
ingested: 2026-09-15
topics: [agentic OS, voice brain-dump interview, selective automation, local vs remote automations, Obsidian vault, vault CLAUDE.md, observability dashboard, headless claude -p]
tags: [source/youtube, topic/agentic-os, topic/skills, topic/automation, topic/scheduling, topic/memory, topic/second-brain, topic/rag, topic/claude-code, topic/teams, topic/permissions]
---

# Chase AI - The Three-Step Claude Code Agentic OS

> **Creator:** [[Chase AI]] · **Published:** 2026-05-05 · **Length:** 17:29 · [Watch on YouTube](https://www.youtube.com/watch?v=Bgxsx8slDEA)

## TL;DR

This is an earlier, shorter version of the framework in [[Chase AI - The Agentic OS Setup for Claude Code]] (2026-06-25). That note covers what the two videos share; this one records only the differences. Here the [[Agentic OS]] has three steps instead of four levels:

1. **Architecture**, where he says the value lies. A spoken brain dump turns into domains, tasks, skills and a few automations, each run locally or remotely.
2. **Memory.** An [[Obsidian]] vault plus a CLAUDE.md that states the system's purpose and maps its memory.
3. **Observability.** Usage and activity panels, and buttons that run skills through `claude -p`, mainly for teammates and clients.

## Key takeaways

- **Start with a spoken brain dump.** Dictate the discrete tasks in your day. Claude then asks, task by task, whether each should become a skill and then an automation [05:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=312s).
- **Automate selectively.** A morning trend scan is worth automating; deep research isn't [05:40](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=340s).
- **CLAUDE.md has two jobs.** It sets out purpose and behaviour [11:32](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=692s), and it maps memory so Claude follows the layout and spends fewer tokens [11:55](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=715s).
- **Observability is a layer of its own.** His panels show 5-hour and weekly usage windows, routines used today, recent vault changes and forecasts [14:55](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=895s).
- **Buttons are for other people:** AI agency work and teams who won't touch a terminal [14:27](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=867s). Anyone fluent in the terminal, VS Code or the desktop app gains little [14:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=858s).

## Three steps vs four levels

| This video | June equivalent | What differs here |
|---|---|---|
| **1. Architecture** [00:59](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=59s) | Level 1 | Voice interview only. No session mining, validate-first step or loops. Adds the local vs remote choice [04:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=241s) |
| **2. Memory** [07:29](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=449s) | Level 2 | Obsidian as a middle ground short of RAG [10:57](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=657s). Option of one folder per domain [10:34](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=634s). No per-folder index.md or run logs. Folders at the time: archive, content, ops, personal, projects, raw, wiki [12:17](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=737s) |
| **3. Observability** [12:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=774s) | Levels 3–4 | Merged into one layer. The dashboard prompt starts from placeholders [15:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=947s). No Obsidian plugin, handoff mechanics or billing note |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=0s) Intro

- **Slot machine vs system.** Random prompts on random tasks give random results [00:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=0s). The fix is a chain: workflows become skills, skills become automations, automations become architecture, all wrapped in memory and observability [00:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=18s).

### [00:37](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=37s) Step 1: Architecture

- **The value is in this step, not the dashboard** [01:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=74s). It pays off even on its own [03:19](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=199s).
- **His domains:** memory, productivity, research, content and community [01:59](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=119s).
- **His research tasks:** YouTube lookups, deep research, LightRAG work, a morning report and competitor watching [02:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=138s).
- **Simple tasks count.** Rather than searching YouTube by hand, a skill returns a complete report every time [02:39](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=159s). Deep research is the complex end [02:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=167s).
- **Deep research skill.** It searches X, GitHub, the web, YouTube and earlier Obsidian entries, then consolidates what it finds [02:53](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=173s).
- **Morning trend scan, his worked automation.** Every morning it writes into his Obsidian vault a scan of what's happening in AI and among his competitors on YouTube, GitHub and elsewhere, which he calls an easy automation win [03:50](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=230s).
- **The interview** (prompt paywalled [04:58](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=298s)). For each task, Claude builds a skill with skill-creator, then decides whether it needs an automation and whether that runs locally or remotely [05:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=351s). It works through every domain this way [06:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=360s). See [[Workflow Audit into Skills]].
- **Codified means handable.** Once everything is a skill, a teammate who would never use Claude Code can use the system, and you can set it up for clients, package it and sell it [06:49](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=409s)–[07:04](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=424s).

### [07:31](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=451s) Step 2: Memory

- **Obsidian.** It's a free interface over markdown, and the value comes from the file structure [07:56](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=476s). Start the terminal inside the vault [08:48](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=528s).
- **Folders.** See [[LLM Wiki]] and [[Ingest Sources into an LLM Wiki]].
  - `raw/` is a staging dump [09:17](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=557s).
  - `wiki/` holds articles written from raw material [09:24](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=564s).
  - `output/` holds deliverables such as slide decks [10:04](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=604s).
- **CLAUDE.md is mandatory** [11:22](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=682s). You should be able to navigate the structure too [12:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=732s). See [[CLAUDE.md as a Router]] and [[Design for Retrieval]].
- **Memory makes tracking and optimising possible** [12:41](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=761s). See [[Agent Memory Patterns]].

### [12:53](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=773s) Step 3: Observability

- **Buttons** trigger the skills and automations you actually use [13:07](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=787s). See [[Build an Agentic OS Dashboard]].
  - The deep research button asks for a topic [13:27](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=807s).
  - It then runs a headless `-p` instance [13:45](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=825s).
  - The report it returns links its sources and its Obsidian note [15:35](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=935s).
- **Choosing panels.** They can show anything, but ideally tie back to your skills [15:10](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=910s). Ask what you wish the terminal showed you. Adding a panel takes one prompt [15:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=914s). See [[Context Window Management]].

### [16:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=974s) Overview

- **You need to see the data too.** It isn't enough for only Claude to know where data lives [16:42](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1002s). Teammates and clients never have to touch a terminal [16:55](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1015s).

## Caveats & disagreements

- **Self-promotion.** This note leaves out a "sponsor" read for his own course and paid community (04:31–04:53) and an outro plug (17:18).
- **Unmeasured claims.**
  - Three steps put you "ahead of 99%" of users [00:34](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=34s).
  - 99.9% of people need neither LightRAG nor a vector database [11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s). Yet LightRAG work is one of his own research tasks [02:22](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=142s).
- **CLAUDE.md isn't "appended to every prompt"** [11:45](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=705s). It loads at session start and stays in context (Beyond the source). The vault makes the same correction for [[Ras Mic - How AI Agents and Claude Skills Work]].
- **Local vs remote is left to Claude** [04:05](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=245s). His trend scan writes to a local vault [03:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=227s), and cloud routines can't reach local files (Beyond the source). See [[Routines and Scheduled Tasks]].
- **No permissions or privacy guidance.**
  - The deep research button passes typed input into an unattended run [13:27](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=807s). [[Build an Agentic OS Dashboard]] allows that only with a length cap, stripped control characters, and read-only tools plus a report folder.
  - Client data goes unmentioned [07:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=421s).
  - See [[Permissions and Approval Gates]].

**Conflicts with vault notes**

- **Validate first?** Here, Claude codifies each task straight away [05:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=351s). His June video [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s) and [[Build a Skill from a Successful Run]] both say to do the task by hand first.
- **[[Second Brain Levels]].** Chase says plain markdown is enough [11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s). [[Nate Herk - Every Level of a Claude Second Brain]] adds retrieval levels when a real pain appears [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s).
- **[[Context vs Connections]].** Chase puts daily trend scans into the vault [03:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=227s). Nate's one-year evergreen test would keep them out [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s).
- **Who buttons serve.** Chase says fluent users gain little [14:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=858s). [[Jay E - The ARMS Framework for a Claude Agentic OS]] keeps his own cleanup skill on his dashboard [09:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=552s).
- **Human navigability.** [[CLAUDE.md as a Router]] files his June video as "in between". Here he sides with Nate: you must be able to see where data lives [16:42](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=1002s), against Jay E's agent-first naming [12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s).
- **[[LLM Wiki]].**
  - **Layout.** He credits Karpathy with raw, wiki and output folders [09:03](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=543s). The gist has raw sources, a wiki and a schema file (Beyond the source). But the raw/wiki/outputs split matches coverage of Karpathy's earlier X post; only a separate output folder looks like Chase's own addition (see [[LLM Wiki]]).
  - **Is it RAG?** He calls it "RAG" in air quotes [08:19](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=499s), then places Obsidian short of full RAG [10:57](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=657s).
- **[[Agentic OS]] and [[Obsidian]].** Three steps here, four levels in June. Obsidian is recommended here [10:57](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=657s) but optional in June [13:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=821s).

## Build from this

1. **Voice architecture interview.** Follow [[Workflow Audit into Skills]], but only codify a task after a good run ([[Build a Skill from a Successful Run]]).
2. **Automation triage.** Use [[Schedule Recurring Claude Tasks]]. *Vault starter rule:* automate only recurring work that needs no judgement call.
   - Needs local files or apps: use a Desktop task on an awake machine.
   - Needs only a repo: use a cloud routine.
3. **Vault CLAUDE.md.** See [[Build a Level 1 Second Brain]] and [[Keep CLAUDE.md Lean]]. *Vault starter content:*

```markdown
## Purpose
My agentic OS for <domains>. Prefer an existing skill over ad-hoc work.

## Memory map
- raw/     unprocessed dumps (research, scans)
- wiki/    one article per topic, built from raw/
- output/  deliverables by type (decks/, briefs/)
New material lands in raw/; only settled findings move to wiki/.
```

4. **Panels and buttons.** Build with [[Build an Agentic OS Dashboard]] and [[Configure Safe Autonomy Permissions]]. Read the usage windows from status-line data (Beyond the source).

## Resources mentioned

- The skill-creator skill [05:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=351s)
- `claude -p` [13:49](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=829s)
- Obsidian [07:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=467s)
- LightRAG and vector databases, named only to dismiss them [11:05](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=665s)

## Beyond the source

*Not in the video. Checked 2026-09-15.*

- **CLAUDE.md** loads at every session start, as a user message after the system prompt. https://code.claude.com/docs/en/memory
- **`claude -p`** starts in Manual permission mode; pre-approve tools with `--allowedTools`, and `--permission-mode dontAsk` denies anything else that would prompt. A `/skill-name` in the prompt is expanded. Without `--bare`, the run executes the folder's hooks and `.mcp.json` servers with no trust dialog. https://code.claude.com/docs/en/headless
- **Usage windows.**
  - Pro and Max limits are shared between Claude and Claude Code. https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
  - Settings → Usage shows the five-hour and weekly limits. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
  - For Pro and Max subscribers, after the session's first response, status-line JSON includes `rate_limits.five_hour` and `rate_limits.seven_day`, each with `used_percentage` and `resets_at`. https://code.claude.com/docs/en/statusline
- **Local vs remote.** Desktop tasks need the machine on and can read local files. Cloud routines run from a fresh clone with no local files, at intervals of at least one hour. https://code.claude.com/docs/en/scheduled-tasks
- **Karpathy's gist** has raw sources, a wiki and a schema file, but no output folder. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Karpathy's earlier X post**, as summarised secondhand, has raw data, a wiki and outputs such as Marp slide decks and charts, filed back into the wiki rather than kept in a separate folder. https://academy.dair.ai/blog/llm-knowledge-bases-karpathy
- **Chase's companion blog post**, from the same day, lists what CLAUDE.md should hold: purpose, folder structure, note conventions, and how to handle material dropped in raw. It calls local automations cron jobs and remote ones server-run, and estimates a couple of hours of work. It skips button security. https://www.chaseai.io/blog/build-claude-code-agentic-os-3-steps

## Transcript notes

| Caption | Corrected |
|---|---|
| "Carpathia", "Andre Karpathy" | Andrej Karpathy |
| "light rag" | LightRAG |
| "Egentic OS", "Agent Go S" | agentic OS |
| "Claude at MD" | CLAUDE.md |
| "dash P flag" | `claude -p` |
| "Chase AI Plus" | Chase AI+, his paid community |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Agentic OS]] · [[Routines and Scheduled Tasks]] · [[LLM Wiki]] · [[CLAUDE.md as a Router]] · [[Second Brain Levels]] · [[Context vs Connections]]
- **Techniques:** [[Workflow Audit into Skills]] · [[Build an Agentic OS Dashboard]] · [[Bootstrap an LLM Wiki from the Karpathy Gist]]
- **People:** [[Chase AI]] · [[Andrej Karpathy]] · [[Nate Herk]] · [[Jay E]]
- **Sources:** [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]
