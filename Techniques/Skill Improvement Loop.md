---
type: technique
goal: "Make a skill more reliable with every use: turn each real failure into a fix written back into the skill, log every run for review, test changes against the same task run without the skill, and keep lessons in a learning.md journal inside the skill folder"
difficulty: intermediate
time_to_build: "About 30 minutes to add the journal, run log, evals and loop files; then about 5 minutes per real failure and 15 to 30 minutes per A/B round (vault estimate)"
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tools: ["[[Claude Code]]"]
tags: [topic/skills, topic/loops, topic/memory, topic/verification, topic/subagents, topic/claude-code, topic/automation]
---

# Skill Improvement Loop

> **Provenance.** Points with a timestamp link come from [[Ras Mic - How AI Agents and Claude Skills Work]], [[AI LABS - Types of Claude Loops Explained]] or [[Chase AI - The Agentic OS Setup for Claude Code]]. Later additions: [[Nate Herk - Build Skills Instead of Agents]] and [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]. None of the first three shows a file. Ras Mic draws his loop on a whiteboard, AI LABS keeps its command and agent files in a paid community, and Chase points to a separate video for loop details. The `learning.md` format, run log, evals file, A/B scripts, `skill-grader` and `skill-improver` subagents, `/skill-loop` skill and prompts below are **vault starter content** written for this note. The two shell scripts were exercised against a stub `claude` before publishing, not against real model runs. Claude Code mechanics are verified under **Beyond the source**. For the ideas behind this, see [[Loop Engineering]], [[Agent Memory Patterns]] and [[Agent Skills]].

## Goal

A skill that gets better each time it's used, instead of failing the same way twice:

- every real failure is diagnosed, fixed, and written back into the skill;
- every run leaves a one-line record that a later review can mine;
- before you trust a change, the skill is tested against the same task run *without* it, so you know it actually helps;
- lessons live in a `learning.md` journal inside the skill folder, and only lessons that held up are promoted into `SKILL.md`.

## Use when

- **A skill you rely on still fails now and then.** Ras Mic's point is that even a skill built from a successful run will slip, because it has gaps ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s)–[21:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1276s)).
- **The workflow has many moving parts.** His YouTube report pulls from about eight data sources, far too much for one prompt. It became reliable only after five fix-and-update rounds ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s)–[22:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1358s)).
- **You can't tell whether a skill helps.** AI LABS built its learning loop after writing several skills for its community site and realising it had no way to know if they worked ([05:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=335s)–[05:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=346s)).
- **A skill already runs as an automation.** Chase's order is skill, then automation, then a self-improvement loop fed by logged runs ([11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s)–[12:15](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=735s), [22:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1371s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)).

**Skip it** for a skill that has never worked end to end. Build that first with [[Build a Skill from a Successful Run]]; Ras Mic calls writing a skill before a working run the worst move ([08:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=518s)–[08:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=527s)). Skip the automated A/B phase when you can't write checkable assertions for the output, and stay with the manual loop.

## How the three sources fit together

| | Ras Mic: fix on failure | Chase: log every run | AI LABS: learning loop |
|---|---|---|---|
| **Trigger** | A real run fails | Every run of a skill or automation | You run a command and name the skill |
| **Who finds the problem** | You ask the agent why it failed and what error it hit ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)–[21:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1301s)) | A loop that can see what past runs did ([22:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1371s)–[22:55](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1375s)) | A skill-improver agent that tests the skill across several areas ([06:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=361s)–[06:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=367s)) |
| **Evidence** | The corrected run, still in the conversation ([22:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1325s)) | Logged outputs; his vault has a `runs` folder ([22:02](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1322s), [22:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1354s)–[22:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1357s)) | The same task run with and without the skill in separate background sessions ([06:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=380s)–[06:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=394s)) |
| **Where lessons go** | Into the skill file itself ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)–[22:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1332s)) | No file named; logs, outputs and loops should all sit in the same place in his vault ([22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s)–[23:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1381s)) | `learning.md` inside the skill folder ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)–[06:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=410s)) |
| **Human role** | In every round | Not specified | None shown; rounds repeat until nothing is left to improve ([05:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=353s)–[05:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=358s)) |

This note combines them. The manual loop is the default, the run log feeds a periodic review, and the A/B round checks a change before you keep it.

## Where the sources differ

- **Human in the loop or autonomous.** Ras Mic works through each failure himself. He treats it as the moment to improve the skill rather than something to get annoyed about ([23:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1387s)–[23:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1400s)). AI LABS's improver runs rounds in background sessions that don't stop to ask permission ([06:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=384s)–[06:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=387s)). *Vault position:* automation may propose changes, but a person approves what reaches `SKILL.md`.
- **Update the skill, or also keep a journal.** Ras Mic edits the skill directly. AI LABS's improver, an agent rather than a person, also edits the skill directly ([06:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=396s)–[06:40](https://www.youtube.com/watch?v=8wsM0euQOvc&t=400s)), and it adds a `learning.md` journal ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)) so the agent knows what caused problems before when the skill is used ([05:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=325s)–[05:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=329s)). *Vault position:* do both, as AI LABS does. The journal holds every attempt, and `SKILL.md` gets only short, proven rules, because everything in a loaded skill costs context each time it runs.
- **How fast it pays off.** Ras Mic warns of an unpleasant early stretch, about two weeks in his case ([23:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1431s)–[24:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1446s)). AI LABS presents rounds running until the skill is as good as it gets ([07:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=424s)–[07:08](https://www.youtube.com/watch?v=8wsM0euQOvc&t=428s)), but reports no before-and-after numbers.
- **Edit a step, or add a rule?** This note says to edit an existing step rather than append one. [[Nate Herk - Build Skills Instead of Agents]] adds an explicit rule once the same mistake repeats (timestamp in the Phase 2 table). *Vault position:* a one-off gets a step edit, and a mistake seen twice earns a Gotchas rule.

## Prerequisites

- [[Claude Code]] in a git repository, so every skill edit is a diff you can review and revert.
- A project skill in `.claude/skills/<name>/` that has completed its job at least once.
- For the A/B phase:
  - `claude`, `jq` and `rsync` on your PATH;
  - three to five realistic test prompts, each with assertions a reader could check;
  - usage budget for about twice as many headless runs as you have prompts, per round. Chase mentions that a plan to bill `claude -p` separately had been walked back when he recorded ([27:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1671s)–[28:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1693s)). The change is still paused as of 2026-09-15, so headless runs draw on your plan's usage limits (Beyond the source).
- Optional: [[Workflow Audit into Skills]] to choose which skills are worth the effort.

## Steps

### Phase 1: prepare the skill (once per skill)

1. **Add the journal.** Create `learning.md` in the skill folder from the starter. AI LABS's journal lives inside the skill itself ([06:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=408s)).
2. **Add a Gotchas section to `SKILL.md`,** capped at about 15 bullets. Proven lessons land here.
3. **Add a last step that logs the run.** The skill appends one line to `runs/<skill>/log.md`. This is the vault's version of Chase's rule that outputs get logged where a loop can find them ([22:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1354s)–[22:42](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1362s)). Keep `runs/` outside the skill folder, and out of git if outputs contain client or personal data.
4. **Write `evals/evals.json`** with three to five prompts taken from real past runs, each with assertions.
5. **Commit.**

### Phase 2: fix on every real failure (Ras Mic)

Greg Isenberg sums up the method on the podcast as: map the workflow, define right and wrong, iterate, then codify ([13:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=831s)–[14:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=842s)). This phase is the iterate step.

6. **Diagnose before retrying.** In the failed session, send Prompt 1. Ras Mic's experience is that the agent will explain the failure in detail when asked, such as a credits problem with an API ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)–[21:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1301s)).
7. **Feed the failure back and have it finish the task.** It might retry the API call, try the step again, or write code to fix it ([21:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1278s)–[21:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1285s), [21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s)–[22:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1323s)).
8. **Confirm the task is now done correctly** before touching the skill ([22:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1325s)).
9. **Write the fix back while it's still in context.** Send Prompt 2. It changes one step or adds one Gotchas bullet, and adds a journal entry ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)–[22:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1332s)).
10. **Review the diff** with `git diff .claude/skills/<name>`, then commit. If the change is more than a few lines, run Phase 4 before you trust it.

**Where the fix goes.** Just saying "fix it" repairs the output but not the process ([05:07](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=307s)–[05:09](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=309s)). After a run you had to correct, send Prompt 4 and route each fix by its cause, following [[Nate Herk - Build Skills Instead of Agents]]:

| Cause | Smallest durable place | Source |
|---|---|---|
| Wrong process | Edit the step in `SKILL.md` | [05:45](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=345s)–[05:49](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=349s) |
| Missing voice, brand or examples | A `references/` file | [05:49](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=349s)–[05:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=352s) |
| Same mistake again | One Gotchas rule | [05:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=352s)–[05:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=357s) |
| Code rewritten each run, or flaky | A working script in `scripts/`, run by `SKILL.md` | Vault mapping to his first practice ([02:23](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=143s)–[02:39](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=159s)); see [[Build a Reference-Rich Skill]] |
| Skill didn't load, or the wrong one did | The `description` | [04:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=286s)–[04:48](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=288s); see [[Audit Skill Descriptions and Triggers]] |
| Looked in the wrong place | The routing; first have it show where it searched | [05:13](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=313s)–[05:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=326s) |

### Phase 3: review the run log (Chase)

11. **Every week, or every ten or so runs, send Prompt 3.** It groups failures by cause, proposes at most three changes, and flags lessons nothing has needed lately. If the skill runs as an automation, schedule the review as well. Chase sets up automations from a prompt or from the Routines page in the Claude desktop app ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s)); see [[Schedule Recurring Claude Tasks]].

### Phase 4: A/B learning round (AI LABS)

12. **Install the starter files:** `ab_run.sh`, `ab_round.sh`, the two subagents and the `/skill-loop` skill.
13. **Run the evals from a normal terminal at the repo root,** not from inside Claude Code (see Pitfalls): `bash .claude/skills/skill-loop/scripts/ab_round.sh .claude/skills/<name> round-01`.
    - Each prompt runs twice, in fresh temporary folders, once with the skill and once without. That mirrors AI LABS's two-way comparison ([06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s)–[06:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=394s)) in separate sessions ([06:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=380s)–[06:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=387s)).
    - AI LABS doesn't say how it launches its background sessions. Using `claude -p` here is the vault's choice.
14. **In Claude Code, run `/skill-loop <name> round-01`.**
    - A read-only `skill-grader` subagent scores both outputs against the assertions. Keeping the judge separate from the editor, with no edit tools, follows AI LABS's score-only reviewer in its verification loop ([10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s)–[10:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=633s)).
    - The `skill-improver` reads the grades and the journal, makes one focused edit, and appends a journal entry ([06:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=396s)–[06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s), [06:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=412s)–[07:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=421s)).
15. **Check the edit.**
    - Run `ab_round.sh … round-01-check`, then `/skill-loop <name> round-01-check`.
    - Keep the edit only if the with-skill pass count rose and nothing that passed before now fails. Otherwise revert it.
16. **Stop** when:
    - a round keeps nothing;
    - the skill passes every assertion; or
    - three edits have been kept in one sitting.

    AI LABS's rule of going until nothing is left to improve has no cap ([05:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=353s)–[05:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=358s)). A cap keeps cost bounded.
17. **If the skill doesn't beat the baseline, treat that as the finding.** The model may already do this job well, and the skill is spending context for nothing. Consider shrinking or deleting it; Ras Mic's advice is to give the model only what is specific to you ([32:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1929s)–[32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).

### Phase 5: promote and prune

18. **Once a month, review `learning.md`.**
    - Promote a lesson into Gotchas only if it held in at least two rounds or two real runs.
    - Mark lessons that no longer apply as `retired`, and remove them from Gotchas.
19. **Commit with a message that names the round,** for example `skill(weekly-report): round 3, 4/5 assertions`.
20. **After each model change, re-baseline** with Phase 4.
    - **Why.** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] warns that a newer model may already do what a skill says ([09:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=580s)–[09:52](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=592s)). `/skill-doctor` shows cost and usage, not whether a skill still helps ([09:53](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=593s)–[10:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=605s)).
    - **Then.** Shrink or retire skills that no longer help.

## Starter files & prompts

*Everything in this section is vault starter content, not from any of the videos. Prompt 4 puts the idea behind Nate Herk's retro prompt into the vault's own words.*

### Folder layout

```text
your-repo/
├── .claude/
│   ├── agents/
│   │   ├── skill-grader.md          # read-only judge
│   │   └── skill-improver.md        # edits SKILL.md and learning.md
│   └── skills/
│       ├── skill-loop/
│       │   ├── SKILL.md             # /skill-loop <name> <round>
│       │   └── scripts/
│       │       ├── ab_round.sh      # every eval, with and without the skill
│       │       └── ab_run.sh        # one eval, two fresh temp folders
│       └── weekly-report/           # the skill being improved
│           ├── SKILL.md             # includes Gotchas and a log-this-run step
│           ├── learning.md          # lesson index + journal (not read at run time)
│           └── evals/
│               ├── evals.json
│               └── files/           # fixture inputs copied into each run
└── runs/
    └── weekly-report/
        ├── log.md                   # one line per real run
        └── ab/round-01/<eval-id>/{with_skill,without_skill}/
```

### `learning.md`

```markdown
# Learning journal: weekly-report

Read by the skill-improver and by you during reviews. The skill does not load
this file at run time; proven lessons are copied into SKILL.md → Gotchas.

## Lesson index
| ID | Lesson (one line) | Evidence | Status | In SKILL.md? |
|---|---|---|---|---|
| L1 | Retry the analytics API once on HTTP 429 before reporting failure | R2, run 2026-09-12 | proven | yes |
| L2 | Ask for the date range when the request doesn't give one | R1 | candidate | no |

Status: candidate (seen once) · proven (held in 2+ rounds or real runs) · retired (no longer true)

## Journal (newest first)

### R3 · 2026-09-15 · A/B round
- Tried: moved chart-format rules into references/charts.md, linked from step 4
- Evals: with skill 4/5 assertions (was 3/5) · without skill 1/5
- Regressions: none
- Lesson: L1 still holds; no new lesson
- Decision: kept (commit a1b2c3d)

### R2 · 2026-09-12 · real failure (manual loop)
- What failed: stopped after the analytics API returned 429
- Root cause given: rate limit; the skill had no retry step
- Fix: retry-once step added; Gotchas bullet L1
- Confirmed by: rerun finished the report
- Decision: kept
```

### Additions to the skill's `SKILL.md`

```markdown
## Gotchas (proven lessons only, max 15)
- Retry the analytics API once on HTTP 429 before reporting failure. (L1)

## Last step: log this run
Append one line to runs/weekly-report/log.md (create it if missing):
YYYY-MM-DD HH:MM | ok / partial / failed | input: <short> | output: <path> | issue: <one line or -> | feedback: <one line or ->
```

### `evals/evals.json`

Field names follow Anthropic's skill-creator (Beyond the source), whose `expectations` list holds each case's checkable assertions. skill-creator uses numeric ids; keep ids as text here, because `ab_run.sh` matches them as strings.

```json
{
  "skill_name": "weekly-report",
  "evals": [
    {
      "id": "report-last-week",
      "prompt": "/weekly-report make last week's report from the CSVs in files/",
      "files": ["files/youtube.csv", "files/links.csv"],
      "expected_output": "report.md with a summary, a per-channel table and three recommendations",
      "expectations": [
        "report.md exists in the working folder",
        "The table has one row per channel that appears in the CSVs",
        "Every total in the summary matches the CSV data",
        "There are exactly three recommendations"
      ]
    }
  ]
}
```

### Prompt 1: diagnose (in the failed session)

```text
Stop. Before trying anything else: what exactly failed, at which step of the
<skill-name> skill, and what error or evidence did you get? Quote the error.
Then say whether the cause is (a) a missing or wrong step in the skill,
(b) something outside the skill (credentials, rate limits, bad input), or
(c) a step the skill already has that you didn't follow.
```

### Prompt 2: write the fix back (after the task succeeded)

```text
That worked. Update .claude/skills/<skill-name> so this doesn't happen again:
- (a) missing or wrong step: change that step and keep it short.
- (b) outside cause: add one Gotchas bullet on how to detect and handle it.
- (c) skipped step: make the existing step more prominent instead of adding text.
Nothing specific to today's input (no names, dates or file names).
Append a journal entry to learning.md (What failed / Root cause / Fix /
Confirmed by / Decision: pending) and add or update the lesson in the index as
"candidate". Show me the diff and stop.
```

### Prompt 3: run-log review (weekly)

```text
Read runs/<skill-name>/log.md for the last 30 days and learning.md. Group failed
and partial runs by likely cause. For each group give the count, two example
dates, and whether an existing lesson covers it. Propose at most three changes to
the skill, each backed by at least two runs. List lessons in the index that no
run has needed in 60 days as candidates to retire. Don't edit anything.
```

### Prompt 4: post-run retro (smallest durable place)

```text
Before we close: for each correction I made this run, name its cause (from the
table in Phase 2) and propose one change in the smallest place that will last.
Nothing specific to today's input. Show the diffs, rerun the same task and
report whether each fix held.
```

### `scripts/ab_run.sh`

```bash
#!/usr/bin/env bash
# Run one eval prompt twice, each in a fresh temporary folder: with the skill, then without it.
# Run from a normal terminal at the repo root, not from inside a Claude Code session.
# Usage: ab_run.sh <skill-dir> <eval-id> <out-dir>
# Optional: EXTRA_TOOLS="Bash(python3 *)" to allow more tools in both runs.
set -euo pipefail

skill_dir=$(cd "$1" && pwd)
id=$2
out=$3
name=$(basename "$skill_dir")
evals="$skill_dir/evals/evals.json"

prompt=$(jq -r --arg id "$id" '.evals[] | select(.id == $id) | .prompt' "$evals")
[ -n "$prompt" ] || { echo "No eval with id '$id' in $evals" >&2; exit 1; }
tools="Read,Write,Edit,Glob,Grep,Skill${EXTRA_TOOLS:+,$EXTRA_TOOLS}"

for mode in with_skill without_skill; do
  work=$(mktemp -d)

  # Copy the fixture files this eval lists (paths are relative to evals/)
  jq -r --arg id "$id" '.evals[] | select(.id == $id) | .files[]?' "$evals" |
    while IFS= read -r f; do
      mkdir -p "$work/$(dirname "$f")"
      cp "$skill_dir/evals/$f" "$work/$f"
    done

  extra=()
  if [ "$mode" = with_skill ]; then
    run_prompt=$prompt
    mkdir -p "$work/.claude/skills"
    # The skill under test, minus its evals and journal
    rsync -a --exclude evals --exclude learning.md "$skill_dir/" "$work/.claude/skills/$name/"
  else
    run_prompt=${prompt#"/$name "}   # the baseline can't call the skill by name
    # Also switch the skill off in case it is installed in ~/.claude/skills
    extra=(--settings "$(jq -cn --arg n "$name" '{skillOverrides: {($n): "off"}}')")
  fi

  (
    cd "$work"
    claude -p "$run_prompt" ${extra[@]+"${extra[@]}"} \
      --permission-mode acceptEdits \
      --allowedTools "$tools" \
      --max-turns 30 \
      --no-session-persistence \
      --output-format json > _result.json < /dev/null
  ) || echo "Run failed: $id / $mode (see _result.json)" >&2

  mkdir -p "$out/$id/$mode"
  cp -R "$work/." "$out/$id/$mode/"
  rm -rf "$work"
done
```

### `scripts/ab_round.sh`

```bash
#!/usr/bin/env bash
# Run every eval of a skill with and without the skill.
# Usage, from the repo root in a normal terminal: ab_round.sh <skill-dir> <round-label>
set -euo pipefail

skill_dir=$1
round=$2
name=$(basename "$(cd "$skill_dir" && pwd)")
here=$(cd "$(dirname "$0")" && pwd)
out="runs/$name/ab/$round"

jq -r '.evals[].id' "$skill_dir/evals/evals.json" | while IFS= read -r id; do
  echo "== $id"
  bash "$here/ab_run.sh" "$skill_dir" "$id" "$out" < /dev/null
done
echo "Done: $out"
echo "Next, in Claude Code: /skill-loop $name $round"
```

If the skill needs to run its own scripts, allow them for both runs, for example `EXTRA_TOOLS="Bash(python3 *)" bash …/ab_round.sh …`. On Claude Code v2.1.259 or later you can also add `--permission-prompts none` to the `claude -p` call. A plain `-p` run already denies requests that nothing approves; the flag also tells Claude that nobody can approve them, so it moves on instead of retrying.

### `.claude/agents/skill-grader.md`

```markdown
---
name: skill-grader
description: Grades the with-skill and without-skill outputs of one eval against its assertions. Read-only. Use only when /skill-loop asks for grading.
tools: Read, Glob, Grep
model: sonnet
---

You are a strict grader and you never change files.

Input: an eval id, its assertions, and two folders (with_skill, without_skill).
Each folder holds the files the run produced plus _result.json.

For each folder and each assertion:
- Look for concrete evidence in the files.
- Mark it passed only if you can point to the evidence (file and line, or a
  short quote). If you are unsure, it failed.

Reply with JSON only:
{"eval_id": "...",
 "with_skill": [{"assertion": "...", "passed": true, "evidence": "..."}],
 "without_skill": [{"assertion": "...", "passed": false, "evidence": "..."}],
 "notes": "one or two sentences on what differed"}
```

### `.claude/agents/skill-improver.md`

```markdown
---
name: skill-improver
description: Improves one skill from A/B grading results and its learning journal. Makes a single focused edit per round and records it. Use only when /skill-loop delegates a round.
tools: Read, Glob, Grep, Edit, Write
model: opus
---

You improve one skill. Inputs: the skill folder path and this round's
grading.json files.

1. Read SKILL.md, the lesson index and the last five journal entries in
   learning.md, and every grading file.
2. Find the most common reason the with-skill runs failed an assertion. Look for
   a pattern across evals; one odd run is not a pattern.
3. Make a single focused change that addresses it:
   - prefer clarifying or reordering an existing step over adding text;
   - put long detail in a references/ file linked from SKILL.md;
   - never touch evals/ or make an assertion easier.
4. Append a journal entry (Tried / Evals / Regressions / Lesson / Decision:
   pending) and add or update the lesson in the index as "candidate".
5. Reply with a summary of the diff, the lesson ID and what the check round
   should confirm.

Make no edit, and say why, if: the skill already passes everything, the failures
come from a broken eval, or the fix would only repeat something the model does
well without the skill.
```

### `.claude/skills/skill-loop/SKILL.md`

```markdown
---
name: skill-loop
description: Grades an A/B round for a skill, then either asks the skill-improver for one edit or decides whether to keep the last edit. Use when the user runs /skill-loop after ab_round.sh.
disable-model-invocation: true
argument-hint: "<skill-name> <round-label>"
allowed-tools: Bash(git status *) Bash(git diff *) Bash(jq *)
---

# Skill loop: $0, $1

Skill: .claude/skills/$0 · Evals: .claude/skills/$0/evals/evals.json
Round outputs: runs/$0/ab/$1/<eval-id>/with_skill and /without_skill

## 1. Preflight
Stop and tell the user if the round folder, evals.json or learning.md is missing.
On a normal round, also stop if `git status` shows uncommitted changes in the
skill folder.

## 2. Grade
For each eval id, give the skill-grader subagent the eval's expectations and both
output folders. Save each reply to runs/$0/ab/$1/<eval-id>/grading.json.
Print a table: eval id · with skill passed/total · without skill passed/total.

## 3a. Normal round (label does not end in -check)
- If the skill passes every assertion, stop and report.
- If the skill does no better than the baseline on any eval, stop and report
  that the skill may not be earning its context.
- Otherwise delegate to the skill-improver with the skill path and this round's
  grading files.
- Then tell the user to run, in a normal terminal:
  bash .claude/skills/skill-loop/scripts/ab_round.sh .claude/skills/$0 $1-check
  and afterwards: /skill-loop $0 $1-check

## 3b. Check round (label ends in -check)
Compare against the grading of the same label without -check.
- Keep the edit only if the with-skill pass count rose and no assertion that
  passed before now fails.
- Kept: set the journal entry's Decision to "kept", propose a commit message,
  and ask before committing.
- Not kept: restore every changed file in the skill folder except learning.md
  (list them with git diff --name-only), set Decision to "reverted", say why.

Finish with a table of rounds so far (with / without / decision) and any
lessons now seen twice, which are ready to promote.
```

## Done when

- [ ] `learning.md` (index plus journal), a capped Gotchas section, a log-this-run step and `evals/evals.json` with at least three cases and assertions are committed.
- [ ] At least one real failure went through Prompts 1 and 2, leaving a one-lesson diff and a journal entry.
- [ ] `runs/<skill>/log.md` has entries from real use, and one Prompt 3 review has been done.
- [ ] One A/B round finished with `grading.json` for both modes of every eval.
- [ ] The with-skill runs beat the baseline on at least one eval, or you've recorded that they don't and decided what to do about the skill.
- [ ] A check round kept or reverted the edit based on pass counts, and the journal says which.
- [ ] Every Gotchas bullet is marked `proven` in the index.
- [ ] `SKILL.md` isn't longer than when you started, unless each added line maps to a proven lesson.

## Pitfalls

- **Skill bloat.** Each fix adds a line, and after ten rounds the skill reads like a changelog.
  - Once a skill is invoked, its content stays in context for the rest of the session (Beyond the source). Ras Mic's case for skills rests on keeping context lean, because a filling context window makes the model worse ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)–[31:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1919s)).
  - Cap Gotchas, edit an existing step rather than appending a new one, and retire stale lessons.
  - Move long detail into `references/` (see [[Build a Reference-Rich Skill]]).
- **Overfitting to one failure.** A rule that names today's client, file or date makes the skill worse for every other input.
  - Prompt 2 bans input-specific rules, and the improver looks for patterns across evals.
  - Promote only lessons seen twice. Anthropic's skill-creator gives the same advice: generalise from feedback rather than fitting the test cases (Beyond the source).
- **Treating noise as a lesson.** One bad run can be a flaky API or a one-off slip. Rerun the task before changing the skill, and log single sightings as `candidate`.
- **Judging with no standard.** AI LABS names this as the weak spot of `/goal`: a model deciding the work is done, with nothing to measure against ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s)–[02:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=171s)). The same applies here. Write assertions a person could check, and keep the grader read-only and separate from the improver.
- **Gaming the evals.** The improver must never edit `evals/`. Grow the eval set from real failures instead.
- **Unattended runs with no permission checks.** AI LABS's background sessions don't stop to ask ([06:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=384s)–[06:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=387s)). The starter scripts instead use throwaway temp folders, `acceptEdits` and a short tool allowlist, and never bypass permissions. See [[Configure Safe Autonomy Permissions]].
- **Launching the A/B runs from inside Claude Code.** A nested-session guard has been reported to block `claude -p` started from a Claude Code Bash tool (Beyond the source). Run `ab_round.sh` from a normal terminal, or use skill-creator's subagent-based evals instead.
- **A contaminated baseline.** If the same rules also live in CLAUDE.md or in another skill, the "without" run isn't really without them. The script switches the skill off with `skillOverrides`; check CLAUDE.md yourself.
- **The with-skill run never used the skill.** Look in its output. Either start the eval prompt with `/<skill-name>`, which Claude Code expands before running, or keep `Skill` in the allowed tools.
- **Reaching for `--bare` to speed things up.** It skips skill discovery, so the with-skill run silently becomes a second baseline (Beyond the source).
- **No round cap.** Running until nothing is left to improve ([05:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=353s)–[05:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=358s)) can burn a lot of usage.
- **Assuming a skill evens out models.** Nate says no skill makes a weaker model perform like a stronger one, and advises testing important skills in another compatible agent to expose hidden assumptions ([06:14](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=374s)–[06:42](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=402s)).
- **Private data in logs and journal.** Run logs can capture client names or personal details. Keep `runs/` out of shared repos, or redact it.
- **Quitting in week one.** Ras Mic expects about two weeks of frustration before an agent setup pays off ([23:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1431s)–[24:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1446s)).
- **Improving a skill that was never grounded.** An improvement loop can't rescue a skill written in the abstract.
  - Ras Mic's order is to walk the agent through the work until it succeeds, then turn that run into a skill ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)–[11:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=676s)).
  - Chase gives the same caution: confirm the task works by hand before asking for a skill ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)–[07:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=456s)).

## Variations

- **Manual only.** Phases 1 and 2 are Ras Mic's whole method; five rounds of it made his report skill dependable ([22:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1352s)–[22:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1358s)).
- **Scheduled review.** Run Prompt 3 as a weekly routine. Chase creates routines from the Claude desktop app by naming the routine, telling it to run the skill and setting a schedule ([11:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=691s)–[11:46](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=706s)). See [[Routines and Scheduled Tasks]].
- **Journal read at run time, as AI LABS describes.** The skill reads the lesson index before starting, so it avoids past problems ([05:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=325s)–[05:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=329s)). This costs context on every run, so keep the index short and keep the journal in a separate file.
- **Improve the whole workflow, not one skill.** AI LABS's workflow improvement loop adds a process-optimizer agent that reviews each iteration of the whole loop ([11:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=706s)–[11:55](https://www.youtube.com/watch?v=8wsM0euQOvc&t=715s), [12:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=744s)–[12:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=754s)). See [[Multi-Agent Review and Scoring Loops]].
- **All in one session with skill-creator.** Anthropic's skill-creator runs with-skill and baseline subagents, grades them and builds a benchmark (Beyond the source). Use it in place of Phase 4 if you'd rather not script headless runs.
- **Ready-made with/without evals: Caliper.** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] shows a terminal tool that compares an agent's work with and without a skill ([10:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=605s)–[10:19](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=619s)).
  - **How it works.** grill-skill interviews you, and evaluate-skill writes and runs the evals (a prompt plus the expected result). Runs are kept in `.caliper` ([10:19](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=619s)–[10:49](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=649s)).
  - **Where it starts.** It begins with evals and grills you only if it gets stuck ([10:51](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=651s)–[11:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=665s)). This note starts from real runs instead.
  - **What it reports.** Whether gains justify the extra tokens. It covers MCP servers too ([11:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=683s)–[11:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=695s)).

  Read the repo before installing ([[Build vs Install Third-Party Skills]]).
- **Hook-based run logging.** Instead of a logging instruction in `SKILL.md`, a `Stop` hook script can check the transcript for the skill's use and append the log line. Hooks run every time; instructions can be skipped (Beyond the source).
- **An improver with its own memory.** Give `skill-improver` a project `memory` scope, so patterns it sees across skills persist, such as descriptions that trigger too often (Beyond the source). See [[Agent Memory Patterns]] and [[Claude Code Auto Memory]].
- **Borrow from others' skills without installing them.** Ras Mic reads published skills, or asks his agent what can be learned from them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)). Feed those ideas in as `candidate` lessons and test them in an A/B round. See [[Build vs Install Third-Party Skills]].
- **Evals from past sessions.** Chase has Claude go through recent sessions to find repeated tasks ([07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s)–[08:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=532s)). The same review can surface failures worth turning into eval cases. See [[Workflow Audit into Skills]].

## Sources

- [[Ras Mic - How AI Agents and Claude Skills Work]]:
  - building skills from successful runs, and why not to install others' skills ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s));
  - recursive skill building and the eight-source report ([20:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1242s)–[23:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1400s));
  - expectations ([23:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1421s)–[24:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1446s));
  - progressive disclosure, token cost and the context budget ([29:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1780s)–[32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).
- [[AI LABS - Types of Claude Loops Explained]]:
  - loop engineering ([00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s)–[01:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=71s));
  - the weakness of `/goal` ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s)–[02:51](https://www.youtube.com/watch?v=8wsM0euQOvc&t=171s));
  - the learning loop ([05:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=303s)–[07:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=429s));
  - the score-only reviewer ([10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s)–[10:47](https://www.youtube.com/watch?v=8wsM0euQOvc&t=647s));
  - the workflow improvement loop ([11:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=687s)–[13:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=790s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]:
  - loop engineering within his levels ([02:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=140s)–[02:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=161s));
  - validating a task by hand before making a skill ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)–[07:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=456s));
  - automations and self-improvement loops ([10:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=657s)–[12:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=748s));
  - logging runs where loops can read them ([22:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1348s)–[22:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1379s));
  - the recap ([30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)–[30:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1852s));
  - the `claude -p` billing aside ([27:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1671s)–[28:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1693s)).
- [[Nate Herk - Build Skills Instead of Agents]]: saving scripts, fixes in the smallest durable place, and the limits across models ([01:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=86s)–[06:42](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=402s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: stale skills after model updates, the limits of `/skill-doctor`, and Caliper ([09:34](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=574s)–[11:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=695s)).
- *Caption fixes used here:*
  - "Ross Mike" is Ras Mic;
  - "create the scale out MD file" is the SKILL.md file;
  - "gold command" is `/goal`;
  - "claw desktop" is the Claude desktop app;
  - "claude-p" is `claude -p`;
  - "skill.mmd" is SKILL.md;
  - "skill doctor command" is `/skill-doctor`;
  - "{dot} Caliper" is the `.caliper` folder.

  AI LABS's exact command names aren't given in the captions. Ras Mic's "505 error, insufficient credits" is a loose example, and the real HTTP code is unclear.

## Beyond the source

*Not from the videos. Each item was checked at the linked page on 2026-09-15.*

- **Skills in Claude Code.**
  - Once invoked, a skill's content stays in context across later turns. After auto-compaction, invoked skills are re-attached, keeping the first 5,000 tokens of each within a 25,000-token total.
  - `skillOverrides` in settings can set a named skill to `"off"`.
  - Frontmatter supports `disable-model-invocation`, `argument-hint` and `allowed-tools`. The body can use `$0` and `$1` for arguments and `${CLAUDE_SKILL_DIR}` for the skill folder.
  - Keep `SKILL.md` under 500 lines.

  Source: [skills docs](https://code.claude.com/docs/en/skills).
- **Subagents.**
  - They are Markdown files in `.claude/agents/` with `name` and `description`, plus optional `tools` (allowlist), `model`, `maxTurns` and `memory`.
  - `memory: project` gives the agent `.claude/agent-memory/<name>/`, and the first 200 lines or 25KB of its `MEMORY.md` go into its system prompt.
  - Subagents can spawn their own subagents, three levels deep by default.

  Source: [subagents docs](https://code.claude.com/docs/en/sub-agents).
- **Headless runs.**
  - **What loads.** `claude -p` loads the same skills and CLAUDE.md as an interactive session. `--bare` skips skills, CLAUDE.md and other auto-discovery, and doesn't use subscription login.
  - **Permissions.** `-p` starts in Manual permission mode, so pass `--permission-mode` and `--allowedTools`. `--permission-prompts none` (v2.1.259+) denies anything that would prompt and tells Claude not to retry; a `-p` run with no permission host denies those requests anyway.
  - **Inputs and outputs.** `/skill-name` inside the prompt is expanded before the run. `--settings` takes a file or JSON. `--output-format json` returns the result, the session ID and an estimated `total_cost_usd`.

  Source: [headless docs](https://code.claude.com/docs/en/headless).
- **CLI flags.** `--max-turns` (print mode only), `--no-session-persistence`, and `--disable-slash-commands`, which turns off all skills and commands for a blunter baseline. Source: [CLI reference](https://code.claude.com/docs/en/cli-reference).
- **Hooks.**
  - Events include `Stop` and `SubagentStop`, which can block stopping with exit code 2, and `SessionEnd`.
  - Hook input includes common fields such as `session_id`, `transcript_path` and `cwd`.
  - Hooks can be set in `.claude/settings.json` or in skill and subagent frontmatter. Skill hooks are registered when the skill runs and last for the session.

  Source: [hooks reference](https://code.claude.com/docs/en/hooks).
- **skill-creator.**
  - **Testing.** It runs each test prompt in two subagents: one with the skill, and a baseline (no skill for a new one, the previous version for an existing one). Test cases live in `evals/evals.json`: each has an integer `id`, a `prompt`, an `expected_output`, optional `files` and an `expectations` list. A grader checks each expectation against the outputs and writes `grading.json` with `text`, `passed` and `evidence` fields.
  - **Benchmark.** Results are aggregated into a benchmark with pass rate, time and tokens.
  - **Guidance.** It advises generalising from feedback rather than overfitting to the test cases. It can also tune the description against should-trigger and should-not-trigger queries, using a train/test split.

  Source: [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [skill-creator schemas](https://github.com/anthropics/skills/blob/main/skills/skill-creator/references/schemas.md).
- **Anthropic's authoring guide.**
  - Build evaluations before writing extensive instructions: start from gaps you see without the skill, write at least three scenarios, and measure a baseline.
  - Iterate with one Claude instance refining the skill and a fresh one using it, and watch which files it reads.
  - There's no built-in way to run these evaluations.

  Source: [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- **Nested sessions.** This is reported behaviour; the current docs don't cover it. An issue filed in February 2026 (Claude Code 2.1.63) shows `claude --print` run from a Claude Code Bash tool being blocked by a nested-session guard. When the guard was bypassed, it printed nothing. The issue was closed as a duplicate, and the current troubleshooting page doesn't mention the guard. Source: [issue #29543](https://github.com/anthropics/claude-code/issues/29543).
- **`claude -p` billing.** Anthropic announced in May 2026 that `claude -p` and Agent SDK usage would move to a separate monthly credit, then paused the change on 15 June 2026, the day it was due. Anthropic's help page says `claude -p` still draws from your subscription's usage limits, the promised credit isn't available, and any new plan will be announced before it takes effect. Source: [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), [The New Stack](https://thenewstack.io/anthropic-pauses-claude-agent-sdk-subscription-change/).
- **`/skill-doctor`** (Claude Code v2.1.252+) reports each skill's context cost and usage, and flags skills that have never been invoked. It covers cost and usage only. Source: [skills docs](https://code.claude.com/docs/en/skills).
- **Model dependence.** Anthropic's authoring guide says a skill's effectiveness depends on the underlying model, and advises testing with every model you plan to use. Source: [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- **Caliper.** MIT licence; install with `pipx install caliper-eval`. `--ablate <skill>` runs without the skill, and `--k` (default 3) repeats attempts. Results, with token use, go under `.caliper/results/`. Source: [Caliper repo](https://github.com/edonadei/caliper).

## Related

- Concepts: [[Loop Engineering]] · [[Agent Memory Patterns]] · [[Agent Skills]] · [[Verification Before Done]] · [[Context Window Management]] · [[Permissions and Approval Gates]] · [[Subagents and Agent Teams]]
- Techniques: [[Build a Skill from a Successful Run]] · [[Build a Reference-Rich Skill]] · [[Multi-Agent Review and Scoring Loops]] · [[Build Verification into Every Task]] · [[Evidence-Gated Completion Ledger]] · [[Schedule Recurring Claude Tasks]] · [[Configure Safe Autonomy Permissions]] · [[Workflow Audit into Skills]]
- Tools and people: [[Claude Code]] · [[Ras Mic]] · [[Greg Isenberg]] · [[AI LABS]] · [[Chase AI]]
- [[Home]]
