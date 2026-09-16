---
type: source
title: "GitHub's #1 Trending Author's New Claude Skill Is Insane"
creator: "[[AI LABS]]"
channel: "AI LABS"
url: https://www.youtube.com/watch?v=c47uqR7XB_c
video_id: c47uqR7XB_c
published: 2026-08-20
duration: "12:54"
ingested: 2026-09-15
topics: [agent laziness, evidence-gated completion, gates ledger, depth tree decomposition, subagent orchestration, parallel dispatch, context dilution, completion loops, cross-agent skill install, model routing]
tags: [source/youtube, topic/skills, topic/verification, topic/loops, topic/subagents, topic/context, topic/agents, topic/claude-code, topic/portability, topic/models]
---

# AI LABS - The Unlazy Skill for Lazy Agents

> **Creator:** [[AI LABS]] · **Published:** 2026-08-20 · **Length:** 12:54 · [Watch on YouTube](https://www.youtube.com/watch?v=c47uqR7XB_c)

## TL;DR

[[AI LABS]] review [[Unlazy]], an open-source agent skill by [[Leon Lin]] (GitHub: Leonxlnx, also the author of the Taste design skill). The video never names him; it calls him GitHub's number-one trending author.

**The diagnosis.** [[Agent Laziness]] comes from a growing session: the history that gets resent every turn spreads the model's attention. The agent then either says unfinished work is done or quietly drops the hard part. The usual fixes (the Ralph loop, Claude Code's `/goal`, AI LABS' own self-graded task lists) still leave the "done" call to agent-written text, a transcript-reading judge, or the agent itself.

**How Unlazy works.**
1. **It splits the task into a tree** whose depth you choose. Each leaf must be worth at least ten minutes of work. At depth 3 or less it runs *solo* in one session. At 4 or more it runs *orchestrated*, with each leaf in a fresh subagent.
2. **It writes a gates file before any work starts.** Each outcome gets a command, the words the command must return, and an evidence line that starts as `pending`. A bundled checker runs the commands and fills in the evidence. A ticked box that still says pending counts as unmet.
3. **It doesn't trust subagents.** The parent re-runs every subagent's checks. Impossible gates must be abandoned in writing, with a reason.

**The catch.** As shipped, orchestrated mode handed out one leaf at a time. In their run, 3–4 hours produced only a login page. They had the agent edit the skill to run subagents in parallel, with file ownership recorded in the plan. That rerun had 10 agents going at once and produced a working first version in about two hours.

**Availability.** The editing prompt is shown only on screen, and their refined version is paywalled. Upstream Unlazy made parallel launch waves mandatory on 2026-08-23 (Beyond the source).

## Key takeaways

- **Laziness grows with context, whatever the model.** Top models do it too; smaller ones just show it sooner [00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s). It's barely visible in a fresh context and grows as the resent history piles up [01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s), [02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s). See [[Context Window Management]].
- **Design against two failure modes.** The first is a false "done": it skims a few of many files and says it read them all [02:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=155s). The second is silent scope shrinkage: it skips the hard part and the summary doesn't mention it [03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s). An honest early stop is fine. A false completion claim costs you because later work builds on it [02:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=166s), [02:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=177s). See [[Agent Laziness]].
- **Ask who judges "done".** Ralph trusts agent-written text [03:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=226s), `/goal` trusts a small model reading the chat [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s), and self-graded lists trust the agent [04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s). All three hold up early and falter deep into real work [04:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=256s). See the table below, [[Verification Before Done]] and [[Loop Engineering]].
- **Put acceptance criteria in files, not instructions.** The earlier version relied on telling the agent to be thorough [07:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=432s), but instructions are the first thing a long session loses [07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s), so the new version writes gates to a file before work begins [07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s). See [[Evidence-Gated Completion Ledger]].
- **A gate is outcome + command + expected words + evidence** [07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s). A checker, not the agent, runs the commands and records the deciding output [07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s). A tick above pending evidence ranks below an empty box [08:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=497s). See [[Build Verification into Every Task]].
- **Give each unit of work a narrow, fresh context.** Leaves get only the plan and their own gates [08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s), and the parent re-checks before moving on [08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s). See [[Subagents and Agent Teams]].
- **Size leaves at ten or more minutes of real work** [06:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=387s). Use depth 2–3 for a feature and 5 for a new app [11:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=683s), [11:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=689s).
- **Fan out in parallel, with file ownership in the plan.** Serial dispatch wasted hours [10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s). Parallel agents with a task-to-file map finished in about two hours [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s), [12:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=726s). See [[Parallel Sessions with Git Worktrees]].
- **Route work by difficulty.** Send mechanical work to a cheaper model and hard parts to a strong one, so big runs hit usage limits later [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s). See [[Route Tasks to the Right Claude Model]] and [[Choosing a Claude Model]].
- **One install can serve two agents.** The skill lives in `.agents` (which Codex reads), and `.claude` holds a shortcut for Claude Code [09:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=568s), [10:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=607s). See [[Tool-Agnostic Context Files]].

## Who judges "done": the video's comparison

This table contains only what the video says. The current docs and repo behaviour are in the matching table under Beyond the source.

| Approach | What ends the work | What the judge sees | The video's objection | When |
|---|---|---|---|---|
| **Ralph loop** | An indicator in the agent's output stops the repeated prompt | Text the agent writes while working | No single word proves a feature was built properly | [03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s), [03:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=226s), [03:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=232s) |
| **Claude Code `/goal`** | A second, smaller model acting as judge | The conversation | It judges what the conversation says, not the work, and can drift from what you needed | [03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s), [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s), [04:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=243s) |
| **AI LABS' task-list loops** | The agent, scoring checks kept in a task list | Real checks, graded by the agent | The agent still decides it's done | [03:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=218s), [04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s) |
| **Unlazy gates** | Every gate ticked by the checker with evidence, or abandoned by name; the parent re-runs leaf checks | Command output matched against expected words, with the deciding output saved | None given; the claim is that the agent never decides | [07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s), [08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s), [09:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=543s) |
| *First three, overall* | — | — | Fine in a fresh context; falter deep in real work, when you need them most | [04:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=256s), [04:20](https://www.youtube.com/watch?v=c47uqR7XB_c&t=260s) |

Reading down the table (the vault's framing), what the judge looks at moves closer to the work itself: a marker word, then the conversation, then real checks the agent grades, then recorded command output. Only the last row takes the verdict away from the agent. The agent still writes the gates, though, so a weak check passes weak work (see Caveats).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=0s) Intro

- **The complaint.** Agents don't own their tasks, so you have to review output you can't trust [00:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=2s), [00:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=6s). They claim the problem "just got solved" [00:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=10s); see Caveats.
- **The author.** He's introduced only as GitHub's number-one trending author and the maker of the popular Taste design skill [00:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=12s), [00:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=16s). His new skill is Unlazy [00:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=22s). The description's repo link identifies him as Leonxlnx ([[Leon Lin]]).
- **The plan for the video.** The workflow is creative but ran very slowly for them, and they found a fix [00:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=27s), [00:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=32s). The video covers what it is, how it works, the problem, and their change [00:41](https://www.youtube.com/watch?v=c47uqR7XB_c&t=41s).

### [00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s) What Unlazy is

- **Laziness is universal.** It hits every model, including Opus and GPT 5.6 [00:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=53s). Small models just expose it sooner because their limits show faster [00:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=56s).
- **Proof, not reports.** The skill doesn't report the agent as done; it proves it [01:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=73s). Work is checked against a ledger, a checklist where each item needs proof of completion [01:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=77s), so you see proof for every part [01:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=82s).
- **Harness support.** It works with [[Claude Code]], [[OpenAI Codex]] and other popular agents [01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s). (A subscribe request is omitted.)

### [01:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=107s) Why agents get lazy

**Mechanism** (see [[Context Window Management]])

- A fresh context holds little, so the model focuses well and laziness can go unnoticed [01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s). It shows more as the context fills [02:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=121s).
- The model remembers nothing between messages [02:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=123s). The agent resends the whole history with each new prompt [02:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=129s).
- As that pile grows, there's more competing for attention [02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s). Focus on each part of the task weakens and the agent slacks [02:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=142s).

**Failure mode 1: "done" when it isn't** [02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s)

- Their example: Claude Code is asked to go through many files, opens a few, and reports that it covered all of them [02:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=155s).
- An early stop with visibly unfinished work is acceptable [02:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=166s). Claiming everything is finished is the costly case: you can't tell until you check [02:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=173s), and building on it causes trouble later [02:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=177s).

**Failure mode 2: quietly shrinking the job** [03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s)

- Their example: a request with five parts, one of them hard. The agent builds the four easy ones, skips the hard one [03:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=185s), and the closing summary never mentions a gap [03:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=193s).

**Why the earlier fixes fall short** (none of this is new [03:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=196s); see the table above)

- **Ralph loop.** It re-sends the same prompt until an indicator in the output says the task is done [03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s). That finish line is only text the agent writes [03:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=226s), and one word can't show a feature is built properly [03:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=232s).
- **`/goal`.** It uses another model as judge [03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s). That smaller model reads the conversation to decide completion [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s), so it judges what was said rather than the work, and can drift [04:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=243s).
- **AI LABS' own loops.** A task list held checks every task had to pass [03:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=218s). The checks were real, but the agent graded them itself, so it still decided when it was done [04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s), [04:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=251s). The video doesn't say which of their videos built these; [[AI LABS - Types of Claude Loops Explained]] covers related loops but shows no task-list setup (vault check).
- **The shared weakness.** All three work in a fresh context and falter deep into real work, which is exactly when they need to hold [04:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=256s), [04:20](https://www.youtube.com/watch?v=c47uqR7XB_c&t=260s).

### [04:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=266s) Sponsor

- Omitted (see Caveats).

### [05:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=326s) The tree

**Decomposition**

- A large task isn't started directly. The skill splits it into smaller tasks, then splits those again, branching like a tree [05:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=331s), [05:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=338s), [05:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=347s).
- When splitting stops, each end task goes to its own subagent [05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s). Per the Modes table below, that holds only for orchestrated runs (see Caveats).
- **Depth.** You pass a number with the prompt, and it sets the tree's depth [05:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=355s). Five means five rounds of breakdown and no more [06:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=362s). The repo counts layers differently; see Caveats. With no number, the skill picks the smallest depth that fits [06:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=368s).
- **Why split.** It's the attention problem again [06:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=372s): a leaf has a single goal, and whoever works it isn't holding the whole job in mind [06:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=378s).
- **Minimum leaf size.** A leaf has to be a proper piece an agent can finish alone, worth at least ten minutes of real work [06:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=387s), [06:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=391s).
- **Depth set too high.** If leaves come out smaller than that, the video says the skill falls back to the default depth of three [06:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=399s), [06:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=403s). The repo differs; see Caveats.

**Modes**

| Mode | Depth | Behaviour | When |
|---|---|---|---|
| **Solo** (default) | 3 or less | One session; the same agent works through everything | [06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s), [06:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=412s) |
| **Orchestrated** | 4 or more | Writes much more down: a plan file with the full breakdown, plus a checklist per task | [06:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=416s), [07:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=420s) |

**Why a file**

- The previous version relied on an instruction to work thoroughly [07:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=432s). But in a long session instructions are the first thing lost, which is the problem it was meant to solve [07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s).
- So this version writes the requirements into a file before work starts [07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s). Compare [[Keep CLAUDE.md Lean]] on what belongs in always-loaded instructions.

**The gates file (the ledger)**

- Each item is a gate: a checkbox next to one outcome that must be true before the task counts as done [07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s), [07:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=452s).
- Three lines sit under each outcome [07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s):
  1. The command that proves it [07:41](https://www.youtube.com/watch?v=c47uqR7XB_c&t=461s).
  2. The exact words that command must return [07:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=465s).
  3. An evidence line that starts as "pending" [07:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=467s).

**The checker**

- The bundled checker walks the file and runs every command itself [07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s), [07:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=475s).
- When the output contains the expected words, it ticks the box and swaps "pending" for the deciding piece of output [07:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=479s), [08:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=481s).

**The pending rule**

- The evidence line closes the hole in all the earlier fixes [08:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=486s).
- A tick with "pending" still underneath means the agent ticked it by hand, which is just another claim of done [08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s). It counts as unmet [08:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=497s).
- The skill ranks it below an empty box, because an empty box at least honestly shows where the work stands [08:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=499s), [08:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=501s).

**Orchestrated runs**

- Each task goes to a fresh agent that gets only the plan and its own gates file [08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s), [08:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=511s).
- When it reports back, the main agent doesn't take its word: it runs that task's checks itself [08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s). Only then does it log a line in the plan and hand out the next task [08:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=522s). This "next task" step is what their fix changes.

**The honest exit**

- If a task proves impossible [08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s), the agent doesn't drop it silently. It writes a line giving up that gate by name, with a reason [08:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=533s), and the line appears in the final report [08:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=537s).

**The claim.** It's a whole system rather than one final check, and at no point does the agent decide the work is done [08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s), [09:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=543s). See [[Evidence-Gated Completion Ledger]].

### [09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s) Install

1. **Copy the command.** Get it from the install section of the official GitHub page; the link is in the description [09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s), [09:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=552s).
2. **Run it** in a terminal inside your project [09:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=557s).
3. **Choose agents** [09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s):
   - Codex needs no change, because the skill installs into the `.agents` folder Codex already reads [09:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=568s).
   - For Claude Code, select it from the menu [09:34](https://www.youtube.com/watch?v=c47uqR7XB_c&t=574s).
   - You can pick several agents at once [09:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=576s).
4. **Choose a scope:** this project only, or everything you build [09:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=580s). They picked project scope to test on one project first [09:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=589s).
5. **Accept the recommended options** [09:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=595s).

After installing:

- **Two new folders.** VS Code shows `.agents` and `.claude` [09:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=598s). They aren't two copies [10:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=603s): the skill lives in `.agents`, and `.claude` holds a shortcut so Claude Code can use it without a duplicate [10:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=607s), [10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s). Beyond the source covers a known bug where the shortcut isn't created.
- **The skill file** inside that folder holds all the agent's usage guidance [10:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=616s).
- See [[Tool-Agnostic Context Files]] and [[Build vs Install Third-Party Skills]].

### [10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s) The fix

**The problem**

- Run as shipped, the skill takes a very long time to build anything meaningful [10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s).
- Their test app session ran for about 3–4 hours and produced only a login page [10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s), [10:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=640s).

**The cause** (found in the skill's instructions [10:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=644s))

- Claude Code and Codex can both run several subagents in parallel [10:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=645s), [10:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=652s).
- The skill instead handed out one task, waited for it to finish, then handed out the next [10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s). It wasn't using the agents' capabilities, and that's where the hours went [10:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=659s), [11:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=663s).

**Their change**

- They edited the skill itself [11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s), using a prompt shown on screen for viewers to copy [11:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=668s). It isn't in the captions; a vault-written equivalent is under Build from this.
- The edit makes the skill take advantage of running several agents at once [11:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=672s).

**Running it**

- **Syntax:** skill name, then depth, then everything you want built [11:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=678s).
- **Depth:** they used 5 for an app built from scratch [11:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=683s). For a single feature, 2 or 3 is enough [11:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=689s). A number that's too high gets lowered automatically, so you can't really pick wrong [11:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=695s).
- **Order of operations:**
  1. It writes PLAN.md, then GATES.md, before building anything [11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s), [11:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=703s).
  2. PLAN.md records which files each task touches, so simultaneous agents don't overwrite each other [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s), [11:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=711s).
  3. It lays the foundation first, then hands work out to agents running at the same time [11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s).

**The result**

- 10 agents worked at once on different parts [12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s), for nearly two hours [12:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=726s).
- The output was a first version of the demo app with every feature working as intended [12:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=728s).

**Scaling tip**

- At this scale, add a model router skill that sends each task to the right model [12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s).
- Mechanical work goes to a cheaper model and hard parts to a strong one, so you hit limits later [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s).
- No router is named. See [[Route Tasks to the Right Claude Model]].

**Paywall**

- Their tested and refined version is sold in their paid community [12:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=748s), [12:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=752s). The pitch is omitted.

## Caveats & disagreements

**About the video**

- **Hype.**
  - "Insane" and "just got solved" [00:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=10s) oversell it. Unlazy is discipline plus tooling.
  - Even its pre-video SKILL.md is more modest: a six-run test found that instructions alone raised effort but still missed some failures.
- **Unverified ranking.**
  - The "number-one trending author" claim [00:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=12s) comes with no name or evidence, and the ranking is unverified.
  - The identity is verified: Leonxlnx is Leon Lin.
- **Sponsor.** A DataForSEO sponsor read (04:26–05:24) is omitted as unrelated to Claude.
- **The fix can't be rebuilt from the captions.**
  - The editing prompt is shown only on screen [11:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=668s), and the refined skill is paywalled [12:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=752s).
  - Upstream now enforces parallel launch waves, so neither is needed for the core fix.
- **Anecdotal results.**
  - One slow run and one fast run. No spec, token or cost figures, and no ledger shown.
  - "All features working" [12:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=728s) is asserted, not demonstrated.
- **Depth fallback misdescribed.**
  - *Video:* a too-high depth drops to the default of three [06:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=399s).
  - *Repo at the video date:* back off one layer.
  - *Current repo:* state the mismatch and use the closest honest decomposition.
- **Depth counting is loose.**
  - *Video:* depth five means five rounds of breakdown [06:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=362s).
  - *Repo at the video date:* layer 1 is the task itself, so tree 5 means five layers counting the root.
- **Subagent wording contradicts the modes.** *Video:* every end task goes to its own subagent [05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s). *Same video:* at depth 3 or less, the default, everything stays in one session with the same agent [06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s), [06:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=412s); only orchestrated runs hand tasks to fresh agents [08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s). *Repo at the video date:* matches the mode split.
- **Gates are only as good as their checks.**
  - *Video:* the agent never decides it's done [09:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=543s).
  - *Vault reading:* the agent or planner still writes the CHECK and EXPECT lines, so a weak check passes weak work.
  - *Current README:* evidence binding catches a changed gate definition, not a deliberately faked ledger (Beyond the source).
- **"One at a time" was the default, not a limit.**
  - *Video:* the skill waits after each task [10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s). This matches the pre-video orchestration loop (dispatch, verify, log, dispatch next).
  - *Repo at the time:* its Parallelism section already allowed leaves that own separate files to run concurrently where the harness supports it.
  - *Since 2026-08-23:* upstream requires native parallel waves.
- **The checker has changed and needs care.**
  - *Video:* the checker simply runs every command [07:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=475s).
  - *Current Unlazy:* previews commands, needs `--approve` to execute them, and binds evidence to a digest of the gate definition.
  - *Safety:* CHECK lines are shell commands running with your full environment, and gate files you didn't write are untrusted. The video doesn't say so. See [[Permissions and Approval Gates]].
- **Hook left out.** The optional Claude Code Stop hook, arguably Unlazy's strongest enforcement, isn't mentioned.
- **`/goal` critique is fair but incomplete.** The docs confirm the evaluator reads only the conversation [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s). They also advise naming a proving command so real output lands in the transcript, which narrows the gap.
- **Ralph is simplified.** Anthropic's plugin stops on an exact completion-promise phrase and recommends an iteration cap. The objection [03:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=226s) still stands.
- **Install bug not mentioned.** There's an open installer bug where a project-scope Claude Code install creates `.agents/skills` but no `.claude/skills` link. Claude Code's documented skill folders don't include `.agents`, so check the shortcut [10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s).
- **Leaf brief simplified.** Subagents get "the plan" [08:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=511s). The pre-video reference sends only the plan's contract section plus the leaf's gates file.
- **Unchecked.** "No inbuilt memory" [02:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=123s) holds at the model level; harness memory doesn't restore focus within a session (vault reading, not checked against docs). "GPT 5.6" [00:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=53s) is recorded as said.

**Conflicts with existing vault notes (both sides kept)**

- **[[AI LABS - Types of Claude Loops Explained]]** (same channel).
  - *That video:* `/goal`'s Haiku judge double-checks the work against your requirements ([02:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=149s), [02:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=153s)). The loop works best when requirements can be checked concretely, for example with tests written first ([02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s), [02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s)).
  - *This one:* `/goal` judges the chat, not the work [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s).
  - *Docs:* side with this video on what the judge sees; the evaluator runs no tools and judges only what reaches the conversation (Beyond the source).
  - *Reconciled:* tests put real output in the transcript, and Unlazy goes further by letting a script decide. See [[Tests-First Goal Loop]].
- **[[Tool-Agnostic Context Files]].**
  - *That note:* shares instruction files across harnesses.
  - *This video:* extends the one-copy idea to skills (`.agents` plus a `.claude` shortcut) [10:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=607s).
  - *Add:* the installer symlink bug. See [[Port a Claude Code Brain to Other Agents]].
- **[[CLAUDE.md as a Router]].**
  - *That note:* relies on always-loaded instructions for routing.
  - *This video:* instructions fade in long sessions [07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s).
  - *Reconciled:* keep routing in CLAUDE.md; put completion criteria in checkable files.
- **[[Claude Code Auto Memory]].**
  - *That note:* memory persists across sessions.
  - *This video:* growing in-session history dilutes attention [02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s).
  - *Reconciled:* memory files don't fix that; fresh subagent contexts do [08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s).
- **[[Grill Me Interview Skill]].** It records a caution that more context can hurt. This video supplies the mechanism [02:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=142s).
- **[[Claude Code]].** Extension rather than conflict. This video adds parallel subagents [10:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=645s) and a `/goal` critique [03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s).

**Other sources in this batch**

- **Self-grading.**
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] rates verification top tier ([08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s)).
  - He warns that tests written after the code just pass Claude's own code ([09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)). That's the same hole as [04:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=251s).
- **Context rot: agreed.**
  - He describes a "dumb zone" that deepens as context grows ([13:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=792s)).
  - [[Ras Mic - How AI Agents and Claude Skills Work]] says the model gets dumber as the window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)).
  - See [[Context Hygiene Routine]].
- **Parallel cost: pushback.**
  - The Coding Sloth says each subagent is a full parallel conversation that can exhaust a $20 plan ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)).
  - Ten agents for two hours [12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s) assumes a big plan, which makes the router tip matter.
- **Scale gradually.**
  - Ras Mic warns against starting with many subagents ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)) and says to begin with one agent ([15:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=927s)).
  - Unlazy's solo default [06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s) fits that advice.
- **Installing others' skills: disagreement.**
  - Ras Mic reviews others' skills rather than installing them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)), and calls downloads an easy attack route ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)).
  - This video installs straight from the repo [09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s).
  - See [[Build vs Install Third-Party Skills]].
- **Lighter checks.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] adds screenshot and DevTools to-dos ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)) and a 95%-confidence rule ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)). By this video's standard that's still self-grading.
- **Separate grader.** [[Anthropic - What Is Claude Managed Agents]] uses a grader in its own context window against rubric criteria ([01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s)). It's a model grader; Unlazy uses commands.
- **Model routing: supported.**
  - Nate Herk runs subagents on Haiku with Opus as the main thread ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)).
  - [[Knowing More - Every Claude Model Explained]] suggests Haiku for quick, batch and repetitive work ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)).
- **Isolation.**
  - The Coding Sloth gives each chat its own worktree ([20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s)).
  - Unlazy assigns file ownership inside one checkout [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s).
  - See [[Parallel Sessions with Git Worktrees]].

## Build from this

Parts from the video carry timestamps. *Vault* content is original starter material, not shown in the video; the facts it relies on are verified under Beyond the source.

### 1. Install Unlazy safely for Claude Code and Codex

- *Video:* install flow [09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s)–[10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s); run as skill name, depth, spec [11:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=678s).
- *Vault steps:*
  1. Read `SKILL.md`, `scripts/` and `SECURITY.md` before installing.
  2. Install at project scope for both agents.
  3. Confirm `.claude/skills/unlazy` resolves to `.agents/skills/unlazy`, and create the symlink if it's missing.
  4. Start at depth 2–3 on one feature.
  5. Read `GATES.md` before approving any CHECK.
- See [[Build vs Install Third-Party Skills]], [[Tool-Agnostic Context Files]], [[Configure Safe Autonomy Permissions]].

### 2. A gates ledger for any task

- *Video:* gates before work [07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s); four-part gates [07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s); checker-written evidence [08:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=481s); abandon with a reason [08:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=533s).
- *Vault starter* `GATES.md`. The field layout matches Unlazy at the video date; the task is invented:

```markdown
# Gates: password reset flow

- [ ] G1: reset-token unit tests pass
  CHECK: npm test -- tests/reset-token.test.ts
  EXPECT: /\d+ passed/
  EVIDENCE: pending

- [ ] G2: an expired token is refused by the API
  CHECK: node scripts/probe-expired-token.mjs
  EXPECT: status=410
  EVIDENCE: pending

- [ ] G3: reset email readable at 375px width (manual: give screenshot path)
  EVIDENCE: pending
```

- *Vault rule:* write each outcome so a stranger could judge it, and turn anything you keep re-checking by reading into a CHECK.
- See [[Evidence-Gated Completion Ledger]], [[Build Verification into Every Task]].

### 3. A parallel orchestrated build with file ownership

- *Video:* plan, then gates [11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s); task-to-file map [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s); foundation first, then concurrent agents [11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s); parent re-checks [08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s).
- *Vault:* update Unlazy first, since upstream already enforces waves. For an older copy, or your own orchestrator, use this starter `PLAN.md` section (column names and Tier values follow current upstream; the leaves are invented):

```markdown
## Dispatch
| Leaf | Owns | Needs | Tier | Planned wave | State |
|---|---|---|---|---|---|
| L1 schema and shared types | src/types/, db/schema/ | none | judgment | 0 | READY |
| L2 auth API | src/api/auth/ | L1 | judgment | 1 | PLANNED |
| L3 settings screen | src/app/settings/ | L1 | mechanical | 1 | PLANNED |
| L4 seed data | scripts/seed/ | L1 | mechanical | 1 | PLANNED |
```

- *Vault patch prompt* (not the on-screen one):

```text
Edit .agents/skills/unlazy so orchestrated mode dispatches in waves: every leaf whose
dependencies are verified and whose Owns paths don't overlap any running leaf. Launch
the whole wave before waiting on any result. Keep per-leaf gates and parent
re-verification unchanged. Refuse to dispatch two leaves owning the same path, and
schedule shared foundations as wave 0. Show me the diff before saving.
```

- See [[Subagents and Agent Teams]], [[Parallel Sessions with Git Worktrees]], [[Multi-Agent Review and Scoring Loops]].

### 4. `/goal` that reads evidence, not claims

- *Video:* the judge reads the conversation [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s).
- *Vault condition:*

```text
/goal every gate in GATES.md is met: the latest Unlazy checker run with --reverify is
printed in the transcript and shows no unmet, pending or abandoned gates, and no test
file was modified; or stop after 25 turns
```

- See [[Tests-First Goal Loop]], [[Loop Engineering]].

### 5. Model-tiered leaves plus a laziness spot-check

- *Video:* router tip [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s); the two failure modes [02:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=155s), [03:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=185s).
- *Vault starter subagent* `.claude/agents/mechanical-leaf.md`. Keep design, integration and verification on the strong model:

```markdown
---
name: mechanical-leaf
description: Works one mechanical Unlazy leaf (renames, fixtures, applying a decided pattern). Use only for leaves whose Tier is mechanical.
model: haiku
tools: Read, Edit, Write, Grep, Glob, Bash
---
Your brief is the PLAN.md contract plus your gates file. Edit only your Owns paths.
Run the gate checker before reporting; never hand-tick a runnable gate. If a gate is
impossible, add an ABANDON line with its id and reason, then stop.
```

- *Vault spot-check prompt*, to use before accepting any summary:

```text
Before summarising: list each file or item I named and how many you actually opened,
counted from your tool calls; map every requirement in my message to a file and line,
or mark it "not done"; re-measure any number you are about to state.
```

- See [[Route Tasks to the Right Claude Model]], [[Agent Laziness]], [[Context Hygiene Routine]].

## Resources mentioned

- **Unlazy repo:** github.com/Leonxlnx/unlazy. The description links it, and the video points to its install section [09:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=550s).
- **Taste design skill** by the same author [00:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=18s). The repo is github.com/Leonxlnx/taste-skill.
- **Ralph loop** [03:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=205s) and **Claude Code `/goal`** [03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s).
- **AI LABS' task-list loops** [03:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=218s). Not identified; [[AI LABS - Types of Claude Loops Explained]] covers related loops but shows no task-list setup (vault check).
- **VS Code** [09:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=598s).
- **An unnamed "model router skill"** [12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s).
- **Their refined variant:** the prompt is shown on screen only [11:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=668s), and the skill is paywalled [12:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=752s).

## Beyond the source

*Not in the video. Verified on 2026-09-15 at the links given.*

**Who judges "done", per current docs and repo**

| Approach | How it actually decides | Source |
|---|---|---|
| Ralph Wiggum plugin | A Stop hook blocks exit and feeds the same prompt back until Claude outputs the exact `--completion-promise` phrase; `--max-iterations` is the safety cap. Credited to Geoffrey Huntley | https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md |
| `/goal` | A session-scoped, prompt-based Stop hook. After each turn the small fast model (Haiku by default) reads the condition and conversation with no tools, and returns not met, met, or impossible. The docs advise a measurable end state, a stated proving command, constraints and a turn cap. Evaluation waits while subagents run | https://code.claude.com/docs/en/goal |
| Unlazy checker (current) | Needs exit 0 *and* an EXPECT match. Evidence is fingerprinted against a SHA-256 digest of the gate. `--status` doesn't execute; `--approve` runs; parents use `--reverify`. ABANDON exits as a handoff, not a success | https://github.com/Leonxlnx/unlazy · https://github.com/Leonxlnx/unlazy/blob/main/CHANGELOG.md |
| Stop hooks | Claude Code overrides a hook that blocks eight times in a row without progress (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises the cap). Unlazy's optional hook releases after six no-progress blocks | https://code.claude.com/docs/en/hooks-guide · https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md |

**Author and repo**

- Leonxlnx's GitHub profile name is Leon Lin: https://github.com/Leonxlnx
- Taste Skill had about 87k stars when checked: https://github.com/Leonxlnx/taste-skill
- Unlazy is MIT-licensed, created 2026-08-09, about 3.4k stars: https://github.com/Leonxlnx/unlazy

**Unlazy at the video date** (commit 40570e1, 2026-08-16, metadata v2.1.0): https://github.com/Leonxlnx/unlazy/blob/40570e1/SKILL.md

- **Leaf size and too-deep trees.** Layer 1 is the task itself. Leaves take ten or more minutes and deliver one coherent result. If leaves come out smaller, back off one layer.
- **Mode thresholds.** Solo means roughly under half an hour and depth 3 or less. Orchestrated means depth 4 or more, with `PLAN.md` plus `gates/` per leaf.
- **Scale guidance.** Depth 2–3 for a feature, 4–5 for a subsystem, 6–7 for a whole project.
- **Why v2 exists.** v1 relied on instructions; a controlled six-run test showed they raised effort but missed wrong self-reported numbers and stalls.
- **Report audit.** Re-measure every number and paste the ledger as N of N.
- **Untrusted gates.** Inherited gate files are untrusted.
- **Ledger rules.** Pending evidence is unmet; the abandon syntax is `ABANDON: <gate id> <reason>`. Gate template: https://github.com/Leonxlnx/unlazy/blob/40570e1/templates/gates-leaf.md

**The pre-video orchestration reference**: https://github.com/Leonxlnx/unlazy/blob/40570e1/references/orchestration.md

- **Serial loop.** Dispatch one leaf with the contract section and its gates, re-verify with `--reverify`, log, dispatch the next.
- **Parallelism was allowed.** A Parallelism section permitted concurrent leaves with separate file ownership where supported. It noted that this saves wall-clock time, not tokens.
- **Model tiering was built in.** Mechanical leaves could use a cheaper model or lower effort. Design, integration, verification and the driver stay on the strong model. That's essentially the video's router tip.

**Upstream changes after the video**

- Commits on 2026-08-23 include "require native parallel launch waves" (be703c5) and "enforce dispatch launch barriers" (b02276e): https://github.com/Leonxlnx/unlazy/commits/main
- The dispatch reference now requires recording every launch in a wave before the first wait. It refuses the serial pattern: https://github.com/Leonxlnx/unlazy/blob/main/references/dispatch.md
- Current SKILL.md adds:
  - scoped pipelines in `.unlazy/<scope>/`
  - a PLAN dispatch table with Owns, Needs, Tier, Planned wave and State
  - `dispatch.json`
  - `OWNS:` leases claimed with `--claim`, described as coordination, not isolation
  - a per-leaf `Tier` of `judgment` or `mechanical`, described as planner metadata rather than a routing guarantee; map it to a model only through controls the host actually has

  Source: https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md
- For over-deep trees, the current method says to state the mismatch and use the closest honest decomposition: https://github.com/Leonxlnx/unlazy/blob/main/references/method.md

**Security, install and Claude Code**

- **Approval isn't sandboxing.** The README warns that approving a check is consent, not a sandbox: checks get your environment, credentials and network. Approvals are stored under `~/.unlazy/approved`, outside the repo.
- **Evidence isn't tamper-proof.** The README says the definition digest detects structural drift in a gate, but someone with write access to a ledger could fake evidence in the expected format. SECURITY.md says to run `--status` and read every CHECK, EXPECT and CWD before `--approve`: https://github.com/Leonxlnx/unlazy/blob/main/SECURITY.md
- **Commands.** Install with `npx skills add Leonxlnx/unlazy`. Claude Code uses `/unlazy tree 5 <task>`, Codex uses `$unlazy`, and the optional hook installs with `node <skill-dir>/scripts/install-hooks.mjs`. Source: https://github.com/Leonxlnx/unlazy
- **Installer bug.** vercel-labs/skills #1355 (open when checked) reports that a project-scope `-a claude-code` install writes `.agents/skills` without the `.claude/skills` symlink: https://github.com/vercel-labs/skills/issues/1355
- **Where Claude Code finds skills.** Personal, project, nested, `--add-dir` and enterprise locations (each a `.claude/skills` folder), plus a plugin's own `skills/` folder. A skill entry can be a symlink, and a target reached from several locations loads once. `.agents` isn't a listed location: https://code.claude.com/docs/en/skills
- **Subagents.** Each has its own context window. Spawning fails once 20 are running unless you raise `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`. `model` accepts `haiku`, `sonnet`, `opus`, `fable`, an ID or `inherit`, and `isolation: worktree` is available: https://code.claude.com/docs/en/sub-agents
- **Models.** The current lineup is Fable 5.1, Opus 5, Sonnet 5 and Haiku 4.5. Haiku is fastest and cheapest ($1/$5 per MTok vs $5/$25 for Opus 5). Opus 4.7 and 4.8 are legacy: https://platform.claude.com/docs/en/about-claude/models/overview

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Claude's gold command" (03:35) | Claude Code's `/goal` |
| "Code X" (09:27) · "Cloud Code" (09:34) | Codex · Claude Code |
| "{dot} agents", "{dot} Claude" | `.agents` and `.claude` folders |
| "plan.md … gates.md" (11:43) | `PLAN.md`, `GATES.md` |
| "design taste skill" (00:18) | Taste Skill, Leonxlnx/taste-skill (likely) |
| "a a of tasks" (03:49) | "a lot of tasks" |
| "goes straight back attention problem" (06:14) | "back to the attention problem" |
| "lowers the split task to the default number" (06:39) | lowers the tree depth to three (as claimed; see Caveats) |
| "runs that task's checks against itself" (08:40) | the main agent runs that task's checks itself |
| "Ralph loop" | Ralph Wiggum loop |
| "Data for SEO" (04:28) | DataForSEO (sponsor, omitted) |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Agent Laziness]] · [[Verification Before Done]] · [[Context Window Management]] · [[Loop Engineering]] · [[Subagents and Agent Teams]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Choosing a Claude Model]] · [[Tool-Agnostic Context Files]] · [[Permissions and Approval Gates]] · [[CLAUDE.md as a Router]] · [[Claude Code Auto Memory]]
- **Techniques:** [[Evidence-Gated Completion Ledger]] · [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Multi-Agent Review and Scoring Loops]] · [[Parallel Sessions with Git Worktrees]] · [[Route Tasks to the Right Claude Model]] · [[Context Hygiene Routine]] · [[Port a Claude Code Brain to Other Agents]] · [[Configure Safe Autonomy Permissions]] · [[Keep CLAUDE.md Lean]]
- **Tools:** [[Unlazy]] · [[Claude Code]] · [[OpenAI Codex]] · [[Hermes Agent]] (another skills-reading harness in the vault; not named here)
- **Sources in this batch:** [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[Anthropic - What Is Claude Managed Agents]] · [[Knowing More - Every Claude Model Explained]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Simon Pittman - Set Up Claude Cowork]]
- **People:** [[Leon Lin]] · [[AI LABS]] · [[The Coding Sloth]] · [[Ras Mic]] · [[Greg Isenberg]] · [[Nate Herk]] · [[Chase AI]] · [[Jay E]] · [[Simon Pittman]]
