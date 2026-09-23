---
type: technique
goal: Stand up an Orgtree organization with one coordinator and a flat team of workers on a real project
difficulty: intermediate
time_to_build: 1–2 hours
sources: ["[[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]"]
tools: ["[[Orgtree]]", "[[Claude Code]]", "[[OpenAI Codex]]"]
tags: [topic/agents, topic/subagents, topic/agentic-os, topic/permissions, topic/claude-code]
---

# Run a Coordinator-Led Agent Team in Orgtree

## Goal

Build a persistent Orgtree org for one project. A strong coordinator sits directly under you, and workers sit side by side beneath it. Every piece of work is on the docket, each agent is scoped to the folders it needs, and your accounts are allocated deliberately.

## Use when

- You already run several Claude Code or Codex sessions on one project and coordinating them by hand is slowing you down.
- You're on Windows, or willing to build from source.

## Prerequisites

- 64-bit Windows and the latest installer (`Orgtree-Setup-<version>.exe`) from the [releases page](https://github.com/Maurdekye/orgtree/releases/latest). No separate Node or Python is needed ([README L25–33](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L25-L33)).
- At least one provider CLI installed and signed in: Claude Code, Codex, Antigravity, or an OpenRouter key ([README L35–44](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L35-L44)).
- The project in a git repo, with its CLAUDE.md and skills in place. Orgtree reuses them as they are ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/paf2u6v/)).
- Charters written or chosen. See [[Write Role Charters for a Multi-Agent Team]].

## Steps

1. **Install and onboard.** Run the installer and launch Orgtree from the Start menu. On the setup card, pick a theme and startup behaviour, then create your first org. Finishing setup copies the bundled charter presets into `~/.orgtree/charters/` ([onboarding doc](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/docs/v2-onboarding.md)).
2. **Connect providers.** Go to **App settings → Providers**. To add a second account, use the add-account button in that provider's header and choose "Create managed account", then sign in from the browser ([README L37–46](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L37-L46); [post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)).
3. **Set the org budget.** Credits cap how many agents can hold seats at once, not dollars. Size the budget to the concurrency your plan limits can actually sustain ([README L60–62](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L60-L62)).
4. **Start with one agent and a small task** before adding a team ([README L58](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L58)). Give it a concrete result, its constraints, and how you'll know it's finished ([README L55](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L55)).
5. **Hire the coordinator.** Use a top-tier model and the `coordinator` charter preset. Leave its tool switches on, because a parent can only grant reports what it holds, and the charter is what keeps it from implementing ([coordinator charter L3–11](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L3-L11)).
6. **Let the coordinator staff flat.** Ask for a feature. The coordinator should put it on the docket, hire one worker per piece directly under itself, and send each worker its first task in the same call as the hire ([coordinator L23–36](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md#L23-L36)). Each worker gets a direct line (audience) to you ([V1 README L135–139](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L135-L139)).
7. **Scope every worker.** Grant only the folders and tools its piece needs ([README L54](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L54)). Parallel implementers editing code should each have their own worktree. See [[Parallel Sessions with Git Worktrees]].
8. **Allocate accounts deliberately.** Choose which account each agent uses when you hire it. Leave automatic fallback (**Settings → Autonomy**) off until you trust it. When a switch happens, it starts a fresh provider cache ([README L78–85](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L78-L85)).
9. **Supervise from the docket.** Watch the docket and the inbox rather than individual chats. Pin the coordinator's chat and the docket as windows, and click into an agent only when a ticket stalls ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)).
10. **Add review seats** as features grow: a redteam under the coordinator, per the review-workflow preset. See [[Write Role Charters for a Multi-Agent Team]].
11. **Retire rather than delete.** Retiring frees capacity and keeps history for a later rehire ([README L68](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L68)).

## Starter files & prompts

First message to the coordinator:

```
Project: <repo path>. Goal for this week: <feature>.
Docket it first, split it into independently shippable pieces, and staff one worker per piece
directly under you. Give each worker only the folders it needs and its own git worktree.
Each ticket is done only when it links a passing test run or a screenshot.
Ask me only for decisions about scope or anything irreversible.
```

## Done when

- [ ] Orgtree is running in the tray and at least one provider shows as signed in.
- [ ] One coordinator is under you and the workers are flat beneath it, each with a charter.
- [ ] Every active piece of work has a docket ticket with an owner and status.
- [ ] Each worker's folder grants cover only its piece, and parallel implementers use separate worktrees.
- [ ] Account choice per agent is deliberate, and fallback is off or consciously enabled.
- [ ] A finished ticket links evidence, not just a claim.

## Pitfalls

- **Limits still bind.** Orgtree includes no model access ([README L48](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L48)). A big team can use up a plan quickly.
- **No sandbox in V2.** Sandboxing was dropped ([post](https://www.reddit.com/r/claudeskills/comments/1wejev5/orgtree_v2_now_an_app/)), and an agent with Bash can get around folder rules ([V1 README L601–604](https://github.com/Maurdekye/claude-orgtree/blob/a8199a598f0c62216ed41cf3e1a099d46517f43d/README.md#L601-L604)). Don't point it at folders holding secrets.
- **V1 data doesn't move by itself.** Use the explicit V1 import in Settings ([README L87–93](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L87-L93)).
- **No session import.** Existing Claude Code chats don't come across. Let the context files carry the knowledge ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/paf2u6v/)).
- **Early software.** Frequent releases, one maintainer. Auto-update is on by default ([README L74](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md#L74)).
- **Account terms.** Check your provider's terms before running several subscription accounts in parallel (see Beyond the source in the Source note).

## Variations

- **Flat chats.** Skip the coordinator and use Orgtree as a set of chats that can message each other ([comment](https://www.reddit.com/r/claudeskills/comments/1wejev5/comment/p9ia1qk/)).
- **Without Orgtree.** Use Claude Code agent teams or subagents with the same charters and a `DOCKET.md`. See [[Subagents and Agent Teams]].

## Sources

- [[DynaBeast - Orgtree v2 Multi-Agent Orchestrator App]]

## Related

- [[Persistent Agent Organizations]] · [[Write Role Charters for a Multi-Agent Team]] · [[Configure Safe Autonomy Permissions]] · [[Parallel Sessions with Git Worktrees]] · [[Orgtree]]
