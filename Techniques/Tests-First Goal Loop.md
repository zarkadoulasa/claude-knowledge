---
type: technique
goal: "Let Claude Code build one feature unattended until a test suite written beforehand passes, committing every green state so the run can roll back instead of undoing changes from memory"
difficulty: intermediate
time_to_build: "About 30–45 minutes to set up the first time, plus however long the tests take to write (vault estimate)"
sources: ["[[AI LABS - Types of Claude Loops Explained]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]"]
tools: ["[[Claude Code]]"]
tags: [topic/loops, topic/verification, topic/claude-code, topic/permissions, topic/planning, topic/automation]
---

# Tests-First Goal Loop

> **Provenance.** Points with a timestamp link come from the named video. The prompts, CLAUDE.md block, goal conditions, hook script and settings below are **original vault starter content**. None was shown in any video (AI LABS keeps its files in a paid community). Claude Code behaviour (`/goal`, hooks, permissions, checkpoints) is verified under **Beyond the source**.

## Goal

A stateless loop in [[Claude Code]] with four parts:

1. You (or a separate session) write the tests first.
2. You set a `/goal` whose completion condition is that suite passing.
3. Every working version gets checkpointed in git.
4. You leave it running and review the result afterwards.

This is the combination [[AI LABS - Types of Claude Loops Explained]] recommends for the stateless loop:

- Tests written before Claude builds the feature ([02:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=174s), [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s)).
- A goal of passing them all ([03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)).
- A CLAUDE.md line telling Claude to save each working version so it can roll back ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s), [03:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=221s)).

The vault version adds two things. A constraint and a hook stop Claude passing by editing the tests, and a git commit on every green turn backs up the CLAUDE.md rule.

## Use when

- **The requirements can be checked concretely.** AI LABS says `/goal` works best on features whose requirements can be verified in some hard way ([02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s)).
- **The feature touches existing code you don't want broken.** With tests covering existing features, the agent can work alone without breaking them ([03:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=187s)).
- **You want to walk away.** The agent works unattended, which is why the rollback rule matters ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)).
- **Your plan has room for it.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] rates `/goal` B tier on lower plans and A tier with high limits ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).

**Don't use it for:**

- Work with no hard check, such as visual polish or copy. Use a reviewer or rubric loop instead: [[Multi-Agent Review and Scoring Loops]].
- Tiny fixes you could describe in one line. Just ask.
- Large multi-part builds where the agent starts skipping parts late in the session. AI LABS later found that completion loops hold in a fresh context but falter deep into real work ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)). See [[Evidence-Gated Completion Ledger]].

## What the sources say

| Point | Source | Timestamp |
|---|---|---|
| `/goal` is the clearest stateless loop: type what you want after the command and Claude adopts it as the goal | [[AI LABS - Types of Claude Loops Explained]] | [02:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=137s) |
| When the agent thinks it's done, a smaller model (Haiku) checks the work against the requirements and reprompts if anything is missing | AI LABS | [02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s), [02:38](https://www.youtube.com/watch?v=8wsM0euQOvc&t=158s) |
| Weakness: a model decides completion with no standard to measure against | AI LABS | [02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s) |
| Tests first; failing tests tell Claude its implementation is off | AI LABS | [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s), [03:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=182s) |
| Set the goal as the feature passing every test; Claude codes, reruns the tests and marks the goal complete when all pass | AI LABS | [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s), [03:22](https://www.youtube.com/watch?v=8wsM0euQOvc&t=202s) |
| Add one CLAUDE.md line to save every working version, so it rolls back rather than undoing from memory | AI LABS | [03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s), [03:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=221s) |
| If Claude implements first, its tests just pass its own code; write the tests first | [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] | [09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s), [09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s) |
| Test only what matters; strong models over-test and bloat the codebase | The Coding Sloth | [09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s) |
| Have Claude run type checkers and linters before calling a task done | The Coding Sloth | [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s) |
| Example goal: every test passes and there are no type errors; Claude keeps going until it succeeds or needs you | The Coding Sloth | [19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s), [19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s) |
| `/goal`'s judge reads the conversation, not the work, so it can drift from what you needed | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s) |
| Prefer explicit allow and deny rules to skipping permissions, for safe autonomy | [[Nate Herk - 32 Tricks to Level Up Claude Code]] | [14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s), [14:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=855s) |

## Prerequisites

- **Claude Code with `/goal`.** It follows the same workspace-trust rule as hooks, and is unavailable if hooks are disabled (Beyond the source).
- **A git repository.** Start from a clean working tree and create a dedicated branch for the run.
- **A test runner** that exits non-zero on failure, ideally plus a type checker and linter ([09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)).
- **A way to run unattended:**
  - auto mode, which needs a supported model and can be turned off by your organization (it's the built-in starting mode on Pro, Max and Team); or
  - an allowlist that covers the test, lint and git commands.

  Manual mode stalls on the first unapproved command (Beyond the source).
- **A written spec** for the feature, e.g. `docs/specs/<feature>.md`. Planning first helps; see [[Plan-First Workflow]].
- `jq` is **not** needed. The hook below is plain bash and git.

## Steps

1. **Pick one feature with checkable requirements** ([02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s)). One goal per feature. Split anything that needs more than roughly 25 turns (vault heuristic).
2. **Branch.** Run `git switch -c goal/<feature>` from a clean tree.
3. **Write the tests first, in a separate session.** Use the test-writing prompt below, or write them yourself.
   - Cover the new behaviour's edge and error cases.
   - Make sure the existing features' tests still pass ([03:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=187s)).
   - Test only what matters ([09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)).
4. **Check that the new tests fail for the right reason.** "Feature missing" is right; import errors and typos are not. Existing tests should stay green.
5. **Freeze the spec.** Commit the tests, then tag the commit: `git commit -m "tests: <feature> (failing)"` and `git tag goal-baseline`.
6. **Add the checkpoint rule to CLAUDE.md** using the block below. It's the video's "save every working version" line ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)), made concrete with git.
7. **Back the rule with a hook.** Add `.claude/hooks/checkpoint-on-green.sh` and the `Stop` hook entry below. Every time Claude finishes a turn, the hook:
   - refuses to let it stop if a baseline test file was changed or deleted;
   - commits when the suite is green.

   CLAUDE.md text is guidance; a hook always runs (Beyond the source).
8. **Protect the tests and set permissions.** Add the settings below: allow the test, lint and read-only git commands, and deny edits under `tests/`. Add this *after* step 5, or it blocks you writing the tests.
9. **Pick the permission mode.** Start the run in auto mode (`claude --permission-mode auto`), or rely on the allowlist. Keep `--dangerously-skip-permissions` for a container or VM (Beyond the source; Nate's warning at [14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)).
10. **Start a fresh session and set the goal.** Paste a condition from the templates below. It has four parts:
    - one measurable end state;
    - the command that proves it;
    - the constraint that tests stay untouched;
    - a turn cap.

    Setting the goal starts work immediately.
11. **Leave it running and check in occasionally.**
    - `/goal` with no argument shows turns, elapsed time, token spend and the evaluator's latest reason. `Ctrl+O` shows the reason behind each verdict.
    - `/goal clear` stops it.
12. **Review when it resolves.** Run the review prompt below in a *fresh* session:
    - confirm no baseline test changed;
    - run everything yourself;
    - compare against the spec for requirements the tests don't cover.

    Then squash the checkpoint commits if you want one clean commit. For a deeper pass, run the verification loop in [[Multi-Agent Review and Scoring Loops]].

## Starter files & prompts

*All vault starter content, written for this note.*

### Folder layout

```text
your-project/
├── CLAUDE.md                          # + "Unattended goal runs" block
├── docs/specs/<feature>.md            # what the feature must do
├── tests/                             # written first, tagged goal-baseline
└── .claude/
    ├── settings.json                  # Stop hook + permission rules
    └── hooks/
        └── checkpoint-on-green.sh     # test guard + commit on green
```

### Prompt 1: write the tests first (separate session, before the goal)

```text
We're adding <feature> described in docs/specs/<feature>.md. In this session, write tests only. Do not write or change any implementation code.

1. Read the spec and the existing tests in tests/ so you follow our conventions and helpers.
2. List the behaviours the feature must have, including edge cases and error handling. Ask me about anything the spec leaves ambiguous before writing tests.
3. Write tests for the behaviours that matter. Don't test every line or private helper.
4. Run the full test command and show me the output. The new tests must fail because the feature is missing, not because of import errors, typos or missing fixtures. Existing tests must still pass.
5. Finish with a table mapping each spec requirement to the test(s) that cover it, and list any requirement you couldn't express as a test.
```

### CLAUDE.md block: unattended goal runs

```markdown
## Unattended goal runs
- Only work on the current goal/* branch. Never push, merge, rebase or rewrite history.
- The tests that existed at tag `goal-baseline` are the spec. Never edit, skip, delete or weaken them to get green. If one looks wrong, stop and explain why.
- After any change that leaves the test command green, commit it: `git commit -am "checkpoint: <what now works>"` (add new files explicitly). The Stop hook also commits green states.
- If a change breaks tests that were passing, don't undo it from memory. Find the last checkpoint with `git log --oneline` and restore the affected files with `git restore --source=<sha> -- <paths>`.
- End every turn by running the test command (and the type check and lint) and showing their real output.
```

### Goal condition templates

JavaScript or TypeScript project:

```text
/goal `npm test` exits 0 with 0 failing tests, `npx tsc --noEmit` exits 0, and `npm run lint` exits 0, with each command's real output shown in your final message this turn. Constraint: `git diff --name-only --diff-filter=MD goal-baseline -- tests` prints nothing (no baseline test modified or deleted). Or stop after 25 turns and report which tests still fail and why.
```

Python project:

```text
/goal `pytest -q` exits 0 with no failures or errors, `mypy src` exits 0, and `ruff check .` exits 0, each command's output shown in your final message. Constraint: no file under tests/ that existed at tag goal-baseline is modified or deleted (check with git diff against goal-baseline). Or stop after 25 turns and list what's still failing.
```

### `.claude/hooks/checkpoint-on-green.sh`

Make it executable with `chmod +x .claude/hooks/checkpoint-on-green.sh`.

```bash
#!/usr/bin/env bash
# Vault starter. Runs as a Stop hook each time Claude finishes a turn.
#  1) Blocks the stop if baseline test files were modified or deleted.
#  2) Commits a checkpoint when the test command passes and there are changes.
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

TEST_CMD="${GOAL_TEST_CMD:-npm test --silent}"   # e.g. export GOAL_TEST_CMD="pytest -q"
TEST_DIR="${GOAL_TEST_DIR:-tests}"
BASELINE="${GOAL_BASELINE_TAG:-goal-baseline}"

# Only act on goal branches.
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null) || exit 0
case "$branch" in goal/*) ;; *) exit 0 ;; esac

# 1) Test guard: compare the working tree with the baseline tag.
if git rev-parse -q --verify "refs/tags/$BASELINE" >/dev/null; then
  touched=$(git diff --name-only --diff-filter=MD "$BASELINE" -- "$TEST_DIR")
  if [ -n "$touched" ]; then
    echo "Baseline tests were changed: $touched. Restore them with 'git restore --source=$BASELINE -- <file>' and fix the implementation instead." >&2
    exit 2   # Stop hook: exit 2 blocks stopping and sends this message to Claude
  fi
fi

# 2) Checkpoint on green.
[ -z "$(git status --porcelain)" ] && exit 0
if bash -c "$TEST_CMD" >/dev/null 2>&1; then
  git add -A
  git commit -q -m "checkpoint: tests green on $branch" || true
fi
exit 0
```

### `.claude/settings.json`

Merge these keys into your existing settings file.

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/checkpoint-on-green.sh",
            "timeout": 600
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "Bash(npm test *)",
      "Bash(npx tsc *)",
      "Bash(npm run lint *)",
      "Bash(git status *)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git commit *)",
      "Bash(git restore --source *)"
    ],
    "deny": [
      "Edit(/tests/**)",
      "Bash(git push *)",
      "Bash(git reset --hard *)"
    ]
  }
}
```

### Prompt 2: review after the goal resolves (fresh session)

```text
Review the work on this branch since tag goal-baseline. Don't change any code yet.
1. Show `git log --oneline goal-baseline..` and `git diff --stat goal-baseline`.
2. Confirm no file under tests/ that existed at goal-baseline was modified or deleted.
3. Run the test suite, the type checker and the linter and show the output.
4. Read docs/specs/<feature>.md and list any requirement that the implementation doesn't meet or that no test actually exercises.
5. Look for implementation shortcuts that make tests pass without doing the real work (hard-coded values, special-casing test inputs, swallowed errors).
Report only issues that affect correctness or the spec. Rank them.
```

## Done when

- [ ] New tests were committed and tagged `goal-baseline` **before** any implementation. They failed for the right reason, and existing tests passed.
- [ ] CLAUDE.md has the unattended-run block. The Stop hook and permission rules are in `.claude/settings.json`, and `/hooks` lists the hook.
- [ ] The goal condition names the commands, the no-test-edits constraint and a turn cap.
- [ ] The goal resolved as **met**, and the transcript shows the real test output in the final turn.
- [ ] `git log goal-baseline..` shows checkpoint commits.
- [ ] `git diff --diff-filter=MD goal-baseline -- tests` is empty.
- [ ] In a fresh session you ran the tests, type check and lint yourself, all green. You checked the spec for requirements the tests miss.
- [ ] You looked at `/goal` status for turns and token spend, and decided whether the run was worth it for this size of feature.

## Pitfalls

- **Weak tests get gamed.** The loop is only as good as its judge. If tests assert little or hard-code happy paths, "all green" means little. That's the gap [[AI LABS - The Unlazy Skill for Lazy Agents]] points at: the `/goal` judge reads what the conversation says, not the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)). Cover edge and error cases, and do the post-run check for shortcuts.
- **Tests written after the code.** They end up shaped to the implementation ([09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)). Keep test writing in its own session, before the goal.
- **Claude edits the tests to pass.** You have four defences here: the condition's constraint, the `Edit(/tests/**)` deny rule, the hook's baseline diff and your review. Deny rules don't stop a script that writes files indirectly, which is why the hook diffs against git (Beyond the source).
- **Over-testing.** Strong models test everything, which bloats the codebase and slows every loop turn ([09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)).
- **Token burn.**
  - `/goal` suits bigger plans ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).
  - Always include a turn cap, keep one feature per goal, and watch token spend in `/goal` status.
  - A flaky test can keep the loop spinning. Fix or quarantine flaky tests before the run.
- **The judge can't see what wasn't printed.** The evaluator doesn't run commands or read files. If Claude doesn't show real test output, the verdict rests on Claude's claims (Beyond the source). Hence the CLAUDE.md line about ending each turn with real output.
- **CLAUDE.md rules aren't enforcement.** The video's safeguard is one CLAUDE.md line ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)), but CLAUDE.md is guidance. Built-in checkpoints (`/rewind`) don't capture bash changes and usually don't restore subagent edits, which is why the hook commits to git.
- **Blanket rollbacks get blocked.** Auto mode's classifier blocks commands like `git restore .` or `git reset --hard` by default, because they discard uncommitted work. Tell Claude to restore specific paths from a checkpoint SHA, as in the CLAUDE.md block (Beyond the source).
- **The hook commits junk.** `git add -A` stages every untracked file. Run on a dedicated branch with a proper `.gitignore`, and squash or amend before merging.
- **Stalls and stuck hooks.**
  - If Claude answers the evaluator without using tools for several turns, Claude Code stops the loop and hands control back.
  - Claude Code also overrides a Stop hook after 8 consecutive blocks. If the test guard keeps firing, a person needs to look.
- **Long-session laziness.** Completion loops weaken as context fills ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)). Start the goal in a fresh session and keep the feature small.

## Variations

- **Two-Claude TDD.** One session writes the tests (Prompt 1) and a different session implements under the goal. Anthropic's guide suggests the same split (Beyond the source).
- **Deterministic judge instead of `/goal`.** Drop `/goal` and make the Stop hook run the test command itself, exiting 2 while it fails. No model judges completion. Guard against endless loops with the block cap (Beyond the source).
- **Headless run.** `claude --permission-mode auto -p "/goal <condition>" --output-format stream-json --verbose` runs the goal to completion in one call, printing progress as it streams (Beyond the source).
- **Ralph plugin.** `/ralph-loop "<task>" --completion-promise "DONE" --max-iterations 20` gives a marker-based loop. It's weaker than tests as a judge, as AI LABS notes ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)).
- **Isolated worktree per goal.** Run the goal in its own worktree so you can keep working in the main checkout. [[Nate Herk - 32 Tricks to Level Up Claude Code]] launches these with `claude --worktree <name>` ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)). See [[Parallel Sessions with Git Worktrees]].
- **Evidence gates for multi-part features.** Swap the single test condition for a gates ledger. Each outcome gets its own check command and recorded evidence, and the parent re-runs checks from subagents ([07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s), [08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)). See [[Evidence-Gated Completion Ledger]].
- **Visual checks for front end.** Add a screenshot or browser pass as a later step, as in Nate's screenshot loop ([09:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=559s)). Keep it outside the goal condition unless you have visual-regression tests that print a pass or fail result.

## Sources

- [[AI LABS - Types of Claude Loops Explained]]: the stateless loop, the `/goal` mechanism as they describe it, tests first and the rollback rule ([01:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=104s)–[03:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=226s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: tests first, test what matters, type checks and linters ([09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=575s)); the `/goal` example and tier rating ([19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s)–[19:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1169s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: why a transcript-reading judge and late-session runs are weak points ([03:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=215s)–[04:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=261s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: allow and deny lists instead of skipping permissions ([14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)); worktrees ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)).

## Beyond the source

*Not from the videos. Each item was checked at the linked page on 2026-09-15.*

- **How `/goal` works (it dates from mid-2026; this is current behaviour).**
  - **Setting a goal.** `/goal <condition>` sets a session-scoped completion condition and starts a turn at once. There is one goal per session, and the condition can be up to 4,000 characters.
  - **How it's judged.** After *every* turn, the small fast model (Haiku by default on the Claude API) reads the condition and the conversation. It returns *not yet met* (Claude keeps going), *met* (the goal clears) or *impossible* (the goal clears as failed). The evaluator calls no tools, so write conditions that Claude's own output can prove, e.g. a test command's exit status.
  - **Writing a condition.** The docs recommend one measurable end state, a stated check, constraints, and a turn or time clause such as "or stop after 20 turns".
  - **Status and stopping.** `/goal` alone shows status. `/goal clear` (or stop, off, reset, none, cancel) removes it, and `/clear` does too.
  - **Resuming.** A goal still active when a session ended is restored on resume, with the turn count and timer reset.
  - **Headless.** It works in `claude -p`; add `--output-format stream-json --verbose` to see progress.
  - **Permissions.** It doesn't change permission mode, so use auto mode for unattended turns.
  - **Stalls.** If Claude replies for several turns without using tools, the loop stops with the goal still set.
  - **Errors.** Unrecoverable errors (auth, exhausted credits, a context overflow compaction can't fix, an unavailable model) clear the goal.
  - **Other failures.** Any other error leaves the goal set. In interactive sessions on recent versions, an overloaded server or dropped connection is retried automatically (up to three times), while a rate limit or usage limit pauses the goal until you prompt or the limit resets.
  - **Background work.** While subagents or background commands are running, evaluation waits for a turn with nothing running. If background work keeps the goal waiting for 30 minutes, Claude Code sends Claude a check-in; `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` changes the interval, and `0` turns check-ins and automatic retries off.
  - **Where it's available.** It follows the workspace-trust rule for hooks, and is unavailable when `disableAllHooks` is true or managed settings allow managed hooks only.
  - **Evaluator model.** Change it with `ANTHROPIC_DEFAULT_HAIKU_MODEL`. That also changes other small-model background tasks.

  Source: [Claude Code docs: /goal](https://code.claude.com/docs/en/goal).
- **`/goal`, `/loop` and Stop hooks compared.** `/goal` runs until the evaluator is satisfied, `/loop` fires on a time interval, and a Stop hook in settings runs your own script or prompt after every turn. `/goal` itself is a session-scoped prompt-based Stop hook. Source: [/goal](https://code.claude.com/docs/en/goal).
- **Stop hooks.**
  - For the `Stop` event, exit code 2 blocks Claude from stopping and passes stderr to Claude.
  - Hooks go under `hooks.Stop` in settings, and `$CLAUDE_PROJECT_DIR` points at the project root.
  - Claude Code overrides a Stop hook that blocks 8 times in a row without progress. Scripts can read `stop_hook_active` from the JSON input to avoid re-blocking, and `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises the cap.
  - `type: "agent"` Stop hooks, which can run the tests themselves, are experimental.

  Sources: [hooks guide](https://code.claude.com/docs/en/hooks-guide), [hooks reference](https://code.claude.com/docs/en/hooks).
- **Anthropic's verification ladder.** The best-practices guide says to give Claude a runnable check and then choose how hard it gates the stop: in the prompt, as a `/goal` condition, as a Stop hook, or with a verification subagent. It tells Claude to show evidence rather than assert success, and suggests one Claude writing tests while another writes code to pass them. It also says CLAUDE.md is advisory while hooks are deterministic. Source: [best practices](https://code.claude.com/docs/en/best-practices).
- **Permission rules.**
  - Rules are evaluated deny, then ask, then allow.
  - `Bash(npm test *)` also matches a bare `npm test`.
  - `Edit(/tests/**)` in project settings is anchored to the working directory. Edit deny rules also cover recognised bash file commands and redirections, but not scripts that write files indirectly; use the sandbox for OS-level enforcement.

  Source: [permissions](https://code.claude.com/docs/en/permissions).
- **Permission modes.**
  - Auto mode has a classifier review actions instead of prompting, and is the default starting mode on Pro, Max and Team when requirements are met. By default the classifier blocks commands it presumes would discard uncommitted work, such as `git reset --hard`, `git restore .` and `git clean -fd`.
  - `bypassPermissions` (`--dangerously-skip-permissions`) is intended for isolated containers and VMs only.

  Source: [permission modes](https://code.claude.com/docs/en/permission-modes).
- **Checkpoints aren't version control.** `/rewind` restores only edits made through Claude's file tools. Bash changes aren't tracked, and most subagent edits aren't restored. The docs say to keep using git. Source: [checkpointing](https://code.claude.com/docs/en/checkpointing).
- **Ralph.** Geoffrey Huntley's original is a shell loop re-feeding one prompt file, with tests as backpressure ([ghuntley.com/ralph](https://ghuntley.com/ralph/)). Anthropic's `ralph-wiggum` plugin uses a Stop hook with `--completion-promise` and `--max-iterations` ([README](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md)).

## Related

- Concepts: [[Loop Engineering]] · [[Verification Before Done]] · [[Agent Laziness]] · [[Permissions and Approval Gates]] · [[Plan Before Executing]] · [[CLAUDE.md as a Router]]
- Techniques: [[Build Verification into Every Task]] · [[Multi-Agent Review and Scoring Loops]] · [[Evidence-Gated Completion Ledger]] · [[Configure Safe Autonomy Permissions]] · [[Plan-First Workflow]] · [[Parallel Sessions with Git Worktrees]] · [[Keep CLAUDE.md Lean]]
- Tools and people: [[Claude Code]] · [[AI LABS]] · [[The Coding Sloth]] · [[Nate Herk]]
- [[Home]]
