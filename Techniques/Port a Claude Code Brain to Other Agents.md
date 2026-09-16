---
type: technique
goal: Make one plain-markdown second brain built for Claude Code readable and correctly routed from OpenAI Codex, Hermes Agent and other agent tools, including its skills and, when an agent runs on another computer, its files, without maintaining separate brains
difficulty: beginner
time_to_build: 30-90 minutes; add about an hour for the skills and cross-machine extensions (estimates, not from the videos)
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Build Skills Instead of Agents]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]", "[[Hermes Agent]]", "[[Obsidian]]", "[[Unlazy]]", "[[Syncthing]]"]
tags: [topic/portability, topic/second-brain, topic/agents, topic/claude-code, topic/memory, topic/skills]
---

# Port a Claude Code Brain to Other Agents

## Goal

One brain, many agents. The same folders, routing rules and memory should give the same answers whether you ask in [[Claude Code]], [[OpenAI Codex]] or [[Hermes Agent]]. [[Nate Herk]] mostly talks about Claude Code, but stresses that the approach works with any AI model ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)). He uses his second brain with Codex ([01:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=107s)) and Hermes Agent ([01:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=108s)). Different agent tools can share it because it's only files and folders ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)). See [[Tool-Agnostic Context Files]].

Two optional extensions come from newer sources:

- **Extension A: skills.** Share each skill from one installed copy that every agent reads. From [[AI LABS - The Unlazy Skill for Lazy Agents]] ([10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- **Extension B: another computer.** Get the brain onto the machine where an always-on agent runs. From [[Jay E - The ARMS Framework for a Claude Agentic OS]] ([17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)).

## Use when

- You already have a Claude Code brain (see [[Build a Level 1 Second Brain]]) and want to use it from a second agent tool.
- You want the brain to be tool-agnostic, which he names as a goal ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s)).
- You want some work to stay away from Anthropic. Anything Claude processes isn't private ([21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s)). For sensitive data he suggests open-source models, and says Claude Code maybe shouldn't hold the brain with everything in it ([21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)). Our inference: a portable brain makes that split possible.
- You want an always-on agent reading the same brain. He's been trying [[GBrain]] (by [[Garry Tan]]) with his Hermes agent ([25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s)) and thinks the pairing works well ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)). See [[Always-On Brain OS]].
- You use skills in more than one agent and want a single copy of each. The Unlazy installer can target several agents in one pass and keeps the real copy in `.agents` ([09:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=578s), [10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)). See Extension A.
- An agent runs on a different computer, such as an always-on Hermes on a cloud machine, and needs the skills and memory files from your Claude Code workspace ([17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s)). See Extension B, and the full build in [[Sync a Workspace to an Always-On Cloud Agent]].

## What the video says

| Point | Detail | Timestamp |
|---|---|---|
| Plain files are what make it portable | His real project, Herk2, is just markdown files organised so both he and his agents understand them | [01:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=70s), [01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s) |
| Keep it simple | Even at Level 4 the layout is still regular folders and plain markdown. His phrase: "boring is beautiful" | [23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s) |
| Codex's router file | Codex users start with AGENTS.md where Claude Code users start with CLAUDE.md | [04:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=263s) |
| What's Claude Code-specific | The CLAUDE.md file name, and the memory file Claude Code keeps updated on its own | [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s) |
| Option A: copy | To move to Codex, copy CLAUDE.md to a file named AGENTS.md | [11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s), [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s) |
| Herk2 uses both | Herk2 keeps a CLAUDE.md and an AGENTS.md, and they're essentially identical: one is read by Codex, the other by Claude Code | [11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s), [11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s) |
| Option B: reference | Inside CLAUDE.md you can reference AGENTS.md with `@` and delete the duplicated text, because the reference pulls that file in | [22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s), [23:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1381s), [23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s) |
| Memory needs a route | Claude Code maintains auto memory itself. Make sure the memory file exists, then tell Codex to look there for memories | [11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s), [11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s), [11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s) |
| The principle | Porting is a routing problem | [11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s) |
| Auto memory toggle | Claude Code's `/memory` command shows whether auto memory is on and lets you switch it | [10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s), [10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s) |
| Other readers of the same files | Obsidian only visualises the same markdown files. Reading this as a sign the files aren't tied to one tool is our inference | [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s) |
| Why Hermes for always-on | You can run GBrain in Claude Code, but you'd have to set up the scheduled cron jobs yourself | [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s) |
| Level 5 and multiple agents | If you run agents "offline" (as captioned, likely meaning unattended), have lots of data and want several Hermes agents synced, he says you're probably looking at Level 5 | [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s) |
| The real test | A good brain handles a vague question by knowing where to look and in what order | [28:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1714s), [28:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1717s) |

The table above is all from [[Nate Herk - Every Level of a Claude Second Brain]].

### What the newer sources add

| Point | Detail | Source | Timestamp |
|---|---|---|---|
| Import beats symlink | CLAUDE.md can import AGENTS.md, which saves keeping a symlink. He'd still prefer Claude to read AGENTS.md natively | [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] | [03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)–[03:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=222s) |
| Skills can cross agents | Unlazy is presented as working with Claude Code, Codex and other popular agents | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s) |
| One install, several agents | The installer asks which agent you use. Codex needs no change because the skill goes into `.agents`, which Codex reads. Tick Claude Code, and any others, in the same pass | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s)–[09:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=578s) |
| Scope | This project only, or everything you build. They chose project scope to test on one app first | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [09:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=580s)–[09:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=589s) |
| One copy, not two | `.agents` holds the skill. `.claude` holds a shortcut, so Claude Code sees it without a duplicate | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [10:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=601s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s) |
| Editing a shared skill | They changed the skill's own instructions so it runs subagents in parallel, which both Claude Code and Codex can do | [[AI LABS - The Unlazy Skill for Lazy Agents]] | [10:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=648s), [11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s) |
| Account-level skills | Skills added in Claude settings are available in Claude Design. The video says the same skills work in Claude Code and Codex, but doesn't show it | [[AI LABS - Claude Design Skills for Beautiful Sites]] | [00:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=52s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s) |
| Remote agents can't see local files | A Hermes agent on its own computer can't reach the skills and context you built up in Claude Code | [[Jay E - The ARMS Framework for a Claude Agentic OS]] | [17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s) |
| Sync the workspace | Install Syncthing on both computers, point it at the workspace, and share the skills and memory files you choose | [[Jay E - The ARMS Framework for a Claude Agentic OS]] | [17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s) |
| Or skip syncing | Claude Code, or Codex, on a VPS keeps all the files and context in one place | [[Jay E - The ARMS Framework for a Claude Agentic OS]] | [17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s) |
| Keep what you port small | Most people don't need AGENTS.md or CLAUDE.md, he argues, and a 1,000-line file costs about 7,000 tokens on every run | [[Ras Mic - How AI Agents and Claude Skills Work]] | [02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s), [04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)–[04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s) |

## Prerequisites

- A working brain with a CLAUDE.md router and plain markdown folders ([[Build a Level 1 Second Brain]]).
- The second agent installed (Codex, Hermes Agent, or similar).
- Nothing important locked in a tool-specific format. The brain should be only files and folders ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).

## Steps

1. **Check the brain is tool-neutral.** Content should be plain markdown in regular folders, with routing written as ordinary text ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s), [23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s)). List anything only Claude Code understands. The two he names are the CLAUDE.md file name and auto memory ([11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s)).
2. **Choose how to share the router.**
   - **A. Two copies**, as in Herk2: duplicate CLAUDE.md as AGENTS.md ([11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s)) and keep them identical ([11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s)).
   - **B. One source via reference**: put the content in AGENTS.md, and have CLAUDE.md reference it with `@AGENTS.md` so the duplicate text can go ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)–[23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s)).
   - *Recommended: B.* It leaves one file to edit, and the reference direction he shows (CLAUDE.md pulling in AGENTS.md) is the one that works in every tool. See "Import direction matters" under Beyond the source.
3. **Make AGENTS.md the router.** For option B, move the CLAUDE.md content into AGENTS.md and reduce CLAUDE.md to the reference line. Starter files and commands are below.
4. **Give memory a route.** Add a Memory section to AGENTS.md that tells every agent where the memory file lives and when to read it ([11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s)–[11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)). First check where Claude Code actually stores memory, which is outside your folder by default. See "Where Claude Code memory actually lives" under Beyond the source.
5. **Apply the per-tool settings** in Beyond the source → "Tool-specific setup (verified)".
6. **Run the same vague questions in both tools** (prompt set below). A good brain answers vague questions by knowing where to look and in what order ([28:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1717s)). Compare which files each agent opened, not just the wording of the answers.
7. **Fix differences by fixing routes.** If the second agent misses something, the route is missing or ambiguous ([11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)). Edit AGENTS.md (option B) or both files (option A), then test again. For a skill that falls apart in another compatible agent, [[Nate Herk - Build Skills Instead of Agents]] says to look for hidden assumptions, missing examples or instructions only one model understands, then tighten it and retest ([06:34](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=394s)); don't expect a weaker model to match a stronger one ([06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)).
8. **Maintain.** With option B, edit only AGENTS.md; Claude-only notes go under the reference line in CLAUDE.md. With option A, run the drift check below after every router edit.

### Extension A: share skills from one copy

Optional. Do this once the router works in both tools. Source: [[AI LABS - The Unlazy Skill for Lazy Agents]] unless noted.

9. **Pick the shared home.** Use `.agents/skills/` as the one real location, since Codex already reads `.agents` ([09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s)). Claude Code gets a link from `.claude/skills/` ([10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s)). Hermes can be pointed at the same folder (see Beyond the source).
10. **Install third-party skills once, for every agent.** Run the installer in the brain folder and tick every agent you use in the same pass ([09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s)–[09:38](https://www.youtube.com/watch?v=c47uqR7XB_c&t=578s)). To try it on one brain first, choose project scope, as AI LABS did ([09:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=589s)).
    - Read the skill before you install it. [[Ras Mic - How AI Agents and Claude Skills Work]] doesn't install other people's skills, partly because a download is an easy attack route ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)).
11. **Move your own skills into the shared folder.** Link each one back into `.claude/skills/` with `link-skills.sh` (under Starter files). This recreates the one-copy layout the installer produced ([10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
12. **Check the links.** Run `check-skills.sh` (under Starter files): every `.claude/skills/<name>` should resolve into `.agents/skills/`. Some project-scope installs skip the Claude Code link (see Beyond the source).
13. **Run each shared skill in every agent.** Use `/name` in Claude Code and `$name` in Codex (verified under Beyond the source). Compare the results, as in step 6.
14. **Edit the skill in one place.** When AI LABS wanted Unlazy to use parallel subagents, they edited the skill itself ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)). With a single copy, every linked agent picks up the change.

### Extension B: reach an agent on another computer

Optional. The full build, with ignore rules, conflict handling and security, is [[Sync a Workspace to an Always-On Cloud Agent]]. The short version, from [[Jay E - The ARMS Framework for a Claude Agentic OS]]:

15. **Give the always-on agent its own computer.** His Hermes agent runs on a computer in the cloud, which is what keeps it on 24/7 ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[16:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1012s)).
16. **Install Syncthing on both computers.** Point it at the workspace Claude Code works in ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1051s)).
17. **Choose what to share.** Include the skills and memory files the remote agent should use ([17:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1051s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)).
    - Before relying on memory, note that Claude Code's auto memory lives outside the workspace by default, so it won't sync unless you move it. See Beyond the source → "Where Claude Code memory actually lives".
18. **Point the remote agent at the synced copy.** Start it from the synced brain folder so it reads AGENTS.md. Add the synced `.agents/skills` to its skill folders (Hermes config under Starter files). These details come from the tool docs, not the video.
19. **Rerun the parity prompts** (step 6) on the remote agent.
20. **Or skip syncing.** Run Claude Code, or Codex, on a VPS, so the files and context already live where the jobs run ([17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)).

## Starter files & prompts

> [!note] Suggested starter content
> Everything in this section is original wording written for this vault. It is not his files. The design follows his two ideas: AGENTS.md as a copy of, or reference from, CLAUDE.md, and an explicit route to memory. The details come from the verified tool docs under Beyond the source.

### Target layout

This builds on the base tree in [[Build a Level 1 Second Brain]]. `memory/MEMORY.md` is the same memory path the vault's other starters route to.

```text
my-brain/
├── AGENTS.md            # the one real router (content lives here)
├── CLAUDE.md            # "@AGENTS.md" + Claude-only notes
├── .claude/
│   └── settings.json    # optional: autoMemoryDirectory → ~/my-brain/memory (must be absolute or ~/; see Beyond the source)
├── memory/
│   └── MEMORY.md        # memory index, reachable by every agent
├── decisions.md
├── context/
└── projects/
```

### `AGENTS.md` (tool-neutral router)

```markdown
# <Your name>'s Second Brain — Agent Router

Every agent working in this folder reads this file. Claude Code imports it through CLAUDE.md; Codex, Hermes Agent and others read it directly.
Plain markdown only. Don't use tool-specific syntax here, and write file paths without "@".

## Who I am
<Two or three lines.> Full background: `context/about-me.md`.

## How to work here
- Check the routing table before asking me for background.
- Open files by path when you need them. Don't read the whole folder.
- Name the file(s) you used in your answer.
- If something isn't in the brain, say so. Don't guess.

## Where things live
| Path | What's in it | Open it when |
|---|---|---|
| `context/about-me.md` | Who I am, goals, preferences | Anything about me |
| `context/stack.md` | Tools I use and what for | Tool or setup questions |
| `projects/priorities.md` | This quarter's priorities | Focus and planning |
| `projects/<name>/README.md` | One folder per project or client | A named project or client |
| `decisions.md` | Dated decision log | "Why / when did we decide…" |
| `memory/MEMORY.md` | Index of learned preferences and corrections | See Memory below |

## Memory
- Learned preferences, past corrections and working notes: `memory/MEMORY.md` (an index; each line points to a topic file in `memory/`).
  <!-- Replace with your real memory path. See "Where Claude Code memory actually lives". -->
- Read it before any task that depends on my preferences or earlier feedback.
- Claude Code updates this memory automatically. Other agents: don't rewrite it. Propose an addition, and append only after I confirm.

## Decision log
When I make a big change, append a dated entry to `decisions.md`: `## YYYY-MM-DD — <decision>`, then what changed and why. Append only.
```

### `CLAUDE.md` (single-source variant)

```markdown
@AGENTS.md

## Claude Code only
- Auto memory is on. Keep `MEMORY.md` as a short index and put detail in topic files.
- Anything that only makes sense in Claude Code goes in this section, never in AGENTS.md.
```

### One-time conversion (single-source variant)

```bash
cd ~/my-brain
cp CLAUDE.md CLAUDE.md.bak          # safety copy
mv CLAUDE.md AGENTS.md              # content now lives in AGENTS.md
printf '@AGENTS.md\n\n## Claude Code only\n' > CLAUDE.md
# Then edit AGENTS.md: remove Claude-only wording, add the Memory section,
# and remove "@" from any file paths written inside it.
```

### Drift check (two-copies variant)

```bash
cmp -s CLAUDE.md AGENTS.md && echo "in sync" || echo "DRIFT: CLAUDE.md and AGENTS.md differ"
```

### Parity prompt set

Run each prompt in a fresh session of Claude Code and of the other agent, both opened in the brain folder. Record the files each one used.

1. "What am I focused on this quarter? Name the file you used."
2. "What did I decide about <topic>, and when?"
3. "How do I like drafts formatted? Check your memory first and tell me where you looked."
4. "Without opening anything except your instruction file, list the file you'd open first for: my background, my tools, client A, my last big decision."
5. "Where would you look first, second and third to find what <person> and I discussed last week about <project>?" This checks the lookup order against [[Tiered Lookup Routing]].

### Shared skills layout (Extension A)

Vault starter content. The one-copy idea is from the Unlazy video. The folder names follow the verified tool docs.

```text
my-brain/
├── AGENTS.md
├── CLAUDE.md                        # @AGENTS.md
├── .agents/
│   └── skills/                      # the only real copies (Codex reads this)
│       ├── unlazy/                  # installed once by the skills installer
│       │   └── SKILL.md
│       └── weekly-review/           # your own skill, moved here
│           └── SKILL.md
└── .claude/
    └── skills/                      # links only (Claude Code reads this)
        ├── unlazy -> ../../.agents/skills/unlazy
        └── weekly-review -> ../../.agents/skills/weekly-review
```

### Install a third-party skill for several agents (example)

```bash
cd ~/my-brain
# Read the repo first. Command from the Unlazy README; tick Claude Code and Codex, choose project scope.
npx skills add Leonxlnx/unlazy
./check-skills.sh                    # confirm Claude Code actually got its link
```

### `link-skills.sh` (link your own skills into Claude Code)

```bash
#!/usr/bin/env bash
# Make every skill in .agents/skills visible to Claude Code through a link.
# First move a Claude-only skill across:  mv .claude/skills/weekly-review .agents/skills/
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p .claude/skills
for dir in .agents/skills/*/; do
  [ -d "$dir" ] || continue
  name="$(basename "$dir")"
  target=".claude/skills/$name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "SKIP $name: a real folder already exists at $target; merge it into .agents/skills first"
    continue
  fi
  ln -sfn "../../.agents/skills/$name" "$target"
  echo "linked $name"
done
```

### `check-skills.sh` (skill parity check)

```bash
#!/usr/bin/env bash
# Every shared skill should be reachable from both folders, and Claude Code should have no private copies.
cd "$(dirname "$0")"
status=0
for dir in .agents/skills/*/; do
  [ -d "$dir" ] || continue
  name="$(basename "$dir")"
  link=".claude/skills/$name"
  if [ ! -L "$link" ]; then
    echo "MISSING LINK: $link"; status=1
  elif [ ! -f "$link/SKILL.md" ]; then
    echo "BROKEN LINK: $link"; status=1
  fi
done
for entry in .claude/skills/*; do
  [ -e "$entry" ] || continue
  [ -L "$entry" ] || echo "CLAUDE-ONLY COPY (not shared): $entry"
done
[ "$status" -eq 0 ] && echo "skills in parity"
exit "$status"
```

### Hermes: read the synced skills folder (Extension B)

The key names come from the Hermes skills docs (Beyond the source). The path is an example.

```yaml
# ~/.hermes/config.yaml on the Hermes computer (merge into the existing skills section)
skills:
  external_dirs:
    - ~/Sync/my-brain/.agents/skills   # wherever Syncthing places the brain folder
```

## Done when

- [ ] The same vague question gets the same routed answer in both tools: same file cited, same facts. A good brain knows where to look, and in what order, from a vague question ([28:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1714s)).
- [ ] The second agent finds and uses the memory file when you ask about a past preference ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)).
- [ ] Single-source variant: changing a route in AGENTS.md changes Claude Code's behaviour too, because the reference pulls the file in ([23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s)).
- [ ] Two-copies variant: the two routers are identical ([11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s)), and the drift check prints "in sync".
- [ ] Both agents pass his question: does it know where my data lives and where to look, and does it answer accurately? ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s))
- [ ] Each tool shows its instruction file loaded (commands under Beyond the source → "Verify what loaded").
- [ ] *Extension A:* each shared skill exists once, in `.agents/skills/`, and `.claude/skills/<name>` points to it, so there's one copy rather than two ([10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)). `check-skills.sh` prints "skills in parity".
- [ ] *Extension A:* the same skill runs from Claude Code (`/name`) and Codex (`$name`), and an edit to its SKILL.md shows up in both.
- [ ] *Extension B:* the remote agent can open the synced skills and memory files you chose to share ([17:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1054s)), and it passes the parity prompts.

## Pitfalls

| Pitfall | What goes wrong | Fix | Source |
|---|---|---|---|
| **Assuming Claude Code features carry over** | He names the CLAUDE.md file and the self-updating memory file as Claude Code-specific. Codex reads AGENTS.md rather than CLAUDE.md, and no other tool maintains Claude Code's memory (Hermes does fall back to CLAUDE.md; see Beyond the source) | Add AGENTS.md and route memory explicitly | [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s) |
| **No memory route** | The second agent never sees the preferences Claude has learned, so answers differ | Tell the other agent where memory lives | [11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s), [11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s) |
| **Treating porting as a privacy fix** | Any cloud model still receives whatever it reads | Keep data you can't share out, or use open-source models for it | [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s) |
| **Expecting always-on behaviour for free in Claude Code** | A syncing brain needs scheduled jobs you have to set up yourself | Run always-on setups in an agent built for it, such as Hermes, or set up the scheduling | [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s) |
| **Starting with team-wide tooling** | For a shared brain, the tool (Google Drive, Notion, GitHub, or what's captioned "cloud plugins", likely Claude plugins) matters less than whether people keep their docs updated | Get your own brain working first, then solve adoption | [29:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1794s), [30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s), [30:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1826s) |
| **Separate skill copies per agent** | Copies in `.claude/skills` and `.agents/skills` drift apart, so a fix made in one tool never reaches the other | Keep one real copy and link it, as the Unlazy install does | [10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s) |
| **Assuming the installer linked Claude Code** | The skill lands in `.agents`, so Codex sees it but Claude Code doesn't | Run `check-skills.sh` after every install. See the open installer bug under Beyond the source | [10:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=610s) |
| **Porting to a computer that doesn't have the files** | A remote agent can't use skills or context that exist only on your laptop | Sync the workspace, or run the agent where the files live | [17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s), [17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s) |
| **Expecting auto memory to follow a synced folder** | Claude Code's auto memory lives outside the workspace by default, so the remote agent gets none of it | Move memory into the brain, or keep shared memory in a brain file | Beyond the source |
| **Porting a bloated router** | Every agent carries the file on every run. Ras Mic puts a 1,000-line file at about 7,000 tokens per run | Keep AGENTS.md to what the agent can't work out for itself | [04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)–[04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s) |
| **Installing unread skills for every agent at once** | One command spreads a stranger's skill to every tool. Ras Mic calls downloaded skills an easy way to attack someone | Read the SKILL.md and any scripts first, or build your own ([[Build a Skill from a Successful Run]]) | [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s) |

More pitfalls from the tool docs (import direction, override files, size caps) are listed under Beyond the source.

## Variations

- **Two synced copies**, as in Herk2 ([11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s)). It's the simplest to understand, but you must keep both files in sync.
- **Single source with an `@` reference**, as shown in his Level 4 example folder ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s)–[23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s)).
- **Always-on in Hermes.** Point a Hermes agent running GBrain at the same brain ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)). Syncing several Hermes agents points to Level 5 ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)).
- **A visual viewer.** Open the same folder in [[Obsidian]]; it only displays the files ([09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)).
- **Symlink, Codex fallback file name, or Gemini CLI setting.** These are verified alternatives, described under Beyond the source.
- **Import rather than symlink, from a coding angle.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] imports AGENTS.md into CLAUDE.md so he doesn't have to keep a symlink ([03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)–[03:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=221s)).
- **Account-level skills instead of repo folders.** For work in Claude's apps, add a skill once in Claude settings and it's available in Claude Design ([[AI LABS - Claude Design Skills for Beautiful Sites]], [00:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=52s)–[01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s)). They say the same skills work in Claude Code and Codex ([01:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=63s)). Local Claude Code needs a one-time download to see account skills (Beyond the source).
- **Claude Code or Codex on a VPS.** Keep the whole brain on a cloud server and skip syncing entirely ([[Jay E - The ARMS Framework for a Claude Agentic OS]], [17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)).

## Beyond the source

Not from the video. Each item was checked against the linked documentation on 2026-09-15. Details change between releases, so recheck the links before relying on exact limits.

### Which instruction files each tool reads

| Tool | Instruction files it loads | Import / include syntax | Size guidance | Source |
|---|---|---|---|---|
| **Claude Code** | `CLAUDE.md` or `.claude/CLAUDE.md` in the project, plus files in parent directories at launch and in subdirectories when needed. Also `~/.claude/CLAUDE.md` and `CLAUDE.local.md`. It **does not read AGENTS.md** unless CLAUDE.md imports it | `@path` (relative to the importing file, up to four levels of nesting; ignored inside code spans and code blocks) | Aim for under 200 lines per file. Imported files still load at launch | [docs](https://code.claude.com/docs/en/memory) |
| **OpenAI Codex** | Global: `~/.codex/AGENTS.override.md`, or else `~/.codex/AGENTS.md`. Then in each directory from the git root down to the working directory: `AGENTS.override.md`, then `AGENTS.md`, then any configured fallback names. Files closer to the working directory appear later and take precedence | None described in the docs | Combined cap `project_doc_max_bytes`, default 32 KiB; files beyond the cap are left out | [docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| **Hermes Agent** | **Only one** project context file *type*, first match wins: `.hermes.md`/`HERMES.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. `SOUL.md` (personality) loads separately, from `HERMES_HOME` only. Inside a git repo, Hermes merges a chain of AGENTS.md files from the git root down to the working directory (deeper files take precedence). Outside git, it checks only the working directory and never its parents. Either way, it also picks up context files in subdirectories as the agent opens them | None described in the docs | Startup files scale with the model's context window (minimum 20,000 characters); files found in subdirectories are capped at 8,000 characters | [docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) |
| **Gemini CLI** | `GEMINI.md` by default (global `~/.gemini/GEMINI.md`, project and parent directories, and files found on demand). The `context.fileName` setting accepts a list, for example `["AGENTS.md", "GEMINI.md"]` | `@file.md` imports | — | [docs](https://geminicli.com/docs/cli/gemini-md/) |
| **AGENTS.md (standard)** | An open markdown format with no required fields, now stewarded by the Agentic AI Foundation under the Linux Foundation. Many tools support it, including Codex, Cursor, GitHub Copilot, Gemini CLI and others. In nested folders, the AGENTS.md closest to the edited file wins | — | — | [agents.md](https://agents.md/) |

### Import direction matters

- **CLAUDE.md → `@AGENTS.md` works.** Claude Code expands the import, and you can add Claude-only instructions below it. This is the documented way to share instructions with other agents without duplicating them. [Claude Code docs: memory (AGENTS.md section)](https://code.claude.com/docs/en/memory)
- **The reverse doesn't work.** Neither the Codex nor the Hermes context-file docs describe any import syntax. An AGENTS.md containing only `@CLAUDE.md` would give those agents a literal line of text and no router. So the content has to live in AGENTS.md. [Codex docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- **Inside AGENTS.md, write paths without `@`.** Since Claude Code imports AGENTS.md, an `@context/about-me.md` inside it would be imported too, loading at launch and using context. Plain paths (for example in backticks) let every agent open files only when needed. [Claude Code docs: import additional files](https://code.claude.com/docs/en/memory#import-additional-files)

### Keeping the router from drifting

| Option | How | Trade-offs | Source |
|---|---|---|---|
| **Import (recommended)** | `CLAUDE.md` holds `@AGENTS.md` plus a Claude-only section | One source of truth. Works on every OS | [Claude Code docs](https://code.claude.com/docs/en/memory) |
| **Symlink** | `ln -s AGENTS.md CLAUDE.md` | No room for Claude-only additions. On Windows, symlinks need Administrator rights or Developer Mode, so the docs say to use the import there | [Claude Code docs](https://code.claude.com/docs/en/memory) |
| **Keep only CLAUDE.md** | Hermes already falls back to CLAUDE.md when there's no AGENTS.md. For Codex, add `project_doc_fallback_filenames = ["CLAUDE.md"]` to `~/.codex/config.toml` | Uses Codex's documented fallback-name setting; the docs' own example names other files. Set in `~/.codex/config.toml`, it applies to every project that uses that config. Tools that only read AGENTS.md will miss the router | [Codex docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Hermes docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) |
| **Two copies** | Keep both files and run the `cmp` drift check after edits | Easy to forget. Note that Claude Code's `/import` command (v2.1.213+) also makes a *one-time copy* of AGENTS.md into CLAUDE.md, which drifts the same way | [Claude Code docs](https://code.claude.com/docs/en/memory) |

### Where Claude Code memory actually lives

- **Default location.** Auto memory is stored per project, *outside* your folder, at `~/.claude/projects/<project>/memory/`. It holds a `MEMORY.md` index and topic files. The first 200 lines or 25KB of `MEMORY.md` load each session; topic files are read when needed. It's stored on one machine only, and it's on by default (toggle it with `/memory`). This location was also confirmed in this environment. [Claude Code docs: auto memory](https://code.claude.com/docs/en/memory#auto-memory)
- **Why this matters.** The video shows a memory.md inside the example brain folder ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s), [23:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1399s)), but by default nothing appears there. An AGENTS.md route to `memory/MEMORY.md` points at nothing unless you do one of the following:
  1. **Move the memory into the brain.** Set `autoMemoryDirectory` in settings. The value must be an absolute path or start with `~/`, for example `{"autoMemoryDirectory": "~/my-brain/memory"}`. If you set it in the project's `.claude/settings.json`, Claude Code applies the same workspace-trust rule it uses for hooks in settings files. Every agent can then read `memory/MEMORY.md`. [Claude Code docs: storage location](https://code.claude.com/docs/en/memory#auto-memory)
  2. **Route to the default path.** Put the absolute path `~/.claude/projects/<project>/memory/MEMORY.md` in AGENTS.md. This only works on that machine, and the other agent must be allowed to read outside the brain folder.
  3. *(Suggestion, not from the docs.)* Skip auto memory for shared notes and keep a hand-curated `memory/MEMORY.md` in the brain that every agent appends to under the same rule. Using the same path as option 1 means the AGENTS.md route stays valid whichever you choose.
- **Hermes has its own, separate memory.** It uses `MEMORY.md` (capped at 2,200 characters) and `USER.md` (capped at 1,375 characters) in `~/.hermes/memories/`, added to the system prompt as a fixed snapshot when a session starts. It doesn't sync with Claude Code's memory, which is why the brain's memory file still needs a route in AGENTS.md. [Hermes docs: memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)

### Tool-specific setup (verified)

1. **Claude Code.** Replace CLAUDE.md's content with `@AGENTS.md` and add any Claude-only section below it. Run `/context` and confirm CLAUDE.md is listed under "Memory files". [docs](https://code.claude.com/docs/en/memory)
2. **Codex.** Launch Codex inside the brain folder, since it reads files from the git root down to the working directory. Keep the combined instruction files under 32 KiB, or raise `project_doc_max_bytes` in `~/.codex/config.toml`. Make sure no stray `AGENTS.override.md` is overriding your AGENTS.md. [docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
3. **Hermes Agent.** Start Hermes from the brain root. Outside git, Hermes checks only the working directory for AGENTS.md. Inside a git repo, it merges every AGENTS.md from the git root down to the working directory, so if the brain sits inside a larger repo, check parent folders for AGENTS.md files that would be merged in. Make sure no `.hermes.md`/`HERMES.md` or `AGENTS.override.md` exists, or Hermes will load that file *instead of* AGENTS.md. `.hermes.md` is searched all the way up to the git root, so check parent folders too. Hermes scans context files for prompt-injection patterns and blocks any that match, so keep the router to plain instructions. [docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
4. **Gemini CLI (optional).** In `settings.json`, set `"context": { "fileName": ["AGENTS.md", "GEMINI.md"] }`. [docs](https://geminicli.com/docs/cli/gemini-md/)

### Verify what loaded

| Tool | Check | Source |
|---|---|---|
| Claude Code | `/context` → "Memory files" list | [docs](https://code.claude.com/docs/en/memory) |
| Codex | `codex --ask-for-approval never "Summarize the current instructions."` | [docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Gemini CLI | `/memory show` prints the combined context; `/memory reload` re-reads the files | [docs](https://geminicli.com/docs/cli/gemini-md/) |
| Hermes Agent | Ask it to summarise its project instructions and name the file (a suggestion; no dedicated command was found in the context-files docs) | [docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) |

### Where each tool looks for skills (verified)

Checked 2026-09-15 for Extension A.

| Tool | Skill folders | Links | Invoke | Source |
|---|---|---|---|---|
| **Claude Code** | Personal: `~/.claude/skills/<name>/SKILL.md`. Project: `.claude/skills/<name>/SKILL.md`. Also nested `.claude/skills` folders in subdirectories, and plugins. No `.agents/skills` location is listed | A skill entry can be a symlink. Claude Code reads the target and loads it once, even if several locations point to it | `/name`, or automatically when relevant | [docs](https://code.claude.com/docs/en/skills) |
| **OpenAI Codex** | `.agents/skills` in the working directory, its parents and the repo root; `$HOME/.agents/skills`; `/etc/codex/skills` | Follows symlinked skill folders | `$name` or `/skills`, or automatically from the description | [docs](https://learn.chatgpt.com/docs/build-skills) |
| **Hermes Agent** | `~/.hermes/skills/` is primary. Add folders with `skills.external_dirs` in `~/.hermes/config.yaml` (the docs' example includes `~/.agents/skills`). A local skill wins over an external one with the same name | — | `/skill-name`, or automatically | [docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) |
| **claude.ai account** | Customize > Skills: create a skill or upload a ZIP. Needs code execution and file creation turned on | — | In Claude's apps | [help](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |

- **One format everywhere.** Agent Skills (a folder with a `SKILL.md`) was developed by Anthropic and released as an open standard. Its client list includes Claude Code, Codex, Hermes Agent, OpenClaw, Cursor and Gemini CLI. [agentskills.io](https://agentskills.io/)
- **Account skills in local Claude Code.** Skills enabled on your claude.ai account load automatically in Cowork and cloud sessions. For local sessions, download them once: `CLAUDE_CODE_SYNC_SKILLS=1 claude -p "List the skills you have available"`. They land in `~/.claude/skills/synced/`, so don't give one of your own skills the folder name `synced`. [docs](https://code.claude.com/docs/en/skills)
- **Claude Design.** Its getting-started article (beta on Pro, Max, Team and Enterprise) doesn't mention skills. The claim that settings skills appear there rests on the AI LABS video. [help](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)

### The skills installer (verified)

- **Unlazy's install command** is `npx skills add Leonxlnx/unlazy`. The README invokes the skill as `/unlazy` in Claude Code and `$unlazy` in Codex, and offers an optional Claude Code Stop hook installer. [repo](https://github.com/Leonxlnx/unlazy)
- **How `npx skills` installs** (vercel-labs/skills):
  - Project scope is the default; `-g` installs globally.
  - Interactive installs offer either a symlink from each agent's folder to one canonical copy (recommended) or separate copies with `--copy`, for when links aren't supported.

  [repo](https://github.com/vercel-labs/skills)
- **Open bug #1355.** A project-scope install for Claude Code can put the skill in `.agents/skills/` without creating the `.claude/skills/` link, which leaves Claude Code unable to see it. Run `check-skills.sh` after installing. [issue](https://github.com/vercel-labs/skills/issues/1355)
- **Global path mismatch.** The CLI's compatibility table and Unlazy's README give `~/.codex/skills` as Codex's global folder. OpenAI's current docs name `$HOME/.agents/skills`. After a global install, confirm Codex lists the skill. [CLI](https://github.com/vercel-labs/skills), [Codex docs](https://learn.chatgpt.com/docs/build-skills)
- **Windows.** Symlinks need Administrator rights or Developer Mode; the Claude Code docs say this about CLAUDE.md links. My inference is that skill links hit the same limit, and `--copy` brings back copies that can drift. [docs](https://code.claude.com/docs/en/memory#agents-md)

### Cross-machine sync (verified)

- **Syncthing** keeps files in continuous sync between your own devices. It's free and open source, and no central server holds your data. [syncthing.net](https://syncthing.net/)
- **Auto memory doesn't travel with the workspace.** It's machine-local and isn't shared across machines or cloud environments. If a remote agent should read it, move it with `autoMemoryDirectory` (see "Where Claude Code memory actually lives" above). [docs](https://code.claude.com/docs/en/memory#storage-location)
- **Hosted alternative for repo-based jobs.** Claude Code routines (research preview) run on Anthropic-managed cloud infrastructure and keep working with your laptop closed. Each run clones the selected GitHub repositories fresh, so they suit a brain kept in a repo, not local-only files. [docs](https://code.claude.com/docs/en/routines)

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]]. Porting steps come from the Level 2 chapter ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s)–[11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)) and the Level 4 example folder ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s)–[23:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1399s)). The framing comes from the intro ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)–[01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)), and the Hermes points from Level 5 ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)) and Finding Your Level ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)). Video: https://www.youtube.com/watch?v=DTCyvo6cC54
- [[AI LABS - The Unlazy Skill for Lazy Agents]]. Extension A: the install walkthrough ([09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)) and editing the shared skill ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)). Video: https://www.youtube.com/watch?v=c47uqR7XB_c
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]. Extension B: Hermes on its own computer, synced with Syncthing ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)), and the VPS alternative ([17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)). Video: https://www.youtube.com/watch?v=8NSyI-npJCU
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]. Import instead of symlink ([03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)–[03:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=221s)). Video: https://www.youtube.com/watch?v=YAsxyoTWFDA
- [[AI LABS - Claude Design Skills for Beautiful Sites]]. Account-level skills across Claude Design and other agents ([00:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=52s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s)). Video: https://www.youtube.com/watch?v=Ysr7oNDajJI
- [[Ras Mic - How AI Agents and Claude Skills Work]]. Pitfalls on router size ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)–[04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s)) and on installing other people's skills ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)). Video: https://www.youtube.com/watch?v=S_oN3vlzpMw

## Related

- Concepts: [[Tool-Agnostic Context Files]] · [[CLAUDE.md as a Router]] · [[Claude Code Auto Memory]] · [[Always-On Brain OS]] · [[Second Brain Levels]]
- Concepts (skills and sync): [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Routines and Scheduled Tasks]] · [[Agentic OS]]
- Techniques: [[Build a Level 1 Second Brain]] · [[Tiered Lookup Routing]]
- Techniques (skills and sync): [[Sync a Workspace to an Always-On Cloud Agent]] · [[Build a Skill from a Successful Run]] · [[Keep CLAUDE.md Lean]]
- Tools: [[Claude Code]] · [[OpenAI Codex]] · [[Hermes Agent]] · [[GBrain]] · [[Obsidian]]
- Tools (skills and sync): [[Unlazy]] · [[Syncthing]] · [[Claude Design]]
- People: [[Nate Herk]] · [[Garry Tan]]
- People (newer sources): [[AI LABS]] · [[Jay E]] · [[The Coding Sloth]] · [[Ras Mic]]
- [[Home]]
