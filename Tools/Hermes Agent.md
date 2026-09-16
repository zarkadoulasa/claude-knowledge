---
type: tool
category: Open-source autonomous agent / agent harness (Nous Research)
website: https://github.com/NousResearch/hermes-agent
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]"]
tags: [topic/agents, topic/automation, topic/second-brain, topic/portability, topic/memory, topic/scheduling, topic/skills, topic/agentic-os]
---

# Hermes Agent

## What it is

Hermes Agent is another agent harness [[Nate Herk]] runs his second brain through. In the video it's also where he experiments with always-on (Level 5) setups. [[Jay E]] is further along: most of his scheduled tasks already run on a Hermes agent with its own cloud computer, fed with his Claude Code skills and memory files through [[Syncthing]]. The official description is under *Beyond the source*.

## How sources use it

### [[Nate Herk - Every Level of a Claude Second Brain]]

#### One brain, several harnesses

- He uses his second brain with Hermes Agent, as well as with [[Claude Code]] and [[OpenAI Codex]] ([01:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=106s), [01:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=108s)).
- It works because the brain is just files and folders, so different agent harnesses can use it ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s), [01:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=112s)).
- Setup mechanics: [[Tool-Agnostic Context Files]] and [[Port a Claude Code Brain to Other Agents]].

#### The natural home for an always-on brain

- **Why Hermes.** Adding [[GBrain]] to something like Hermes Agent would work really well, in his view ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s), [25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s)).
- **The contrast with Claude Code.** You could run it in Claude Code, but you'd have to handle the crons and all the setup yourself ([25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s), [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s)).
- **His status.** He doesn't currently run GBrain ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)). He has been experimenting with it on his Hermes agent ([25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s)).
- See [[Always-On Brain OS]].

| Harness | Running an always-on brain like GBrain | Where |
|---|---|---|
| Hermes Agent | Nate thinks it's a really good fit and is experimenting with it | [25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s), [25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s) |
| Claude Code | Possible, but you set up and handle the cron jobs yourself | [25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s), [25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s) |

#### Hermes as a Level 5 signal

- In "Finding your level" he describes a situation that points to Level 5 ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s), [29:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1769s)):
  - you're running agents "offline" (as captioned; probably meaning unattended, see Notes),
  - you have a lot of data,
  - you want several Hermes agents synced together.
- In that case you probably want Level 5, something like GBrain ([29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)). See [[Second Brain Levels]].

#### Cautions he attaches to always-on setups

- **Level 5 isn't automatically best.** He has reasons for not sitting at Level 5 himself ([03:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=235s), [03:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=237s)). Choose the lowest level that fits your needs. Without a pain point there's no reason to build new architecture ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)). See [[Second Brain Pain-Point Audit]].
- **Too much context.** Automatic ingestion scares him a bit. At some point more context may do more harm than good ([26:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1572s), [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1580s)). He prefers full control over what gets ingested ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
- **Keep fast-changing data out.** Slack threads, emails and customer data change constantly, and ingesting them adds noise ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [27:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1657s)). Give the brain access to fetch that data when needed instead ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)). See [[Context vs Connections]].

### [[Jay E - The ARMS Framework for a Claude Agentic OS]]

#### Where Hermes sits in his routine levels

| Level | What runs where | Where |
|---|---|---|
| 1 | Local routines in the Claude Code desktop app. They only run while the computer is on | [15:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=956s)–[16:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=966s) |
| 2 | Scheduled tasks in the cloud that run with the computer off. He names OpenClaw (which he thinks probably popularised the idea), Grok Bot (new, but expensive) and Hermes, the one he set up and uses | [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)–[16:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=989s) |
| Next stage (he doesn't number it) | Claude Code, or Codex, installed on a VPS, with all files and context living there. He describes other users experimenting with this, not his own setup | [17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s) |

#### Why Hermes is always on

- **24/7 is the selling point.** He calls Hermes powerful because it runs around the clock ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[16:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1002s)).
- **It has its own computer.** That's how it stays on: most users give Hermes a dedicated machine, and his is a computer in the cloud ([16:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1004s)–[16:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1012s)).
- **Most of his schedule lives there.** The majority of tasks on his routines board are loaded into his Hermes agent ([16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)).

#### The missed step: giving Hermes your Claude Code skills and memory

- **The problem.** If Hermes runs on its own computer, it can't reach the skills and context you've built up in Claude Code. He says most people miss this ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s)).
- **His fix.** There are several ways to solve it. He uses Syncthing, free open-source software that syncs files between computers ([17:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1030s)–[17:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1043s)).
- **Setup.**
  1. Point Syncthing at the workspace Claude Code works in.
  2. Install it on the Hermes computer as well.
  3. Sync the files you want, including the skills and memory files Hermes should share.

  ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s))
- **His prompt isn't in the captions.** He gets started with a single prompt that's shown only on screen ([17:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1059s)).
- **Go deeper.** Full build: [[Sync a Workspace to an Always-On Cloud Agent]]. Tool note: [[Syncthing]].

#### What he expects next

- **One platform, no sync.** Running Claude Code itself on a VPS gives routines that run 24/7 on a single platform, with no sync tool between two setups ([18:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1084s)–[18:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1101s)).
- **Hosted versions later.** He thinks OpenAI and Anthropic may offer this, but later rather than now, because of file-storage and security concerns ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)–[18:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1112s)). Beyond the source notes what Anthropic already offers.

#### Learning Hermes

- He points to his other Hermes tutorials on his channel, and to a Hermes Agent masterclass inside his paid community ([16:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=989s)–[16:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=996s)). No link is recorded here.

### Two practitioners compared

| | [[Nate Herk - Every Level of a Claude Second Brain]] | [[Jay E - The ARMS Framework for a Claude Agentic OS]] |
|---|---|---|
| How far along | Experimenting with GBrain on his Hermes agent ([25:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1559s)) | Runs most of his scheduled tasks on Hermes ([16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)) |
| Why Hermes rather than Claude Code | In Claude Code you'd set up the crons yourself ([25:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1555s)) | Local routines stop when the computer is off, while Hermes has its own always-on computer ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s), [16:48](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1008s)) |
| How Hermes gets the brain | Plain files any harness can read ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)) | Syncthing copies skills and memory files over from the Claude Code workspace ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)) |
| Main caution | Automatic ingestion and too much context ([26:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1572s)) | A remote agent can't see your skills and context unless you get them there ([17:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1021s)) |

They don't contradict each other. Jay E is simply further down the same path.

## Notes

- **What the video doesn't show.** There's no Hermes Agent configuration, and no demonstration of how he points Hermes at his brain or wires GBrain into it. Everything above is his stated usage and opinion.
- **"Offline" is ambiguous.** The captions have him describing agents running "offline" at [29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s). From context he likely means agents running unattended or autonomously, but the exact word is *(unclear in captions)*.
- **Caption fixes.** "Gbrain" and "G brain" → GBrain. From Jay E's video: "Sync Thing" → Syncthing, "masterass" → masterclass, "Codeex" → Codex. "Grockbot" → Grok Bot, likely xAI's product, as identified in [[Jay E - The ARMS Framework for a Claude Agentic OS]].
- **What Jay E's video doesn't show.** It shows no Hermes configuration, no cron job definitions, and no Syncthing folder or ignore settings. His setup prompt appears only on screen. The practical gaps are covered in [[Sync a Workspace to an Always-On Cloud Agent]].
- **Promotion.** The Hermes masterclass is part of a paid-community pitch. This note records only that it exists.

## Beyond the source

*Not from the video. Each item was checked on 2026-09-15 at the linked page.*

- **What it is.** Hermes Agent is an open-source, MIT-licensed, self-improving AI agent built by Nous Research. Its built-in learning loop creates skills from experience and improves them as they're used. <https://github.com/NousResearch/hermes-agent>
- **Why it suits always-on use (from the README).**
  - A built-in cron scheduler runs unattended jobs, such as daily reports or weekly audits, and delivers results to any platform.
  - A single messaging gateway covers Telegram, Discord, Slack, WhatsApp, Signal and email.
  - It can run on a cheap VPS, a GPU cluster or serverless infrastructure, with several terminal backends (local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox).

  <https://github.com/NousResearch/hermes-agent>
- **Its own memory.**
  - The agent writes `MEMORY.md` and `USER.md` itself, through its memory tool, into `~/.hermes/memories/`. You can gate saves with a `write_approval` option.
  - It also recalls past sessions using full-text session search with LLM summarisation.

  <https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what>, <https://github.com/NousResearch/hermes-agent>
- **Which context file it reads.**
  - Hermes loads only one project context file type per session, and the first match wins: `.hermes.md`/`HERMES.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`.
  - A global `SOUL.md` from `HERMES_HOME` loads separately as the agent's identity.
  - The docs don't describe any `@` import syntax.

  <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>
- **Implication for Nate's setup (my synthesis).**
  - **It reads AGENTS.md.** In a brain with both AGENTS.md and CLAUDE.md, Hermes reads AGENTS.md. That's fine if AGENTS.md is the real router file.
  - **Keep the real content in AGENTS.md.** The context-files docs describe no `@` import syntax, so don't count on Hermes expanding an `@`-reference stub.
  - **Memories don't cross over.** Hermes's memory and Claude Code's auto memory (`~/.claude/projects/<project>/memory/`) are separate stores, and neither agent reads the other's automatically. Route to shared memory explicitly, as he does for Codex.

  <https://code.claude.com/docs/en/memory#storage-location>
- **GBrain is built with Hermes in mind.** GBrain's GitHub description calls it Garry's opinionated brain for OpenClaw and Hermes Agent, and its README lists Hermes among the agents it works with. <https://github.com/garrytan/gbrain>

### Added with Jay E's video

*Not from the videos. Checked 2026-09-15.*

- **Pointing Hermes at synced skills.** <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
  - `~/.hermes/skills/` is Hermes's primary skills directory.
  - You can add more folders under `skills.external_dirs` in `~/.hermes/config.yaml`. The docs' own example lists a shared `~/.agents/skills`, and paths accept `~` and `${VAR}`.
  - If the same skill name exists in both places, the local copy wins.
  - `create_dir` changes where the agent saves skills it creates.
  - Hermes skills follow the agentskills.io standard.
  - For Jay's setup, this is how Hermes can use a synced skills folder directly.
- **Watch the learning loop on shared skills.** Hermes's skills docs warn that external folders aren't write-protected. If the Hermes process can write to an external skills folder, its own skill updates can change the files there. <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
  - *My inference:* on a two-way sync, Hermes could change the skills your laptop's Claude Code uses. Decide who may write to that folder.
- **Syncthing** keeps files in continuous sync between your own devices. It's free and open source, and no central server holds your data. <https://syncthing.net/>
- **Anthropic's hosted option already exists for repo-based work.** <https://code.claude.com/docs/en/routines>
  - Claude Code routines (research preview) run on Anthropic-managed cloud infrastructure and keep working with your laptop closed.
  - They can be triggered on a schedule, by an API call or by GitHub events, on Pro, Max, Team and Enterprise plans.
  - Each run clones the selected GitHub repositories fresh, and choosing "Local" in the desktop app creates a scheduled task that runs on your own machine instead.
  - Jay's "near future" expectation is therefore partly met already. Hosted scheduled runs exist, but they don't give you a persistent workspace of local files, which is what his Hermes and VPS setups provide.
- **Syncing the workspace doesn't carry Claude Code's auto memory.** It lives outside the project (see "Memories don't cross over" above), so move it with `autoMemoryDirectory`, or keep shared memory in workspace files. <https://code.claude.com/docs/en/memory#storage-location>

## Related

- **Concepts:** [[Always-On Brain OS]], [[Tool-Agnostic Context Files]], [[Second Brain Levels]], [[Context vs Connections]]
- **More concepts:** [[Routines and Scheduled Tasks]], [[Agentic OS]], [[Agent Skills]]
- **Techniques:** [[Port a Claude Code Brain to Other Agents]], [[Second Brain Pain-Point Audit]]
- **More techniques:** [[Sync a Workspace to an Always-On Cloud Agent]], [[Schedule Recurring Claude Tasks]], [[Build an Agentic OS Dashboard]]
- **Tools:** [[GBrain]], [[Claude Code]], [[OpenAI Codex]]
- **More tools:** [[Syncthing]], [[OpenClaw]]
- **People:** [[Nate Herk]], [[Garry Tan]], [[Jay E]]
- **Source:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **Source:** [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- [[Home]]
