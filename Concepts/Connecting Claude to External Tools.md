---
type: concept
aliases: ["MCP", "Connectors"]
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]"]
tags: [topic/mcp, topic/context, topic/claude-code, topic/cowork, topic/managed-agents, topic/agentic-os, topic/permissions, topic/media, topic/skills]
---

# Connecting Claude to External Tools

## In one sentence

Claude only reaches systems outside its own files through a connector: an MCP server, a direct API call, or a command-line tool. The sources agree on three habits. Add only the connectors a job needs, pick the leanest format for it, and decide up front what each connected tool may do without asking.

## How it works

### Three connector formats

[[Jay E - The ARMS Framework for a Claude Agentic OS]] makes applications the last layer of his agentic OS. Doing real work with agents means they have to reach your apps ([18:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1114s)–[18:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1120s)). He names three usual ways people connect agents to apps: CLIs, APIs and MCP servers ([19:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1158s)–[19:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1170s)). The other sources each lean on one or more of them:

| Format | What Claude gets | Where the sources use it | Trade-off the sources raise |
|---|---|---|---|
| **MCP server** | A catalogue of tools it can inspect and call | Nate: Claude can see every tool and run any of them ([11:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=689s)). Simon: Notion in Cowork ([28:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1717s)). Managed Agents: Slack and Asana ([02:07](https://www.youtube.com/watch?v=NLWiIj47IdI&t=127s)). Nate: Context7 ([15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s)) | Tool definitions take up context ([11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s)). This is now largely dated for Claude Code; see *Beyond the source* |
| **Direct API endpoint** | The one call a project needs, hardcoded | Nate: reading a single Notion database ([11:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=701s)–[11:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=716s)) | Leaner, but you build and maintain it yourself (this note's inference) |
| **CLI** | An existing command-line tool run from the shell | Nate: BigQuery's bq ([13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s)). Jay: CLIs he generated for MyFitnessPal and Skool ([20:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1211s)) | Works for any CLI-based tool, Nate says ([13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)) |

Why a connector costs anything at all: [[Ras Mic - How AI Agents and Claude Skills Work]] explains that tool definitions have to sit in the context window. The model doesn't execute tools; the harness around it does, so the model needs the definitions in front of it to ask for a call ([06:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=370s)–[06:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=385s)). See [[Context Window Management]].

### Jay E: three levels of getting connected

1. **Browse the directory.** In the Claude Code desktop app, Customize > Connectors lists apps you can connect ([18:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1122s)–[18:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1131s)). He doesn't think this is the most efficient route ([18:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1134s)).
2. **Let Claude find the connector.** Claude Code can connect apps itself or search for connectors that exist ([18:59](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1139s)–[19:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1145s)).
   - His *search connectors* skill looks on the web for an official connector first. Failing that, it looks for community-made ones as CLIs, APIs or MCP servers ([19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s)–[19:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1165s)).
   - For Adobe Premiere it checked for an official Adobe connector, looked at community options and recommended an open-source GitHub repo ([19:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1172s)–[19:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1183s)).
   - To use it, he stays in the same session and asks Claude Code to scan the repo for safety and then set it up ([19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)–[19:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1191s)). The skill's contents and the scanning method aren't shown.
3. **Build your own.** Where no agent connector exists, he generates one with Matt Van Horn's CLI Printing Press ([19:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1193s)–[20:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1207s)). His examples are MyFitnessPal and Skool ([20:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1211s)–[20:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1221s)).

### The Coding Sloth: only when Claude must touch something outside the code

- He rates MCP servers A tier. They give Claude access to GitHub, your database, Slack, analytics, deployments and, for front-end work, a browser ([10:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=600s)–[10:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=610s)).
- His own uses: pulling design inspiration, seeding a database with fake data to test features, researching documentation, and browser testing ([10:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=611s)–[10:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=619s)).
- **His rule:** you only need an MCP server when Claude has to interact directly with something outside your codebase. Best practices, patterns and how-to knowledge belong in a skill ([10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s)–[10:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=631s)). See [[Agent Skills]].
- **Don't pile them up.** Install only what's necessary, which he calls the big pattern with AI generally ([10:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=633s)–[10:40](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=640s)).
- Some former MCP jobs are now built in. For front-end verification he uses screenshot testing and browser testing, and says these used to need MCP servers but now come built in ([09:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=577s)–[09:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=596s)).
- Connectors spend budget. Asking Claude to research, use a skill or call an MCP server can push a single task past 100,000 tokens ([14:16](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=856s)–[14:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=859s)).

### Nate Herk: context cost, narrow endpoints, CLIs and live docs

- **Find the bloat first.** `/context` breaks token use down by category, MCP servers included, so you can see what's eating the window ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)–[02:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=125s)).
- **Hack 24, API endpoints instead of MCP servers (situational).** He says MCP servers load their entire tool definitions into context, so when tokens are tight a direct endpoint can be better ([11:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=684s)–[11:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=699s)). If a project only needs to read one Notion database, there's no point teaching Claude every other Notion function. Hardcode that endpoint instead ([11:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=701s)–[11:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=716s)). *Dated: current Claude Code defers MCP tool definitions by default. See Beyond the source.*
- **Hack 28, analytics without SQL.** Connect a CLI such as BigQuery's `bq`, then ask plain-English questions like last quarter's top revenue sources. Claude writes the query, runs it and answers ([13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s)–[13:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=811s)).
- **Browser control as a fallback.** Where there's no API, browser control lets Claude go in and do the steps by hand ([09:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=593s)–[09:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=596s)).
- **Hack 32, Context7.** Install the Context7 MCP server and tell Claude to use it whenever you need current documentation ([15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s)–[15:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=916s)).
  - The problem it solves: because of its training cutoff, Claude may suggest functions or APIs that were renamed, deprecated or never existed ([15:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=917s)–[15:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=925s)).
  - Context7 holds up-to-date, version-specific docs and code examples for popular libraries such as Next.js, React and MongoDB ([15:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=925s)–[15:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=939s)).
  - It puts current docs into the conversation before Claude writes code. He says it takes one command to install ([15:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=941s)–[15:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=951s)). This matches the Sloth's "researching documentation" use above.

### Simon Pittman: connectors in Claude Cowork

- **Where they live.** Customize > Connectors. His connected tools: Notion, Slack, Supabase, Vercel (for building websites), Make.com automations, Google Calendar, Google Drive and Gmail ([20:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1236s)–[20:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=1257s)).
- **Claude in Chrome** is enabled from the same page. It's a browser extension that lets Claude browse sites, read pages, fill in forms and click through multi-step workflows ([21:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1263s)–[21:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=1279s)). It's a beta that comes with risks ([22:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=1326s)–[22:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1331s)), and optional: everything else works without it ([23:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=1393s)–[23:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=1396s)).
- **Breadth.** His advice is to add every tool you use from the directory; each one asks permission ([23:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1417s)–[23:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1424s)). He jokes that connecting PayPal would get scarier ([23:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1429s)–[23:54](https://www.youtube.com/watch?v=pl90LATQlHI&t=1434s)).
- **Per-tool permissions.** Gmail allowed only one connected account when he recorded ([24:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1455s)–[24:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1460s)). Tools like Notion expose many permissions, and each can be allowed, set to need approval, or blocked ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)). See [[Permissions and Approval Gates]].
- **Test and inspect.** He asks Cowork to check his inbox and calendar for tomorrow, then expands the tool calls to see what it actually ran ([24:54](https://www.youtube.com/watch?v=pl90LATQlHI&t=1494s)–[25:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=1513s)).
- **Context systems behave differently.** Email and calendar hold messages and meetings; Notion holds context ([28:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=1692s)–[28:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1698s)).
  - Notion connects through an MCP server that can query, read and write ([28:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1717s)–[28:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=1725s)). Finding one project page still took Claude several attempts ([28:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1731s)–[28:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1736s)).
  - His fix is a context map, a markdown file describing the workspace's databases, referenced from global instructions ([29:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1760s)–[30:05](https://www.youtube.com/watch?v=pl90LATQlHI&t=1805s)). With it, Claude went straight to the right database ([30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)–[30:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1838s)).
  - He says it works for any store you use ([30:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1844s)–[30:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1853s)) and stops Claude burning tokens hunting for things ([31:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1863s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s)). Build it with [[Build a Context Map for a Connected Tool]]; the lookup-order idea is in [[Tiered Lookup Routing]].
- **Connectors keep working on a schedule.** Scheduled tasks use your instructions, connectors and context ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)–[41:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2501s)). His weekly briefer tells Claude to read his About Me files and use the Notion MCP ([42:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2538s)–[42:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2542s)). See [[Schedule Recurring Claude Tasks]].

### Anthropic: MCP and custom tools in Claude Managed Agents

- MCP is one of the building blocks [[Anthropic - What Is Claude Managed Agents]] lists, alongside agents, sessions, environments, tools, memory, outcomes and multi-agent coordination ([03:32](https://www.youtube.com/watch?v=NLWiIj47IdI&t=212s)–[03:43](https://www.youtube.com/watch?v=NLWiIj47IdI&t=223s)).
- **Outbound.** The pricing agent posts a report link to Slack and opens a review task in Asana, both through MCP servers ([02:07](https://www.youtube.com/watch?v=NLWiIj47IdI&t=127s)–[02:13](https://www.youtube.com/watch?v=NLWiIj47IdI&t=133s)).
- **Inbound.** A monitoring alert arrives through a custom tool. The developer's backend receives the payload and passes it into a new session as a tool result ([02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s)–[02:40](https://www.youtube.com/watch?v=NLWiIj47IdI&t=160s)).
- **Gated.** Before the incident update goes to Slack, a permission policy stops it until a person approves the draft ([02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)).
- Environments are configured with packages and network controls ([00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s)–[00:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=17s)). See [[Build an Event-Triggered Managed Agent]].

### Connectors versus "connections"

[[Context vs Connections]] (from Nate Herk's second-brain video) says volatile data such as email and Slack stays where it lives, but the brain must be able to reach it. This note is about how it reaches that data. Jay's "connectors" are the plumbing, and Nate's "connections" are the data behind it. Keep the two words apart (this note's framing).

## When to use it — and when not to

The table combines the sources' advice. The choices in the middle column are this note's synthesis; each rationale cites its source.

| Situation | Leaning | Why |
|---|---|---|
| Claude must read from or act in a system outside the codebase | Add a connector | Sloth [10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s) |
| You want Claude to follow a practice or pattern | Write a skill, not an MCP server | Sloth [10:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=626s) |
| The project needs one narrow operation from a big service | A direct endpoint or CLI can be leaner. Check `/context` first | Nate [11:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=701s), [01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s) |
| A mature CLI already exists for the system | Let Claude drive the CLI | Nate [13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s) |
| Library APIs change faster than the model's training data | Add a live-docs server such as Context7 | Nate [15:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=917s) |
| There's no official connector | Search for community options, scan them, or generate your own CLI | Jay [19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s), [19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s), [20:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1201s) |
| The connected workspace is large and Claude flounders | Write a context map | Simon [28:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1731s), [29:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1760s) |
| A tool sends, posts, deletes or pays | Put it behind approval or block it | Simon [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s); Managed Agents [02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s) |
| A repeatable workflow calls a paid generation API | Wrap it in a skill; key in the project env | Scrollcraft [05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s) |
| Claude needs a service's rules and live access to it | A skill plus an MCP server | AI LABS [04:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=241s) |
| Several harnesses need the same apps | One scoped aggregator connector such as Zapier | Jack [12:27](https://www.youtube.com/watch?v=NAumQObJEwM&t=747s) |

**Pitfalls**

- **Connector sprawl.** The Sloth says not to install a bunch of MCPs, only what's necessary ([10:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=633s)–[10:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=642s)). *This note's reading:* every extra server is more to trust and more for Claude to choose between.
- **Installing community code on trust.** Jay's safety step is a single request to Claude Code, and no method is shown ([19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)). Ras Mic makes the same warning about downloadable skills: he reviews them and mines them for ideas but doesn't install them, and calls random people's skills an easy way to attack someone ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)). Treat third-party connectors the same way (this note's extension). See [[Build vs Install Third-Party Skills]].
- **Connecting high-stakes accounts casually.** Simon's PayPal aside ([23:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1429s)) is the case to plan for before you click connect.
- **Blind search in a big connected system.** It wastes attempts and tokens until you give Claude a map (Simon [28:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1731s), [31:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1863s)).
- **One connector that reaches everything.** Jack shares a single Zapier connection across all his harnesses ([12:27](https://www.youtube.com/watch?v=NAumQObJEwM&t=747s)). *This note's reading:* if that connection leaks or is scoped too broadly, every app behind it is exposed in every harness.

## Where sources disagree

- **Is MCP's context cost a reason to avoid it?** Nate says MCP servers load every tool definition, so a hardcoded endpoint can save tokens ([11:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=693s)). The Sloth still rates MCP A tier and only warns against installing too many ([10:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=600s), [10:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=633s)). Current Claude Code docs defer tool definitions by default (see *Beyond the source*), so Nate's token argument is mostly dated. *This note's reading:* in Claude Code, the stronger case for a narrow endpoint or CLI today is scope. Claude gets exactly one capability, and there are fewer tools to permission.
- **Directory or agent-driven discovery, and how many?** Simon says to browse the directory and add every tool you use ([23:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1417s)). Jay calls the directory the least efficient route and has Claude search for connectors itself ([18:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1134s), [19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s)). The Sloth pushes the other way on breadth: only what's necessary ([10:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=637s)).
- **MCP or CLI?** AI LABS' repos video picks MCP because its tools stay available. With a CLI you have to tell the agent when to use it, in the prompt or project instructions ([05:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=317s)). Nate's 32 Tricks has Claude drive CLIs such as `bq` or call narrow endpoints ([13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s)). AI LABS' June design video also claims MCP stays in context while skills load on demand ([04:41](https://www.youtube.com/watch?v=Ot582-E61ac&t=281s)), but tool search makes that mostly out of date (see *Beyond the source*). *This note's reading:* the choice is really about discoverability versus scope.

## Perspectives from sources

- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: connectors come as CLIs, APIs or MCP servers. Level 1 is the desktop directory, level 2 a skill that finds official or community connectors plus a safety scan, level 3 building your own CLI connectors ([19:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1158s), [19:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1148s), [20:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1201s)). See [[Agentic OS]].
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: use MCP only for systems outside the codebase, put knowledge in skills, and don't pile servers up ([10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s)–[10:40](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=640s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: check `/context`, swap a server for one endpoint when tokens are tight, drive CLIs like `bq`, and add Context7 for current docs ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s), [11:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=684s), [13:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=793s), [15:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=906s)).
- [[Simon Pittman - Set Up Claude Cowork]]: Cowork connectors for Gmail, Calendar, Notion and more, with per-tool allow, needs-approval or blocked settings, plus a context map so Claude can find its way around Notion ([20:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1236s), [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s), [29:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1760s)). See [[Set Up Claude Cowork]].
- [[Anthropic - What Is Claude Managed Agents]]: MCP servers for Slack and Asana, a custom tool for inbound alerts, and a permission policy before posting ([02:07](https://www.youtube.com/watch?v=NLWiIj47IdI&t=127s), [02:33](https://www.youtube.com/watch?v=NLWiIj47IdI&t=153s), [02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: tool definitions must sit in context because the harness runs the tools ([06:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=370s)). He is also wary of installing other people's packaged capabilities ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]]: adds Higgsfield's remote MCP server to claude.ai as a custom connector under Customize > Connectors, then signs in ([16:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1004s)). See [[Higgsfield]].
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: calls Zapier his "authentication layer". He connects it once and uses it from Claude, Codex, Antigravity and Hermes Agent instead of reconnecting tools in each ([12:15](https://www.youtube.com/watch?v=NAumQObJEwM&t=735s)).
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] and [[Nate Herk - The Scrollcraft Website Design Skill]]: call aggregator APIs (fal.ai and Kie.ai) from inside a skill ([07:19](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=439s)). Scrollcraft keeps the key in the project's environment ([05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s)).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: shadcn's skill and its MCP server are two parts that work together ([04:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=241s)). The MCP gives live access to the component registry, and the skill's rules, patterns and project context give the agent judgement to use components correctly ([04:49](https://www.youtube.com/watch?v=Ot582-E61ac&t=289s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: picks the MCP server over the CLI so the agent finds UI Skills without being told ([05:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=317s)). Caliper can test whether an MCP server earns its tokens ([11:29](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=689s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]]: uses a vendor plugin that connects the model to a desktop app and bundles skills for it. The model drives After Effects with scripts and computer use ([01:38](https://www.youtube.com/watch?v=C8dWdic-oK4&t=98s)). His demo runs in Codex.

## Beyond the source

*Not from the videos. Each item was checked on 2026-09-15 against the linked page.*

- **MCP tool search is the Claude Code default, which undercuts Nate's hack 24.**
  - At session start only tool names and server instructions load. Full definitions are deferred until Claude searches for them, so extra servers have little effect on the context window.
  - Claude Code falls back to loading tools upfront when `ANTHROPIC_BASE_URL` points to a non-first-party host. `ENABLE_TOOL_SEARCH` accepts `true`, `false`, `auto` (defer once definitions reach 10% of the window) or `auto:N`.
  - It needs Sonnet 4.5, Haiku 4.5, Opus 4.5 or a later model. A server can opt out with `alwaysLoad: true`.
  - Practical upshot: check `/context` before rewriting an MCP integration as raw API calls. Verified: [Claude Code docs, MCP](https://code.claude.com/docs/en/mcp).
- **Claude apps have their own loading setting.** Tool access can be Auto (the default, where Claude decides which connectors to load), Always available, or On demand (connectors load only when Claude searches for them). The two Help Center pages give slightly different thresholds:
  - The tool-access article suggests Always available for fewer than 10 frequently used connectors, Auto for roughly 10 to 30, and On demand for 30 or more, or when conversations hit length limits.
  - The general connectors article suggests considering On demand once 10 or more connectors are active.
  - Either way, the more connectors you have, the more deferred loading makes sense. Verified: [Manage Claude's tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access), [Use connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).
- **Adding servers in Claude Code.**
  - Remote server: `claude mcp add --transport http <name> <url>`. Local server: `claude mcp add --transport stdio <name> -- <command> [args]`.
  - Scopes: local (the default), project (a shared `.mcp.json`) and user.
  - Project-scope servers need workspace trust in interactive sessions.
  - Verified: [Claude Code docs, MCP](https://code.claude.com/docs/en/mcp).
- **Least privilege for connectors.**
  - The MCP docs say to verify you trust each server before connecting it, and warn that servers which fetch external content can expose you to prompt injection.
  - For databases, the docs' DBHub example connects as a read-only database user.
  - For OAuth servers, `oauth.scopes` pins the scopes Claude Code requests.
  - Verified: [Claude Code docs, MCP](https://code.claude.com/docs/en/mcp).
- **Permission rules for MCP tools.** Rules use `mcp__<server>` or `mcp__<server>__*` for a whole server, or `mcp__<server>__<tool>` for one tool. Deny and ask rules accept tool-name globs such as `mcp__*`. Allow rules accept a glob only after a literal `mcp__<server>__` prefix, so an allow rule like `mcp__*` is skipped with a warning. If an organization sets a claude.ai connector tool to `ask`, Claude Code prompts on every call, even in `auto` and `bypassPermissions` modes; a `blocked` tool is removed before Claude sees it. Verified: [permissions](https://code.claude.com/docs/en/permissions), [MCP org controls](https://code.claude.com/docs/en/mcp). Setup steps: [[Configure Safe Autonomy Permissions]].
- **Context7's current install.** The README gives `npx ctx7 setup` (with `--claude` to target Claude Code), recommends a free API key for higher rate limits, and suggests adding "use context7" to prompts. The remote server URL is `https://mcp.context7.com/mcp`. Verified: [upstash/context7 README](https://github.com/upstash/context7).
- **Gmail can now send, with approval by default.** The Google Workspace connector article says Claude can send, reply to and forward Gmail, and asks for approval before each of these by default. On Team and Enterprise plans, owners decide whether members may skip that. So Simon's "drafts only" is a habit enforced by instructions and permissions, not a product limit. Verified: [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors).
- **Cowork connector tools on Team and Enterprise.**
  - An organization setting, "Allow 'Always allow' for connector tools", decides whether members can skip per-task approval for write-capable tools.
  - Read-only tools are exempt only when the connector annotates them as read-only. Most custom connectors don't annotate their tools, so every tool on them stays gated.
  - Verified: [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans).
- **Managed Agents defaults.** MCP toolsets default to `always_ask`, so tools newly added to a server can't run without approval; the built-in agent toolset defaults to `always_allow`. Custom tools, like the demo's alert tool, run in your own application and aren't governed by permission policies. Verified: [Managed Agents permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies).
- **claude.ai connectors in Claude Code.** Custom connectors you add at claude.ai (Free plans get one) only load in Claude Code when you're signed in with a claude.ai subscription, not an API key. Turn them off with `disableClaudeAiConnectors`. Anthropic says to connect only servers you trust. Verified: [Claude Code docs, MCP](https://code.claude.com/docs/en/mcp), [Custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).
- **Scoping a shared Zapier connection.** You choose which apps and actions the AI can use, and you can require approval, review an action log or revoke access. Verified: [Zapier MCP](https://zapier.com/mcp).

## Related

- Concepts: [[Context vs Connections]] · [[Permissions and Approval Gates]] · [[Context Window Management]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Agentic OS]] · [[Routines and Scheduled Tasks]] · [[Generating Images and Video with Claude]]
- Techniques: [[Build a Context Map for a Connected Tool]] · [[Tiered Lookup Routing]] · [[Configure Safe Autonomy Permissions]] · [[Set Up Claude Cowork]] · [[Build an Event-Triggered Managed Agent]] · [[Schedule Recurring Claude Tasks]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[Claude Managed Agents]] · [[Claude in Chrome]] · [[Higgsfield]] · [[shadcn]]
- People: [[Jay E]] · [[The Coding Sloth]] · [[Nate Herk]] · [[Simon Pittman]] · [[Ras Mic]] · [[Jack Roberts]] · [[AI LABS]] · [[Chase AI]]
- [[Home]]
