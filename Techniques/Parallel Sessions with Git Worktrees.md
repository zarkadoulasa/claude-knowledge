---
type: technique
goal: Run several Claude Code sessions on one repository at the same time, each in its own git worktree (separate folder and branch), then merge the results back without any session overwriting another
difficulty: intermediate
time_to_build: 15 minutes to prepare the repo once; about a minute per extra session
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Anthropic - What Is Claude Managed Agents]]"]
tools: ["[[Claude Code]]"]
tags: [topic/claude-code, topic/subagents, topic/agents, topic/context]
---

# Parallel Sessions with Git Worktrees

## Goal

Keep two to five Claude Code sessions busy on one project at once without them colliding. Each session gets its own folder and branch. You merge the finished branches back one at a time and remove the worktrees afterwards.

- **The problem.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] points out that two sessions working in the same folder can overwrite each other's work ([10:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=639s)–[10:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=647s)).
- **The fix.** A worktree works like a parallel copy of the project on its own branch, but costs far less than copying the folder ([10:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=648s)–[11:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=660s)).
- **The habit.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] makes it a default: every chat gets its own worktree, so agents can't interfere with one another ([20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s)–[20:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1256s)).

## Use when

- **You have independent tasks.** Two or more tasks (a feature, a bug fix, a spike) could run at the same time instead of one after another ([20:48](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1248s)–[20:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1252s), Coding Sloth).
- **You want to keep working.** A long goal or build runs in its own session while you work in the main checkout. See [[Tests-First Goal Loop]].
- **You're comparing approaches.** Several attempts or skills tackle the same brief and must not share files.

**Skip it** when the tasks edit the same files, or when one task depends on another's output. Run those one after another, or use a single session with subagents (see [[Subagents and Agent Teams]]). Skip it too if your plan's limit can't cover several full conversations at once (see Pitfalls).

## Prerequisites

- Claude Code installed, and a git repository with **at least one commit** (see Beyond the source).
- Comfort with basic git: branches, merge, resolving a conflict.
- Your project's setup command (for example `npm ci`, `uv sync`) and test command.
- If the app runs a dev server or a local database, a free port and a database name for each worktree.

## Steps

### A. Prepare the repository (once)

1. **Check the repo is ready.** Make sure `git log` shows at least one commit. Run `claude` once in the repo root and accept the workspace-trust prompt, because `--worktree` exits with an error in an untrusted folder *(docs; Beyond the source)*.
2. **Ignore the worktree folder.** Add `.claude/worktrees/` to `.gitignore` (starter 1). Otherwise worktree contents show up as untracked files in your main checkout *(docs)*.
3. **Carry over gitignored config.** A worktree is a fresh checkout, so `.env`-style files aren't there. List them in `.worktreeinclude` (starter 2) and Claude Code copies them into each new worktree *(docs)*.
4. **Add worktree rules to CLAUDE.md** (starter 3).
5. **Commit and push that setup.** By default a new worktree branches from the remote's default branch, not your local `HEAD`, so unpushed changes won't appear in it *(docs)*. To branch from local work instead, set `worktree.baseRef` to `"head"` (Variations).

### B. Split the work

6. **One task per worktree, with non-overlapping files.**
   - Write the tasks into a board (starter 4). Give each task an owned set of paths, a port and a database name.
   - This borrows the file map from [[AI LABS - The Unlazy Skill for Lazy Agents]]. Its plan records which files each task touches, so agents working at the same time don't overwrite each other ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s)–[11:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=714s)). Applying it to worktrees, to cut merge conflicts, is the vault's adaptation.
7. **Name each worktree after its task.** Nate passes the feature name to the command ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)).
   - *Vault convention:* `feat-<thing>`, `fix-<thing>`, `spike-<thing>`, lowercase with hyphens.
   - Claude Code creates the branch as `worktree-<name>` *(docs)*.
8. **Decide how many to run.**
   - Nate says three, four or five at once is workable ([11:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=671s)).
   - On a small plan, start with two. The Coding Sloth's warning about subagents, that each is a full conversation eating the same limit ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)), applies to parallel sessions for the same reason. That extension is the vault's.

### C. Launch the sessions

9. **Terminal 1:** `claude --worktree feat-login`. Claude creates an isolated workspace on its own branch ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)–[11:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=660s), Nate). Per the docs it lives in `.claude/worktrees/feat-login/` on branch `worktree-feat-login`.
10. **Terminal 2 and more:** run the same command with a different name ([11:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=662s)–[11:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=665s)). The Coding Sloth notes that Claude Code supports worktrees natively ([20:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1257s)).
11. **Set up each worktree's environment.** Have the session install dependencies, since `node_modules` and virtualenvs aren't shared. Start any server on the port from the board *(docs and Beyond the source)*.
12. **Paste the kickoff prompt** (starter 5) into each session, filled in from the board.

### D. While they run

13. **Keep sessions in their lanes.** If a session needs a file another task owns, stop it and re-split the work. Don't let two branches edit the same file.
14. **Check progress from the main checkout.**
    - `git worktree list` shows every worktree and its branch.
    - `git diff --stat main...worktree-feat-login` shows what a branch has changed so far (committed work only).
    - Swap `main` for your default branch name if it differs.

### E. Merge back

15. **Commit on each branch.** The kickoff prompt asks each session to commit on its own branch and not merge. Uncommitted work in a worktree won't come across in a merge.
16. **Merge one branch at a time from the main checkout.**
    - Nate merges the branches back like any other git branch, so all the work lands in the main project without clobbering files ([11:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=674s)–[11:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=682s)).
    - *Vault addition:* run the tests after each merge, not once at the end. Starter 6 does this and stops at the first conflict or failure. Or push each branch and open a pull request.
17. **Resolve conflicts in the main checkout.** Do it yourself, or in a fresh Claude session there that is told what both branches were meant to do.

### F. Clean up

18. **Exit each worktree session.**
    - If the worktree is clean, an unnamed session removes it and its branch automatically. A session you have given a session name asks first. The docs mean the session's name here, not the worktree name.
    - If there's work in it, Claude asks whether to keep or remove it. Removing deletes the directory, the branch and the work *(docs)*. Only remove after the merge.
19. **Sweep leftovers** with starter 7: `git worktree remove`, `git branch -d`, `git worktree prune`. This matters for worktrees from `claude -p` runs, which Claude Code never cleans up, and ones you made with `git worktree add` *(docs)*.

## Starter files & prompts

*Everything in this section is **vault starter content**, written for this note. None of it is quoted from the videos. Commands and file names were checked against the Claude Code and git docs (see Beyond the source).*

### 1. `.gitignore` line

```gitignore
# Claude Code worktrees live here; keep them out of the main checkout's status
.claude/worktrees/
```

### 2. `.worktreeinclude` (project root)

```text
# Gitignored files every new worktree needs. gitignore syntax; tracked files are never copied.
.env
.env.local
```

### 3. CLAUDE.md block

```markdown
## Parallel worktree rules
- If your working directory is under .claude/worktrees/, you are one of several parallel sessions.
- Edit only the paths your kickoff prompt says you own. If you need anything else, stop and ask.
- Never edit files in the main checkout, and never merge, rebase onto main, or push unless asked.
- Install dependencies inside this worktree before running anything.
- Start dev servers on the port you were given, and use the database name you were given.
- Commit to your own branch with clear messages. Report "done" only with the test output shown.
```

### 4. `parallel-board.md` (keep it in the main checkout, uncommitted)

```markdown
# Parallel board — <date>

| Worktree | Task (one outcome) | Owns (paths) | Port | DB / schema | Status |
|---|---|---|---|---|---|
| feat-login | Email + password login with tests | src/auth/, tests/auth/ | 3001 | app_feat_login | running |
| fix-cart-total | Cart total rounds to 2 decimals | src/cart/total.ts, tests/cart/ | 3002 | app_fix_cart | running |
| spike-search | Compare two search libraries, write notes | docs/spikes/search.md | none | none | running |

Shared files nobody may edit in parallel: package.json, lockfile, db/migrations/, CLAUDE.md
Merge order: fix-cart-total → feat-login → spike-search
```

### 5. Kickoff prompt (one per session)

```text
You are in worktree "<name>" on branch worktree-<name>, one of several parallel sessions.
Task: <one-sentence outcome>.
You own: <paths>. Don't change anything outside them; if you must, stop and tell me why first.
Setup: install dependencies here. Use port <port> for any server and database "<db>" for local data.
Done means: `<test command>` passes and <observable check>. Paste the command output as proof.
When done, commit on this branch. Do not merge, rebase, or push.
```

### 6. `merge-worktrees.sh` (run from the main checkout)

```bash
#!/usr/bin/env bash
# Vault starter: merge finished worktree branches one at a time, testing after each merge.
# Usage: MAIN=main TEST_CMD="npm test" ./merge-worktrees.sh worktree-fix-cart-total worktree-feat-login
set -euo pipefail
MAIN="${MAIN:-main}"
TEST_CMD="${TEST_CMD:-npm test}"

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Main checkout has uncommitted changes; commit or stash first." >&2
  exit 1
fi
git switch "$MAIN"

for branch in "$@"; do
  echo "== Merging $branch into $MAIN"
  if ! git merge --no-ff "$branch"; then
    echo "Conflict while merging $branch. Resolve it, commit, then re-run with the remaining branches." >&2
    exit 1
  fi
  echo "== Testing after $branch"
  if ! bash -c "$TEST_CMD"; then
    echo "Tests failed after merging $branch. Fix on $MAIN (or revert the merge) before continuing." >&2
    exit 1
  fi
done
echo "All branches merged and tests passing."
```

### 7. Cleanup commands

```bash
git worktree list                                  # what exists, and on which branch
git worktree remove .claude/worktrees/feat-login   # refuses if the worktree has uncommitted work
git worktree unlock .claude/worktrees/feat-login   # only if remove says it is locked
git branch -d worktree-feat-login                  # -d refuses unless the branch is merged
git worktree prune                                 # clear records of worktrees deleted by hand
```

## Done when

- [ ] `.claude/worktrees/` is gitignored, and `git status` in the main checkout stays clean while sessions run.
- [ ] At least two sessions started with distinct names, and `git worktree list` shows each on its own `worktree-<name>` branch.
- [ ] Each worktree has its dependencies and needed env files, and its tests run there.
- [ ] Any dev servers or local databases run side by side without port or data clashes.
- [ ] Every task branch is committed, and its tests passed inside its worktree.
- [ ] Branches were merged into the main branch one at a time, with tests passing after each merge.
- [ ] Merged worktrees and branches are removed, and `git worktree list` shows only the main checkout plus any you kept on purpose.
- [ ] No file in the main checkout was edited by a parallel session.

## Pitfalls

- **Running two sessions in one folder anyway.** This is the failure the technique exists to prevent ([10:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=643s)–[10:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=647s), Nate). Opening a second terminal in the same directory gives you no isolation.
- **Thinking a worktree is a full copy.**
  - The Coding Sloth describes it as copying the project into its own folder ([20:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1237s)–[20:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1242s)), while Nate stresses it's more efficient than a copy ([10:50](https://www.youtube.com/watch?v=jqoFP9QapXI&t=650s)–[10:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=653s)).
  - Per the docs, a worktree has its own tracked files and branch but shares the repository's history. Gitignored files such as `.env` and `node_modules` are missing until you copy or install them.
- **Shared runtime clashes.** Worktrees separate files, not processes. Two dev servers both on port 3000 collide. Worktrees also share the same local database, Docker daemon and caches, so parallel migrations or test data can corrupt each other. Give each worktree its own port and database name, or containers *(Beyond the source)*.
- **Overlapping files mean merge conflicts.** If two tasks touch the same files, or shared files like lockfiles and migrations, you pay at merge time. Split the ownership up front (steps 6 and 13).
- **Token and limit cost.** Each session is a full conversation. The docs note that parallel sessions multiply token use, and the Coding Sloth's point that parallel conversations can use up a $20 plan ([20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)) applies here too. Run fewer sessions on small plans.
- **A stale base.** New worktrees start from the remote default branch, so commits you haven't pushed are missing. Push first, or set `worktree.baseRef: "head"` *(docs)*.
- **Removing before merging.** Choosing "remove" on exit deletes the worktree's branch and uncommitted work *(docs)*.
- **Orphans from scripted runs.** `claude -p --worktree` runs have no exit prompt, so their worktrees stay on disk. Clean up with starter 7 *(docs)*.
- **Assuming agent teams get worktrees.** They don't. Teammates share one checkout, so split files by owner instead *(docs)*.

## Variations

- **Worktree per chat vs per feature.** The Coding Sloth gives every chat its own worktree as a daily habit ([20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s)). Nate files it under advanced tricks for pushing Claude Code hard, one worktree per feature ([10:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=630s), [10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)).
- **Other launch routes** *(docs)*:
  - **Desktop app.** Choose the worktree option when starting a session.
  - **By hand.** `git worktree add ../project-feat-a -b feat-a`, then `cd` in and run `claude`. Use this for an existing branch or a folder outside the repo.
  - **From local work.** Set `"worktree": {"baseRef": "head"}` in settings.
  - **For a pull request.** Run `claude --worktree "#1234"`. Keep the quotes, or your shell treats `#` as a comment.
- **Subagents, not sessions.** A custom subagent with `isolation: worktree` in its frontmatter runs in a temporary worktree. The bundled `/batch` skill splits a large change into worktree-isolated subagents that each open a PR *(docs)*. See [[Subagents and Agent Teams]].
- **One checkout, file-ownership map.**
  - [[AI LABS - The Unlazy Skill for Lazy Agents]] ran ten subagents in one project at once. Its plan assigned files per task, and a working first version took about two hours ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s)–[12:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=730s)).
  - This is lighter than worktrees but gives no write isolation. Current [[Unlazy]] itself recommends worktrees when outputs would collide *(Beyond the source)*.
- **Cloud analogue.** In [[Anthropic - What Is Claude Managed Agents]], each Kanban ticket starts its own session in its own container, and two tickets run in parallel ([01:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=93s)–[01:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=98s)). See [[Claude Managed Agents]].
- **Verification per worktree.** Give each session a tests-first goal so it proves its own branch before you merge. See [[Tests-First Goal Loop]] and [[Build Verification into Every Task]].

## Sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]], hack 23:
  - Advanced tier ([10:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=630s)); sessions in one folder overwrite each other ([10:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=639s)); worktree as an efficient parallel copy ([10:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=648s)).
  - `claude --worktree <feature>` in each terminal ([10:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=655s)–[11:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=669s)); three to five at once ([11:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=671s)); merge back like normal branches ([11:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=674s)–[11:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=682s)).
  - Captions render the command as "Claude dash dash work tree", which is `claude --worktree`.
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]:
  - Worktrees rated A tier, one folder per branch, good for parallel AI work ([20:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1232s)–[20:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1242s)).
  - Every chat a worktree, fully isolated ([20:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1246s)–[20:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1256s)); native support in Claude Code ([20:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1257s)).
  - Cost of parallel conversations, said of subagents ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: file ownership in the plan so parallel agents don't overwrite each other, then all agents at once ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s)–[12:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=730s)).
- [[Anthropic - What Is Claude Managed Agents]]: parallel sessions in separate containers ([01:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=93s)).

## Beyond the source

*Not from the videos. Checked on 2026-09-15 at the linked pages.*

- **`--worktree`.**
  - **What it creates.** `claude --worktree <name>` (or `-w`) creates `.claude/worktrees/<name>/` on branch `worktree-<name>`. Leave out the name and Claude makes one up.
  - **Requirements.** At least one commit, and workspace trust for interactive runs.
  - **Housekeeping.** Gitignore `.claude/worktrees/`.
  - **Mid-session.** Asking Claude to work in a worktree uses its `EnterWorktree` tool.

  <https://code.claude.com/docs/en/worktrees>, <https://code.claude.com/docs/en/common-workflows>
- **Setup and base branch.**
  - **Fresh checkout.** Install dependencies inside the worktree.
  - **`.worktreeinclude`.** Uses gitignore syntax and copies files that match and are gitignored. It works for `--worktree`, subagent and desktop worktrees, but not when a `WorktreeCreate` hook replaces git.
  - **`worktree.baseRef`.** Defaults to `"fresh"` (the remote default branch). If no remote is configured, or `origin/HEAD` can't be found or fetched, it falls back to your local `HEAD`. `"head"` uses your local `HEAD`. It can't be a branch name; create a worktree from an existing branch with `git worktree add`.
  - **PR worktrees.** `--worktree "#<n>"` or a PR/MR URL creates `.claude/worktrees/pr-<n>`.

  <https://code.claude.com/docs/en/worktrees>
- **Cleanup.**
  - **On exit.** A clean unnamed worktree and its branch are removed, and named sessions ask first. A worktree with work in it prompts keep or remove, and remove deletes the work.
  - **`-p` runs.** No prompt, so their worktrees stay until you remove them.
  - **Subagent worktrees.** Unchanged ones are removed when the subagent finishes. Ones with changes stay on disk. A periodic sweep removes Claude-created subagent and background-session worktrees older than `cleanupPeriodDays`, but only once they hold no uncommitted, untracked or unpushed work.

  <https://code.claude.com/docs/en/worktrees>
- **Sharing and isolation.**
  - **Shared with the main checkout.** `.git`, project-scope plugins and "don't ask again" Bash approvals.
  - **Blocked.** Edits and git commands aimed at the main checkout.
  - **Hooks.** `${CLAUDE_PROJECT_DIR}` stays at the launch directory, while `cwd` follows the worktree.

  <https://code.claude.com/docs/en/worktrees>
- **Git.** `git worktree add <path> -b <branch>`, `list`, `remove` (clean worktrees only, unless `--force`) and `prune`. One branch can't be checked out in two worktrees without `--force`. <https://git-scm.com/docs/git-worktree>
- **Other parallel options.** The docs compare subagents, agent view, agent teams and dynamic workflows. Worktrees isolate edits for sessions you run yourself. Agent teams don't use them, and parallel sessions multiply token use. <https://code.claude.com/docs/en/agents>, <https://code.claude.com/docs/en/agent-teams>
- **Runtime conflicts.** Worktrees isolate code, not the runtime. Default ports collide, and the local database, Docker daemon and caches are shared, so simultaneous database changes can race. Each worktree also needs its own install and `.env`. <https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents>
- **Unlazy leases.** Parallel leaves declare non-overlapping `OWNS:` paths. The repo calls this coordination, not write isolation, and points to worktrees for colliding output. <https://github.com/Leonxlnx/unlazy>

## Related

- **Concepts:** [[Subagents and Agent Teams]] · [[Context Window Management]] · [[Verification Before Done]] · [[Choosing a Claude Model]]
- **Techniques:** [[Tests-First Goal Loop]] · [[Plan-First Workflow]] · [[Context Hygiene Routine]] · [[Build Verification into Every Task]] · [[Evidence-Gated Completion Ledger]] · [[Configure Safe Autonomy Permissions]]
- **Tools:** [[Claude Code]] · [[Claude Managed Agents]] · [[Unlazy]]
- **People:** [[Nate Herk]] · [[The Coding Sloth]] · [[AI LABS]]
