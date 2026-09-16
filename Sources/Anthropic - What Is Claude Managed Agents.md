---
type: source
title: "What is Claude Managed Agents?"
creator: "Anthropic (Claude channel)"
channel: "Claude"
url: https://www.youtube.com/watch?v=NLWiIj47IdI
video_id: NLWiIj47IdI
published: 2026-04-09
duration: "3:52"
ingested: 2026-09-15
topics: [claude managed agents, agent sessions, sandbox environments, outcomes, rubric grading, memory stores, multi-agent orchestration, permission policies, event-triggered agents, mcp]
tags: [source/youtube, topic/managed-agents, topic/agents, topic/verification, topic/memory, topic/subagents, topic/permissions, topic/mcp, topic/skills, topic/automation, topic/scheduling]
---

# Anthropic - What Is Claude Managed Agents

> **Creator:** Anthropic (Claude channel) · **Published:** 2026-04-09 · **Length:** 3:52 · [Watch on YouTube](https://www.youtube.com/watch?v=NLWiIj47IdI)

## TL;DR

This is Anthropic's official launch explainer for [[Claude Managed Agents]], posted on the Claude channel the day after launch. An unnamed narrator presents it as a set of APIs for building agents and running them at scale. You set up three things:

- an **agent**: its tools, persona and capabilities
- an **environment**: packages and network controls
- a **session**, started by your own app, in which Claude works inside an isolated container with a filesystem, bash and web search.

Three scripted demos show the parts:

1. **Kanban coding agent.** Moving a ticket to In Progress starts a session with Lighthouse and Puppeteer installed and the GitHub repo mounted. A separate grader checks the work against a rubric, Claude revises on its feedback, and the Lighthouse score reaches 96. A second ticket runs at the same time in its own container.
2. **SaaS pricing watcher.** It uses web search, Python, an Excel skill, and Slack and Asana through MCP. A memory store means each weekly report shows only what changed.
3. **Incident triage.** A custom tool passes an alert into a new session. A coordinator hands the work to three specialists, and a permission policy holds the Slack update until a person approves it. Memory of a past DNS incident flags a repeat.

The slogan at the end: describe the finished state, and Claude iterates until it reaches it.

This is marketing. There's no code, configuration, cost or failure case. At publication, outcomes, multi-agent coordination and memory were an apply-for-access research preview (per the video description). All three have since reached public beta, and the revision loop has an iteration cap (Beyond the source).

## Key takeaways

- **Three objects, then a run.** An agent [00:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=11s), an environment [00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s), and a session your app starts [00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s). The session runs in an isolated container with filesystem, bash and web search [00:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=26s). See [[Claude Managed Agents]].
- **Your software starts the agent, not a chat box.** A board move [00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s) and a monitoring alert delivered through a custom tool [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s) each open a session. See [[Build an Event-Triggered Managed Agent]].
- **Define done as checks a machine can confirm.** The demo rubric asks for Lighthouse above 90, no render-blocking resources, and lazy-loaded images [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s). See [[Verification Before Done]].
- **Keep the judge out of the worker's context.** A grader with its own context window evaluates the output; Claude uses that feedback to revise and resubmit [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s), [01:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=81s). See [[Build Verification into Every Task]].
- **You can watch it work.** Each tool call appears live in your app via the event stream [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s).
- **Parallel work = one session per task.** A second ticket gets its own container [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s). The local Claude Code equivalent is [[Parallel Sessions with Git Worktrees]] (vault link, not from the video).
- **Skills and MCP reach other tools.** The spreadsheet comes from an Excel skill, and Slack and Asana are reached through MCP servers [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s), [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s). See [[Connecting Claude to External Tools]].
- **Read memory first, record changes last.** This turns a weekly report into a list of what changed [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s), and lets an incident agent recognise a repeat problem [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s). See [[Agent Memory Patterns]]; compare [[Claude Code Auto Memory]].
- **Split investigation across specialists.** Each specialist has its own context window, but all share one filesystem [02:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=168s); the coordinator merges their findings [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s). See [[Subagents and Agent Teams]].
- **Gate side effects on a person.** A permission policy stops the Slack post until the draft is approved [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s). See [[Permissions and Approval Gates]] and [[Configure Safe Autonomy Permissions]].

## The three demos at a glance

Everything in this table comes from the narration. "Not shown" means the video doesn't cover it.

| | Demo 1: Kanban coding agent | Demo 2: SaaS pricing watch | Demo 3: Incident triage |
|---|---|---|---|
| **Trigger** | Card dragged to In Progress; backend creates the session [00:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=45s) | Not shown. The report must be ready before stand-up [01:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=108s) | Monitoring alert, fed in through a custom tool [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s) |
| **Environment / resources** | Lighthouse and Puppeteer pre-installed [00:47](https://www.youtube.com/watch?v=NLWiIj47IdI&t=47s); repo mounted [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s) | Python runs in the sandbox [01:59](https://www.youtube.com/watch?v=NLWiIj47IdI&t=119s) | Specialists share one filesystem [02:50](https://www.youtube.com/watch?v=NLWiIj47IdI&t=170s) |
| **Tools, skills, MCP** | Audit, image compression, inlined CSS, deferred scripts [01:07](https://www.youtube.com/watch?v=NLWiIj47IdI&t=67s) | Web search [01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s); Excel skill [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s); Slack and Asana via MCP [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s) | Custom tool; Slack post [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s) |
| **Feature shown** | Rubric plus separate grader [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s); event stream [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s); parallel sessions [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s) | Memory store: read before, write after [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s) | Multi-agent coordination [02:42](https://www.youtube.com/watch?v=NLWiIj47IdI&t=162s); permission policy [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s); incident memory [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s) |
| **Human role** | Moves the card and watches; no approval step | An Asana review task is opened [02:10](https://www.youtube.com/watch?v=NLWiIj47IdI&t=130s); the review itself isn't shown | Approves the draft [03:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=185s) |
| **Output** | Lighthouse 96 [01:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=89s) | Spreadsheet, summary, Slack link, week-on-week changes [02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s) | One incident summary [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s); match to a past DNS issue [03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s) |

## Notes by chapter

The metadata has no chapters, so these sections follow the video's segments.

### [00:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=0s) What Managed Agents is

- A set of APIs for building agents and deploying them at scale [00:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=2s).
- **Agents** are defined by their tools, personas and capabilities [00:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=11s).
- **Environments** are sandboxes set up with the right packages and network controls [00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s).
- **Sessions** are started by your own application [00:20](https://www.youtube.com/watch?v=NLWiIj47IdI&t=20s). Claude then works in an isolated container with full filesystem access, bash and web search [00:24](https://www.youtube.com/watch?v=NLWiIj47IdI&t=24s).
- *Vault framing:* who does the work, where it runs, and one run of it. The docs add a fourth core concept, events (Beyond the source).

### [00:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=32s) Demo 1: a Kanban board that starts coding sessions

- **The board.** The narrator's own board is built on top of Managed Agents [00:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=32s). The captions are garbled here (Transcript notes).
- **Trigger.** Moving a card to In Progress starts a session automatically [00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s). The ticket asks for faster website performance [00:40](https://www.youtube.com/watch?v=NLWiIj47IdI&t=40s).
- **What the backend sets up.** It creates a session [00:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=45s) that uses an environment with Lighthouse and Puppeteer pre-installed [00:47](https://www.youtube.com/watch?v=NLWiIj47IdI&t=47s), and mounts the GitHub repo into the container [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s). Claude therefore has the codebase, the tools and a rubric [00:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=54s).
- **The rubric.** Lighthouse above 90 [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s), no render-blocking resources [00:59](https://www.youtube.com/watch?v=NLWiIj47IdI&t=59s), every image lazy-loaded [01:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=62s).
  - *Vault observation:* each criterion is pass/fail and machine-checkable, which is what makes it gradeable.
- **The work.** Claude runs the audit [01:04](https://www.youtube.com/watch?v=NLWiIj47IdI&t=64s), then compresses images, inlines CSS and defers scripts [01:07](https://www.youtube.com/watch?v=NLWiIj47IdI&t=67s).
- **Live view.** The board shows each tool call as it happens, fed by the session's event stream [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s).
- **Grading loop.** A separate grader with its own context window checks the output against the criteria [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s). Claude takes its feedback, fills the gaps and submits again [01:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=83s). See [[Verification Before Done]] and [[Build Verification into Every Task]].
- **Result.** The score reaches 96 [01:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=89s). No starting score, round count or runtime is given.
- **Parallel work.** A second ticket can start while the first is mid-run [01:31](https://www.youtube.com/watch?v=NLWiIj47IdI&t=91s). That means two sessions and two containers working separately at once [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s).

### [01:41](https://www.youtube.com/watch?v=NLWiIj47IdI&t=101s) Demo 2: a weekly SaaS pricing report with memory

- **The job.** This agent tracks price and plan changes for every SaaS product the company pays for, with a report ready before stand-up [01:43](https://www.youtube.com/watch?v=NLWiIj47IdI&t=103s). What starts each run isn't shown.
- **Research.** Claude finds current pricing pages by web search [01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s), looks for plan-tier changes [01:55](https://www.youtube.com/watch?v=NLWiIj47IdI&t=115s), and flags new features that could affect contracts [01:57](https://www.youtube.com/watch?v=NLWiIj47IdI&t=117s).
- **Analysis.** A Python cost analysis runs inside the sandbox [01:59](https://www.youtube.com/watch?v=NLWiIj47IdI&t=119s).
- **Deliverables.** Claude builds the spreadsheet with an Excel skill and adds an executive summary [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s). See [[Agent Skills]].
- **Hand-off.** Claude shares the report link in Slack and opens an Asana task for review [02:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=128s), both through MCP servers [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s). See [[Connecting Claude to External Tools]].
- **Memory.** The agent has read and write access to a memory store [02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s). It first looks at last week's findings [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), and at the end records what changed [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s).
- **Payoff.** The following Monday's report leads with the change (their example: cloud compute down 15% on last week) [02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s), not a repeat of static price lists [02:28](https://www.youtube.com/watch?v=NLWiIj47IdI&t=148s). See [[Agent Memory Patterns]].

### [02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s) Demo 3: alert-triggered incident triage with an approval gate

- **Trigger.** An alert fires from the narrator's monitoring stack [02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s).
- **How the alert gets in.** Their backend picks up the payload through a custom tool and delivers it to a fresh session as a tool result [02:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=158s). Captions lack punctuation here (Transcript notes).
- **Coordination.** The session uses multi-agent coordination [02:42](https://www.youtube.com/watch?v=NLWiIj47IdI&t=162s).
  - A coordinator takes the alert and hands parts of it to three specialist agents [02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s).
  - Each specialist has a separate context window, and they all work on one shared filesystem [02:50](https://www.youtube.com/watch?v=NLWiIj47IdI&t=170s).
  - The specialists' roles aren't named. See [[Subagents and Agent Teams]].
- **Synthesis.** The specialists report back [02:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=174s), and the coordinator merges their results into one incident summary [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s).
- **Approval gate.** Before the Slack update goes out, the permission policy triggers [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s). The narrator reviews the draft on screen, approves it, and it posts [03:05](https://www.youtube.com/watch?v=NLWiIj47IdI&t=185s). See [[Permissions and Approval Gates]].
- **Memory.** Memory connects the pieces [03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s).
  - The coordinator looks through earlier incidents stored in memory and spots a match [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s).
  - The match is a DNS resolution problem from two weeks before, caused by a wrong TTL setting [03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s).
  - When a similar alert comes in later, the agent begins with that history rather than re-diagnosing from zero [03:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=201s).
- *Vault reading:* the narration mentions the memory check after the approval. Logically, though, a match would feed into the summary before it's posted. The real order isn't shown.

### [03:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=212s) The building blocks and the closing promise

- Anthropic frames the product as a fully managed, stateful agent experience for developers [03:34](https://www.youtube.com/watch?v=NLWiIj47IdI&t=214s).
- The listed blocks are agents, sessions, environments, tools, MCP, memory, outcomes and multi-agent coordination [03:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=218s).
- The list leaves out three things the demos relied on:
  - skills [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s)
  - the event stream [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s)
  - permission policies [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s).
- **Closing line** [03:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=225s): you specify what done means, and Claude keeps at it until it gets there. This is Demo 1's rubric loop as a slogan (see Caveats).

## Caveats & disagreements

**About the video itself**

- **Marketing, not a tutorial.** No API calls, agent definitions, rubric files, costs, latency or failed runs are shown. Every buildable detail below comes from the docs (Beyond the source). The board [00:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=32s) and the incident console are the narrator's own front ends: they refer to their own backend [00:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=45s), [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s). Neither appears to be a Managed Agents product screen (vault inference).
- **One staged number.** Lighthouse reaches 96 [01:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=89s), but no baseline, round count, time or token cost is given.
- **"Until it gets there" is overstated** [03:45](https://www.youtube.com/watch?v=NLWiIj47IdI&t=225s). Outcomes stop after `max_iterations` (default 3, maximum 20), and a run can end as `max_iterations_reached` or `failed` (Beyond the source).
- **Availability has changed.** The description says outcomes, multi-agent orchestration and memory were a limited research preview you had to apply for. Memory reached public beta on 2026-04-23, and outcomes and orchestration followed in May 2026. The product as a whole is still in beta (Beyond the source).
- **The recurring trigger is missing.** Demo 2 has to run before stand-up and again the next Monday [01:48](https://www.youtube.com/watch?v=NLWiIj47IdI&t=108s), [02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s), but no scheduler is shown. Scheduled deployments, in public beta since June 2026, now cover this (Beyond the source).
- **Black boxes.** The specialists' roles, models and prompts aren't shown [02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s). Nor is how the past DNS incident got into memory [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s).
- **Missing safety details.** All of these are from the docs (Beyond the source):
  - **Memory poisoning.** The pricing agent reads live web pages [01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s) and writes to memory [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s). With `read_write` access, which is the default, a prompt injection in fetched content can plant memories that later sessions trust.
  - **Unguarded alert input.** Demo 3's alert arrives through a custom tool [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s). Permission policies don't cover custom tools, so validating that payload is your job.
  - **Approvals in Demo 2.** MCP toolsets default to `always_ask`, but Demo 2's Slack and Asana actions [02:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=128s) show no approval step. Presumably those servers were set to `always_allow` (vault inference).
  - **`auto` isn't approval.** The `auto` policy is not a human checkpoint: the server can run a call it judges safe before anyone sees it. Only `always_ask` guarantees the approval shown at [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s).
  - **Data retention.** Managed Agents isn't eligible for Zero Data Retention or HIPAA BAA coverage.
- **No pricing and no sponsor.** Pricing is standard token rates plus $0.08 per active session-hour (launch blog). The video is Anthropic's own promotion.

**Conflicts with existing vault notes (both sides kept)**

- **[[Always-On Brain OS]]: who runs the always-on part.**
  - *Vault:* [[Nate Herk - Every Level of a Claude Second Brain]] says an always-on brain in Claude Code means managing cron jobs yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)), and he prefers pairing GBrain with Hermes Agent ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)).
  - *This video:* a recurring agent runs on Anthropic's infrastructure and carries memory from one run to the next [02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s), [02:23](https://www.youtube.com/watch?v=NLWiIj47IdI&t=143s).
  - *Reconciled:* there is now a first-party hosted route. It's a developer API billed per token and session-hour, not a Claude Code setting, and scheduling was added later (Beyond the source). Nate's point still holds for a brain that lives only in Claude Code.
- **[[Claude Code Auto Memory]]: where memory lives.**
  - *Vault:* auto memory is a `MEMORY.md` index plus topic files, kept per project on one machine and not shared with cloud environments (that note's Beyond the source).
  - *This video:* a store that agents read before each run and write after, across weeks [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s) and across incidents [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s).
  - *Reconciled:* these are different systems. Managed Agents stores are workspace-scoped, server-side, versioned, and can be attached to many sessions (Beyond the source). Cross-link the notes; don't merge them.
- **[[Context vs Connections]]: storing volatile data.**
  - *Vault:* Nate keeps fast-changing data such as Slack, email and customer records out of the brain because it becomes noise ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)). His test is whether it would still help in a year ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)).
  - *This video:* prices are fetched live every run [01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s), which agrees. But the agent also stores what changed [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s), so the report can show deltas [02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s).
  - *Reconciled:* keep raw volatile data out. Derived change history and root causes, such as the DNS TTL finding [03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s), can pass the one-year test.
- **[[Tool-Agnostic Context Files]]: portability.**
  - *Vault:* Nate's brain is just files and folders, so different agent harnesses can use it ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).
  - *This video:* memory lives in the platform's store [02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s).
  - *Reconciled:* per the docs, memories are text documents stored at paths, which you can edit, seed and export through the API. Portability therefore needs an export step (Beyond the source).

**Where other sources in this batch agree or push back**

- **A separate judge: agreed.** In [[AI LABS - Types of Claude Loops Explained]], the verification loop uses a reviewer whose only output is a score and which has no editing tools ([10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s), [10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s)). That's the same worker/judge split as the grader here [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s).
- **Why separation matters.** [[AI LABS - The Unlazy Skill for Lazy Agents]] faults three weak finish lines:
  - a Ralph finish line that's just text the agent writes ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s))
  - a `/goal` checker that judges the conversation rather than the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s))
  - loops where the agent grades its own checks ([04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s)).

  The Managed Agents grader runs in a separate context and grades the artifact itself (per docs). This video offers no evidence about whether it can be gamed.
- **Hosted always-on agents: a prediction partly met.** [[Jay E]], in [[Jay E - The ARMS Framework for a Claude Agentic OS]]:
  - runs many of his routines as cloud scheduled tasks so they fire with his computer off ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s))
  - expects Anthropic and OpenAI to offer an all-in-one version without file syncing in the near future rather than now, citing storage and security concerns ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s), [18:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1106s)).

  *Vault reading:* Managed Agents offers hosted sessions with server-side memory, but as a developer API. It doesn't sync your Claude Code workspace, so his Syncthing route still covers that case. See [[Sync a Workspace to an Always-On Cloud Agent]].

## Build from this

For each system, the video's part is timestamped, and the vault's additions come from the docs under Beyond the source.

1. **Ticket-triggered coding agent with a graded outcome.**
   - *Video:* card move starts a session [00:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=36s); environment with pre-installed tools [00:47](https://www.youtube.com/watch?v=NLWiIj47IdI&t=47s); repo mounted [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s); rubric [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s); live events [01:11](https://www.youtube.com/watch?v=NLWiIj47IdI&t=71s); grader loop [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s); parallel tickets [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s).
   - *Vault addition:*
     - Put lighthouse and puppeteer under the environment's `packages.npm`. If networking is `limited`, also set `allow_package_managers: true`.
     - Mount the repo as a `github_repository` resource.
     - Start the work with a `user.define_outcome` event.
     - Render `agent.tool_use` and `span.outcome_evaluation_end` events on the card.
     - Fetch deliverables from `/mnt/session/outputs/` through the Files API.
     - GitHub Issues or Linear labels can replace the board.
   - See [[Build an Event-Triggered Managed Agent]], [[Build Verification into Every Task]], [[Parallel Sessions with Git Worktrees]].
2. **Weekly SaaS spend watcher that reports changes.**
   - *Video:* web search [01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s); Python analysis [01:59](https://www.youtube.com/watch?v=NLWiIj47IdI&t=119s); Excel skill [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s); Slack and Asana via MCP [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s); memory read then write [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s); deltas [02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s).
   - *Vault addition:*
     - Attach the `xlsx` skill and a memory store with instructions (starter C).
     - Run it as a scheduled deployment set to fire before stand-up, with a budget per run.
     - Limit `web_search` and `web_fetch` to vendor domains, which shrinks the injection risk to memory.
     - Only set Slack and Asana to `always_allow` if unreviewed posts are acceptable.
   - See [[Schedule Recurring Claude Tasks]], [[Configure Safe Autonomy Permissions]], [[Agent Memory Patterns]].
3. **Alert-triggered incident coordinator with human sign-off.**
   - *Video:* alert in as a custom tool result [02:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=158s); coordinator plus three specialists [02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s); shared filesystem [02:50](https://www.youtube.com/watch?v=NLWiIj47IdI&t=170s); one summary [02:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=176s); approval before Slack [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s); past-incident memory [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s).
   - *Vault addition:*
     - Give the coordinator a `multiagent.agents` roster. Logs, metrics and recent-deploys specialists are a suggestion; the video names no roles.
     - Declare the Slack MCP server only on the coordinator, keep it on `always_ask`, and route `requires_action` pauses to on-call.
     - Attach a `read_only` runbook store and a `read_write` incident-history store.
     - Validate alert payloads in your backend.
   - See [[Build an Event-Triggered Managed Agent]], [[Permissions and Approval Gates]], [[Subagents and Agent Teams]].
4. **Reusable gradeable rubric kit.**
   - *Video:* machine-checkable criteria [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s); grader feedback drives revision [01:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=81s).
   - *Vault addition:*
     - Write one checkable line per criterion under markdown headings.
     - With no rubric to hand, have Claude analyse a known-good example and turn that into criteria (docs advice).
     - Reuse the rubric with a read-only reviewer subagent in Claude Code.
   - See [[Build Verification into Every Task]], [[Multi-Agent Review and Scoring Loops]], [[Evidence-Gated Completion Ledger]].
5. **Read-before, write-after memory routine.**
   - *Video:* the pattern appears twice [02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s).
   - *Vault addition:* in Claude Code, make the memory file the first stop in CLAUDE.md's lookup order. Save changes and root causes as small dated files named for the question you'll ask later. The docs give the same "many small files" advice for stores.
   - See [[Tiered Lookup Routing]], [[Design for Retrieval]], [[Claude Code Auto Memory]].
6. **A subscription-plan version without the API.**
   - *Vault addition, not in the video:*
     - Claude Code routines (research preview) run on a schedule, from an HTTP call, or on GitHub events. The docs use alert triage as an example.
     - Routines have no approval prompts, so leave the Slack connector out and have the run open a draft PR for a person to act on.
   - See [[Routines and Scheduled Tasks]], [[Schedule Recurring Claude Tasks]], [[Sync a Workspace to an Always-On Cloud Agent]].
7. **Grader for this vault's notes.**
   - *Vault addition:* a rubric of CLAUDE.md conventions, checked by a separate-context reviewer after each ingest:
     - a timestamp on every video claim
     - additions kept under Beyond the source
     - no quote over about 15 words
     - Technique notes complete.
   - See [[Build Verification into Every Task]], [[Ingest Sources into an LLM Wiki]].

**Vault starter content (not shown in the video).** Field names follow the Managed Agents docs; the wording is placeholder.

A. Rubric for Demo 1. The first three sections mirror [00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s)–[01:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=62s); the report path, the first-viewport exception for images and the last section are additions.

```markdown
# Website performance rubric
## Lighthouse
- Home page performance score is 90 or more; JSON report saved to /mnt/session/outputs/lighthouse.json
## Render path
- The saved report lists zero render-blocking resources
## Images
- Every image outside the first viewport uses lazy loading
## No regressions
- The existing test command exits with status 0
```

B. Session request for Demo 1:

```yaml
agent: <agent_id>                 # agent toolset enabled
environment_id: <environment_id>  # config.packages.npm: [lighthouse, puppeteer]
resources:
  - type: github_repository
    url: https://github.com/<org>/<repo>
    mount_path: /workspace/site
    authorization_token: <from your secret store>
initial_events:
  - type: user.define_outcome
    description: "Ticket <id>: improve site performance; save reports to /mnt/session/outputs/"
    rubric: {type: text, content: "<rubric A>"}
    max_iterations: 5             # default 3, maximum 20
```

C. Memory store attachment for Demo 2:

```yaml
resources:
  - type: memory_store
    memory_store_id: <memstore_id>
    access: read_write
    instructions: >
      SaaS pricing history. Before researching, read latest.md in this store.
      When finished, replace latest.md with this run's prices and append one
      dated line per change to changes/<YYYY-MM>.md.
```

D. Slack approval gate for Demo 3's coordinator:

```yaml
mcp_servers:
  - {type: url, name: slack, url: <slack MCP endpoint>}
tools:
  - type: agent_toolset_20260401            # defaults to always_allow
  - type: mcp_toolset
    mcp_server_name: slack
    default_config:
      permission_policy: {type: always_ask} # the MCP default, stated so nobody loosens it by accident
```

## Resources mentioned

- **Early-access form** (from the video description): https://claude.com/form/claude-managed-agents. Today only dreaming and MCP tunnels need an access request (Beyond the source).
- **Lighthouse** [00:49](https://www.youtube.com/watch?v=NLWiIj47IdI&t=49s); link added at ingest: https://developer.chrome.com/docs/lighthouse/overview
- **Puppeteer** [00:49](https://www.youtube.com/watch?v=NLWiIj47IdI&t=49s); link added at ingest: https://pptr.dev/
- **GitHub** repo mount [00:52](https://www.youtube.com/watch?v=NLWiIj47IdI&t=52s); **Python** [02:01](https://www.youtube.com/watch?v=NLWiIj47IdI&t=121s).
- **Excel spreadsheet skill** [02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s). Presumably Anthropic's pre-built `xlsx` skill; the video doesn't name it.
- **Slack and Asana MCP servers** [02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s).
- **Monitoring stack**, unnamed [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s).

## Beyond the source

*Not said in the video. Added at ingest on 2026-09-15 and verified at the links given.*

- **Launch and pricing.**
  - Announced 2026-04-08 as composable APIs for cloud-hosted agents, with sandboxing, persistent sessions, scoped permissions and tracing.
  - Price: standard token rates plus $0.08 per session-hour of active runtime.
  - The launch post lists multi-agent coordination and self-evaluation (outcomes) as research previews behind an access request. The video description also puts memory in that group.
  - Source: https://claude.com/blog/claude-managed-agents
- **Status now.**
  - Still in beta, behind the `managed-agents-2026-04-01` header, and enabled by default for all API accounts.
  - Dreaming and MCP tunnels remain a narrower research preview.
  - Sessions keep history, sandbox state and outputs server-side, so the product isn't eligible for ZDR or HIPAA BAA coverage. You can delete sessions and files through the API.
  - Source: https://platform.claude.com/docs/en/managed-agents/overview
- **Memory, outcomes and orchestration went public.**
  - Memory reached public beta on 2026-04-23 (https://claude.com/blog/claude-managed-agents-memory).
  - Outcomes, multi-agent orchestration and webhooks reached public beta in May 2026, alongside dreaming, a scheduled process that curates memories (research preview). SD Times dates the announcement 2026-05-06.
  - Anthropic claims outcomes add up to 10 percentage points of task success. That's a vendor figure.
  - Sources: https://claude.com/blog/new-in-claude-managed-agents, https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/
- **Four core concepts.**
  - Agent (model, system prompt, tools, MCP servers, skills); environment (cloud or self-hosted sandbox); session; events.
  - Results stream as server-sent events, and history is stored server-side. You can steer a session with more user events or interrupt it.
  - Source: https://platform.claude.com/docs/en/managed-agents/overview
- **Environments.**
  - `config.packages` pre-installs apt, cargo, gem, go, npm or pip packages, cached per environment.
  - `networking` is `unrestricted` by default, or `limited` with `allowed_hosts`. The docs recommend `limited` for production.
  - With `limited` networking, an environment that lists `packages` must also set `allow_package_managers: true`, or the create request fails with a 400.
  - Network rules don't cover `web_search` and `web_fetch`; use `allowed_domains` on those tools.
  - Each session gets its own fresh container, with no shared filesystem state (matching "two containers" [01:36](https://www.youtube.com/watch?v=NLWiIj47IdI&t=96s)).
  - Source: https://platform.claude.com/docs/en/managed-agents/environments
- **Repos and skills.**
  - A `github_repository` resource takes `url`, optional `mount_path` (default `/workspace/<repo-name>`) and `authorization_token`.
  - Skills in the repo's `.claude/skills/<name>/SKILL.md` load at session start, which makes the repo part of your trust boundary.
  - Pre-built skills are `pptx`, `xlsx`, `docx` and `pdf`, attached via the agent's `skills` array. Limit: 500 skills per session.
  - Source: https://platform.claude.com/docs/en/managed-agents/skills
- **Outcomes.**
  - A markdown rubric is required, inline or uploaded through the Files API. Send it with `user.define_outcome` (`description`, `rubric`, `max_iterations`: default 3, max 20).
  - The grader uses a separate context window.
  - Results: `satisfied`, `needs_revision`, `max_iterations_reached`, `failed` or `interrupted`.
  - One outcome runs at a time; chain further ones after it ends.
  - Outputs go to `/mnt/session/outputs/`.
  - Vague criteria make grading noisy, so write explicit ones, or derive them from a known-good example.
  - Source: https://platform.claude.com/docs/en/managed-agents/define-outcomes
- **Memory stores.**
  - Workspace-scoped text documents, mounted under `/mnt/memory/<slug>/` and attached in `resources[]` at session creation only.
  - `access` is `read_write` by default, or `read_only`. Optional `instructions` can be up to 4,096 characters.
  - Limits: 8 stores per session, 100 kB per memory, 10,000 memories per store.
  - Every change creates an immutable version, kept 30 days (recent versions of live memories are retained), and versions can be redacted.
  - The docs warn that prompt injection can poison `read_write` stores.
  - Store endpoints use the `agent-memory-2026-07-22` header.
  - Source: https://platform.claude.com/docs/en/managed-agents/memory
- **Multi-agent orchestration.**
  - Agents share the sandbox, filesystem and vault credentials. Each runs in its own persistent thread with its own model, prompt, tools, MCP servers and skills.
  - The roster lives in `multiagent.agents`.
  - Limits: one delegation level, up to 20 unique agents (copies allowed), 25 concurrent threads.
  - The primary stream shows a condensed view, including permission requests.
  - Source: https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration
- **Permission policies.**
  - Three policies: `always_allow`, `always_ask`, `auto`. The agent toolset defaults to `always_allow` and MCP toolsets to `always_ask`; per-tool overrides go in `configs`.
  - A pause emits `session.status_idle` with `stop_reason.type: requires_action`. Answer with `user.tool_confirmation` (`tool_use_id`, `result`, optional `deny_message`).
  - `auto` is not a human checkpoint.
  - Custom tools aren't governed by policies (`agent.custom_tool_use` → your app → `user.custom_tool_result`).
  - Source: https://platform.claude.com/docs/en/managed-agents/permission-policies
- **Scheduled deployments** (public beta since 2026-06-09, alongside credential vaults: https://claude.com/blog/whats-new-in-claude-managed-agents).
  - A deployment needs an agent, an environment, at least one initial `user.message` or `user.define_outcome`, and a cron `schedule` with an IANA `timezone`.
  - Optional: files, GitHub, memory stores, vaults, and a budget per run.
  - Runs start with jitter of up to 15% of the interval (capped at 9 minutes). Limit: 1,000 per organisation. A manual `run` endpoint is available.
  - Source: https://platform.claude.com/docs/en/managed-agents/scheduled-deployments
- **Claude Code routines** (research preview).
  - Triggers: schedule, API (`/fire` with a `text` payload marked as untrusted) and GitHub events. The docs include an alert-triage example.
  - Runs have no approval prompts, and included connectors can write without asking.
  - Source: https://code.claude.com/docs/en/routines

## Transcript notes

| Time | Captions | Reading used | Confidence |
|---|---|---|---|
| [00:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=32s) | "I have a year a Kanban board" | "I have here a Kanban board" | Likely |
| [01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s) | "running at its own context window" | running *in* its own context window (the docs' separate grader context) | Certain |
| [01:51](https://www.youtube.com/watch?v=NLWiIj47IdI&t=111s) | "Common." after the stand-up line | *(unclear in captions)*. Possibly "come Monday", given the later Monday reference | Uncertain |
| [02:35](https://www.youtube.com/watch?v=NLWiIj47IdI&t=155s) | "A custom tool my back end receives…" | "Via a custom tool, my backend receives…" | Likely |
| [03:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=183s) | "permissions policy" | "permission policy", the docs' term | Certain |
| [03:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=212s) | "Managed agents gives developers…" | Claude Managed Agents, the product name | Certain |

## Related

- **Tools:** [[Claude Managed Agents]] · [[Claude Code]]
- **Concepts:** [[Verification Before Done]] · [[Subagents and Agent Teams]] · [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[Routines and Scheduled Tasks]] · [[Agent Memory Patterns]] · [[Claude Code Auto Memory]] · [[Context vs Connections]] · [[Always-On Brain OS]] · [[Design for Retrieval]] · [[Agent Skills]] · [[Tool-Agnostic Context Files]]
- **Techniques:** [[Build an Event-Triggered Managed Agent]] · [[Build Verification into Every Task]] · [[Configure Safe Autonomy Permissions]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Parallel Sessions with Git Worktrees]] · [[Tiered Lookup Routing]] · [[Multi-Agent Review and Scoring Loops]] · [[Evidence-Gated Completion Ledger]] · [[Ingest Sources into an LLM Wiki]]
- **Sources:** [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[Jay E - The ARMS Framework for a Claude Agentic OS]] · [[Nate Herk - Every Level of a Claude Second Brain]] · [[Knowing More - Every Claude Model Explained]]
- **People:** [[Jay E]] · [[Nate Herk]]
- [[Home]]
