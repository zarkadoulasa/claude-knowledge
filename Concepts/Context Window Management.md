---
type: concept
aliases: ["Context Rot", "Dumb Zone", "Token Budget"]
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Knowing More - Every Claude Model Explained]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tags: [topic/context, topic/claude-code, topic/skills, topic/subagents, topic/models, topic/agentic-os]
---

# Context Window Management

## In one sentence

Everything an agent works from shares one finite token budget: system prompt, instruction files, skill metadata, tool definitions, files and the conversation ([06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s)–[06:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=402s)). Output quality slips as that budget fills ([13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s), [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)), and on subscription plans the same tokens drain your usage limit ([12:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=771s)). So the job is to keep each session lean, and to compact or restart *before* the degraded zone rather than after it.

## How it works

### What fills the window

[[Ras Mic - How AI Agents and Claude Skills Work]] builds the window up layer by layer on a whiteboard. His definition of context is the information the model gathers before it takes an action ([01:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=88s)).

| Layer | What it is | Cost note (his framing) | Timestamps |
|---|---|---|---|
| System prompt | The provider's general instructions on how to behave | Always there. He read Claude Code's after its source leaked | [01:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=100s) |
| AGENTS.md / CLAUDE.md | Your always-loaded instruction file | Present on every exchange. His hypothetical: a 1,000-line file of ~7,000 tokens is paid on every run | [03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s), [04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)–[04:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=266s) |
| Skill metadata | Only each skill's name and description | The body loads only when a request matches it (progressive disclosure) | [03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)–[03:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=219s), [05:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=319s)–[05:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=323s) |
| Tool definitions | Built-in tools such as read and write | Must sit in context, because the harness (not the model) runs tool calls | [06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s)–[06:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=385s) |
| Codebase / files | Whatever the agent reads | Grows as it explores | [06:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=388s) |
| Conversation | Your back-and-forth | Grows every turn | [06:38](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=398s)–[06:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=402s) |

- **Growth.** A session might open at around 20,000 tokens and grow until it reaches the limit. At that point Claude Code and Codex compact ([06:47](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=407s)–[07:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=421s)). He puts the limit at about 250,000 tokens. Current figures are under *Beyond the source*.
- **Measured idle cost of a skill.** His 116-line code-structure skill counts 944 tokens in full, but only 53 for its name and description, which is all it costs until it's used ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)–[30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s)). See [[Agent Skills]].
- **The view from inside Claude Code.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] shows that `/context` splits usage into percentages by system prompt, file contents, MCP servers and so on ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)–[02:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=121s)).
  - He calls CLAUDE.md "basically the system prompt": it loads into every conversation, so everything in it eats context ([06:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=413s)–[07:01](https://www.youtube.com/watch?v=jqoFP9QapXI&t=421s)).
  - He also says MCP servers load their entire tool definitions ([11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s)–[11:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=696s)). That point is now dated; see *Beyond the source*.
- **Why the conversation layer dominates.** [[AI LABS - The Unlazy Skill for Lazy Agents]] explains that the model keeps no memory between messages. The agent therefore resends every earlier message along with each new prompt, and that pile keeps growing ([02:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=123s)–[02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)).

### Quality degrades as it fills

The four practitioner sources agree that more context means worse work. They disagree on where the line is.

| Source | What goes wrong | Where to act | What to do | Timestamps |
|---|---|---|---|---|
| [[Nate Herk]] | "Context rot" | About **60%** | Watch context % in a status line. Run `/compact` and say what to keep. `/clear` before an unrelated task | [01:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=71s)–[01:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=74s), [02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)–[02:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=150s), [02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s)–[02:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=161s) |
| [[Ras Mic]] | The model gets "dumb" as the window closes. About 10% is used before you type anything | Stay between fresh and about **70%**. Expect trouble from 80% up | Keep always-loaded context minimal; put procedures in skills | [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s), [31:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1879s)–[31:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1893s) |
| [[The Coding Sloth]] | A "dumb zone": Claude forgets things, contradicts itself and makes silly mistakes | In his experience, past roughly **100K–200K tokens**. Also: *any* auto-compaction mid-task | One session per task. After an auto-compact, start a new session rather than carrying on. Compact manually only if the task truly must stay in one conversation | [13:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=793s)–[13:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=800s), [13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)–[13:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=824s), [14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=844s), [15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s) |
| [[AI LABS]] | Laziness is barely visible in a fresh window and shows up as it fills. Completion loops that hold early start to falter deep into real work | No number. "Fresh" vs "deep in the work" | Give each unit of work its own narrow, fresh context. Write requirements to files | [01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s)–[02:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=121s), [04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)–[04:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=263s), [06:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=372s)–[06:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=383s) |

- **A bigger window doesn't move the line.** The Coding Sloth's view is that a larger limit only extends the dumb zone ([13:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=809s)–[13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)). Ras Mic compares an overfilled agent to last-minute exam cramming: information piled on again and again stops sticking ([31:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1895s)–[31:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1917s)).
- **Percentages vs tokens** *(this note's synthesis, not a source claim)*. A percentage means different things on different window sizes.
  - On a 200K window, Nate's 60% is about 120K tokens and Ras Mic's 70% is about 140K. Both land inside the Coding Sloth's 100K–200K range.
  - On a 1M window the same percentages are 600K–700K, far past where the Coding Sloth says quality dips.
  - If you use a 1M-window model, reading the thresholds as token counts is the more cautious choice.
- **Laziness is the same symptom seen from the task side.** See [[Agent Laziness]].

### Tokens are also your usage limit

- **Usage is metered in tokens, not prompts.** The Coding Sloth: every message, file read and response costs tokens, so context management matters on the $20 plan and the $100/$200 plans alike ([12:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=762s)–[12:59](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=779s)). The aim is to make tokens last for your limit and for Claude's performance at the same time ([13:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=780s)–[13:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=784s)).
- **Tight plans run out fast.** On the $20 plan he has hit the limit after one or two prompts ([00:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=21s)–[00:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=25s)).
  - A medium or big task always takes at least ~50K tokens, and research, a skill or an MCP can push it past 100K ([14:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=853s)–[14:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=859s)).
  - So chaining tasks in one session both worsens output and burns through the limit ([14:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=862s)–[14:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=866s)).
- **Subagents multiply spend.** Each runs as its own complete conversation alongside the others, so on the cheapest paid plan a modest multi-agent setup can exhaust the allowance before the task ends ([20:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1206s)–[20:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1221s)).
- **Savings count twice.** Ras Mic: saving context saves money *and* gives a better-performing agent ([31:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1919s)–[32:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1926s)).
- **Opus is especially hungry.** [[Knowing More - Every Claude Model Explained]] counts heavy token use among Claude's downsides ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)–[06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)). It jokes that Opus can hit a rate limit within three prompts ([04:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=256s)–[04:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=262s)). See [[Choosing a Claude Model]].
- **Track the usage windows as a metric.** [[Chase AI - The Three-Step Claude Code Agentic OS]] keeps his 5-hour window, weekly window and routines used today on a dashboard beside the terminal ([14:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=894s)). See [[Build an Agentic OS Dashboard]].

### The levers

| Lever | What it does | Source and timestamps |
|---|---|---|
| Status line | Keeps context % (plus model and cost) always visible | Nate [00:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=54s)–[01:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=74s) |
| `/context` | Shows what is consuming the window | Nate [01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)–[02:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=127s). The Coding Sloth: run it before big tasks, though the number alone fixes nothing [13:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=831s)–[13:58](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=838s) |
| `/compact` with keep-instructions | Summarises the history; you name what must survive | Nate [02:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=143s)–[02:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=150s). The Coding Sloth [15:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=923s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s) |
| `/clear` or a new session | Empties the conversation. CLAUDE.md and your files are still there | Nate [02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s)–[02:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=165s). The Coding Sloth [14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=849s) |
| Esc early, `/rewind` | Stops tokens being spent in the wrong direction; rolls back | Nate [07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)–[07:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=474s), [08:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=503s) |
| Specific prompts, no research tangents | Stops Claude reading everything to guess what you meant | The Coding Sloth [14:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=866s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s). Nate: give only what the task needs, in small steps [01:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=95s)–[01:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=106s) |
| Subagents | Heavy reading happens in a separate window, and only a summary comes back | Nate [04:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=293s)–[05:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=313s), [06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)–[06:23](https://www.youtube.com/watch?v=jqoFP9QapXI&t=383s). The Coding Sloth [19:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1189s)–[19:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1196s) |
| Skills instead of always-loaded text | While idle, a skill costs only its name and description | Ras Mic [04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)–[04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s), [30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)–[30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s) |
| Lean, routed CLAUDE.md | 150–200 lines at most; point to files instead of holding their content | Nate [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)–[07:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=461s) |
| Requirements written to files | Still there late in a long session, when chat instructions have faded | AI LABS [07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s) |
| Terse replies and trimmed tool output | Fewer words and no unneeded code; in Claude Code, repeated text is also stripped from tool results | AI LABS on the Chisle plugin [03:14](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=194s), [04:03](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=243s) |

The buildable version of this table is [[Context Hygiene Routine]].

### Files beat instructions in long sessions

- **Why instructions fail.** [[AI LABS - The Unlazy Skill for Lazy Agents]] says the earlier version of the Unlazy skill fought laziness by telling the agent to be thorough. That failed, because an instruction is the first thing to fade in a long session ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)).
- **The fix.**
  - The new version writes the requirements into a file before any work begins ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)).
  - In orchestrated mode, each task goes to a fresh agent that receives only the plan and its own checklist ([08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)–[08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)).
- **The general lesson** *(this note's framing)*. Anything that must still be true three hours into a session belongs on disk, not only in the chat. See [[Agent Laziness]] and [[Evidence-Gated Completion Ledger]].

### What the agent writes and reads back fills the window too

- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] counts long, oddly laid-out replies and unneeded code as token waste ([03:06](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=186s)–[03:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=203s)). Its pick is the Chisle plugin (captioned "Chisel"): four skills plus hooks that fire at session start, on each prompt and after each tool call ([03:45](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=225s)–[04:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=241s)).
- The context saving is Claude Code-only: repeated or unnecessary text is stripped from tool results before the agent reads them ([04:03](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=243s)–[04:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=263s)).
- The figures are the author's: about 1,500 tokens down to about 600 on a search-box change ([03:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=206s)). No independent test is shown; the repo's own caveats are under *Beyond the source*.

## When to use it — and when not to

- **Always:** in long or multi-step Claude Code sessions, on plans with tight limits, and whenever you run subagents or agent teams.
- **Most important at three moments:** before a big task (check how much headroom you have), when you switch topics, and when you pass your threshold.
- **Less important:** a quick one-off question in a fresh session, or a small edit that fits comfortably. Don't spend effort optimising a 20K-token session.
- **Counterpoint: a large window is real capacity.**
  - [[Knowing More - Every Claude Model Explained]] pitches Sonnet 4.6's 1M-token window as roughly 2,000–3,000 pages in one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)–[02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)), used for whole-document research ([02:40](https://www.youtube.com/watch?v=BJauPEH_9OU&t=160s)–[02:42](https://www.youtube.com/watch?v=BJauPEH_9OU&t=162s)).
  - It cites Rakuten engineers running Opus 4 for seven straight hours without it losing focus ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s)–[04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)). Note that this is an older model than the Opus 4.7 the segment is about.
  - Having room to load everything doesn't mean quality holds at that load, which is the other sources' point. The same video also complains that Claude burns through tokens fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)).

## Perspectives from sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]] treats context as the first thing beginners should manage:
  - a status line to watch context rot ([01:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=71s));
  - `/context` to find bloat ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s));
  - `/compact` at ~60% with keep-instructions ([02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)) and `/clear` between tasks ([02:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=155s));
  - early Esc ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)), cheap subagents that return short summaries ([06:10](https://www.youtube.com/watch?v=jqoFP9QapXI&t=370s)), and a CLAUDE.md capped at 150–200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]] supplies the anatomy of the window ([06:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=368s)) and the ~70% ceiling ([31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)). He also makes the strongest case for keeping always-loaded files nearly empty: tell the model only what it can't know by itself, such as a non-default currency rather than "use a dollar sign" ([32:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1951s)–[32:52](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1972s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] writes from a $20-plan perspective. Tokens are both quality and quota ([12:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=771s)), and the dumb zone starts well before the limit ([13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)). His habits: a new session per task, stopping tangents, very specific prompts ([14:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=841s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s)), and starting over after an auto-compact ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]] ties a filling context to agents cutting corners ([02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s)–[02:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=148s)). Its answer is structural rather than a habit: requirements in files, and fresh subagent contexts per task ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s), [08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)).
- [[Knowing More - Every Claude Model Explained]] is the counterpoint that sells window size as capacity ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)). It says nothing about quality at high fill, but does flag token burn and rate limits ([04:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=256s), [06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] adds output-side savings through Chisle ([03:14](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=194s)).
- [[Chase AI - The Three-Step Claude Code Agentic OS]] treats the usage windows as dashboard metrics ([14:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=894s)).

## Where sources disagree

- **Compact and continue, or start again?**
  - Nate presents `/compact` at ~60% as the way to keep going without losing what matters ([02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)–[02:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=140s)).
  - The Coding Sloth treats a mid-task auto-compaction as a signal to open a new session, because quality drops noticeably. He compacts by hand only when a task truly can't be split ([15:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=911s)–[15:28](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=928s)).
  - The two may be closer than they sound *(this note's reading)*. Nate describes an early, manual compact with explicit keep-instructions. The Coding Sloth's warning is about the automatic one that fires at the limit.
- **Where the threshold sits.** 60% (Nate, [02:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=134s)), about 70% (Ras Mic, [31:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1884s)–[31:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1887s)), or 100K–200K tokens (the Coding Sloth, [13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)–[13:44](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=824s)). All three are personal rules of thumb; none of them shows a measurement.
- **How much belongs in CLAUDE.md.**
  - Ras Mic says 95% of people don't need AGENTS.md or CLAUDE.md at all ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). His exception is proprietary facts, or a methodology that must be referenced in every conversation ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)–[03:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=196s)).
  - Nate keeps a routed CLAUDE.md of up to 150–200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)–[07:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=435s)).
  - Chase AI adds a description of how memory is structured, arguing it saves tokens when Claude looks things up ([11:55](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=715s)).
  - Ras Mic and Nate agree the always-loaded file must stay small. See [[Keep CLAUDE.md Lean]] and [[CLAUDE.md as a Router]].
- **Is a big window capacity or a trap?** Knowing More sells 1M tokens as thousands of pages ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)). The Coding Sloth says a bigger window just means a bigger dumb zone ([13:29](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=809s)–[13:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=815s)).

## Beyond the source

- **Window sizes and auto-compaction today.**
  - Per Claude Code's model-config docs, Fable 5 and 5.1, Sonnet 5 and Opus 4.7 and later run with a 1M-token window by default on the Anthropic API, and auto-compact at about 967K tokens. Sonnet 4.6 and Opus 4.6 without extended context compact at 200K, as do Opus 4.8 and Opus 5 where a cloud provider runs them with a 200K window.
  - You can lower the auto-compact point with `/autocompact 500k` (saved to user settings), `claude --autocompact 500k` (one launch only), the `autoCompactWindow` setting, or the `CLAUDE_CODE_AUTO_COMPACT_WINDOW` variable, which takes a plain token count and overrides the others. The command and flag accept 100K–1M, capped at the model's window.
  - So Ras Mic's "~250K" ([06:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=413s)) and the Coding Sloth's "about 300K" ([13:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=801s)) are not current figures.
  - Verified: <https://code.claude.com/docs/en/model-config>
- **Window sizes on other Claude surfaces.**
  - claude.ai chat on paid plans: 1M tokens for Fable 5.1, Opus 5 and Sonnet 5; 500K for Opus 4.6–4.8 and Sonnet 4.6; 200K (about 500 pages) for other models.
  - In Cowork, Sonnet 5 auto-compacts at 500K.
  - Verified: <https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans>
- **CLAUDE.md is a permanent occupant, not re-added each turn.**
  - It loads at session start and stays in the window. Claude Code sends the whole conversation with every request, and prompt caching makes re-reading that history cheaper. Ras Mic's "added at every turn" ([03:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=198s)) is loose wording for that.
  - Per the docs, CLAUDE.md arrives as a user message after the system prompt, not inside it. That qualifies Nate's "basically the system prompt" ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s)).
  - Target: under 200 lines per file, because longer files use more context and reduce adherence.
  - Verified: <https://code.claude.com/docs/en/costs>, <https://code.claude.com/docs/en/memory>
- **What survives `/compact`.**
  - The project-root CLAUDE.md is re-read from disk and re-injected.
  - Nested CLAUDE.md files and path-scoped rules reload when Claude reads matching files.
  - Instructions given only in chat can be lost.
  - The startup list of skill descriptions is not re-injected, but the bodies of skills you already invoked are, capped at 5,000 tokens each and 25,000 in total (oldest dropped first).
  - Auto memory and a plan written in plan mode are also re-injected from disk, and Claude Code re-reads up to five of the most recently modified files from the session.
  - Verified: <https://code.claude.com/docs/en/memory>, <https://code.claude.com/docs/en/context-window>
- **Compaction has a cost; `/clear` doesn't.**
  - `/compact` reads the whole conversation it summarises, so compacting a large context is itself a large request. `/clear` costs nothing.
  - You can add a "Compact instructions" section to CLAUDE.md to steer every compaction.
  - Verified: <https://code.claude.com/docs/en/costs>
- **MCP definitions are now deferred.**
  - By default only tool names enter context until a tool is used, which largely retires Nate's MCP-bloat argument ([11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s)).
  - CLI tools (`gh`, `aws` and similar) are still leaner, and `/context` shows what is really using space.
  - Verified: <https://code.claude.com/docs/en/costs>
- **How subagent isolation works.**
  - Each subagent starts with a fresh context and none of your conversation history. Verbose output stays in the subagent, and only a summary returns.
  - The built-in Explore subagent is read-only and skips CLAUDE.md to stay cheap.
  - Verified: <https://code.claude.com/docs/en/sub-agents>
- **Anthropic's own framing.**
  - Anthropic's engineering team calls the degradation *context rot* and treats context as a limited "attention budget". A transformer relates every token to every other token, so attention is stretched as length grows.
  - It recommends compaction, structured note-taking to files outside the window, and subagents that return condensed summaries of roughly 1,000–2,000 tokens.
  - Verified: <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
- **Chisle's README adds caveats.**
  - Its SessionStart ruleset costs about 1.6k tokens up front plus about 50 per turn. A user's audit of 173 sessions, linked from the README, found that overhead roughly cancelled the compressor's savings, because the ruleset was re-sent on every resume and clear. The README says that bug is fixed, but concedes the overhead still outweighs the saving on a one-line prompt.
  - Tool-output compression runs only in Claude Code and Pi. The headline benchmark measures output tokens on 20 single-turn prompts with no tools, and caveman still won on short coding tasks.
  - Verified: <https://github.com/JayPokale/Chisle>
- **Usage windows inside Claude Code.**
  - For Pro and Max subscribers, status-line scripts receive `rate_limits.five_hour` and `rate_limits.seven_day`, each with `used_percentage` and `resets_at`. `/usage` shows plan usage bars plus a breakdown by skills, subagents, plugins and MCP servers.
  - Session and weekly limits apply across models, so switching with `/model` doesn't restore access.
  - The docs' own take on trimming tool output is a PreToolUse hook that filters test output down to failures.
  - Verified: <https://code.claude.com/docs/en/statusline>, <https://code.claude.com/docs/en/costs>

## Related

- [[Context Hygiene Routine]]: the step-by-step routine built from this note
- [[Agent Laziness]]: what a filling context does to task completion
- [[Keep CLAUDE.md Lean]] and [[CLAUDE.md as a Router]]: shrinking the always-loaded layer
- [[Agent Skills]]: progressive disclosure as a context saver
- [[Subagents and Agent Teams]]: moving heavy reading out of the main window
- [[Choosing a Claude Model]] and [[Route Tasks to the Right Claude Model]]: token cost by model
- [[Context vs Connections]]: deciding what deserves to enter context at all
- [[Build an Agentic OS Dashboard]]: putting usage windows on screen
- [[Claude Code]]
- People: [[Nate Herk]], [[Ras Mic]], [[The Coding Sloth]], [[AI LABS]], [[Chase AI]]
