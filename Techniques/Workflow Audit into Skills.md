---
type: technique
goal: "Find the work you keep repeating with Claude, using your session history and a Claude-led interview, and turn it into a prioritised backlog of skills, automation candidates and loop candidates grouped by domain"
difficulty: beginner
time_to_build: "About 1 to 2 hours for the first audit (session mining, interview, triage), then 30 to 90 minutes per skill you build from it (vault estimate)"
sources: ["[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]"]
tools: ["[[Claude Code]]", "[[Claude Cowork]]", "[[OpenAI Codex]]"]
tags: [topic/skills, topic/claude-code, topic/automation, topic/scheduling, topic/loops, topic/agentic-os, topic/prompting, topic/teams]
---

# Workflow Audit into Skills

> **Provenance.** The method is mainly from [[Chase AI - The Agentic OS Setup for Claude Code]], where the workflow audit is the first sub-phase of his "Level 1" ([04:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=275s)). Ideas from [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[Nate Herk - 32 Tricks to Level Up Claude Code]], [[Ras Mic - How AI Agents and Claude Skills Work]], [[Simon Pittman - Set Up Claude Cowork]], [[Chase AI - The Three-Step Claude Code Agentic OS]] and [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] are credited by name where they appear. Chase only paraphrases his prompts on screen and shows no files. **The prompts, backlog template, scoring rubric and folder layout below are original vault starter content.** Facts about Claude Code, Desktop routines and skills that no video states are listed under **Beyond the source**, with links.

## Goal

End with one file, `ops/skills-backlog.md`. It lists every recurring task you do with Claude, grouped by domain. Each row records the expected output, the evidence that the task really repeats, a proposed skill name, whether it has been validated by a successful run, and whether it should later become a scheduled automation or a self-improving loop.

Why bother:
- Chase calls skills arguably the most powerful part of Claude Code, because they pin down exactly how Claude should produce a particular output ([04:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=291s)). Yet most people can't say which outputs they produce over and over, and fewer have turned them into skills ([05:06](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=306s)).
- The default is a manual back-and-forth in which you keep typing the same instructions ([05:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=331s)). He calls codifying that work the easiest way to improve Claude Code ([06:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=407s)), and says it helps even if you do nothing else ([05:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=317s)).
- The audit is the foundation for what comes next. Skills lead to automations, and automations lead to loops ([13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s)). None of it needs a dashboard ([12:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=778s)).

## Use when

- **You've used Claude Code, Cowork or Codex for a few weeks** and recognise the same requests coming back. Chase says Levels 1 and 2 of his model work in a plain Claude Code terminal, the Codex CLI or the Codex desktop app ([03:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=224s)).
- **You've typed the same task twice.** Jay E's rule of thumb: once you prompt Claude for the same task a second time, it's probably worth making a skill ([05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s)).
- **You're planning an [[Agentic OS]], dashboard or routines.** Chase puts about 90% of an AI OS's value in skills, loops, memory and state rather than the interface ([02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s), [30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)). Jay E teaches his ARMS framework bottom-up: skills first, then memory, and only then routines and applications ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)).
- **A team keeps re-explaining the same procedures.** Nate Herk frames shared skills committed to GitHub as a way to automate your actual SOPs ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)).

**Don't use it for:**
- One-off or judgement-heavy work that never repeats in the same shape.
- Jumping straight from "found a workflow" to "wrote a skill". The audit only nominates candidates. Chase warns that a process you haven't run by hand may not be validated ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)), and Ras Mic calls writing the skill before a successful run the worst thing you can do ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). Build each skill with [[Build a Skill from a Successful Run]].

## What the sources say

### Chase: the four sub-phases of Level 1

| Point | Detail | Timestamp |
|---|---|---|
| Order | Workflow audit, then skill creation, then automation, then loop engineering | [04:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=275s) |
| Audit first | Before creating skills you need to know what you actually need skills for | [04:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=281s) |
| Scale | Do what you already do with skills, but many times more: codify all your daily and weekly work | [05:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=343s)–[06:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=364s) |
| Domains | Split your Claude use into domains. His are research, content, community, agency and sales | [06:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=370s) |
| Tasks per domain | Under content: project outlines, video hooks, repurposing, carousels. He asks why each isn't already a skill | [06:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=380s)–[06:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=395s) |
| Route 1, manual | Explain a task you know you do and have the skill-creator skill turn it into a skill | [06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s)–[07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s) |
| Caveat on route 1 | You may not have validated how Claude should do it. Ideally do the task by hand first, confirm it works, then ask Claude to turn what you just did into a skill | [07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)–[07:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=451s) |
| Route 2, session mining | Claude Code can see your previous sessions: tool calls, instructions and the full back-and-forth | [07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s) |
| How many sessions | Ask it to look at the last 3, 5, 10 or 20 sessions and list things you do all the time | [07:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=476s) |
| Why | It works from real data rather than guesses about what you do | [08:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=495s) |
| His prompt (paraphrased) | Go through our last 10 sessions, pull out repeated tasks that aren't skills yet, and chart the task, what the output should be, and a proposed skill | [08:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=504s) |
| Keep it plain | It doesn't need to be fancy. Claude starts by locating the session files | [08:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=527s)–[08:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=532s) |
| Route 3, interview | Give Claude a stream of consciousness about your day and week, have it ask about blind spots, then pull out tasks that could be skills | [08:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=536s)–[09:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=557s) |
| His interview prompt (paraphrased) | You want daily and weekly tasks turned into skills where sensible. Start with a stream of consciousness, have Claude turn it into an interview, flag blind spots, gather maximum context on the work and desired outcomes, then extract tasks for skills and later automations | [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s)–[09:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=598s) |
| Mindset | Turn your work into a checklist, as if onboarding a personal assistant with step-by-step instructions | [10:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=616s)–[10:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=629s) |
| Skills are editable | A skill is a tangible workflow you can inspect and edit until the outputs are dialled in | [10:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=640s) |
| Demo result | Session mining surfaced tasks such as checking for tool and repo updates for his videos | [10:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=646s)–[10:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=651s) |
| Automation pass | If a skill keeps getting repeated, make it an automation where that makes sense | [11:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=665s)–[11:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=681s) |
| Two ways to automate | Ask Claude Code whether the skill can become an automation, or in the Claude desktop app open Routines, name one, set the instructions to run the named skill, and pick a schedule | [11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s)–[11:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=704s) |
| Loop pass | Consider adding a self-improvement loop to an automation, tied to memory and state. He leaves the details to another video | [11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s)–[12:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=733s) |
| Logging for loops | Skill and automation outputs need to be logged where the loop can see past runs, all in the same place | [22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1377s) |
| Recap | Audit (manually, from sessions, or by interview), create skills, ask which can be automated, then ask whether a loop fits | [13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s)–[13:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=805s) |

### Chase's earlier version: one spoken interview that builds as it goes

In [[Chase AI - The Three-Step Claude Code Agentic OS]] (May 2026), the audit and the build happen in one conversation. The prompt itself isn't given in the video.

| Point | Detail | Timestamp |
|---|---|---|
| Map | Break everything you do, personal and especially business, into domains. His: memory, productivity, research, content, community | [01:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=111s), [01:59](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=119s) |
| Tasks | Each domain holds discrete tasks. Anything you do regularly belongs on the map as a skill candidate, even a simple YouTube search, which then returns a complete report every time | [02:15](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=135s), [02:31](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=151s), [02:39](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=159s) |
| Speak it | Open the terminal, turn on your microphone, and give a stream of consciousness about your day and your discrete tasks | [05:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=312s) |
| Per task | Claude asks whether the task can become a skill, then whether that skill should become an automation | [05:30](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=330s)–[05:33](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=333s) |
| Build | It creates each skill with skill-creator so the task runs the same way every time, then decides whether an automation is needed and whether it runs locally or remotely | [05:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=351s), [05:56](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=356s) |
| Selective | A morning trend scan should be automated; deep research shouldn't | [05:40](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=340s) |
| Why | Codified behaviour can be tracked and optimised, and a teammate who would never use Claude Code can use the system | [06:23](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=383s), [06:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=411s) |

### Jay E, Nate Herk, Ras Mic and Simon Pittman

| Source | Point | Timestamp |
|---|---|---|
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | Skills are shortcuts to your standard operating procedures | [05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s) |
| Jay E | **Trigger:** prompting Claude for the same task twice means it's probably time for a skill | [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s) |
| Jay E | Start from Anthropic's pre-built skills (Claude desktop app, Customize, Skills). skill-creator is one of the most popular | [05:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=339s)–[05:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=354s) |
| Jay E | Make your own skills, because everyone's work is custom and the habit gets you refined results faster. Inspiration is everywhere | [06:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=360s)–[06:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=371s) |
| Jay E | He pasted an X post with a tip for speeding up his machine, invoked skill-creator, and Claude Code built a cleanup skill he could test | [06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s)–[06:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=386s) |
| Jay E | Routines come only after skills and memory, because that's when you trust the agent to work unwatched | [14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s) |
| Jay E | A routine that uses a custom skill gives him a draft he is 70–80% confident is in his voice | [15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s) |
| [[Nate Herk - 32 Tricks to Level Up Claude Code]] | Hack 12: build custom skills as reusable prompt files in `.claude/skills`, e.g. a tech-debt scanner and a code reviewer | [05:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=328s)–[05:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=339s) |
| Nate | Invoke them in natural language or with the slash command, and the workflow runs the same way every time | [05:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=344s) |
| Nate | Commit them to GitHub so the whole team can use them, which automates your SOPs | [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s) |
| Nate | After making new skills, update CLAUDE.md | [06:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=396s) |
| Nate | When pushback gets a better output, tell Claude to update the skill or CLAUDE.md so the mistake isn't repeated | [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s) |
| [[Ras Mic - How AI Agents and Claude Skills Work]] | Spotting a workflow and going straight to writing the skill is the anti-pattern. Walk the agent through it first | [08:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=509s)–[09:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=563s) |
| Ras Mic | Don't set up many subagents and skills before you have working workflows. Scale for productivity, not for looks | [14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)–[14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s) |
| [[Simon Pittman - Set Up Claude Cowork]] | In Cowork: Customize, Skills, then the plus button lets you create a skill with Claude, write instructions, or upload one. Turn on skill-creator | [32:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1956s)–[32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s) |
| Simon | Skills that break a large task into steps let you start it and walk away | [34:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2041s) |

### Where sources differ

- **Write the skill now, or after a proven run?** Chase offers a manual route in which you describe a task to skill-creator ([06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s)), and Jay E builds a skill straight from a pasted post, then tests it ([06:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=380s)). Chase himself prefers doing the task by hand first ([07:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=448s)), and Ras Mic says a skill written without a successful run lacks the context it needs ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)). **This technique follows the stricter view:** the backlog has a *Validated run?* column, and nothing moves to "built" until a real run succeeds.
- **What counts as recurring?** Jay E's threshold is twice ([05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s)). Chase talks about tasks you do all the time, daily and weekly ([07:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=476s), [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s)). *(Vault approach:)* use "twice" to *nominate* a candidate and frequency to *prioritise* it.
- **Build skills during the interview?** In the May video Claude creates each skill with skill-creator as the interview reaches it ([05:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=351s)). By June Chase wants the task done by hand and confirmed first ([07:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=448s)). This technique keeps the June gate, so the interview only fills the backlog.
- **Who decides local or remote?** Chase says you needn't know, because Claude Code can work it out ([04:05](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=245s)). Prompt D asks Claude for that proposal, and you approve it.
- **When to automate.** Chase says turning a skill into an automation is very easy ([11:23](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=683s)). Jay E says to schedule only once you're confident in your skills and memory ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)). The two fit together: setup is easy, but automate only validated skills.
- **Mention new skills in CLAUDE.md?** Nate says to update CLAUDE.md after making new skills ([06:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=396s)). Ras Mic argues CLAUDE.md is always in context and procedures belong in skills ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)–[04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)). *(Vault inference:)* skill names and descriptions already reach Claude on their own (see Beyond the source), so only add a CLAUDE.md line when you need a rule about *when* to prefer a skill. Don't copy the skill in. See [[Keep CLAUDE.md Lean]].

## Prerequisites

- [[Claude Code]] (or Codex) with **recent session history** in the project folders you want to audit. Transcripts are deleted after 30 days by default (Beyond the source), so a first audit only sees the last month. If you're new, skip session mining and use the interview route.
- Optional: the **skill-creator** skill, named by Chase ([07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s)), Jay E ([05:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=354s)) and Simon ([32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)). Install paths are under Beyond the source.
- A home for the audit: a project or vault folder with an `ops/` directory (layout below).
- 30–45 uninterrupted minutes for the interview.
- **A privacy decision.** Transcripts are plaintext and can hold pasted secrets and client data (Beyond the source). The mining prompt below tells Claude not to copy them into the report.

## Steps

1. **Map your domains.** List 3 to 7 areas where you use Claude, each with a few example tasks, the way Chase splits his into research, content, community, agency and sales ([06:10](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=370s)–[06:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=386s)). Save the list at the top of `ops/skills-backlog.md` (template below).
2. **Mine your session history.** Open Claude Code in each project you use heavily and run **Prompt A**. It reads recent transcripts and charts repeated tasks, their expected outputs and proposed skills, as in Chase's route 2 ([07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s)–[08:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=532s)). Transcripts are stored per project folder, so repeat this in each one. Check the date range it reports.
3. **Run the discovery interview.** Start a fresh session, paste **Prompt B**, then give a stream of consciousness about your day and week and let Claude turn it into an interview that calls out blind spots, as Chase describes ([08:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=536s)–[09:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=598s)). Prompt B adds monthly work and one question at a time *(vault additions)*. This catches work that never appeared in a Claude session: things you do in other tools, monthly chores, and hand-offs.
   - *Speak it.* Chase suggests dictating this brain dump rather than typing it ([05:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=312s)). In the Claude Code CLI, run `/voice` and hold Space while you talk (Beyond the source).
4. **Add your "typed it twice" list.** Jot down anything you remember prompting for more than once, including in the Claude apps and Cowork ([05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s)).
5. **Merge and score.** Run **Prompt C** to combine the two audit files and your list into the backlog table, remove duplicates, score each row with the rubric, and recommend the top three. Review the diff yourself.
6. **Park what isn't a skill.** Move one-offs, pure judgement calls and "I just need live data" items to the *Parked* list with a reason. Live data is better handled by a connector than a skill (see [[Connecting Claude to External Tools]]).
7. **Validate and build the top three, one at a time.** For each, do the task by hand with Claude until it succeeds, then have Claude turn that run into a skill, following Chase's ideal route ([07:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=448s)–[07:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=451s)) and Ras Mic's method. Full playbook: [[Build a Skill from a Successful Run]]. Set *Validated run?* to the run's date and *Status* to `built`.
8. **Use and edit until the outputs are dialled in** ([10:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=640s)). When a run disappoints, push back, then have Claude write the fix into the skill ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)). See [[Skill Improvement Loop]].
9. **Share team SOPs.** Commit project skills under `.claude/skills/` so teammates get them ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)).
10. **Automation pass.** For each `built` skill, run **Prompt D**. Where a schedule makes sense, either ask Claude Code to set one up or create a Desktop routine whose instructions run that skill, following Chase's two options ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s)–[11:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=704s)). Click **Run now** once and approve the permissions it needs, so later runs don't stall (Beyond the source). Playbook: [[Schedule Recurring Claude Tasks]]. Set *Status* to `automated`.
11. **Loop pass.** Where output quality varies from run to run, log every run and your feedback in one place a later review can read ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1377s)). The layout below uses `runs/<skill>/`. Design the review with [[Loop Engineering]] and [[Skill Improvement Loop]]. Set *Status* to `looped`.
12. **Repeat the audit every month** *(vault suggestion)*. Retention defaults to 30 days, so a monthly run sees everything since the last one. Rows that show up again in a later audit but are still only `idea` are your next builds.

## Starter files & prompts

*Everything in this section is original vault starter content. Chase's own prompts appear only in paraphrase in the table above.*

### Folder layout

```text
your-project-or-vault/
├── CLAUDE.md
├── ops/
│   ├── skills-backlog.md            # the backlog (template below)
│   └── audits/
│       ├── 2026-09-15-session-mining.md
│       └── 2026-09-15-interview.md
├── .claude/
│   └── skills/
│       └── <skill-name>/SKILL.md    # built skills (commit to share)
└── runs/
    └── <skill-name>/                # one dated log per run, for loop candidates
        └── 2026-09-16.md
```

### Prompt A: session mining

```text
Audit how I've been using you in this project so we can turn repeated work into skills.

1. Find this project's session transcripts (Claude Code stores them as .jsonl files in this
   project's folder under ~/.claude/projects/). Read the most recent 15 main sessions, or all
   of them if there are fewer. Ignore subagent transcripts. Tell me the date range you covered.
2. List the skills that already exist, in .claude/skills/ here and in ~/.claude/skills/.
3. Find tasks I asked for more than once: the same kind of request, the same output format,
   or the same multi-step procedure I had to explain again. Count each occurrence.
4. Leave out one-off tasks and anything an existing skill already covers.
5. Write the results to ops/audits/<today>-session-mining.md as a table with these columns:
   Task | Times seen (session dates) | What I asked for | Expected output |
   Steps I had to explain | Proposed skill name | Could it run on a schedule? | Notes
6. Under the table, list every correction I gave you more than once. The skills will need
   those as rules.

Don't create or edit any skill yet. Don't copy secrets, API keys, passwords or personal
details from the transcripts into the report. Describe them generically instead.
```

### Prompt B: discovery interview

```text
I want to turn my recurring daily, weekly and monthly work into skills, and later into
scheduled automations where that makes sense. Interview me to find all of it.

How to run this:
- First I'll give you an unstructured brain dump of what I do. Let me finish.
- Then propose a list of domains from what I said and confirm it with me.
- Interview me ONE question per message, one domain at a time.
- For every task, get: what triggers it, how often, what the finished output looks like,
  who it's for, the steps I take, the tools and files involved, and how I know it's good.
- Call out blind spots: work I do outside Claude, monthly or quarterly chores, things I
  review or check for other people, hand-offs, and tasks I mentioned but skipped over.
- If an answer is vague ("I do some reporting"), follow up until you have a concrete output.
- Stop when every domain is covered and two questions in a row turn up nothing new, or
  when I say "wrap up".

Then write ops/audits/<today>-interview.md as domain > task. For each task give its trigger,
frequency, expected output and steps, and label it skill candidate, automation candidate or
neither, with a one-line reason. Don't create any skills yet.
```

**Blind-spot prompts the interviewer should cover** (paste under Prompt B if you like):
- What did you produce last Monday, and last month-end?
- What do you send other people on a schedule?
- What do you check before publishing, sending or shipping?
- What do you copy from one tool into another?
- What did you explain to Claude, a teammate or a contractor more than once?
- What do you put off because it's tedious?

### Prompt C: merge and triage

```text
Read ops/audits/<date>-session-mining.md, ops/audits/<date>-interview.md and my
"typed it twice" list below. Update ops/skills-backlog.md using the table and rubric
already in that file.

- Merge duplicates into one row and cite all the evidence.
- Fill every column. Set "Validated run?" to "no" unless a transcript shows a run of that
  exact task that I accepted as correct, and if so give its date.
- Score each row with the rubric. Put anything that scores 1 on Clarity in the Parked list
  with "needs interview" as the reason.
- Recommend the top 3 to build first, with two sentences on why for each.
Show me the diff before saving.

My typed-it-twice list:
- ...
```

### Prompt D: automation and loop fit

```text
For each row in ops/skills-backlog.md with status "built":
1. Is it triggered by a time, by an event, or only by me? Does it send, delete, publish,
   pay for or change anything outside this folder?
2. If a schedule fits: should it be a local Desktop routine (needs my files, and my
   computer must be awake) or a cloud routine (no local files)? Propose the schedule, the
   instructions (which should just run the skill), the permissions it will need, and a guard
   for late catch-up runs, e.g. skip the task if it's running after a cutoff time.
3. Does output quality vary from run to run? If so, propose a run log in runs/<skill>/
   (inputs, output path, what I changed, pass/fail) and a weekly review that proposes
   SKILL.md edits for my approval.
Fill the "Automation fit" and "Loop fit" columns. Don't create any routine yet.
```

### `ops/skills-backlog.md` template

```markdown
---
type: skills-backlog
updated: YYYY-MM-DD
---

# Skills backlog

Domains: Research · Content · Clients · Sales · Ops   <- replace with yours
Status flow: idea → validated → built → automated → looped   (or parked)

| ID | Domain | Task | Trigger and frequency | Expected output | Evidence | Proposed skill | Validated run? | Automation fit | Loop fit | Score | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | Content | Check tools and repos in upcoming videos for updates | Before each script, ~2 per week | Change summary per tool, with links | Sessions 09-02, 09-05, 09-09 | `tool-update-check` | no | Good: weekday morning routine | Low | 15 | idea |
| S02 | Clients | Turn a sales-call transcript into a proposal outline | After each call, ~3 per week | `proposal-outline.md` in the client folder | Interview + 2 sessions | `call-to-proposal` | yes (2026-09-10) | No: I trigger it | Medium: log my edits | 16 | built |
| S03 | Ops | Monday metrics roll-up | Weekly, Monday 09:00 | One page, 5 numbers, week-on-week change | Interview | `weekly-metrics` | no | Good: weekly routine | Medium | 14 | idea |

## Scoring rubric
Add the four scores (max 20):
- Frequency: 1 monthly or less · 3 weekly · 5 daily
- Time per run: 1 under 5 min · 3 15–30 min · 5 over an hour
- Consistency need: 1 output can vary · 3 has a set format · 5 must match every time
- Clarity: 1 can't describe "done" · 3 mostly clear · 5 clear pass/fail
Build the highest scores first. Clarity 1 goes back to the interview.

## Parked
- <task>: <reason: one-off / judgement call / needs live data, so a connector / needs interview>
```

*S01 is modelled on the repeated task Chase's session mining found ([10:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=651s)). S02 and S03 are made-up examples.*

## Done when

- [ ] `ops/audits/` has a session-mining report that states the date range covered, and an interview report.
- [ ] `ops/skills-backlog.md` has every candidate grouped by domain, with evidence, expected output, proposed skill name, score and status, plus a Parked list with reasons.
- [ ] The top three candidates are chosen, and at least one is `built` from a real successful run (date recorded).
- [ ] That skill triggers in a fresh session, from a natural request as well as its slash command.
- [ ] Every `built` skill has an Automation fit and Loop fit decision, and any routine created has been run once with its permissions approved.
- [ ] Shared skills are committed under `.claude/skills/`, if you work in a team.
- [ ] A reminder is set to rerun the audit next month.

## Pitfalls

- **Codifying a process nobody has validated.** A skill written from a description alone can encode the wrong steps ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)). Ras Mic's agent failed at API calls and fetched the wrong data until he walked it through ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)–[11:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=692s)).
- **Auditing from memory only.** Your guesses miss things. Chase mines sessions precisely so the list rests on real data ([08:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=495s)). Do both routes.
- **Expecting a year of history.** Transcripts older than the retention window are gone, and each project folder has its own. Mine every project you use, and do it monthly.
- **Building the whole backlog at once.** Many skills before any working workflow is the "looks cool" trap Ras Mic warns about ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)). Build three, use them, then continue.
- **Automating too early.** Jay E schedules only once skills and memory are trusted ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)). Unattended runs can also stall on permission prompts or fire late after sleep (Beyond the source).
- **Turning pasted web tips straight into skills.** Jay E made a skill from an X post ([06:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=380s)). *(Vault caution:)* read any commands the skill will run before using it, especially system clean-up or delete steps.
- **Leaking secrets into the audit.** Transcripts record whatever passed through tools. Keep the "don't copy secrets" line in Prompt A, and keep `ops/audits/` out of shared repos if it holds client details.
- **Bloating CLAUDE.md with skill copies.** List a skill in CLAUDE.md only when a routing rule is needed, and put the procedure itself in the skill ([04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)).
- **Chasing the dashboard first.** Chase calls buttons and visuals the cherry on top ([30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)).

## Variations

- **Interview-only** (new users or no history): skip step 2 and run Prompt B. It's Chase's route 3 ([08:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=536s)).
- **One-pass interview (Chase's May version).** Add to the end of Prompt B *(vault starter wording)*: "For each task, also ask me whether it should be a skill, whether that skill should run on a schedule, and whether it needs files on my computer. Record the answers next to the task. Don't build anything." It keeps his per-task questions ([05:33](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=333s)) without skipping the validated-run gate.
- **A daily review that suggests skills (Jack Roberts).** Jack's Claude Code OS reviews his chats locally every day and tells him which new skills he could use ([14:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=889s)). *(Vault approach:)* schedule Prompt A as a local routine, since transcripts live on your disk, and have it append suggestions to `ops/audits/` rather than create skills. See [[Schedule Recurring Claude Tasks]].
- **Package the interview as a skill.** Once Prompt B has worked for you, turn it into a reusable interview skill. Chase aims his at discovering workflows; the vault's [[Grill Me Interview Skill]] aims at capturing knowledge. Same interview style, different output.
- **Team audit.** Each teammate runs Prompts A and B, then you merge the backlogs, keep tasks two or more people repeat, and commit those skills as shared SOPs ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)).
- **Cowork users.** Use Customize, Skills, + to create each skill with Claude, and ask skill-creator to build a clarifying-question step into it ([33:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2010s)). Chase's session-mining route is Claude Code specific; in Cowork, rely on the interview.
- **Codex.** Chase says the same Level 1 work runs in the Codex CLI or desktop app ([03:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=224s)). Point Prompt A at wherever your harness keeps its history.
- **Quick native starting point.** Run Claude Code's `/insights` report before Prompt A and paste its friction points into the interview (Beyond the source).
- **Buttons later.** Once skills are stable, a dashboard can run them headlessly with `claude -p` ([27:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1642s)–[27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s); Jay E's skills deck, [09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s)). See [[Build an Agentic OS Dashboard]].

## Sources

- [[Chase AI - The Agentic OS Setup for Claude Code]]: Level 1 sub-phases ([04:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=275s)–[07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s)), session mining and interview ([07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s)–[10:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=651s)), automation and loops ([10:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=657s)–[13:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=805s)), logging runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)–[22:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1377s)). Captions render "skill creator skill" for Anthropic's skill-creator and "claw desktop" for the Claude desktop app.
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: bottom-up order ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)), the prompted-twice rule and skill-creator ([05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s)–[06:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=390s)), routines after skills and memory ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)–[15:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=943s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: team SOP skills ([05:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=328s)–[05:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=354s)), updating skills after corrections ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: don't write skills up front ([08:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=509s)–[11:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=692s)), scale for productivity ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)).
- [[Simon Pittman - Set Up Claude Cowork]]: creating skills in Cowork ([32:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1956s)–[34:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2041s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]]: domains, tasks and skills ([01:51](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=111s)–[02:31](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=151s)), the spoken interview and local or remote automations ([05:12](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=312s)–[06:23](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=383s)).
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: a daily local chat review that suggests skills ([14:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=889s)).

## Beyond the source

Not from the videos. Each item was checked at the linked page on 2026-09-15.

- **Where the history Chase mines lives.** Claude Code writes each session's full transcript (every message, tool call and tool result) to `~/.claude/projects/<project>/<session>.jsonl`. Files older than `cleanupPeriodDays` are deleted at startup: the default is 30 days, the minimum 1. Transcripts are plaintext and not encrypted, so anything a tool read or printed, including credentials, can end up in them. Sessions you started or last continued in Claude Desktop or Cowork are kept at any age unless you set `desktopSessionCleanupPeriodDays`. Source: [Claude Code docs: Explore the .claude directory](https://code.claude.com/docs/en/claude-directory).
- **A built-in session analysis.** `/insights` analyses up to 200 recent sessions on the machine that it hasn't seen before. It writes an HTML report covering what you work on, friction points and suggestions to `~/.claude/usage-data/report.html`. It doesn't include other devices or claude.ai. Source: [Claude Code docs: Manage costs effectively](https://code.claude.com/docs/en/costs).
- **Skill format and location.** In Claude Code a skill is a folder containing `SKILL.md`: `.claude/skills/<name>/SKILL.md` for a project (commit it to share), `~/.claude/skills/<name>/SKILL.md` for all your projects. Nate describes single files such as `techdebt.md` inside `.claude/skills` ([05:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=334s)); a loose `.md` file there isn't a skill. Single-file prompts are the older `.claude/commands/<name>.md` format, which still works and creates the same `/name` command, but the docs recommend the skill folder for new workflows. Personal skills don't sync to Cowork or cloud sessions, so commit project skills that a cloud routine needs. Sources: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills), [Explore the .claude directory](https://code.claude.com/docs/en/claude-directory).
- **Skill descriptions are already in context.** Only descriptions load by default, and the full skill loads when invoked. So Claude can find a new skill without a CLAUDE.md entry. The docs suggest keeping CLAUDE.md under 200 lines and moving specialised workflow instructions into skills. Sources: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills), [Manage costs effectively](https://code.claude.com/docs/en/costs).
- **Getting skill-creator.** In Claude Code, run `/plugin install skill-creator@claude-plugins-official`. It can also evaluate a skill against test prompts, with and without the skill. Anthropic's skill-creator instructions say that when you're capturing a workflow that already happened in the conversation, it should first pull the steps, tools, corrections and formats from that history. In the Claude apps, skills are under Customize, Skills. Sources: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills), [anthropics/skills: skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [Claude Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
- **Desktop routines, the automation pass.** In Claude Desktop's Code tab, open Routines, choose New routine, then Local, and set a name, description, instructions (with a permission mode and model), a working folder and a schedule. Local tasks fire only while the app is open and the computer awake. After sleep, Desktop runs one catch-up for the most recent missed time within the last seven days, which is why Prompt D asks for a late-run guard. A task in Manual permission mode stalls on unapproved tools; click **Run now** once and choose "always allow". Remote routines run in the cloud against a fresh clone, with no local files and a 1-hour minimum interval. Source: [Claude Code docs: Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks).
- **Skills that scheduled tasks can't use.** Since Claude Code v2.1.196, a skill with `disable-model-invocation: true` also won't run when a scheduled task fires with that skill as its prompt, so don't set it on a skill you plan to automate. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **Dictating the brain dump.** In the Claude Code CLI, `/voice` turns on dictation: hold Space to record, or use `/voice tap` to tap on and off. It needs a Claude.ai login (not an API key) and a local microphone, so it won't work over SSH. Audio goes to Anthropic for transcription and doesn't count toward usage limits. Tap mode stops after 15 seconds of silence or two minutes, so dictate a long brain dump in chunks. Source: [Claude Code docs: Voice dictation](https://code.claude.com/docs/en/voice-dictation).

## Related

- Concepts: [[Agent Skills]] · [[Agentic OS]] · [[Loop Engineering]] · [[Routines and Scheduled Tasks]] · [[Build vs Install Third-Party Skills]] · [[CLAUDE.md as a Router]] · [[Permissions and Approval Gates]]
- Techniques: [[Build a Skill from a Successful Run]] · [[Skill Improvement Loop]] · [[Grill Me Interview Skill]] · [[Schedule Recurring Claude Tasks]] · [[Build a Reference-Rich Skill]] · [[Build an Agentic OS Dashboard]] · [[Keep CLAUDE.md Lean]] · [[Configure Safe Autonomy Permissions]]
- Tools & people: [[Claude Code]] · [[Claude Cowork]] · [[OpenAI Codex]] · [[Chase AI]] · [[Jay E]] · [[Nate Herk]] · [[Ras Mic]] · [[Simon Pittman]] · [[Jack Roberts]]
- [[Home]]
