---
type: source
title: "Orgtree v2 - now an app!"
creator: "[[DynaBeast]]"
channel: "r/claudeskills (Reddit)"
url: https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/
repo: https://github.com/Maurdekye/orgtree
repo_commit: 0008ccb94edfb986396c49ced3e2d2c885e1fb16
published: 2026-09-12
ingested: 2026-09-23
topics: [multi-agent orchestration, agent hierarchy, work docket, multi-account, role charters, coordinator pattern, Electron app]
tags: [source/reddit, topic/agents, topic/subagents, topic/claude-code, topic/agentic-os, topic/permissions, topic/context]
---

# DynaBeast - Orgtree v2 Multi-Agent Orchestrator App

> **Creator:** [[DynaBeast]] (GitHub: Maurdekye) · **Published:** 2026-09-12 · **Format:** Reddit post + GitHub repo · [Read the post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/) · [Repo](https://github.com/Maurdekye/orgtree)

This source is a Reddit launch post plus the repository it links, not a video. There are no timestamps, so provenance links point to:

- **the post** (one link, since Reddit posts have no anchors),
- **individual comments** (permalinks),
- **repo files pinned to the commit read on 2026-09-23**, so the line numbers stay valid: V2 at [`0008ccb`](https://github.com/Maurdekye/orgtree/tree/0008ccb94edfb986396c49ced3e2d2c885e1fb16), V1 at [`a8199a5`](https://github.com/Maurdekye/claude-orgtree/tree/a8199a598f0c62216ed41cf3e1a099d46517f43d).

## TL;DR

[[Orgtree]] is a desktop app for running a **persistent team of coding agents laid out as an org chart**. You sit at the top, agents sit beneath you, and any agent can be clicked to open its chat. Agents hire their own reports, message each other, and log their work as tickets on a shared **work docket**. It drives the Claude Code, Codex and Antigravity CLIs you already have installed (plus OpenRouter models) rather than replacing them.

V2 rebuilds the V1 web app (Node, Python and Docker, run in a browser) as a self-contained Windows Electron app with a tray icon. It also makes features that were Claude-only work across providers, above all a multi-account system that can run several subscription accounts of the same provider at once.

For this vault, the most reusable part isn't the app. It's the **bundled role charters** (coordinator, implementer, redteam, curator, review workflow). They're a hard-won set of rules for keeping a multi-agent team honest. See [[Write Role Charters for a Multi-Agent Team]].

## Key takeaways

- **Show the team as a tree, not a list.** The author's pitch: seeing every agent in a hierarchy you can rearrange gives more control and visibility than a flat list of sessions or workflows ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)). See [[Persistent Agent Organizations]].
- **A shared ticket board is what keeps two dozen agents legible.** Agents know to record their task as a ticket and update it as they go, so a glance at the docket shows all work in flight ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/); [README L17](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L17)).
- **Run several accounts in parallel on purpose.** Each account gets its own tint, and you or the agents choose which account an agent runs on. Automatic failover when a limit hits exists but is off by default ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/); [README L78–85](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L78-L85)). The author's real use: work development spread in parallel across several AI accounts with little oversight ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9fpwmz/)).
- **Coordination overhead is the real bottleneck.** He could use the plain CLIs, but coordinating many agents by hand became the limit, and Orgtree absorbs that overhead ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9fpwmz/)).
- **It reuses your existing setup.** Because it runs the installed Claude Code / Codex / Antigravity harnesses, your CLAUDE.md files, skills and docs apply unchanged ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/paf2u6v/)).
- **Credits cap concurrency, not spend.** Each agent holds a model-dependent seat and a grant for its reports; retiring frees it. Credits don't buy tokens ([README L60–62](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L60-L62)).
- **The charter is the job; permissions are the fence.** An agent's charter says what it should do; its folder and tool grants decide what it can touch ([README L64–66](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L64-L66)).

## Notes by section

### Why v2 exists (post)

The author names three problems with V1 ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)):

1. It needed Node.js, Python and Docker set up to run as a persistent web app. That was too much for most individuals to install and update.
2. You couldn't tell whether it was running unless the web page was open.
3. It favoured Claude, with extra features only for Claude Code.

V2 is a standalone Electron app with its own bundled Python and Node, a tray icon that shows it's running, and provider parity for secondary accounts, API-key use and theming.

### New in v2 (post)

- **Work docket.** A Trello- or issue-tracker-style board built for agents. Giving an agent a task makes it file and track a ticket there.
- **Multi-account, redone.**
  - V1 only had a Claude fallback token from `claude setup-token`. You couldn't see its usage, you couldn't control it, and the author found the tokens often stopped working.
  - V2 lets any provider have a secondary subscription account, added via "Add a secondary account" → "Create managed account" and a browser sign-in.
  - Every provider supports API keys.
  - The usage window shows limits for every account at once.
  - Several same-provider accounts can run agents at the same time.
- **Presentations.** All agent-presented documents are viewable in one place, and agents can present HTML mockups as well as markdown.
- **Window management.** Pin any chat or modal as a movable, resizable window, or pop it out to its own OS window across monitors.
- **Auto-update**, plus smaller touches: themes, context menus, message replies, image embeds, desktop notifications, hiding retired agents, and a move from JSON storage to SQLite for large orgs.

**Carried over from V1:** cheap compaction, watchdogs, credit allowances and the agent mailhub.

**Dropped:** kiosk mode, public internet exposure and sandboxing. They were cheap to build in a web app, hard to port, and little used.

**Platform:** releases are 64-bit Windows only; build from source for Mac or Linux ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/); [comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9jaoxk/)).

**Positioning:** a personal, multi-provider orchestrator for one developer working on their own project on a home PC.

### How the model works (V1 README, still the fullest description)

- **Tree and tools.** You're the root. You hire top-level agents, and they hire their own reports through `orgtree_*` MCP tools that every node gets ([V1 README L38–41](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L38-L41)).
- **Messaging rules.** Messages can go down to any depth, up one hop, or sideways to peers. A deeper agent needs an **audience** to reach you. Reading transcripts and scratch files only works downward. Capabilities flow down like credits: a parent can't grant what it doesn't hold ([V1 README L53–59](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L53-L59)).
- **Resume on demand.** Each node keeps a durable provider session, and new mail starts a turn in it ([V1 README L61–62](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L61-L62)).
- **Compaction by splitting.** Near the context limit (80% by default), a node splits. A compacted successor keeps the name, and the old self stays archived and can be consulted as a "knowledge bearer" ([V1 README L64–67](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L64-L67), [L145](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L145)). This is the "cheap compaction" the post mentions.
- **The coordinator pattern.** The intended everyday shape is one strong coordinator directly under you and every worker flat beneath it. The coordinator splits your asks, hires one agent per piece, and gives each hire a direct line to you ([V1 README L135–143](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L135-L143)).
- **Watchdogs.** Persistent watchers on files, commands, processes or streams send mail when a condition is met, so nobody has to poll an agent ([V1 README L170–173](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L170-L173)).
- **Safety warning.** Agents run autonomously in the folders you grant. Read-only folder rules can be bypassed by an agent that has Bash, so grant folders as carefully as you would to a contractor ([V1 README L599–607](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L599-L607)).

### First organization (V2 README)

The five-step start is: create an org with a capacity budget → hire an agent with a model and a charter → grant folders and tools → send a concrete task with a finish condition → follow up via the docket, inbox and presentations. Start with one agent and a small task ([README L50–58](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L50-L58)). Built out in [[Run a Coordinator-Led Agent Team in Orgtree]].

### Bundled charters (engine/docs/charters)

The charter presets are copied into `~/.orgtree/charters/`, where you can edit them, and every `.md` file there shows up as a preset when hiring ([onboarding doc](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/docs/v2-onboarding.md)). They're written from real incidents. Highlights of the [coordinator charter](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md):

- **Docket before building.** Put every new feature request on the docket before staffing it ([L23](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L23)).
- **A hire does nothing until it's given a task.** Send the task together with the hire ([L32](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L32)).
- **Don't reply to status updates.** "Thanks" costs the other agent a full turn ([L37](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L37)).
- **Write every user decision to a file the turn it arrives,** because compaction wipes open questions ([L42](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L42)).
- **One agent per piece, and check nobody is already on it.** The charter records three duplicate-staffing incidents in 24 hours ([L53](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L53)).
- **Look, don't ask.** Read a report's transcript or files instead of asking it for status ([L61](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L61)).
- **Label relays as verified or inferred** ([L66](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L66)).
- **Keep idle agents unless you're short of credits** ([L71](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L71)).
- **Re-check what was waiting on an agent you retire** ([L80](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L80)).

The [implementer](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/implementer.md), [redteam](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/redteam.md) and [curator](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/curator.md) charters form a three-seat team: one ships, one attacks, one keeps the record. The [review-workflow](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/review-workflow.md) preset scales redteam review by feature size. All three seat charters treat peer messages as coordination, never authority. The full set is distilled in [[Write Role Charters for a Multi-Agent Team]].

### Comments

- **Paperclip comparison.** Asked how it compares to Paperclip ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9g4ogq/)), the author first conceded someone had the idea earlier ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9hwb7l/)). He then drew a distinction: Paperclip is opinionated and has you act like a CEO over your AIs, while Orgtree is a free-form sandbox of coordination tools. It can be set up Paperclip-style or used as ordinary chats that happen to talk to each other ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9ia1qk/)).
- **Importing existing sessions.** There's no session import. He suggests asking Claude or Codex to bring them over by hand, and notes that existing CLAUDE.md files and skills just work ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/paf2u6v/)).

## Caveats & disagreements

- **One author, early software.** It's weeks old, and there were 70-plus releases and release candidates between 2.1.0 and 2.1.12 ([docs folder](https://github.com/Maurdekye/orgtree/tree/0008ccb94edfb986396c49ced3e2d2c885e1fb16/docs)). Expect churn.
- **Windows only** for packaged builds.
- **Costs still apply.** Orgtree includes no model access. Provider subscriptions and limits still apply ([README L48](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L48)), and many agents running in parallel burn limits fast. See the cost warnings in [[Subagents and Agent Teams]].
- **Sandboxing was dropped in v2.** Folder grants are the main fence, and V1's own README warns that Bash can get around read-only rules.
- **"Unique" is contested.** Paperclip does something similar (see comments). Separately, [[Ras Mic - How AI Agents and Claude Skills Work]] argues most people get more done building their own system than adopting a ready-made multi-agent one. That applies here too.
- **Multi-account use.** Running several subscription accounts at once to multiply capacity may conflict with a provider's terms. Check them (see Beyond the source).

## Build from this

- **A charter set for your own agents, with or without Orgtree.** → [[Write Role Charters for a Multi-Agent Team]]
- **A coordinator-led Orgtree org for a real project.** → [[Run a Coordinator-Led Agent Team in Orgtree]]
- **A docket file for a Claude Code agent team.** Use the "docket first" rule with a shared markdown or issue tracker so parallel agents stay visible. Pairs with [[Evidence-Gated Completion Ledger]] and [[Parallel Sessions with Git Worktrees]].

## Resources mentioned

- Orgtree V2 repo: <https://github.com/Maurdekye/orgtree> · latest installer: <https://github.com/Maurdekye/orgtree/releases/latest>
- V1 (deprecated): <https://github.com/Maurdekye/claude-orgtree>
- Mail hub submodule: <https://github.com/Maurdekye/orgtree-mailhub>
- Paperclip (mentioned in comments; not linked in the thread)

## Beyond the source

- **Account terms.** Anthropic's consumer terms govern how Claude subscriptions are used, including account sharing and automated access. Read them before running several subscription accounts in parallel through one tool. <https://www.anthropic.com/legal/consumer-terms>
- **Claude Code has built-in alternatives.** For multi-agent work without a separate app, Claude Code offers subagents, experimental agent teams and agent view. See Beyond the source in [[Subagents and Agent Teams]]. <https://code.claude.com/docs/en/agents>
- **Latest release.** Checked 2026-09-23: 2.1.12 (published 2026-09-22), up from 2.1.0 at the time of the post. <https://github.com/Maurdekye/orgtree/releases>

## Transcript notes

- Reddit username **DynaBeast** is the same person as GitHub **Maurdekye**. The post links the Maurdekye repo as "my Orgtree project", and DynaBeast answers comments as the author.
- "claude.md" in a comment was auto-linked by Reddit to a website; it means CLAUDE.md.
- The post says v2.1.0 was current when posted; the release is dated 2026-09-12, which matches the comment ages.

## Related

- **Concepts:** [[Persistent Agent Organizations]] · [[Subagents and Agent Teams]] · [[Agentic OS]] · [[Permissions and Approval Gates]] · [[Context Window Management]] · [[Verification Before Done]]
- **Techniques:** [[Run a Coordinator-Led Agent Team in Orgtree]] · [[Write Role Charters for a Multi-Agent Team]] · [[Parallel Sessions with Git Worktrees]] · [[Multi-Agent Review and Scoring Loops]]
- **Tools:** [[Orgtree]] · [[Claude Code]] · [[OpenAI Codex]]
- **People:** [[DynaBeast]]
