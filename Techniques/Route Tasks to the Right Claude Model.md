---
type: technique
goal: "Send each kind of task to the cheapest Claude model tier that does it well, with written triggers for moving up, and keep every model name in one file you can update when models change"
difficulty: intermediate
time_to_build: "About 30 minutes to write the routing file, subagents and settings; about a week of normal use to tune the triggers (vault estimate)"
sources: ["[[Knowing More - Every Claude Model Explained]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]"]
tools: ["[[Claude Code]]", "[[Claude Cowork]]"]
tags: [topic/models, topic/claude-code, topic/cowork, topic/subagents, topic/skills, topic/context]
---

# Route Tasks to the Right Claude Model

> **Provenance.** Points with a timestamp link come from the six source videos. None of them shows a routing file, a subagent definition or a settings snippet. [[Knowing More - Every Claude Model Explained]] doesn't even show how to switch models. The routing table layout, files, prompts and checklists below are **vault starter content** written for this note. Every command, flag and setting was checked against current docs on 2026-09-15 (see **Beyond the source**). For the ideas behind this and where the sources disagree, see [[Choosing a Claude Model]].

## Goal

Write down which model tier each kind of work goes to, and what should make you move up a tier. Then wire that into [[Claude Code]]: a session default, cheap subagents, a planning model and headless runs. Carry the same rule into [[Claude Cowork]]. Model names live in **one** file, so a new release means changing one line instead of hunting through prompts.

## Use when

- **You keep hitting usage limits.** The Coding Sloth can hit his $20 plan's limit within a prompt or two ([[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s)–[00:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=25s)). Knowing More warns that Opus can hit a rate limit within a few prompts ([[Knowing More - Every Claude Model Explained]] [04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s)–[04:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=262s)).
- **Expensive models are doing bulk reading.** A flagship shouldn't read hundreds of thousands of tokens to pull out a few facts ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=383s)).
- **You plan big changes and want a cheaper model to carry them out** ([[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s)–[07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s)).
- **You run large orchestrated jobs with many subagents.** AI LABS suggest adding a router that sends mechanical tasks to a cheap model and hard ones to a strong model ([[AI LABS - The Unlazy Skill for Lazy Agents]] [12:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=733s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s)).
- **You use Cowork and want a habit for when to pick Opus over Sonnet** ([[Simon Pittman - Set Up Claude Cowork]] [04:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=295s)–[05:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=301s)).

**Don't expect routing to fix a confused agent.** A strong model can still skip obvious steps. Ras Mic's example happened on Opus, and his fix was a skill, not a bigger model ([[Ras Mic - How AI Agents and Claude Skills Work]] [09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s)). Context and harness decide much of the quality ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s), [27:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1647s)).

## Prerequisites

- **[[Claude Code]]** installed, in a project folder. For Fable 5.1 you need version 2.1.255 or later (Beyond the source).
- **A plan that includes the tiers you want to route to.**
  - Fable costs usage credits on Pro, which is why the Coding Sloth dropped it for planning ([07:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=473s)–[08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)).
  - Max and Premium seats include some Fable use (Beyond the source).
- **For the Cowork steps:** the Claude desktop app with Cowork set up. See [[Set Up Claude Cowork]].
- **A way to see what you're spending**, e.g. a status line showing the model and cost. Nate sets one up with `/statusline` ([00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)–[01:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=61s)).

## The decision table

This is the rule, built from the sources. It uses **tiers**, not versions: *small* is Haiku, *balanced* is Sonnet, *flagship* is Opus and *frontier* is Fable. Which version each tier currently means is recorded once, in Starter file A.

| Task type | Start on | Move up when… | Basis |
|---|---|---|---|
| Quick answers, summaries, pulling facts from documents, batch or repetitive jobs | Small | The output misses nuance, or the job turns out to need judgement | Knowing More [01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s), [01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s), [06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s) |
| Subagent that reads a large volume (scraping, searching docs or a codebase) and returns a summary | Small (the subagent) | The summaries leave out facts the main thread needs | Nate [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s) |
| Everyday coding, writing, analysis, operations work | Balanced | Balanced keeps struggling on the task | Knowing More [02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s), [04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s), [06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s) |
| Planning a big, multi-file change | Flagship, or frontier if your plan includes it | *(You're already at the top of your plan)* | Coding Sloth [07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s), [08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s) |
| Carrying out an approved plan | Balanced | A step fails twice and its checks don't show why *(vault trigger)* | Coding Sloth [07:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=459s), [08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s) |
| Leaf tasks in a large orchestrated run | Small or balanced for mechanical leaves, flagship for hard ones | A leaf fails its gate check *(vault trigger)* | AI LABS [12:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=739s)–[12:25](https://www.youtube.com/watch?v=c47uqR7XB_c&t=745s) |
| Architecture decisions, complex debugging, big refactors | Flagship, with deeper thinking | A couple of prompts still haven't produced the right answer | Nate [13:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=814s)–[13:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=824s), [13:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=837s) |
| Hard engineering, financial modelling, decisions that are hard to reverse | Flagship | *(Start here)* | Knowing More [02:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=173s), [07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s) |
| Cowork: quick documents and answers | Balanced, thinking on | The task becomes an ambitious, multi-step project | Simon [04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s), [04:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=297s), [33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s) |
| Cowork: restructuring folders or systems, ambitious projects | Flagship | *(Start here)* | Simon [04:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=299s), [35:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=2138s) |
| The agent skips steps, drifts, or says it's done when it isn't | **Don't move up yet.** Clear or split the context, add a check, or write a skill | It still fails with a clean context and a clear procedure | Ras Mic [09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s), [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s); AI LABS [00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s) |

*Vault reading of "struggling":* none of the videos defines it. This note uses concrete triggers:
- the same check fails twice;
- the model contradicts its own plan;
- the task is flagged as hard to reverse.

## Steps

1. **List your recurring task types.** Look through a week of sessions and write down the jobs you actually run: triage, summaries, feature work, reviews, migrations. Put each into a row of the decision table. *(Vault step.)*
2. **Create the routing file.** Copy **Starter file A** to `.claude/model-routing.md`. The file uses tiers throughout, and the one "Registry" block at the top maps each tier to a Claude Code alias and a pinned ID. This is the only place a model name appears.
3. **Point CLAUDE.md at it in one line.** Add **Starter snippet B**. Don't paste the table into CLAUDE.md. Everything in that file sits in context on every turn ([[Ras Mic - How AI Agents and Claude Skills Work]] [04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)). See [[Keep CLAUDE.md Lean]].
4. **Set the session default.**
   - Put `"model": "sonnet"` (or your chosen default) in `.claude/settings.json`, as in **Starter file C**.
   - Switch mid-session with `/model opus`, or `/model` alone for the picker.
   - Set one session at launch with `claude --model opus`.

   The priority order for these is under Beyond the source.
5. **Move bulk reading onto a small-tier subagent.** Create **Starter file D** (`.claude/agents/bulk-reader.md`, with `model: haiku`). Nate's pattern: the subagent reads a lot, and the main thread gets a short summary ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)–[05:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=326s), [06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=377s)).
   - To route Claude Code's own codebase searches to Haiku as well, add **Starter file E**. It overrides the built-in `Explore` subagent, which now inherits your main model (Beyond the source).
6. **Split planning from building.** Pick one of these for any big change:
   - **Option 1, one session:** `/model opusplan`. Claude Code uses Opus in plan mode and switches to Sonnet once you approve the plan.
   - **Option 2, two sessions:** plan with `claude --model opus` and save the plan file. Then build in a fresh session with `claude --model sonnet` and **Prompt F**.

   This is the Coding Sloth's split ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)–[08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s)). For the full plan workflow see [[Plan-First Workflow]].
7. **Give the implementer its own subagent (optional).** Create **Starter file G** (`model: sonnet`) so the main flagship thread can delegate approved steps to it.
8. **Write escalation down as a skill.** Add **Starter file H** (`.claude/skills/escalate/SKILL.md`, with `model: opus` and `effort: xhigh`). Use `xhigh` rather than `high`: `high` is already the default, and Starter file C sets it too, so it would add nothing.
   - Run `/escalate` when a trigger in the decision table fires. The stronger model and effort apply only for that turn, then the session returns to its default.
   - This turns Knowing More's "move up to Opus when Sonnet struggles" ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)) into a repeatable action.
   - For one deeper turn without changing model, put `ultrathink` in your prompt instead, matching Nate's "after a couple of tries" trigger ([13:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=837s)–[14:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=840s)).
9. **Route headless and scheduled runs explicitly.** A script shouldn't depend on whatever model the account defaults to. Pass `--model` in every `claude -p` call, as in **Starter script I**.
10. **Route inside big orchestrated runs.** In a subagent-heavy job such as [[Unlazy]]'s orchestrated mode, give each worker type a `model:` in its definition. Tell the orchestrator to follow the routing file when it hands out leaf tasks (**Prompt J**). This is the router AI LABS recommend ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s)).
11. **Apply the same rule in Cowork.**
    - **Pick the model per task** in the model menu at the prompt, as Simon does ([04:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=270s)–[04:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=273s)). Use Sonnet with thinking on for quick documents ([33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s)) and Opus for structural work ([35:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=2138s)).
    - **Add Snippet K** to your Cowork global instructions. Simon keeps a separate set of instructions for Cowork, under Settings, then the Cowork tab, then Global instructions ([08:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=521s)–[08:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=531s)). Claude will then tell you *before starting* when a task looks like it needs a different tier, and you make the switch.
    - **Set a model on scheduled tasks** using the task's optional model field (Beyond the source). See [[Schedule Recurring Claude Tasks]].
12. **Measure for a week, then adjust.**
    - Keep the model and cost visible in the status line (Nate [00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)). **Starter file C** includes a status line command.
    - Check `/usage` at the end of each day.
    - Record every escalation in the log section of the routing file.
    - If one task type escalates most of the time, change its starting tier. If a flagship task always succeeds on the first try, try one tier down.
13. **When a new model ships, edit only the Registry block.** Update the aliases and pinned IDs, change the "Last checked" date, and re-run one sample task per tier. Nothing else should need editing. If it does, a model name has leaked outside the registry. Grep for it (Pitfalls).

## Starter files & prompts

*All vault starter content, written for this note. Model aliases, fields and flags were checked against current docs. See Beyond the source.*

### A. `.claude/model-routing.md`

```markdown
# Model routing

## Registry (the ONLY place model names appear)
Last checked: 2026-09-15 against platform.claude.com/docs/en/about-claude/models/overview

| Tier      | Claude Code alias | Pinned ID (scripts, API)    | Notes                                      |
|-----------|-------------------|-----------------------------|--------------------------------------------|
| small     | haiku             | claude-haiku-4-5-20251001   | Retirement not before 2026-10-15: recheck  |
| balanced  | sonnet            | claude-sonnet-5             | Session default                            |
| flagship  | opus              | claude-opus-5               | Planning, hard or irreversible work        |
| frontier  | fable             | claude-fable-5-1            | Only if the plan includes it (credits on Pro) |

## Routing rules (tiers only, no model names below this line)
- Bulk reading, summaries, extraction, batch jobs -> small (bulk-reader subagent)
- Everyday coding, writing, analysis -> balanced
- Planning a multi-file change -> flagship (or opusplan)
- Implementing an approved plan -> balanced (implementer subagent)
- Architecture, hard debugging, irreversible decisions -> flagship, effort xhigh (/escalate)
- Mechanical leaf tasks in orchestrated runs -> small or balanced; hard leaves -> flagship

## Escalation triggers
1. The same check fails twice on the current tier.
2. The model contradicts the approved plan or its own earlier finding.
3. The task is marked irreversible (data deletion, migrations, money, public releases).
Before escalating: is the context clean, is the task split small enough, is there a skill for it?

## Escalation log
| Date | Task type | From -> to | Trigger | Fixed it? |
|------|-----------|------------|---------|-----------|
```

### B. CLAUDE.md snippet (one line on purpose)

```markdown
- Model choice: follow `.claude/model-routing.md`. Before starting a task that the rules put on a higher tier than this session, say so and suggest `/escalate` or a subagent.
```

### C. `.claude/settings.json` (merge with your existing file)

```json
{
  "model": "sonnet",
  "effortLevel": "high",
  "fallbackModel": ["sonnet", "haiku"],
  "statusLine": {
    "type": "command",
    "command": "jq -r '\"\\(.model.display_name) · effort \\(.effort.level // \"-\") · ctx \\(.context_window.used_percentage // 0)% · $\\(.cost.total_cost_usd // 0)\"'"
  }
}
```

The status line command needs `jq` installed. If you'd rather have Claude Code write the script for you, run `/statusline show model, effort, context percentage and cost` instead. That is Nate's approach ([00:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=56s)–[01:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=63s)).

### D. `.claude/agents/bulk-reader.md`

```markdown
---
name: bulk-reader
description: Use for high-volume reading that needs only a short answer back - scraping or searching many pages, scanning logs, reading large parts of the codebase or docs to find specific facts. Returns a compact summary, never full file contents.
tools: Read, Grep, Glob, WebFetch, WebSearch
model: haiku
---
You read a lot so the main thread doesn't have to.
- Read what the task asks for; stop once you can answer.
- Return at most 300 words: the facts found, each with its file path or URL, then anything you could not find.
- If the question needs judgement rather than lookup (design choices, trade-offs, "is this safe"), say so in one line and return the raw findings instead of deciding.
```

### E. `.claude/agents/Explore.md` (optional override)

```markdown
---
name: Explore
description: Fast read-only codebase search and analysis. Use for finding files, symbols and usages before planning or editing.
tools: Read, Grep, Glob
model: haiku
---
Search the codebase read-only and report file paths, line numbers and a short explanation of what you found. Do not propose edits.
```

### F. Hand-off prompt for the building session (paste into a fresh `claude --model sonnet` session)

```text
Implement the approved plan in plans/<file>.md, one step at a time.
For each step: make the change, run the check listed for that step, and paste the check's output under the step's status line.
Do not change the plan. If a step fails its check twice, or the plan looks wrong, stop and tell me which escalation trigger in .claude/model-routing.md fired - don't improvise a new approach.
```

### G. `.claude/agents/implementer.md`

```markdown
---
name: implementer
description: Use to carry out one approved step from a saved plan file - edit code, run that step's check, report the result. Not for planning or design decisions.
model: sonnet
---
You implement exactly one plan step per invocation.
1. Read the step and its check from the plan file named in the task.
2. Make the smallest change that satisfies the step.
3. Run the check and return: files changed, the check command, its output, pass/fail.
If the check fails twice, stop and return "ESCALATE: <one-line reason>".
```

### H. `.claude/skills/escalate/SKILL.md`

```markdown
---
name: escalate
description: Re-attempt the current problem on the flagship tier with higher effort after an escalation trigger fires (repeated failed check, contradiction, irreversible action). Invoke manually with /escalate.
disable-model-invocation: true
model: opus
effort: xhigh
---
An escalation trigger from .claude/model-routing.md has fired.
1. Restate the goal and what has already been tried, in five lines or fewer.
2. Before proposing a fix, check whether the failure is really a context problem: stale or contradictory context, a task too big for one pass, or a missing procedure. If so, say that plainly.
3. Otherwise diagnose the root cause and give the next concrete step, including how it will be checked.
4. Append a row to the Escalation log table in .claude/model-routing.md.
```

### I. Headless run with an explicit model (`scripts/nightly-digest.sh`)

```bash
#!/usr/bin/env bash
set -euo pipefail
# Small tier for bulk summarising; keep aliases in sync with the Registry in .claude/model-routing.md
claude -p "Summarise every file changed in the last 24 hours of git log into notes/digest-$(date +%F).md: one bullet per change, with the file path." \
  --model haiku \
  --allowedTools "Bash(git log *),Bash(git diff *),Read,Write" \
  --output-format json | jq '{result: .result, cost_usd: .total_cost_usd}'
```

### J. Prompt for an orchestrated run

```text
Before dispatching any leaf task, label it mechanical or hard using the routing rules in .claude/model-routing.md.
Mechanical leaves go to the bulk-reader or implementer subagent; hard leaves stay on this thread or go to a subagent with model: opus.
Record the label next to each task in the plan file, and if a mechanical leaf fails its check, relabel it hard and re-dispatch once.
```

### K. Cowork global-instructions snippet

```markdown
## Model choice
I pick the model myself in the model menu. Before you start a task, check it against this rule and tell me in one line if I should switch first:
- Quick answers, short documents, summaries: Sonnet with thinking on is fine.
- Restructuring folders or systems, multi-step projects, anything hard to undo: suggest Opus.
- Simple, repetitive batch work: suggest a lighter model if one is available.
Don't start a long task on a model the rule says is wrong without asking me.
```

## Done when

- [ ] `.claude/model-routing.md` exists. Its Registry is the only place in the repo that names a model version: `grep -rnE "claude-(haiku|sonnet|opus|fable)-[0-9]" --include=*.md --include=*.json --include=*.sh .` finds matches only in the Registry block.
- [ ] `/model` with no argument opens on your chosen default in a new session.
- [ ] Asking Claude to "use the bulk-reader subagent to find every TODO in src/" runs the subagent on Haiku. Check its model in the transcript.
- [ ] A big change was planned on the flagship and built on the balanced tier, either with `opusplan` or with two sessions and Prompt F.
- [ ] `/escalate` answers on the flagship, and the next normal prompt is back on your default model.
- [ ] Every scheduled or scripted `claude -p` call passes `--model`.
- [ ] Your Cowork global instructions include Snippet K, and Claude suggested a switch at least once when a task needed one.
- [ ] After one week, the escalation log has entries, and you've changed at least one starting tier based on it, or confirmed that none needed changing.

## Pitfalls

- **Model names go stale.** Every source here names a model that is now dated: Sonnet 4.6, Opus 4.7 (Knowing More [02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s), [03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)), and Opus 4.6 / GPT 5.4 (Ras Mic [00:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=50s)).
  - Use tiers in rules and aliases in config, and keep pinned IDs in the Registry only.
  - Aliases such as `opus` move to the newest release when you update Claude Code. If you need a run you can reproduce exactly, pin the ID, or pin what the alias resolves to with `ANTHROPIC_DEFAULT_OPUS_MODEL` and similar variables.
- **Retirement dates arrive.** Haiku 4.5 is only guaranteed until 2026-10-15. Put a reminder on the Registry's "Last checked" line and look at the deprecations page monthly (Beyond the source).
- **Cheap subagents still use your limit.** Each subagent is its own full conversation, and on a $20 plan a small multi-agent setup can use up the limit ([[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)). Only delegate reading that would otherwise fill the main thread.
- **A small model on hard work fails faster.** Smaller models show their limits sooner ([[AI LABS - The Unlazy Skill for Lazy Agents]] [00:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=56s)–[01:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=62s)). Give bulk-reader subagents lookup tasks, not judgement calls. Starter file D tells the subagent to hand back judgement calls.
- **Moving up a tier to fix a context problem.** If the session is past the "dumb zone" (the Coding Sloth says about 100–200K tokens, [13:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=817s)), a bigger model just costs more for the same drift. Start a fresh session first ([14:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=844s)). See [[Context Hygiene Routine]].
- **Assuming the built-in Explore subagent is cheap.** It used to run on Haiku but now inherits your main model (Beyond the source). Nate's advice to put reading on Haiku ([06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)) now needs Starter file E or explicit subagents.
- **Believing `ultrathink` sets a 32K budget.** Nate describes it that way ([13:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=827s)), but it now only asks for deeper reasoning on one turn. Use `/effort` for depth that lasts the whole session (Beyond the source).
- **Switching models too often in one session.** Changing models mid-session loses the prompt cache, while turning `/advisor` on or off doesn't (Beyond the source). Switch at task boundaries, or use subagents and skills for short detours.
- **Organisation allowlists change the model you asked for.** If `availableModels` blocks a model, Claude Code substitutes the newest permitted version of that family and shows a notice. If a skill's `model:` value is blocked, the skill simply runs on the session model. Check the transcript before assuming a route worked (Beyond the source).
- **Expecting Claude to switch its own model in Cowork.** Snippet K has Claude *recommend* a switch; you still make it in the model menu. The Cowork help pages checked here say nothing about instruction-driven switching, so don't rely on it.

## Variations

- **Adviser instead of switching.** Run the balanced tier and add a flagship adviser with `/advisor opus` or `"advisorModel": "opus"`. Claude consults it at decision points, which suits long tasks that are mostly routine (Beyond the source).
- **Change effort before changing model.** Anthropic's docs say adjusting effort is often a better lever than changing model. Try `/effort xhigh` on your current model before escalating, and `/effort low` on routine sessions (Beyond the source).
- **Efficiency-first vs capability-first.** A cost-sensitive project can start every task type on the small tier and move up only where it fails. A high-stakes project can start on the flagship and step down once it's reliable. These are Anthropic's two starting strategies (Beyond the source).
- **API and managed pipelines.** Outside Claude Code, the same table maps onto an orchestrator with cheaper workers. [[Claude Managed Agents]] multi-agent orchestration lets each agent in the roster have its own model (Beyond the source).
- **Cross-vendor routing.** The Coding Sloth notes that Cursor, OpenCode and Codex let you mix models from different vendors ([08:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=485s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s)). Keep the tier table and add a vendor column to the Registry.
- **Enterprise default.** Admins can set an organisation-wide default model for chat, Cowork and Claude Code. The routing file then only covers when to leave that default (Beyond the source).

## Sources

- [[Knowing More - Every Claude Model Explained]]: the tier sketches, "Sonnet for 90%", and moving up to Opus when Sonnet struggles or a decision is irreversible ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s), [04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s), [06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)–[07:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=426s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: Haiku subagents under an Opus main thread ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s), [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)), ultrathink after repeated misses ([13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)), and a status line showing model and cost ([00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: plan on Opus, build on Sonnet ([07:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=457s)–[08:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=483s)); what subagents cost ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)); the dumb zone ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)).
- [[Simon Pittman - Set Up Claude Cowork]]: Sonnet with extended thinking by default and Opus for ambitious work in Cowork ([04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s)–[04:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=299s)), with switches per task shown in the demos ([33:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1994s), [35:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=2138s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: a model router for large orchestrated runs ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)); laziness affects every tier ([00:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=48s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: context and harness matter more than which model ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s), [27:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1647s)), and a skill fixed what Opus got wrong ([09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s)).

## Beyond the source

*None of this comes from the videos. It was checked on 2026-09-15 at the links given.*

- **Current tiers.** Source: https://platform.claude.com/docs/en/about-claude/models/overview
  - Claude Fable 5.1 (`claude-fable-5-1`, $10/$50 per MTok)
  - Claude Opus 5 (`claude-opus-5`, $5/$25)
  - Claude Sonnet 5 (`claude-sonnet-5`, $2/$10)
  - Claude Haiku 4.5 (`claude-haiku-4-5-20251001`, $1/$5, 200K context)
- **Deprecations.** Haiku 4.5 is committed only until 2026-10-15, and Anthropic gives at least 60 days' notice before retiring a public model. Source: https://platform.claude.com/docs/en/about-claude/model-deprecations
- **Claude Code aliases.** Source: https://code.claude.com/docs/en/model-config
  - `default`, `best`, `fable`, `opus`, `sonnet`, `haiku` and `opusplan`, plus `[1m]` variants.
  - On the Anthropic API, `opus` maps to Opus 5, `sonnet` to Sonnet 5 and `fable` to Fable 5.1.
  - `default` is Opus 5 on Max, Team Premium, Enterprise and the API, and Sonnet 5 on Pro and Team Standard.
- **Where the model is set, highest priority first.** Source: https://code.claude.com/docs/en/model-config
  1. `/model` during a session. In the picker, Enter saves the choice as your default and `s` applies it to this session only.
  2. `claude --model` at launch.
  3. The `ANTHROPIC_MODEL` environment variable.
  4. The `"model"` settings key.
  5. `ANTHROPIC_DEFAULT_MODEL`, the default for new sessions.
- **Pinning and limiting models.** Source: https://code.claude.com/docs/en/model-config
  - `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` and `ANTHROPIC_DEFAULT_FABLE_MODEL` pin what each alias resolves to.
  - `availableModels` restricts which models can be selected. When it blocks a family alias, Claude Code substitutes the newest permitted version and names both models in a notice. A skill or command whose `model:` is blocked runs on the session model instead.
  - `fallbackModel` (an array in settings) and `--fallback-model` (a comma-separated list) define a fallback chain, capped at three models. Rate-limit, authentication and billing errors never trigger a switch.
- **Effort.** On Fable 5.1, Opus 5 and Sonnet 5 the levels are `low`, `medium`, `high`, `xhigh` and `max`, with `high` as the default. Haiku 4.5 doesn't support effort. Sources: https://code.claude.com/docs/en/model-config, https://platform.claude.com/docs/en/about-claude/models/overview
  - Set it with `/effort`, `--effort`, `CLAUDE_CODE_EFFORT_LEVEL`, the `effortLevel` setting or per-model `modelSettings`. Neither settings key accepts `max`.
  - `ultrathink` asks for deeper reasoning on one turn without changing the session's effort.
- **Subagent models.** Source: https://code.claude.com/docs/en/sub-agents
  - The frontmatter `model:` field accepts `sonnet`, `opus`, `haiku`, `fable`, a full model ID or `inherit`.
  - Resolution order: the per-invocation `model` parameter, then frontmatter, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main conversation's model. Setting `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` forces one model for every subagent.
  - Subagent files live in `.claude/agents/` (project) or `~/.claude/agents/` (user). Subagents also accept `effort:`.
  - The built-in Explore subagent inherits the main model, capped at Opus on the Claude API. Define your own `Explore` with `model: haiku` to override it.
- **Skill models.** In a SKILL.md, `model:` applies for the rest of the current turn and isn't saved, and `effort:` overrides the session's effort while the skill is active. With `context: fork`, `model:` sets the model of the forked subagent instead. Source: https://code.claude.com/docs/en/skills
- **Headless runs.** Source: https://code.claude.com/docs/en/headless and https://code.claude.com/docs/en/cli-reference
  - `claude -p` accepts most CLI flags, including `--model`, `--effort` and `--agents` (JSON subagent definitions with a `model` field). A few, such as `--bg`, are rejected.
  - With `--output-format json`, the response includes `total_cost_usd` and a per-model cost breakdown. Both are client-side estimates.
  - In `-p` mode, `/model sonnet` also works as an argument form.
- **Status line fields.** The status line script receives session JSON including `model.display_name`, `effort.level`, `context_window.used_percentage` and `cost.total_cost_usd`. Source: https://code.claude.com/docs/en/statusline
- **Adviser.** Source: https://code.claude.com/docs/en/advisor
  - Turn it on with `/advisor <model>`, the `advisorModel` setting or `--advisor`. It is experimental and works only on the Anthropic API.
  - The adviser must be at least as capable as the main model, and Haiku can't act as an adviser.
  - Turning it on or off keeps the prompt cache, whereas switching models loses it.
- **Managed Agents.** In multiagent orchestration every agent is configured separately, so each one can run a different model with its own prompt, tools, MCP servers and skills. Source: https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration
- **Choosing a model in Cowork and the apps.**
  - The model menu next to the send button sets the model, the effort and whether thinking is on. For models with effort levels, the Thinking toggle sits under Effort; other models show an "Extended" toggle. The help article describes chat. Simon uses the same kind of picker in Cowork ([04:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=270s)). Source: https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
  - Cowork scheduled tasks have an optional model field. Source: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
  - Enterprise admins can set a default model for chat, Cowork and Claude Code. Members can still choose another, and Claude remembers each member's last selection. Source: https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization
- **Fable access.** Max plans and Premium seats can spend up to 50% of the weekly limit on Fable at no extra cost. Pro plans and Standard seats on Team and Enterprise need usage credits. The API bills Fable at standard API rates. Fable 5.1 in Claude Code needs version 2.1.255 or later. Source: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- **Anthropic's own guidance.** Source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model and https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - The two starting strategies are efficiency-first (Haiku 4.5) and capability-first (Opus 5).
  - Build a use-case eval set before switching models.
  - Before building an adviser or orchestrator setup, sweep effort on your current model and price the stronger model at `low` effort.

## Related

- Idea: [[Choosing a Claude Model]]
- Pairs with: [[Plan-First Workflow]] · [[Plan Before Executing]] · [[Subagents and Agent Teams]] · [[Context Hygiene Routine]] · [[Keep CLAUDE.md Lean]] · [[Agent Skills]] · [[Evidence-Gated Completion Ledger]] · [[Schedule Recurring Claude Tasks]] · [[Set Up Claude Cowork]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[Unlazy]] · [[Claude Managed Agents]]
- People: [[Nate Herk]] · [[The Coding Sloth]] · [[Simon Pittman]] · [[Ras Mic]] · [[AI LABS]]
