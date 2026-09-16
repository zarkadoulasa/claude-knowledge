---
type: technique
goal: Keep every Claude Code session inside its useful context range with a short, repeatable routine for setup, session start, mid-session checks, thresholds and topic switches
difficulty: beginner
time_to_build: 15–20 minutes to set up; under a minute per session after that
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Knowing More - Every Claude Model Explained]]"]
tools: ["[[Claude Code]]"]
tags: [topic/context, topic/claude-code, topic/subagents, topic/planning]
---

# Context Hygiene Routine

## Goal

The aim is for each session to start lean, stay below a context threshold you've chosen, and end or compact on your terms before quality slips. As a side effect you spend less of your plan's usage.

The routine combines four sources:

- Nate Herk's session commands (status line, `/context`, `/compact`, `/clear`, Esc).
- Ras Mic's context budget.
- The Coding Sloth's one-task-per-session habits.
- AI LABS's lesson that files outlast instructions.

The reasoning behind every step is in [[Context Window Management]].

## Use when

- You run long or multi-step Claude Code sessions.
- Your plan's usage limit bites. The Coding Sloth has hit his limit on the $20 plan after one or two prompts ([00:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=21s)–[00:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=25s)), and says usage is metered by tokens on every plan ([12:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=762s)–[12:59](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=779s)).
- Late in sessions you see forgetting, contradictions, silly mistakes ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)–[13:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=800s)) or skipped work ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)–[02:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=121s)). See [[Agent Laziness]].
- You lean on research, skills or MCP servers, which can push a task past 100,000 tokens ([14:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=853s)–[14:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=859s)), or on subagents, each a full conversation of its own ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).

**Skip it** for a quick one-off question in a fresh session.

## Prerequisites

- Claude Code installed, and a project folder to work in.
- `jq`, if you use the manual status-line script below. `/statusline` can generate a script for you instead.
- A project CLAUDE.md you're willing to trim. See [[Keep CLAUDE.md Lean]].
- A decision about your threshold (step 2).

## Steps

### A. One-time setup

1. **Add a status line that shows context use.**
   - Run `/statusline` and describe what to show, for example model, context percentage and cost ([00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)–[01:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=63s)).
   - [[Nate Herk - 32 Tricks to Level Up Claude Code]] says the point is to always see how much context is left, so you avoid context rot ([01:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=71s)–[01:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=74s)).
   - Use starter 1 or 2 below.
2. **Pick your threshold and write it down.** The sources offer three:
   - Compact at about 60% ([02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s), Nate).
   - Stay between fresh and about 70% ([31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)–[31:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1887s), [[Ras Mic - How AI Agents and Claude Skills Work]]).
   - A token ceiling somewhere in the 100K–200K range where quality starts to dip ([13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)–[13:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=824s), [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]).
   - *Vault suggestion:* on a 1M-window model, use a token figure. 60% of 1M is far past every source's line.
   - Put the number in CLAUDE.md (starter 4) and in the status-line warning.
3. **Trim the always-loaded layer.**
   - Keep CLAUDE.md to 150–200 lines at most, and point to other files instead of holding their content ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)–[07:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=461s)).
   - Delete anything the model already knows or can read from the code, such as which framework the codebase uses ([02:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=144s)–[02:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=153s)). Keep only what it can't know ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)–[32:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1972s)).
   - Move multi-step procedures into skills ([04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)–[04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s)).
4. **Take a baseline.** In a fresh session, run `/context` to see what is using space: system prompt, files, MCP servers ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)–[02:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=121s)). If it looks bloated, find the cause and restructure ([02:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=121s)–[02:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=127s)).
5. **Paste the context-hygiene block into CLAUDE.md** (starter 4).

### B. Starting a task

6. **One task, one session.**
   - Start a new session, or run `/clear`, for every new task ([14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=849s)).
   - Chaining tasks in one session degrades output and uses up your limit ([14:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=862s)–[14:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=866s)).
   - You don't lose much by clearing, because CLAUDE.md and your files are still there ([02:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=162s)–[02:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=165s)).
7. **Check headroom before a big task.** Run `/context` first ([13:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=831s)–[13:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=835s)).
8. **Write a very specific first prompt.**
   - Name the files and sources to use. Vague prompts make Claude read everything to work out what you mean ([14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s)).
   - Give only what this task needs, and split big problems into focused steps ([01:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=95s)–[01:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=106s)).
   - Use starter 5.
9. **Put the plan and requirements in a file before work starts.**
   - [[AI LABS - The Unlazy Skill for Lazy Agents]] found that telling an agent to be thorough fades in long sessions, while requirements written to a file up front hold ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)).
   - For multi-step work, keep a PLAN.md. For work you need proven, see [[Evidence-Gated Completion Ledger]] and [[Plan-First Workflow]].

### C. During the session

10. **Stop research tangents at once.** If Claude starts exploring files or topics it doesn't need, say so straight away. Every file and web page it reads costs tokens ([14:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=866s)–[14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)).
11. **Steer early.**
    - Press Esc as soon as it heads the wrong way, correct it and re-prompt. Tokens spent going the wrong way are wasted context ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)–[07:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=474s)).
    - Use `/rewind` to roll back a wrong turn ([08:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=503s)–[08:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=509s)).
12. **Push exploration and bulk reading into subagents.**
    - Each subagent works in its own window and reports back, so the main thread stays clean ([04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s)–[05:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=313s); [19:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1189s)–[19:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1196s)).
    - Nate's pattern is a cheaper model reading hundreds of thousands of tokens and handing back only the highlights ([06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=383s)).
    - Budget for it: each subagent is a full conversation, and on the $20 plan they can use your whole limit ([20:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1206s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).
    - Use starter 6.
13. **Glance at the status line after every big step.** This habit is the vault's suggestion. Knowing the number only helps if you act on it ([13:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=835s)–[13:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=838s)).

### D. At your threshold

14. **Choose: split or compact.**
    - **Split (the Coding Sloth's default).** If the remaining work can stand on its own, have Claude write HANDOFF.md (starter 7) and start a fresh session from it. He treats a fresh session as better than pushing a compacted one ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s)).
    - **Compact (Nate's approach).** If the work truly has to stay in one conversation, run `/compact` yourself and state exactly what to keep ([02:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=143s)–[02:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=150s); [15:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=923s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s)). Use starter 3.
15. **If Claude auto-compacted mid-task, don't push on.** Start a new session from PLAN.md or HANDOFF.md, because a self-compacted session loses quality noticeably ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s)).

### E. Switching topics

16. **Run `/clear` when you move to unrelated work.** You get a fresh conversation, with CLAUDE.md and your files still in place ([02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s)–[02:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=165s)).

### F. Before you close (optional)

17. **Leave the next session a file, not a memory.** Update PLAN.md or HANDOFF.md with status and next steps, so the next session starts from disk rather than from a long chat. This applies AI LABS's files-over-instructions idea ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)) to handoffs; the extension is the vault's.

## Starter files & prompts

*Everything in this section is **vault starter content**, written for this note. None of it is quoted from the videos. Settings keys and JSON field names were checked against the Claude Code docs (see Beyond the source).*

### 1. Status-line request

```text
/statusline Show the model name, context used as a percentage and as
approximate thousands of tokens, and session cost. Add the word WARN
after the context figure once it passes 60% or 150K tokens.
```

Change 60% and 150K to your own threshold from step 2.

### 2. Manual status-line script (if you'd rather not generate one)

Save as `~/.claude/statusline.sh`, then run `chmod +x ~/.claude/statusline.sh`:

```bash
#!/bin/bash
# Vault starter: context-aware status line for Claude Code
WARN_PCT=60     # your percentage threshold
WARN_K=150      # your token ceiling in thousands (matters on 1M-window models)

input=$(cat)
MODEL=$(echo "$input" | jq -r '.model.display_name // "model"')
PCT=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
SIZE=$(echo "$input" | jq -r '.context_window.context_window_size // 200000')
USED_K=$(( PCT * SIZE / 100 / 1000 ))

STATE="ok"
if [ "$PCT" -ge "$WARN_PCT" ] || [ "$USED_K" -ge "$WARN_K" ]; then
  STATE="WARN: split or /compact"
fi

echo "[$MODEL] context ${PCT}% (~${USED_K}K of $(( SIZE / 1000 ))K) | $STATE"
```

Register it in `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh"
  }
}
```

### 3. `/compact` with keep-instructions

The general form borrows Nate's idea of naming what must survive ([02:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=143s)–[02:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=150s)). The wording is original.

```text
/compact Keep: the goal and acceptance criteria from PLAN.md; every
decision we made and the reason for it; the files changed so far with
one line each on what changed; failing tests with their exact error
messages; the next three steps. Drop: exploratory file reads, approaches
we abandoned, full logs and command output that already passed.
```

For a debugging session:

```text
/compact Keep: the bug's symptoms and how to reproduce it, hypotheses we
ruled out and why, the current best hypothesis with evidence (file:line),
and the next check to run. Drop everything else.
```

### 4. CLAUDE.md block

```markdown
## Context hygiene
- One task per session. If I start an unrelated task, remind me to /clear first.
- Before reading files or doing web research I didn't name, say what you want
  to read and why in one line, then wait for my go-ahead.
- Keep plans, requirements and progress in PLAN.md, not only in chat.
  Update it after each finished step.
- Send bulk reading (long logs, many files, long docs) to a subagent and keep
  only its summary in this conversation.
- If I say "threshold", stop at the next clean point and offer two options:
  (a) write HANDOFF.md for a fresh session, or (b) a /compact line listing
  what to keep.
- Our threshold: 60% of the window or 150K tokens, whichever comes first.

# Compact instructions
When compacting, keep the goal, acceptance criteria, decisions with reasons,
files changed, failing tests with exact errors, and next steps. Drop
exploratory reads and abandoned approaches.
```

Claude can't see your status line, so the block asks *you* to call "threshold". The `# Compact instructions` heading is the documented way to steer compaction from CLAUDE.md.

### 5. Specific first prompt (template)

```text
Task: <one sentence>.
Read only: <file 1>, <file 2>, <doc URL>. Ask before reading anything else.
Done means: <observable result, e.g. `npm test -- auth` passes>.
Write the plan to PLAN.md first, then wait for my OK.
```

### 6. Subagent delegation prompt

```text
Use a subagent to read everything in logs/ and the two docs pages below.
Return only: the five most likely causes of the timeout, each with file:line
or URL as evidence, in under 300 words. Don't paste raw logs back here.
```

### 7. HANDOFF.md template (for splitting a session)

```markdown
# HANDOFF
## Task
## Done so far (file → one line on what changed)
## Decisions (and why)
## Open problems (exact errors, file:line)
## Next steps (numbered)
## Don't redo / don't re-read
```

The prompt for the new session:

```text
Read HANDOFF.md and PLAN.md, then carry out next step 1. Don't re-read
other files unless that step needs them.
```

## Done when

- [ ] Every session shows context % and approximate tokens in the status line.
- [ ] You've chosen a threshold and written it into CLAUDE.md and the status-line warning.
- [ ] CLAUDE.md is under about 200 lines, and you've taken one `/context` baseline.
- [ ] Each new task starts in a fresh session or after `/clear`.
- [ ] Multi-step tasks get a PLAN.md before work begins.
- [ ] You've run at least one `/compact` with keep-instructions and checked the summary kept what you listed.
- [ ] You've split at least one session through HANDOFF.md, and the new session carried on without re-reading the whole project.
- [ ] You've sent at least one bulk-reading job to a subagent, and the main session's context stayed small.

## Pitfalls

- **Pushing on after an auto-compact.** The Coding Sloth's warning: a session that compacts itself mid-task loses quality noticeably ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=921s)). Split instead.
- **Treating thresholds as laws.**
  - 60% ([02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)), about 70% ([31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)) and 100K–200K tokens ([13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)) are personal heuristics, and none is measured.
  - Start with one, then adjust based on when *your* sessions start slipping.
- **Reading percentages on a 1M window.** 60% of a 1M-token window is 600K, far past the point where the Coding Sloth sees quality dip. He also says a bigger window only extends the dumb zone ([13:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=809s)–[13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)). The token ceiling in starter 2 exists for this reason.
- **Trusting a big window.** [[Knowing More - Every Claude Model Explained]] pitches 1M tokens as roughly 2,000–3,000 pages in one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)–[02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)). The same video warns that Claude burns tokens fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)). Capacity isn't quality.
- **Watching instead of acting.** Seeing the number doesn't fix anything by itself ([13:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=835s)–[13:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=838s)). Tie the threshold to an action: split or compact.
- **Keeping rules only in chat.**
  - An instruction is the first thing to fade in a long session ([07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s)–[07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)).
  - Chat-only instructions can also be lost at compaction (docs; see Beyond the source).
  - Put anything that must persist in CLAUDE.md or a task file.
- **Treating subagents as free.** Each one is a full conversation that runs in parallel ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)). Delegate bulk reading, not every small step.
- **Over-trimming CLAUDE.md.** Ras Mic's rule removes what the model already knows. It keeps what it can't know, such as proprietary facts or a method you use every time ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)–[03:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=196s)).
- **Compacting when clearing would do** *(docs; see Beyond the source)*. Compacting a big context is itself a large request, while `/clear` costs nothing, and `/compact` in a fresh session only reports that there's nothing to compact. When you don't need continuity, clear.
- **Skills after compaction** *(vault inference from the docs)*. The startup list of skill descriptions isn't re-injected after `/compact`. If Claude stops picking up a skill it hadn't used yet, invoke that skill by name.

## Variations

- **Strict splitter** (the Coding Sloth, $20 plan): one task per session, a manual `/compact` only when splitting is impossible, subagents used sparingly because of their cost ([14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s), [15:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=923s), [20:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1206s)).
- **Long-haul compactor** (Nate): one long session, compacting at about 60% with keep-instructions and clearing only between unrelated tasks ([02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)–[02:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=161s)).
- **Minimal context** (Ras Mic): a near-empty CLAUDE.md, with every procedure moved into skills that cost only their name and description until used ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)–[30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s)). See [[Agent Skills]].
- **Files-first for big builds** (AI LABS): the plan file and gates file come first, and each task runs in a fresh subagent that sees only the plan and its own checklist ([08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)–[08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s), [11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s)–[11:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=714s)). See [[Evidence-Gated Completion Ledger]] and [[Unlazy]].
- **Automatic backstop** *(Beyond the source)*: set the auto-compact window close to your threshold with `/autocompact <tokens>` (100K minimum), so that if you miss the warning, compaction happens nearer your line than the default. Step 15 still applies after it fires.
- **Parallel work:** one session per git worktree, so parallel tasks never share a window. See [[Parallel Sessions with Git Worktrees]].
- **Cheaper bulk reading:** give reading subagents a cheaper model. See [[Route Tasks to the Right Claude Model]].

## Sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]:
  - status line ([00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)); keep context small ([01:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=95s)); `/context` ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s));
  - `/compact` at about 60% with keep-instructions and `/clear` between tasks ([02:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=128s)–[02:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=165s));
  - subagents ([04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s), [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)); a lean, routed CLAUDE.md ([06:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=413s)–[07:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=461s));
  - Esc early ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)); `/rewind` ([08:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=503s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]:
  - what fills the window ([06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s)); skills versus always-loaded files ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s), [30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s));
  - stay under about 70% ([31:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1879s)–[31:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1893s)); tell the model only what it can't know ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]:
  - tokens as your usage limit ([12:34](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=754s)); the dumb zone ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)); `/context` before big tasks ([13:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=831s));
  - new session per task, no tangents, specific prompts ([14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s));
  - after an auto-compact start fresh, or compact manually with what to keep ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s)); what subagents cost ([20:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1206s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]:
  - agents get lazier as context fills ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)–[02:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=148s));
  - requirements in files rather than instructions ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)); fresh-context subagents per task ([08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)).
- [[Knowing More - Every Claude Model Explained]]: the big window as capacity ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)), and Claude burning tokens fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)). It serves here as a caution, not a method.

## Beyond the source

Command behaviour below was checked against the Claude Code docs on 2026-09-15.

- **`/context [all]`.** Shows context usage as a coloured grid, with suggestions for context-heavy tools, memory bloat and capacity warnings. In fullscreen mode the per-item breakdown is collapsed; pass `all` to expand it. Its "Memory files" list shows which CLAUDE.md files loaded. <https://code.claude.com/docs/en/commands>, <https://code.claude.com/docs/en/memory>
- **`/compact [instructions]`.**
  - Summarises the conversation; the optional text tells it what to focus on.
  - In a fresh session it prints `Not enough messages to compact.`
  - A `# Compact instructions` section in CLAUDE.md steers every compaction.
  - Compacting a large context is itself a large request, while `/clear` costs nothing.
  - <https://code.claude.com/docs/en/commands>, <https://code.claude.com/docs/en/costs>
- **What survives compaction.**
  - The project-root CLAUDE.md is re-read from disk and re-injected.
  - Nested CLAUDE.md files and path-scoped rules reload when Claude reads matching files.
  - Instructions given only in conversation can be lost.
  - The startup skill-description list isn't re-injected, but the bodies of skills you already invoked are (up to 5,000 tokens each, 25,000 in total).
  - Auto memory and a plan written in plan mode come back from disk, and Claude Code re-reads up to five of the most recently modified files from the session.
  - <https://code.claude.com/docs/en/memory>, <https://code.claude.com/docs/en/context-window>
- **`/clear [name]`.** Starts a new conversation with empty context; its aliases are `/reset` and `/new`. Pass a name to label the old conversation, then return to it with `/resume`. The costs page also suggests `/rename` before clearing. <https://code.claude.com/docs/en/commands>, <https://code.claude.com/docs/en/costs>
- **Auto-compaction threshold.**
  - Models running a native 1M window on the Anthropic API (Fable 5 and 5.1, Sonnet 5, Opus 4.7 and later) auto-compact at about 967K tokens by default. Sonnet 4.6 and Opus 4.6 without extended context compact at 200K.
  - Change it with `/autocompact 500k` (saved to user settings), `claude --autocompact 500k` (one launch only), the `autoCompactWindow` setting, or `CLAUDE_CODE_AUTO_COMPACT_WINDOW` (a plain token count that overrides the rest). The command and flag accept 100K–1M.
  - <https://code.claude.com/docs/en/model-config>
- **Status line.**
  - `/statusline <description>` generates a script in `~/.claude/` and updates your settings.
  - A manual setup uses `"statusLine": {"type": "command", "command": "..."}`.
  - The script receives JSON on stdin, including `model.display_name`, `context_window.used_percentage`, `context_window.remaining_percentage` and `context_window.context_window_size` (200000 by default, or 1000000 with extended context).
  - `used_percentage` counts input tokens only and can be `null` early in a session, which is why the starter uses `// 0`.
  - <https://code.claude.com/docs/en/statusline>
- **Esc and `/rewind`.** Esc stops Claude immediately. `/rewind`, or pressing Esc twice, restores conversation and code to an earlier checkpoint. <https://code.claude.com/docs/en/costs>
- **Subagents.** Each starts with a fresh, isolated context and none of your history. Verbose output such as test runs, docs and logs stays there, and only a summary returns. The built-in Explore subagent is read-only. <https://code.claude.com/docs/en/sub-agents>
- **Specific prompts and stale context.**
  - The costs page contrasts a vague "improve this codebase", which triggers broad scanning, with a specific request naming a function and file.
  - It says stale context wastes tokens on every later message.
  - It recommends skills over long CLAUDE.md sections, keeping CLAUDE.md under 200 lines, and CLI tools over MCP where possible.
  - <https://code.claude.com/docs/en/costs>
- **Why this works.** Anthropic's context-engineering guidance describes context rot and a limited attention budget. It recommends compaction, structured notes kept outside the window, and subagents that return condensed summaries. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

## Related

- [[Context Window Management]]: the concept this routine applies
- [[Agent Laziness]]: what happens when a session runs too long
- [[Keep CLAUDE.md Lean]] and [[CLAUDE.md as a Router]]
- [[Subagents and Agent Teams]]
- [[Plan-First Workflow]] and [[Evidence-Gated Completion Ledger]]
- [[Parallel Sessions with Git Worktrees]]
- [[Route Tasks to the Right Claude Model]]
- [[Claude Code]]
