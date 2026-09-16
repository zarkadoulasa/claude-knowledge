---
type: source
title: "All The Types Of Claude Loops Explained In 13 Minutes"
creator: "[[AI LABS]]"
channel: "AI LABS"
url: https://www.youtube.com/watch?v=8wsM0euQOvc
video_id: 8wsM0euQOvc
published: 2026-07-09
duration: "13:25"
ingested: 2026-09-15
topics: [loop engineering, agent loops, verification, tests first, subagents, multi-agent review, skill improvement, self-improving workflows]
tags: [source/youtube, topic/loops, topic/verification, topic/subagents, topic/skills, topic/agents, topic/claude-code, topic/memory, topic/automation]
---

# AI LABS - Types of Claude Loops Explained

> **Creator:** [[AI LABS]] · **Published:** 2026-07-09 · **Length:** 13:25 · [Watch on YouTube](https://www.youtube.com/watch?v=8wsM0euQOvc)

## TL;DR

[[AI LABS]] describe themselves as a software company. They argue that agent loops only waste tokens when the loop type doesn't fit the job, and they sort the loops they run in [[Claude Code]] into five types:

1. **Stateless loop.** Ralph or `/goal` repeats work until a completion check passes. It's most reliable when you write tests first and make passing them the goal.
2. **Learning loop.** A skill-improver agent runs a skill with and without it, edits the skill, and keeps a `learning.md` journal in the skill folder.
3. **Multi-agent review loop.** An orchestrate command runs four specialist critics (factual, domain, safety, style) through fix-and-review rounds.
4. **Verification loop.** An implementer works to raise the score given by a separate reviewer that can't edit, modelled on Cursor's "thermonuclear" review.
5. **Workflow improvement loop.** A builder, a rubric scorer (out of 100) and a process-optimizer agent improve the loop as well as the output.

The taxonomy is useful and the setups can be rebuilt. However, it's narration over screen recordings: no prompts, agent files, rubrics or command files are shown (the description says they're in a paid community), and no results are measured. The descriptions of `/goal`, Karpathy's LLM Council and Cursor's review skill are loose; see Caveats and Beyond the source.

## Key takeaways

- **Match the loop to the job.** They say the token burn people complain about comes from using the wrong loop type [00:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=7s), [00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s). See [[Loop Engineering]].
- **Loop engineering, their definition.** Instead of hand-writing the prompts that steer the agent, you build a system that runs the loop itself [00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s), [00:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=58s). Loops split into those whose outcome can be checked (deterministic) and those that need other ways to judge the work [01:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=79s), [01:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=87s).
- **The stateless loop is the building block** of every other loop. It keeps nothing between runs and never improves itself [01:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=106s), [01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s).
- **A model judging "done" needs a hard standard.** `/goal` leaves completion to a model, so pair it with tests written *before* the feature [02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s), [02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s). See [[Tests-First Goal Loop]] and [[Verification Before Done]].
- **Checkpoint unattended runs.** They add a CLAUDE.md line telling the agent to save each working version so it can roll back [03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s), [03:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=221s). Caveats explain why a hook or git step is sturdier.
- **Measure a skill against a run without it, and keep lessons with the skill.** The learning loop compares the same task with and without the skill [06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s). It logs the results in a per-skill `learning.md`, which they call the most important part [06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s). See [[Skill Improvement Loop]] and [[Agent Memory Patterns]].
- **One reviewer has blind spots.** Split review across agents that each cover one dimension, coordinated by an orchestrator that carries context between rounds [07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s), [09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s). See [[Multi-Agent Review and Scoring Loops]] and [[Subagents and Agent Teams]].
- **Separate the worker from the judge.** In the verification loop the reviewer only returns a score and has no editing tools [10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s). See [[Build Verification into Every Task]].
- **Save fan-out review for big finished apps.** Multi-subagent review is slow and token-hungry; a normal reviewer agent is much cheaper [10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s), [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s).
- **Improve the process, not just the product.** Plan, implement and verify gain a fourth step: review the iteration and propose loop improvements [11:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=687s), [12:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=744s).

## The five loop types at a glance

Token cost is given only where the video gives it. "Not stated" means the video doesn't say.

| Loop type | Memory / state | Who judges "done" | Best for | Token cost | Their example | When |
|---|---|---|---|---|---|---|
| **Stateless** · [[Tests-First Goal Loop]] | None; no learning or self-improvement [01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s) | With `/goal`, a smaller model (Haiku) checks the work against the prompt and reprompts [02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s). Anchor it to tests [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s) | Features with requirements you can verify objectively, e.g. with tests [02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s) | Not stated in the video. The description cites one run of about 39 min and 200k+ tokens (no timestamp) | Ralph loop [02:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=124s); `/goal` with the feature passing every test as its condition [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s) | [01:43](https://www.youtube.com/watch?v=8wsM0euQOvc&t=103s) |
| **Learning** · [[Skill Improvement Loop]] | `learning.md` journal in the skill folder, added to every round [06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s) | Skill-improver agent comparing runs with and without the skill; repeats until nothing is left to improve [05:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=353s), [06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s) | Refining a reusable skill or workflow [05:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=307s), [07:08](https://www.youtube.com/watch?v=8wsM0euQOvc&t=428s) | Not stated; each round launches background sessions [06:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=376s) | Skill loop command plus skill-improver agent, used on their community-site skills [05:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=335s), [05:49](https://www.youtube.com/watch?v=8wsM0euQOvc&t=349s) | [04:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=293s) |
| **Multi-agent review** · [[Multi-Agent Review and Scoring Loops]] | Orchestrator holds context from earlier rounds [09:21](https://www.youtube.com/watch?v=8wsM0euQOvc&t=561s) | Four specialist critics report; the main agent applies every fix, over several rounds [08:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=534s) | Any review, coding or not, that needs several perspectives [08:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=513s) | Not stated | `/orchestrate` with factual, domain, safety and style critics [08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s), [08:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=517s) | [07:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=442s) |
| **Verification** · [[Multi-Agent Review and Scoring Loops]] | Findings saved to a JSON file between rounds [10:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=645s) | Separate scorer with no edit tools, against a set metric; the implementer tries to raise the score [09:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=574s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s) | Reaching a quality bar; the heavy variant is only for a whole app built at scale [11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s) | Fan-out variant: very long and token-heavy. Normal reviewer: less time, far fewer tokens [10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s), [11:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=675s) | Review loop command, PRD-reading implementer and thermonuclear reviewer [10:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=619s) | [09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s) |
| **Workflow improvement** · [[Multi-Agent Review and Scoring Loops]] | JSON log of each round's score; optimizer reviews the conversation [12:47](https://www.youtube.com/watch?v=8wsM0euQOvc&t=767s), [12:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=771s) | Rubric scorer (out of 100) as the quality guardrail, plus a process optimizer [12:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=730s), [12:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=740s) | Building a whole app part by part while testing and refining the workflow [12:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=758s), [13:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=782s) | Not stated | `/iterate all` with builder, scorer and process-optimizer agents [11:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=717s), [12:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=756s) | [11:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=695s) |

Reading the table as a ladder (the vault's framing, not the video's): memory grows from nothing, to a per-skill journal, to a per-round score log. The judge moves from a small model reading the conversation, to specialist critics, to a scorer that can't edit, to a rubric plus a process critic.

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=8wsM0euQOvc&t=0s) Intro

- Agent loops are heavily hyped, and because they eat tokens you might suspect AI companies push them to sell usage [00:00](https://www.youtube.com/watch?v=8wsM0euQOvc&t=0s), [00:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=5s). Their counter: heavy burn comes from choosing the wrong loop type [00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s).
- They've tried loops on their own AI coding tasks and matched each type to its use cases [00:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=16s), [00:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=22s). They share only the ones they found genuinely useful, with setup steps and the workflow impact [00:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=27s), [00:31](https://www.youtube.com/watch?v=8wsM0euQOvc&t=31s).

### [00:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=38s) Loop engineering

- This is a quick recap; the full breakdown is in an earlier video on their channel [00:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=41s), [00:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=45s).
- **Core idea:** stop hand-writing the prompts that steer the agent and make it a system that runs its own loop [00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s). The captions say "writes the loop"; see Transcript notes.
- Skip the setup and the long structured prompts and let the agent handle the work [00:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=58s). They add that it picks up lessons, adapts to obstacles and decides its next step [01:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=63s). That fits the later loop types better than the stateless one (see Caveats).
- **Their earlier split by outcome** [01:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=73s):
  - **Deterministic:** the target result is known in advance, so the agent has a reliable yardstick and keeps going until it's met [01:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=79s).
  - **Non-deterministic:** there's no reliable self-check, so something else has to judge the work [01:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=87s).
- That split was broad, and their earlier video showed only one build of each. Each type can be built many ways, and each setup changes what's possible [01:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=96s), [01:40](https://www.youtube.com/watch?v=8wsM0euQOvc&t=100s).

### [01:43](https://www.youtube.com/watch?v=8wsM0euQOvc&t=103s) The stateless loop

- It's the type most viewers have already used and the base of every other loop; `/goal` is the clearest example [01:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=104s), [01:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=108s).
- **Stateless** means it retains nothing and doesn't get better as it works. No step learns from what happened, which makes these the simplest loops [01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s), [01:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=117s), [02:00](https://www.youtube.com/watch?v=8wsM0euQOvc&t=120s).
- **Ralph loop:** memoryless. It repeated the same task and stopped once it saw the task was finished [02:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=124s), [02:08](https://www.youtube.com/watch?v=8wsM0euQOvc&t=128s). Origin and plugin details are under Beyond the source.
- **`/goal`, as they describe it:**
  - Put what you want built after the command; Claude adopts it as the goal and starts [02:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=137s), [02:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=142s).
  - When the main agent thinks a task is done, a smaller model (Haiku in Claude Code) double-checks the work against the prompt's requirements [02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s), [02:31](https://www.youtube.com/watch?v=8wsM0euQOvc&t=151s).
  - If anything is missing, it reprompts the agent to finish [02:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=158s).
  - The docs describe the check differently; see Caveats.
- **The problem:** the loop relies entirely on a model to call a task done, with no standard to measure against [02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s). It suits features whose requirements can be verified objectively [02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s).
- **Tests as the standard** (a practice from their earlier video) [02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s):
  - Tests come first, before any feature is requested [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s).
  - If Claude then changes a feature wrongly, the failing tests signal the implementation is off [03:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=182s).
  - With every feature covered, the agent can work autonomously without breaking other features or building the target one wrong [03:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=187s), [03:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=192s).
- **The workflow:** once the tests exist, tell Claude Code the goal is for this feature to pass every test [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s). It writes code and reruns the tests until all pass, then marks the goal complete [03:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=202s), [03:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=209s). See [[Tests-First Goal Loop]].
- **Rollback rule:** because the agent works alone, add one CLAUDE.md line telling it to save every working version of the app [03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s), [03:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=217s).
  - If it later breaks something, it reverts to the last good version rather than undoing changes from memory [03:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=221s), [03:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=226s).
  - The exact wording and the saving mechanism aren't given. See [[Keep CLAUDE.md Lean]] and [[CLAUDE.md as a Router]].

### [04:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=293s) The learning loop

- **The contrast:** the stateless loop holds no state and doesn't improve itself; the learning loop does the opposite [04:56](https://www.youtube.com/watch?v=8wsM0euQOvc&t=296s), [05:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=301s). Rather than finishing and stopping like `/goal`, it improves something you reuse, such as a skill or workflow [05:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=307s), [05:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=312s).
- **Mechanism:** run the skill, observe the results, improve it, and record every lesson [05:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=316s), [05:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=322s). Later, in real use, the agent knows what went wrong before and avoids it [05:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=325s), [05:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=329s).
- **Why they built it:** building their community website produced several skills for repeated workflows, which raised the question of whether a skill actually works as intended [05:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=335s), [05:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=342s).
- **Setup** (see [[Skill Improvement Loop]]):
  1. **Skill loop command.** Its instructions invoke a skill-improver agent repeatedly until it finds nothing more to fix [05:49](https://www.youtube.com/watch?v=8wsM0euQOvc&t=349s), [05:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=353s).
  2. **Skill-improver agent.** A custom agent that assesses the skill's quality, tests it across several areas and watches for issues [05:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=358s), [06:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=361s).
  3. **Run it** and name the skill to improve [06:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=369s).
- **Each round** [06:14](https://www.youtube.com/watch?v=8wsM0euQOvc&t=374s):
  - After editing, it runs its tests and checks [06:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=376s).
  - It spins off a background Claude session dedicated to a single prompt, which never pauses for permission and reports back [06:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=380s), [06:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=384s). The mechanism isn't named; possible candidates are under Beyond the source.
  - Those sessions run the implementation both with and without the skill, to measure what the skill really changes [06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s), [06:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=394s).
  - The comparison pinpoints what to fix, and the improver edits the skill directly [06:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=396s), [06:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=398s).
- **`learning.md`, the key piece** [06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s):
  - Stored in the skill's own folder, it records which approaches succeed or fail [06:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=404s), [06:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=408s).
  - It's a structured improvement journal [06:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=410s). Each entry covers the attempt and its outcome with and without the skill, and the file keeps lessons from all rounds [06:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=414s), [06:59](https://www.youtube.com/watch?v=8wsM0euQOvc&t=419s).
  - No entry format is shown. See [[Agent Memory Patterns]] and [[Claude Code Auto Memory]].
- Rounds continue until the skill is as refined as it gets, and the same setup works for any workflow [07:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=424s), [07:08](https://www.youtube.com/watch?v=8wsM0euQOvc&t=428s).

### [07:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=442s) Multi-agent review loop

- **Bridge from their earlier video** [07:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=433s): an implementer agent plus a reviewer that reports fixes back.
- **The flaw:** one reviewer handles every aspect alone, but real reviews draw on many perspectives, which is too much ground for a single agent [07:23](https://www.youtube.com/watch?v=8wsM0euQOvc&t=443s), [07:28](https://www.youtube.com/watch?v=8wsM0euQOvc&t=448s). Agents that each review one dimension cover each other's blind spots [07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s), [07:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=462s).
- **Inspiration:** [[Andrej Karpathy]]'s LLM Council. They describe it as agents that debate a topic, pooling several models' reasoning to reach the right answer [07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s), [07:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=472s). The repo works differently; see Beyond the source.
- **Their four critic agents** [08:00](https://www.youtube.com/watch?v=8wsM0euQOvc&t=480s):

  | Critic | Checks | Special tools | When |
  |---|---|---|---|
  | Factual correctness | Whether claims are true | Web search, to back claims with real sources | [08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s), [08:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=487s) |
  | Domain checker | Relevance of the reviewed work to the goal | None mentioned | [08:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=491s) |
  | Safety critic | Sensitive content, security risks, policy violations | None mentioned | [08:18](https://www.youtube.com/watch?v=8wsM0euQOvc&t=498s) |
  | Style critic | Clarity, writing quality, fit to the target style | None mentioned | [08:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=506s) |

- The critics work for coding and non-coding tasks alike [08:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=513s).
- **Orchestrate command:** detailed instructions for coordinating the four agents and handling each one's feedback [08:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=517s), [08:40](https://www.youtube.com/watch?v=8wsM0euQOvc&t=520s). You point it at anything to review and it launches the critics [08:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=528s), [08:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=532s).
- **Rounds:** all critics run each round. The main agent applies every reported fix, then relaunches them [08:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=534s), [08:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=538s), [09:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=542s). After the last pass the app is in much better shape [09:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=544s). Round count and stop condition aren't given.
- **Orchestrator vs agent teams:**
  - If you want the agents to talk to each other directly, Claude Code agent teams (from an earlier video) give more of a council feel, with no single agent routing messages [09:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=549s), [09:14](https://www.youtube.com/watch?v=8wsM0euQOvc&t=554s).
  - They chose the orchestrator because one agent needs the earlier rounds' context to coordinate [09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s), [09:21](https://www.youtube.com/watch?v=8wsM0euQOvc&t=561s). See [[Subagents and Agent Teams]].

### [09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s) The verification loop

- **Shape:** one agent implements, another scores, and the implementer's job is to push the score as high as possible against a set metric [09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s), [09:31](https://www.youtube.com/watch?v=8wsM0euQOvc&t=571s), [09:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=574s). A command runs the whole review workflow [09:40](https://www.youtube.com/watch?v=8wsM0euQOvc&t=580s).
- **The scorer's basis, Cursor's "thermonuclear review", as they describe it:**
  - A strong review skill that judges code health and cleanliness so future work stays easy [09:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=584s), [09:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=588s).
  - It audits all the code and returns a deep review held to non-negotiable standards [09:56](https://www.youtube.com/watch?v=8wsM0euQOvc&t=596s), [09:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=598s).
  - Because it covers many categories, it runs as a dynamic workflow, fanning out to parallel subagents that each take one aspect [10:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=603s), [10:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=609s).
  - The fan-out and scoring look like AI LABS's own adaptation; see Caveats and Beyond the source.
- **The two agents** [10:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=615s):
  - **Implementer:** reads the PRD and builds the required functionality [10:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=619s), [10:21](https://www.youtube.com/watch?v=8wsM0euQOvc&t=621s).
  - **Thermonuclear code reviewer:** only returns a review score, so it has no editing tools [10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s).
- **Demo run of the review loop command** [10:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=633s):
  1. It establishes what the app is supposed to do, then starts round one [10:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=635s), [10:39](https://www.youtube.com/watch?v=8wsM0euQOvc&t=639s).
  2. Round one flags issues, including a critical bug that stops the app from starting [10:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=641s), [10:43](https://www.youtube.com/watch?v=8wsM0euQOvc&t=643s). This is the video's only concrete result.
  3. Findings go into a JSON file, the implementer is launched to address them, and the loop repeats [10:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=645s), [10:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=650s).
- **Cost warning:** with so many dimensions fanned out across subagents at once, it takes a very long time and uses a lot of tokens [10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s), [10:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=657s), [11:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=661s). They'd only use it once a large app is fully built and needs a thorough review [11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s).
- **Cheaper variant:** the same loop with an ordinary reviewer agent instead of the dynamic workflow is quicker and far lighter on tokens [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s), [11:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=675s).
- Not shown: the metric definition, a target score, a round cap, or the JSON format.

### [11:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=695s) The workflow improvement loop

- **Motivation** (starts just before the chapter mark): none of the earlier loops had a step for improving the loop itself, which they call central to what a loop should do [11:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=687s), [11:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=690s). This one studies the process and suggests workflow changes [11:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=697s), [11:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=701s).
- **How it differs from the learning loop:** the learning loop improves one skill inside the process; this one improves the whole process [11:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=706s), [11:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=711s), [11:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=713s).
- **Entry point:** an iterate command that orchestrates each run [11:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=717s).
- **Three agents** [12:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=723s):
  1. **Builder:** implements one app requirement per run [12:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=724s), [12:06](https://www.youtube.com/watch?v=8wsM0euQOvc&t=726s).
  2. **Scorer:** grades the work out of 100 against a rubric they wrote as the app's quality guardrail [12:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=730s), [12:14](https://www.youtube.com/watch?v=8wsM0euQOvc&t=734s). The rubric isn't shown.
  3. **Process optimizer:** handles self-improvement [12:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=740s).
- A normal loop cycles plan, implement, verify, repeat. The optimizer adds a pass over each iteration that proposes improvements [12:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=744s), [12:28](https://www.youtube.com/watch?v=8wsM0euQOvc&t=748s), [12:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=750s).
- **`iterate all`** builds the entire app, split into parts, within one workflow [12:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=756s), [12:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=758s). Per run:
  1. The builder builds [12:43](https://www.youtube.com/watch?v=8wsM0euQOvc&t=763s).
  2. The scorer grades against the rubric, and scores accumulate round by round in a JSON file [12:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=765s), [12:47](https://www.youtube.com/watch?v=8wsM0euQOvc&t=767s).
  3. The optimizer reads the conversation for workflow improvements and checks quality and that the right steps were followed [12:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=771s), [12:55](https://www.youtube.com/watch?v=8wsM0euQOvc&t=775s), [12:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=778s).
- **Outcome:** a built app plus a refined workflow in which every step has been shown to be necessary [13:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=782s), [13:06](https://www.youtube.com/watch?v=8wsM0euQOvc&t=786s). Not shown: whether optimizer suggestions are applied automatically or reviewed by a person, or any evidence that it helped.

## Caveats & disagreements

**About the video itself**

- **Nothing buildable is shown verbatim.** The description says all agents, commands and skills are in their paid community. No prompts, agent definitions, rubrics, JSON formats or command files appear on screen. The vault rebuilt the setups in [[Tests-First Goal Loop]], [[Skill Improvement Loop]] and [[Multi-Agent Review and Scoring Loops]] from the narration.
- **Sponsor.** A sponsor read for the MiniMax M3 model (03:50–04:53) is omitted; its claims weren't checked.
- **Nothing is measured.** No before/after skill scores, rubric numbers or evidence that the optimizer helped. The only concrete result is the startup bug caught in round one [10:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=641s). The 39-minute, 200k+ token run appears only in the description.
- **"Learns as it goes" overstates it.** The definition claims learning [01:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=63s), but the stateless loop has no learning step by their own account [01:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=117s). The multi-agent loop's only memory is the orchestrator's context.
- **`/goal` is described loosely.** The video has the small model check whenever the agent thinks it's done [02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s), and has you type what to build [02:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=139s). Per the docs, the evaluator runs after every turn, reads only the conversation (no commands, no file reads), and works best with a measurable end state plus a stated check. Their tests-first advice fits that.
- **LLM Council is mischaracterised.** The video says its agents argue [07:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=470s). In the repo, models answer independently, rank each other's anonymised answers, and a chairman combines them. The "arguing" picture is closer to the debate example in the agent-teams docs.
- **Thermonuclear review is probably adapted.** The video claims fan-out and a numeric score [10:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=603s), [10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s). Cursor's published skill is a single qualitative pass against a list of presumptive blockers, with no fan-out and no numeric score.
- **Permissions risk goes unmentioned.** The learning loop's background sessions skip permission prompts [06:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=384s) with no warning. See [[Permissions and Approval Gates]] and [[Configure Safe Autonomy Permissions]].

**Conflicts with existing vault notes (both sides kept)**

- **[[Claude Code]]: CLAUDE.md as a safety net.**
  - *Video:* one CLAUDE.md line is the rollback mechanism for unattended runs [03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s).
  - *Vault:* that note's Beyond the source cites the docs: CLAUDE.md is context, compliance isn't guaranteed, and must-happen actions belong in hooks.
  - *Reconciled:* keep the line as a nudge, and back it with a git commit step or hook. Built-in checkpoints don't cover bash or subagent edits.
- **[[Claude Code]]: loop mechanisms.** Not a conflict. Its scheduling table covers routines, desktop tasks and `/loop`, while `/goal` [02:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=135s) sits in its separate /loop and /goal section. Its first source showed no subagents or hooks, so this video's subagents, custom commands, agent teams and dynamic workflows are additions, not corrections.
- **[[Claude Code Auto Memory]]: who curates memory.**
  - *Vault:* that note's memory table lists curated ingest, where [[Nate Herk]] and Claude decide together what goes in ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)). [[Context vs Connections]] and [[Agent Memory Patterns]] carry his caution, from [[Nate Herk - Every Level of a Claude Second Brain]], that too much context can do more harm than good, which is why he controls ingest ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
  - *This video:* an agent appends to `learning.md` every round with no human review shown [06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s), [07:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=421s), which risks bloat or locking in wrong lessons.
  - *Reconciled:* cap and prune the journal, and link a short lessons summary from SKILL.md. See [[Agent Memory Patterns]].
- **[[Andrej Karpathy]].** Not a conflict: that note now lists the LLM Council, citing this video [07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s), alongside the LLM Wiki. The video's account of how the council works is inaccurate (above).
- **[[Second Brain Levels]].** Not a conflict: its rule of picking the lowest level that fixes a pain you actually have matches this video's advice to keep fan-out review for large finished apps [11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s).

**Where other sources in this batch agree or push back**

- **Six weeks later, the same channel says these finish checks fall short.** [[AI LABS - The Unlazy Skill for Lazy Agents]] argues:
  - Ralph's finish line is just text the agent writes ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)).
  - `/goal`'s judge reads the conversation rather than the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)).
  - Their own task-list loops let the agent grade its own checks ([04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s)).

  See [[Evidence-Gated Completion Ledger]] and [[Agent Laziness]].
- **Tests-first: agreed.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] ranks verification top tier ([08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s)). He warns that if Claude implements before writing tests, it writes tests that pass its own code ([09:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=544s)).
- **Loop hype: skeptical.** The same video mocks the loop trend as rediscovering the for loop ([15:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=939s)). It also rates `/goal` lower on smaller plans because of token use ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).
- **Separate grader: agreed.** [[Anthropic - What Is Claude Managed Agents]] shows a grader in its own context window checking output against the demo's rubric criteria before Claude fixes it and resubmits ([01:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=75s)).
- **Different definition of loop engineering.** [[Chase AI - The Agentic OS Setup for Claude Code]] defines it as recording runs so loops can learn from past iterations ([02:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=156s)). That matches the learning and workflow-improvement loops here, not the stateless one.
- **Skill improvement by hand.** [[Ras Mic]] feeds each failure back to the agent ([21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s)) and has it update the skill once fixed ([23:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1398s)), in [[Ras Mic - How AI Agents and Claude Skills Work]]. The learning loop automates that.
- **The same pattern outside code.** [[Simon Pittman]] tells Claude to update its memory or instructions after feedback so a behaviour sticks, in [[Simon Pittman - Set Up Claude Cowork]] ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)).
- **Lighter in-session verification.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] puts check steps (screenshot, DevTools) straight into Claude's to-do list, with no extra agents ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)).

## Build from this

Parts from the video carry timestamps; vault additions lean on Beyond the source.

1. **Tests-first `/goal` harness with real checkpoints.**
   - *Video:* failing tests first [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s), the goal "this feature passes all tests" [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s), and a save-working-versions rule [03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s).
   - *Vault:* phrase the goal as a check with constraints and a cap, e.g. "`npm test` exits 0, no test file modified, or stop after 20 turns". Run in auto mode and commit on green via a hook or explicit step.
   - See [[Tests-First Goal Loop]], [[Build Verification into Every Task]], [[Keep CLAUDE.md Lean]].
2. **Skill learning loop.**
   - *Video:* a skill-loop entry point re-invokes a `skill-improver` subagent [05:49](https://www.youtube.com/watch?v=8wsM0euQOvc&t=349s), which runs with/without-skill comparisons in background sessions [06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s), edits the skill, and appends to `learning.md` [06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s).
   - *Vault:* keep test prompts and assertions in the skill folder (as Anthropic's skill-creator does), cap rounds, and link a short lessons section from SKILL.md.
   - A good first target is a skill you already use, e.g. [[Grill Me Interview Skill]] (originally by [[Matt Pocock]], per [[Nate Herk - Every Level of a Claude Second Brain]]).
   - See [[Skill Improvement Loop]], [[Build a Reference-Rich Skill]], [[Agent Memory Patterns]].
3. **Four-critic review orchestrator.**
   - *Video:* `/orchestrate` plus factual (web search), domain, safety and style critics [08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s); the main agent fixes, then respawns them each round [08:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=538s).
   - *Vault:* stop when no new high-severity findings appear or after three rounds; keep a findings file per round.
   - See [[Multi-Agent Review and Scoring Loops]], [[Subagents and Agent Teams]].
4. **Score-maximizing verification loop.**
   - *Video:* PRD-driven `implementer`, reviewer with no edit tools [10:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=619s), JSON findings [10:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=645s), and cheap vs heavy modes [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s).
   - *Vault:* give the reviewer read/search tools only; use a 0–100 rubric; stop at a target score or after two flat rounds. Save the heavy mode as a Claude Code dynamic workflow.
   - See [[Multi-Agent Review and Scoring Loops]], [[Build Verification into Every Task]].
5. **Self-improving `/iterate` workflow.**
   - *Video:* `builder`, `scorer` (rubric, JSON score log) and `process-optimizer` [12:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=723s), [12:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=765s), [12:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=771s).
   - *Vault:* the optimizer proposes diffs to command and agent files for a person to approve.
   - See [[Multi-Agent Review and Scoring Loops]], [[Loop Engineering]].
6. **Loop picker.**
   - *Vault:* a checklist or small skill that recommends one of the five types, names the available hard check (tests, rubric, none), and flags relative cost before launch. It's based on the table above and the cost warning at [10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s).
   - See [[Loop Engineering]].
7. **Isolated A/B runs.**
   - *Vault, not in the video:* run with/without-skill comparisons or parallel builders in separate git worktrees so they can't overwrite each other.
   - See [[Parallel Sessions with Git Worktrees]].

Vault starter layout covering all five loops. None of this is shown in the video; fill it in yourself:

```text
.claude/
├── skills/
│   ├── skill-loop/SKILL.md        # learning loop entry point (video calls it a command)
│   ├── orchestrate/SKILL.md       # multi-agent review entry point
│   ├── review-loop/SKILL.md       # verification loop entry point
│   ├── iterate/SKILL.md           # workflow improvement entry point ("iterate all")
│   └── <skill-under-test>/
│       ├── SKILL.md               # links to learning.md's lessons section
│       └── learning.md            # per-round journal: tried / with vs without / lessons
└── agents/
    ├── skill-improver.md
    ├── factual-critic.md          # tools include WebSearch
    ├── domain-critic.md
    ├── safety-critic.md
    ├── style-critic.md
    ├── implementer.md             # edit tools
    ├── code-reviewer.md           # read/search tools only; returns score + findings
    ├── builder.md
    ├── scorer.md                  # grades against rubric.md, out of 100
    └── process-optimizer.md
loops/
├── rubric.md
├── review-findings.json           # verification loop, one entry per round
└── iterate-rounds.json            # workflow improvement loop, one score per round
```

## Resources mentioned

- **Their earlier loop-engineering video** (deterministic vs non-deterministic, tests-first, implementer + reviewer) [00:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=45s), [07:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=433s), and **their agent-teams video** [09:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=551s). Neither is linked in the captions or description.
- **Ralph loop** [02:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=124s).
- **Claude Code `/goal`** [02:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=135s), with Haiku as the checker [02:31](https://www.youtube.com/watch?v=8wsM0euQOvc&t=151s).
- **CLAUDE.md** [03:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=214s).
- **Karpathy's LLM Council** [07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s).
- **Claude Code agent teams** [09:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=549s).
- **Cursor's thermonuclear review** [09:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=584s).
- **Claude Code dynamic workflows** [10:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=603s).
- **Their custom commands and agents** (skill loop, orchestrate, review loop, iterate, plus the agents above): available only in their paid community, per the description.

## Beyond the source

*Not said in the video; added at ingest and verified at the links given.*

- **How `/goal` works.**
  - It wraps a session-scoped, prompt-based Stop hook. After each turn, the condition and conversation go to the small fast model (Haiku by default on the Claude API), which returns not-yet-met, met or impossible.
  - The evaluator calls no tools, so it judges only what Claude has surfaced.
  - The docs recommend a measurable end state, a stated check, constraints, and an optional turn clause. `/goal` doesn't change permission mode, so use auto mode for unattended turns. It also runs under `claude -p`.
  - Source: https://code.claude.com/docs/en/goal
- **`/goal` vs `/loop` vs Stop hooks.** `/goal` continues until the evaluator is satisfied, `/loop` fires on a time interval, and a settings Stop hook can run a deterministic script. Claude Code overrides a Stop hook that blocks eight times in a row without progress. Sources: https://code.claude.com/docs/en/goal, https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks
- **Anthropic's own taxonomy** (blog, 30 June 2026) sorts loops by trigger: turn-based, goal-based, time-based and proactive. It favours deterministic completion criteria and secondary review agents. AI LABS instead sorts by memory and who judges, so the two views complement each other (vault's comparison). Source: https://claude.com/blog/getting-started-with-loops
- **Ralph.**
  - Geoffrey Huntley's technique is a bash loop that keeps re-feeding one prompt file, with tests as backpressure. Source: https://ghuntley.com/ralph/
  - Anthropic's `ralph-wiggum` plugin does this with a Stop hook, a `--completion-promise` phrase, and a recommended `--max-iterations` cap. Source: https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md
- **CLAUDE.md rules aren't enforcement.**
  - CLAUDE.md arrives as a user message after the system prompt, so strict compliance isn't guaranteed; use hooks for must-run steps. Source: https://code.claude.com/docs/en/memory#troubleshoot-memory-issues
  - Checkpoints (`/rewind`) track only Claude's file-tool edits, not bash changes, usually not subagent edits, and aren't a git replacement. Source: https://code.claude.com/docs/en/checkpointing
- **Score-only reviewer.** Subagents in `.claude/agents/` take a `tools` allowlist (e.g. `Read, Grep, Glob`) or `disallowedTools: Write, Edit`. `isolation: worktree` gives one its own worktree. Source: https://code.claude.com/docs/en/sub-agents
- **Commands, skills and `learning.md`.** Custom commands have merged into skills. Claude reads supporting files in a skill folder only when needed, so SKILL.md should say what each holds; keep SKILL.md under 500 lines. Source: https://code.claude.com/docs/en/skills
- **With-skill vs without-skill evals already exist.** Anthropic's skill-creator runs each test case with and without the skill in parallel subagents, grades assertions, benchmarks pass rate, time and tokens, and iterates. Sources: https://code.claude.com/docs/en/skills#run-evals-with-skill-creator, https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- **Background sessions that don't ask permission (unconfirmed mechanism).**
  - Plausible route 1: `claude -p` with `--permission-mode auto` (a classifier reviews actions) and `--permission-prompts none` (anything that would prompt is denied). Source: https://code.claude.com/docs/en/headless
  - Plausible route 2: `bypassPermissions`, which disables prompts *and* safety checks. Source: https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode
- **Dynamic workflows.** Claude writes a JavaScript orchestration script that runs in the background, with up to 16 concurrent agents and 1,000 per run. Workflows can be saved to `.claude/workflows/`. A "Large workflow" warning appears past 25 agents or 1.5M projected tokens. Source: https://code.claude.com/docs/en/workflows
- **Agent teams.** Experimental and off by default (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Teammates message each other directly and share a task list. They cost significantly more tokens than one session, and the docs suggest 3–5 teammates. Source: https://code.claude.com/docs/en/agent-teams
- **LLM Council.** Models answer independently, review and rank anonymised peer answers, and a chairman compiles the final answer; there's no direct debate. Source: https://github.com/karpathy/llm-council
- **Cursor's thermo-nuclear-code-quality-review** (in the `cursor-team-kit` plugin) is a strict single-pass maintainability review. It hunts for "code judo" simplifications, treats a change that pushes a file past 1,000 lines as a strong smell, ranks findings with structural regressions first, and gates approval on a list of presumptive blockers. It has no numeric score and no fan-out. Source: https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "goal command" | Claude Code's `/goal` command |
| "gold command" (05:10) | `/goal`; mis-transcription |
| "Claude.md" | CLAUDE.md |
| "Claude code" | Claude Code |
| "Ralph loop" | the Ralph Wiggum loop ("Ralph" for short) |
| "a system that writes the loop itself" (00:56) | as captioned; the description says *runs* the loop, which fits the rest of the video |
| "how to build a loop agents" (07:13) | most likely "two agents" (implementer + reviewer); likely |
| "LLM council that Andrej Karpathy released" | Karpathy's LLM Council repo |
| "cursor has thermonuclear review" | Cursor's thermo-nuclear-code-quality-review skill; likely |
| "dynamic workflow", "agent teams workflow" | Claude Code dynamic workflows; Claude Code agent teams |
| "skill loop command", "review loop command" | custom commands; exact names never shown (*uncertain*) |
| "orchestrate command", "iterate all" | custom `/orchestrate`; `/iterate` with an `all` argument; likely |
| "learning.md" | kept; the description spells it the same way |
| "contains the detailed instructions" (08:40) | subject dropped: the orchestrate command contains them |
| "by understanding what the app is meant to build" (10:35) | start dropped: the review loop command first works out the app's purpose |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Loop Engineering]] · [[Verification Before Done]] · [[Subagents and Agent Teams]] · [[Agent Memory Patterns]] · [[Claude Code Auto Memory]] · [[CLAUDE.md as a Router]] · [[Agent Skills]] · [[Agent Laziness]] · [[Permissions and Approval Gates]] · [[Second Brain Levels]]
- **Techniques:** [[Tests-First Goal Loop]] · [[Build Verification into Every Task]] · [[Multi-Agent Review and Scoring Loops]] · [[Skill Improvement Loop]] · [[Build a Reference-Rich Skill]] · [[Parallel Sessions with Git Worktrees]] · [[Keep CLAUDE.md Lean]] · [[Configure Safe Autonomy Permissions]] · [[Evidence-Gated Completion Ledger]] · [[Grill Me Interview Skill]] · [[Build a Level 1 Second Brain]] (its dated decision log is the human-curated cousin of `learning.md`)
- **Tools:** [[Claude Code]]
- **Sources in this batch:** [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Anthropic - What Is Claude Managed Agents]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[Simon Pittman - Set Up Claude Cowork]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Nate Herk - Every Level of a Claude Second Brain]]
- **People:** [[AI LABS]] · [[Andrej Karpathy]] · [[The Coding Sloth]] · [[Chase AI]] · [[Ras Mic]] · [[Simon Pittman]] · [[Nate Herk]] · [[Matt Pocock]]
