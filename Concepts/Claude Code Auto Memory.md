---
type: concept
aliases: ["Auto Memory", "MEMORY.md"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Anthropic - What Is Claude Managed Agents]]"]
tags: [topic/memory, topic/claude-code, topic/portability, topic/second-brain]
---

# Claude Code Auto Memory

## In one sentence

Auto memory is Claude Code's built-in feature for writing and updating its own memory notes across sessions without you maintaining them. It's a natural Level 2 addition to a second brain, but it only exists in Claude Code, so other agents have to be told where the memory is.

## How it works

### What the video shows

- **Memory arrives at Level 2.** The Level 2 router keeps its routes to context, projects and decisions, and adds routes to a wiki, references and a memory file ([10:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=629s), [10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). Along with growing those folders, this is the level where the idea of memory comes in ([10:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=641s), [10:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=647s)).
- **What auto memory does.** Once it's switched on in Claude Code ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)), the AI writes and updates that memory by itself ([10:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=650s), [10:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=652s)), so you don't have to think about it ([10:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=655s)).
- **How to toggle it.** Run the /memory command ([10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s)). It shows whether auto memory is on or off ([10:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=658s)), and you can switch it on from there ([11:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=661s)).
- **It's tool-specific.** He points out that the self-updating memory file, like CLAUDE.md, belongs to Claude Code, which works against keeping a brain tool-agnostic ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s), [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s), [11:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=671s)).
- **Using it from other tools.** Claude Code keeps the memory up to date ([11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s)). Make sure the memory file exists ([11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s)) and tell Codex to look in it for memories ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)). It's a routing problem ([11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)). See [[Tool-Agnostic Context Files]].
- **It keeps growing.** In his Level 4 example the memory is still there and has grown as more layers were added ([23:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1399s), [23:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1401s)).

### Other memory-like mechanisms in the video

| Mechanism | Who writes it | Where it appears |
|---|---|---|
| Decision log | Claude, because CLAUDE.md tells it to append each big decision with its date | Level 1 ([06:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=368s), [06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)) |
| Auto memory file | Claude Code, automatically once switched on | Level 2 ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)) |
| Always-on memory (GBrain) | A system that keeps syncing and refreshing memories | Level 5 ([25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s)). See [[Always-On Brain OS]] |
| Curated ingest | He and Claude together, e.g. a skill that collects the week's meeting transcripts before they decide what to ingest | His own practice ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s), [26:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1596s)) |

Later sources add more memory-like mechanisms that aren't Claude Code auto memory:

- a `learning.md` journal that an improver agent keeps inside a skill, in [[AI LABS - Types of Claude Loops Explained]] ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s));
- Managed Agents memory stores, which an agent reads before a run and writes after it, in [[Anthropic - What Is Claude Managed Agents]] ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)).

[[Agent Memory Patterns]] compares all of them side by side.

## When to use it — and when not to

**What the video says directly:**
- Switch it on when you want memory without maintaining it by hand. He introduces it as part of Level 2 ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)).
- If you also work in Codex or another harness, route that agent to the memory file ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)).

**Related cautions he raises.** These are about automated ingestion in general, especially always-on Level 5 systems. He doesn't aim them at auto memory specifically:
- **Too much context can hurt.** More context can reach a point where it does more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1580s)). That's why he stays in full control of what his brain ingests ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s), [26:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1597s)).
- **Store only durable things.**
  - Fast-changing data like Slack threads, emails and customer records becomes noise if ingested ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)).
  - The brain should hold things you won't later delete ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)). His test: will this memory still be useful a year from now ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s))?
  - For everything else, give the brain access to the source rather than copying it in ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)).

  See [[Context vs Connections]].

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: auto memory is a low-effort Level 2 upgrade you switch on with /memory ([10:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=657s)). He treats it as a Claude Code-specific piece that other agents reach through routing ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)). In his example projects the memory file sits alongside the other routed folders ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: calls the CLAUDE.md that `/init` generates Claude's "permanent memory" for the project ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)).
  - That file is written by `/init` and by you, not the Claude-written auto memory this note covers.
  - He contrasts it with the context window, which he calls Claude's short-term memory ([13:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=790s)).
  - Over months he has used CLAUDE.md to counter habits he's noticed in the models ([04:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=254s)). Still, he says it isn't make-or-break ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s)).
  - He never mentions auto memory.
- [[Simon Pittman - Set Up Claude Cowork]]: in Cowork he specifies a memory system by hand.
  - He has Claude create a `memory.md` and add new entries at the bottom or update related ones ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)).
  - His global instructions point Claude to that file at the start of every session ([15:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=918s), [18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)). Each project later gets its own memory file ([35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s)).
  - When he corrects Claude, he asks it to update its memory or its instructions so the change sticks ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)).
  - Claude does the writing. Simon names the file, its purpose and the append-or-update rule, and Claude drafts the sections itself: session log, active projects, key decisions, preferences ([17:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1069s)). Compare option 1 under Beyond the source.
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: runs a correction loop into CLAUDE.md, not auto memory, and doesn't mention auto memory.
  - After a new discovery, Claude logs new patterns, gotchas and conventions into CLAUDE.md ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)).
  - When pushing back gets a better result, he tells it to update the skill or CLAUDE.md ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - To stop that loop bloating the file, he caps CLAUDE.md at 150–200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).

## Where sources disagree

- **Where learnings and corrections should go.**
  - In [[Nate Herk - Every Level of a Claude Second Brain]], Claude Code writes memory on its own ([10:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=650s)), in a memory file separate from CLAUDE.md ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)).
  - In [[Nate Herk - 32 Tricks to Level Up Claude Code]], Claude writes learnings and corrections into CLAUDE.md itself ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s), [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - In [[Simon Pittman - Set Up Claude Cowork]], Claude chooses between its memory and its instructions ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)).
  - The docs' own split is under Beyond the source.
- **What "memory" means.**
  - Coding Sloth uses the word for CLAUDE.md ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)).
  - In Nate Herk's Level 2 framing, memory is a separate file that Claude maintains ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)).
- **Automatic vs specified.**
  - Auto memory is pitched as something you needn't think about ([10:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=655s)).
  - Simon spells out the memory file's purpose and its append-or-update rule ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)), and Claude drafts its sections ([17:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1069s)).
- **Full comparison.** [[Agent Memory Patterns]] also covers the per-skill journal, Managed Agents stores and always-on memory.

## Beyond the source

*Not from the video. Checked 2026-09-15 against the Claude Code memory docs: <https://code.claude.com/docs/en/memory>*

**The two memory systems in Claude Code** (<https://code.claude.com/docs/en/memory#claude-md-vs-auto-memory>):

| | CLAUDE.md | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| Contents | Instructions and rules | Learnings and patterns |
| Loaded | Every session, in full (a file over 4 MiB is skipped; CLAUDE.md files in subdirectories load on demand) | Every session: the first 200 lines or 25KB of `MEMORY.md`, whichever comes first |
| Scope | Project, user or organization | Per repository, shared across worktrees |

Both are context rather than enforced configuration. See [[CLAUDE.md as a Router]].

- **On by default.**
  - `/memory` lists your CLAUDE.md, CLAUDE.local.md and other memory files, lets you toggle auto memory, and can open the auto memory folder.
  - The toggle saves `autoMemoryEnabled` to `~/.claude/settings.json`.
  - To turn it off for one project, set `"autoMemoryEnabled": false` in that project's settings.
  - To turn it off with an environment variable, set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.

  <https://code.claude.com/docs/en/memory#enable-or-disable-auto-memory>
- **What it saves.** Each memory has a `type` field: `user` (your role and preferences), `feedback` (corrections and approaches you confirm), `project` (ongoing work, deadlines and decisions not visible in code or git), or `reference` (where outside information lives). It skips anything it can work out from the codebase and anything your CLAUDE.md already says. It doesn't save something every session. <https://code.claude.com/docs/en/memory#auto-memory>
- **Where it's stored: outside your project.**
  - The directory is `~/.claude/projects/<project>/memory/`. The `<project>` part comes from the git repository, so all worktrees and subdirectories share one memory directory. Outside a git repo, the project root is used.
  - It's machine-local and isn't shared across machines or cloud environments.
  - Old session transcripts are cleaned up after a retention period, but memory files are excluded from that cleanup.

  <https://code.claude.com/docs/en/memory#storage-location>
- **How the files are organized.** A `MEMORY.md` index has one line per memory, and each memory has its own topic file. Only the index (up to 200 lines or 25KB) loads at startup. Claude reads topic files on demand. When the index gets close to the limit, Claude Code prompts Claude to shorten it. <https://code.claude.com/docs/en/memory#how-it-works>
- **About the memory file in his example folders.** The video shows a memory file inside the project ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)), but by default Claude Code keeps auto memory in the `~/.claude/projects/...` directory above, not in the repo. A memory file you see inside a project folder is either:
  - an ordinary file kept up by instructions (like his decision log), or
  - auto memory moved into the project with the `autoMemoryDirectory` setting.

  He presents it as the file auto memory writes ([10:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=652s)), but doesn't show how it came to sit inside the project. **Don't assume that copying, cloning or syncing a vault brings Claude's auto memory with it.** <https://code.claude.com/docs/en/memory#storage-location>
- **Moving it.** `autoMemoryDirectory` in `settings.json` relocates auto memory. The value must be an absolute path or start with `~/`. It can be set at any settings scope, but in a project's `.claude/settings.json` or `.claude/settings.local.json` it is honored only under the same workspace-trust rule as hooks. <https://code.claude.com/docs/en/memory#storage-location>
- **Remember vs. instruct.** Asking Claude to "remember" something saves it to auto memory. To make it a standing instruction, ask Claude to add it to CLAUDE.md, or edit that file through `/memory`. <https://code.claude.com/docs/en/memory#view-and-edit-with-%2Fmemory>
- **Subagents don't get it.** A subagent doesn't load the main conversation's auto memory; a fork does. Subagents can have their own separate memory. <https://code.claude.com/docs/en/memory#how-it-works>
- **Other harnesses keep their own memory.** Hermes Agent writes its own `MEMORY.md` and `USER.md` into `~/.hermes/memories/`. Its docs don't describe reading Claude Code's auto memory. It can load a project's CLAUDE.md as context, but only when no `.hermes.md` or AGENTS.md matches first. So route each tool to shared memory explicitly. <https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what>
- **Options for making memory part of a portable vault.** My synthesis of the facts above, not steps from the video:
  1. **Route to an in-repo memory file.** Keep a `memory/MEMORY.md` inside the vault. That is the path the vault's starter layouts route to, and dated decisions stay in the separate `decisions.md` log. Add a rule to CLAUDE.md/AGENTS.md such as "append durable learnings and corrections here, with dates." Every agent can read and write it, and it travels with the vault. If you later switch to option 2, point `autoMemoryDirectory` at that same `memory/` folder. This builds on the append-with-dates habit of his Level 1 decision log ([06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)).
  2. **Move auto memory into the vault** with `autoMemoryDirectory`. Because the value must be an absolute path or start with `~/`, it depends on each machine's folder layout. Other agents still need a route pointing at it.
  3. **Point other agents at the default location** (`~/.claude/projects/<project>/memory/MEMORY.md`). This only works on the same machine.

  Whichever you choose, review memory now and then with `/memory`. It's plain markdown you can edit or delete.

  <https://code.claude.com/docs/en/memory#audit-and-edit-your-memory>

*Added 2026-09-15 for the newer sources. Each item was checked at the link given.*

- **Where corrections belong, according to the docs.**
  - **CLAUDE.md.** The docs suggest adding to it when Claude repeats a mistake or you retype the same correction. That backs Nate Herk's habit of writing standing rules into CLAUDE.md ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - **Auto memory.** Asking Claude to "remember" something saves it to auto memory instead, where corrections are stored with the `feedback` type.
  - **What stays out of CLAUDE.md.** Keep it to facts needed in every session; move multi-step procedures into skills.
  - **How it's delivered.** CLAUDE.md is delivered as a user message after the system prompt, and following it isn't guaranteed. Coding Sloth's "permanent memory" ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)) and Nate Herk's "basically the system prompt" ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s)) are both loose descriptions.

  <https://code.claude.com/docs/en/memory>
- **Cowork's built-in memory, which Simon's video doesn't mention.**
  - **Cloud only.** Memory is shared between chat and Cowork only when Cowork runs in the cloud, and isn't available in sessions that run locally on your computer. You view, edit and delete it in Settings > Memory. <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
  - **Per project.** Cowork projects keep memory scoped to each project. <https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork>
  - *My inference:* Simon's `memory.md` works as a file-based equivalent that also covers local sessions and any agent that can read the folder. In a cloud session, it would run alongside the built-in memory.

## Related

- [[Agent Memory Patterns]], a side-by-side comparison of every memory approach in the vault
- [[CLAUDE.md as a Router]] and [[Keep CLAUDE.md Lean]]
- [[Tool-Agnostic Context Files]]
- [[Port a Claude Code Brain to Other Agents]]
- [[Second Brain Levels]], where auto memory enters at Level 2
- [[Always-On Brain OS]] and [[Context vs Connections]]
- [[Set Up Claude Cowork]] and [[Skill Improvement Loop]]
- [[Claude Code]], [[OpenAI Codex]], [[Hermes Agent]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]], [[Nate Herk - 32 Tricks to Level Up Claude Code]], [[The Coding Sloth - 1000 Hours of Claude Code Lessons]], [[Simon Pittman - Set Up Claude Cowork]], [[AI LABS - Types of Claude Loops Explained]], [[Anthropic - What Is Claude Managed Agents]]
- [[Home]]
