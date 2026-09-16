---
type: source
title: "The Agentic OS Setup That Will 10x Claude Code"
creator: "[[Chase AI]]"
channel: "Chase AI"
url: https://www.youtube.com/watch?v=HRw-vP0j8OM
video_id: HRw-vP0j8OM
published: 2026-06-25
duration: "31:20"
ingested: 2026-09-15
topics: [agentic OS, workflow audit, skills, automations, routines, loop engineering, memory and state, Obsidian vault structure, nested index files, CLAUDE.md navigation pattern, headless claude -p, dashboards, Obsidian plugin, distribution to teams and clients]
tags: [source/youtube, topic/agentic-os, topic/skills, topic/automation, topic/loops, topic/scheduling, topic/memory, topic/second-brain, topic/retrieval, topic/claude-code, topic/teams, topic/permissions]
---

# Chase AI - The Agentic OS Setup for Claude Code

> **Creator:** [[Chase AI]] · **Published:** 2026-06-25 · **Length:** 31:20 · [Watch on YouTube](https://www.youtube.com/watch?v=HRw-vP0j8OM)

## TL;DR

Chase (Chase AI) argues that an agentic OS for [[Claude Code]] is worth building for what sits under the hood, not for the dashboard. He splits it into four levels:

1. **Skills and loop engineering (the backbone).** Audit the work you repeat, turn it into skills, schedule the skills that recur, then add self-improvement loops.
2. **Memory and state.** A coherent file structure, shown with an [[Obsidian]] vault, gives Claude a map. His version uses Karpathy-style raw/wiki/outputs folders, an index.md in every folder, and a vault CLAUDE.md that describes the structure and a navigation pattern. Run logs live in the same place so loops can learn from past runs.
3. **Interface.** A custom web app or Obsidian plugin shows chosen metrics, and its buttons run skills through headless `claude -p`.
4. **Distribution.** The same interface is handed to non-technical teammates and clients, who press buttons instead of learning the terminal.

He puts about 90% of the value in Levels 1 and 2 and says both work in a plain terminal or in Codex. Levels 3 and 4 are a showcase of finished builds: he walks through no code, config or prompt files for them.

## Key takeaways

- **The value is under the hood, not in the visuals.** Loop engineering, skill architecture, state management and a second brain are the point; a dashboard is a wrapper [00:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=4s), [00:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=14s). What you learn carries over to any Claude Code project [00:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=29s). See [[Agentic OS]].
- **Four levels, with the weight at the bottom.** He claims Levels 1–2 hold about 90% of the value [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s) and calls Levels 3–4 the cherry on top [30:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1826s). Everything below the UI works in a normal Claude Code terminal or the Codex CLI and desktop app [03:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=224s).
- **Start with a workflow audit, not a skill.** Most people can't list the specific outputs they need every day and week [05:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=300s), [05:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=306s). Split your work into domains, list the recurring tasks under each, and treat every one as a skill candidate [06:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=370s), [06:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=395s). See [[Workflow Audit into Skills]].
- **Three ways to find skill candidates:** describe a task you already know [06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s), have Claude mine your recent sessions [07:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=469s), or have Claude interview you about your week [09:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=542s). Mining sessions works from real data rather than guesses [08:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=495s).
- **Validate before you codify.** It's better to do the task by hand, confirm it works, then ask Claude to turn what you just did into a skill [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s). See [[Build a Skill from a Successful Run]].
- **Skill → automation → loop.** Anything repeated often should become a scheduled automation, either by asking Claude Code or through the Routines page in the Claude desktop app [11:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=665s), [11:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=690s). Loops then add self-improvement on top [12:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=728s). See [[Schedule Recurring Claude Tasks]] and [[Loop Engineering]].
- **Structure beats tooling.** Obsidian is optional and a database works too [13:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=821s), [13:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=829s). He claims a coherent file structure alone gets you about 99% of the way [14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s). A flat pile of unlinked files makes Claude slower and costs more tokens [16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s), [16:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=997s). See [[Design for Retrieval]].
- **Put an index.md in every folder.** He says the indexes, not the folder names, are where the power lies, because each folder Claude enters tells it what's inside and where to go next [19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s), [20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s), [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s). See [[LLM Wiki]] and [[CLAUDE.md as a Router]].
- **Log runs where loops can see them.** Skill and automation outputs need to be recorded in the same system, so a loop can review past runs and improve the next one [22:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1356s), [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s). See [[Skill Improvement Loop]].
- **Dashboard buttons are headless Claude Code.** A button runs a skill through `claude -p`, as if you'd typed the slash command in an invisible terminal [27:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1642s), [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s). As of the video, this still drew on his Max plan [28:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1690s). See [[Build an Agentic OS Dashboard]].
- **Dashboards are an adoption lever.** Most people are put off by the terminal and even the desktop app. Buttons or voice let teammates and clients use your skills without learning Claude Code [24:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1472s), [29:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1789s), [30:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1806s).

## The four levels at a glance

| Level | What it is | Key moves | His weighting | Build notes |
|---|---|---|---|---|
| **1 — Skills & loop engineering** (the backbone) [01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s) | Everything you do in Claude Code codified as a skill or automation [01:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=116s) | Workflow audit (manual, session mining or interview) → skills → automations → loops [04:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=275s), [13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s) | With Level 2, ~90% of the value [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s). Needs no other level [13:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=780s) | [[Workflow Audit into Skills]] · [[Build a Skill from a Successful Run]] · [[Schedule Recurring Claude Tasks]] · [[Loop Engineering]] |
| **2 — Memory & state** [02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s) | A store the OS can draw on (Obsidian or a database), combined with skills so loops can improve themselves [02:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=125s), [02:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=140s) | Open Claude Code in the vault folder [15:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=919s); coherent structure as a map [16:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1004s); index.md at every level [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s); vault CLAUDE.md with structure and navigation pattern [21:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1310s); run logs for loops [22:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1362s) | Structure alone is "99% of the way" [14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s) | [[Design for Retrieval]] · [[LLM Wiki]] · [[Ingest Sources into an LLM Wiki]] · [[CLAUDE.md as a Router]] · [[Tiered Lookup Routing]] |
| **3 — Interface & customisation** [02:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=173s) | A custom visual wrapper over Levels 1–2, web-app or Obsidian based [23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s), [23:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1414s) | Metrics panels [23:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1429s); skill and automation buttons [24:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1444s); Obsidian plugin version [26:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1613s); buttons call `claude -p` [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s) | Cherry on top [30:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1826s); buys customisation [28:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1703s) | [[Build an Agentic OS Dashboard]] · [[Agentic OS]] |
| **4 — Distribution** [03:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=190s) | Share the OS with teammates or clients to raise the floor [03:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=196s), [03:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=200s) | Web version shared via GitHub repo or zip [29:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1748s); Obsidian version set up per person [29:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1761s) | Cherry on top [30:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1826s); big for client work [29:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1780s) | [[Build an Agentic OS Dashboard]] · [[Agentic OS]] |

The numbering is his own. [[Nate Herk - Every Level of a Claude Second Brain]] uses "levels" for five retrieval tiers [03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s), so a Chase Level 2 is not a Nate Level 2. Chase's memory level covers roughly Nate's Levels 1–2 (router and wiki) and never touches semantic search, graphs or auto memory. See [[Second Brain Levels]].

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=0s) Intro

- **The hook.** Falling behind isn't about lacking a flashy dashboard or a Jarvis-style assistant. The value is what you can't see [00:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=4s), [00:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=12s): loop engineering, skill architecture, state management, a second brain, and bundling them into one product fitted to you [00:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=16s).
- The same skills carry over to any Claude Code project, which is why he goes level by level through both how and why [00:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=29s), [00:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=39s).

### [00:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=48s) Agentic OS

- **Two camps, both wrong.** Shown a web-app or Obsidian-based OS [00:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=49s), people either fall for the visuals [01:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=65s) or dismiss them as smoke and mirrors [01:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=74s). Both miss the fundamentals underneath that turn a nice-looking web app into a customised tool for any problem [01:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=84s).
- **Model-agnostic.** He demos Claude Code but says Codex or even a local model would work [01:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=98s).
- **The four levels:**
  - **Level 1, the backbone:** skills and loop engineering, with everything you do in Claude Code codified as a skill or some kind of automation [01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s).
  - **Level 2, memory and state:** a store the OS can draw on (Obsidian or a standard database), combined with your skills and automations to build loops that are somewhat self-improving [02:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=123s), [02:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=140s). His one-line version of loop engineering: record what happens so loops can look at past iterations and improve future runs [02:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=154s). See [[Loop Engineering]].
  - **Level 3, interface and customisation:** getting beyond the terminal and the Claude desktop app, which he calls great but limited in what you can do or configure [02:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=173s), [03:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=184s).
  - **Level 4, distribution:** share the OS with teammates or clients to raise the floor. Level 1–2 work becomes a button or voice command anyone can use without running Claude Code [03:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=190s), [03:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=202s).
- **Where the value is.** Levels 1–2 are about 90% of the value [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), so most of the video goes there. Nail them and you could do all of it in a standard Claude Code terminal, the Codex CLI or the Codex desktop app, on any problem [03:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=224s).

### [04:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=266s) Level 1

**Four sub-phases:** workflow audit, skill creation, automation and loop engineering [04:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=275s). See [[Workflow Audit into Skills]].

**Phase 1: workflow audit**

- **Why audit first.** He calls skills arguably the most powerful thing in Claude Code, because they pin down what Claude does, how, and what it produces [04:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=289s). So first work out which specific outputs you need day to day and week to week. Most people can't say, and even fewer have turned their manual workflows into skills or automations [05:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=300s), [05:09](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=309s).
- **The default pattern** is a manual back-and-forth in the terminal or desktop app, giving the same instructions again and again [05:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=331s). The fix: audit your daily and weekly work and codify it into skills so outputs stay consistent. If you already use skills, do it a hundred times more [05:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=343s), [06:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=362s).
- **Domains, then tasks.** His domains include research, content, his community, his agency and sales [06:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=373s). Under content sit project outlines, video hooks, repurposing and carousels, and each should be a skill [06:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=386s), [06:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=395s). He calls this the easiest way to improve Claude Code [06:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=407s).

**Three ways to surface skill candidates**

| Route | How it works (paraphrased) | Strength / risk | Timestamp |
|---|---|---|---|
| 1. Manual | Explain a task you already know you do; have the skill-creator skill turn it into a skill | Simple, but the process may never have been validated | [06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s), [07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s) |
| 2. Session mining | Ask Claude to review your last 3–20 sessions and list repeated tasks that could become skills | Based on what you actually did, not guesses | [07:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=474s), [08:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=495s) |
| 3. Interview | Give Claude a stream of consciousness about your day and week; it asks about blind spots, then extracts tasks | Draws out work you'd forget to list | [09:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=542s), [09:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=548s) |

- **Validate before codifying (route 1).** Especially if you're new, you probably haven't confirmed how Claude should do the task [07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s). Better: do it by hand, confirm it works, then ask Claude to turn what you just did into a skill [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s). See [[Build a Skill from a Successful Run]].
- **Session mining (route 2).** He says Claude Code can see essentially all your previous sessions, including tool calls and your instructions [07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s).
  - **His prompt, paraphrased:** review our last ten sessions, find tasks we keep repeating that aren't skills yet, and chart each task, the output it should produce and a proposed skill [08:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=504s).
  - Plain language is fine; on screen, Claude starts by locating the session files [08:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=527s), [08:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=532s). His run surfaced tasks such as checking for tool and repo updates for his videos [10:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=646s).
  - Where those files live, and their 30-day retention default, are under Beyond the source.
- **Interview (route 3).** His prompt, paraphrased: state the goal of turning daily and weekly tasks into skills where sensible; open with a stream of consciousness; have Claude turn it into an interview that calls out blind spots until it understands your work and the outcomes you want; then extract tasks for skills and, later, automations [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s). It needn't be fancier than that [10:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=602s). This aims the [[Grill Me Interview Skill]] idea at workflow discovery; see Caveats.
- **The mindset.** Pour as much context about your work into Claude Code as you can and turn it into a checklist, the way you'd onboard a personal assistant with step-by-step instructions [10:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=607s), [10:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=619s). Because they're skills, they become tangible workflows you can inspect and edit until the outputs are dialled in [10:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=638s). See [[Skill Improvement Loop]].

**Phase 3: automation**

- If a skill will be repeated over and over, there's little reason not to automate it: manual task, then codified skill, then automation where it makes sense [11:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=663s), [11:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=675s).
- **Two routes.** Ask Claude Code whether the skill can become an automation [11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s), or use the Claude desktop app [11:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=690s):
  1. Go to Routines and give the routine a name [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s), [11:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=696s).
  2. Set the instructions to run the named skill [11:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=699s).
  3. Pick a schedule [11:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=704s).
- See [[Schedule Recurring Claude Tasks]] and [[Routines and Scheduled Tasks]]. Documented limits of local tasks and cloud routines are under Beyond the source.

**Phase 4: loop engineering**

- He deliberately skims this third layer, pointing to the loop-engineering video he'd posted the day before [11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s), [11:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=713s).
- A skill turned into an automation is the foundation. The open question is whether to add a self-improvement loop to a given automation, which ties into memory and state [11:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=718s), [12:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=725s), [12:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=733s). For loop designs, see [[Loop Engineering]], [[Multi-Agent Review and Scoring Loops]], [[Tests-First Goal Loop]] and [[AI LABS - Types of Claude Loops Explained]].

**Zooming out**

- **The backbone** is codifying your work so Claude Code gives consistent outputs for the tasks you care about [12:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=748s). It has nothing to do with dashboards, which he likes but says aren't where the power is [12:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=763s), [12:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=770s). It applies to any Claude Code use and needs none of the other levels; stacking levels shows how modular the design is [12:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=778s), [13:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=787s).
- **Recap:** audit by one of the three routes, create the skills, ask which can be automated, then decide whether loop engineering fits each case [13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s).

### [13:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=809s) Level 2

**Structure over tooling**

- He uses [[Obsidian]] as the example, but it's optional. People like it because it's free and fairly easy to understand, and anything it does can be done in a traditional database [13:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=817s), [13:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=823s), [13:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=827s).
- More important than either is a coherent file structure. With that alone, and no database or Obsidian, he claims you're about 99% of the way there [13:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=837s), [14:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=846s). See [[Design for Retrieval]].

**Setting up the vault**

- Download Obsidian (free) and designate an existing or new folder as the vault; the first-run dialog offers both [14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s), [14:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=883s). A vault is just a folder (captioned "file") [14:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=890s).
- Decide which folder the OS lives in and what it needs to know about. His example: if one domain is sales, put at least a copy of all your sales data in the vault [14:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=893s), [15:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=908s). This clashes with the vault's evergreen-only guidance; see Caveats and [[Context vs Connections]].
- "Connecting" Claude Code just means opening it inside the vault folder, which he has literally named "the vault" [15:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=917s), [15:27](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=927s).

**Why structure matters: a map for Claude**

- The payoff is Claude giving quick, accurate answers about any file among huge numbers of folders and files [15:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=957s). One folder of millions of unlinked files with no hierarchy leaves Claude struggling, and slow also means more tokens and higher cost [16:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=985s), [16:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=997s).
- **The mental model is a map** [16:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1004s). He shows his vault's graph view: every file and how they connect [16:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1008s). Ideally Claude has a clear path from your question to the file that answers it [16:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1014s). Obsidian is your filing cabinet [17:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1028s).

**The Karpathy-style layout**

- He credits a now-common layout to a tweet by [[Andrej Karpathy]], which he says drew over 20 million views, about structuring an Obsidian knowledge base so models like Claude can reach information quickly [17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s), [17:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1042s). (The post showed about 21.9 million views on 2026-09-15, so his figure holds; see Beyond the source.)
- **Three subfolders under the vault** [17:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1056s):

| Folder | Holds | His example | Timestamp |
|---|---|---|---|
| `raw/` | All unstructured data | A pile of research articles on AI agents | [17:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1063s), [18:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1082s) |
| `wiki/` | Structured data made from the raw material: Wikipedia-style articles | One clear article about AI agents instead of 20 source documents | [17:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1074s), [18:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1093s) |
| `outputs/` | Deliverables built from the structured data | A slide deck on AI agents | [18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s), [18:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1132s) |

- **The flow** is unstructured, then structured, then outputs, which suits most data [19:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1144s). He calls it the Karpathy Obsidian "RAG", in air quotes, as a new kind of RAG [19:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1155s).

**Nested index files, the real power**

- **Indexes, not folders.** What makes it work isn't the three-way split but an index.md at every level: a plain markdown file telling Claude Code what it's looking at on each level it descends [19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s), [19:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1177s).
- **Retrieval walk-through.** You ask your OS for everything on AI agents, having built a wiki article on them earlier [19:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1185s):
  1. Claude opens the vault and hits the root index.md [19:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1197s).
  2. That index says raw holds unstructured data, wiki structured data, and outputs deliverables such as slide decks [20:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1203s).
  3. So Claude goes to wiki/ [20:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1213s), reads the index.md there [20:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1221s), and finds the article.
- **Overkill at first, essential later.** A table of contents for a folder with one article isn't needed, but after years of use, with thousands of documents and perhaps subfolders, it makes each folder far easier for Claude to understand [20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s), [20:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1237s). If every room Claude enters has a spot explaining what's there, lookups are faster and cheaper [20:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1254s).
- **The folders are arbitrary.** You don't need raw, outputs or any of the Karpathy layout, just a map that makes sense to Claude Code. It will probably be unique to you, because your data and goals are [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s), [21:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1273s), [21:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1281s). If stuck, ask Claude to review your vault and propose a structure, using Karpathy's setup for inspiration [21:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1292s).

**The vault CLAUDE.md**

- **Add a CLAUDE.md that describes all this** [21:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1306s). His covers vault conventions, starting with the structure: which files and folders Claude is looking at [21:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1312s). He has more than three top-level folders, including content, notes, runs, inbox, ops and projects [21:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1319s).
- **Navigation pattern.** A separate section tells Claude which path to follow when it's looking for something [22:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1325s). He finds the template flexible enough for any structure or data [22:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1333s). See [[CLAUDE.md as a Router]], [[Keep CLAUDE.md Lean]] and [[Tiered Lookup Routing]].

**State for loops**

- Skill and automation outputs need somewhere to go and should be logged in a way that suits loop engineering [22:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1348s), [22:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1356s). For self-improving skills and automations, the loop needs to see what past runs did, with everything tied together in one place [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s), [22:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1377s). See [[Skill Improvement Loop]].
- **Levels 1 + 2 = 90%.** Master both and you have about 90% of an AI OS's power, from the terminal, the desktop app or anywhere: codified workflows, a record of what's going on, and a second brain Claude can mine for insights you'd otherwise miss [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s), [23:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1387s), [23:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1394s).

### [23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s) Level 3

- **A custom visual wrapper** around everything so far. It can be fully custom; the two options he shows are web-app based and Obsidian based [23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s), [23:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1410s). See [[Build an Agentic OS Dashboard]].

**Demo 1: the web-app dashboard**

- **Same engine.** It's Claude Code under the hood, connected to Obsidian, with custom metrics tuned to what he needs to see [23:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1421s).
- **Left side:** YouTube subscribers, Instagram, his latest video, his Claude 5-hour usage window, directives pulled from Google Calendar, and documents the system has created [23:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1435s), [23:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1439s), [24:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1441s). The metrics are yours to change [24:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1464s).
- **Right side:** skills and automations as single buttons [24:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1444s).
  - Clicking "inbox brief" queues a run in which Claude works through his inbox, creates drafts and reports what it thinks matters [24:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1451s), [24:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1457s).
  - A voice later announces the brief: 32 threads triaged, two items flagged urgent [25:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1504s). Clicking the result opens the full write-up, which also opens in Obsidian [25:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1530s).
- **Floor raising.** The buttons let non-technical teammates and clients use some of Claude Code's power. Instead of teaching them Claude Code, skill installs and automation, he sets the OS up for them; they click a button and results land in their own or the team's Obsidian [24:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1472s), [24:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1486s), [24:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1498s).
- **Local voice.** The attached voice model, which he can talk to and hear back from, runs entirely on his computer rather than through ElevenLabs, so it's free [25:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1517s), [25:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1522s). He doesn't name it.

**Demo 2: an Obsidian command center**

- **A visual layer inside Obsidian itself** [25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s), with similar metrics including token burn, buttons that run skills or automations, and tabs for audience metrics and research [25:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1545s), [25:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1551s), [25:54](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1554s).
- **The sell isn't the visuals.** It's a one-stop view of things that are hard to see from inside the terminal [26:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1565s).

**How to build them (as described)**

- **Web app.** Build it like any web app with Claude Code [26:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1580s):
  1. Screenshot a site or layout you like as the visual reference [26:32](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1592s).
  2. Give Claude Code the skills you already use, the requirement to connect to the vault, and the metrics you want in one place [26:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1599s).
  3. Ask it to build a visual wrapper over all of it [26:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1608s).
- **Obsidian version.** Obsidian runs on plugins, so you're effectively building an app for Obsidian [26:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1613s). Ask Claude Code to make an Obsidian plugin version of the web app, then install and run it [27:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1623s). Plugin mechanics are under Beyond the source.

**Under the hood: headless Claude Code**

- **What a button does.** Clicking, say, the morning brief button calls a headless Claude Code, as if he'd opened a terminal and run /morning-brief [27:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1638s), [27:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1642s). No terminal appears, because it runs through `claude -p` [27:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1660s).
- **The billing scare.** Not long before, Anthropic said `claude -p` usage would stop drawing on the subscription and come from a separate credit (he cites $200) tied to API costs [27:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1671s). They walked it back, and for now it still draws on his Max plan, the same as running it in the terminal [28:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1686s), [28:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1690s). The verified status is under Beyond the source.
- That is how these wrappers still get Claude Code's full power, invisibly in the background [28:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1696s).

### [28:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1703s) Level 4

- **What Level 3 bought:** customisation, since you aren't locked into the terminal or desktop app, plus the ability to hand the OS to your team [28:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1703s), [28:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1710s).
- **One click from the power.** Someone handed the web app tied to your skills is one click from getting a lot out of Claude Code. The power lives in the skills and automations, so it's like setting them up on Claude Code without actually doing so [28:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1719s), [28:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1726s).

| Version | Route | Effort | Timestamp |
|---|---|---|---|
| Web app | Put it on GitHub or send a zip; easy to transfer and get running | Low | [29:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1741s), [29:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1748s) |
| Obsidian command center | Set it up for each person; not much harder, but not as simple as cloning a repo and pointing Claude Code at it | More hands-on | [29:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1761s), [29:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1773s) |

- **Client work.** Customisation is a big selling point if you do client work [29:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1780s). Many people who want to use Claude are put off by the terminal and even the desktop app [29:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1786s); he tells viewers they live in a bubble most people won't enter [29:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1798s). Setting it up so they talk to it or press a few buttons goes a long way [30:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1806s).
- **The dashboard effect.** He thinks its effect on non-technical people deserves proper study, because it changes how they perceive technical tools [30:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1814s).
- **Zooming out.** Levels 3 and 4 are the cherry on top; nearly all your time belongs in Levels 1–2 [30:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1822s), [30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s). His closing test: can you get consistent results from Claude Code, log them, and build a second brain it can reference and use to improve? If so, you're well ahead of most users [30:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1841s), [30:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1852s).

### [31:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1860s) Outro

- He hopes the four levels clarify how these systems work, where the value is, and how to build one yourself [31:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1863s).

## Caveats & disagreements

### Limits of this video

- **Self-promotion.** A "sponsor" read for his own paid course and community, where his builds live (03:59–04:26), recurs briefly at 26:28 and 31:12; these notes omit it. He shares no dashboard code, plugin or skill files, and his vault CLAUDE.md is only described in passing [21:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1312s).
- **Levels 3–4 are a showcase, not a build.** Each gets a one-paragraph "how": screenshot a layout and ask Claude to build it [26:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1594s), then ask for a plugin version [27:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1623s). There's nothing on job queues, run history, output storage, auth or per-user config.
- **Loop engineering is only named.** He defers to another video [11:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=713s) and never shows a run-log format, a review step or how a loop edits a skill [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s). See [[Loop Engineering]] and [[Skill Improvement Loop]] for concrete designs.
- **Unmeasured numbers:**
  - Levels 1–2 are "90%" of the value [02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s).
  - Structure alone is "99% of the way" [14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s).
  - "99%" of people won't use the terminal [30:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1803s).
  - The "10x" in the title is never quantified.
- **Level 2 is narrow.** It covers folders, indexes and a CLAUDE.md. Semantic search, knowledge graphs and Claude Code auto memory never come up. Compare [[Second Brain Levels]].
- **Session mining depends on what's still on disk.** He says Claude can see essentially all your previous sessions [07:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=463s). By default, transcripts are local files deleted after 30 days, in a format the docs call internal (Beyond the source). "Last 20 sessions" may not reach far back.
- **Routines have limits he skips.** The Desktop Routines demo [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s) doesn't mention that local tasks fire only while the app is open and the machine is awake. It also skips that a task in Manual permission mode stalls until someone approves (Beyond the source).
- **Headless buttons, but no word on permissions.** The inbox-brief button reads his mail and creates drafts unattended [24:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1459s). A `claude -p` run starts in Manual permission mode, so anything that would normally prompt (file edits, most shell commands, MCP tools) is denied unless pre-approved with `--allowedTools` or a permission mode (Beyond the source). He covers none of that, nor what a button is allowed to touch. For any button that touches email, calendars or client data, see [[Configure Safe Autonomy Permissions]] and [[Permissions and Approval Gates]].
- **The billing statement is time-sensitive.** His "still on the Max plan" [28:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1690s) was true when recorded. The change Anthropic paused on 2026-06-15 was still paused at ingest, and Anthropic says it will share any update before it takes effect (Beyond the source).
- **A gap in the distribution story** *(this note's inference, not his words)*. He says recipients needn't run Claude Code themselves [03:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=215s), yet the web version is shared by cloning a repo and pointing Claude Code at it [29:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1778s), and buttons work by calling `claude -p` [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s). Someone's machine still needs Claude Code installed and signed in. He doesn't say whose plan the runs count against or how clients' data is kept separate.
- **Privacy isn't mentioned.** He suggests copying a domain's data, such as all your sales data, into the vault [15:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=912s) and handing the OS to clients [29:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1784s). [[Nate Herk - Every Level of a Claude Second Brain]] warns that data processed through Claude goes to Anthropic [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), and suggests open-source models for client data [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s).
- **Minor gaps.** The local voice model is never named [25:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1517s). The inbox items read aloud are garbled in the captions and are private demo content [25:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1508s).

### Conflicts with existing vault notes

- **[[Context vs Connections]]: copy everything vs ingest only evergreen.**
  - **Chase:** put at least a copy of each domain's data, such as all your sales data, into the vault [15:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=912s).
  - **[[Nate Herk - Every Level of a Claude Second Brain]]:** don't ingest volatile data like Slack threads, email or customer records, because it becomes noise [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [27:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1657s). His test is whether it will still be useful a year from now [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s).
  - **Where that leaves it** *(this note's reading)*. Chase's own dashboard pulls calendar directives live [23:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1439s), which fits "connections". A workable reconciliation: copy settled reference material (price lists, playbooks, closed-deal summaries) and reach live pipeline records through a connector.
- **[[LLM Wiki]]: what Karpathy's structure is.**
  - **Chase:** raw/, wiki/ and outputs/, with an index.md at every level [17:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1056s), [18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s), [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s).
  - **The vault note, from Karpathy's gist:** raw sources, a wiki and a schema file (CLAUDE.md/AGENTS.md), with a single wiki index.md plus an append-only log.md and ingest/query/lint operations.
  - **Where that leaves it.** The gist and coverage of Karpathy's original post both mention answers produced as slide decks or charts and filed back into the wiki (Beyond the source), so deliverables have a basis. A separate outputs/ folder and an index in every folder look like Chase's own extensions. He also omits log.md and lint.
- **[[LLM Wiki]]: is it RAG?**
  - **Chase:** a new kind of "RAG", said in air quotes [19:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1155s).
  - **The vault:** the LLM Wiki is knowledge compiled once and kept current, explicitly contrasted with RAG re-deriving answers from raw chunks on every query.
- **[[CLAUDE.md as a Router]]: a refinement, not a contradiction.**
  - **The vault:** CLAUDE.md is the main router and the wiki index a second-tier router.
  - **Chase:** routes room by room. Every folder has its own index [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s), the folder names are arbitrary [21:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1266s), and the vault CLAUDE.md adds a "navigation pattern" section [22:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1325s).
  - **Fit** *(this note's inference)*. Pushing detail down into folder indexes also fits [[Keep CLAUDE.md Lean]].
- **[[Second Brain Levels]]: clashing terms and scope.**
  - **Numbering.** Chase's levels are skills, memory, UI and distribution [01:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=110s), while Nate's are five retrieval tiers, so notes should always say whose "Level N" is meant.
  - **Scope.** Chase says structure alone is ~99% of the way [14:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=854s). Nate says to climb beyond folders when a real retrieval pain appears [19:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1159s).
  - **Common ground.** There's no universal structure: Chase says yours will be unique [21:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1281s), and Nate says no best structure has been proven [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s).
- **[[Obsidian]] and team adoption: viewer vs control surface.**
  - **Nate:** Obsidian is only a viewer [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s), and a team brain is mainly a change-management problem [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s).
  - **Chase:** agrees visuals aren't the value [12:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=766s), [26:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1567s). But he turns Obsidian into a control surface whose buttons run skills [25:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1551s), and argues a buttons-and-voice dashboard is itself the adoption lever for non-technical people [30:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1814s).
  - **[[Jay E - The ARMS Framework for a Claude Agentic OS]]:** weighs the interface similarly, at about 20–30% of the value [03:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=213s).
- **[[Always-On Brain OS]]: how hard is scheduling?**
  - **Nate:** discussing always-on memory syncing (GBrain), says that in Claude Code you'd have to set up and manage the crons yourself [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s).
  - **Chase:** turning a skill into an automation is very easy, via a prompt or Desktop Routines [11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s), [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s).
  - **Jay:** local routines only run while the computer is on [16:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=961s).
  - **Current docs** offer both local tasks and cloud routines, each with limits (Beyond the source). See [[Routines and Scheduled Tasks]].
- **[[Grill Me Interview Skill]]: a new use, not a disagreement.**
  - **Nate:** uses the interview to pull knowledge about a topic out of your head [20:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1258s).
  - **Chase:** aims it at discovering recurring workflows to codify [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s).
  - **For the technique note:** worth adding as a variation.

### How other sources compare

- **Validate first: agreement.** [[Ras Mic - How AI Agents and Claude Skills Work]] says skills should come from your own successful run [12:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=773s), the same as Chase's "do it by hand, then codify" [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s). See [[Build a Skill from a Successful Run]].
- **When to make a skill: complementary triggers.** [[Jay E - The ARMS Framework for a Claude Agentic OS]] makes a skill once you've prompted for the same job twice [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s). Chase instead audits everything up front [05:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=343s). *This note's reading:* audit to seed the backlog, then use the twice rule to catch new candidates.
- **Headless skill buttons: same mechanism.** [[Jay E - The ARMS Framework for a Claude Agentic OS]] also runs skills headlessly through `claude -p` [09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s). See [[Build an Agentic OS Dashboard]].
- **Loop definitions.** [[AI LABS - Types of Claude Loops Explained]] maps out several loop types [00:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=22s), from stateless loops that keep nothing between runs [01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s) to learning loops [05:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=305s). Chase's "record runs so future runs improve" [02:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=154s) is only one kind. See [[Loop Engineering]].

## Build from this

1. **Session-mining skill backlog.**
   - **What it does:** reads recent sessions and writes `skills-backlog.md` with task, frequency, expected output, proposed skill, and whether it could be automated or looped [08:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=504s).
   - **Build note:** read sessions through `claude -p --resume <id>` or `/export`, not raw JSONL, and mind the 30-day retention (Beyond the source).
   - See [[Workflow Audit into Skills]].
2. **Workflow discovery interview.**
   - **What it does:** starts from a brain-dump, asks one blind-spot question at a time per domain, and outputs a domain → task → proposed-skill inventory [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s).
   - See [[Grill Me Interview Skill]] and [[Workflow Audit into Skills]].
   - *Vault starter prompt (original wording, not his):* "I want to turn my recurring work into Claude skills. I'll describe my typical week in one messy brain-dump. Then interview me one question at a time, grouped by domain, until you can list every repeated task with its trigger, inputs and expected output. Finish with a table: domain, task, frequency, proposed skill name, and whether it could run on a schedule."
3. **Codify after success.**
   - **What it does:** right after a task works by hand, runs skill-creator on "what we just did", adds test prompts, and records the source session ID [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s).
   - See [[Build a Skill from a Successful Run]] and [[Build a Reference-Rich Skill]].
4. **Skill-to-routine converter.**
   - **What it does:** for each approved skill, proposes a schedule, permission mode and time guardrails, then creates a local Desktop task or a cloud routine [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s).
   - See [[Schedule Recurring Claude Tasks]] and [[Routines and Scheduled Tasks]]. For runs with the laptop closed, see [[Sync a Workspace to an Always-On Cloud Agent]].
5. **Run log + improvement loop.**
   - **Log:** each scheduled skill appends a dated record to `runs/<skill>/` covering inputs, output path, problems and your feedback [22:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1356s).
   - **Loop:** a weekly review reads the logs and proposes SKILL.md diffs, applied only after approval [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s).
   - See [[Skill Improvement Loop]], [[Multi-Agent Review and Scoring Loops]], [[Tests-First Goal Loop]] and [[Loop Engineering]].
6. **Nested-index vault with a navigation pattern.**
   - **What it does:** an index.md in every folder [19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s), a CLAUDE.md with structure and navigation-pattern sections [22:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1325s), and a lint that flags missing indexes and dead entries.
   - See [[Build a Level 1 Second Brain]], [[Tiered Lookup Routing]], [[CLAUDE.md as a Router]] and [[Keep CLAUDE.md Lean]].
   - *Vault starter CLAUDE.md block (original wording):*

     ```markdown
     ## Vault structure
     - raw/      unprocessed sources (never edited)
     - wiki/     one synthesised page per topic, built from raw/
     - outputs/  dated deliverables built from wiki pages (link back to sources)
     - runs/     one folder per skill; append-only run logs
     Every folder has an index.md listing its contents in one line each.

     ## Navigation pattern
     1. Read the index.md of the folder you are in before opening files.
     2. Topic questions: wiki/index.md, then the page, then its raw/ sources if needed.
     3. "What did the last run do?": runs/<skill>/ newest file first.
     4. Never scan a folder file by file when its index answers the question.
     ```

7. **raw → wiki → outputs pipeline.**
   - **What it does:** ingest sources into wiki pages, then a `/make-output` skill builds a deck or brief from named pages into `outputs/YYYY-MM-DD-<name>/`, with links back [18:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1113s).
   - See [[Ingest Sources into an LLM Wiki]].
8. **Agentic OS dashboard, web or Obsidian plugin.**
   - **What it does:** shows the metric panels you choose [23:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1429s). Its buttons run allowlisted skills through a job queue with `claude -p "/<skill>" --output-format json` [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s). Results are saved to the vault [25:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1533s), and the same buttons can be ported into an Obsidian plugin [27:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1625s).
   - **Safety:** give each button its own allowed-tools list, and make email buttons drafts-only.
   - See [[Build an Agentic OS Dashboard]] and [[Configure Safe Autonomy Permissions]].
9. **Team starter repo.**
   - **What it does:** a clonable template with the vault CLAUDE.md, a skills folder, the dashboard, a setup script and a plain-language README [29:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1748s).
   - **Build note:** document which Claude account runs use, and keep client data out of the repo.
   - See [[Agentic OS]].

## Resources mentioned

- **His loop-engineering video**, which he says he posted the day before [11:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=713s). It isn't linked in the captions or the description.
- **Andrej Karpathy's viral post** on LLM knowledge bases in Obsidian [17:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1040s). The related gist is linked under Beyond the source.
- **Anthropic's skill-creator skill** [07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s).
- **Claude desktop app → Routines** [11:33](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=693s).
- **Obsidian** [14:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=870s) and its plugin system [26:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1615s).
- **`claude -p`**, headless Claude Code [27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s).
- **Codex CLI and Codex desktop app**, as alternative harnesses [03:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=227s).
- **Named in the demos:** Google Calendar [23:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1439s), YouTube and Instagram stats [23:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1435s), ElevenLabs (only as what his local voice avoids) [25:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1528s), and GitHub as a distribution route [29:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1750s).

## Beyond the source

*None of this is said in the video. Each item was checked against the linked page on 2026-09-15.*

- **Running skills headlessly with `claude -p`.**
  - **Invocation.** `-p` (or `--print`) runs Claude Code non-interactively. User-invoked skills work by putting `/skill-name` in the prompt string.
  - **Permissions.** A `-p` run starts in Manual permission mode on every plan. Pre-approve tools with `--allowedTools` (permission-rule syntax, e.g. `Bash(git diff *)`), or set a baseline with `--permission-mode`: `auto`, `dontAsk` (denies anything that would prompt) or `acceptEdits`. `--permission-prompts none` (v2.1.259+) tells Claude nobody can approve requests in unattended runs.
  - **Output.** `--output-format json` returns the result, session ID and an estimated `total_cost_usd`, which suits a dashboard job queue.
  - **Two gotchas for dashboards:**
    - `--bare` skips skills, CLAUDE.md, hooks and MCP discovery, and does *not* use your subscription login (for the Anthropic API it needs `ANTHROPIC_API_KEY` or an `apiKeyHelper`). A skills dashboard on a subscription therefore shouldn't use it as-is. The docs also say `--bare` will become the default for `-p` in a future release, so re-check such a dashboard after upgrading.
    - Without `--bare`, a `-p` run executes the project's hooks and `.mcp.json` servers with no trust dialog.
  - Source: https://code.claude.com/docs/en/headless
- **Sessions from `-p` runs don't clutter your history.** Claude Code leaves `claude -p` sessions out of the session picker and `claude --continue`, but you can resume one by session ID. Source: https://code.claude.com/docs/en/sessions
- **`claude -p` billing status.**
  - **What was announced:** Anthropic planned for Agent SDK, `claude -p` and third-party app usage to move to a separate monthly credit from 2026-06-15.
  - **What happened:** the change was paused on that date. That usage still draws from subscription limits, the announced credits aren't available, and Anthropic says it will give notice before any future change.
  - **Amounts:** the paused credits ranged from $20 (Pro) to $200 (Max 20x) by plan, so his "$200" is the top tier.
  - Source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
- **Where the sessions he mines actually live.**
  - **Location:** `~/.claude/projects/<project>/<session-id>.jsonl`, one JSON object per line.
  - **Stability:** the docs say the entry format is internal and changes between versions, so scripts that parse the files can break on any release. They recommend `/export`, `claude -p --resume <session-id>` or hooks' `transcript_path` instead.
  - **Retention:** 30 days by default, changeable with `cleanupPeriodDays` in settings.json.
  - Source: https://code.claude.com/docs/en/sessions
- **Desktop Routines, as documented.**
  - **Creating one:** in the Code tab, Routines → New routine → Local. Fields: name, description, instructions (with permission-mode and model pickers), a working folder and a schedule (Manual, Hourly, Daily, Weekdays, Weekly). Other intervals can be asked for in plain language.
  - **When it runs:** local tasks fire only while the app is open and the computer awake. After sleep, Desktop runs one catch-up for the most recent missed time within seven days.
  - **Permissions:** a task in Manual mode stalls on a tool it lacks permission for. The docs suggest clicking Run now and choosing "always allow" for each prompt.
  - **Storage:** the prompt lives at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`.
  - **Cloud routines:** they run with the computer off, but from a fresh clone with no local files and a 1-hour minimum interval.
  - Source: https://code.claude.com/docs/en/desktop-scheduled-tasks
- **Karpathy's structure, gist vs post.**
  - **The gist ("LLM Wiki")** describes raw sources, an LLM-maintained wiki and a schema file. It has one `index.md` catalogue plus an append-only `log.md`. It lists slide decks (Marp) and charts among possible answer formats and says good answers can be filed back as wiki pages, but it describes no separate outputs folder. Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - **The original X post** (posted 2026-04-02) showed 21,894,606 views when checked on 2026-09-15, which matches Chase's "over 20 million"; early-April press coverage cited 16M+. Source: https://api.fxtwitter.com/karpathy/status/2039805659525644595
  - As covered secondhand, it described query results such as Marp slide decks and charts being filed back into the wiki, which supports Chase's outputs idea. Source (secondary coverage): https://joseluischavezcalva.substack.com/p/karpathys-llm-knowledge-bases
- **Building an Obsidian plugin.** Plugins are written in TypeScript from the official sample-plugin template. A plugin needs `manifest.json` and a compiled `main.js` in the vault's `.obsidian/plugins/` folder and is enabled under Settings → Community plugins. Obsidian's docs warn never to develop plugins in your main vault and to use a separate one. Source: https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin
- **skill-creator.** It is in Anthropic's public skills repo. Its description covers creating, editing and improving skills and running evals to measure them, and its folder includes scripts and an eval viewer. Source: https://github.com/anthropics/skills/tree/main/skills/skill-creator

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "clawed code", "cloud code" | Claude Code |
| "claw desktop", "Claw Desktop" | the Claude desktop app |
| "codeex", "codec cli" | Codex, Codex CLI |
| "AIOS" | AI OS, used interchangeably with "agentic OS" |
| "Carpathy", "Cararpathy" | Andrej Karpathy |
| "slash raw folder. R A." (17:43) | the `raw/` folder; he spells R-A-W and the captions drop the W |
| "index MD", "index.n MD" | index.md |
| "claw.md" | CLAUDE.md |
| "obsidian rag" (19:15) | Obsidian "RAG", said in air quotes |
| "claude-p", "claude dashp", "claw-p" | `claude -p` (headless print mode) |
| "cla subscription" | Claude subscription |
| "forward slashming brief" (27:37) | likely `/morning-brief` |
| "clawed 5 hour window" (23:57) | likely the Claude 5-hour usage window |
| "11 Labs" | ElevenLabs |
| "the cell here" (05:58, 26:07, 29:42) | "the sell here", i.e. the selling point |
| "what is this bias? Well, bias customization" (28:25) | likely "what does this buy us? It buys customisation" |
| "point Cloud code edit" (29:38) | "point Claude Code at it" |
| "it's literally just a file" (14:51) | he means a folder |
| "Gear Up contract", "Open AI merge campaign" (25:08) | private demo inbox items read by the voice model (*unclear in captions*) |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Agentic OS]] · [[Loop Engineering]] · [[Routines and Scheduled Tasks]] · [[Design for Retrieval]] · [[LLM Wiki]] · [[CLAUDE.md as a Router]] · [[Second Brain Levels]] · [[Context vs Connections]] · [[Always-On Brain OS]] · [[Permissions and Approval Gates]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]]
- **Techniques:** [[Workflow Audit into Skills]] · [[Build a Skill from a Successful Run]] · [[Build a Reference-Rich Skill]] · [[Skill Improvement Loop]] · [[Multi-Agent Review and Scoring Loops]] · [[Tests-First Goal Loop]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Build an Agentic OS Dashboard]] · [[Build a Level 1 Second Brain]] · [[Ingest Sources into an LLM Wiki]] · [[Tiered Lookup Routing]] · [[Keep CLAUDE.md Lean]] · [[Grill Me Interview Skill]] · [[Configure Safe Autonomy Permissions]]
- **Tools:** [[Claude Code]] · [[Obsidian]] · [[OpenAI Codex]]
- **People:** [[Chase AI]] · [[Andrej Karpathy]] · [[Nate Herk]] · [[Matt Pocock]] (Grill Me's originator, per Nate [20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s)) · [[Jay E]] · [[Ras Mic]] · [[AI LABS]]
- **Other creators in this batch:** [[Simon Pittman]] · [[Greg Isenberg]] · [[The Coding Sloth]]
- **Sources:** [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Nate Herk - Every Level of a Claude Second Brain]] · [[AI LABS - Types of Claude Loops Explained]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Simon Pittman - Set Up Claude Cowork]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[AI LABS - Claude Design Skills for Beautiful Sites]]
