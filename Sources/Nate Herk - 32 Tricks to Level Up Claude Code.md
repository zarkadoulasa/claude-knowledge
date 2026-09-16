---
type: source
title: "32 Tricks to Level Up Claude Code in 16 Mins"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=jqoFP9QapXI
video_id: jqoFP9QapXI
published: 2026-04-27
duration: "16:15"
ingested: 2026-09-15
topics: [claude code tips, context management, plan mode, self-verification, subagents, skills, git worktrees, scheduling, permissions, MCP]
tags: [source/youtube, topic/claude-code, topic/context, topic/planning, topic/verification, topic/subagents, topic/skills, topic/models, topic/loops, topic/scheduling, topic/permissions, topic/mcp, topic/memory, topic/design, topic/automation]
---

# Nate Herk - 32 Tricks to Level Up Claude Code

> **Creator:** [[Nate Herk]] · **Published:** 2026-04-27 · **Length:** 16:15 · [Watch on YouTube](https://www.youtube.com/watch?v=jqoFP9QapXI)

## TL;DR

[[Nate Herk]] runs through 32 [[Claude Code]] habits at about 30 seconds each, in three tiers: beginner (1–10), intermediate (11–22) and pro (23–32). Most fall into six groups:

- **Keep context lean:** a status line, /context, /compact at about 60%, /clear, Esc early, and a CLAUDE.md capped at 150–200 lines that routes out to other files.
- **Align before building:** plan mode, give Claude problems rather than commands, and have it ask questions until it's 95% confident.
- **Self-checking:** verification to-dos, screenshot passes and browser checks.
- **Scaling out:** Haiku subagents under an Opus main thread, skills, git worktrees and agent teams.
- **Running while you're away:** notification hooks, /loop, desktop scheduled tasks, a VPS and Remote Control.
- **Power features:** CLI analytics, ultrathink, allow/deny permissions and the Context7 MCP server.

It's a checklist, not a tutorial: nothing is set up on screen. Several specifics are dated. Check Caveats and Beyond the source before building.

## Key takeaways

- **Context is the budget.** Watch context % in a status line and find bloat with /context. Compact at about 60% and say what to keep. /clear between unrelated tasks, and press Esc as soon as Claude goes off course. [01:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=72s), [01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s), [02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s), [02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s), [07:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=469s). See [[Context Window Management]] and [[Context Hygiene Routine]].
- **Align before code.** Start in plan mode and give Claude problems to reason about. Have it ask questions (AskUserQuestion) until it's 95% sure; he says this saves three or four revision rounds. [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s), [03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s), [03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s), [03:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=233s). See [[Plan Before Executing]] and [[Plan-First Workflow]].
- **Put checks inside the plan.** Follow each build to-do with a verification to-do, and don't move on below 95% confidence. For websites he runs about three screenshot-and-fix passes before he sees V1. [04:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=242s), [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s), [09:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=564s). See [[Verification Before Done]] and [[Build Verification into Every Task]].
- **Grow CLAUDE.md, but keep it lean.** Log new patterns and gotchas as you find them. Trim once it passes 150–200 lines, and route style guides, business context and project status out to separate files. [06:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=400s), [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), [07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s). See [[CLAUDE.md as a Router]] and [[Keep CLAUDE.md Lean]].
- **Push back, then persist the lesson.** Reject work that's merely okay. Once a better version lands, have Claude update the skill or CLAUDE.md. [08:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=484s), [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s). See [[Agent Laziness]] and [[Build a Skill from a Successful Run]].
- **Scale out.** He covers four ways to work in parallel. See [[Subagents and Agent Teams]], [[Agent Skills]], [[Parallel Sessions with Git Worktrees]] and [[Route Tasks to the Right Claude Model]].
  - Subagents get their own context windows, so put cheap Haiku on bulk reading. [05:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=301s), [06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)
  - Skills turn SOPs into repeatable commands. [05:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=354s)
  - Worktrees keep parallel sessions from clobbering each other's files. [10:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=653s)
  - Agent teams message each other and give more cohesive output, at a higher cost. [14:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=883s), [15:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=900s)
- **Mind tool context.** He says MCP servers load every tool definition, so when tokens are tight and a project needs only one narrow call, hardcode that endpoint instead [11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s), [11:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=712s). As a separate hack, he connects CLIs such as bq for plain-English analytics [13:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=795s). He still rates the Context7 MCP server highly [15:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=908s). See [[Connecting Claude to External Tools]]. *(The MCP cost claim is dated.)*
- **Autonomy without the dangerous flag.** Allowlist safe commands and deny destructive ones instead of skipping permissions; deny wins. [14:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=844s), [14:32](https://www.youtube.com/watch?v=jqoFP9QapXI&t=872s). See [[Configure Safe Autonomy Permissions]]. *(He overstates how safe this is.)*
- **Work while away.** He covers /loop polling, desktop scheduled tasks (each run is a fresh session), a VPS and Remote Control. [11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s), [12:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=744s), [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s), [12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s). See [[Routines and Scheduled Tasks]] and [[Schedule Recurring Claude Tasks]].

## The 32 hacks at a glance

Tiers follow the video's chapters: beginner from 00:14, intermediate from 04:53, pro from 10:29.

| # | Hack | Tier | Where | Vault note |
|---|---|---|---|---|
| 1 | Run /init on every project to generate CLAUDE.md | Beginner | [00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s) | [[CLAUDE.md as a Router]], [[Build a Level 1 Second Brain]] |
| 2 | Status line (model, context %, cost) | Beginner | [00:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=52s) | [[Context Window Management]] |
| 3 | Voice input: /voice or a dictation app | Beginner | [01:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=76s) | [[Claude Code]] |
| 4 | Keep context small; split big problems | Beginner | [01:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=95s) | [[Context Window Management]] |
| 5 | /context to find token bloat | Beginner | [01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s) | [[Context Hygiene Routine]] |
| 6 | /compact at ~60% with keep-instructions; /clear between tasks | Beginner | [02:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=128s) | [[Context Hygiene Routine]] |
| 7 | Always start in plan mode | Beginner | [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s) | [[Plan Before Executing]], [[Plan-First Workflow]] |
| 8 | Treat Claude like a junior dev: pose problems, not commands | Beginner | [03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s) | [[Plan Before Executing]] |
| 9 | Make Claude ask questions until 95% confident | Beginner | [03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s) | [[Plan-First Workflow]], [[Grill Me Interview Skill]] |
| 10 | Build self-checks into the to-do list | Beginner | [03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s) | [[Verification Before Done]], [[Build Verification into Every Task]] |
| 11 | Subagents for parallel work | Intermediate | [04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s) | [[Subagents and Agent Teams]] |
| 12 | Custom skills for SOPs | Intermediate | [05:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=328s) | [[Agent Skills]], [[Workflow Audit into Skills]] |
| 13 | Haiku for subagents | Intermediate | [05:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=355s) | [[Choosing a Claude Model]], [[Route Tasks to the Right Claude Model]] |
| 14 | Keep refreshing CLAUDE.md, capped at 150–200 lines | Intermediate | [06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s) | [[Keep CLAUDE.md Lean]], [[Agent Memory Patterns]] |
| 15 | Have CLAUDE.md route to other files | Intermediate | [07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s) | [[CLAUDE.md as a Router]], [[Tiered Lookup Routing]] |
| 16 | Exit early (Esc) and re-ask | Intermediate | [07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s) | [[Context Hygiene Routine]] |
| 17 | Challenge outputs, then update the skill or CLAUDE.md | Intermediate | [07:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=478s) | [[Agent Laziness]], [[Skill Improvement Loop]] |
| 18 | /rewind for quick undos | Intermediate | [08:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=502s) | [[Context Hygiene Routine]] |
| 19 | Hooks for sound notifications | Intermediate | [08:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=514s) | [[Claude Code]] |
| 20 | Screenshots: errors, inspiration, self-check loop | Intermediate | [08:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=537s) | [[Build Verification into Every Task]] |
| 21 | Chrome DevTools for functional browser checks | Intermediate | [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s) | [[Build Verification into Every Task]], [[Claude in Chrome]] |
| 22 | Clone inspiration sites as a template | Intermediate | [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s) | [[Escaping the Default AI Design Look]], [[Build a Distinctive Site with Design Skills]] |
| 23 | Parallel sessions with git worktrees | Pro | [10:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=637s) | [[Parallel Sessions with Git Worktrees]] |
| 24 | Direct API endpoints instead of MCP (situational) | Pro | [11:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=684s) | [[Connecting Claude to External Tools]], [[Context vs Connections]] |
| 25 | /loop for recurring tasks and reminders | Pro | [11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s) | [[Routines and Scheduled Tasks]], [[Schedule Recurring Claude Tasks]] |
| 26 | VPS for always-on sessions | Pro | [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s) | [[Always-On Brain OS]], [[Sync a Workspace to an Always-On Cloud Agent]] |
| 27 | Remote Control from your phone | Pro | [12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s) | [[Claude Code]] |
| 28 | Plain-English analytics via CLI tools (bq) | Pro | [13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s) | [[Connecting Claude to External Tools]] |
| 29 | ultrathink for hard problems (announced as "28") | Pro | [13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s) | [[Choosing a Claude Model]] |
| 30 | Permission allow/deny lists for safe autonomy | Pro | [14:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=840s) | [[Permissions and Approval Gates]], [[Configure Safe Autonomy Permissions]] |
| 31 | Agent teams | Pro | [14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s) | [[Subagents and Agent Teams]], [[Multi-Agent Review and Scoring Loops]] |
| 32 | Context7 MCP for current library docs | Pro | [15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s) | [[Connecting Claude to External Tools]] |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=0s) Intro

- He pitches these as the hacks that took him from beginner to quickly producing workflows, websites, apps and agents [00:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=0s). The list runs beginner to power user, and he says the best are saved for last [00:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=9s).

### [00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s) Beginner Hacks

**1. /init on every project** [00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s)
- In an existing project, run /init first [00:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=18s). Claude Code scans the codebase and writes CLAUDE.md as a cheat sheet covering architecture, conventions and key files [00:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=23s), [00:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=31s). You then stop re-explaining the project every session [00:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=35s).
- For a new project, have Claude help write CLAUDE.md from the project goal, tech stack, rules and key folders [00:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=42s).

**2. Status line** [00:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=52s)
- Run /statusline and describe what to show, e.g. model, context percentage and cost [00:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=56s), [01:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=61s). It generates a script that renders at the bottom of the terminal as a mini dashboard [01:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=63s), [01:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=70s).
- The main value is always seeing how much context is left, so you avoid context rot [01:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=72s).

**3. Voice input** [01:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=76s)
- Claude Code had just shipped a native /voice command [01:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=78s), still rolling out at recording [01:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=84s). The alternative is a system-wide dictation app, so you can talk and have text appear in any window [01:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=87s).

**4. Keep context small** [01:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=95s)
- Don't dump the whole codebase in; give only what the current task needs [01:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=97s). Split big problems into small, focused steps, because less noise gives better results [01:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=102s). He says many people ignore this [01:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=108s).

**5. /context for token bloat** [01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)
- It breaks token use into percentages across system prompt, files and MCP servers [01:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=113s), [02:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=121s). Use it to diagnose a bloated session and then restructure [02:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=124s).

**6. Compact at 60%, clear between tasks** [02:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=128s)
- At about 60% context, run /compact to compress history [02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s). You can tell it what to keep, e.g. the API integration decisions and the database schema [02:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=143s), [02:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=147s).
- When switching to an unrelated task, /clear starts fresh [02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s). CLAUDE.md and your files remain, so you're not starting from scratch [02:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=162s).

**7. Always start in plan mode** [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)
- Cycle to plan mode with Shift+Tab or pick it manually [02:50](https://www.youtube.com/watch?v=jqoFP9QapXI&t=170s). Claude can still read and research but changes nothing [02:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=174s). It outlines steps, asks clarifying questions and maps the approach before coding [02:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=179s).
- He says this "has been shown" to improve quality, but gives no source [03:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=183s). Approve the plan, leave plan mode and tell Claude to execute [03:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=187s). He says this alone sharply cuts corrections [03:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=189s).

**8. Treat Claude like a junior developer** [03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s)
- Don't always hand it direct commands like "write a function that does X" [03:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=197s). Pose the problem and let Claude reason through the approach [03:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=200s).
- Ask it to explain the assumptions and decisions it makes [03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s). He says reasoning first gives better outputs [03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s): like plan mode, but thinking deeper [03:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=214s).

**9. Make Claude ask questions** [03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)
- Plan mode often does this on its own [03:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=220s), but you can tell Claude to use its AskUserQuestion tool [03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s). His pattern is to keep it asking until it's 95% confident it knows what you need and what to do [03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s).
- The upfront alignment saves three or four revision rounds [03:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=233s). It's a lighter, task-scoped relative of the [[Grill Me Interview Skill]].

**10. Self-checking to-do lists** [03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)
- Add verification steps to the to-do list Claude writes [04:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=242s). Example: after "build the website", add "screenshot it and check it looks right" [04:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=247s), then a Chrome DevTools check that nothing is broken [04:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=254s). Claude then checks its own work before asking for your feedback [04:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=260s).
- Add a gate: don't move on until 95% confident the current to-do is good [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s). One-shotting is hard, but 90% of the way beats 60–65% [04:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=277s), [04:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=280s).

### [04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s) Intermediate Hacks

For people already using Claude Code who want to move faster [04:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=288s).

**11. Subagents for parallel work** [04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s)
- On complex problems, tell the main session to use subagents [04:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=297s). Each has its own context window and can use its own model, and they run in parallel [05:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=301s), [05:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=304s).
- The main thread stays clean while subagents research, write tests or explore approaches, then report back [05:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=308s), [05:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=313s). It's like a team of developers [05:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=316s). Put subagents on Haiku and keep Opus for the main thread [05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s).

**12. Custom skills** [05:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=328s)
- Skills are reusable prompt files in .claude/skills [05:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=330s), e.g. techdebt.md and codereview.md [05:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=334s), [05:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=339s). Invoke one by name in plain language or as a slash command, and it runs the workflow the same way each time [05:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=344s).
- Commit them to GitHub so the team gets them, which amounts to automating your SOPs [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s), [05:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=354s). (The real format is a folder with SKILL.md; see Caveats.) See [[Build vs Install Third-Party Skills]].

**13. Haiku for subagents** [05:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=355s)
- Set the subagent model to Haiku for simple tasks or large data volumes; it's much cheaper [06:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=363s), [06:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=367s).
- His example: a subagent scrapes many articles, reads hundreds of thousands of tokens, and hands Opus only a short summary [06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s), [06:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=375s). An expensive model shouldn't read that much for a few facts [06:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=378s). Done well, this cuts cost without hurting quality where it matters [06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s).

**14. Keep refreshing CLAUDE.md** [06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s)
- Update CLAUDE.md after new discoveries and new skills [06:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=393s), [06:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=396s). Have Claude log patterns, gotchas and conventions so the next session knows them and doesn't repeat mistakes [06:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=400s), [06:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=406s). Over time, he says, Claude gets smarter about you, your business and your project [06:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=407s).
- The catch is bloat [06:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=413s). He calls CLAUDE.md basically the system prompt, loaded into every conversation and eating context [06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s). He keeps his to 150–200 lines at most and trims when it grows [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), [07:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=430s).

**15. Route CLAUDE.md to other files** [07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)
- Keep CLAUDE.md lean, but point it at separate files for style guides, business context and reference docs so Claude knows where to look [07:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=442s), [07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s), [07:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=451s).
- His example: it doesn't need a project's exact status, only where to find it [07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s). See [[Design for Retrieval]] and [[Tiered Lookup Routing]].

**16. Exit early and re-ask** [07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)
- If Claude heads the wrong way, hit Escape, correct course and re-prompt [07:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=466s), [07:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=469s). Tokens spent going the wrong way are wasted context, so steer early [07:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=473s).

**17. Challenge outputs aggressively** [07:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=478s)
- Push back on okay work [08:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=482s). Tell Claude to scrap it for a more elegant version or try a completely different approach [08:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=484s), [08:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=488s). The second try is often much better, because the bar is higher and Claude now knows what to avoid [08:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=490s), [08:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=493s).
- Once it improves, tell Claude to update the skill or CLAUDE.md so it doesn't repeat the mistake [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s).

**18. /rewind** [08:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=502s)
- Roll back to an earlier point in the conversation without starting over [08:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=507s).

**19. Notification hooks** [08:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=514s)
- Set one up via /hooks, or ask Claude Code in plain language [08:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=517s), [08:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=520s). His plays a sound when a session finishes [08:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=527s). That way he can do other work or run around 15 sessions, and hear when one needs input [08:50](https://www.youtube.com/watch?v=jqoFP9QapXI&t=530s), [08:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=535s).

**20. Screenshots** [08:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=537s)
- Claude can see, so feed it error messages and inspiration sites [09:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=540s), [09:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=543s). As a self-check, ask it to screenshot the site and say whether the layout looks right [09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s), [09:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=550s).
- His website flow runs design, screenshot, fix, repeat, for about three passes before he sees V1 [09:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=559s), [09:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=564s). That V1 is far better than before [09:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=567s).

**21. Chrome DevTools** [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)
- Claude can open a browser, interact with an app and check that it works [09:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=575s). It's like the screenshot loop, but for functionality rather than design [09:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=580s), and he calls it huge for front-end work [09:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=586s).
- It can also fill in forms and act where no API exists [09:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=588s), [09:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=593s). He floats that it could "potentially" solve CAPTCHAs [09:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=596s), but prefers working in a session you're already signed into [09:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=598s). **Flagged, not advice:** see Caveats.
- He doesn't say which tool he means. It's probably the Chrome DevTools MCP server, possibly [[Claude in Chrome]].

**22. Clone inspiration sites** [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)
- Give Claude screenshots of sites you like and ask it to match the look. It borrows their design patterns and avoids the generic AI-slop look [10:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=607s), [10:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=612s). You can also feed in the site's HTML and styling [10:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=618s).
- Treat the result as a template and add your own touch rather than a straight copy [10:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=625s). See [[Escaping the Default AI Design Look]] and, as a vault cross-reference, [[Claude Design]].

### [10:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=629s) Pro Hacks

For pushing Claude Code to its limits [10:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=630s).

**23. Git worktrees** [10:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=637s)
- Two sessions working in the same folder can overwrite each other [10:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=643s). A worktree is an efficient parallel copy of the project [10:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=648s).
- Run `claude --worktree <feature-name>` in one terminal to get an isolated workspace on its own branch. Run it again in another terminal with a different name [10:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=653s), [10:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=657s), [11:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=660s).
- He suggests running three to five without them stepping on each other [11:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=671s), then merging the branches back like any git branch [11:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=673s).

**24. API endpoints instead of MCP (situational)** [11:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=684s)
- It depends on the situation [11:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=686s). MCP servers expose all their tools, but he says they load every tool definition into context [11:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=689s), [11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s).
- When tokens are tight, and a project only needs to read one Notion database, hardcode that single endpoint instead of teaching Claude every function [11:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=696s), [11:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=701s), [11:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=712s). *(Dated; see Caveats.)*

**25. /loop** [11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s)
- Example: check the deployment every 5 minutes. Claude re-runs the prompt in the same session until you close it [12:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=720s), [12:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=723s). Other uses: PRs, error logs, builds [12:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=728s). It interrupts only when something needs you [12:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=732s). One-off reminders also work in plain language [12:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=736s).
- His caveat: loops last only 3 days [12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s). For longer schedules he uses desktop scheduled tasks [12:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=744s), though each run is its own session with no context memory [12:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=750s). See [[Loop Engineering]].

**26. VPS for always-on sessions** [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)
- On a remote server, Claude Code keeps running with your laptop closed [12:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=759s). You reach it over SSH or through Telegram [12:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=765s), [12:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=767s). He recommends it for long jobs you'd otherwise have to watch in a local terminal [12:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=769s).
- No setup or hardening is shown.

**27. Remote Control** [12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s)
- He calls it a fairly new feature [12:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=776s): steer a local session from your phone or any browser [12:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=777s). Start a task at your desk and keep steering it while you're out [13:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=781s), [13:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=790s).
- He says your code never leaves your machine; only the connection is remote [13:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=784s), [13:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=787s). That's only partly true (see Caveats).

**28. Analytics without SQL** [13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s)
- Connect a CLI like BigQuery's bq [13:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=795s). Ask in plain English, e.g. last quarter's top 10 revenue sources, and Claude writes and runs the query [13:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=802s), [13:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=806s). He says it should work with any CLI tool [13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s).

**29. ultrathink** (announced as "28") [13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)
- Use it for architecture decisions, complex debugging and big refactors, or when a couple of prompts haven't worked [13:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=814s), [13:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=822s). Type the word and it turns colourful [13:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=824s). He says it allocates a maximum thinking budget of about 32,000 tokens [13:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=827s) (dated).
- Skip it for simple fixes, and use it for system-wide decisions or repeated misses [13:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=831s), [13:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=835s).

**30. Permissions for safe autonomy** [14:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=840s)
- Many creators, including him, have shown --dangerously-skip-permissions for speed, but it's named that for a reason [14:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=844s), [14:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=851s).
- Instead, explicitly allow commands you know are safe and deny destructive ones like deletes [14:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=857s), [14:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=860s). He claims this matches skip-permissions speed without the danger [14:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=864s). The deny list beats the allow list [14:32](https://www.youtube.com/watch?v=jqoFP9QapXI&t=872s).

**31. Agent teams** [14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)
- He says subagents can't talk to each other [14:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=879s), whereas agent teams can [14:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=883s). Teammates share a task list, communicate and assign each other work [14:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=888s), [14:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=891s). You can also talk to any agent directly [14:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=892s).
- Teams cost more and run longer, but give more cohesive output on big projects [15:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=900s).

**32. Context7 MCP** [15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s)
- He calls it a game-changer: install it, then prompt Claude to use it when you need current documentation [15:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=908s), [15:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=912s).
- Claude's training cutoff means it may suggest renamed, deprecated or missing APIs [15:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=917s), [15:21](https://www.youtube.com/watch?v=jqoFP9QapXI&t=921s). Context7 provides up-to-date, version-specific docs and code examples for thousands of libraries (Next.js, React, MongoDB). It injects them before Claude writes code [15:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=927s), [15:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=936s), [15:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=939s).
- He says it takes one command to install [15:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=946s), but the command isn't shown.

### [15:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=953s) Final Thoughts

- He wraps up by pointing viewers to a downloadable recap of the hacks [15:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=956s) (see Promotion under Caveats).

## Caveats & disagreements

**About the video**

- **Ideas, not demos.** No settings, hook config, skill contents or install commands are shown. Build from the Technique notes and the verified details under Beyond the source.
- **Numbering slip.** Ultrathink is announced as a second "28" [13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s). This note numbers it 29.
- **Unsourced claims.** He says plan mode and reasoning first "have been shown" to help [03:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=183s), [03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s), but cites nothing. Anthropic's best-practices guide backs planning, but says to skip it for changes you could describe in one sentence. His "always" [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s) is stronger than that.
- **Personal thresholds.** Compacting at 60% [02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s), the 95% confidence gates [03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s) and 150–200 CLAUDE.md lines [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s) are his own rules of thumb. The docs do suggest keeping CLAUDE.md under about 200 lines.
- **Permissions overclaim.** Allow/deny lists aren't "the same speed without the danger" [14:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=864s). Per the docs:
  - Deny rules don't stop subprocesses from reaching files indirectly.
  - Bypass mode belongs only in isolated containers or VMs.
  - Auto mode (classifier review) is the documented middle ground.
- **CAPTCHAs: flagged, not advice.** He floats browser automation "potentially" solving CAPTCHAs [09:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=588s), [09:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=596s). Bypassing CAPTCHAs generally violates site terms and defeats a deliberate human check, so the vault doesn't carry it forward. Claude in Chrome pauses and hands CAPTCHAs to you.
- **Hacks 24 and 32 pull in opposite directions.** One warns about MCP context cost [11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s), the other recommends an MCP server [15:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=908s). He frames hack 24 as situational [11:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=686s), which reconciles them (this note's reading).
- **Dated specifics** (checked 2026-09-15; details under Beyond the source):
  1. **/loop:** "3 days" [12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s). Recurring tasks now expire after 7 days and are restored on `--resume`.
  2. **ultrathink:** "~32,000 tokens" [13:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=827s). It now adds an in-context instruction and leaves the effort level unchanged. Current models use adaptive reasoning.
  3. **MCP cost:** "loads entire tool definitions" [11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s). MCP tool search (deferred loading) is now on by default.
  4. **/voice:** "still rolling out" [01:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=84s). Now documented hold/tap dictation that needs a claude.ai login.
  5. **Agent teams:** the flag goes unmentioned [14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s). They're experimental, need `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, and use far more tokens.
  6. **Subagents:** "can't talk to each other" [14:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=879s). Named subagents can now message each other.
  7. **Skills:** single files like techdebt.md [05:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=334s). The documented layout is `.claude/skills/<name>/SKILL.md`.
  8. **Remote Control:** "code never leaves your machine" [13:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=784s). Execution stays local, but the transcript is stored on Anthropic servers while connected. API keys aren't supported.
  9. **Models** reflect April 2026 (Haiku under Opus) [05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s). The current lineup includes Opus 5, Sonnet 5, Fable 5.1 and Haiku 4.5; see [[Choosing a Claude Model]].
- **Promotion.** The outro offers a free PDF in his community [15:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=956s). The description also has paid and affiliate links, none reproduced here.

**Versus existing vault notes**

- [[Claude Code]]: its scheduling table says /loop tasks expire after 7 days; he says 3 [12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s). The docs back 7.
- [[CLAUDE.md as a Router]]: he calls CLAUDE.md basically the system prompt [06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s). That note, citing the docs, says it arrives as a user message after the system prompt. His 150–200 line cap and routing out [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), [07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s) agree with that note's guidance.
- [[Build a Level 1 Second Brain]]: he says run /init on every project [00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s). That note says /init suits code repos and a personal brain's router is better written by hand. His advice assumes a codebase.
- [[Claude Code Auto Memory]]: he logs gotchas and corrections into CLAUDE.md or skills [06:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=400s), [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s). Per the docs, the vault keeps learned material (auto memory, including its `feedback` type) separate from standing instructions. He never mentions auto memory.
- [[Context vs Connections]]: that note wires connections through MCP. He hardcodes endpoints when tokens are tight [11:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=696s). With tool search now the default, measure with /context first.
- [[Grill Me Interview Skill]]: a refinement, not a clash. His version is a one-line AskUserQuestion prompt for aligning on a task [03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s). The skill is a deep interview that captures knowledge into a file.
- [[Always-On Brain OS]]: that note says in Claude Code you build the scheduling yourself. He names the pieces: /loop, desktop tasks, VPS and Remote Control [11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s), [12:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=744s), [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s), [12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s). None of them gives a self-refreshing memory, and he doesn't mention cloud Routines.

**Versus other sources in this batch**

- **Plan mode.** He says always start in it [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s). [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] keeps it for big tasks and skips it for typos or renames [07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s).
- **/init.** He runs it on every project [00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s); the Sloth rates it "pretty mid" [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s).
- **CLAUDE.md.** He keeps refreshing a file capped at 150–200 lines [06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s). [[Ras Mic - How AI Agents and Claude Skills Work]] says 95% of people don't need one [02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s).
- **Self-checks.** He gates each to-do on Claude's own 95% confidence [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s). [[AI LABS - The Unlazy Skill for Lazy Agents]] warns that checks the agent grades itself still leave the agent deciding when it's done [04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s).
- **Subagent cost.** He says Haiku subagents keep costs down [06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s). The Sloth says each subagent is a full conversation of its own, so even a small multi-agent setup can use up a $20 plan's limit [20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s).
- **Open problems vs specific prompts.** He says to give Claude problems and let it reason out the approach [03:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=198s). The Sloth wants "stupidly specific" prompts, or Claude reads everything to work out what you want [14:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=882s).

## Build from this

Hack numbers refer to the table. Thresholds that aren't his are marked.

1. **Session dashboard and hygiene routine.** A status line showing model, context % and cost, with a warning colour before 60% (warning level is a vault suggestion). Pair it with a routine:
   - scope context tightly;
   - run /context when a session feels heavy;
   - /compact at about 60% with keep-instructions, and /clear between tasks;
   - press Esc early, and /rewind wrong turns.

   Hacks 2, 4–6, 16, 18. See [[Context Hygiene Routine]].
2. **Plan-first alignment command.** Enter plan mode, then interview with AskUserQuestion until 95% confident. List assumptions, write a plan with a verification step after each build step, and wait for approval. Hacks 7–10. See [[Plan-First Workflow]] and [[Grill Me Interview Skill]].
3. **Verify-before-done UI loop.** Screenshot, compare with the reference and fix, up to three passes. Then do a browser pass for console errors and key flows. No to-do is ticked without evidence. Hacks 10, 20, 21. See [[Build Verification into Every Task]], [[Evidence-Gated Completion Ledger]], and [[Tests-First Goal Loop]] for code with tests.
4. **Lessons-learned loop.** After a rejected output is fixed, Claude proposes a one-line addition to the skill or CLAUDE.md. It flags when CLAUDE.md passes about 200 lines and suggests what to route out. Hacks 14, 15, 17. See [[Keep CLAUDE.md Lean]], [[Skill Improvement Loop]] and [[Build a Skill from a Successful Run]].
5. **Team SOP skill pack.** Package a tech-debt scan and a code review as skill folders committed to the repo. Hack 12. See [[Workflow Audit into Skills]].
6. **Cheap-reader subagent.** A Haiku researcher that reads long sources and returns a short structured summary to a stronger main thread. Hacks 11, 13. See [[Route Tasks to the Right Claude Model]].
7. **Parallel feature lanes.** One `claude --worktree <name>` per feature, a notification hook to tell you when a lane needs you, and a merge checklist. Hacks 19, 23. See [[Parallel Sessions with Git Worktrees]].
8. **Safe-autonomy baseline.** Allow read-only and test commands, ask before pushes and network calls, and deny destructive patterns. Add the sandbox or a PreToolUse hook as a backstop, and consider auto mode. Hack 30. See [[Configure Safe Autonomy Permissions]].
9. **Monitoring recipes.** Use /loop prompts for deploys, PRs and logs. Anything that must outlive the session or the 7-day expiry becomes a desktop task or cloud routine written to need no conversation context. Hacks 25–27. See [[Schedule Recurring Claude Tasks]] and [[Sync a Workspace to an Always-On Cloud Agent]].
10. **Lean-connection review.** Check each connection's cost in /context. Use a CLI or single endpoint for narrow needs, and add Context7 for library docs. Hacks 24, 28, 32. See [[Build a Context Map for a Connected Tool]].
11. **Reference-driven site build.** Collect inspiration screenshots, extract patterns, build, then run the screenshot loop. Hack 22. See [[Build a Distinctive Site with Design Skills]].
12. **Agent-team review.** 3–5 teammates (the docs' suggested range), each with a separate lens: security, performance, tests. Hack 31. See [[Multi-Agent Review and Scoring Loops]].

## Resources mentioned

- **Claude Code features:** /init, /statusline, /voice, /context, /compact, /clear, plan mode, AskUserQuestion, subagents, skills, /rewind, /hooks, `claude --worktree`, /loop, desktop scheduled tasks, Remote Control, ultrathink, permission lists, --dangerously-skip-permissions, agent teams.
- **Models:** Haiku and Opus [05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s).
- **Other tools:** Chrome DevTools [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s), Notion [11:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=701s), BigQuery bq CLI [13:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=795s), Telegram [12:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=767s), GitHub [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s), Context7 MCP [15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s), a VPS [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s), and a system-wide dictation app [01:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=87s).

## Beyond the source

*Not from the video. Each item was checked on 2026-09-15 at the linked page.*

- **Scheduling (hack 25).**
  - **`/loop` tasks.** Recurring tasks expire 7 days after creation. They're session-scoped (they fire only while Claude Code is running), and `--resume`/`--continue` restores unexpired ones; a self-paced `/loop` must be restarted. Plain-language one-off reminders delete themselves after firing.
  - **Desktop scheduled tasks.** Each run starts a fresh session, and the app must be open with the computer awake.
  - **Cloud Routines.** They run in the cloud (Anthropic-managed by default) against a fresh clone rather than your local files, with a one-hour minimum interval, and don't need your machine on.

  <https://code.claude.com/docs/en/scheduled-tasks>, <https://code.claude.com/docs/en/desktop-scheduled-tasks>
- **ultrathink (hack 29).** The keyword adds an in-context instruction for deeper reasoning on that turn, and the effort level sent to the API is unchanged. Phrases like "think hard" are ordinary text. Fable models, Sonnet 5 and Opus 4.7+ always use adaptive reasoning. Only Opus 4.6 and Sonnet 4.6 can be switched back to a fixed thinking budget, with `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. Use `/effort` to set depth for the whole session. <https://code.claude.com/docs/en/model-config>
- **MCP context cost (hacks 24, 28).** MCP tool search is on by default (v2.1.221+), so tool definitions are deferred and load on demand. `ENABLE_TOOL_SEARCH=false` or a custom `ANTHROPIC_BASE_URL` turns it off. Anthropic's best-practices guide calls CLI tools the most context-efficient way to reach external services. <https://code.claude.com/docs/en/mcp>, <https://code.claude.com/docs/en/best-practices>
- **Voice (hack 3).** Enable with `/voice`, then hold Space to talk, or use `/voice tap` to tap to start and send. Audio streams to Anthropic for transcription and doesn't use tokens. It needs a claude.ai account and a local microphone, so it won't work over SSH. <https://code.claude.com/docs/en/voice-dictation>
- **Subagents (hacks 11, 13).** Each starts with a fresh, separate context window. They're defined in `.claude/agents/` or `~/.claude/agents/`, and `model:` accepts `haiku`, `sonnet`, `opus`, `fable`, a full ID or `inherit`. Subagents Claude names at spawn can message each other via `SendMessage`. <https://code.claude.com/docs/en/sub-agents>
- **Agent teams (hack 31).** Experimental and off by default; enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in the environment or the `env` block of settings.json. Teammates have their own contexts, share a task list, message each other, and can be addressed directly. They use significantly more tokens. The docs suggest starting with 3–5 teammates, giving each its own files, and there's one team per session. <https://code.claude.com/docs/en/agent-teams>
- **Skills (hack 12).** A skill is a folder containing `SKILL.md` and optional supporting files. Project skills live in `.claude/skills/<name>/` (commit to share), personal ones in `~/.claude/skills/<name>/`. You invoke one with `/name`, or Claude invokes it when its `description` matches; `disable-model-invocation: true` makes it manual-only. Legacy `.claude/commands/<name>.md` files still work. <https://code.claude.com/docs/en/skills>
- **Remote Control (hack 27).** Start it with `/remote-control` (`/rc`), `claude --remote-control` or `claude remote-control`, and connect from claude.ai/code or the Claude app. Execution and files stay local, using outbound HTTPS only. While connected, the session transcript (messages, responses, tool activity) is stored on Anthropic servers, and all traffic goes through the Anthropic API. It needs a claude.ai login (API keys aren't supported), and on Team and Enterprise an Owner must enable it. <https://code.claude.com/docs/en/remote-control>
- **Permissions (hack 30).** Rules are checked deny → ask → allow, with the first match winning. A deny in any scope beats an allow. Read/Edit deny rules don't cover subprocesses that open files indirectly; use the sandbox for OS-level enforcement. `bypassPermissions` is for isolated containers or VMs only. Auto mode, where a classifier reviews actions instead of you, is the default starting mode on Pro, Max and Team. <https://code.claude.com/docs/en/permissions>, <https://code.claude.com/docs/en/permission-modes>
- **Plan mode and interviews (hacks 7, 9).** Shift+Tab cycles modes, and `/plan` puts a single prompt in plan mode. Plan mode explores without editing until you approve. The best-practices guide recommends explore → plan → implement → commit, but says to skip planning for one-sentence changes. It also suggests having Claude interview you with `AskUserQuestion` (multiple-choice questions), write a spec, and then implement in a fresh session. <https://code.claude.com/docs/en/best-practices>, <https://code.claude.com/docs/en/tools-reference>
- **Verification (hacks 10, 20).** The best-practices guide's first tip is to give Claude a check it can run (tests, a build, a screenshot comparison) and have it show evidence. Stronger gates are a `/goal` condition, a Stop hook that blocks the turn from ending, or a verification subagent. <https://code.claude.com/docs/en/best-practices>
- **Browser tooling (hack 21).**
  - **Claude in Chrome** (`claude --chrome` or `/chrome`) shares your login state, reads console errors and fills forms. It pauses at login pages and CAPTCHAs for you to handle, and needs a Pro, Max, Team or Enterprise plan. <https://code.claude.com/docs/en/chrome>
  - **Google's Chrome DevTools MCP** installs as a plugin: `/plugin marketplace add ChromeDevTools/chrome-devtools-mcp`, then `/plugin install chrome-devtools-mcp@chrome-devtools-plugins`. Google warns it exposes browser content to the agent. <https://developer.chrome.com/docs/devtools/agents/get-started>
- **Status line and hooks (hacks 2, 19).** `/statusline <description>` writes a script into `~/.claude/` and adds a `statusLine` setting. The script reads session JSON with fields such as `model.display_name`, `context_window.used_percentage` and `cost.total_cost_usd`. The `Notification` hook event fires when Claude waits for input or permission, and the docs show a macOS `osascript` example. `/hooks` is a read-only browser: add hooks by editing settings or asking Claude. <https://code.claude.com/docs/en/statusline>, <https://code.claude.com/docs/en/hooks-guide>
- **Worktrees (hack 23).** `claude --worktree <name>` (or `-w`) creates `.claude/worktrees/<name>/` on a `worktree-<name>` branch; gitignore that folder. Each worktree is a fresh checkout, so install dependencies there, and list gitignored files like `.env` in `.worktreeinclude` to copy them in. On exit, a clean worktree from an unnamed session is removed automatically; a named session, or a worktree with changes or new commits, prompts you to keep or remove it. <https://code.claude.com/docs/en/worktrees>
- **/rewind, /compact, /context (hacks 5, 6, 18).** `/rewind` (or Esc twice) restores code, conversation or both, or summarizes from a chosen point; it doesn't track Bash-made file changes. `/compact` takes optional focus instructions, and auto-compaction also runs. `/context` shows usage with optimization suggestions. <https://code.claude.com/docs/en/checkpointing>, <https://code.claude.com/docs/en/commands>
- **CLAUDE.md (hacks 1, 14, 15).** `/init` generates a starter file. The docs suggest under about 200 lines per file, since longer files use more context and reduce adherence. CLAUDE.md is delivered as a user message after the system prompt. <https://code.claude.com/docs/en/memory>
- **Context7 (hack 32).** Made by Upstash. Set up with `npx ctx7 setup`, or add the MCP server at `https://mcp.context7.com/mcp` (or locally with `npx @upstash/context7-mcp`). An API key is optional and raises rate limits. Trigger it with "use context7". <https://github.com/upstash/context7>
- **Telegram (hack 26).** Claude Code Channels (research preview) include a Telegram plugin that pushes messages into a running session and replies back. Messages arrive only while that session is open. <https://code.claude.com/docs/en/channels>
- **Model aliases (hack 13).** On the Anthropic API, `opus` maps to Opus 5, `sonnet` to Sonnet 5 and `fable` to Fable 5.1; `haiku` selects the latest Haiku model. <https://code.claude.com/docs/en/model-config>

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Cloudcode", "Cloud code", "Cloud" | Claude Code / Claude (captions switch to "Claude" from about 10:10) |
| "cloud.md" | CLAUDE.md |
| "{slash} init" … "{slash} loop" | /init, /statusline, /voice, /context, /compact, /clear, /rewind, /hooks, /loop |
| "voice tate" | dictate |
| "ask user question tool" | AskUserQuestion tool |
| "{dot}cloud/skills" | .claude/skills |
| "Claude {dash} {dash} work tree" | `claude --worktree <feature-name>` |
| "there's no SQL data analytics" | analytics without writing SQL (not NoSQL) |
| "BigQuery's BQ tool" | BigQuery's `bq` CLI |
| "Number 28 is ultra think" | Hack 29, `ultrathink` |
| "dangerously skip permissions" | `--dangerously-skip-permissions` |
| "Context 7 MCP" | Context7 MCP server (Upstash) |
| "up to eight version-specific technical documentation" | up-to-date, version-specific documentation |
| "Chrome DevTools" | probably the Chrome DevTools MCP server; possibly Claude in Chrome (*uncertain*) |
| "How should we handle growth tracking?" | example design question; topic may be garbled (*unclear in captions*) |
| "free school community" | free Skool community (AI Automation Society) |

## Related

- **Concepts:** [[Context Window Management]], [[Agent Laziness]], [[Plan Before Executing]], [[Verification Before Done]], [[Loop Engineering]], [[Agent Skills]], [[Build vs Install Third-Party Skills]], [[Subagents and Agent Teams]], [[Choosing a Claude Model]], [[Connecting Claude to External Tools]], [[Permissions and Approval Gates]], [[Routines and Scheduled Tasks]], [[Agent Memory Patterns]], [[Claude Code Auto Memory]], [[CLAUDE.md as a Router]], [[Context vs Connections]], [[Always-On Brain OS]], [[Design for Retrieval]], [[Escaping the Default AI Design Look]]
- **Techniques:** [[Context Hygiene Routine]], [[Plan-First Workflow]], [[Build Verification into Every Task]], [[Tests-First Goal Loop]], [[Multi-Agent Review and Scoring Loops]], [[Workflow Audit into Skills]], [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]], [[Parallel Sessions with Git Worktrees]], [[Route Tasks to the Right Claude Model]], [[Configure Safe Autonomy Permissions]], [[Schedule Recurring Claude Tasks]], [[Sync a Workspace to an Always-On Cloud Agent]], [[Keep CLAUDE.md Lean]], [[Build a Level 1 Second Brain]], [[Tiered Lookup Routing]], [[Grill Me Interview Skill]], [[Build a Distinctive Site with Design Skills]], [[Build a Context Map for a Connected Tool]], [[Evidence-Gated Completion Ledger]]
- **Tools:** [[Claude Code]], [[Claude in Chrome]], [[Claude Design]]. The vault covers other always-on routes relevant to hack 26 in [[OpenClaw]] and [[Syncthing]]; the video doesn't mention them.
- **People:** [[Nate Herk]], [[Matt Pocock]] (original Grill Me skill, which hack 9 resembles), and [[Andrej Karpathy]] (the LLM Wiki pattern behind the vault's routing notes; not in this video).
- **Same creator:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **Sources in this batch that compare against it:** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- [[Home]]
