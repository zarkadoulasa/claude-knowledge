---
type: tool
category: Open-source agent skill for completion discipline (depth-tree decomposition plus runnable gate ledgers)
website: https://github.com/Leonxlnx/unlazy
sources: ["[[AI LABS - The Unlazy Skill for Lazy Agents]]"]
tags: [topic/skills, topic/verification, topic/subagents, topic/loops, topic/claude-code, topic/portability, topic/agents]
---

# Unlazy

## What it is

Unlazy is an agent skill by [[Leon Lin]] (GitHub handle Leonxlnx, taken from the repo link in the video description). It targets [[Agent Laziness]], meaning agents that call unfinished work done ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s)) or quietly skip the hard part ([03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s)).

[[AI LABS - The Unlazy Skill for Lazy Agents]] sums up its promise this way: the skill doesn't tell you the agent is done, it proves it ([01:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=73s)). It does that by checking the work against a ledger where every item needs proof ([01:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=77s)). According to the video it works with [[Claude Code]], [[OpenAI Codex]] and other popular agents ([01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s)).

The video describes three mechanisms:

1. **A depth tree.** The task is split N layers deep, and each leaf becomes its own unit of work ([05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s), [06:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=362s)).
2. **A gates ledger (GATES.md).** It's written before any work starts ([07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s)). A checker, not the agent, fills in the evidence ([07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s)).
3. **Parent verification.** The main agent re-runs each subagent's checks before accepting its work ([08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s)).

The ledger idea works without the skill. See [[Evidence-Gated Completion Ledger]].

## How sources use it

### [[AI LABS - The Unlazy Skill for Lazy Agents]]

#### The depth tree

- **Split before working.** Given a large task, the skill splits it into smaller tasks, then splits those again, so the plan branches like a tree ([05:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=331s), [05:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=338s), [05:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=347s)). When the splitting stops, the video says each end task goes to its own subagent ([05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s)); per its own mode description below, that applies only in orchestrated mode, depth 4+ ([08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s)).
- **You choose the depth.** Put a number in the prompt: 5 means five rounds of breakdown and no more ([05:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=355s), [06:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=362s)). With no number, it picks the smallest depth that fits ([06:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=368s)).
- **Why split.** Each piece has one clear goal, and the agent working on it doesn't carry the rest of the job ([06:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=372s), [06:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=378s)).
- **Minimum leaf size.** Each leaf must be worth at least ten minutes of real work: a proper piece an agent can finish alone ([06:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=387s), [06:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=391s)).
- **Depth set too high.** If the leaves come out smaller than that, the video says the skill falls back to the default depth of three ([06:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=395s), [06:41](https://www.youtube.com/watch?v=c47uqR7XB_c&t=401s)). The repo says something different; see *Beyond the source*.

#### Solo vs orchestrated mode

| Mode | Depth | What happens | When |
|---|---|---|---|
| **Solo** (default) | 3 or under | Everything stays in one session, and the same agent works through it all | [06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s), [06:50](https://www.youtube.com/watch?v=c47uqR7XB_c&t=410s) |
| **Orchestrated** | 4 or more | Writes much more down: a plan file with the whole breakdown, plus a separate checklist for every task | [06:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=414s), [07:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=420s), [07:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=422s) |

#### The gates ledger

- **Why a file.** The earlier version fought laziness by telling the agent to be thorough ([07:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=428s), [07:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=432s)). But instructions are the first thing a long session loses ([07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s)). So this version writes requirements into a file before any work begins ([07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s)).
- **What a gate is.** Each gate is a checkbox next to one outcome that must be true before the task counts as done ([07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s), [07:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=452s)). Three lines sit under the outcome ([07:39](https://www.youtube.com/watch?v=c47uqR7XB_c&t=459s)):
  1. the command that proves it ([07:41](https://www.youtube.com/watch?v=c47uqR7XB_c&t=461s))
  2. the exact words that command must return ([07:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=465s))
  3. an evidence line that starts as "pending" ([07:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=467s))
- **The checker.** A bundled checker walks the file and runs every command itself ([07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s), [07:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=475s)). If the output has the expected words, it ticks the box and replaces "pending" with the part of the output that decided it ([07:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=479s), [08:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=481s)).
- **The pending rule.** A ticked box with "pending" still under it means the agent ticked it by hand ([08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s)). That counts as unmet, and worse than an empty box, because an empty box at least shows honestly where the work stands ([08:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=497s), [08:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=501s)).
- **The honest exit.** If a task proves impossible, the agent writes a line giving up that gate by name with a reason, and the line appears in the final report ([08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s), [08:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=533s), [08:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=535s)).

#### The parent verifies each leaf

- **Narrow briefs.** In orchestrated mode each task goes to a fresh agent that gets only the plan and its own gates file ([08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s), [08:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=511s)).
- **No trust on return.** When that agent says it's finished, the main agent runs the task's checks itself ([08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s)). Only then does it log a line in the plan file and hand out the next task ([08:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=522s)).
- **The claim.** The video presents Unlazy as a whole system rather than one final check, with no point where the agent decides the work is done ([08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s), [09:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=541s)).

#### One install for Claude Code and Codex

1. **Copy the command** from the install section of the repo ([09:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=550s), [09:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=552s)). Run it in a terminal inside your project ([09:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=557s)).
2. **Pick agents.** The installer first asks which agent you use ([09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s)).
   - Codex needs no change, because the skill goes into the `.agents` folder Codex already reads ([09:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=567s), [09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s)).
   - For Claude Code, select it from the menu ([09:34](https://www.youtube.com/watch?v=c47uqR7XB_c&t=574s)).
   - You can pick several agents at once ([09:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=576s)).
3. **Pick a scope:** this project only, or everything you build ([09:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=580s)). AI LABS chose project scope to test on one project first ([09:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=589s)).
4. **Accept the recommended options** ([09:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=595s)).
5. **Check the result.** Two new folders appear, `.agents` and `.claude`, and they aren't two copies ([09:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=598s), [10:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=603s)). The skill lives in `.agents`. The `.claude` entry is only a shortcut so Claude Code can use it without a duplicate ([10:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=607s), [10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s)). The skill file inside holds all the agent's guidance ([10:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=616s)).

The same one-copy idea applied to instruction files is in [[Tool-Agnostic Context Files]].

#### AI LABS' patch: parallel dispatch

- **The problem.** As shipped, the skill took a very long time to build anything meaningful ([10:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=629s)). Their test app ran for about 3–4 hours and produced only a login page ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s), [10:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=640s)).
- **The cause.** Claude Code and Codex can both run several subagents in parallel ([10:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=645s), [10:50](https://www.youtube.com/watch?v=c47uqR7XB_c&t=650s)). The skill instead handed out one task, waited for it to finish, and only then handed out the next ([10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s), [10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s)). That's where the hours went ([11:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=663s)).
- **The fix.** They had the agent edit the skill itself so it uses the tools' ability to run several agents at once ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s), [11:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=672s)). The prompt they used is shown only on screen, not in the narration ([11:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=668s)), and the refined skill they ran isn't published in the video ([12:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=748s)).
- **How the patched run goes.**
  1. Before building anything, it writes PLAN.md and then GATES.md ([11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s), [11:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=703s)).
  2. PLAN.md says which files each task works on, so agents running at the same time don't overwrite each other ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s), [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s)).
  3. It lays the foundation, then hands work to agents running simultaneously ([11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s)).
- **Result.** Ten agents worked at once for nearly two hours ([12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s), [12:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=724s)). The output was a first version of the demo app with every feature working as they wanted ([12:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=726s), [12:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=728s)). That's asserted in the video, not demonstrated.

#### Running it

- **Syntax:** skill name, then the tree depth, then everything you want built ([11:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=678s)).
- **Depth:** 5 for their app built from scratch ([11:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=683s)), and 2 or 3 for a single feature ([11:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=689s), [11:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=691s)). A number that's too high gets lowered automatically ([11:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=696s), [11:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=698s)).
- **At scale:** pair it with a model router skill that sends mechanical work to a cheaper model and hard parts to a strong one, so you don't hit usage limits as soon ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s), [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s)). See [[Route Tasks to the Right Claude Model]].

## Notes

- **What to take from it (vault reading).** The part worth copying is the ledger rule: outcomes, checks and evidence exist before the work, and the worker never grades itself. The depth tree and subagent fan-out are for large builds. For a single feature, the solo mode the video describes as the default is enough.
- **Before copying AI LABS' patch,** compare it with the current repo. How upstream dispatch has changed since the video is under *Beyond the source*, and an old copy plus a home-made patch may diverge from it.
- **Caption fixes:** "Code X" → Codex; "Cloud Code" → Claude Code; "{dot} agents / {dot} Claude" → `.agents` / `.claude`; "plan.md / gates.md" → PLAN.md / GATES.md.

## Beyond the source

*Not from the video. Checked on 2026-09-15 at the linked pages. The repo moves quickly, so re-check before building.*

- **Repo basics.** MIT licence, created 2026-08-09, about 3.4k stars when checked. Its GitHub description names the Depth Tree as the core method. <https://github.com/Leonxlnx/unlazy>
- **Install.**
  - Command: `npx skills add Leonxlnx/unlazy`. The `-g` flag installs for your user instead of the project; `--all` targets every agent the CLI finds.
  - Manual install: clone into `~/.claude/skills/unlazy` (Claude Code) or `~/.codex/skills/unlazy` (Codex CLI).
  - Invocation: `/unlazy` where slash skills work (for example `/unlazy tree 5 <task>`), or `$unlazy` in Codex.
  - The checker and hook need Node 16 or newer and have no third-party runtime dependencies.

  <https://github.com/Leonxlnx/unlazy#install>
- **Current version.** The source targets **2.1.0**, which the README calls unreleased. There is no GitHub release or tag, and the README advises pinning an exact commit if you need an immutable install. The latest commit when checked was `1667149` (2026-09-03). The changelog dates the 1.0.0 (instructions only) and 2.0.0 (gates, checker, Stop hook) milestones to 2026-08-10. <https://github.com/Leonxlnx/unlazy/blob/main/CHANGELOG.md> · <https://github.com/Leonxlnx/unlazy/commits/main>
- **How the installer lays out folders.** The skills CLI installs at project scope by default. At project level Claude Code reads `.claude/skills/` and Codex reads `.agents/skills/`. The recommended interactive method symlinks each agent to one canonical copy, which is the shortcut the video describes. <https://github.com/vercel-labs/skills>
  - **Known bug.** Issue #1355, open when checked: a project-scope `-a claude-code` install writes `.agents/skills/` but not the `.claude/skills/` symlink, so Claude Code can't see the skill. Check the link exists after installing. <https://github.com/vercel-labs/skills/issues/1355>
- **Where the video and the current repo differ.**

| Video | Repo |
|---|---|
| A too-high depth drops to three ([06:41](https://www.youtube.com/watch?v=c47uqR7XB_c&t=401s)) | The SKILL.md from before the video said to back off one layer. The current method says to state the mismatch and use the closest honest decomposition. [SKILL.md at 40570e1](https://github.com/Leonxlnx/unlazy/blob/40570e1/SKILL.md) · [method.md](https://github.com/Leonxlnx/unlazy/blob/main/references/method.md) |
| Solo at depth 3 or under, orchestrated at 4 or more ([06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s), [06:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=414s)) | Same thresholds before the video (solo was also "roughly under half an hour"). The current SKILL.md drops the depth numbers: pick the smallest mode that fits, with solo for a focused one-session task and orchestrated for a build or deep review. [SKILL.md at 40570e1](https://github.com/Leonxlnx/unlazy/blob/40570e1/SKILL.md) · [SKILL.md](https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md) |
| The checker runs every command itself ([07:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=475s)) | Now:<ul><li>`--status` never executes anything.</li><li>A normal run only prints a command that hasn't been approved.</li><li>`--approve` executes, and `--reverify` re-runs gates that are already ticked.</li><li>A pass needs exit code 0 *and* an EXPECT match.</li><li>Evidence is bound to a SHA-256 digest of the gate definition.</li></ul>[README](https://github.com/Leonxlnx/unlazy#quick-start) |
| One task, wait, then the next ([10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s)) | The orchestration guide from before the video already allowed concurrent leaves with separate file ownership where the harness supports it. Commits on 2026-08-23 (`be703c5`, `b02276e`) made launch waves mandatory: every ready leaf is launched and recorded before the first wait. [Old orchestration.md](https://github.com/Leonxlnx/unlazy/blob/40570e1/references/orchestration.md) · [dispatch.md](https://github.com/Leonxlnx/unlazy/blob/main/references/dispatch.md) |
| PLAN.md maps tasks to files ([11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s)) | Each leaf ledger declares `OWNS:` paths and claims them with `--claim`, which the repo calls coordination, not isolation. PLAN.md has a dispatch table with Owns, Needs, Tier, Planned wave and State. Pipelines live under `.unlazy/<scope>/`. [SKILL.md](https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md) |
| Give up a gate by name with a reason ([08:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=533s)) | `ABANDON: <id> <reason>` goes at column 1. The checker then exits 1 with `HANDOFF REQUIRED`, which is terminal but never counts as success. [gates.md](https://github.com/Leonxlnx/unlazy/blob/main/references/gates.md) |
| Add a model router skill ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)) | Already built in before the video: mechanical leaves could use a cheaper model. The current PLAN table has a `Tier` column (`judgment` or `mechanical`), mapped to a model only where the host offers that control. [PLAN template](https://github.com/Leonxlnx/unlazy/blob/main/templates/PLAN.md) |

- **Not mentioned in the video.**
  - **Stop hook.** An optional Claude Code Stop hook (`node <skill-dir>/scripts/install-hooks.mjs`, removed with `--uninstall`) blocks the end of a turn while gates are unmet or launch waves are incomplete. It doesn't run checks itself, and it lets go after six blocks with no progress. It writes `.claude/settings.local.json` by default. The skill says to install it only with the user's consent.
  - **Linter.** `scripts/gate-lint.mjs` flags gates that can't fail.

  <https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md>
- **Security.** CHECK lines are shell code that runs with your environment, credentials and network access. The README says approving a command is consent, not a sandbox. Approvals are stored under `~/.unlazy/approved`, and gate files you inherit are untrusted. <https://github.com/Leonxlnx/unlazy#security-boundary> · See [[Permissions and Approval Gates]].
- **Parallel launch per agent** (from dispatch.md).
  - *Claude Code:* launch each leaf as a background Agent task, or use a Dynamic Workflow for a large fan-out.
  - *Codex:* call `spawn_agent` once per leaf and call `wait_agent` only after the wave is sealed.

  <https://github.com/Leonxlnx/unlazy/blob/main/references/dispatch.md>

## Related

- **Concepts:** [[Agent Laziness]] · [[Verification Before Done]] · [[Agent Skills]] · [[Subagents and Agent Teams]] · [[Loop Engineering]] · [[Context Window Management]] · [[Build vs Install Third-Party Skills]] · [[Tool-Agnostic Context Files]] · [[Permissions and Approval Gates]]
- **Techniques:** [[Evidence-Gated Completion Ledger]] · [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Parallel Sessions with Git Worktrees]] · [[Route Tasks to the Right Claude Model]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]]
- **People:** [[Leon Lin]] · [[AI LABS]]
- **Source:** [[AI LABS - The Unlazy Skill for Lazy Agents]]
- [[Home]]
