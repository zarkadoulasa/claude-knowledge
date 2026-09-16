---
type: tool
category: Open-source personal AI assistant (agent harness)
website: https://openclaw.ai
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]"]
tags: [topic/agents, topic/skills, topic/memory, topic/automation, topic/scheduling]
---

# OpenClaw

## What it is

In this vault's sources, OpenClaw is the personal-assistant agent [[Ras Mic]] runs every day. His advice on skills comes from using it. [[Simon Pittman]] and [[Jay E]] mention it only as the familiar example of an always-on assistant. No video shows it being installed or configured. The official description is under *Beyond the source*.

| Source | How OpenClaw figures | Where |
|---|---|---|
| [[Ras Mic - How AI Agents and Claude Skills Work]] | His main harness: its own inbox, skills built from real runs, a main agent plus five subagents | [07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s), [26:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1584s) |
| [[Simon Pittman - Set Up Claude Cowork]] | A yardstick: Dispatch gives you an OpenClaw-style assistant on your desktop | [45:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2727s) |
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | Named as the tool that probably popularised cloud scheduled agents | [16:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=980s) |

## How sources use it

### [[Ras Mic - How AI Agents and Claude Skills Work]]

- **It gets its own inbox, not yours.** His OpenClaw agent has a separate email address instead of access to his inbox ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)). He cites attack vectors and a past hack ([07:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=463s)). He forwards sponsor emails to it ([07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s)).
- **A vague brief failed.** At first he only told it to check every 15 minutes and research each sponsor ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)). It approved every single one ([08:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=487s)). That told him it needed a step-by-step guide ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s)).
- **Walk it through first, then turn the run into a skill.** He guided the agent through the workflow step by step ([09:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=563s)). Only after repeated successful runs did he convert it into a skill ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)). A skill written without that context, especially on OpenClaw, will probably fail at the API call or pull the wrong data ([11:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=688s)). See [[Build a Skill from a Successful Run]].
- **Memory doesn't replace context.** OpenClaw has a memory layer, but he says the agent still only gets things right when you give it proper context ([13:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=796s), [13:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=802s)). See [[Agent Memory Patterns]].
- **Don't start with 15 subagents.** He sees people set up OpenClaw with 15 subagents and 30 skills ([14:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=867s)) before building any workflows of their own ([14:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=873s)). He does use subagents a lot, once there's a reason to ([14:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=877s)).
- **Grow from one agent.** He started with a single main agent that did everything ([25:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1551s)). He added subagents only once workflows were defined ([26:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1561s)). He now has five, among them marketing, business and personal ([26:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1584s), [26:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1589s)). He bets his setup would beat anyone's OpenClaw head to head, because he scaled for productivity rather than looks ([26:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1594s)). See [[Subagents and Agent Teams]].
- **Expect about two rough weeks.** When he first set up OpenClaw he thought it was garbage ([24:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1446s)). He suggests budgeting roughly two weeks of investment ([24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s)).
- **Build your own before adopting a big framework.** He tried Paperclip and loved it ([14:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=888s)); what Paperclip is appears under *Beyond the source*. He still argues people would do better spending 2–3 weeks prompting their agent to build only the parts they need ([27:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1672s), [27:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1678s)).
- **Under the hood it writes code.** He groups [[Claude Cowork]] and OpenClaw as tools that work by writing code that calls APIs ([19:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1163s)).
- **He reads other people's skills but doesn't install them.** He mines marketplace skills for ideas but won't download them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)), calling them an easy way to attack someone ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)). See [[Build vs Install Third-Party Skills]].

### [[Simon Pittman - Set Up Claude Cowork]]

- **A comparison only.** From his phone, he uses Dispatch to ask his desktop for today's calendar. He then says you now have an OpenClaw-style assistant on your desktop that you can direct while you're out ([45:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2727s)). He adds it could also browse, research or continue projects with your plugins and skills ([45:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=2739s)).

### [[Jay E - The ARMS Framework for a Claude Agentic OS]]

- **The tool that made cloud routines popular.** Local routines stop when your computer is off, so many of his run in the cloud ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s), [16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)). He credits OpenClaw with probably popularising that ([16:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=980s)). He mentions Grok Bot as a newer but pricey option and says he uses [[Hermes Agent]] himself ([16:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=988s)). See [[Routines and Scheduled Tasks]] and [[Sync a Workspace to an Always-On Cloud Agent]].

## Notes

- **No setup in any video.** None of the three shows install commands, config files, skill folders or how memory is set up. Everything above is stated usage and opinion.
- **Anecdotal claims.** Ras Mic's head-to-head productivity bet and his reliability claims come without any evaluation.
- **Caption fixes.** Ras Mic: "open cloud agent", "Open Cloud" and "Open Claw" → OpenClaw. At [27:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1674s) the captions say "open Claude"; given the Paperclip context it's most likely OpenClaw *(unclear in captions)*. Simon: "open Claude style assistant" → OpenClaw-style (likely). "Paper claw" → Paperclip.

## Beyond the source

*Not from the videos. Checked 2026-09-15 at the linked pages.*

- **What it is.** OpenClaw is an MIT-licensed, open-source AI assistant that runs on your own computer. You reach it through 20+ messaging platforms (e.g. WhatsApp, Telegram, Slack, Discord, Signal, iMessage) and native apps. It can serve one person or a shared team. Install it with the scripts on openclaw.ai or via npm, then run `openclaw onboard --install-daemon`. <https://github.com/openclaw/openclaw>
- **Skills.** Skills are `SKILL.md` files with `name` and `description` frontmatter, the same basic shape as [[Agent Skills]]. OpenClaw loads them from several places, and the highest-priority copy of a skill wins. Workspace `skills/` comes first, then the workspace's `.agents/skills`, then `~/.agents/skills`, then managed, bundled and other lower-priority locations. ClawHub is the public registry (`openclaw skills install @owner/<slug>`). The docs tell you to treat third-party skills as untrusted code and read them before enabling. <https://docs.openclaw.ai/tools/skills>
- **The memory layer Ras Mic mentions.** Memory is plain Markdown in the agent workspace (default `~/.openclaw/workspace`). `MEMORY.md` holds durable facts and decisions and loads at session start. Daily notes live in `memory/YYYY-MM-DD.md`; today's and yesterday's load automatically when you start fresh with `/new` or `/reset`. There's also an optional `USER.md`. Two agent tools read it: `memory_search` (hybrid semantic and keyword search) and `memory_get`. The docs stress there's no hidden state: only what's written to disk is remembered. That fits his point that memory can't stand in for the context you teach it. <https://docs.openclaw.ai/concepts/memory>
- **His marketplace worry has precedent.** On 2026-02-02, The Hacker News reported that Koi Security audited 2,857 ClawHub skills and found 341 malicious ones. The report ties them to a campaign called ClawHavoc. In 335 of them, a fake "prerequisites" step installed Atomic Stealer (AMOS), a macOS stealer, and Windows users were pointed to a separate malicious download. <https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html>
- **Paperclip, which Ras Mic mentions.** An MIT-licensed, open-source project for orchestrating teams of AI agents. Its README casts OpenClaw as the employee and Paperclip as the company, and it can coordinate OpenClaw, Claude Code, Codex and other agents. <https://github.com/paperclipai/paperclip>

## Related

- **Concepts:** [[Agent Skills]], [[Build vs Install Third-Party Skills]], [[Subagents and Agent Teams]], [[Agent Memory Patterns]], [[Routines and Scheduled Tasks]], [[Agentic OS]]
- **Techniques:** [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]], [[Sync a Workspace to an Always-On Cloud Agent]]
- **Tools:** [[Hermes Agent]], [[Claude Cowork]], [[Claude Code]]
- **People:** [[Ras Mic]], [[Greg Isenberg]], [[Simon Pittman]], [[Jay E]]
- **Sources:** [[Ras Mic - How AI Agents and Claude Skills Work]], [[Simon Pittman - Set Up Claude Cowork]], [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- [[Home]]
