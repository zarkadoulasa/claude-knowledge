---
type: concept
aliases: ["Agent Org Chart", "Agent Hierarchy", "Persistent Agent Team", "Tree of Authority"]
sources: ["[[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]"]
tags: [topic/agents, topic/subagents, topic/agentic-os, topic/permissions, topic/context]
---

# Persistent Agent Organizations

## In one sentence

Instead of spinning up throwaway helpers for one task, you keep a standing team of long-lived, addressable agents arranged in a tree of authority. Each has a role, a budget and permissions, and they delegate and message each other within the tree's rules.

## How it works

Standard subagents live and die inside one task and report back to their caller (see [[Subagents and Agent Teams]]). A persistent organization changes four things. This framing is the vault's, drawn from [[Orgtree]]:

| Dial | Ephemeral subagents | Persistent organization |
|---|---|---|
| **Lifetime** | One task | Survives across tasks and restarts. Retiring keeps history so the agent can be rehired ([README L68](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L68)) |
| **Who hires** | The main session | Any agent can hire its own reports ([V1 README L40–41](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L40-L41)) |
| **Who talks to whom** | Caller ↔ helper | Down to any depth, up one hop, sideways to peers. Reaching the human needs an *audience* ([V1 README L53–59](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L53-L59)) |
| **What limits it** | Your usage limit | A credit budget: seats plus grants that flow down the tree. A parent can't grant tools or folders it doesn't hold ([V1 README L41–43, L57–59](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L41-L59)) |

Three supporting pieces make it work at scale:

1. **A shared work docket.** Agents file and update tickets themselves, so the state of 20+ agents fits on one board ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)).
2. **Role charters.** Standing instructions per seat (coordinator, implementer, redteam, curator) that hold across tasks ([README L53](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L53)). See [[Write Role Charters for a Multi-Agent Team]].
3. **Context that outlives the window.** A node near its limit splits into a compacted successor. The old self stays consultable ([V1 README L64–67](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L64-L67)). Compare [[Context Window Management]].

## When to use it, and when not to

**Use it when:**

- **You routinely run many agents in parallel,** and coordinating them by hand has become the bottleneck ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9fpwmz/)).
- **Specialists need to keep context between tasks.** A reviewer who remembers last week's design, for example.

**Hold off when:**

- **You don't have repeatable workflows yet.** [[Ras Mic - How AI Agents and Claude Skills Work]] warns against starting with many agents before any workflow exists ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)).
- **Your plan limits are tight.** Many live agents burn usage fast (see the cost points in [[Subagents and Agent Teams]]).
- **A one-off task fits a single session with a few subagents.**

## Perspectives from sources

- **[[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]** argues the tree beats a list. You can see every agent's place, move agents up and down the hierarchy, and click into any one to chat ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)). He insists the tree is only a suggestion inside a sandbox: you can also run it as a flat set of chats that happen to talk to each other ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9ia1qk/)). The V1 README says the same: siblings can always reach each other, so a flat org is fully connected ([V1 README L27–36](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L27-L36)).
- **Recommended shape.** One strong coordinator under you, and workers flat beneath it, each given a direct line to you ([V1 README L135–139](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L135-L139)). This is the hub pattern from [[Subagents and Agent Teams]], made permanent.

## Where sources disagree

- **Ready-made vs self-built.** Orgtree and Paperclip are ready-made multi-agent systems. [[Ras Mic - How AI Agents and Claude Skills Work]] liked Paperclip but thinks most people get more done building their own ([14:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=888s)–[14:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=899s)). DynaBeast's answer is that Orgtree is a sandbox of tools rather than a fixed framework.
- **Opinionated vs free-form.** DynaBeast describes Paperclip as CEO-style and opinionated, and Orgtree as open-ended ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9ia1qk/)). Paperclip hasn't been ingested, so this is one side's view.

## Beyond the source

- **Built-in alternatives.** Claude Code's own teams feature is experimental and not persistent in the same way: teammates share a task list and message each other within a session. <https://code.claude.com/docs/en/agent-teams>
- **Hosted equivalent.** [[Claude Managed Agents]] multiagent sessions give each agent its own persistent thread, but delegation goes one level deep (see Beyond the source in [[Subagents and Agent Teams]]).

## Related

- **Concepts:** [[Subagents and Agent Teams]] · [[Agentic OS]] · [[Permissions and Approval Gates]] · [[Context Window Management]] · [[Agent Memory Patterns]]
- **Techniques:** [[Run a Coordinator-Led Agent Team in Orgtree]] · [[Write Role Charters for a Multi-Agent Team]] · [[Parallel Sessions with Git Worktrees]]
- **Tools:** [[Orgtree]] · [[Claude Code]] · [[Claude Managed Agents]]
- **People:** [[DynaBeast]] · [[Ras Mic]]
