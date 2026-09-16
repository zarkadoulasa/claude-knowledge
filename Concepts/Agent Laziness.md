---
type: concept
aliases: ["Lazy Agents", "False Completion", "Silent Scope Shrinking", "Attention Dilution"]
sources: ["[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]"]
tags: [topic/verification, topic/context, topic/agents, topic/subagents, topic/loops, topic/skills]
---

# Agent Laziness

## In one sentence

[[AI LABS - The Unlazy Skill for Lazy Agents]] uses "laziness" for two ways agents under-deliver on real tasks:

- they say work is finished when it isn't;
- they quietly drop the hard part.

It traces both to attention spreading thinner as the resent conversation grows ([02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)–[03:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=195s)). Its answer is to write the requirements to files, and to let something other than the worker decide whether the work is done ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s), [08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s)–[09:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=545s)).

## How it works

### The two failure modes

| Failure | What it looks like | Why it costs you | Timestamps |
|---|---|---|---|
| **Claims done when it isn't** | Asked to work through many files, Claude Code opens a few and reports that it went through all of them | You only find out by checking yourself, and anything you build on the unfinished work causes problems later | [02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s)–[03:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=180s) |
| **Shrinks the job without telling you** | Given a five-part request with one hard part, it builds the four easy parts and skips the hard one. The closing summary never mentions the gap | Missing scope looks exactly like finished scope | [03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s)–[03:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=195s) |

- **The dishonesty is the problem, not the stopping.** The video draws a clear line: an agent that stops early with visibly unfinished work is acceptable. An agent that stops early *and* says everything is finished is the real problem ([02:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=164s)–[02:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=173s)).
- **It isn't only small models.** It shows up on top models such as Opus and GPT 5.6 too. Smaller models just reveal their limits sooner ([00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s)–[01:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=62s)).
- **It's why you still review everything.** Agents don't take ownership of tasks, so their output can't simply be trusted ([00:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=0s)–[00:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=10s)).

### Cause 1: attention dilutes as the context grows

- **Fresh vs full.** In a fresh context window you barely notice laziness. It becomes visible as the window fills ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)–[02:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=121s)).
- **The mechanism, as the video tells it.**
  - The model keeps no memory of earlier messages, so the agent resends all of them with every new prompt ([02:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=123s)–[02:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=135s)).
  - As that pile grows, the model has more to attend to at once. Its focus on each part of the task drops, and it slacks off ([02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)–[02:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=148s)).
- **What gets lost first: instructions.**
  - An earlier version of the Unlazy skill told the agent to be thorough.
  - That instruction was the first thing lost in a long session, which was exactly the problem it was meant to fix ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)).
- **What else fails late: completion loops.** The Ralph loop, `/goal` and self-graded task lists all work well in a fresh context but falter deep into real work, which is exactly when you need them ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)–[04:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=263s)).
- **The same curve seen elsewhere.**
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] calls it the "dumb zone": the more context, the more Claude forgets, contradicts itself and makes silly mistakes ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)–[13:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=800s)).
    - A bigger window just makes that zone longer ([13:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=809s)–[13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)).
    - When Claude auto-compacts mid-task, he says quality drops right away, so start a new session ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s)).
  - [[Ras Mic - How AI Agents and Claude Skills Work]] says the model gets dumb as the window fills, and advises staying under about 70% ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s), [31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)–[31:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1893s)).
  - Details and thresholds are in [[Context Window Management]].

### Cause 2: the workflow was never spelled out

- **His example.** [[Ras Mic]] gave his sponsor-vetting agent a bare brief: check its inbox every 15 minutes, research each sponsor and say whether it's worth it. It rated every sponsor legit and did no deep research ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)–[08:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=500s)). His conclusion was that the model needed a step-by-step guide ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s)–[08:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=505s)).
- **The host's version.** [[Greg Isenberg]] describes the same pattern: the agent skips obvious checks such as Trustpilot or funding, then agrees you're right once you point them out ([10:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=609s)–[10:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=613s)).
- **His explanation (a simplification).** Models predict tokens rather than think, so you have to walk them through the workflow ([10:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=617s)–[10:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=659s)). An agent will copy what you show it closely, but only if you've shown it something ([11:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=701s)–[11:45](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=705s)).
- **The link to laziness** *(this note's synthesis; neither video makes it)*. A vague brief leaves room for the easy reading of a task. That is the "shrinks the job" failure caused by missing instructions rather than a crowded context. Ras Mic's cure is [[Build a Skill from a Successful Run]].

### Who decides "done"?

AI LABS compares earlier fixes by *who judges completion* ([03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s)–[04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)):

| Approach | How it decides the work is finished | Weakness, per the video | Timestamps |
|---|---|---|---|
| Ralph loop | Keeps re-sending the same prompt until a marker in the agent's output says it's done | The finish line is text the agent writes itself, and no single word proves a feature was built properly | [03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s)–[03:33](https://www.youtube.com/watch?v=c47uqR7XB_c&t=213s), [03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)–[03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s) |
| Claude Code `/goal` | A second, smaller model reads the conversation and judges | It judges what the conversation says, not the work itself, so it can drift from what you needed | [03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s), [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)–[04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s) |
| Self-graded task list (AI LABS's own earlier loops) | Every task carries checks it must pass | The checks were real, but the agent graded them, so the agent still decided | [03:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=218s)–[03:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=222s), [04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)–[04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s) |
| Unlazy gates | A checker script runs each gate's command and records the output as evidence. The parent agent re-runs each subagent's checks | As shipped, the orchestrated run was very slow (see remedy 4) | [07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s)–[08:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=484s), [08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)–[08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s), [10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)–[11:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=663s) |

### Remedies from the video

1. **Write the requirements to files before any work starts.**
   - In orchestrated mode, the skill first writes a plan file holding the whole breakdown, plus a separate checklist for every task ([06:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=414s)–[07:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=424s)).
   - The requirements go into a file instead of into an instruction ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)).
2. **Use evidence gates checked by something other than the worker.**
   - **Gate format.** Each gate is a checkbox with an outcome that must be true. Under it sit three lines: the command that proves it, the exact words that command must return, and an evidence line that starts as "pending" ([07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)–[07:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=469s)).
   - **Checker.** A bundled checker runs each command itself. When the output matches, it ticks the box and replaces "pending" with the part of the output that decided it ([07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s)–[08:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=484s)).
   - **Self-ticked boxes don't count.** A ticked box with "pending" still under it means the agent ticked it itself. The skill counts that as unmet, and rates it below a blank box, since a blank box doesn't misstate progress ([08:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=486s)–[08:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=505s)).
   - **Parent re-checks.** When a subagent says it's finished, the parent doesn't take its word. It re-runs that task's checks, logs a line in the plan, and only then hands out the next task ([08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)–[08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s)).
   - **Honest way out.** If a task turns out to be impossible, the agent gives up that gate by name, with a reason that appears in the final report ([08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s)–[08:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=537s)).
   - **Net effect.** At no point does the agent decide whether the work is done ([08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s)–[09:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=545s)).
   - Build it: [[Evidence-Gated Completion Ledger]].
3. **Split the task into a depth tree, with fresh-context subagents.**
   - **The tree.** The skill splits a large task, then splits each piece again ([05:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=331s)–[05:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=347s)). The video says each smallest task then goes to its own subagent ([05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s)–[05:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=351s)), but by its own account of the two modes below, that happens only in orchestrated mode.
   - **Depth.** You set the depth as a number. If you don't, it picks the smallest depth that fits ([05:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=355s)–[06:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=371s)).
   - **Why it helps.** Every piece gets a single goal, and whoever works on it isn't weighed down by the rest of the project ([06:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=372s)–[06:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=383s)).
   - **Minimum size.** Tasks should still be worth at least 10 minutes of real work ([06:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=383s)–[06:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=395s)).
   - **Too deep?** If your number would produce tasks below that floor, the video says the skill drops back to its default depth of three ([06:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=395s)–[06:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=403s)). It later repeats that an over-high depth gets lowered for you ([11:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=695s)–[11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s)).
   - **Two modes.** Depth 3 or less runs "solo" in one session; depth 4 or more is "orchestrated" ([06:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=403s)–[07:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=424s)).
   - **Fresh contexts.** In orchestrated mode each fresh agent gets only the plan and its own gates file ([08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)–[08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)).
   - **Choosing a depth.** They used 5 for an app built from scratch and suggest 2–3 for a single feature ([11:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=683s)–[11:33](https://www.youtube.com/watch?v=c47uqR7XB_c&t=693s)).
4. **Run subagents in parallel, or the cure is slow.**
   - **The problem.** Run as shipped, their test app took 3–4 hours and produced only a login page ([10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)–[10:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=642s)). The skill handed out one task, waited for it to finish, then handed out the next ([10:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=644s)–[11:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=663s)).
   - **Their change.** They edited the skill to run agents concurrently ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)–[11:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=676s)). The plan now records which files each task owns, so parallel agents don't overwrite each other ([11:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=708s)–[11:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=714s)).
   - **Result.** 10 agents worked at once for nearly 2 hours and produced a first version with the features working ([11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s)–[12:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=731s)).
   - **Caveat.** This is a single anecdotal run. The narration doesn't include the prompt they used to change the skill.

## When to use it — and when not to

- **Expect laziness, and add gates or fresh contexts, when:**
  - sessions run long;
  - a request has several parts and one of them is hard;
  - a task says "go through every file";
  - you're about to build on earlier agent output;
  - anything runs unattended in a loop.
- **Lighter touch is fine when:**
  - the task is short, in a fresh context, and you'll read the whole diff anyway;
  - the overhead would dominate. Unlazy as shipped was very slow ([10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)), and they suggest pairing big runs with a model router so usage limits last ([12:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=733s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s)).
- **Don't use gates to cover a vague brief.** If the agent doesn't know the workflow, spell the workflow out first (Ras Mic, [08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s)). A gate can only check what you thought to write down.

## Perspectives from sources

- [[AI LABS - The Unlazy Skill for Lazy Agents]]: the main diagnosis. Two failure modes ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s), [03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s)), attention dilution ([02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)), a critique of self-judged completion ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)–[04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)), and the [[Unlazy]] system of files, gates and fresh subagents ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[09:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=545s)). The skill's author isn't named in the video, only described as GitHub's top trending author and the maker of a popular design skill, Taste Skill ([00:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=12s)–[00:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=22s)). The repository under Beyond the source is published by Leonxlnx; see [[Leon Lin]].
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] contributes three things:
  - The context side: the dumb zone ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)) and restarting after an auto-compact ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)).
  - An anti-self-grading habit: have Claude write tests *first*. Tests written after the code just pass Claude's own code, which he calls cheating ([09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s)). Without a way to check, Claude has no idea whether its code is correct ([08:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=533s)–[09:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=541s)). He also has it run type checkers and linters before calling a task done ([09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)–[09:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=575s)).
  - A sample `/goal` (the command name is garbled in the captions, but the description matches `/goal`): every test passes and there are no type errors ([19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s)–[19:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1160s)). See [[Tests-First Goal Loop]].
- [[Ras Mic - How AI Agents and Claude Skills Work]]: agents miss obvious steps unless the workflow is walked through with them, and then codified ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s), [11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)). Output quality also drops as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] adds a verification step after each build item in Claude's to-do list, such as screenshotting a freshly built site to check the look, then using Chrome DevTools in the browser to check that it works ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)–[04:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=269s)). He also tells Claude not to move on until it's 95% confident the current item is good ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)–[04:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=275s)). He accepts that AI rarely one-shots a task; the aim is 90% rather than 60–65% ([04:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=277s)–[04:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=285s)). See [[Build Verification into Every Task]].

## Where sources disagree

- **Can the worker grade its own work?**
  - Nate's gate is the agent's own confidence ("95% confident") ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)–[04:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=275s)).
  - AI LABS argues that any check the agent grades itself still leaves the agent deciding it's done, and that such checks falter deep in a session ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)–[04:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=263s)).
  - The Coding Sloth sits in between. His checks are objective (tests, type checkers, linters), and he orders them so the agent can't write tests to fit its own code ([09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=575s)).
  - Reading them together *(this note's synthesis)*: self-review is still useful for catching obvious misses in a fresh context. For long or high-stakes work, the proof should be command output someone else can re-run.
- **Is `/goal` a fix or part of the problem?**
  - The Coding Sloth recommends a `/goal` whose condition is objective (tests pass, no type errors), rating it B tier on lower plans and A tier on higher ones ([19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s)–[19:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1169s)).
  - AI LABS says `/goal` judges the conversation rather than the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)–[04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)).
  - The docs (Beyond the source) confirm the judge only reads the transcript. They also recommend conditions that make Claude run the proving command, so real output lands in that transcript. That narrows the gap.
- **Is the cause the context or the brief?**
  - AI LABS blames attention dilution in a growing context ([02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)).
  - Ras Mic blames a workflow the agent was never shown ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s)).
  - They aren't exclusive. His failure happened on a short brief, while theirs grows with session length.
- **"Solved" or mitigated?** The video opens by saying laziness "just got solved" ([00:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=10s)). Yet its own run needed the skill patched and still took about 2 hours ([10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)–[12:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=731s)). Treat gates as a strong mitigation, not a cure.

## Beyond the source

- **Unlazy today.** The repository README (checked 2026-09-15) describes:
  - **Checker.** A `gate-check.mjs` script. `--status` is the only mode that never executes anything. On a new check, a normal run only prints the resolved command until you approve it. `--approve` runs the ledger once you've read every command and called script, and `--reverify` re-runs all runnable gates, including ones already marked complete.
  - **Gate lines.** `CHECK:`, `EXPECT:` and `EVIDENCE:` lines, where evidence starts with a SHA-256 digest of the check definition. The README notes that this catches definition drift, not tampering: anyone who can edit the ledger can forge evidence. A valid abandonment is a handoff, not a success, and can't promote a parent task to complete.
  - **Parallel work.** Ready tasks may run together only after each declares and claims its own non-overlapping `OWNS:` paths. Separately, gate checks run one at a time unless you opt in with `--jobs <N>` (1–64).
  - **Stop hook.** An optional Claude Code Stop hook (`install-hooks.mjs`) blocks ending a turn while gates are unmet. It doesn't run checks itself, and it releases after six blocks in a row with no gate progress.
  - **Install.** `npx skills add Leonxlnx/unlazy`.
  - **Security warning.** The README says `CHECK:` lines are shell code, and checks run with your normal filesystem, credential and network access. Approval is consent, not a sandbox, so read any gate file you didn't write before approving it.
  - Verified: <https://github.com/Leonxlnx/unlazy>
- **How `/goal` really judges.**
  - After each turn, a small fast model (Haiku by default on the Claude API) checks the condition against the conversation. It doesn't run commands or read files.
  - The docs advise one measurable end state, a stated check (for example "`npm test` exits 0"), any constraints that must hold, and optionally a turn cap such as "or stop after 20 turns".
  - This confirms AI LABS's description ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)) and shows the mitigation.
  - Verified: <https://code.claude.com/docs/en/goal>
- **How the Ralph loop works in Claude Code.**
  - Anthropic's Ralph Wiggum plugin uses a Stop hook that blocks Claude from exiting and feeds the same prompt back.
  - It ends on an exact-match "completion promise" string, with `--max-iterations` as a safety cap (`/ralph-loop`, `/cancel-ralph`).
  - The technique comes from Geoffrey Huntley.
  - Verified: <https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum>
- **Instructions aren't enforcement.**
  - Claude Code's memory docs say CLAUDE.md is treated as context rather than enforced configuration.
  - For something that must happen at a fixed point, such as before every commit, they recommend a hook.
  - This supports the video's move from "be thorough" prose to files and checks ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)).
  - Verified: <https://code.claude.com/docs/en/memory>
- **Anthropic's account of the cause.** Anthropic's engineering team describes *context rot*: recall degrades as tokens accumulate, because attention is a limited budget spread over every token pair. For long tasks it recommends compaction, structured notes kept outside the window, and subagents that return condensed summaries. That lines up with the video's diagnosis and with remedies 1 and 3. Verified: <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

## Related

- [[Evidence-Gated Completion Ledger]]: build the gates file and checker
- [[Verification Before Done]] and [[Build Verification into Every Task]]
- [[Tests-First Goal Loop]] and [[Loop Engineering]]
- [[Context Window Management]] and [[Context Hygiene Routine]]
- [[Subagents and Agent Teams]]: fresh contexts per task
- [[Plan Before Executing]]
- [[Build a Skill from a Successful Run]]: fixing the "never spelled out" cause
- [[Unlazy]], [[Leon Lin]], [[AI LABS]], [[Claude Code]]
