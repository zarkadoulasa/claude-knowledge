---
type: technique
goal: "Get an agreed, written plan with its assumptions and a verification step after every build step before Claude Code edits anything, then carry it out, optionally on a cheaper model"
difficulty: beginner
time_to_build: "About 10 minutes to add the settings, template and prompts, then 10 to 30 minutes of planning per big task (vault estimate)"
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]"]
tools: ["[[Claude Code]]"]
tags: [topic/planning, topic/claude-code, topic/prompting, topic/models, topic/verification, topic/context]
---

# Plan-First Workflow

> **Provenance.** Points with a timestamp link come from [[Nate Herk - 32 Tricks to Level Up Claude Code]] or [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]. Neither video shows a planning prompt, a plan file or a settings file. The prompts, template, settings snippet, skill and checklists below are **vault starter content** written for this note. Claude Code mechanics (plan-mode controls, `plansDirectory`, `opusplan`, `/model`) are verified under **Beyond the source**. For the idea itself and where the sources disagree, see [[Plan Before Executing]].

## Goal

On a big task, Claude first researches without editing and questions you until the requirements are clear. It then writes a plan with a check after every build step. You review the plan and save it to `plans/`. Claude then executes it, either on the same model or on a cheaper one working from the saved file, and nothing counts as done until the checks pass.

## Use when

- **The task is big or touches many files.** A mistake is much cheaper to catch in a plan than in a large diff ([[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [07:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=434s)–[07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s)).
- **Requirements are fuzzy** enough that you'd expect three or four revision rounds ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)–[03:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=236s)).
- **You want a strong model's judgement at a cheaper model's price.** Let the smart model plan and a faster, cheaper one build (Coding Sloth [07:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=455s)–[07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s)).

**Skip it for** typos, renames and small design tweaks, where it's wasted effort (Coding Sloth [07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)). Anthropic's quick test: if you could describe the diff in one sentence, don't plan (Beyond the source).

## Prerequisites

- [[Claude Code]] running in a git repository, so every stage can be committed and rolled back.
- **Something Claude can run to check its work:** a test runner, a type checker or linter, or for front-end work a screenshot or browser tool (Coding Sloth [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:40](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=580s); Nate [04:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=249s)–[04:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=254s)).
- **Two models in `/model` for the two-model variants**, e.g. Opus and Sonnet. The Coding Sloth notes that Fable now needs usage credits ([07:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=472s)–[08:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=480s)); which plans that applies to is under Beyond the source.
- **Optional:** a requirements-interview skill, such as [[Grill Me Interview Skill]] or [[Matt Pocock]]'s grill-with-docs, which the Coding Sloth uses to refine requirements ([06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)).

## Steps

1. **Triage.** Big, multi-file or unclear work gets a plan. A one-line change doesn't (Coding Sloth [07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)).
2. **Start clean.** Open a new session for the task, since a medium or big task uses at least about 50K tokens (Coding Sloth [14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=856s)). Run `/context` before you begin (Coding Sloth [13:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=831s)).
3. **Pick the planning model.** Run `/model opus`, or `/model opusplan` if you want Claude Code to switch to Sonnet automatically once you approve (Variant A). Typing `/model <name>` also saves that model as your default; to change it for this session only, open the `/model` picker and press `s` (Beyond the source). The Coding Sloth plans on Opus and implements on Sonnet ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)).
4. **Enter plan mode.** Press `Shift+Tab` until the status bar says plan mode is on (Nate [02:50](https://www.youtube.com/watch?v=jqoFP9QapXI&t=170s); Coding Sloth [06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s)), or start the prompt with `/plan`.
5. **Describe the problem, not the solution.** Send **Prompt 1**.
   - Ask how the problem should be handled instead of dictating a function (Nate [03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s)–[03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s)).
   - Be exact about constraints, the files and sources to use, and what done looks like (Coding Sloth [14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s)).
6. **Let Claude question you.** Prompt 1 tells it to use AskUserQuestion until more answers wouldn't change the plan. This is Nate's version of the step, which he frames as keeping going until Claude is 95% confident ([03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s)–[03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)). Answer with specifics. If none of the options fit, type your own answer in the "Other" row.
7. **Cut off tangents.** If Claude starts reading files or topics it doesn't need, stop it straight away, because every file it reads costs tokens (Coding Sloth [14:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=866s)–[14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)). Nate's version: press Esc, correct course and re-prompt ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)–[07:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=474s)).
8. **Review the plan before approving.** When the approval prompt appears, choose **No, keep planning** and send **Prompt 2** so Claude lays out its assumptions and decisions (Nate [03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s)–[03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s)), then work through the review checklist. To fix things, keep planning with your corrections, or press `Ctrl+G` and edit the plan yourself.
9. **Check verification is built in.** Every build step needs a check straight after it (Nate [03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)–[04:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=260s)). That means:
   - tests written *before* the code they test (Coding Sloth [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s));
   - a type check and lint run (Coding Sloth [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s));
   - screenshot or browser checks for UI work (Nate [04:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=249s)–[04:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=254s); Coding Sloth [09:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=577s)).

   Add a gate so Claude doesn't start the next step until the current one passes. Nate tells Claude not to move to the next to-do until Claude is 95% confident the current to-do is good ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)).
10. **Approve and save.**
    - Approving exits plan mode and Claude starts editing at once (Beyond the source), so the stop has to be in the plan itself. Prompt 1 makes step 0 "save this plan to `plans/` and wait".
    - Choose **Yes, manually approve edits**. The first edit you're asked to approve should be the plan file; approve it and Claude stops.
    - If Claude heads for code first, press Esc, reject the edit and send **Prompt 3**.
    - Commit the plan. After that, pick the executing model and approve edits however you like.

    Plan mode also writes its own plan file, under a name it picks, to `~/.claude/plans/` by default. Files there are deleted once they're older than `cleanupPeriodDays`, which is 30 days by default. The settings starter points that folder at `./plans` instead, so the step 0 file is the one to keep and commit.
11. **Execute.** To stay in the same session, send **Prompt 4**. To hand off to a cheaper model, start a fresh session with `claude --model sonnet` and send **Prompt 5** (Variant C). Either way, Claude works one step at a time, runs each check and logs the evidence.
12. **Steer early.** If Claude drifts, press Esc and re-prompt (Nate [07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)). Use `/rewind` to undo a wrong turn (Nate [08:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=503s)). If Claude auto-compacts in the middle of the task, start a new session from the plan file instead of carrying on, because quality drops (Coding Sloth [15:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=914s)–[15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s)).
13. **Close out.** Compare the evidence against the plan's "Done means" list. If a result is only okay, push back. Then have Claude write the lesson into CLAUDE.md or the relevant skill (Nate [07:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=478s)–[08:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=500s)).

## Starter files & prompts

*Everything in this section is vault starter content, not from either video.*

### Folder layout

```text
your-repo/
├── CLAUDE.md
├── .claude/
│   ├── settings.json            # plansDirectory, optional plan-mode default
│   └── skills/
│       └── plan-first/
│           └── SKILL.md         # optional /plan-first command
└── plans/
    ├── _template.md
    └── 2026-09-15-oauth-login.md
```

### `.claude/settings.json`

```json
{
  "plansDirectory": "./plans",
  "permissions": {
    "defaultMode": "plan"
  }
}
```

Keep `permissions.defaultMode` only if most work in this repo is big. Otherwise every small edit pays the planning overhead. Both keys are verified under Beyond the source.

### Prompt 1: problem, then interview (in plan mode)

```text
Problem: <what's wrong or missing, in user terms>
Why it matters: <who is affected; what good looks like>
Constraints: <stack, allowed or banned libraries, performance, deadlines>
Read first: <files, docs, example patterns>. Tell me before exploring anything else.
Out of scope: <what must not change>
Done means: <observable results, e.g. these tests pass, this page renders>

No code yet. First tell me how you think this should be handled.
Then use the AskUserQuestion tool to resolve anything ambiguous: requirements,
edge cases, trade-offs, and things I haven't considered. Ask in small batches
and stop only when further answers would not change the plan.
Then write the plan with:
- step 0: save this plan to plans/<YYYY-MM-DD>-<slug>.md using plans/_template.md,
  then stop and wait for my go-ahead before any other change
- the approach, plus the alternatives you rejected and why
- every assumption you are making
- the files you will touch
- numbered build steps, each followed by a verification step (a test written
  first, a command to run, or a screenshot/browser check) and its pass condition
- risks and how to roll back
```

### Prompt 2: pre-approval review (still in plan mode)

```text
Before I approve: list every assumption in this plan and label each one
"confirmed by me", "confirmed by the code" or "guess". Ask me about each guess.
Name the step most likely to go wrong and the cheapest early check for it.
Flag any build step without a verification step and any test planned after
the code it tests.
```

### Your review checklist

- [ ] The problem statement is what you actually want.
- [ ] No assumption is still labelled "guess".
- [ ] Out of scope is written down.
- [ ] Every build step has a check and a pass condition, and tests come before code.
- [ ] Tests cover what matters, not every line (Coding Sloth [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)).
- [ ] The file list holds no surprises.
- [ ] If handing off, a cheaper model could follow it without re-deciding anything.

### `plans/_template.md`

```markdown
---
title: <task>
status: draft          # draft | approved | in-progress | done | abandoned
planned_with: <model>
executed_with: <model>
created: YYYY-MM-DD
---

# <task>

## Problem

## Done means
- [ ] <observable, checkable result>

## Constraints

## Out of scope

## Decisions and assumptions
| Decision or assumption | Why | Confirmed by (user / code / guess) |
|---|---|---|

## Files to touch
- `path/to/file` — what changes

## Steps
1. **Build:** <change>
   **Verify:** <test written first / command / screenshot or browser check>
   **Pass when:** <exact signal>

## Risks and rollback

## Hand-off notes for the executing model
- Commands: <test, typecheck, lint, dev server>
- Patterns to copy: <file and line>
- Ruled out by the planner: <don't do these>

## Status log
- YYYY-MM-DD step 1: pass — <evidence>
```

### Prompt 3: save the approved plan (fallback if step 0 didn't happen)

```text
Before changing any code, write the approved plan to
plans/<YYYY-MM-DD>-<slug>.md using plans/_template.md. Fill every section from
this conversation, set status to approved and planned_with to your model name.
Reply with the path and stop.
```

### Prompt 4: execute in the same session

```text
Implement plans/<file>.md one step at a time. For each step: write the test
first if the step has one, make the change, run the verification, and append
the result with evidence (command and output summary, or screenshot path) to
the Status log. Do not start the next step until the current check passes.
If a check fails twice or the plan proves wrong, stop and tell me rather than
improvising. Finish by checking every "Done means" item with evidence.
```

### Prompt 5: hand-off to a cheaper model (fresh session)

Start the session with `claude --model sonnet`, then send:

```text
You are implementing a plan written by another model. Read plans/<file>.md in
full before doing anything. Follow it as written: no redesign, no extra scope,
no skipped verification steps. Set executed_with to your model name. Work step
by step and log evidence in the Status log. If a step is ambiguous or a check
cannot pass as written, stop and ask instead of guessing. When every step
passes, check each "Done means" item and report.
```

### Optional skill: `.claude/skills/plan-first/SKILL.md`

```markdown
---
name: plan-first
description: Plan a big coding task before any edits. Interviews the user, writes a plan with a verification step after every build step, and saves it to plans/. Use for /plan-first or when the user wants a feature, refactor or multi-file change planned before building.
disable-model-invocation: true
argument-hint: "[task description]"
---

# Plan first

Task: $ARGUMENTS

1. If the session is not in plan mode, switch to it or ask the user to press
   Shift+Tab. Make no edits until the plan is approved.
2. Read the files and sources the user named. Say why before reading anything else.
3. Use AskUserQuestion in small batches until more answers would not change the plan.
4. Draft the plan with the sections in plans/_template.md. Every build step gets a
   verification step and a pass condition. Tests come before the code they test and
   cover behaviour that matters, not every line.
5. Label each assumption confirmed-by-user, confirmed-by-code or guess; ask about guesses.
6. Present the plan for approval. After approval, save it to
   plans/<YYYY-MM-DD>-<slug>.md with status approved, then stop so the user can
   choose the executing model.
```

## Two-model variants

| Variant | How | Good for | Watch out for |
|---|---|---|---|
| **A. `opusplan`** | `/model opusplan` before planning. Opus runs in plan mode, and Claude Code switches to Sonnet once you approve | Least effort | Execution carries the whole planning conversation. Enable `showClearContextOnPlanAccept` to get an approve-and-clear option |
| **B. Manual switch** | Plan on Opus, approve, then switch to Sonnet. Typed `/model sonnet` also saves Sonnet as your default; open `/model` and press `s` to switch for this session only | Picking the executor task by task | Same context carry-over as A |
| **C. Fresh session from the file** (best for big tasks) | Prompt 3, exit, `claude --model sonnet`, Prompt 5 | A clean context and a hand-off you can audit. It matches the Coding Sloth's one-session-per-task habit ([14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)) and Anthropic's advice to run a spec in a fresh session | The plan has to stand on its own |
| **D. Audit-and-plan skill** | shadcn's improve: a strong model audits the codebase and writes plans for other agents (Coding Sloth [06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s)–[06:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=409s)). Execution details are under Beyond the source | Improvement passes across the whole codebase | It produces many plans at once, so review them before executing |
| **E. Another vendor builds** | Execute the saved plan in Cursor, OpenCode or [[OpenAI Codex]], which let you mix models (Coding Sloth [08:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=485s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s)) | Cheap in-house models | Other harnesses may not read CLAUDE.md, so put the key rules in the plan. See [[Tool-Agnostic Context Files]] |

The Coding Sloth's reason for not planning on Fable is that it now needs usage credits ([07:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=472s)–[08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)). That applies to Pro, not Max (Beyond the source). For routing more generally, see [[Route Tasks to the Right Claude Model]] and [[Choosing a Claude Model]].

## Done when

- [ ] `plans/_template.md` exists, and `.claude/settings.json` sets `plansDirectory` (or you always save with Prompt 3).
- [ ] On a real big task, Claude asked clarifying questions before writing the plan, and no assumption is still marked "guess".
- [ ] The saved plan has a verification step and pass condition after every build step, with tests before code.
- [ ] `git status` showed no source edits before you approved.
- [ ] Execution logged evidence for each step, and every "Done means" item passes.
- [ ] For a two-model run, `planned_with` and `executed_with` are filled in and the executor didn't redesign anything.
- [ ] After two or three tasks, you've checked whether you needed fewer correction rounds than before, which is Nate's claimed payoff ([03:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=233s)). If not, tune the prompts.

## Pitfalls

- **Planning everything.** Small edits gain nothing (Coding Sloth [07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)). Nate's "always" ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)) is the stronger claim of the two. See [[Plan Before Executing]].
- **Rubber-stamping.** The point of a plan is to catch mistakes before they spread across a dozen files (Coding Sloth [07:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=434s)–[07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)).
- **Treating "95% confident" as a measurement.** *Vault reading:* it's a prompt device. Stop when new answers no longer change the plan.
- **Vague instead of open.** Posing a problem (Nate [03:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=198s)) doesn't mean leaving out constraints. Vague prompts send Claude off reading everything (Coding Sloth [14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s)).
- **No checks in the plan.** Without them Claude can't tell whether its code works, only that it's written (Coding Sloth [08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s)–[09:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=541s)).
- **Tests after code**, which just pass that code (Coding Sloth [09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)–[09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s)). **Over-testing**, which bloats the codebase (Coding Sloth [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)–[09:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=568s)).
- **A plan only the planner could follow.** The Coding Sloth says cheaper models are capable ([07:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=462s)–[07:48](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=468s)). *Vault inference:* they still shouldn't be re-deciding the design, so write file paths, commands and pass conditions into the plan. shadcn's improve plans are built this way (Beyond the source).
- **Assuming plan mode can't change anything.** Nate's "won't change anything" ([02:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=174s)–[02:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=178s)) is the normal case. In the current docs, exploration commands can still run, and sessions with bypass permissions don't enforce the edit block.
- **Losing plans.** The default `~/.claude/plans/` is cleaned up automatically. Set `plansDirectory` or save with Prompt 3.
- **Looking for Ultraplan.** The Coding Sloth mentions it ([02:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=130s)), but it has been removed.
- **Assuming two models is always cheaper.** Anthropic suggests first trying a lower effort level on one model (Beyond the source).

## Variations

- **Deeper requirements first.** Run [[Grill Me Interview Skill]] or grill-with-docs (Coding Sloth [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)), then feed its output into Prompt 1.
- **Light version for medium tasks.** Skip the mode. Frame the problem and ask Claude to explain its assumptions before coding (Nate [03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s)–[03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s)).
- **Cheap research subagents while planning.**
  - Nate has Haiku subagents do the bulk reading and pass short summaries to an Opus lead ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s), [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s)).
  - The Coding Sloth warns that subagents can eat a low plan's whole limit ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).
  - See [[Subagents and Agent Teams]].
- **Goal-gated execution.** Turn the plan's "Done means" into a goal condition, such as every test passing with no type errors (Coding Sloth [19:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1149s)–[19:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1157s)). The command name is inaudible in the captions, but the feature he describes matches Claude Code's `/goal`. See [[Tests-First Goal Loop]].
- **Parallel plans.** Give each executing chat its own worktree (Coding Sloth [20:43](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1243s)). See [[Parallel Sessions with Git Worktrees]].
- **Ask "why?" without derailing the run.** `/btw` answers from the conversation so far and doesn't add to the history (Coding Sloth [11:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=670s)–[11:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=690s)).
- **Learn while delegating.** Have Claude explain each change before you accept it (Coding Sloth [16:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1004s)–[16:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1009s)).
- **Independent review against the plan.** A fresh reviewer compares the diff with the plan file. See [[Multi-Agent Review and Scoring Loops]] and [[Evidence-Gated Completion Ledger]].

## Sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]:
  - hacks 7–10, covering plan mode, problems instead of orders, AskUserQuestion and verification to-dos ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)–[04:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=285s));
  - Haiku subagents ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s));
  - hacks 16–18, covering exiting early, challenging outputs and `/rewind` ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)–[08:32](https://www.youtube.com/watch?v=jqoFP9QapXI&t=512s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]:
  - skills and shadcn's improve ([06:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=364s)–[06:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=409s));
  - plan mode, and planning strong while building cheap ([06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s));
  - verification ([08:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=511s)–[09:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=597s));
  - context habits ([13:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=831s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s));
  - `/goal`, subagents and worktrees ([19:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1149s)–[20:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1257s)).
- *Caption fixes used here:*
  - "Shatien's improved" is shadcn's improve;
  - "grow with doc" is grill-with-docs;
  - "easiest here" is the S-tier rating;
  - "ask user question tool" is AskUserQuestion;
  - the goal command's name is garbled at 19:05 ("It's here. It's straight."), and the description matches `/goal`.

## Beyond the source

*Not from either video. Each item was checked at the linked page on 2026-09-15.*

- **Plan-mode controls.**
  - **Entering.** `Shift+Tab` cycles modes, and the status bar shows `⏸ plan mode on`. A `/plan` prefix applies plan mode to one prompt, and `claude --permission-mode plan` starts a session in it. Pressing `Shift+Tab` again leaves without approving.
  - **What runs while planning.** Claude reads, runs exploration commands and writes a plan, but doesn't edit source until approval. A classifier reviews commands when auto mode is available; otherwise commands outside the read-only set prompt. In sessions with bypass permissions available, the edit block isn't enforced.
  - **Approving.** The approval prompt offers approve with auto mode (or auto-accept edits), approve with manual edit review, or **No, keep planning**. Approving exits plan mode and Claude starts editing straight away. `Ctrl+G` opens the plan in your editor, and `showClearContextOnPlanAccept` adds an approve-and-clear-context option.
  - **Defaults.** `defaultMode: "plan"` in `.claude/settings.json` makes plan mode the project default for terminal sessions. The VS Code extension uses `claudeCode.initialPermissionMode` instead.

  Source: [permission modes](https://code.claude.com/docs/en/permission-modes), [settings reference](https://code.claude.com/docs/en/settings-reference).
- **Where plans live.** By default plan files go to `~/.claude/plans/`, and Claude Code deletes files there once they're older than `cleanupPeriodDays` (default 30). `plansDirectory` sets a folder relative to the project root instead (a path outside the project falls back to the default), and Anthropic's example team settings use `"./plans"` to keep plans in the repo. Source: [the .claude directory](https://code.claude.com/docs/en/claude-directory), [example settings](https://code.claude.com/docs/en/settings-example).
- **Question and plan tools.** `AskUserQuestion` asks multiple-choice questions with a free-text "Other" row and needs no permission. Questions stay open unless you set `askUserQuestionTimeout`, and plan approval never auto-resolves. `EnterPlanMode` needs no permission; `ExitPlanMode`, which presents the plan, does. Source: [tools reference](https://code.claude.com/docs/en/tools-reference).
- **Switching models.**
  - `opusplan` uses Opus in plan mode and Sonnet in execution.
  - `/model <alias>` switches mid-session and, typed that way, also saves the model as your default. In the `/model` picker, `Enter` saves as default and `s` switches for this session only. `claude --model <alias>` sets the model for that launch without changing your default.
  - On the Anthropic API, `opus` is Opus 5 and `sonnet` is Sonnet 5. Fable is never a default and may bill usage credits after a consent prompt.

  Source: [model configuration](https://code.claude.com/docs/en/model-config).
- **Build-relevant facts, summarised.** The details are in [[Plan Before Executing]] under Beyond the source.
  - **Fable by plan.** It needs usage credits on Pro and standard seats, and is included on Max and premium seats. [Help Center](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
  - **Anthropic's flow.** Explore → plan → implement → commit. Skip the plan for one-sentence diffs, and run a spec in a fresh session; stronger gates are `/goal` or a Stop hook. [best practices](https://code.claude.com/docs/en/best-practices)
  - **Cost.** Try an effort sweep before adding a second model. [cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)
  - **shadcn's improve.** Read-only audit that writes one self-contained plan per finding to `plans/`. `/improve execute <plan>` hands a plan to cheaper subagents in isolated worktrees and checks the done criteria. Install with `npx skills add shadcn/improve`. [repo](https://github.com/shadcn/improve)
  - **Ultraplan** has been removed. [docs](https://code.claude.com/docs/en/ultraplan)

## Related

- Concepts: [[Plan Before Executing]] · [[Verification Before Done]] · [[Choosing a Claude Model]] · [[Context Window Management]] · [[Permissions and Approval Gates]]
- Techniques: [[Grill Me Interview Skill]] · [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Route Tasks to the Right Claude Model]] · [[Context Hygiene Routine]] · [[Parallel Sessions with Git Worktrees]]
- Tools and people: [[Claude Code]] · [[OpenAI Codex]] · [[Nate Herk]] · [[The Coding Sloth]] · [[Matt Pocock]]
- [[Home]]
