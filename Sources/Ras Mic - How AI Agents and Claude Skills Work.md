---
type: source
title: "How AI agents & Claude skills work (Clearly Explained)"
creator: "[[Ras Mic]]"
channel: "Greg Isenberg"
url: https://www.youtube.com/watch?v=S_oN3vlzpMw
video_id: S_oN3vlzpMw
published: 2026-04-08
duration: "35:25"
ingested: 2026-09-15
topics: [agent skills, progressive disclosure, context windows, CLAUDE.md and AGENTS.md, building skills from successful runs, recursive skill improvement, subagents, token efficiency, OpenClaw]
tags: [source/youtube, topic/skills, topic/context, topic/agents, topic/subagents, topic/claude-code, topic/models, topic/automation]
---

# Ras Mic - How AI Agents and Claude Skills Work

> **Creator:** [[Ras Mic]] (guest), interviewed by [[Greg Isenberg]] on Greg's podcast · **Published:** 2026-04-08 · **Length:** 35:25 · [Watch on YouTube](https://www.youtube.com/watch?v=S_oN3vlzpMw)

> **Format and harness.** This is a two-person podcast. Ras Mic does almost all the teaching, talking over hand-drawn whiteboard diagrams, with one live demo that counts the tokens in one of his skills. His everyday agent is [[OpenClaw]], a personal-agent harness (details under Beyond the source), not [[Claude Code]]. He uses Claude Code mainly as the example when he explains how a harness builds up context. No Claude Code session, SKILL.md writing or configuration is shown. The model names he uses (Opus 4.6, GPT 5.4) date the episode to April 2026.

## TL;DR

Ras Mic argues that frontier models are now good enough that the context you give them, plus the harness around them, decides whether you get quality or slop. He lists what fills an agent's context window: the provider's system prompt, AGENTS.md or CLAUDE.md, skill metadata, tool definitions, the codebase and the conversation. He says most people should drop always-loaded instruction files. His reasons: they sit in context on every turn, they cost tokens, and the model gets worse as the window fills. Skills are his alternative. Because of progressive disclosure, only a skill's name and description are in context until the agent needs the rest. In his demo that was 53 tokens, against 944 for the whole file.

The heart of the episode is how to build skills:

1. Never write the skill first. Walk the agent through the workflow by hand and correct it until it succeeds.
2. Then have it review that run and write the skill.
3. Each time the skill later fails, have the agent diagnose and fix the problem, then update the skill. Five of these loops made his eight-source YouTube report reliable.

He doesn't install other people's skills: they are an attack vector, and they lack your context. He started with one agent and added a few domain subagents only once his workflows existed. He tries to keep context usage below about 70%. His claim that 95% of people don't need CLAUDE.md contradicts this vault's router notes; see [Caveats & disagreements](#caveats--disagreements).

## Key takeaways

- **The models are good, so context decides the outcome.** He names Opus 4.6 and GPT 5.4 as proof the models are good ([00:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=48s)). The same model can be steered toward quality or toward slop ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s)), and he thinks harness, tools and context will matter even more as models improve ([27:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1647s)). See [[Choosing a Claude Model]].
- **Know what fills the window.** System prompt, instruction file, skill metadata, tools, codebase and conversation all add up ([06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s), [06:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=402s)). When the window is full, the harness compacts ([06:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=419s)). See [[Context Window Management]].
- **His hot take: 95% of people don't need AGENTS.md or CLAUDE.md** ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). The exception is proprietary company information, or a methodology of your own that every conversation needs ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). This clashes with [[CLAUDE.md as a Router]]; compare [[Keep CLAUDE.md Lean]].
- **Skills cost almost nothing until they're used.** Only the name and description are in context ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s), [05:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=319s)). In his demo the whole skill was 944 tokens and its name plus description 53 ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s), [30:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1854s)). See [[Agent Skills]].
- **Don't write a skill before the workflow has worked.** He calls writing it up front the worst thing you can do ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). Instead, walk the agent through the work step by step ([09:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=563s)). After a successful run, ask it to review what it did and create the skill ([12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)). See [[Build a Skill from a Successful Run]].
- **Treat every failure as a skill update.** Ask why it failed, have it fix the problem, then have it update the skill ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)). Five loops made his report skill reliable ([22:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1354s)). See [[Skill Improvement Loop]].
- **Build your own skills; read other people's, don't install them.** Downloaded skills lack your run's context ([12:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=773s)) and are an easy way to be attacked ([13:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=784s)). See [[Build vs Install Third-Party Skills]].
- **Scale for productivity, not for what looks cool** ([14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s)). Start with one agent, then build skills, then add subagents ([15:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=928s), [25:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1548s)). See [[Subagents and Agent Teams]].
- **Keep context between fresh and about 70%.** Quality drops as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s), [31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)). See [[Context Hygiene Routine]].
- **Only tell the model what it can't already know.** Code is context now ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). Don't say "use React" ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)), but do mention a non-default currency ([32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)).
- **Expect a bad first stretch.** Give a new agent setup about two weeks before judging it ([23:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1433s), [24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s)).
- **Give agents the least access they need.** His agent has its own email address rather than access to his inbox ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s), [07:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=461s)). See [[Configure Safe Autonomy Permissions]].

## The context stack at a glance

All from the video, as he draws it. Where current Claude Code behaviour differs, it's noted under [Beyond the source](#beyond-the-source).

| Layer | What it is | When it's in context, per Ras Mic | His advice | Timestamps |
|---|---|---|---|---|
| Provider system prompt | General instructions from the model provider on how to behave | Always | Very important. He read Claude Code's after the leak | [01:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=100s), [01:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=116s) |
| AGENTS.md / CLAUDE.md | Your always-loaded instruction file | Added on every turn, in his words | Skip it unless you have proprietary facts or a methodology needed every turn. Put procedures in skills instead | [02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s), [03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s), [04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s) |
| Skills (SKILL.md) | Name, description and body | Name and description only; the body loads once the agent decides it needs it | Build your own from successful runs; don't install other people's | [03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s), [05:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=319s), [12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s) |
| Tools | Built-in tools such as read and write | Always, because the harness runs tool calls, not the model | (Explanation only) | [06:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=372s), [06:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=381s) |
| Codebase | The project being built | The agent can read and check it | Let the code, or a solid template, show the stack instead of describing it | [06:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=386s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s), [20:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1211s) |
| User conversation | Your back-and-forth with the agent | Grows every turn | Teach workflows here; the conversation becomes the context a skill is written from | [06:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=398s), [11:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=663s) |
| The whole window | The sum of everything above | Starts around 20K tokens, grows toward his stated ~250K limit, then compacts | Stay between fresh and ~70%; it gets "dumb" near 80–100% | [06:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=407s), [06:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=419s), [31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s) |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=0s) Intro

- Ras Mic wants to help people use agents better. He says he disagrees with most of the advice going around ([00:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=4s), [00:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=10s)). The aim is the best outcome, whether you're building something or using an agent for work ([00:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=15s)).
- Anyone can follow it, technical or not, and it leans heavily on diagrams ([00:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=25s)).

### [00:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=42s) The Models Are Good Now

- In earlier episodes they might have disagreed, but his current view is that the models are good. He names Opus 4.6 and GPT 5.4 ([00:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=44s), [00:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=50s)).
- He mentions the two camps among programmers: Opus as the better UI designer, GPT 5.4 as better for back-end work ([00:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=55s), [01:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=60s)). Broadly, though, models have reached "good", even if this isn't AGI ([01:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=64s)).
- Context still matters. You can push the same model toward quality or toward slop, and that's what the episode is about ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s), [01:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=75s)). He gives no model-routing advice. The takeaway is that model choice matters less than context. See [[Choosing a Claude Model]] and [[Route Tasks to the Right Claude Model]].

### [01:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=80s) How Context Windows Actually Work

- **Definition:** context is the model gathering the information it needs to take an action ([01:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=88s)).
- **Layer 1, the system prompt.** Coding agents, and really any agent, start with a general system prompt from the model provider that tells the model how to act ([01:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=96s), [01:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=100s)). Claude Code had recently leaked, and as a developer he got to read its system prompt ([01:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=103s), [01:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=111s)). He calls the system prompt very important ([01:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=116s)).
- **Layer 2, AGENTS.md or CLAUDE.md.** Many people keep one ([01:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=118s)). His position: 95% of people don't need it ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)).
  - Assume the model is already good ([02:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=127s)). His analogy: he wouldn't remind Greg before every recording that he needs a microphone ([02:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=132s)).
  - Coding example: telling Claude Code the codebase uses React is pointless, because it has the code and can check ([02:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=144s), [02:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=152s)).
  - He thinks people put too much weight on the harness and on building context. He is cutting his own setup back to something very minimal ([02:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=156s), [02:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=163s)).
  - Greg asks whether he really needn't bother with the file 95% of the time. Yes, Ras Mic says, unless the information is proprietary ([02:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=177s), [03:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=182s)).
  - **The 5% exception:** information specific to your company, or a methodology of yours that has to be referenced in every conversation ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
  - What bothers him is that the file is added to context on every exchange with the agent ([03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s)).
- **Layer 3, skills and progressive disclosure.** A skill file isn't added to context in full; only its title and description are ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s), [03:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=215s)). His example is a Notion-report skill. Ask for a Notion report and the agent notices it has a matching skill, then opens the whole document ([03:45](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=225s), [03:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=233s)). The name and description are enough for it to recognise the match ([04:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=240s)). He calls himself a skills maxi and promises to show how to craft good skills later ([04:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=249s)).
- **The cost argument.** Content in AGENTS.md or CLAUDE.md is added at every turn ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)). His hypothetical: a thousand-line CLAUDE.md of about 7,000 tokens means spending 7,000 tokens on every run ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s), [04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s)). You most likely don't need to, and it should probably be a skill ([04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)). Keep a context file only for proprietary or personal specifics the model needs at every turn, which most people don't have ([04:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=273s), [04:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=281s)). Otherwise the tokens are wasted on every turn ([04:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=290s)).

### [04:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=295s) The Power of Skills

- **What a skill looks like on his whiteboard** (he says this isn't the literal format): a name, a description, and a body of detailed information underneath ([05:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=300s), [05:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=305s), [05:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=312s)).
- When you create a SKILL.md, only the name and description go into context; the body doesn't ([05:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=316s), [05:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=319s)).
- Two sentences versus a thousand-line AGENTS.md is a couple of hundred tokens versus thousands ([05:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=329s), [05:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=336s)). The agent reads the body only when it realises it needs the skill ([05:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=340s)).
- So a particular way of generating a report or structuring code belongs in a skill the agent pulls in when needed, not in AGENTS.md ([05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s), [05:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=352s)).
- He loves skills but says people build them wrong, and promises the right way ([05:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=359s), [06:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=362s)).
- **Layer 4, tools.** Claude Code has built-in tools such as a read tool and a write tool ([06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s), [06:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=372s)). They have to be in context because the model doesn't call tools itself; the harness around it does ([06:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=379s), [06:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=381s)). See [[Connecting Claude to External Tools]].
- **Layer 5, the codebase** of whatever you're building, whether a web app or a mobile app ([06:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=386s)). Non-technical builders increasingly needn't care which framework it uses ([06:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=392s)).
- **Layer 6, the user conversation** ([06:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=398s)). Together these layers fill the context window ([06:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=402s)).
- **Scale.** A session might start around 20,000 tokens. As the conversation grows it can hit the limit, which he puts at 250,000 tokens ([06:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=407s), [06:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=413s)). That's when Claude Code and [[OpenAI Codex]] compact ([06:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=419s)). Current window sizes are under Beyond the source.
- **Case study: vetting sponsor emails.** His YouTube channel now attracts sponsors. The emails are a mix of good and bad and take a lot of time to comb through ([07:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=430s), [07:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=447s)).
  - He runs an OpenClaw agent that has its own email address ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)). He deliberately hasn't given it access to his own email, because of attack vectors. He has been hacked before and is careful ([07:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=461s), [07:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=463s)). He forwards each sponsor email to the agent's address ([07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s)). See [[Permissions and Approval Gates]].
  - His first instruction was brief: he'd forward emails, it should check every 15 minutes, research each sponsor and say whether it was worth it ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s), [08:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=482s)). That was the whole instruction ([08:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=485s)).
  - The result: every sponsor came back as legit ([08:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=487s)). There were no rejections, no warnings about scams or bad products, and no deep research ([08:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=495s), [08:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=500s)). See [[Agent Laziness]] for the wider pattern of agents doing shallow work.
  - He concluded the model needed a step-by-step guide, and that's the point where he creates a skill ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s), [08:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=507s)).
- **The common mistake:** people spot a workflow and jump straight to creating the skill ([08:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=514s), [08:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=520s)). He calls this the worst thing you can do ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)).
- Why: think about hiring or mentoring someone ([08:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=535s)). You tell them what to do and help when they ask ([09:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=545s)). Ideally you let them fail, then show them how it's done. People learn by experience ([09:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=550s), [09:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=555s)).

### [09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s) How to create Skills

- His method, which he says now gives a 100% hit rate on specific tasks: walk through the workflow with the agent, step by step ([09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s), [09:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=563s)).
- **The walkthrough for sponsors.** He calls it his "YouTube analysis" ([09:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=569s)), but the steps are the sponsor workflow:
  1. He tells the agent he has just sent an email and asks it about the company ([09:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=572s)).
  2. He has it check the company's Twitter, YouTube and Trustpilot, and whether it has raised money ([09:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=577s), [09:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=581s)).
  3. Rule: if two of those don't exist or aren't in good standing, the sponsor is rejected automatically ([09:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=584s), [09:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=588s)).
  4. The agent, running on Opus, agreed the company wasn't good ([09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s)).
  5. It marked the company "No contact" in their Google Sheet ([09:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=596s)).
- Greg describes the frustration. The task seems black and white, and when you ask why it skipped Trustpilot or the funding check, it just tells you you're absolutely right ([09:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=599s), [10:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=609s)).
- **His explanation**, which is a heavy simplification (see Caveats): models don't think, they predict tokens. He says a model maps your words onto a vector space and returns the nearest match, so "capital of France" gives Paris ([10:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=617s), [10:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=624s), [10:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=633s)). All that training data makes it feel like it understands, even like it has emotions ([10:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=642s), [10:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=648s)). So you have to walk it through the work ([10:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=656s)).
- He continued the walkthrough. He told it how to research, it researched, and all of that became part of the context ([10:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=659s), [11:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=663s)). Then he spelled out what a good company looks like, and told it to email him when one is really good ([11:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=665s), [11:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=668s)).
- **Only after a successful run, done again and again, did he convert it into a skill** ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s), [11:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=674s)).
- **Why skills written up front fail.** Whether you write them by hand or have AI write them, they lack any record of what a successful run looks like ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s), [11:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=683s)). In OpenClaw especially, the agent will probably fail at the API call or fetch the wrong data ([11:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=688s), [11:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=692s)). People then decide the technology is terrible ([11:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=696s)). His diagnosis is that they don't understand how agents work. An agent copies what you show it, and if you've shown it nothing there's nothing to copy ([11:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=701s), [11:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=703s)).
- **His revised process** ([11:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=710s)):
  1. Identify the workflow.
  2. Teach it through back-and-forth. Tell it to do the research first, look at the result, ask what it thinks, then tell it to mark the company as bad in the Google Sheet ([11:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=715s), [12:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=720s), [12:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=727s)).
  3. Once that's done, tell the AI to review what it did and create the skill ([12:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=733s), [12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)). Now it writes the skill from how the work actually went ([12:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=742s)).
- He doesn't handwrite skills and doesn't think you need to. AI can write them, and there's even a skill for creating skills, which he calls skill inception ([12:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=748s), [12:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=752s)). What it needs is the record of a successful run ([12:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=754s)). See [[Workflow Audit into Skills]] for choosing which workflows to capture.
- **Why he doesn't install skills** ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)):
  - He'll look at someone else's Notion or social-media skill and review it. He might hand it to his AI and ask what they can learn from it, but he won't download it ([12:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=763s), [12:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=768s), [12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)). His agent needs the context of its own successful run ([12:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=773s)).
  - Skill marketplaces are an easy way to attack someone. Be very careful about downloading a stranger's skills ([12:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=778s), [13:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=784s), [13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)).
  - It all comes back to context. OpenClaw has a memory layer, but the agent only does the right thing when it has proper context ([13:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=791s), [13:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=796s), [13:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=802s)). See [[Agent Memory Patterns]].
  - His preferred route to a skill: do your own workflow together with the agent. After a successful run, tell it to review what it just did and turn that into the skill ([13:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=806s), [13:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=811s)).
- **Greg's four-step summary:** map out the workflow, identify what's right and wrong, iterate, then codify ([13:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=831s), [13:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=835s), [14:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=842s)).
- **Agents are new employees.** Ras Mic agrees. Treat agents like very new hires, not black boxes that know everything. They know a lot from training but not your workflow or your steps ([14:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=845s), [14:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=857s), [14:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=860s)).
- **Mistake: sprawl from day one.** People set up OpenClaw with 15 subagents and 30 skills before building a single workflow of their own ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s), [14:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=872s)). He uses subagents a lot, and there's a right time for them ([14:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=877s)).
- **Scale for productivity, not for what looks cool** ([14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s)). He used Paperclip and loved it, but thinks people would be more productive building their own version from scratch ([14:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=888s), [14:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=894s)).
- Greg: so you're asking people to do the work. Yes ([15:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=905s)). He admits that as a builder he'd benefit from people buying beefed-up products, because he could build one himself ([15:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=913s), [15:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=919s)). But productivity starts with one agent and building up skills. Only then do you add a subagent and have the main agent manage the others ([15:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=928s), [15:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=934s), [15:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=938s)). His analogy: starting a company with 10 employees when you've never managed a team ([15:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=940s)).
- It isn't glamorous; you have to put in the work ([15:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=953s), [15:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=957s)). The human skill of building agents and crafting skills will make you more valuable as models improve ([16:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=960s), [16:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=968s)). As long as LLMs remain token predictors, people who understand these tools are in for a good run ([16:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=974s), [16:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=986s)).

### [16:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=995s) Skill Maxxing

- Despite the title, this chapter is about two minutes of banter with no agent guidance. Topics: the "permanent underclass" meme, knowledge that once took decades now costing about a subscription a month ([17:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1053s)), an unverified story of a vibe-coded app worth a huge sum, and Ras Mic admitting he overthinks launches ([18:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1084s)).
- He then recaps. You don't need an AGENTS.md unless you have something proprietary. Skills are valuable, but build your own ("we have food at home") ([18:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1126s), [18:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1133s), [19:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1140s)).

### [19:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1145s) What you need to build a project

- Model companies have found that agents are very good at writing code, especially TypeScript ([19:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1151s), [19:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1158s)). He says that's why products like [[Claude Cowork]] and OpenClaw have moved so fast: under the hood they write code that calls APIs ([19:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1161s), [19:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1167s)).
- So when you build a project, you don't need skills or an AGENTS.md about your tech stack ([19:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1173s), [19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s)). People used to fill these files with lines like "React and Convex" or "Next.js and Supabase" ([19:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1183s), [19:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1189s)). Unless you have a specific workflow, that's unnecessary, because the code itself has become context ([19:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1193s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
- **Templates are coming back.** What matters more is starting from a solid foundation ([20:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1202s)). Templates were big once, and he expects a renaissance: a good web or mobile template becomes context the agent builds on ([20:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1206s), [20:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1211s), [20:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1218s)).
- He didn't need a big AGENTS.md or CLAUDE.md. He needed to use little context, plus skills ([20:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1225s), [20:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1230s)).

### [20:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1240s) Recursively Building and Improving Skills

- Diagram: a workflow you've set up with the agent becomes a SKILL.md ([20:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1252s), [21:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1261s)).
- Even with a SKILL.md, the agent will mess up at some point, because the skill has gaps ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s), [21:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1274s)).
- **The loop:**
  1. When it messes up, work with it again. Tell it that it failed and have it retry, for example the API call ([21:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1278s), [21:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1283s)).
  2. Or ask it why it failed and what error it got. It will explain in detail, for example that you're out of API credits ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s), [21:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1295s), [21:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1299s)). His "505" error code is loose; see Transcript notes.
  3. Pass the failure back: this is where it failed, fix it ([21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s), [21:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1317s)).
  4. It fixes the problem, writing code or whatever else it takes ([22:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1322s)).
  5. Once it has done the task correctly, and with the fix still in context, tell it to update the skill so this doesn't happen again ([22:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1325s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).
- **Proof point.** His YouTube report generator pulls from about eight data sources, including Notion, Dub, YouTube Analytics and Twitter analytics ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s), [22:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1337s)). No single prompt could do that ([22:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1345s)). It now takes about 10 minutes and runs flawlessly, because he put it through five iterations of this loop ([22:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1350s), [22:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1354s)).
- **Prediction.** If skill marketplaces take off, people will sell well-defined, step-by-step skills, because most people build skills without first working through the workflow with the agent ([22:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1361s), [22:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1367s), [22:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1372s)).
- **Recap of the whole cycle:**
  - Run the workflow by hand, one instruction per step ([23:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1380s)).
  - Once it's complete, create the SKILL.md and keep using it ([23:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1384s)).
  - When it messes up, don't complain: be glad of it ([23:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1389s)).
  - That's your chance to name the error and have it fix itself ([23:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1394s)).
  - Then have it update the skill file ([23:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1400s)).
- **The expectations curve.** Greg: people assume it works from the start, when really there will be a handful of hiccups first ([23:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1403s), [23:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1415s)). Ras Mic draws a dip: an early stretch of investment that is painful, and that harness companies won't tell you about ([23:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1426s), [23:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1433s), [23:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1438s)). Give it about two weeks. That's how long it took him with OpenClaw, which he first thought was garbage ([24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s), [24:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1447s), [24:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1449s)).
- What changed was going lower-level: agents don't think the way people do ([24:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1454s), [24:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1458s)). A colleague who knows the business understands "a report on the financials in Notion". A new hire wouldn't know where to start ([24:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1463s), [24:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1475s)). Greg adds a story from The Office: a new boss asks for a "rundown" and nobody knows what he means, because they lack the context ([24:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1482s), [25:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1524s)).
- Back to the thesis: the models are really good, but context matters more than anything ([25:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1526s), [25:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1533s)). He isn't saying big multi-agent "company" setups don't work. They probably won't work for you straight away, because you haven't built up to them ([25:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1535s), [25:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1544s)).
- **How his own setup grew** ([25:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1548s)):
  - One main agent did everything, including checking his spreadsheet and his sponsor email ([25:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1555s), [25:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1559s)).
  - Once workflows such as sponsor handling were defined, a subagent made sense ([26:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1563s), [26:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1569s)). The marketing subagent handles marketing with its own skills and context. It wasn't created just for the sake of having one ([26:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1572s), [26:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1576s)).
  - He now has five subagents and names marketing, business and personal, three of the five ([26:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1584s), [26:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1586s)).
  - He bets his OpenClaw setup is more productive than anyone else's, because he scaled for productivity rather than looks ([26:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1594s), [26:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1600s)).
- **The harness matters more than ever.** He mentions an unnamed benchmark, which he says he doesn't fully back. It found different output quality from Cursor, Claude Code and Codex ([27:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1625s), [27:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1630s), [27:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1633s)). His reading: the models are very good and will keep improving, but the harness, tools and context will matter even more ([27:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1641s), [27:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1647s)).
- Less is more. Build step by step, and make something productive before adding the shiny new thing ([27:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1655s), [27:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1660s)). He tries every tool, and Paperclip is fantastic ([27:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1666s)). Still, he bets that people who spent two or three weeks prompting OpenClaw into their own Paperclip-style setup, with only what they actually need, would be far more productive ([27:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1672s), [28:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1680s)).
- **He hedges his own advice.** It could change within two weeks, perhaps to "give the agent everything". He points to a new Google memory paper about indexing information ([28:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1706s), [28:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1711s)). For real work today, though, less is more and simple is better ([28:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1718s)).
- Model companies are aiming at programming, building and everyday white-collar work such as finance and contract checks ([28:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1727s), [28:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1736s), [29:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1741s)). The bigger lever is the harness and tooling around the model ([29:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1749s)). The one thing you have that the models don't is your own workflow, taste and strategy, and those can be captured in skills ([29:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1751s), [29:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1760s)).

### [29:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1763s) Context Window Management and Token Efficiency

- Skills pay off when you build them yourself, not when you download his ([29:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1762s), [29:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1767s)). He has published one skill anyway, tells people not to download it, and jokes that he posted it for GitHub stars ([29:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1769s), [29:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1776s)).
- **Demo: his code-structure skill** ([29:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1779s)). It is 116 lines ([29:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1786s)). After AI has generated a lot of code, the skill restructures it the way he likes, so it's easy for him to review ([29:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1789s), [29:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1793s)). See [[Build a Reference-Rich Skill]] for keeping long skill material out of the always-loaded part.
  - Only the name, "code structure", and the description sit in context ([29:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1795s), [30:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1800s)). The description says to use it when several workflows repeat the same operational logic ([30:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1802s)).
  - Ask the agent to clean up the code structure, and it checks its skills and reads the name and description. It decides the skill fits, then loads the rest ([30:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1811s), [30:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1814s), [30:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1821s)).
- **Token count in OpenAI's web tokenizer** ([30:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1831s), [30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)):
  - The whole file is 944 tokens. As an AGENTS.md, that would be added to every chat ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s), [30:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1846s)), and tokens aren't cheap ([30:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1852s)).
  - The name and description alone are 53 tokens ([30:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1854s)).
- Greg adds that it isn't only cost: you also don't want to hit the limit sooner than you have to ([30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s)). Ras Mic: the model gets dumber as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)).
- **Context budget diagram** ([31:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1870s)):
  - About 10% of the window is already taken by the system prompt and similar content ([31:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1879s)).
  - Aim to stay between a fresh window and about 70% ([31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)).
  - From about 80% toward 100%, the model starts to get dumb ([31:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1889s), [31:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1893s)).
  - His human comparison: cramming at the last minute never worked for him at school, because there was too much to absorb at once ([31:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1895s), [31:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1903s), [31:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1916s)).
- Saving context saves money, and it also makes a better-performing agent. Less is more ([31:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1919s), [32:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1924s), [32:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1926s)).
- **What to tell the model.** Rely on its strengths. Give it what's unique to you, your workflow and your business, not general knowledge ([32:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1929s), [32:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1933s)).
  - Don't tell it to use React ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).
  - Don't tell a financial-report agent to write money with a dollar sign, because it will anyway ([32:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1949s), [32:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1953s), [32:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1959s)).
  - A specific non-default currency is worth stating ([32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)).
  - AGENTS.md or CLAUDE.md is for things the agent won't know on its own ([32:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1966s)). Yet he ends by calling these files a farce you don't need and repeating the word "skills" ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s), [32:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1976s)).

### [33:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1982s) Closing Thoughts

- Greg thanks him and points to Ras Mic's links in the show notes ([33:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1983s), [33:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1988s)).
- Ras Mic nearly didn't come on. He felt he had no big new tool to review: few new tools are launching, and the big labs, Anthropic and OpenAI, dominate general-purpose and coding agents ([33:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=2004s), [33:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=2013s), [33:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=2019s)).
- Greg reads out a viewer's message crediting an earlier episode with getting him into coding, then asks for likes and comments ([34:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=2049s), [34:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=2090s)). There's no further technical content.

## Caveats & disagreements

### About the video itself

- **Anecdote, not evaluation.** His claims come without measurement: a "100% hit rate" ([09:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=559s)), a skill that runs flawlessly ([22:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1352s)), and his system being more productive than anyone else's ([26:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1596s)).
- **Different harness.** His hands-on experience is with OpenClaw ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s), [24:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1447s)). The ideas carry over to Claude Code's Agent Skills. The details don't: the agent's own inbox, the subagent layout and the memory layer are all OpenClaw's.
- **"Added at every turn" is imprecise.** He says the instruction file is added on every exchange and in every chat ([03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s), [04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s), [30:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1846s)). Claude Code loads CLAUDE.md once when the session starts, and it then stays in the context window (see Beyond the source). His real point stands and matches the docs: the file occupies context permanently, and skills avoid that.
- **The token numbers are approximate.** He counted with OpenAI's tokenizer, not Claude's ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)), and "1,000 lines ≈ 7,000 tokens" was a hypothetical ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)). The 944-to-53 ratio shows the scale of the saving, not exact Claude numbers.
- **The window size is wrong.** He gives about 250,000 tokens ([06:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=413s)). Claude Code windows are 200K or 1M depending on the model (Beyond the source).
- **"Stay under 70%" is a rule of thumb** with no source ([31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)). The underlying idea, that quality drops as context fills, is backed by Anthropic's own guidance (Beyond the source).
- **"Models don't think" oversimplifies** ([10:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=617s)). Treat it as motivation for spelling workflows out, not as an account of how LLMs work.
- **Internal tensions:**
  - He says never install other people's skills ([12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)), yet predicts people will sell good skills ([22:45](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1365s)) and publishes one of his own ([29:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1769s)).
  - He says he has five subagents but names three ([26:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1586s)).
  - He admits his minimal-context advice could flip soon ([28:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1706s)).
- **Unidentified references.** Neither the harness benchmark ([27:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1625s)) nor the Google memory paper ([28:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1711s)) is named, so don't build on them.
- **The error example is loose.** A "505" code for running out of credits ([21:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1299s)) doesn't match what HTTP 505 means (Beyond the source). The lesson is only that you should ask the agent for the actual error.
- **Dated details.** The models he names ([00:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=50s)) are from April 2026, and the leak he mentions ([01:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=103s)) happened on 31 March 2026 (Beyond the source).
- **Off-topic stretches.** Roughly 16:37–18:43 and most of the outro are banter.
- **Promotion.** No sponsor read. The video description links to the host's own businesses; those links are left out here.

### Where this disagrees with the vault

**1. Do you need CLAUDE.md at all?** Notes affected: [[CLAUDE.md as a Router]], [[Keep CLAUDE.md Lean]], [[Build a Level 1 Second Brain]].

- *Ras Mic:* 95% of people don't need AGENTS.md or CLAUDE.md ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). The only exceptions are proprietary company information or a methodology every conversation needs ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). He ends by calling these files a farce ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).
- *The vault's router note*, drawn from [[Nate Herk - Every Level of a Claude Second Brain]], says the opposite. Every second brain starts with a CLAUDE.md that routes the agent to the right folders, because Claude won't search the whole project on its own ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s), [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)).
- *Other sources in this batch mostly keep a file, but a lean one:*
  - [[Nate Herk - 32 Tricks to Level Up Claude Code]] keeps CLAUDE.md to 150–200 lines at most, because it loads into every conversation ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)). He has it point to other files rather than hold everything ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)).
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] rates CLAUDE.md more highly after months of learning models' bad habits ([04:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=253s)). He also says it isn't make-or-break, and skills can give similar or better results ([04:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=293s)).
  - [[Jay E - The ARMS Framework for a Claude Agentic OS]] calls router files the minimum an agentic OS workspace needs ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)).
  - [[Chase AI - The Agentic OS Setup for Claude Code]] uses his vault's CLAUDE.md for conventions and navigation ([21:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1310s)).
- *How they fit.* This reconciliation is the vault's, not Ras Mic's. Every example he gives of pointless content is something the agent can find out or already knows: the stack of a codebase ([02:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=149s), [19:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1183s)), or defaults like the dollar sign ([32:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1953s)). A router listing where non-code knowledge lives is exactly what an agent can't work out for itself. That is close to his "specific to you" exception ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s), [32:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1966s)). Every source agrees that a bloated file hurts. A workable rule: keep a short file of facts and locations the agent can't discover, and move procedures into skills. See [[Keep CLAUDE.md Lean]].

**2. How the file loads.** Note affected: [[CLAUDE.md as a Router]].
- *Ras Mic:* the file is added at every turn, so its full token count is paid on every chat ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s), [30:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1846s)).
- *Vault note:* it loads at session start ([04:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=271s)).
- *Both are partly right.* It is loaded once and then stays in context for every request that follows; it isn't appended again each turn, though Claude Code re-reads it after `/compact` (Beyond the source).

**3. A stack file in the Level 1 layout.** Note affected: [[Build a Level 1 Second Brain]].
- *Ras Mic:* don't describe your tech stack in context files, because the code already shows it ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
- *Vault:* the Level 1 layout includes `context/stack.md`, a list of the tools you use. That note now carries a stack-file caveat citing this video.
- *How they fit:* his argument is about code repositories. In a knowledge brain the tools may live outside the files, so a stack file can still be worth keeping, but only for facts the agent can't find elsewhere.

**4. Writing a skill before running the workflow.** Note affected: [[Grill Me Interview Skill]].
- *Ras Mic:* writing the skill first is the worst thing you can do ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). Create it from a successful run ([13:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=806s)).
- *Vault:* that technique note provides an original starter SKILL.md written before any real interview had been run. It now recommends a distil-first route, running one interview by hand before Claude writes the skill, and keeps the starter as a fallback.
- *How they fit:* treat the starter as a draft. Run one interview by hand, have Claude rewrite the SKILL.md from that session, then update it after each failure. See [[Build a Skill from a Successful Run]] and [[Skill Improvement Loop]].

**5. Installing other people's skills.** Notes affected: [[Grill Me Interview Skill]], [[Build vs Install Third-Party Skills]].
- *Ras Mic:* don't install other people's skills. They're an attack vector and carry none of your context, so read them and extract the lessons instead ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [13:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=784s)).
- *Vault:* the Grill Me technique gives install commands for [[Matt Pocock]]'s skills from Anthropic's official plugin marketplace.
- *Another source:* [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] values community skills as packaged best practice he learns from ([05:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=339s)). He warns against installing a hundred of them ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)).
- *How they fit:* a reviewed skill from a trusted source carries a different risk from a random marketplace upload, and Anthropic's docs say to use trusted sources only (Beyond the source). Either way, Ras Mic's key point still applies: shape any skill to your workflow through real runs.

**6. Keeping AGENTS.md alongside CLAUDE.md.** Notes affected: [[Tool-Agnostic Context Files]], [[Port a Claude Code Brain to Other Agents]].
- *Ras Mic:* most people don't need AGENTS.md ([18:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1128s)).
- *Vault:* both notes invest in keeping the two files in sync across harnesses.
- *How they fit:* sync only matters if you keep such a file. Under his rule the file would be tiny, which makes syncing trivial. His skills repo gained an AGENTS.md template in August 2026, after this episode (Beyond the source).

**Agreements worth recording**
- *Improving the skill after a correction.* [[Nate Herk - 32 Tricks to Level Up Claude Code]] also says: once Claude produces the better version, have it update the skill or CLAUDE.md so the mistake doesn't recur ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)). That's the last step of Ras Mic's loop ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).
- *Context rot.* [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] describes a "dumb zone" where Claude gets worse as context fills ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)). That matches Ras Mic's claim that models get dumber as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)).
- *Grow only when it hurts.* Ras Mic's "scale for productivity" ([14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s)) is the agent-architecture version of the pick-the-lowest-level principle in [[Second Brain Levels]].

## Build from this

*Build ideas based on the video, written for this vault. The Claude Code commands, paths and APIs they mention don't come from the video; they are checked under Beyond the source.*

1. **Turn a successful session into a skill.**
   - In Claude Code, do a real workflow by hand in one session: give each step, the decision rules and where results go.
   - Correct it until the run fully succeeds.
   - Then ask Claude to review the session and draft `.claude/skills/<name>/SKILL.md`. The draft should have a description that makes the trigger clear, the exact steps, the decision criteria and a "Known failures" section.
   - See [[Build a Skill from a Successful Run]], and [[Workflow Audit into Skills]] for choosing which workflows deserve a skill.
2. **A recursive skill-fix loop.** On every failure:
   - ask for the exact error and its cause;
   - have Claude fix it and re-run;
   - once the run is correct, have it update the skill and add a dated line saying what failed and how it was fixed.
   - Define "stable" up front, for example three clean runs in a row. See [[Skill Improvement Loop]].
3. **Audit CLAUDE.md for slimming.**
   - Go through it section by section. Cut what the model can infer from the code: stack names, directory listings, default formatting.
   - Keep proprietary facts and where-things-live routes. Move multi-step procedures into skills.
   - Compare context usage before and after with `/context`. See [[Keep CLAUDE.md Lean]], [[CLAUDE.md as a Router]] and [[Context Hygiene Routine]].
4. **Report what each skill costs in context.**
   - For every skill, compare the always-loaded tokens (name plus description) with the body, which loads only when the skill is used. Use Claude's token-counting API, not OpenAI's tokenizer.
   - Flag descriptions that overlap and could trigger the wrong skill.
   - Move long reference material into bundled files so it loads only when read. See [[Agent Skills]] and [[Build a Reference-Rich Skill]].
5. **Review third-party skills instead of installing them.**
   - Read the external SKILL.md and every file bundled with it.
   - Flag risky patterns: network calls, credential access, shell commands, embedded instructions.
   - List the ideas worth rebuilding into your own skill from real runs. See [[Build vs Install Third-Party Skills]].
6. **An agent that vets inbound email.**
   - Give it a dedicated inbox rather than yours, and have it check that inbox on a schedule.
   - For each email, research the sender's social accounts, reviews and funding. Reject when two of the four checks fail.
   - Log every result to a sheet, and alert yourself about strong leads.
   - Build the steps with the successful-run method before making it a skill. See [[Schedule Recurring Claude Tasks]], [[Configure Safe Autonomy Permissions]], [[Permissions and Approval Gates]] and [[Connecting Claude to External Tools]].
7. **A skill for a report drawn from several sources.**
   - Assemble a weekly report from several analytics tools by hand first. Turn it into a skill, then harden it over several fix loops.
   - For tools with a lot of internal structure, start from a context map. See [[Build a Context Map for a Connected Tool]] and [[Skill Improvement Loop]].
8. **Grow from one agent to domain subagents.**
   - Start with a single agent.
   - Only once a domain has stable skills, split out a subagent for it with its own skills and context. See [[Subagents and Agent Teams]].
9. **A context budget guard.**
   - Show context usage in the status line.
   - Adopt a personal rule: past about 70% (his heuristic), compact with focus instructions, clear the session, or hand the bulky work to a subagent. See [[Context Window Management]] and [[Context Hygiene Routine]].
10. **Start projects from a template.** Begin new builds from a well-structured template so the code itself carries the conventions, rather than describing the stack in CLAUDE.md. He names no specific template.

## Resources mentioned

- **Ras Mic's code-structure skill** ([29:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1779s), [29:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1786s)). The video gives no link, and he says not to download it. Where it's published is under Beyond the source.
- **OpenAI's web tokenizer** ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)). Not linked in the video; see Beyond the source.
- **A skill for creating skills** ([12:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=752s)). Not named in the video; Anthropic's skill-creator is covered under Beyond the source.
- **Paperclip** ([14:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=888s), [27:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1666s)). Named but not linked in the video; see Beyond the source.
- **Unnamed references.** The harness-quality benchmark ([27:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1625s)) and the Google memory paper ([28:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1711s)).
- **Other tools and products named:**
  - Agents and harnesses: OpenClaw, Claude Code, OpenAI Codex, Cursor, Claude Cowork
  - Data sources: Notion, Dub, YouTube Analytics, Twitter/X analytics, Google Sheets, Trustpilot
  - Models: Opus 4.6, GPT 5.4
  - Web stack examples: React, Convex, Next.js, Supabase, TypeScript
- **Ras Mic online** (from the video description): X https://x.com/Rasmic · YouTube https://www.youtube.com/@rasmic

## Beyond the source

*None of this is said in the video. It was added at ingest on 2026-09-15 and checked against the links given.*

- **How CLAUDE.md actually loads in Claude Code.**
  - It's read at the start of every session and stays in the context window. After `/compact`, the project-root CLAUDE.md is re-read from disk and injected again.
  - The docs suggest keeping each file under 200 lines, because longer files use more context and are followed less reliably.
  - Keep CLAUDE.md for facts needed in every session. Move multi-step procedures, or anything relevant to only one part of the codebase, into a skill or a path-scoped rule.
  - `/doctor` suggests trims for a checked-in CLAUDE.md (v2.1.206+). It cuts what Claude can work out from the codebase, such as directory layouts, dependency lists and architecture overviews. It keeps pitfalls, rationale and conventions that differ from tool defaults, which closely matches Ras Mic's "only tell it what it can't know".
  - Sources: https://code.claude.com/docs/en/memory#write-effective-instructions, https://code.claude.com/docs/en/memory#my-claude-md-is-too-large, https://code.claude.com/docs/en/memory#troubleshoot-memory-issues
- **Anthropic's cost guide makes the same move.** Detailed workflow instructions in CLAUDE.md are present even during unrelated work, while skills load only when invoked. It recommends moving specialised instructions into skills. It also explains that each request re-sends the conversation, with prompt caching lowering the cost of repeated content. So "in context every turn" is accurate; "added again every turn" is not. https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills
- **Progressive disclosure as documented.**
  - Skill metadata loads at startup, at roughly 100 tokens per skill.
  - The SKILL.md body enters context only when the skill triggers, and is typically under 5k tokens.
  - Bundled files load only when read. Bundled scripts run without their code entering context; only their output does.
  - The `description` must say both what the skill does and when to use it, up to 1,024 characters. Claude Code cuts the combined description and `when_to_use` text at 1,536 characters in its skill listing.
  - Once a skill loads, its body stays in context across turns, so keep bodies concise too.
  - After `/compact`, the skill listing isn't re-injected; only skills you actually invoked are kept.
  - Skills marked `disable-model-invocation: true` stay out of context until you invoke them by name.
  - Claude Code looks for custom skills in `~/.claude/skills/` (personal) or `.claude/skills/` (project).
  - Sources: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, https://code.claude.com/docs/en/skills, https://code.claude.com/docs/en/context-window
- **Measure with Claude's tools, not OpenAI's.**
  - `/context` in Claude Code shows which memory files loaded and what is using space.
  - Anthropic's token-counting endpoint (`POST /v1/messages/count_tokens`) is free but rate-limited.
  - Tokenizers differ between vendors, and within Claude too. Claude Opus 4.7 and later and the Fable models use a newer tokenizer that produces roughly 30% more tokens for the same text than earlier models, so recount against the model you use.
  - His demo count came from OpenAI's web tokenizer (https://platform.openai.com/tokenizer), which splits text with OpenAI's encodings, not Claude's.
  - Sources: https://platform.claude.com/docs/en/build-with-claude/token-counting, https://code.claude.com/docs/en/memory#set-up-a-project-claude-md
- **Current window sizes, not 250K.** On the Anthropic API, Claude Code runs Fable 5.1, Fable 5, Sonnet 5, and Opus 4.7 and later with a 1M window by default. Those models auto-compact at about 967K tokens by default. Opus 4.6 and Sonnet 4.6 without extended context compact at the 200K boundary. You can change the compaction window from 100K to 1M with `/autocompact`, `--autocompact` or `CLAUDE_CODE_AUTO_COMPACT_WINDOW`. See [[Choosing a Claude Model]]. https://code.claude.com/docs/en/model-config
- **Quality really does drop as context grows.** Ras Mic's direction is right even though his 70% figure is unsourced. Anthropic's context-engineering post (2025-09-29) calls the effect "context rot": recall falls as the number of tokens rises. It recommends the smallest set of high-signal tokens, and loading data just in time through references and tools. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Keeping context usage visible.** The cost guide suggests showing context usage in the status line, using `/clear` between unrelated tasks, using `/compact` with instructions on what to keep, and handing verbose work to subagents so only a summary comes back. https://code.claude.com/docs/en/costs#manage-context-proactively
- **Skill security.**
  - Anthropic's guidance: use skills only from trusted sources (ones you made or got from Anthropic). Audit every bundled file, and treat installing a skill like installing software. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#security-considerations
  - Cisco (28 January 2026) ran a top-ranked third-party OpenClaw skill through its tests. It found nine issues, including silent data exfiltration via a curl command and prompt injection. Cisco released an open-source Skill Scanner. https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare
  - Snyk's ToxicSkills research (5 February 2026) scanned 3,984 skills from ClawHub and skills.sh. Human review confirmed 76 malicious payloads aimed at credential theft, backdoors and data exfiltration. The larger headline figure, 1,467 skills (about 37%), counts skills with at least one security flaw of any severity, not only malware. https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
  - All of this supports his warning about marketplaces.
- **Anthropic's skill creator.** In Claude Code, `/plugin install skill-creator@claude-plugins-official` adds tooling to test skills: stored test cases, isolated runs, grading, A/B comparisons and description tuning. It pairs well with his loop: draft the skill from a successful run, then check it with evals. https://code.claude.com/docs/en/skills. The skill also lives in Anthropic's public repo: https://github.com/anthropics/skills/tree/main/skills/skill-creator
- **His skills repo today.**
  - The code-structure skill is 116 lines, the same length he gives in the video. It describes separating a service layer from actions so that duplicated operational logic is removed. https://github.com/michaelshimeles/skills/tree/main/code-structure
  - The repo also has skills for isolated worktrees (`new-feature`), evidence-driven testing, before-and-after proof, PR review loops and prose clean-up (`unslop`).
  - It also has an AGENTS.md workflow template chaining those skills together. The repo's commit history dates the template to 28 August 2026, almost five months after this April episode. So it postdates his "you don't need AGENTS.md" stance rather than contradicting it at the time of recording. https://github.com/michaelshimeles/skills/commits/main/AGENTS.md
  - Related vault notes: [[Parallel Sessions with Git Worktrees]] and [[Write Anti-AI Writing Rules]]. https://github.com/michaelshimeles/skills
- **OpenClaw in brief.**
  - It's an open-source (MIT-licensed) AI assistant that runs on your own hardware and works through messaging apps. https://github.com/openclaw/openclaw
  - ClawHub is its public registry for skills and plugins. https://docs.openclaw.ai/clawhub
  - Its memory is plain Markdown in the workspace: a `MEMORY.md` of durable facts loaded at session start, plus dated daily notes, of which today's and yesterday's load automatically only on a bare `/new` or `/reset`. With an embedding provider configured, memory search combines vector and keyword matching. https://docs.openclaw.ai/concepts/memory
  - Compare [[Claude Code Auto Memory]] and [[Agent Memory Patterns]].
- **Paperclip in brief.** An open-source orchestrator (Node.js server with a React UI) that runs a team of AI agents as a business, with org charts, budgets, goals and governance. It works with agents including Claude Code, Codex, OpenClaw and Cursor. https://github.com/paperclipai/paperclip
- **The leak he mentions.** On 31 March 2026, a source-map file in the public Claude Code npm package exposed its source code. Anthropic said no customer data or credentials were exposed. https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/
- **HTTP 505** means "HTTP Version Not Supported"; it isn't a billing error. https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/505. The nearest code, 402 Payment Required, is nonstandard and reserved for future use, so services signal billing problems in different ways; read the actual error body. https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402
- **Ras Mic's name.** His personal site gives his name as Michael Shimeles. https://www.rasmic.xyz/

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Ross, Mike", "Ross Mike" | Ras Mic (Michael Shimeles, @rasmic) |
| "open cloud agent", "Open Cloud", "Open Claw", "open claw", "prompt open Claude" (27:56) | OpenClaw |
| "I don't I given it access" (07:39) | he has *not* given the agent access to his own inbox; it has its own address |
| "paper claw", "paper paperclip" | Paperclip |
| "cloud code" | Claude Code |
| "claw.md", "cloud.md", "Claude.md's" | CLAUDE.md |
| "agent.md", "agent MD" | AGENTS.md (he uses the singular loosely throughout) |
| "Claude co-work" | Claude Cowork |
| "Dub Analytics" (22:17) | probably Dub, the link-analytics platform (likely, not verified) |
| "skill that MD files" (16:06) | SKILL.md files |
| "create the scale out MD file" (23:04) | create the SKILL.md file |
| "limit of 25 250,000 tokens" (06:53) | he corrects himself to about 250,000; the figure itself is inaccurate (see Beyond the source) |
| "OpenAI token tokenizer" (30:35) | OpenAI's web tokenizer |
| "a 505 error, you have insufficient credits" (21:39) | a loose example; 505 isn't a credits error, and the real code is *unclear* |
| "my YouTube uh analysis" (09:29) | from context, the sponsor-email workflow he's walking through |
| "now I have five sub agents" (26:26) | he names only three: marketing, business, personal |
| "Twitter Analytics" | X analytics |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Context Window Management]] · [[Agent Laziness]] · [[Subagents and Agent Teams]] · [[Choosing a Claude Model]] · [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[Agent Memory Patterns]] · [[Claude Code Auto Memory]] · [[CLAUDE.md as a Router]] · [[Tool-Agnostic Context Files]] · [[Second Brain Levels]] · [[Escaping the Default AI Design Look]]
- **Techniques:** [[Build a Skill from a Successful Run]] · [[Skill Improvement Loop]] · [[Workflow Audit into Skills]] · [[Build a Reference-Rich Skill]] · [[Keep CLAUDE.md Lean]] · [[Context Hygiene Routine]] · [[Configure Safe Autonomy Permissions]] · [[Route Tasks to the Right Claude Model]] · [[Schedule Recurring Claude Tasks]] · [[Build a Context Map for a Connected Tool]] · [[Parallel Sessions with Git Worktrees]] · [[Write Anti-AI Writing Rules]] · [[Build a Level 1 Second Brain]] · [[Port a Claude Code Brain to Other Agents]] · [[Grill Me Interview Skill]] · [[Set Up Claude Cowork]] · [[Build a Distinctive Site with Design Skills]]
- **Tools:** [[OpenClaw]] · [[Claude Code]] · [[OpenAI Codex]] · [[Claude Cowork]] · [[Hermes Agent]]
- **People:** [[Ras Mic]] · [[Greg Isenberg]] · [[Nate Herk]] · [[Matt Pocock]] · [[The Coding Sloth]] · [[Jay E]] · [[Chase AI]] · [[Simon Pittman]]
- **Sources compared above:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Chase AI - The Agentic OS Setup for Claude Code]]
- **Sources that cite this:** [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[AI LABS - Types of Claude Loops Explained]]
