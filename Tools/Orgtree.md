---
type: tool
category: Desktop multi-agent orchestrator (Windows, Electron) that runs Claude Code, Codex, Antigravity and OpenRouter agents as an org chart
website: https://github.com/Maurdekye/orgtree
sources: ["[[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]"]
tags: [topic/agents, topic/subagents, topic/claude-code, topic/agentic-os, topic/permissions]
---

# Orgtree

## What it is

Orgtree is an open-source (MIT) desktop app by [[DynaBeast]] (GitHub: Maurdekye) for running a **persistent team of coding agents** laid out as an interactive org chart. You're at the top. Agents beneath you each have a role (their *charter*), a model, an account, and folder and tool permissions. They can hire reports, delegate, message each other, ask you for decisions, and track work on a shared docket ([README L3–21](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L3-L21)).

It doesn't replace the agent harnesses. It drives the Claude Code, Codex and Antigravity CLIs already installed and signed in, or OpenRouter models via an API key, so your CLAUDE.md files and skills keep working ([README L35–48](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L35-L48); [author comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/paf2u6v/)).

| Fact | Value (checked 2026-09-23) |
|---|---|
| Current version | V2, 2.1.12 (2026-09-22). V1 [claude-orgtree](https://github.com/Maurdekye/claude-orgtree) is deprecated |
| Platform | 64-bit Windows installer; other OSes build from source |
| Stack | Electron + React + TypeScript, bundled Python engine, SQLite storage |
| Data | Local, under `%APPDATA%\Orgtree v2\data`; inference still goes to your providers |
| Charter presets | `~/.orgtree/charters/*.md` (user-editable; bundled: coordinator, implementer, redteam, curator, review-workflow, business, a-list-team-coordinator) |

## How sources use it

- [[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]: the launch post and repo.
  - **Headline features:** the work docket, multi-account (several same-provider accounts running at once, each with its own tint), HTML presentations, pinned and popped-out windows, and a tray icon ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)).
  - **Author's own use:** parallel work development across several AI accounts, because coordinating agents by hand had become his bottleneck ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9fpwmz/)).

## Key mechanics

- **Credits.** A capacity budget, not money. Each agent holds a seat that depends on its model, plus a grant it can hand to its reports ([README L60–62](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L60-L62)).
- **Audiences.** An extra communication link, such as a direct line to you, for an agent that would otherwise be out of reach ([README L64–66](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L64-L66)).
- **Retire vs delete.** Retiring keeps an agent's history so it can be rehired; deleting is a separate action ([README L68](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L68)).
- **Account fallback.** Off by default. It applies only to Claude and Codex profiles with verified capacity, and a switch starts a new provider cache ([README L78–85](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L78-L85)).
- **Carried over from V1:** compaction by splitting, watchdogs and the mail hub. See the Source note.

## Notes

- **Alternatives.**
  - Paperclip is the comparison raised in the thread. The author describes Paperclip as more opinionated ("run your AIs like a CEO") and Orgtree as a free-form sandbox ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9ia1qk/)).
  - Inside Claude Code, the built-in options are subagents and agent teams. See [[Subagents and Agent Teams]].
- **Safety.** V2 dropped V1's Docker sandboxing, so folder and tool grants are the fence. V1's README warns that an agent with Bash can get around read-only folder rules. See [[Permissions and Approval Gates]].

## Related

- [[Persistent Agent Organizations]] · [[Run a Coordinator-Led Agent Team in Orgtree]] · [[Write Role Charters for a Multi-Agent Team]] · [[Claude Code]] · [[OpenAI Codex]] · [[Agentic OS]]
