---
type: source
title: "I Have Spent 1000+ Hours With Claude Code. This Is What I Learned"
creator: "[[The Coding Sloth]]"
channel: "The Coding Sloth"
url: https://www.youtube.com/watch?v=YAsxyoTWFDA
video_id: YAsxyoTWFDA
published: 2026-08-18
duration: "22:30"
ingested: 2026-09-15
topics: [claude code features, tier list, verification, plan mode, skills, mcp, context management, token budgeting, loops, goal command, subagents, git worktrees, model routing, coding agent alternatives]
tags: [source/youtube, topic/claude-code, topic/verification, topic/planning, topic/skills, topic/mcp, topic/context, topic/models, topic/loops, topic/scheduling, topic/subagents, topic/portability, topic/agents]
---

# The Coding Sloth - 1000 Hours of Claude Code Lessons

> **Creator:** [[The Coding Sloth]] · **Published:** 2026-08-18 · **Length:** 22:30 · [Watch on YouTube](https://www.youtube.com/watch?v=YAsxyoTWFDA)

## TL;DR

[[The Coding Sloth]] is a developer on the $20 Pro plan. This video is his comic, opinionated tier list of [[Claude Code]] features, mixed with habits for stretching tight usage limits.

- **Top tiers:**
  - **Verification** (S, up to "SSS"): tests written before code, type checks, linters, and screenshot or browser checks.
  - **Plan mode** (S): for big tasks only, ideally with a strong model planning and a cheaper one building.
  - **Skills** (A, or S if used well).
- **MCPs** are A tier, but only for reaching systems outside the codebase.
- **CLAUDE.md** is where you counter the model's bad habits. It isn't make-or-break, and `/init` is "mid".
- **Context rules:** tokens are the budget, so run one task per session, stop tangents, be very specific, and start fresh after an auto-compact.
- **Plan-dependent features:** `/goal` and subagents move up a tier with bigger limits. Worktrees are A tier, and `/loop` runs his side-project automations.

Treat it as experience, not measurement:

- The ratings are subjective, and some footage is a month old.
- He now uses [[OpenAI Codex]] most, for its limits.
- A few claims don't match the docs, such as a "300K" context limit and `/loop` as unattended automation. See Caveats and Beyond the source.

## Key takeaways

- **Verification comes first.**
  - It's his top rating [08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s). Without a check, Claude can't tell whether its code is correct [08:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=535s).
  - Write tests before code. Otherwise Claude writes tests fitted to its own implementation [09:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=554s).
  - Test only what matters [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s).
  - See [[Verification Before Done]], [[Build Verification into Every Task]] and [[Tests-First Goal Loop]].
- **Plan only big changes.**
  - Claude explores before acting, and errors are cheaper to catch in a plan [07:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=431s), [07:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=436s).
  - Skip it for typos and renames [07:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=444s).
  - See [[Plan Before Executing]] and [[Plan-First Workflow]].
- **A strong model plans, a cheap model builds.**
  - Fast models can now implement a good plan, and it saves money [07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s), [07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s).
  - In Claude Code he uses Opus to plan and Sonnet to build [08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s).
  - See [[Choosing a Claude Model]] and [[Route Tasks to the Right Claude Model]].
- **Tokens are the budget, and a fuller window makes Claude worse** [12:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=771s), [13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s).
  - Run one task per session [14:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=844s).
  - Stop tangents and name the files to use [14:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=870s), [14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s).
  - Start fresh if Claude auto-compacts mid-task [15:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=913s).
  - See [[Context Window Management]], [[Context Hygiene Routine]] and [[Agent Laziness]].
- **CLAUDE.md counters quirks; skills carry procedures.**
  - Add rules for habits you've watched the model repeat [04:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=254s).
  - The file isn't make-or-break, and skills can do as well [04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s).
  - See [[Keep CLAUDE.md Lean]] and [[CLAUDE.md as a Router]].
- **Curate skills and MCPs.**
  - Keep to one family of skills, because skills disagree about good code [08:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=498s), [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s).
  - Use MCPs only for systems outside the codebase [10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s).
  - See [[Build vs Install Third-Party Skills]] and [[Connecting Claude to External Tools]].
- **Match power features to your plan.**
  - Each subagent is a full parallel conversation and can drain a $20 limit [20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s), [20:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1216s).
  - `/goal` is B tier on low plans and A on high ones [19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s).
  - One worktree per chat keeps parallel agents apart [20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s).
  - See [[Subagents and Agent Teams]] and [[Parallel Sessions with Git Worktrees]].
- **Stay the engineer.**
  - Coding knowledge is why these tips work [16:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=980s).
  - Have Claude explain each change [16:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1007s).

## The tier list at a glance

These are his personal ratings, and they assume the $20 Pro plan [00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s). Graded features are listed highest first. The last three rows are features he discussed without giving a letter.

| Feature | His tier | His reasoning | When | Vault note |
|---|---|---|---|---|
| Verification | S, up to "triple S" | Basic engineering that AI makes more important | [08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s) | [[Verification Before Done]] |
| Plan mode | S *(garbled in captions)* | Explores first; a plan is easier to check than 3,000 lines; big tasks only | [06:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=411s) | [[Plan Before Executing]] |
| Skills | A, "easy S" if smart | Reusable guides; reading community skills teaches you too | [05:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=307s) | [[Agent Skills]] |
| Subagents | A; S with high limits | Much better implementations, but they drain a $20 plan | [20:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1223s) | [[Subagents and Agent Teams]] |
| Worktrees | A | One folder and branch per chat, so agents stay isolated | [20:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1232s) | [[Parallel Sessions with Git Worktrees]] |
| MCPs | "B… actually A" | Only for systems outside the codebase | [10:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=600s) | [[Connecting Claude to External Tools]] |
| `/goal` | B on low plans, A on high | Works until a goal like "tests pass, no type errors" is met | [19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s) | [[Tests-First Goal Loop]] |
| `/teleport` and Remote Control | A if you're out a lot; C/D for him | Moves sessions between phone, web and terminal | [11:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=713s) | [[Claude Code]] |
| Built-in code review and security review skills | B/A | A good bonus after a feature is built | [05:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=332s) | [[Build Verification into Every Task]] |
| `/voice` | B | More descriptive prompts; keeps your technical thinking sharp | [10:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=651s) | [[Claude Code]] |
| `/context` | B | Check before big tasks; the number alone fixes nothing | [13:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=827s) | [[Context Hygiene Routine]] |
| `/compact` | C when Claude triggers it; B when you do | Self-triggered mid-task compaction drops quality | [15:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=903s) | [[Context Window Management]] |
| `/btw` | C | Side question with no tools and no history impact | [11:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=670s) | [[Claude Code]] |
| `!` shell mode | C, "underrated" | Normal shell command whose output Claude sees | [12:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=721s) | [[Claude Code]] |
| `/init` | C or D; later "pretty mid" | Scans code into CLAUDE.md; the interview version shows promise | [04:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=242s), [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s) | [[Keep CLAUDE.md Lean]] |
| `/radio` | F for productivity, "triple S for vibes" | Opens Claude FM lo-fi music | [12:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=739s) | none |
| CLAUDE.md file | No letter; "moving that up" | Where you counter model quirks; not make-or-break | [04:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=253s) | [[CLAUDE.md as a Router]] |
| `/loop` | No letter; a life-changing command *(captions: "live-changing")* | AI cron job that keeps side projects moving | [18:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1080s) | [[Routines and Scheduled Tasks]] |
| Ultraplan | No letter; since removed | Nobody seemed to use it | [02:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=130s) | [[Plan Before Executing]] |

## Notes by chapter

The video has no chapter markers, so these sections follow the order of the talk.

### [00:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=0s) Intro: the usage-limit complaint

- **Usage limits are his main gripe.** A trivial message can use his allowance and force a three-hour wait [00:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=3s), [00:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=7s).
- **His plan:** he codes on the $20 plan and has hit the limit within one or two prompts [00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s), [00:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=23s). He suspects tight limits keep people from getting enough practice to see good results [00:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=25s) (captions garbled).
- **Dated footage:** he says much of it was recorded about a month earlier [00:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=13s).
- **What he promises:** his workflow, favourite MCPs and skills [00:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=33s), and token-saving habits [00:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=37s).

### [00:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=51s) What Claude Code is, and why learn it

- **What it is:** Claude specialised for coding, running in the terminal [00:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=55s).
  - He prefers an IDE-plus-agent setup [00:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=58s).
  - Claude Code also runs in IDEs and on the web [01:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=72s).
- **Why learn it** (claims checked in Beyond the source):
  - Wide adoption, with a jab that Uber overdid it [01:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=77s).
  - Roughly $1B in six months [01:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=81s).
  - Competitors copying it [01:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=84s).
  - Employers asking for it [01:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=101s).
- **What transfers:** most concepts carry over to other agents, and since the video isn't sponsored he covers alternatives too [01:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=106s), [01:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=110s). See [[Tool-Agnostic Context Files]].

### [01:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=113s) Choosing what to rank

- **Research:** posts, videos, Anthropic's tutorials and material from Claude Code's creator [01:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=116s), [02:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=120s). He found more than 80 commands and features [02:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=125s).
- **Ultraplan** existed, but nobody seemed to use it [02:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=130s). An insert says it has since been removed [02:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=137s).
- **Scope:** most commands are configuration or not useful, so he tier-ranks only the essentials [02:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=147s), [02:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=152s).

### [03:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=186s) `/init` and CLAUDE.md

- **`/init`** is meant to be run when you first open a project. Claude reads the codebase and writes CLAUDE.md [03:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=189s), [03:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=194s).
  - He calls that file Claude's permanent memory for the project [03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s). See Caveats and [[Claude Code Auto Memory]].
- **AGENTS.md gripe:** other agents use AGENTS.md, and Claude doesn't [03:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=206s).
  - His workaround is to import AGENTS.md inside CLAUDE.md instead of symlinking [03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s), [03:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=219s).
  - See [[Tool-Agnostic Context Files]] and [[Port a Claude Code Brain to Other Agents]].
- **Experimental `/init`:** behind an environment flag, it interviews you instead of scanning, and it recommends skills and hooks. He sees potential in it [03:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=225s), [03:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=231s), [03:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=236s).
- **Rating:** C or D [04:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=242s). A month later it's still "pretty mid" [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s).
- **CLAUDE.md itself moves up** [04:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=253s). After months you learn each model's habits, and this file is where you counter them [04:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=254s).
- **His CLAUDE.md contains:**
  - a project description and status [04:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=267s)
  - his coding style [04:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=271s)
  - an experimental "working philosophy" section [04:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=275s)
  - a rule against ALL-CAPS text shown to users, because models love all caps in their designs [04:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=277s), [04:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=284s)
  - the language to use for pull requests [04:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=290s)
- **How to treat it:** keep it flexible [04:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=293s). It isn't make-or-break, and skills can match or beat it [04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s). See [[Keep CLAUDE.md Lean]].

### [05:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=305s) Skills

- **Rating:** A tier, and an easy S if used smartly [05:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=307s).
- **What a skill is:** a SKILL.md holding instructions for a task you repeat. Claude uses it when it's relevant or when you ask [05:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=311s), [05:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=317s).
  - Examples: best practices, a workflow, a research method [05:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=320s).
  - See [[Agent Skills]].
- **Built-in code review and security review skills:** B/A. They're worth running after Claude implements a feature [05:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=329s), [05:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=332s).
- **Community skills** package the know-how of companies and top engineers, and reading them has taught him a lot [05:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=342s), [05:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=352s).
  - He finds them on skills.sh and in GitHub repos [05:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=357s), [06:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=361s).
- **Favourites:**
  - **[[Matt Pocock]]'s skills.** grill-with-docs refines requirements [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s). improve-codebase-architecture he likes partly for its visual output [06:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=377s), [06:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=381s). grill-with-docs is a code-focused relative of [[Grill Me Interview Skill]].
  - **Cursor's thermo-nuclear code quality review.** It simplifies AI-written code and strips out slop [06:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=384s), [06:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=390s). He runs it alongside improve-codebase-architecture [06:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=399s). [[AI LABS - Types of Claude Loops Explained]] models a scoring reviewer on it; see [[Multi-Agent Review and Scoring Loops]].
  - **shadcn's improve.** It audits a codebase and writes plans for other agents to carry out [06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s), [06:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=407s).

### [06:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=411s) Plan mode, and planning with a stronger model

- **Rating:** S tier (garbled in captions) [06:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=411s).
- **How it works:** Shift+Tab enters plan mode [06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s). Claude reads the code more thoroughly, writes a full plan, and waits for you to approve or deny it [06:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=418s), [07:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=425s).
- **Why:** results improve because Claude explores first [07:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=427s), [07:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=431s). A mistake is also easier to spot in a plan than in 3,000 lines across 12 files [07:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=436s).
- **When not to:** typos, renames or small design tweaks, where it's wasted effort [07:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=444s), [07:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=449s).
- **Plan big, build cheap** (the idea behind shadcn's improve skill) [07:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=452s). He expects it to become the default approach [07:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=453s).
  - A smart model plans, and a cheaper, faster one implements [07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s), [07:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=459s).
  - Fast doesn't mean dumb, and the split saves money [07:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=464s), [07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s).
  - In Claude Code he'd have planned with Fable [07:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=475s). Fable now needs usage credits, so he plans with Opus and builds with Sonnet [08:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=480s), [08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s).
  - Cursor, OpenCode and Codex let you mix models from different vendors [08:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=487s).
  - See [[Route Tasks to the Right Claude Model]] and [[Plan-First Workflow]].
- **Skill hygiene** [08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s):
  - Don't install a hundred skills [08:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=494s).
  - Skills are opinionated about what good code is, so stick to one family that matches your style [08:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=498s), [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s).
  - See [[Build vs Install Third-Party Skills]].

### [08:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=511s) Verification

- **Rating:** S, even double or triple S [08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s). He calls it a practice rather than a feature [08:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=513s): basic engineering that AI makes more important [08:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=525s).
- **What it means:** give Claude a way to test its output before it declares the work finished. Otherwise it can't tell whether the code is correct [08:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=531s), [08:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=535s). See [[Verification Before Done]].
- **Tests:**
  - Write them first, then implement [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s).
  - If Claude implements first, its tests are fitted to its own code, which he calls cheating [09:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=554s), [09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s).
  - Test only the most important behaviour. Smart models over-test and bloat the codebase [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s), [09:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=563s).
- **Type checkers and linters:** have Claude run them before it calls a task done [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s).
- **Frontend:**
  - Screenshot and browser testing let an otherwise blind Claude open the app, click around and see the results [09:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=578s), [09:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=582s), [09:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=587s).
  - This once needed MCPs and is now built in [09:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=596s).
  - See [[Claude in Chrome]] and [[Build Verification into Every Task]].

### [09:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=597s) MCPs

- **Rating:** "B tier… actually A" [10:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=600s).
- **What they connect:** GitHub, databases, Slack, analytics, deployments and browsers [10:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=602s), [10:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=608s).
- **His uses:** design inspiration, seeding a database with fake data, researching docs, and browser testing [10:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=611s), [10:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=617s).
- **His rule:**
  - An MCP is only warranted when Claude must interact directly with something outside the codebase [10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s).
  - Patterns and how-to knowledge belong in skills [10:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=626s).
  - Install only what's necessary [10:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=635s), [10:40](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=640s).
  - See [[Connecting Claude to External Tools]].

### [10:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=644s) Underrated commands

- **`/voice` (B)** [10:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=651s):
  - Your speech becomes the prompt [10:54](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=654s).
  - Speaking makes it easier to be descriptive and think aloud [10:59](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=659s), and helps keep your technical knowledge sharp [11:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=663s).
  - It beats slow typing [11:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=666s).
- **`/btw` (C)** [11:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=670s):
  - Ask a question mid-task without interrupting Claude or changing the history [11:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=673s).
  - It can't read files or run commands, only draw on the conversation so far [11:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=682s).
  - That makes it good for asking why Claude made a decision [11:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=689s).
- **`/teleport` and Remote Control** [11:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=695s):
  - They move sessions between phone, web and terminal [11:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=698s).
  - His example: start an idea in the mobile app while waiting at a drive-thru, then pick it up in the terminal at home [11:48](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=708s).
  - A tier if you're out a lot; C or D for him [11:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=713s), [11:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=716s).
- **`!` shell mode (C, underrated)** [12:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=721s): start a message with `!` to get a normal shell, and Claude also sees the output [12:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=729s), [12:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=734s).
- **`/radio`** (F for productivity, triple S for vibes) opens Claude FM, a lo-fi music stream [12:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=739s), [12:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=743s).

### [12:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=754s) Tokens and the context window

- **Who this applies to:** anyone on the $20, $100 or $200 plan [12:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=762s), [12:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=769s).
- **How usage is metered:** in tokens, not prompts. Messages, file reads and responses all count [12:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=771s), [12:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=775s).
- **The "dumb zone."** The context window is Claude's short-term memory [13:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=790s). The more of it you use, the worse Claude gets: it forgets things and contradicts itself [13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s), [13:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=797s).
  - He cites limits of "about 300,000" and a million tokens [13:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=801s).
  - A bigger window only stretches the dumb zone [13:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=811s).
  - In his experience, quality and usage both suffer beyond roughly 100K–200K tokens [13:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=817s).
- **`/context` (B)** shows usage. Run it before big tasks, though the number alone fixes nothing [13:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=827s), [13:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=833s).
- **Tip 1: a new session per task** [14:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=844s).
  - A medium or big task uses at least ~50K tokens, and research, skills or MCPs push it past 100K [14:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=853s), [14:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=857s).
  - Chaining tasks makes the output worse and burns your limit [14:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=863s).
- **Tip 2: stop research tangents at once.** Every file and page Claude reads costs tokens [14:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=870s), [14:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=875s). Point Claude at the files and sources it should use [14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s).
- **Tip 3: be very specific.** Vague prompts make Claude read everything, and specificity matters most for technical decisions [14:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=885s), [14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s), [14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s).
- **`/compact`:**
  - C tier when Claude triggers it, B when you use it well [15:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=903s). It summarises the history so it fits the window [15:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=908s).
  - If Claude compacts itself mid-task, start a new session, because quality visibly drops [15:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=913s), [15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s).
  - If the task must stay in one conversation, compact manually and say exactly what to keep [15:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=926s).
- **More tools:** community tools for saving context are linked in the description [15:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=933s).
- See [[Context Window Management]], [[Context Hygiene Routine]] and [[Agent Memory Patterns]].

### [15:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=939s) The "for loop" satire

- **The joke:** he mocks the AI loop trend as people rediscovering the for loop, and says object-oriented prompting is surely next [15:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=947s), [15:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=953s).
- **His point:** old ideas keep getting rebranded, and people who can't code don't notice [16:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=968s), [16:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=974s). For the vault's serious take, see [[Loop Engineering]].
- **Learn to code:** it's why these tips work [16:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=980s), and it means you aren't stranded when you hit your limit [16:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=985s).
- **Use AI to get smarter:** have Claude teach as it goes and explain every change [16:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1004s), [16:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1007s).

### [17:59](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1079s) `/loop` automations

- **What `/loop` does:** repeats a task on an interval, like an AI cron job [18:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1084s), [18:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1087s).
- **Why he uses it:** he doesn't work on his side projects daily, so loops act as routines that make progress while he's away [18:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1096s), [18:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1102s). See Caveats for why this is doubtful.
- **His automations** [18:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1106s):
  1. **Daily issue worker:** picks an open GitHub issue, works on it, and leaves a PR [18:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1111s), [18:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1114s).
  2. **Security and bug sweep:** scans for known vulnerabilities and bugs, and files GitHub issues for what it finds [18:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1118s), [18:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1124s).
  3. **Feature brainstorm:** reads the code, PRs and issues to suggest useful features [18:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1129s), [18:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1132s).
- **Event triggers:** automations can also fire when something happens [18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s). He believes companies and open-source maintainers are trying this with decent results [19:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1140s).
- See [[Routines and Scheduled Tasks]] and [[Schedule Recurring Claude Tasks]].

### [19:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1145s) `/goal`

- **Which command:** the name is garbled in the captions, but the behaviour matches `/goal` [19:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1145s).
- **What it does:** Claude keeps working until the goal is met or it needs you [19:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1149s). His example goal is every test passing with no type errors [19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s).
- **Rating:** B on lower plans; A on higher plans or with unlimited tokens [19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s).
- See [[Tests-First Goal Loop]] and [[Loop Engineering]].

### [19:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1170s) Subagents

- **What they are:** the main chat is the "daddy agent" [19:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1174s). A subagent is a mini Claude it starts for one job, such as researcher, reviewer or debugger [19:40](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1180s), [19:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1185s).
- Each subagent has its own context window and reports back a summary [19:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1191s), [19:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1193s).
- **Creating one:** the easiest way is to ask Claude to make it, describing the job [20:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1200s).
- **Cost:** each subagent is a full parallel conversation [20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s). A modest multi-agent setup can use up a $20 plan's limit before the task is done [20:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1216s).
- **Rating:** still A, and easily S on bigger plans, because implementation quality improves a lot [20:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1223s), [20:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1228s).
- See [[Subagents and Agent Teams]].

### [20:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1232s) Worktrees

- **Rating:** A tier [20:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1232s).
- **What they are:** a worktree checks out a branch of the same repo into its own folder, which suits parallel AI work [20:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1234s), [20:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1238s), [20:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1242s).
- **His workflow:** every chat gets its own worktree. Branches move forward in parallel, and agents can't collide [20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s), [20:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1252s).
- Claude Code supports worktrees natively [20:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1256s). See [[Parallel Sessions with Git Worktrees]].

### [21:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1260s) Alternatives

- **[[OpenAI Codex]]:** his most-used tool now. Its limits are generous, and someone he calls "Tibo" keeps resetting them [21:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1268s), [21:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1270s), [21:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1274s).
- **OpenCode:** an open-source equivalent of Claude Code that works with any model [21:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1280s), [21:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1283s).
- **Pi:** a minimalist harness for people who want to build their own workflow [21:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1288s), [21:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1291s).
- **Cursor:** his pick when he wants an IDE plus an agent. He likes its fast, cheap models, naming Grok and Composer [21:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1298s), [21:43](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1303s).
- **VS Code with GitHub Copilot:** the original [21:48](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1308s).
- **T3 Code:** an open-source control plane for coding agents [21:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1317s). It gives a Claude subscription a nicer UI [22:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1320s) and can run several subscriptions from one app [22:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1331s).

## Caveats & disagreements

**About the video**

- **Omitted:** the sponsor (Brilliant, about 16:51–17:57), his newsletter plug (02:38–03:02) and the affiliate links in the description.
- **Subjective ratings.** They come from a $20 Pro user [00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s) who now prefers Codex for its limits [21:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1270s). The captions show no hands-on demo.
- **Dated footage** [00:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=13s). The inserts are right on two points:
  - Ultraplan has been removed [02:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=137s).
  - Fable needs usage credits [07:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=478s). That applies to Pro, not Max (Beyond the source).
- **Context figures.** "300K" [13:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=801s) isn't a documented window size; the docs list 200K and 1M. His 100K–200K threshold [13:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=817s) is anecdote.
- **`/loop` isn't unattended automation** [18:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1102s).
  - Per the docs, it's session-scoped and recurring tasks expire after 7 days.
  - His daily and event-driven jobs [18:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1111s), [18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s) fit cloud Routines, Desktop scheduled tasks or GitHub triggers instead.
  - Cloud Routines run without approval prompts (Desktop tasks set this per task), so limit which repos and connectors they can reach.
  - See [[Routines and Scheduled Tasks]], [[Permissions and Approval Gates]] and [[Configure Safe Autonomy Permissions]].
- **"Built in, no MCP needed" is loose** [09:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=596s). Browser testing in the CLI uses the Claude in Chrome extension, which shows up as its own MCP server. See [[Claude in Chrome]].
- **Plan approval** now offers more than approve or deny [07:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=425s); see Beyond the source.
- **The `/goal` name** is inaudible [19:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1145s).
- **Community token tools** are only linked [15:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=933s). JetBrains measured caveman at about 8.5% output-token savings on benchmark tasks run in Claude Code, against an advertised 65%.

**Conflicts with existing vault notes (both sides kept)**

- **[[CLAUDE.md as a Router]]: foundation or optional?**
  - *Vault:* following [[Nate Herk - Every Level of a Claude Second Brain]], every brain starts from a router file ([04:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=260s)). See [[Build a Level 1 Second Brain]].
  - *This video:* it isn't make-or-break, and skills can do as well [04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s). His file holds quirk rules, not routes [04:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=267s).
  - *Reconciled:* a notes brain needs routes, because nothing else says where knowledge lives. A code repo largely describes itself, so the file can shrink to the rules the model keeps breaking. Both views say keep it lean ([[Keep CLAUDE.md Lean]]).
- **[[CLAUDE.md as a Router]]: does Claude search everything?**
  - *Vault:* Nate Herk says it won't search the whole codebase on its own ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)).
  - *This video:* vague prompts make it read everything [14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s).
  - *Reconciled:* the fix is the same either way: tell Claude where to look. Anthropic's cost docs side with this video on vague prompts.
- **[[CLAUDE.md as a Router]]: `/init`.** That note presents `/init` as a generator for a starter file. This video calls it mid [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s) and points to the interview version, which also proposes skills and hooks [03:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=225s). That's a refinement, not a contradiction.
- **[[Claude Code Auto Memory]]: "permanent memory"** [03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s).
  - In the docs and the vault, CLAUDE.md is instructions you write and auto memory is notes Claude writes. CLAUDE.md is context, not enforcement.
  - Read his phrase as "persists across sessions", and use hooks for anything that must always happen. See [[Agent Memory Patterns]].
- **[[Claude Code]]: `/loop`.**
  - *Vault:* its table says `/loop` is session-only, expires after 7 days, and Routines handle cloud runs.
  - *This video:* daily automation while he's away [18:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1102s).
  - *Reconciled:* the docs back the vault; see [[Schedule Recurring Claude Tasks]]. They also update Nate Herk's point that in Claude Code you build crons yourself ([25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s)): Routines and Desktop tasks now handle scheduling.
- **[[Claude Code]]: how many skills.** The vault says skills cost little until used, because only their descriptions load. This video still says avoid hundreds, because their style advice conflicts [08:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=498s). Both points hold.
- **[[Matt Pocock]].** Before this batch the vault knew him only for Grill Me. This video adds grill-with-docs and improve-codebase-architecture [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s), [06:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=377s).

**Where other sources in this batch agree or push back**

| Topic | This video | Other source |
|---|---|---|
| Plan mode | Big tasks only [07:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=444s) | [[Nate Herk - 32 Tricks to Level Up Claude Code]]: always start in plan mode ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)) |
| `/init` | "Pretty mid" [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s) | Nate Herk: run it on every existing project ([00:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=14s)) |
| Compaction | Auto-compact mid-task means start over; compact manually with a keep list [15:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=913s), [15:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=926s) | Nate Herk: compact at ~60% with keep instructions, and clear between tasks ([02:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=128s), [02:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=145s), [02:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=159s)) |
| Context rot | Dumb zone [13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s) | [[Ras Mic]], in [[Ras Mic - How AI Agents and Claude Skills Work]] on [[Greg Isenberg]]'s channel: the model gets dumb as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)). [[AI LABS - The Unlazy Skill for Lazy Agents]]: laziness shows up as context fills ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)); see [[Agent Laziness]] |
| Need a CLAUDE.md? | Helpful, not essential [04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s) | Ras Mic: most people don't need one ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). Nate Herk: keep adding gotchas but cap it at 150–200 lines ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)) |
| Others' skills | Installs from skills.sh and learns by reading them [05:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=352s) | Ras Mic: reviews others' skills instead of installing them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)); see [[Build a Skill from a Successful Run]] |
| Turning quirks into rules | Add rules for repeated habits [04:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=254s) | [[Simon Pittman]], in [[Simon Pittman - Set Up Claude Cowork]]: have Claude update its memory or instructions after feedback ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)) |
| Verification | Tests first, plus screenshots [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s), [09:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=578s) | Nate Herk: screenshot and DevTools checks as to-dos ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)). [[AI LABS - Types of Claude Loops Explained]]: anchor `/goal` to tests written first ([02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s)) |
| Loop hype | Mocks the for-loop trend [15:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=947s) | AI LABS: five loop types, one they liken to [[Andrej Karpathy]]'s LLM Council ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)); see [[Loop Engineering]] |
| Subagent cost | Can drain a $20 plan [20:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1216s) | Nate Herk: put subagents on Haiku for simple work ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)) |
| Scheduling | `/loop` as daily automation [18:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1102s) | Nate Herk: `/loop` reruns only in the open session ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s)). [[Jay E]], in [[Jay E - The ARMS Framework for a Claude Agentic OS]]: local routines need the computer on, so many of his run in the cloud ([15:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=956s), [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)). [[Chase AI]], in [[Chase AI - The Agentic OS Setup for Claude Code]]: ask Claude Code to turn a skill into an automation ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s)) |
| Worktrees | One per chat [20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s) | Nate Herk: `claude --worktree` for parallel sessions ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)) |
| Portability | Concepts transfer to other agents [01:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=106s) | [[Nate Herk]] also runs his brain in [[OpenAI Codex]] and [[Hermes Agent]] ([01:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=106s)), per [[Claude Code]] |

## Build from this

Each item gives what the video says, with timestamps, and what the vault adds, checked in Beyond the source.

1. **Definition-of-done kit**
   - *Video:* tests first, critical paths only, type checks and linting, screenshot or browser checks [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s), [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s), [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s), [09:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=578s).
   - *Vault:* put the rules in CLAUDE.md. Enforce them with a Stop hook or a `/goal` that names the commands. Use [[Claude in Chrome]] for UI checks.
   - See [[Build Verification into Every Task]], [[Tests-First Goal Loop]] and [[Evidence-Gated Completion Ledger]].
2. **Plan big, build cheap**
   - *Video:* plan mode for big tasks; Opus plans and Sonnet builds; shadcn's improve writes the plans [07:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=444s), [08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s), [06:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=407s).
   - *Vault:* plan with improve (it writes to `plans/`) or with the `opusplan` alias. Implement each plan on Sonnet in its own worktree, then finish with `/code-review` and `/security-review`.
   - See [[Plan-First Workflow]], [[Route Tasks to the Right Claude Model]], [[Parallel Sessions with Git Worktrees]] and [[Multi-Agent Review and Scoring Loops]].
3. **Context routine for a $20 plan**
   - *Video:* `/context` before big tasks, one task per session, stop tangents, specific prompts, and a fresh start after an auto-compact [13:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=833s), [14:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=844s), [14:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=870s), [14:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=885s), [15:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=913s).
   - *Vault:* show context usage in the status line, add a "Compact instructions" section to CLAUDE.md, and optionally lower the auto-compact window.
   - See [[Context Hygiene Routine]] and [[Context Window Management]].
4. **His repo automations, made durable**
   - *Video:* daily issue-to-PR, security and bug sweep to issues, feature brainstorm, and event triggers [18:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1111s), [18:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1118s), [18:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1129s), [18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s).
   - *Vault:* use cloud Routines (`/schedule`) or Desktop scheduled tasks instead of `/loop`, with GitHub pull-request triggers for events. Keep changes on `claude/` branches and give each routine only the connectors it needs.
   - See [[Schedule Recurring Claude Tasks]], [[Routines and Scheduled Tasks]], [[Configure Safe Autonomy Permissions]] and [[Sync a Workspace to an Always-On Cloud Agent]].
5. **Quirk-driven CLAUDE.md**
   - *Video:* description, status, style, philosophy, no ALL-CAPS, PR language [04:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=267s), [04:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=290s), and an AGENTS.md import [03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s).
   - *Vault:* add a rule only after a repeated mistake, and move procedures into skills.
   - See [[Keep CLAUDE.md Lean]], [[Port a Claude Code Brain to Other Agents]] and [[Tool-Agnostic Context Files]].
6. **Skills-and-MCP audit**
   - *Video:* one skill family, MCPs only for outside systems, and his review stack [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s), [10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s), [06:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=399s), [05:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=329s).
   - *Vault:* list your skills and MCP servers. Flag style skills that conflict and MCPs that only supply knowledge, and disable unused servers with `/mcp`.
   - See [[Build vs Install Third-Party Skills]], [[Agent Skills]], [[Connecting Claude to External Tools]] and [[Grill Me Interview Skill]].
7. **Budget-aware subagents**
   - *Video:* researcher, reviewer and debugger roles, created by asking Claude, plus the cost warning [19:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1185s), [20:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1200s), [20:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1216s).
   - *Vault:* set `model: haiku` or `sonnet` in each agent file, and give reviewers read-only tools.
   - See [[Subagents and Agent Teams]].
8. **Teach-me habit**
   - *Video:* have Claude explain every change [16:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1007s).
   - *Vault:* a CLAUDE.md section asking for a short "what changed and why" after each edit.

**Vault starter content (not shown in the video; fill in the placeholders)**

```markdown
@AGENTS.md

## Project
<One paragraph: what the app does, who uses it, the stack.>

## Status
- Current focus: <milestone>. Known broken or half-done: <list>.

## Coding style
- <naming, file-size limits, patterns to prefer or avoid>

## Working philosophy
- Make the smallest change that solves the task. Ask before adding a dependency.

## Rules from repeated mistakes
- User-facing text uses sentence case. No ALL CAPS in UI copy.
- Write pull request titles and descriptions in <language>.
- Write a failing test before the implementation. Test critical behaviour only.
- Before calling a task done, run `<typecheck command>` and `<lint command>` and show the result.

# Compact instructions
When compacting, keep: the task goal, files changed and why, decisions made, checks still failing, the next step.
```

```text
/compact Keep the task goal, each file changed and why, decisions we made, checks still failing, and the next step. Drop the exploration of files we ruled out.
```

Routine prompts (one routine each):

```text
Daily issue worker: Pick one open GitHub issue labelled `ready` with no linked PR. If it is unclear, comment with questions and stop. Otherwise write failing tests, implement until tests, type check and lint pass, and open a PR from a claude/ branch that links the issue and lists the checks you ran.

Weekly security and bug sweep: Review code merged since the last run for vulnerabilities and likely bugs. Open one GitHub issue per real finding with file and line, impact, and a suggested fix. Change no code. If nothing turns up, say so in one line.

Weekly feature brainstorm: Read the README, open issues and the last 20 merged PRs. Propose up to five features that fit the project, each with the user problem, rough scope and affected files, as a single GitHub issue titled "Feature ideas <date>".
```

## Resources mentioned

- **Skills:**
  - skills.sh [05:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=357s)
  - [[Matt Pocock]]'s grill-with-docs [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s) and improve-codebase-architecture [06:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=377s)
  - Cursor's thermo-nuclear code quality review [06:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=384s)
  - shadcn's improve [06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s)
  - Claude Code's built-in code review and security review [05:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=329s)
- **Claude FM** via `/radio` [12:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=743s).
- **Community context tools** from the description, mentioned at [15:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=933s): ponytail (github.com/DietrichGebert/ponytail), rtk (github.com/rtk-ai/rtk) and caveman (caveman.so).
- **Alternatives:**
  - [[OpenAI Codex]] [21:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1268s)
  - OpenCode [21:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1280s)
  - Pi [21:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1288s)
  - Cursor [21:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1298s)
  - VS Code with GitHub Copilot [21:48](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1308s)
  - T3 Code [21:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1317s)

## Beyond the source

*Not said in the video. Checked on 2026-09-15 at the links given.*

- **Ultraplan** has been removed. The docs point to plan mode, or to Claude Code on the web for cloud sessions. https://code.claude.com/docs/en/ultraplan
- **Plan mode.**
  - Claude reads and explores but edits nothing until you approve.
  - Enter it with Shift+Tab, `/plan` or `--permission-mode plan`.
  - When you approve, you can switch to auto mode (or auto-accept edits), approve with manual edit review, or keep planning. Ctrl+G opens the plan for editing.
  - https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode
- **`opusplan`** is a built-in alias that uses Opus in plan mode and Sonnet for execution. The `default` alias is Sonnet 5 on Pro and Team Standard, and Opus 5 on Max, Team Premium, Enterprise and the API. https://code.claude.com/docs/en/model-config
- **Fable by plan.**
  - Pro plans and standard Team or Enterprise seats need usage credits for Fable 5 and 5.1.
  - Max plans and premium seats can spend up to 50% of their weekly limits on Fable.
  - The promotion that included Fable 5 ended on 19 July 2026.
  - https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- **Context windows.**
  - On the Anthropic API, Fable 5.1, Fable 5, Sonnet 5, and Opus 4.7 and later default to 1M tokens. Older models such as Opus 4.6 and Sonnet 4.6 default to 200K.
  - On Pro, Opus with the 1M window needs usage credits.
  - Sessions with a native 1M window auto-compact at about 967K. `/autocompact` sets the threshold anywhere from 100K to 1M. Lowering it to avoid his "dumb zone" is the vault's suggestion.
  - https://code.claude.com/docs/en/model-config
- **The docs' token advice matches his:**
  - `/clear` between unrelated tasks. It costs nothing, while compacting a large context is itself a large request.
  - `/compact <focus>`, or a "Compact instructions" section in CLAUDE.md.
  - Specific prompts, since vague requests make Claude scan broadly.
  - Plan mode for complex work, and giving Claude a way to verify.
  - Subagents for verbose output, CLI tools instead of MCPs where possible, and workflow instructions in skills.
  - After compaction, the project-root CLAUDE.md is re-injected, and Claude re-reads up to five of the most recently modified files it had read or edited.
  - https://code.claude.com/docs/en/costs#reduce-token-usage, https://code.claude.com/docs/en/context-window
- **Small commands:**
  - `/btw` has no tools and stays out of history. Press `f` to fork the question into a subagent that does have tools.
  - `!` runs a command and adds its output to the session.
  - `/voice` needs a Claude.ai login and streams audio to Anthropic. Transcription doesn't use tokens.
  - `/teleport` pulls a web session into your terminal. `/remote-control` makes a local session available on claude.ai or mobile.
  - `/radio` opens Claude FM.
  - https://code.claude.com/docs/en/interactive-mode, https://code.claude.com/docs/en/voice-dictation, https://code.claude.com/docs/en/remote-control, https://code.claude.com/docs/en/commands
- **Interview-style `/init`.** Set `CLAUDE_CODE_NEW_INIT=1`. It asks which artifacts to create (CLAUDE.md, skills, hooks), explores with a subagent, asks follow-up questions, and shows a proposal before writing anything. https://code.claude.com/docs/en/memory#set-up-a-project-claude-md
- **AGENTS.md.**
  - Claude Code reads CLAUDE.md, not AGENTS.md. The docs recommend putting `@AGENTS.md` at the top of CLAUDE.md, or using a symlink.
  - The new `/init` flow reads AGENTS.md, and `/import` copies another agent's setup.
  - https://code.claude.com/docs/en/memory#agents-md
- **When to add CLAUDE.md rules.**
  - Add one when Claude repeats a mistake, and keep each file under about 200 lines.
  - Use hooks for actions that must always happen, because CLAUDE.md is context, not enforcement.
  - Auto memory is written by Claude and kept separately.
  - https://code.claude.com/docs/en/memory#when-to-add-to-claude-md
- **Built-in reviews.** `/code-review` is a bundled skill (`--fix` applies its findings). `/security-review` reviews your branch's diff against the default branch. https://code.claude.com/docs/en/commands
- **The skills he names:**
  - **Matt Pocock's skills** install with `claude plugins install mattpocock-skills` or `npx skills@latest add mattpocock/skills`. grill-with-docs interviews you and writes a `CONTEXT.md` glossary and architecture decision records (ADRs). improve-codebase-architecture produces an HTML report of design improvements. https://github.com/mattpocock/skills
  - **Cursor's thermo-nuclear-code-quality-review** is a strict maintainability review that favours simplifications which keep behaviour the same, and flags files over 1,000 lines. https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md
  - **shadcn/improve** writes only to `plans/`: one plan per finding plus a priority index. Install with `npx skills add shadcn/improve`. https://github.com/shadcn/improve
  - **skills.sh** is a cross-agent skills directory. Install with `npx skills add <owner/repo>`. https://www.skills.sh/
- **Browser testing.** Claude in Chrome needs the extension and a direct Anthropic plan; start it with `claude --chrome` or `/chrome`. Claude can click through pages, read console errors and take screenshots. https://code.claude.com/docs/en/chrome
- **Subagents.**
  - Ask Claude to create one, or add a file in `.claude/agents/`. Each gets its own context and returns a summary.
  - A `model` field (for example `haiku`) cuts cost.
  - Agent teams use roughly 7x the tokens of a normal session when teammates run in plan mode.
  - https://code.claude.com/docs/en/sub-agents, https://code.claude.com/docs/en/costs#manage-agent-team-costs
- **Scheduling.**
  - `/loop` is session-scoped: its tasks fire only while that session is running (a backgrounded session counts) and are cleared by a new conversation. Recurring tasks expire after 7 days.
  - Routines (research preview, Pro and above) run in Anthropic's cloud on a schedule (hourly at most), on API calls, or on GitHub pull request and release events.
  - Routines push to `claude/` branches, skip approval prompts and have a daily cap. Create them with `/schedule`.
  - https://code.claude.com/docs/en/scheduled-tasks, https://code.claude.com/docs/en/routines
- **`/goal`.** After each turn, a small model (Haiku by default) judges the condition from the conversation alone, without tools. Give it a measurable check and a turn limit, and use auto mode for unattended runs. https://code.claude.com/docs/en/goal
- **Worktrees.** `claude --worktree <name>` creates `.claude/worktrees/<name>/` on branch `worktree-<name>`. A `.worktreeinclude` file copies files such as `.env` into it, and `isolation: worktree` gives a subagent its own worktree. https://code.claude.com/docs/en/worktrees
- **Token tools:**
  - JetBrains ran caveman on 86 SkillsBench tasks in headless Claude Code and found about 8.5% output-token savings, against a claimed 65%. https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/
  - rtk compresses shell output through a Claude Code hook (`rtk init -g`), and notes that smaller output isn't the same as a smaller bill. https://github.com/rtk-ai/rtk
  - ponytail pushes agents to reuse existing code, the standard library or native features before writing new code; its savings figures come from the authors' own benchmarks. https://github.com/DietrichGebert/ponytail
- **Alternatives:**
  - OpenCode is MIT-licensed and connects to 75+ model providers, including local models. https://opencode.ai/, https://github.com/anomalyco/opencode/blob/dev/LICENSE
  - Pi is a minimal, extensible coding-agent harness created by Mario Zechner and now maintained by Earendil Works. https://pi.dev/, https://en.wikipedia.org/wiki/Pi_(AI_agent)
  - T3 Code is an MIT-licensed control surface for Claude Code, Codex, Cursor, OpenCode and others. https://github.com/pingdotgg/t3code
- **Background claims:**
  - Claude Code reached a $1B annual revenue run-rate about six months after general availability. https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
  - Uber used up its annual AI budget in four months, then capped spending at $1,500 per employee per agentic coding tool, Claude Code included. https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/
  - "Tibo" is most likely OpenAI's Thibault Sottiaux, who has announced several resets of Codex usage limits for paid plans on X. https://x.com/thsottiaux/status/2055707616605835333

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Claude.md", "claw.md", "cloud file" | CLAUDE.md |
| "agents.md", "skill.md" | AGENTS.md, SKILL.md |
| "Cloud Code" | Claude Code |
| "tonex engineer" (01:31) | "10x engineer" |
| "no wonder people are getting better results" (00:25) | probably "aren't getting"; *unclear in captions* |
| "ultra plan mode" (02:10) | Ultraplan, since removed |
| "grow with doc skill" (06:13) | Matt Pocock's grill-with-docs; likely |
| "improved code base architecture skill" | improve-codebase-architecture |
| "cursors … Thermonuclear code quality review skill" | Cursor's thermo-nuclear-code-quality-review |
| "a Shatien's improved skill" (06:42) | shadcn's improve; likely |
| "Oh yeah, play / easiest here" (06:51) | "Plan mode, S tier"; likely |
| "{slash} BTW", "{exclamation point}" | `/btw`, the `!` prefix |
| "{slash} teleport and remote control" | `/teleport` and `/remote-control` |
| "live-changing command" (18:00) | probably "life-changing"; the command is `/loop` |
| "It's here. It's straight." (19:05) | intro to `/goal`, with the name inaudible; *unclear in captions* |
| "one is at like 300,000 tokens" (13:23) | as spoken; the docs list 200K and 1M windows |
| "I think Claude code to a million tokens" (13:25) | probably "Claude Code goes up to a million tokens" |
| "work trees", "CodeX", "open code" | git worktrees, Codex, OpenCode |
| "Tibo" (21:14) | OpenAI's Thibault "Tibo" Sottiaux, who announces Codex limit resets; likely (see Beyond the source) |
| "pie" (21:28) | Pi, the minimal coding-agent harness; likely |
| "Grok and Composer" (21:43) | Cursor's Composer models and Grok models available in Cursor; likely |
| "the Chad" (19:36) | joking name for the main agent, possibly "the chat"; *unclear in captions* |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Verification Before Done]] · [[Plan Before Executing]] · [[Context Window Management]] · [[Agent Laziness]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Connecting Claude to External Tools]] · [[Subagents and Agent Teams]] · [[Choosing a Claude Model]] · [[Loop Engineering]] · [[Routines and Scheduled Tasks]] · [[Permissions and Approval Gates]] · [[CLAUDE.md as a Router]] · [[Claude Code Auto Memory]] · [[Agent Memory Patterns]] · [[Tool-Agnostic Context Files]] · [[Escaping the Default AI Design Look]]
- **Techniques:** [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Plan-First Workflow]] · [[Route Tasks to the Right Claude Model]] · [[Context Hygiene Routine]] · [[Parallel Sessions with Git Worktrees]] · [[Multi-Agent Review and Scoring Loops]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Configure Safe Autonomy Permissions]] · [[Keep CLAUDE.md Lean]] · [[Build a Level 1 Second Brain]] · [[Port a Claude Code Brain to Other Agents]] · [[Grill Me Interview Skill]] · [[Build a Skill from a Successful Run]] · [[Evidence-Gated Completion Ledger]] · [[Build a Distinctive Site with Design Skills]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]] · [[Claude in Chrome]] · [[Hermes Agent]]
- **Sources in this batch:** [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[Simon Pittman - Set Up Claude Cowork]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Knowing More - Every Claude Model Explained]] · [[Anthropic - What Is Claude Managed Agents]] · [[AI LABS - Claude Design Skills for Beautiful Sites]]
- **Earlier sources:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **People:** [[The Coding Sloth]] · [[Matt Pocock]] · [[Nate Herk]] · [[Ras Mic]] · [[Greg Isenberg]] · [[Simon Pittman]] · [[Jay E]] · [[Chase AI]] · [[AI LABS]] · [[Andrej Karpathy]]
