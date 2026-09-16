---
type: concept
aliases: ["Claude Models", "Model Selection"]
sources: ["[[Knowing More - Every Claude Model Explained]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Sergei Chyrkov - Claude Design Full Tutorial]]"]
tags: [topic/models, topic/claude-code, topic/cowork, topic/subagents, topic/context, topic/planning, topic/design]
---

# Choosing a Claude Model

> [!warning] Model names in the videos are out of date
> The first six sources were published between 2026-04-08 and 2026-08-20. Between them they name Sonnet 4.6, Opus 4.6, Opus 4.7, an unversioned Haiku, a restricted Mythos and, in passing, Fable. [[Sergei Chyrkov - Claude Design Full Tutorial]] (2026-07-30) already uses the current Opus 5 and Sonnet 5. Timestamped sections record what each video said. The lineup as of 2026-09-15 (Claude Fable 5.1, Opus 5, Sonnet 5, Haiku 4.5) and how to switch between them are under **Beyond the source**. For the hands-on playbook, see [[Route Tasks to the Right Claude Model]].

## In one sentence

Claude comes in speed-and-price tiers: default to the balanced tier, push quick or bulk work down to the small one, move up to the flagship when the work is hard, keeps failing or can't easily be undone, and fix context and harness first, because they now shape results as much as the model does.

## How it works

### 1. The tiers, as one explainer sketched them in May 2026

[[Knowing More - Every Claude Model Explained]] says Claude is a family of models, not one model. It adds that many users pick the wrong one or don't know the others exist ([00:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=4s)). Its sketch of each tier:

| Tier | Character in the video | Use it for | Where it falls short | Timestamps |
|---|---|---|---|---|
| **Haiku** | Smallest and fastest. Just does the task without overthinking | Quick summaries, pulling key facts from documents, simple questions, batch and repetitive jobs | Depth: hard engineering and nuanced analysis. The video compares it to an intern on routine work | [01:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=81s), [01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s), [01:51](https://www.youtube.com/watch?v=BJauPEH_9OU&t=111s), [01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s) |
| **Sonnet** | The everyday workhorse. Considers how best to approach a task before starting | Senior-level coding, serious writing, whole-document analysis, a business's operations brain | None named. It is presented as the default | [02:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=135s), [02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s), [03:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=184s) |
| **Opus** | The paid flagship | Hard engineering, financial modelling, decisions that are hard to reverse | Expensive and token-hungry. The video jokes that you can hit a rate limit within a few prompts | [03:17](https://www.youtube.com/watch?v=BJauPEH_9OU&t=197s), [04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s), [07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s) |
| **Mythos** (restricted; at the time, Claude Mythos Preview) | Withheld from the public for its offensive-security ability, and available only to partners in Project Glasswing | Not a choice for ordinary users | You can't use it | [04:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=292s), [05:10](https://www.youtube.com/watch?v=BJauPEH_9OU&t=310s), [07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s) |

- **Version details it gave.** Sonnet 4.6 came out in February 2026 with a 1M-token window ([02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s)). Opus 4.7 came out in April 2026 at $5 per million input tokens ([03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)).
- **Opus benchmark figures.** It gives Opus 4.7 87.6% on SWE-bench (the published figure is SWE-bench Verified) and 94.2% on GPQA Diamond ([03:38](https://www.youtube.com/watch?v=BJauPEH_9OU&t=218s), [03:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=232s)). Inside the same Opus 4.7 section it cites Rakuten engineers running Opus 4 for seven hours on an open-source refactor as an example of long, focused work ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s)).
- **Why Mythos was held back, in the video's account.** It found vulnerabilities in major operating systems and browsers ([05:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=315s)), and it scored 64.7% on Humanity's Last Exam ([05:31](https://www.youtube.com/watch?v=BJauPEH_9OU&t=331s)).
- **Accuracy.** Every one of these figures is dated, and some are easy to misread: the Rakuten run used an older model, and the Humanity's Last Exam score is a with-tools result. See "Corrections to the Knowing More figures" under Beyond the source.

### 2. Default, then escalate

The video's routing rule has three parts.

- **Sonnet is the default.** The narrator attributes to the community a split of Sonnet for about 90% of work and Opus only when a decision can't easily be undone ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s)–[03:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=181s)). Newcomers should start on Sonnet ([03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s)).
- **Escalate on struggle.** When Sonnet starts to struggle, move up to Opus ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)). The video also says nothing matches Opus on a genuinely hard problem ([04:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=275s)).
- **The final summary.** Haiku for quick, fast, batch and repetitive work because it's cheap ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)). Sonnet for everything else as the balance of intelligence and speed ([06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s)). Opus for hard engineering, financial modelling and irreversible decisions ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)).

The video never explains how to switch models, and never says how to tell that Sonnet is "struggling". Both gaps are filled in [[Route Tasks to the Right Claude Model]].

### 3. Split one job across several models

Four sources split a single job across models, and each splits it along a different line.

- **By volume, per [[Nate Herk - 32 Tricks to Level Up Claude Code]].** Subagents each get their own context window and can each run their own model ([05:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=301s)–[05:04](https://www.youtube.com/watch?v=jqoFP9QapXI&t=304s)). Put the subagents on Haiku for simpler work and keep the main thread on Opus ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)–[05:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=326s)).
  - His hack 13 example is a subagent that scrapes many articles, reads hundreds of thousands of tokens and hands the Opus thread a short summary ([06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=377s)).
  - His reasoning: a heavy, expensive model shouldn't read that much to extract a few facts. Done well, this cuts cost without losing quality where it counts ([06:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=379s)–[06:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=388s)).
- **By phase, per [[The Coding Sloth - 1000 Hours of Claude Code Lessons]].** A smart model writes the plan and a cheaper, faster one implements it ([07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s)–[07:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=461s)).
  - He stresses that "cheaper" doesn't mean dumb. Today's fast models are capable enough for this to work, and it saves money ([07:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=462s)–[07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s)).
  - In Claude Code he would once have planned on Fable. Fable now costs usage credits on his plan, so he plans on Opus and implements on Sonnet ([07:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=473s)–[08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s)).
  - Tools such as Cursor, OpenCode and Codex let you mix models from different vendors ([08:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=485s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s)).
  - The idea came from a skill that audits a codebase and writes plans for other agents to carry out ([06:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=407s)). See [[Plan Before Executing]].
- **By difficulty, per [[AI LABS - The Unlazy Skill for Lazy Agents]].** In orchestrated mode (depth 4+), Unlazy hands each leaf task to its own subagent ([05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s), [06:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=416s)).
  - At that scale AI LABS suggest adding a model-router skill ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)). It sends mechanical subtasks to a cheaper model and the hard parts to a strong one, so a long run doesn't use up your limits early ([12:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=739s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s)).
  - They don't name a specific router.
- **By surface, per [[Sergei Chyrkov - Claude Design Full Tutorial]].** Design on the expensive surface, then build on the cheap one.
  - He designs in Claude Design on Opus 5 ([02:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=139s)) and hits his usage limit mid-session ([07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s)).
  - Claude Design uses a lot of tokens, so he stops iterating there once the layout looks right ([09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s)).
  - He hands off to Claude Code and switches to Sonnet 5. His reasoning is that the design already exists, so building it is much cheaper ([10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s), [11:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=673s)). He still polishes the hero section in Claude Code afterwards ([13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s)).
  - *Vault reading:* this is the Coding Sloth's plan-then-implement split, with a finished design standing in for the plan.

### 4. Choosing a model in Cowork

[[Simon Pittman - Set Up Claude Cowork]] makes picking a model part of setup day, right after choosing the workspace folder ([04:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=270s)–[04:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=273s)).

- **His setup advice.**
  - Turn extended thinking on ([04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s)).
  - Sonnet handles most tasks. Opus is more powerful but uses more tokens ([04:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=276s)–[04:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=284s)).
  - Start with Sonnet; use Opus for ambitious projects ([04:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=295s)–[04:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=299s)). His "faster quick answers" remark just before refers to another menu option *(unclear in captions)*.
- **His own usage.** He is on a Max plan, uses Opus heavily and has had no problems. He says whether that works for you depends on what you pay ([04:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=284s)–[04:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=291s)).
- **His demos match the rule.**
  - A one-page Word brief runs on Sonnet to save credits ([33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s)).
  - Restructuring the workspace into output and project folders runs on Opus ([35:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=2136s)).

### 5. Thinking depth is a second dial

Two sources adjust how hard the model thinks on top of which model it is.

- **Simon** turns extended thinking on in Cowork ([04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s)).
- **Nate** uses the `ultrathink` keyword in Claude Code on architecture decisions, complex debugging, big refactors, or when a couple of prompts haven't produced the right output ([13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)–[13:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=824s)).
  - He says the keyword allocates about 32,000 thinking tokens ([13:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=827s)).
  - It isn't for simple fixes ([13:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=831s)–[13:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=839s)).

Both descriptions predate today's effort settings. The current mechanics are under Beyond the source.

### 6. The counterweight: context and the harness

[[Ras Mic - How AI Agents and Claude Skills Work]] says model choice matters less than it did.

- **His view.** Frontier models are now exceptionally good. He names Opus 4.6 and GPT 5.4 ([00:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=48s)–[00:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=52s)). Arguments like "Opus for UI, GPT for back end" matter less now that the models have reached "good" ([00:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=58s)–[01:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=68s)).
- **Context still decides quality.** The same model can be steered toward quality or toward slop ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s)–[01:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=77s)).
- **Harness and tools will matter more.** He mentions an unnamed benchmark, which he doesn't fully endorse, that found different output quality from Cursor, Claude Code and Codex ([27:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1625s)–[27:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1635s)). His conclusion is that as models improve, the harness, the tools and the context you give will matter even more ([27:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1641s)–[27:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1653s), [29:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1747s)–[29:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1753s)).
- **A strong model can still fail.** His story of an agent skipping obvious checks happened on Opus ([09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s)). His fix was a step-by-step skill, not a bigger model.

Two other sources back this up.

- **Every model gets lazy.** [[AI LABS - The Unlazy Skill for Lazy Agents]] says laziness shows up on every model, including Opus and GPT 5.6. Smaller models just reveal their limits sooner ([00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s)–[01:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=62s)). See [[Agent Laziness]].
- **A bigger window isn't a fix.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] says the "dumb zone" grows with context. A 1M window only extends it, and in his experience quality dips beyond about 100–200K tokens ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s), [13:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=811s)–[13:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=821s)). See [[Context Window Management]].

The practical takeaway: before moving up a tier, check whether a cleaner context or a skill would fix the failure.

### 7. Limitations the model video lists

[[Knowing More - Every Claude Model Explained]] closes with Claude's downsides.

- **Speed.** Claude can be slow ([05:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=358s)).
- **Usage limits.** Free-tier users can hit a wall within two or three prompts, while casual ChatGPT and Gemini users rarely see a limit ([06:03](https://www.youtube.com/watch?v=BJauPEH_9OU&t=363s)).
- **Token use.** Claude uses tokens fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)).
- **Image and video.** The video says Claude doesn't generate images or video and describes it as text and code only ([06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)).
- **Caution.** Claude hesitates more than ChatGPT or Gemini on edgy but legitimate requests ([06:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=382s)). When the narrator wants a blunt answer, they switch to Grok ([06:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=392s)).

The token-use complaint matches the budget worries in two other sources.

- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] can hit his $20 plan's limit with one or two prompts ([00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s)–[00:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=25s)). He points out that usage is counted in tokens, not prompts ([12:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=773s)).
- AI LABS want a model router mainly so that big runs stay within usage limits ([12:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=745s)).

## When to use it — and when not to

| Situation | Tier the sources point to | Who says so |
|---|---|---|
| New to Claude, or unsure | The balanced tier (Sonnet) | Knowing More [03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s); Simon [04:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=297s) |
| Summaries, extraction, simple Q&A, batch jobs | The small tier (Haiku) | Knowing More [06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s) |
| A subagent reading large volumes and returning a short summary | Small tier for the subagent, flagship for the main thread | Nate [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s) |
| Planning a big change | The strongest tier you can afford | Coding Sloth [07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s), [08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s) |
| Carrying out an approved plan | One tier down from the planner | Coding Sloth [07:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=459s), [08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s) |
| Building a site already designed in Claude Design | Sonnet 5 in Claude Code, after designing on Opus 5 | Sergei [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s) |
| Mechanical subtasks in a big orchestrated run | A cheaper model, with hard parts on a strong one | AI LABS [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s) |
| Hard engineering, financial modelling, irreversible decisions | The flagship (Opus) | Knowing More [07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s) |
| The default tier keeps failing | Move up a tier, or think harder on the same model | Knowing More [04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s); Nate [13:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=821s), [13:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=837s) |
| Structural or ambitious work in Cowork | Opus | Simon [04:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=299s), [35:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=2138s) |
| The agent skips steps, drifts or says it's done when it isn't | **Usually not a model problem.** Fix the context, split the task or write a skill first | Ras Mic [01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s), [09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s); AI LABS [00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s) |
| Tight plan limits and a multi-agent setup | Expect subagents to use up the limit whichever model they run | Coding Sloth [20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s) |

## Perspectives from sources

- [[Knowing More - Every Claude Model Explained]]: the only source devoted to model choice. It gives a character sketch of each tier ([01:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=81s)–[05:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=358s)), the default-then-escalate rule ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s), [04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)) and a list of limitations ([05:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=358s)–[06:37](https://www.youtube.com/watch?v=BJauPEH_9OU&t=397s)). It is narration only, and its version numbers are dated.
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: cheap subagents feed an expensive main thread ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s), [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)). He turns on deeper thinking for system-wide decisions or repeated misses ([13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)). He suggests a status line that shows the current model and cost ([00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)–[01:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=61s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: plan on the strongest model and implement on a cheaper one ([07:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=452s)–[08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s)). Fable costs usage credits on his plan ([07:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=478s)). He finds smarter models over-test ([09:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=563s)), and subagents drain small plans ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)).
- [[Simon Pittman - Set Up Claude Cowork]]: in Cowork, Sonnet with extended thinking is the default and Opus is for ambitious projects ([04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s)–[04:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=299s)). He switches per task in his demos ([33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s), [35:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=2138s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: route subtasks by difficulty in large orchestrated runs ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)). Laziness affects every model tier ([00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s)). Claude Code's `/goal` uses a smaller model as its judge ([03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s), [03:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=238s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]], on [[Greg Isenberg]]'s podcast: the models are good enough that context and harness now matter more than which model you pick ([00:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=48s), [27:21](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1641s)). Keep context lean so whichever model you use stays sharp ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)–[31:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1889s)).
- [[Sergei Chyrkov - Claude Design Full Tutorial]]: designs on Opus 5 in Claude Design, then builds on Sonnet 5 in Claude Code to save tokens ([10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s)).

## Where sources disagree

- **Which tier is the everyday default.** Knowing More and Simon default to Sonnet ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s); [04:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=297s)). Nate keeps his main Claude Code thread on Opus and pushes only the subagents down to Haiku ([05:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=323s)–[05:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=326s)).
  - *Vault reading:* the difference is mostly about audience. Knowing More and Simon speak to chat and Cowork users who are watching their limits. Nate is talking about coding sessions where the main thread makes the decisions. Anthropic's current guidance shows a similar split (see Beyond the source).
- **Does Opus use up your limits?** Knowing More says Opus burns tokens and can hit a rate limit within a few prompts ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s)–[04:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=262s)). Simon uses Opus heavily on Max without trouble and says the answer depends on your plan ([04:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=284s)–[04:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=291s)). Both can be true, since limits vary by plan.
- **Do subagents save money or cost it?** Nate says Haiku subagents keep costs down ([06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s)). The Coding Sloth says each subagent is a full conversation of its own, so even a small multi-agent setup can use up a $20 plan's limit ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).
  - *Vault reading:* both are right. A cheap subagent is cheaper than doing the same reading on the flagship, but it isn't free. On a small plan, adding subagents can cost more than they save.
- **How much the model matters.** Knowing More presents the model as the key choice and says many people get it wrong ([00:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=9s)–[00:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=16s)). Ras Mic says context and harness now decide the outcome ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s), [29:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1747s)–[29:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1749s)). AI LABS sit between the two: every model gets lazy, but small ones show it sooner ([00:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=53s)–[00:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=58s)).
- **When to use the flagship.** Knowing More keeps Opus for hard or irreversible decisions ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)). The Coding Sloth uses the strongest model for every big plan ([07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s)). *Vault reading:* a plan for a big change is exactly the kind of decision that is costly to reverse, so the two rules mostly agree.

## Beyond the source

*None of this comes from the videos. It was checked on 2026-09-15 at the links given.*

### The lineup on 2026-09-15

| | Claude Fable 5.1 | Claude Opus 5 | Claude Sonnet 5 | Claude Haiku 4.5 |
|---|---|---|---|---|
| Docs positioning | Demanding reasoning, long-horizon agentic work | Complex agentic coding and enterprise work | Best mix of speed and intelligence | Fastest, near-frontier intelligence |
| Released | 2026-09-01 | 2026-07-24 | 2026-06-30 | 2025-10 |
| API ID | `claude-fable-5-1` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`) |
| Price per MTok (in / out) | $10 / $50 | $5 / $25 | $2 / $10 | $1 / $5 |
| API context window | 1M | 1M | 1M | 200K |
| Relative latency | Slower | Moderate | Fast | Fastest |
| Thinking | Adaptive, always on | Adaptive | Adaptive | Extended |
| Earliest retirement | 2027-09-01 | 2027-07-24 | 2027-06-30 | **2026-10-15** |

- **Where the table comes from.** IDs, prices, latency, thinking and retirement dates: https://platform.claude.com/docs/en/about-claude/models/overview and https://platform.claude.com/docs/en/about-claude/model-deprecations.
- **Release dates.** Fable 5.1: Anthropic's announcement is dated only "September 2026" (https://www.anthropic.com/claude-fable-and-mythos-5-1); launch coverage gives 2026-09-01 (https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/). Opus 5: https://www.anthropic.com/news/claude-opus-5. Sonnet 5: https://www.anthropic.com/news/claude-sonnet-5.
- **Haiku 4.5's retirement commitment runs out next month.** Any rule that hard-codes "Haiku 4.5" needs watching.
- **All current models accept text and image input.** That corrects the video's "text and code only" claim ([06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)). Claude still doesn't generate images. Source: https://platform.claude.com/docs/en/about-claude/models/overview

### Corrections to the Knowing More figures

- **SWE-bench.** Opus 4.7's 87.6% ([03:38](https://www.youtube.com/watch?v=BJauPEH_9OU&t=218s)) is its SWE-bench Verified score. The 94.2% GPQA Diamond figure checks out. Source: https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained
- **Opus 4.7 price.** Opus 4.7 launched 2026-04-16. It cost $5 per million input tokens and $25 per million output tokens, and the video gave only the input price ([03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)). Anthropic also warned that its new tokenizer can turn the same text into roughly 1.0–1.35× as many tokens. Source: https://www.anthropic.com/news/claude-opus-4-7
- **The Rakuten run.** Anthropic's Claude 4 launch post (2025-05-22) credits Claude Opus 4 with a seven-hour open-source refactor at Rakuten. Claude's Rakuten case study describes it differently: Claude Code implementing an activation-vector extraction method in vLLM (about 12.5M lines) with 99.9% numerical accuracy, naming no model. The narration says "Opus 4" ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s)) but files the example under Opus 4.7. Sources: https://www.anthropic.com/news/claude-4, https://claude.com/customers/rakuten
- **Humanity's Last Exam.** The 64.7% ([05:31](https://www.youtube.com/watch?v=BJauPEH_9OU&t=331s)) is Claude Mythos Preview's score with tools. Without tools it scored 56.8%. The same Anthropic page supports the video's vulnerability claim ([05:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=315s)): thousands of high-severity flaws, including in every major operating system and browser. Source: https://www.anthropic.com/glasswing
- **The model's name.** In April–May 2026 the restricted model was Claude Mythos Preview. It is now deprecated in favour of Claude Mythos 5. Source: https://platform.claude.com/docs/en/about-claude/model-deprecations
- **1M context.** The video presents a 1M-token window for Sonnet 4.6 and Opus 4.7 ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s), [03:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=212s)). Anthropic's help page now lists 500K for both models when chatting on paid plans. Source: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans

### What changed since the videos

- **Opus 4.8** launched 2026-05-28. Source: https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/
- **Fable 5 and Mythos 5** launched 2026-06-09. They are the same model with different safeguards. Mythos 5 went first to Project Glasswing partners. Biomedical researchers were promised access later through a trusted-access programme. Source: https://www.anthropic.com/news/claude-fable-5-mythos-5
  - This means the "restricted frontier tier" now has a public counterpart. The Knowing More claim that nobody can use the top model ([07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s)) no longer holds.
- **Sonnet 5** launched 2026-06-30. It is the default on Free and Pro, priced at $2/$10, and Anthropic says it performs close to Opus 4.8. Source: https://www.anthropic.com/news/claude-sonnet-5
- **Opus 5** launched 2026-07-24. It is the default on Max and the strongest model on Pro. It has adjustable effort and a faster, pricier fast mode. Source: https://www.anthropic.com/news/claude-opus-5
- **Fable 5.1 and Mythos 5.1** launched on 2026-09-01 (date per https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/). Fable 5.1 is generally available. Mythos 5.1 goes through trusted-access programmes for cyber defence and life sciences. Source: https://www.anthropic.com/claude-fable-and-mythos-5-1
  - Anthropic's model-choice page describes Mythos 5.1 as available to Project Glasswing participants only. Both descriptions are recorded here. Source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- **Fable costs usage credits on some plans.** Pro plans and Standard seats on Team and Enterprise need usage credits. Max plans and Premium seats can spend up to 50% of their weekly limit on Fable at no extra cost, though the total limit stays the same. On the API, Fable is billed at standard API rates. This confirms what the Coding Sloth said at [07:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=478s) for Pro. Source: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan

### Anthropic's current guidance

- **Two starting strategies.** Source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
  - *Efficiency-first:* start on Haiku 4.5 and upgrade only where you find a capability gap.
  - *Capability-first:* start on Opus 5, then lower effort or move to a cheaper model. Go up to Fable 5.1 if evals at `xhigh` or `max` effort still fall short.
  - The same page says most workloads start with Opus 5, and that changing effort is often a better lever than changing model. Its selection matrix puts sub-agent tasks on Haiku 4.5.
- **The Academy tutorial for app users** calls Sonnet the daily driver. It says to move down to Haiku for quick or simple work, up to Opus when Sonnet struggles, and up to Fable for critical accuracy or when Opus underperforms. It lists token cost per tier as Haiku lightest, then Sonnet, then Opus, with Fable heaviest. Source: https://academy.claude.com/tutorials/choosing-the-right-claude-model
- **Anthropic's two audiences get different defaults.** The API docs start most workloads on Opus 5, while the Academy tutorial for app users calls Sonnet the daily driver. This mirrors the Knowing More/Simon versus Nate split under Where sources disagree.
- **Build an eval set before switching.** The docs call a use-case-specific eval set the most important step in deciding to switch models. Source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- **Two patterns for combining models.** Source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - **Advisor:** a cheaper executor runs the loop and consults a stronger model at hard decisions.
  - **Orchestrator:** a frontier coordinator hands independent work to cheaper workers.
  - The page says to sweep effort on your current model first, and to price the stronger model alone at `low` effort, before building either.
  - These are the grown-up versions of Nate's subagent split and the Coding Sloth's plan/implement split.

### Mechanics that replace the videos' descriptions

- **Thinking controls.** `ultrathink` is now a keyword that asks for deeper reasoning on one turn without changing the session's effort. It no longer sets a fixed 32K budget, which corrects Nate at [13:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=827s). On Fable 5.1, Opus 5 and Sonnet 5 the effort levels are `low`, `medium`, `high`, `xhigh` and `max`, set with `/effort` or `--effort`. Haiku 4.5 has no effort setting. Sources: https://code.claude.com/docs/en/model-config, https://platform.claude.com/docs/en/about-claude/models/overview
  - In the Claude apps, models with effort levels have a Thinking toggle under Effort. Other models keep the "Extended" toggle Simon used. Source: https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
- **Claude Code has built-in model splits.**
  - `opusplan` plans on Opus and executes on Sonnet, which is the Coding Sloth's split as a single alias.
  - Subagents take a `model:` field.
  - An experimental `/advisor` pairs a main model with a stronger adviser.
  - The built-in Explore subagent now inherits the main model, capped at Opus on the Claude API, instead of always running Haiku. To send exploration to Haiku as Nate suggests, define your own `Explore` subagent with `model: haiku`.
  - Sources: https://code.claude.com/docs/en/model-config, https://code.claude.com/docs/en/sub-agents, https://code.claude.com/docs/en/advisor
- **Context windows differ by surface.**
  - In Cowork, Fable, Opus 5 and Sonnet 5 get 1M tokens, and Sonnet 5 auto-compacts at 500K. Haiku 4.5 gets 200K.
  - In chat on paid plans, Fable 5.1, Opus 5 and Sonnet 5 get 1M.
  - Source: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
- **Choosing models in Cowork.**
  - Cowork scheduled tasks have an optional model field. Source: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
  - Enterprise admins can set a default model for chat, Cowork and Claude Code. Members can still pick another model, and Claude remembers each member's last choice. Source: https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization
- **Claude Design shares your plan's limits.** Design activity counts toward the same usage pool as chat, Claude Code and Cowork. There is no separate design allowance (the article says there used to be a weekly one), so Sergei's design-then-build split now draws on a single budget. Claude Design's getting-started article doesn't say which model it runs or whether you can pick one. Source: https://support.claude.com/en/articles/14604416-get-started-with-claude-design
  - *Vault reading:* `opusplan` (above) makes the same split inside a single Claude Code session.

## Related

- Build it: [[Route Tasks to the Right Claude Model]] · [[Plan-First Workflow]] · [[Set Up Claude Cowork]]
- Ideas: [[Plan Before Executing]] · [[Subagents and Agent Teams]] · [[Context Window Management]] · [[Agent Laziness]] · [[Agent Skills]] · [[Loop Engineering]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[Claude Managed Agents]] · [[Unlazy]] · [[Claude Design]]
- Design handoff: [[Create and Reuse a Claude Design System]] · [[Sergei Chyrkov - Claude Design Full Tutorial]]
- People: [[Nate Herk]] · [[The Coding Sloth]] · [[Simon Pittman]] · [[Ras Mic]] · [[AI LABS]] · [[Sergei Chyrkov]]
