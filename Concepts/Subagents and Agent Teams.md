---
type: concept
aliases: ["Subagents", "Sub-agents", "Agent Teams", "Multi-Agent Coordination", "Coordinator and Specialists"]
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]"]
tags: [topic/subagents, topic/agents, topic/claude-code, topic/context, topic/models, topic/loops, topic/managed-agents]
---

# Subagents and Agent Teams

## In one sentence

A main agent hands pieces of a job to helper agents that each work in their own clean context and return a short result, and the design choices are who coordinates, whether helpers talk to each other, which model each runs, and how they avoid editing the same files.

## How it works

### Four dials (vault framing)

Every design in the sources makes four choices: what each helper sees, who coordinates, which model each helper runs, and how parallel helpers stay out of each other's files. This framing is the vault's.

Short names below refer to these sources:

- **Nate:** [[Nate Herk - 32 Tricks to Level Up Claude Code]]
- **Coding Sloth:** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]
- **Loops video:** [[AI LABS - Types of Claude Loops Explained]]
- **Unlazy video:** [[AI LABS - The Unlazy Skill for Lazy Agents]]
- **Anthropic's demo:** [[Anthropic - What Is Claude Managed Agents]]
- **Ras Mic:** [[Ras Mic - How AI Agents and Claude Skills Work]]

For separate sessions, keeping files apart means one worktree each: [[Parallel Sessions with Git Worktrees]].

### Subagents: one job, own context, summary back

- **The shape.** The main chat is the lead. A subagent is a mini Claude it starts for one job, such as researcher, reviewer or debugger. The subagent does its work in its own window and hands back a summary ([19:38](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1178s)–[19:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1196s), Coding Sloth).
- **What it buys.** Subagents run in parallel, each can use its own model, and the main thread stays clean while they research, write tests or try alternatives ([05:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=301s)–[05:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=315s), Nate).
- **Why clean context matters.** The Unlazy video argues that attention thins as the resent history grows. A fresh window focuses better ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)–[02:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=148s)). A helper with one clear goal isn't carrying the rest of the job ([06:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=378s)–[06:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=383s)). See [[Context Window Management]] and [[Agent Laziness]].

### Agent teams: peers with a shared task list

Nate describes agent teams as subagents that can also talk to each other. Teammates share a task list, message one another and can assign each other work ([14:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=883s)–[14:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=892s)). You can address any teammate directly instead of going through the main agent ([14:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=892s)–[14:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=899s)). The current docs add an experimental flag, and they say named subagents can also message each other. See Beyond the source.

### Hub, coordinator, tree or mesh

| Pattern | How it runs | Source |
|---|---|---|
| **Orchestrator + critics** | A custom orchestrate command runs four critics (factual, domain, safety, style). It applies their fixes and reruns them each round | [[AI LABS - Types of Claude Loops Explained]] [08:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=481s)–[09:04](https://www.youtube.com/watch?v=8wsM0euQOvc&t=544s) |
| **Coordinator + specialists** | Delegates to three specialists, each with its own context on one shared filesystem, then merges their findings into one summary | [[Anthropic - What Is Claude Managed Agents]] [02:42](https://www.youtube.com/watch?v=NLWiIj47IdI&t=162s)–[02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s) |
| **Tree of leaf tasks** | Splits the task into a tree. In orchestrated mode (depth 4+) each leaf gets a fresh subagent, and the parent re-runs the leaf's checks before moving on | [[AI LABS - The Unlazy Skill for Lazy Agents]] [05:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=349s), [06:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=416s), [08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)–[08:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=526s) |
| **Agent team (mesh)** | Peers share a task list and message each other directly | [[Nate Herk - 32 Tricks to Level Up Claude Code]] [14:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=883s) |
| **Fan-out workflow** | A dynamic workflow spreads one review across many subagents at once | [[AI LABS - Types of Claude Loops Explained]] [10:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=601s)–[10:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=613s) |

The vault's reading of these sources: a hub suits work where one agent must remember earlier rounds, and a mesh suits work where the peers need to argue with each other. [[Multi-Agent Review and Scoring Loops]] builds the orchestrator pattern.

## When to use it — and when not to

**Use it when:**

- **A side task would flood the main window.** An example is a scraping job that reads hundreds of thousands of tokens and only needs to return highlights ([06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=378s), Nate).
- **The work splits into independent parts that can run at once.** Run them in parallel and declare which files each part owns ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s)–[12:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=726s), Unlazy video).
- **A review needs several perspectives.** One reviewer misses what separate critics catch ([07:21](https://www.youtube.com/watch?v=8wsM0euQOvc&t=441s)–[07:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=464s), loops video).
- **A domain has a defined workflow of its own.** It then earns its own skills and context ([26:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1561s)–[26:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1582s), Ras Mic).

**Hold off when:**

- **You have no workflows yet.** Ras Mic's anti-pattern is starting [[OpenClaw]] with 15 subagents and 30 skills before any workflow exists ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)–[14:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=874s)).
- **Your plan is small.** Each subagent is a full conversation, and on the $20 plan a small multi-agent setup can use up the limit before the task finishes ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s), Coding Sloth).
- **The tasks are tiny.** Unlazy's rule is that each leaf must be worth at least ten minutes of real work ([06:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=386s)). If the depth you ask for would produce smaller tasks, the video says the skill drops back to its default depth of three ([06:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=395s)); the repo at the time said to back off one layer (see [[Unlazy]]).
- **The app isn't built yet.** A fan-out review is slow and token-hungry, so AI LABS keeps it for large finished apps. A single normal reviewer is much cheaper ([10:55](https://www.youtube.com/watch?v=8wsM0euQOvc&t=655s)–[11:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=677s)).

## Perspectives from sources

- **[[Nate Herk - 32 Tricks to Level Up Claude Code]]** treats subagents as an intermediate trick:
  - Ask for subagents on complex problems ([04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s)). He likens them to a team of developers instead of one ([05:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=316s)).
  - Pair them with model choice: Haiku subagents for simpler work and an Opus main thread ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)–[05:26](https://www.youtube.com/watch?v=jqoFP9QapXI&t=326s)). An expensive model shouldn't read that much to extract a few facts, and done well this cuts cost without losing quality where it counts ([06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=388s)).
  - Agent teams come among his last and most advanced tricks. They cost more and run longer, but give a more cohesive result on big projects ([14:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=899s)–[15:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=905s)). See [[Choosing a Claude Model]] and [[Route Tasks to the Right Claude Model]].
- **[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]** stresses cost:
  - The easiest way to make a subagent is to ask Claude to create one with a description of its job ([19:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1196s)–[20:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1202s)).
  - He rates subagents A tier, and S tier on big plans, because implementations get much better ([20:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1223s)–[20:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1229s)). What holds the rating down is the drain on usage limits, which stops most people running them all the time ([20:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1204s)–[20:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1210s)).
- **[[AI LABS - Types of Claude Loops Explained]]** considered agent teams, where agents talk directly, which they liken to [[Andrej Karpathy]]'s LLM Council, and chose an orchestrator instead ([09:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=549s)–[09:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=557s)). Their picture of the council as agents arguing ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)) doesn't match the repo; see Beyond the source in [[Loop Engineering]]. The reason: one agent has to hold the context of earlier rounds to coordinate well ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)–[09:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=565s)). See [[Loop Engineering]].
- **[[AI LABS - The Unlazy Skill for Lazy Agents]]**, with [[Unlazy]]:
  - **Parent checks, doesn't trust.** In orchestrated mode, each leaf goes to a fresh subagent. When it reports done, the parent re-runs that leaf's checks before logging it and handing out the next task ([08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)–[08:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=526s)).
  - **Serial dispatch was the bottleneck.** A 3–4 hour run produced only a login page ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s)–[10:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=642s)). Claude Code and Codex can run subagents side by side, but the skill waited for each one to finish ([10:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=648s)–[10:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=658s)).
  - **The fix.** After their edit, the plan recorded each task's files, the foundation went first, and then all agents launched together. Ten ran at once and finished a working first version in about two hours ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s)–[12:10](https://www.youtube.com/watch?v=c47uqR7XB_c&t=730s)).
  - **Routing.** At that scale they add a model-router skill, so mechanical tasks go to a cheaper model ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s)). See [[Evidence-Gated Completion Ledger]].
- **[[Anthropic - What Is Claude Managed Agents]]** shows the hosted version on [[Claude Managed Agents]]:
  - **Separate grader.** A grader with its own context window checks output against a rubric ([01:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=77s)).
  - **Parallel sessions.** Separate tickets run as parallel sessions in separate containers ([01:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=93s)–[01:38](https://www.youtube.com/watch?v=NLWiIj47IdI&t=98s)).
  - **Human approval gate.** The coordinator's Slack post waits for a person to approve it under a permission policy ([03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)).
  - **Memory.** The coordinator checks a memory store for past incidents ([03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)–[03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s)).

  See [[Build an Event-Triggered Managed Agent]], [[Permissions and Approval Gates]] and [[Agent Memory Patterns]].
- **[[Ras Mic - How AI Agents and Claude Skills Work]]** says to scale for productivity, not looks ([14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s)):
  - **Order.** Start with one agent and build its skills, then add a subagent so the main agent manages others ([15:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=928s)–[15:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=938s)). His analogy is founding a company with ten staff when you have never managed anyone ([15:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=940s)–[15:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=947s)).
  - **His path.** One agent did everything. Once his sponsor workflows were defined, a marketing subagent took that work with its own skills and context. He now runs five subagents, including marketing, business and personal ([25:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1548s)–[26:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1592s)).
  - **Ready-made systems.** He liked Paperclip, a ready-made multi-agent setup, but thinks most people would get more done building their own ([14:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=888s)–[14:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=899s)). See [[Agentic OS]] and [[Second Brain Levels]].
- **[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]** gives the clearest plain-language version of the subagent/team split, and a working example:
  - **Subagents work for the main session and can't talk to each other.** The session you talk to is the lead; its five research lenses report back to it but not to one another ([08:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=514s)–[08:55](https://www.youtube.com/watch?v=Tj3018n5MVg&t=535s)). You can click a subagent and see the exact prompt the main session sent it ([08:15](https://www.youtube.com/watch?v=Tj3018n5MVg&t=495s)).
  - **Agent teams can talk to each other and debate.** He spins up teams/councils that message the main session *and* each other, and has them argue until they reach consensus ([08:57](https://www.youtube.com/watch?v=Tj3018n5MVg&t=537s)–[09:19](https://www.youtube.com/watch?v=Tj3018n5MVg&t=559s)). This restates his 32-Tricks framing; the docs now allow named subagents to message too (Beyond the source).
  - **Cost.** Agent teams are "much more expensive" than subagents ([09:19](https://www.youtube.com/watch?v=Tj3018n5MVg&t=559s)). His five lenses ran on Opus 4.8 but could run on Haiku or Sonnet ([09:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=574s)). See [[Route Tasks to the Right Claude Model]].
  - **When to fan out fixed vs many.** Against Claude Code's Deep Research (100+ agents, rate-limited), his fixed five-persona subagent pipeline was faster and cheaper ([04:04](https://www.youtube.com/watch?v=Tj3018n5MVg&t=244s)–[04:30](https://www.youtube.com/watch?v=Tj3018n5MVg&t=270s)). See [[Claude Deep Research]] and [[Multi-Perspective Research]].

## Where sources disagree

- **Can subagents talk to each other?**
  - Nate says no; that's his whole contrast with agent teams ([14:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=878s)–[14:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=883s)).
  - The current Claude Code docs say subagents that Claude names can message each other (Beyond the source). Treat his line as dated. The difference that still holds is the one below.
  - **Remaining difference.** Subagents report to their caller. Teammates share a task list and coordinate with each other.
- **Hub vs mesh.**
  - Nate sells the mesh for cohesion on big projects ([15:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=900s)).
  - AI LABS deliberately picks the hub for multi-round review ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)). Anthropic's demo also uses a hub, the coordinator ([02:46](https://www.youtube.com/watch?v=NLWiIj47IdI&t=166s)).
  - These aren't really in conflict. Pick by whether one agent has to carry state from round to round.
- **Cheap or expensive?**
  - Nate presents subagents as a way to cut cost, if they run on Haiku ([06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s)).
  - The Coding Sloth presents them as a drain on limits ([20:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1208s)).
  - Both can be true. Nate's saving comes from moving bulk reading to a cheaper model. The Sloth's cost comes from running several full conversations at once.
- **Serial or parallel?**
  - Unlazy as shipped handed out one leaf at a time. AI LABS found that far too slow and switched to parallel dispatch with file ownership ([10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s), [11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s)).
  - Upstream has since adopted parallel dispatch too (Beyond the source).
- **How early to adopt.**
  - Nate lists subagents as an intermediate trick ([04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s)), and the Coding Sloth rates them S tier on big plans ([20:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1226s)).
  - Ras Mic says a subagent should come only after a workflow exists ([26:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1561s)–[26:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1575s)).
  - They mean different things: Nate and the Sloth talk about delegating within one task, Ras Mic about permanent domain agents.

## Beyond the source

*Not from the videos. Checked on 2026-09-15 at the linked pages.*

- **Claude Code subagents.**
  - **Files.** Each subagent is a Markdown file in `.claude/agents/` or `~/.claude/agents/`.
  - **Fields.** `name` and `description` are required. Optional fields include `tools`, `model` (e.g. `haiku` or `inherit`), `isolation: worktree`, `background` and `memory`.
  - **Built-ins.** Explore, Plan and general-purpose.
  - **Creating one.** Since v2.1.198, `/agents` no longer opens a wizard. Ask Claude to write the file, or edit it yourself.
  - **Limits.** By default, nesting goes three layers below the main conversation (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; the default has changed across versions) and 20 can run at once (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`). Many detailed results can still fill the main context.
  - **Messaging exists now.** A subagent whose tools include `SendMessage` gets a roster of `main` and every other named agent, and can message any of them. It needs at least one other agent to have a name. The agent-teams comparison table says subagents that Claude named at spawn can message each other. This dates Nate's claim.

  <https://code.claude.com/docs/en/sub-agents>
- **Agent teams.**
  - **Enabling.** Experimental and off by default. Turn them on with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.
  - **Structure.** A lead, teammates, a shared task list and a mailbox. You can message any teammate directly, and teammates don't inherit the lead's history.
  - **Limits.** The docs suggest 3–5 teammates. There is one team per session and no nesting.
  - **Files.** Teammates aren't isolated in worktrees, so split files by owner.
  - **Side effect.** While teams are enabled, a subagent that Claude names launches as a teammate. This happens only in interactive sessions; with `-p` (and the Agent SDK) it runs as an ordinary subagent. Setting the variable to `0` turns the behaviour off.

  <https://code.claude.com/docs/en/agent-teams>
- **Cost.**
  - Team tokens grow roughly with team size, and a team in plan mode uses about 7× a standard session.
  - The docs suggest Sonnet teammates, shutting them down when done, and `model: haiku` for simple subagent work.

  <https://code.claude.com/docs/en/costs>
- **Other parallel options in Claude Code.**
  - Agent view (`claude agents`, research preview).
  - Dynamic workflows.
  - `/batch`, which splits a change into 5–30 worktree-isolated subagents that each open a PR.
  - Cross-session messaging.

  <https://code.claude.com/docs/en/agents>
- **Managed Agents multiagent orchestration.**
  - **Shared vs own.** Agents share the sandbox, filesystem and vault credentials. Each runs in its own persistent thread with its own model, prompt, tools, MCP servers and skills.
  - **Roster.** The coordinator lists up to 20 agents in `multiagent.agents`, including `self` copies.
  - **Limits.** Delegation goes one level deep, and a session allows 25 concurrent threads.
  - **Access.** Requests need the `managed-agents-2026-04-01` beta header.

  <https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration>
- **Unlazy upstream.** Unlazy now launches ready leaves in parallel waves, after each declares non-overlapping `OWNS:` paths. The repo calls this a coordination guard, not write isolation, and suggests worktrees when outputs collide. <https://github.com/Leonxlnx/unlazy>

## Related

- **Concepts:** [[Context Window Management]] · [[Agent Laziness]] · [[Loop Engineering]] · [[Verification Before Done]] · [[Choosing a Claude Model]] · [[Agent Skills]] · [[Agentic OS]] · [[Permissions and Approval Gates]] · [[Agent Memory Patterns]] · [[Second Brain Levels]] · [[Multi-Perspective Research]]
- **Techniques:** [[Parallel Sessions with Git Worktrees]] · [[Route Tasks to the Right Claude Model]] · [[Multi-Agent Review and Scoring Loops]] · [[Evidence-Gated Completion Ledger]] · [[Context Hygiene Routine]] · [[Build an Event-Triggered Managed Agent]] · [[Build a STORM Multi-Perspective Research Skill]]
- **Tools:** [[Claude Code]] · [[Claude Managed Agents]] · [[Unlazy]] · [[OpenClaw]] · [[Claude Deep Research]]
- **People:** [[Nate Herk]] · [[The Coding Sloth]] · [[AI LABS]] · [[Ras Mic]] · [[Andrej Karpathy]]
