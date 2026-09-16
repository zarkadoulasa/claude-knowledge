---
type: concept
aliases: ["Self-Verification", "Who Judges Done"]
sources: ["[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/verification, topic/loops, topic/agents, topic/subagents, topic/claude-code, topic/managed-agents, topic/design, topic/skills, topic/media]
---

# Verification Before Done

## In one sentence

Before Claude calls a task finished, it should run something objective against the work: tests, type checks, linters, a screenshot, a browser run or a rubric. For anything that matters, the verdict should come from something other than the agent that did the work.

## How it works

### Why "done" needs proof

- **Claude can't tell whether its own code is right.**
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] defines verification as giving Claude a way to check its work before it treats a task as done, rather than just announcing completion ([08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s), [08:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=535s)).
  - He rates it S tier, arguably SSS ([08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s)). It's basic engineering practice, and working with AI makes it matter more ([08:43](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=523s)).
- **Agents claim more than they did.** [[AI LABS - The Unlazy Skill for Lazy Agents]] names two failure modes:
  - reporting a job done when it isn't, e.g. opening a few files and saying it went through all of them ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s), [02:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=157s));
  - silently dropping the hard part of a multi-part request ([03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s), [03:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=193s)).
  - An honest early stop is acceptable. A false "finished" costs you, because you only find out by checking, and work built on top inherits the gap ([02:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=164s), [02:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=173s)). See [[Agent Laziness]].
- **It gets worse deep into a session.** Completion checks that hold in a fresh context start to slip once real work fills the context ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)).
- **First attempts are rarely right.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] argues that self-checks aim to get a first version 90% of the way there, not 60–65% ([04:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=277s), [04:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=280s)).
- **Checkability shapes the loop.** [[AI LABS - Types of Claude Loops Explained]] recaps two kinds of loop ([01:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=73s)):
  - deterministic loops, where the agent has a solid way to check its work ([01:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=79s));
  - non-deterministic loops, where it has no solid way to check, so you need other ways to handle it ([01:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=87s)).
  - See [[Loop Engineering]].
- **A fancy process isn't proof.** [[AI LABS - Claude Design Skills for Beautiful Sites]] notes that some skills run elaborate workflows and still produce a generic-looking site ([00:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=7s)).
- **The 70% problem.** [[Nate Herk - Build Skills Instead of Agents]]: a skill reports done and you finish the last 20–30% by hand ([07:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=425s)). Build the checks you'd run yourself into the skill instead ([07:12](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=432s)).

### The objective checks sources name

| Check | What it catches | Source |
|---|---|---|
| Tests written **before** the implementation | Wrong or regressed behaviour. Tests written afterwards just pass Claude's own code, which the Sloth calls cheating | Sloth [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s), [09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s); loops video [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s) |
| Tests for the important paths only | Stops test bloat, since strong models tend to test everything | Sloth [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s) |
| Type checker and linter before "done" | Type and lint errors | Sloth [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s) |
| Screenshot, then judge the layout | Visual problems Claude otherwise can't see | Nate [04:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=251s), [09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s); Sloth [09:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=577s) |
| Browser run: open the app, click around | Broken buttons, flows and features | Nate [04:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=254s), [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s); Sloth [09:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=586s) |
| Tool-measured thresholds, e.g. Lighthouse above 90 | Measurable quality targets written as rubric criteria | Managed Agents [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s) |
| A command, its expected output, and the result recorded as evidence | Claims no real run backs up | Unlazy [07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s), [07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s) |
| Design review skills that score or list findings | Layout, type, spacing, accessibility and screen-size problems | Design video [05:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=303s), [09:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=581s), [11:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=705s) |
| Before/after comparison against git | Things that worked before the last change and don't now | Design video [09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s) |
| Runtime checks inside the running app | Failures hiding behind an app that loads and matches the design, where agents tend to stop ([01:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=100s)) | [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: Reticle [02:00](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=120s) |
| Lint rules for coding patterns agents tend to write | Mistakes you'd otherwise read the code to spot | Repos video: anti-slop [11:43](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=703s) |
| Evidence suited to the output: rendered slides, primary sources, persona subagents | Cropped slides, unsupported claims, flat copy | Skills video [07:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=437s) |

### Who judges done: the spectrum

The table orders the sources' answers roughly by how far the judge sits from the worker. The ordering is this note's synthesis; each row is sourced, and weak spots come from the sources unless marked as this note's observation.

| # | Mechanism | Who decides | Weak spot | Where |
|---|---|---|---|---|
| 1 | Self-check to-dos with a confidence gate | The working agent | The agent still grades itself, which is Unlazy's objection to AI LABS' own task-list checks ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)) | Nate [03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s), [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s) |
| 1b | Self-check of screenshots or renders | The working agent: Scrollcraft's keyframes ([08:48](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=528s)), Codex against its storyboard ([06:05](https://www.youtube.com/watch?v=C8dWdic-oK4&t=365s)), Claude's QA pass on UGC clips ([32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s)) | This note's observation: it judges looks, not facts, and a wrong photo caption got through ([11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s)). Chase wants a human in the loop for creative work ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)) | Scrollcraft, motion and marketing videos |
| 2 | Text completion marker (Ralph loop) | Words the agent writes | No single word proves a feature was built properly ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)) | Loops [02:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=124s); Unlazy [03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s) |
| 3 | Judge model (/goal) | A smaller model (Haiku) checking against the prompt's requirements | Has no standard to measure against ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s)) and reads the conversation rather than the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)) | Loops [02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s); Sloth [19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s) |
| 4 | Separate critic or scorer agents | Other agents, the scorer with no edit tools | Fanning a review out across many dimensions is slow and token-heavy ([10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s)) | Loops [07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s), [12:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=730s) |
| 5 | Rubric grader in its own context window | A separate grader whose feedback drives fix-and-resubmit | Not raised in the video. This note's observation: only as good as the criteria, which are all measurable in the demo ([00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s)) | Managed Agents [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s), [01:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=83s) |
| 6 | Evidence gates with runnable checks | A checker script, then the parent re-running each subagent's checks | Slow as tested in the video: it handed out one task at a time, and 3–4 hours produced only a login page ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s), [10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s)). Since changed upstream (Beyond the source) | Unlazy [07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s), [08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s), [08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s) |
| 6b | Held-out acceptance checks | An evaluator whose check method and expected results stay out of the builder's instructions; after each fix the checks run again | Narrated, not measured. This note's observation: checks are only as good as their author | Repos video: Ouroboros [07:58](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=478s) |
| 7 | Design review skills that score | A review skill applying design rules | This note's observation: the video describes results rather than measuring them | Design video [05:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=303s), [09:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=558s), [12:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=723s) |

A person can also be the judge. In the Managed Agents incident demo, a permission policy holds the Slack post until someone approves the draft ([03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s), [03:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=185s)). See [[Permissions and Approval Gates]].

### The principle: separate the worker from the judge

- **Each row moves the verdict further from the worker.**
  - The loops video's reviewer only returns a score and has no editing tools ([10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s)).
  - The Managed Agents grader works in its own context window ([01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s)).
  - Unlazy's orchestrator doesn't take a subagent's word for it; it re-runs that task's checks itself ([08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)). The agent never decides it's done ([08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s)).
- **Two dials, not one** (this note's framing of Unlazy's critique). *Independence* is who judges; *objectivity* is what they judge against. /goal has an independent judge that reads the transcript ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)). AI LABS' earlier task lists had real checks that the agent graded itself ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)). Unlazy turns both dials.

| | Agent judges itself | Something else judges |
|---|---|---|
| **Against impressions or prose** | "95% confident" to-dos; Ralph marker | /goal judge model; a single reviewer agent |
| **Against a runnable standard** | Self-graded task-list checks | Tests as the /goal condition; rubric grader; Unlazy gates plus checker |

### Put the standard in files, not instructions

- **Instructions get lost.** Unlazy's first version just told the agent to be thorough, and instructions are the first thing a long session drops. The fix was to write requirements to a gates file before any work ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s), [07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s), [07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s)).
- **A tick without proof is worse than an empty box.** If a box is ticked but its evidence still says pending, it counts as unmet, and as worse than an empty box ([08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s), [08:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=499s)).
- **Honest failure counts.** An impossible gate is abandoned by name with a reason, and that reason goes in the final report ([08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s), [08:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=532s)).
- **In unattended loops:** tests come first, passing them becomes the goal ([03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)), and a CLAUDE.md line keeps every working version for rollback ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)).

### What counts as evidence

- **"Couldn't tell" is a third verdict.** Reticle marks each tested part worked, didn't work or not enough information ([02:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=146s)). This note's reading: count the third as unmet, like Unlazy's tick whose evidence is still pending.
- **Outside the draft.** [[Nate Herk - Build Skills Instead of Agents]]: Claude approving its own reread isn't verification; the evidence must come from outside the draft ([07:59](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=479s)). Revise on persona issues that recur, not on every note ([07:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=466s)).

## When to use it — and when not to

**Scale the judge to the stakes.** The tiers are this note's synthesis; each element is sourced.

- **Every task:** at least one objective check in the plan (Sloth [08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s); Nate [03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)).
- **Features left running:** the loops video says tests are what let you give the agent real autonomy ([03:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=187s)).
- **Front ends:** screenshot and browser passes. Nate calls browser checks huge for front-end work ([09:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=586s)). He runs about three design–screenshot–fix passes before V1 ([09:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=564s)).
- **Whole-app reviews:** critic or scorer loops. Keep the fan-out version for large apps, and use a normal reviewer agent otherwise ([11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s), [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s)).
- **Large multi-part builds:** evidence gates. Unlazy breaks a large task into a tree of subtasks ([05:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=331s)) and only writes a plan plus per-task gates at depth 4 and up ([06:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=416s)). Lighter checks tend to slip deep into long sessions ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)).
- **Repeat-use skills:** put the checks inside the skill, so your first look is the agent's fourth to sixth ([08:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=537s)).
- **Pages that state facts:** add a human or source-of-truth content check to visual passes (row 1b). Nate still had to check where a button linked ([11:27](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=687s)).
- **Slow creative renders:** skip the autonomous storyboard-driven loop, because each pass is slow (Chase [07:42](https://www.youtube.com/watch?v=C8dWdic-oK4&t=462s)).

**Don't:**
- Test every line (Sloth [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)).
- Treat a judge model without a hard standard as proof ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s), [02:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=170s)).
- Run heavyweight review on small work ([10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s)). The Sloth rates /goal a tier lower on low-usage plans ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).

## Where sources disagree

- **Is /goal enough?**
  - **For:** the loops video calls it the best example of a stateless loop and says it works best when requirements can be checked concretely ([02:15](https://www.youtube.com/watch?v=8wsM0euQOvc&t=135s), [02:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=170s)). The Sloth's example goal is tests passing with no type errors ([19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s)).
  - **Against:** Unlazy says the judge reads the conversation, not the work, and that such loops falter deep into a session ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s), [04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)).
  - **Reconciled:** a condition that names a check whose output lands in the transcript answers both (Beyond the source).
- **Is a self-check verification?** Nate's gate is Claude's own 95% confidence ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)). Unlazy says checks the agent grades itself still leave the agent deciding ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)). Nate's later skills video moves toward Unlazy (see *What counts as evidence*).
- **Do browser checks need an MCP?** Nate names Chrome DevTools ([09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)). The Sloth says browser testing used to need MCPs and is now built in ([09:54](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=594s)), though browser testing still appears among his MCP uses ([10:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=611s)).
- **Iterate to a perfect score?** The design video suggests re-running a scoring skill until the score is perfect ([05:09](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=309s)). Beyond the source: one review skill it names returns a verdict rather than a number, and Anthropic warns that gap-hunting reviewers usually find something.
- **Who judges creative output?** [[Nate Herk - Build Skills Instead of Agents]] lets skills iterate to their criteria, ideally an objective metric ([08:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=510s)), but leaves taste to you ([08:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=526s)). [[Chase AI - GPT-6 Astra Motion Design in After Effects]] keeps a human in the loop (row 1b). In [[Nate Herk - Claude as a One-Person Marketing Team]], Claude's QA pass checked the UGC clips before it reported done ([32:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1978s)), and Nate himself caught a wrong logo in a separate sizzle reel ([28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s)).
- **Do checkers run unasked?** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] says that once installed, Reticle checks every app build and anti-slop runs on every task ([02:07](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=127s), [12:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=724s)). Their docs start new checks on request or with `/reticle`, though remembered flows re-run after each change (Beyond the source).

## Perspectives from sources

- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] ([[The Coding Sloth]]):
  - Verification gets one of his highest ratings, S tier or above ([08:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=511s), [08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s)).
  - He rates Claude Code's built-in code review and security review skills B to A tier, and recommends running them once Claude implements a feature ([05:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=327s), [05:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=334s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] ([[Nate Herk]]):
  - Verification to-dos, the screenshot loop and Chrome DevTools checks ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s), [09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s), [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)).
  - When a correction produces a better result, he writes the lesson into the skill or CLAUDE.md ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
- [[AI LABS - Types of Claude Loops Explained]] ([[AI LABS]]):
  - Tests as the standard for /goal ([02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s)); critic agents ([07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s)), an implementer paired with a scorer ([09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s)) and a rubric scorer that marks out of 100 ([12:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=730s)).
  - A process optimizer that checks the loop itself ([12:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=740s)).
  - See [[Tests-First Goal Loop]] and [[Multi-Agent Review and Scoring Loops]].
- [[AI LABS - The Unlazy Skill for Lazy Agents]] ([[AI LABS]], on [[Leon Lin]]'s [[Unlazy]]):
  - The sharpest critique of existing completion checks ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s), [04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)), and evidence gates as the fix ([07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)).
  - See [[Evidence-Gated Completion Ledger]].
- [[Anthropic - What Is Claude Managed Agents]] ([[Claude Managed Agents]]):
  - You define what done looks like, and Claude keeps working until it gets there ([03:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=225s)).
  - A grader in its own context window checks each attempt ([01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s)). See [[Build an Event-Triggered Managed Agent]].
- [[AI LABS - Claude Design Skills for Beautiful Sites]] ([[Claude Design]]):
  - Verification for design, including exact layout fixes such as how many pixels a cramped date needs ([09:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=599s)).
  - See [[Escaping the Default AI Design Look]].
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] ([[AI LABS]]): Reticle explains each failure so the agent can fix it and retry ([02:31](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=151s)).
- [[Nate Herk - Build Skills Instead of Agents]] ([[Nate Herk]]): verification is the most important of his four skill practices ([06:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=406s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]] ([[Scrollcraft]]): watch the verification pass to learn how the harness behaves ([09:06](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=546s)).

## Beyond the source

*Not from the videos. Checked against the linked pages on 2026-09-15.*

- **Anthropic's best-practices guide makes this its lead tip.**
  - **Escalation path:** a check inside the prompt, then a /goal condition, then a Stop hook (overridden after 8 consecutive blocks), then a verification subagent or dynamic workflow.
  - **Evidence, not assertions:** ask Claude to show outputs, not just say it passed.
  - **Keep reviewers scoped:** a reviewer told to find gaps usually reports some, so limit it to correctness and requirements.
  - **Fresh eyes:** a fresh context reviews better because Claude isn't biased toward code it just wrote. The guide's Writer/Reviewer pattern splits the roles across two sessions, and one Claude can write tests for another to pass.
  - Source: [Claude Code docs: Best practices](https://code.claude.com/docs/en/best-practices)
- **/goal's evaluator only sees the conversation.**
  - **How it works:** it wraps a prompt-based Stop hook. After each turn a small fast model (Haiku by default) returns not yet met, met or impossible. It doesn't run commands or read files.
  - **The docs' fix:** one measurable end state, a stated check such as a test command exiting 0, any constraints, and a turn limit.
  - Source: [Claude Code docs: /goal](https://code.claude.com/docs/en/goal)
- **Ralph Wiggum plugin.** A Stop hook re-feeds the prompt until an exact completion-promise string appears. Its README calls `--max-iterations` the main safety net and credits Geoffrey Huntley with the technique. Source: [anthropics/claude-code ralph-wiggum plugin](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)
- **Managed Agents outcomes are capped.**
  - **Grader:** runs in a separate context window so the agent's implementation choices don't sway it.
  - **Rubric:** markdown with explicit, per-criterion checks.
  - **Cap:** `max_iterations` defaults to 3, with a maximum of 20.
  - **Results:** satisfied, needs_revision, max_iterations_reached, failed or interrupted.
  - Source: [Claude Platform docs: Define outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)
- **Unlazy today.**
  - **Approval before execution:** CHECK lines are shell code that runs with your filesystem, environment, credential and network access, so the checker runs them only with `--approve`. `--reverify` re-runs them.
  - **Evidence:** records a SHA-256 digest of each gate definition.
  - **Optional Stop hook:** installed via `scripts/install-hooks.mjs`.
  - **Dispatch has changed:** the current SKILL.md launches independent ready tasks in waves instead of one at a time, and records launch state in `.unlazy/<scope>/dispatch.json`. That targets the slowness the video hit.
  - Sources: [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy), [Unlazy SKILL.md](https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md)
- **Two review skills the videos name don't output scores.**
  - **Cursor's thermo-nuclear review:** returns prioritised findings, with no score and no fan-out, so the loops video's scoring, fanned-out reviewer is AI LABS' own adaptation. Source: [cursor/plugins SKILL.md](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md)
  - **Jakub Krehel's interface-review:** reviews diffs, PRs or working-tree changes, finds regressions from removed lines, and ends in Block or Approve. Source: [jakubkrehel/skills interface-review](https://github.com/jakubkrehel/skills/blob/main/skills/interface-review/SKILL.md)
- **Self-grading bias is measured.** Panickssery, Bowman and Feng (2024) found LLM evaluators recognise and favour their own generations, and the preference grows with how well they recognise themselves. Source: [arXiv 2404.13076](https://arxiv.org/abs/2404.13076)
- **Repo docs.** Reticle returns pass, fail or "couldn't tell". New checks start when you call `/reticle` or ask, but remembered flows re-run after each change, every run is kept, and it has an in-app HUD (issue #783, a closed bug report about that HUD). Ouroboros's README keeps the grading command and expected result out of the builder's contract. anti-slop's only bundled skill installs it, so a lint step or hook has to run it. Details in [[Build Verification into Every Task]]. Sources: [reticlehq/reticle](https://github.com/reticlehq/reticle), [reticle.sh](https://www.reticle.sh/), [reticle issue #783](https://github.com/reticlehq/reticle/issues/783), [Q00/ouroboros](https://github.com/Q00/ouroboros), [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop)

## Related

- **Concepts:** [[Agent Laziness]], [[Loop Engineering]], [[Plan Before Executing]], [[Subagents and Agent Teams]], [[Context Window Management]], [[Permissions and Approval Gates]], [[Escaping the Default AI Design Look]], [[Agent Skills]]
- **Techniques:** [[Build Verification into Every Task]], [[Evidence-Gated Completion Ledger]], [[Tests-First Goal Loop]], [[Multi-Agent Review and Scoring Loops]], [[Plan-First Workflow]], [[Skill Improvement Loop]], [[Build a Distinctive Site with Design Skills]], [[Build an Event-Triggered Managed Agent]], [[Build a Scroll-Driven Landing Page]], [[Storyboard-First AI Video and Motion Graphics]], [[Build a Brand-Aware Marketing Project]]
- **Tools:** [[Claude Code]], [[Claude in Chrome]], [[Unlazy]], [[Claude Managed Agents]], [[Claude Design]], [[Scrollcraft]], [[OpenAI Codex]], [[Higgsfield]]
- **People:** [[The Coding Sloth]], [[Nate Herk]], [[AI LABS]], [[Leon Lin]], [[Chase AI]]
- [[Home]]
