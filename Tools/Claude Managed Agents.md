---
type: tool
category: hosted agent harness and API suite (Anthropic, beta)
website: https://platform.claude.com/docs/en/managed-agents/overview
sources: ["[[Anthropic - What Is Claude Managed Agents]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]"]
tags: [topic/managed-agents, topic/agents, topic/verification, topic/memory, topic/subagents, topic/permissions, topic/mcp, topic/skills, topic/automation]
---

# Claude Managed Agents

## What it is

In [[Anthropic - What Is Claude Managed Agents]], Anthropic presents Claude Managed Agents as a set of APIs for building agents and deploying them at scale ([00:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=2s)). You define the pieces, and your own application starts the work ([00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s)). The video names three building blocks:

| Block | What you configure (per the video) | Where |
|---|---|---|
| **Agent** | Its tools, persona and capabilities | [00:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=11s) |
| **Environment** | A sandbox with the right packages and network controls | [00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s) |
| **Session** | Started from your own application. Claude works in an isolated container with full filesystem access, bash and web search | [00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s), [00:24](https://www.youtube.com/watch?v=NLWiIj47IdI&t=24s), [00:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=26s) |

The closing summary calls it a fully managed, stateful agent experience ([03:34](https://www.youtube.com/watch?v=NLWiIj47IdI&t=214s)). It lists the parts as agents, sessions, environments, tools, MCP, memory, outcomes and multi-agent coordination ([03:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=218s)). The pitch is that you say what done looks like and Claude works until it gets there ([03:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=225s)). Notes explains the limit on that claim, and current status is under Beyond the source.

## How sources use it

### [[Anthropic - What Is Claude Managed Agents]]

The video consists of three scripted demos.

| Capability | What the video shows | Where | Vault notes |
|---|---|---|---|
| Event-triggered sessions | A card drag starts a session; a monitoring alert reaches a new session as a tool result through a custom tool | [00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s), [02:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=158s) | [[Build an Event-Triggered Managed Agent]] |
| Configured environments | Lighthouse and Puppeteer pre-installed; GitHub repo mounted | [00:49](https://www.youtube.com/watch?v=NLWiIj47IdI&t=49s), [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s) | |
| Live event stream | Every tool call appears on the board in real time | [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s) | |
| Outcomes | Rubric of checkable criteria; a separate grader with its own context window; Claude revises and resubmits | [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s), [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s), [01:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=83s) | [[Verification Before Done]] |
| Parallel sessions | A second ticket runs in a second container | [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s) | |
| Skills and MCP | Excel spreadsheet skill; Slack and Asana through MCP servers | [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s), [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s) | [[Agent Skills]], [[Connecting Claude to External Tools]] |
| Memory stores | Reads the last run first, stores changes last; past incidents flag a repeat | [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s), [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s) | [[Agent Memory Patterns]] |
| Coordinator and specialists | Three specialists, each with its own context window, share one filesystem; the coordinator merges their findings | [02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s), [02:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=168s), [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s) | [[Subagents and Agent Teams]] |
| Permission policy with human approval | The policy fires before the Slack post; the draft is approved on screen | [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s), [03:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=185s) | [[Permissions and Approval Gates]] |

**The three demos**

1. **Kanban coding agent.**
   - Dragging a card to In Progress starts a session ([00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s)). The session's environment has Lighthouse and Puppeteer, and the repo is mounted ([00:49](https://www.youtube.com/watch?v=NLWiIj47IdI&t=49s), [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s)).
   - The rubric: Lighthouse above 90, no render-blocking resources, all images lazy-loaded ([00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s)–[01:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=62s)).
   - Claude runs the audit, then compresses images, inlines CSS and defers scripts ([01:04](https://www.youtube.com/watch?v=NLWiIj47IdI&t=64s)).
   - After grader feedback and a resubmit, the score reaches 96 ([01:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=83s), [01:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=89s)). A second ticket runs in its own container at the same time ([01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s)).
2. **SaaS pricing watch.**
   - The report must be ready before stand-up ([01:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=108s)).
   - The agent searches pricing pages ([01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s)), checks for plan-tier changes and flags new features that could affect contracts ([01:55](https://www.youtube.com/watch?v=NLWiIj47IdI&t=115s)–[01:59](https://www.youtube.com/watch?v=NLWiIj47IdI&t=119s)). It runs a Python cost analysis ([02:01](https://www.youtube.com/watch?v=NLWiIj47IdI&t=121s)), builds a spreadsheet with an Excel skill and writes an executive summary ([02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s)–[02:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=125s)). It then posts a link to Slack and opens a review task in Asana through MCP ([02:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=128s)–[02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s)).
   - It reads last week's findings first and stores what changed last ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)). So the next Monday report states the change, such as cloud compute 15% lower, instead of repeating the same static prices ([02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s)–[02:28](https://www.youtube.com/watch?v=NLWiIj47IdI&t=148s)).
3. **Incident triage.**
   - A custom tool delivers a monitoring alert into a new session as a tool result ([02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s)–[02:40](https://www.youtube.com/watch?v=NLWiIj47IdI&t=160s)).
   - A coordinator splits the investigation across three specialists and merges their findings into one summary ([02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s), [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s)).
   - A permission policy holds the Slack post until a person approves ([03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s), [03:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=185s)).
   - Memory flags a repeat of a DNS issue caused by a misconfigured TTL, so the next similar alert starts with that context ([03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s), [03:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=201s)).

### [[Jay E - The ARMS Framework for a Claude Agentic OS]] (context, no mention by name)

[[Jay E]] describes people who get 24/7 routines by running Claude Code on a cloud server, so they don't need a file-sync tool ([17:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1071s)–[18:19](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1099s)). He thinks Anthropic or OpenAI may well offer such a setup ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)). Because of file storage and security concerns, though, he expects it later rather than now ([18:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1106s)).

*Vault reading:* Managed Agents partly meets that prediction. It provides hosted sessions with server-side memory, but as a developer API, not as a synced Claude Code workspace. His sync route still covers the workspace case; see [[Sync a Workspace to an Always-On Cloud Agent]] and [[Always-On Brain OS]].

## Notes

- **A promo, not a tutorial.**
  - There are no API calls, configuration, costs, latency or failures.
  - The board ([00:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=32s)) and the incident console are the narrator's own front ends.
  - Nothing shows what starts the weekly report ([01:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=108s)).
  - For a build plan, see [[Build an Event-Triggered Managed Agent]].
- **"Until it gets there" is left open-ended** ([03:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=225s)). The video shows no iteration cap and no failed run. The documented cap and end states are under Beyond the source.
- **Availability is dated.** The video's description (published 2026-04-09) put outcomes, multi-agent orchestration and memory in a limited research preview behind an early-access form. Current status is under Beyond the source.
- **The closing list is incomplete.** The demos also rely on skills ([02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s)), the event stream ([01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s)) and permission policies ([03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s)), none of which appear in the summary ([03:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=218s)).
- **How it differs from Claude Code.** See the last item under Beyond the source.

## Beyond the source

*Not said in the video. Checked on 2026-09-15 at the linked pages.*

- **Official description.** A pre-built, configurable agent harness running on managed infrastructure, for long-running and asynchronous work.
  - Four core concepts: agent (model, system prompt, tools, MCP servers and skills; versioned), environment (cloud or self-hosted sandbox), session, and events.
  - Events stream as server-sent events, and you can steer or interrupt a running session.
  - The built-in toolset is bash, read, write, edit, glob, grep, web fetch and web search.
  - Sources: [overview](https://platform.claude.com/docs/en/managed-agents/overview) · [tools](https://platform.claude.com/docs/en/managed-agents/tools) · [quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).
- **Status.**
  - Still beta: calls need the `managed-agents-2026-04-01` header, except memory store endpoints, which use `agent-memory-2026-07-22`. Access is on by default for API accounts.
  - Dreaming and MCP tunnels need an access request.
  - Also offered on Claude Platform on AWS, with some differences, but not on partner-operated clouds.
  - Because sessions are stored server-side, it isn't eligible for Zero Data Retention or HIPAA BAA coverage.
  - Sources: [overview](https://platform.claude.com/docs/en/managed-agents/overview) · [pricing](https://platform.claude.com/docs/en/about-claude/pricing).
- **Timeline.**
  - 2026-04-08: launch as a public beta. Multi-agent coordination and outcomes (self-evaluation) were research previews behind an access request; the video description also puts memory in that group.
  - 2026-04-23: memory reaches public beta.
  - May 2026: outcomes and multiagent orchestration join memory in public beta, webhooks become available, and dreaming arrives as a research preview. The Anthropic post's page is dated 2026-05-19; an SD Times newswire copy of it ran on 2026-05-06.
  - 2026-06-09: scheduled deployments and vaults reach public beta.
  - Anthropic says that in its own testing, outcomes raised task success by up to 10 points over a standard prompting loop. That is a vendor figure.
  - Sources: [launch](https://claude.com/blog/claude-managed-agents) · [memory](https://claude.com/blog/claude-managed-agents-memory) · [May update](https://claude.com/blog/new-in-claude-managed-agents) · [SD Times](https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/) · [June update](https://claude.com/blog/whats-new-in-claude-managed-agents).
- **Pricing.**
  - Tokens are billed at model rates, with caching multipliers and no Batch discount.
  - Web searches cost $10 per 1,000.
  - Runtime costs $0.08 per session-hour and accrues only while a session is `running`.
  - Optional per-session budgets set a hard spend cap, and the session pauses (goes idle with `budget_reached`) when it's reached. The amount is whole US cents written as a string, so `"125"` means $1.25. The request already in flight still finishes, so spend can land slightly past the cap, by at most one model request per thread.
  - Sources: [pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [budgets](https://platform.claude.com/docs/en/managed-agents/budgets).
- **Documented limits.**

  | Area | Limit | Source |
  |---|---|---|
  | Outcomes | `max_iterations` default 3, max 20. Each evaluation returns `needs_revision` (another round) or ends the outcome as `satisfied`, `max_iterations_reached`, `failed` (the rubric doesn't fit the deliverable) or `interrupted`. One outcome at a time; the grader has its own context window and no web tools | [define outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes), [tools](https://platform.claude.com/docs/en/managed-agents/tools) |
  | Memory | 8 stores per session, attached at creation only; `instructions` up to 4,096 characters; 100 kB per memory; 10,000 memories per store; versions kept 30 days (recent versions of live memories longer) | [memory](https://platform.claude.com/docs/en/managed-agents/memory) |
  | Multiagent | One delegation level; 20 roster agents; 25 concurrent threads | [multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) |
  | Sessions | `initial_events`: up to 50, only `user.message` or `user.define_outcome`. A budget can only be attached at creation, though its cap can be changed or removed later | [sessions](https://platform.claude.com/docs/en/managed-agents/sessions), [budgets](https://platform.claude.com/docs/en/managed-agents/budgets) |
  | Skills | 500 per session | [skills](https://platform.claude.com/docs/en/managed-agents/skills) |
  | Tools | Output over 100,000 characters goes to a file; web domain lists hold 1–64 entries | [tools](https://platform.claude.com/docs/en/managed-agents/tools) |
  | Vaults | 20 credentials per vault | [vaults](https://platform.claude.com/docs/en/managed-agents/vaults) |
  | Scheduled deployments | 1,000 per organisation; minute-level cron; jitter up to 15% of the interval, capped at 9 minutes | [scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) |
  | Webhooks | Up to three delivery attempts, then dropped; no ordering guarantee | [webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) |
  | Dreams | 1–100 sessions per dream, written to a new store | [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) |

- **Safety defaults the video skips.**
  - **Tool approvals.** The built-in toolset defaults to `always_allow`, and MCP toolsets to `always_ask`. `auto` is not a human checkpoint, and custom tools aren't governed by any policy. Source: [permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies).
  - **Memory.** Stores attach `read_write` by default, and the docs warn that prompt injection can plant memories later sessions trust. They recommend `read_only` for reference material. Source: [memory](https://platform.claude.com/docs/en/managed-agents/memory).
  - **Networking.** Environment networking doesn't restrict web search or fetch; use per-tool domain lists instead. Source: [environments](https://platform.claude.com/docs/en/managed-agents/environments).
  - **Mounted repos.** Skills in a mounted repo's `.claude/skills` load automatically, which puts that repo inside the agent's trust boundary. Source: [skills](https://platform.claude.com/docs/en/managed-agents/skills).
- **Recurring runs.** Scheduled deployments start sessions on a cron schedule. That covers the before-stand-up report the video never shows being triggered. Source: [scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments).
- **How it differs from Claude Code** (vault comparison built on these docs).
  - With Managed Agents, Anthropic runs the harness, and each session gets its own isolated sandbox. Your application drives the work through events. Sources: [overview](https://platform.claude.com/docs/en/managed-agents/overview) · [environments](https://platform.claude.com/docs/en/managed-agents/environments).
  - [[Claude Code]] is a harness you drive yourself. Its hosted, unattended option on Pro, Max, Team and Enterprise plans is routines (research preview), which run without approval prompts. See [[Routines and Scheduled Tasks]]. Source: [routines](https://code.claude.com/docs/en/routines).
  - Memory stores are workspace-scoped collections mounted into the session sandbox under `/mnt/memory/`. That is a different system from [[Claude Code Auto Memory]]. Source: [memory](https://platform.claude.com/docs/en/managed-agents/memory).

## Related

- **Source:** [[Anthropic - What Is Claude Managed Agents]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- **Techniques:** [[Build an Event-Triggered Managed Agent]] · [[Build Verification into Every Task]] · [[Configure Safe Autonomy Permissions]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]]
- **Concepts:** [[Verification Before Done]] · [[Agent Memory Patterns]] · [[Subagents and Agent Teams]] · [[Permissions and Approval Gates]] · [[Connecting Claude to External Tools]] · [[Agent Skills]] · [[Routines and Scheduled Tasks]] · [[Claude Code Auto Memory]] · [[Always-On Brain OS]]
- **Tools:** [[Claude Code]]
- **People:** [[Jay E]]
- [[Home]]
