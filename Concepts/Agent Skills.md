---
type: concept
aliases: ["Claude Skills", "SKILL.md"]
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]"]
tags: [topic/skills, topic/claude-code, topic/context, topic/portability, topic/teams, topic/cowork, topic/design, topic/mcp, topic/models]
---

# Agent Skills

## In one sentence

A skill packages a procedure. It is a folder whose SKILL.md tells the agent how to do one recurring job, optionally backed by reference files and scripts, and until a request matches it the agent holds only the skill's name and description ([[Ras Mic - How AI Agents and Claude Skills Work]] [03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s); [[Jay E - The ARMS Framework for a Claude Agentic OS]] [06:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=406s)).

## How it works

### One general agent, many skills

- **Skills instead of a new agent per job.** [[Nate Herk]] retells [[Barry Zhang]] and [[Mahesh Murag]]. Anthropic stopped building a separate agent for each job once the agent underneath proved general-purpose ([[Nate Herk - Build Skills Instead of Agents]] [00:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=29s)).
- **The phone analogy.** The model is the processor, the agent runtime is the operating system, and skills are the apps ([00:58](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=58s)). Each skill carries one job's process, context, scripts and examples ([01:15](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=75s)).
- **The talk is older than his framing suggests.** See Beyond the source.

### Anatomy: from one file to a folder with references and scripts

- **The minimum.** [[The Coding Sloth]] describes SKILL.md as a markdown guide for something you do over and over: your best practices, a process, or how you research something. Claude uses it when it judges it relevant, or when you tell it to ([[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [05:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=309s)–[05:25](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=325s)). [[Ras Mic]]'s whiteboard version has three parts: a name, a description, and the instructions underneath ([05:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=305s)).
- **Thin vs rich.** [[Jay E]] compares two of his own skills:
  - His cleanup skill is a single SKILL.md of instructions ([07:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=420s)).
  - His /robo brand skill is a folder. Its SKILL.md works as a router to reference files, such as a brand HTML page covering fonts and colour palettes ([07:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=436s)–[08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s)).
  - For complex jobs, enrich the skill with files rather than cramming everything into SKILL.md ([08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)).
  - Because /robo is so well defined, a one-line request plus a few answers to Claude's questions produced a finished PDF guide in one or two prompts ([08:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=510s)).
- **Bundled references.** ConardLi's web-design-engineer skill carries references for judging a design, spotting typical design failures, and reproducing the style of well-known sites. It consults them while it builds ([[AI LABS - Claude Design Skills for Beautiful Sites]] [04:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=271s)).
- **Scripts first.** Normally a model turns a reference image into a text summary and loses detail. tastemaker instead uses scripts to extract the exact design details into a structured format that agents can reuse ([10:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=628s)–[10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s)). It also hands scripts anything that doesn't need the agent ([10:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=647s)).
- **Save scripts that already work (DRY, "don't repeat yourself").** In Nate's retelling, Claude kept rewriting nearly the same slide-styling script, which wasted tokens and gave varying results, until the team had Claude save the script inside the skill ([01:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=90s)). Have Claude put a working script in the skill's scripts folder and point SKILL.md at it ([02:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=149s)). Then check that later runs call that file ([02:42](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=162s)).
- **One skill can call another.** AI LABS's marketing-UI skill tells Claude to use GSAP's skill whenever a landing page needs animation ([[AI LABS - Design Skills from Landing Pages to Mobile Apps]] [09:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=561s)).
- **Files beat exhortation.** Unlazy's first version just told the agent to be thorough. Instructions are the first thing lost in a long session, so the rewrite writes the requirements to a gates file before any work begins ([[AI LABS - The Unlazy Skill for Lazy Agents]] [07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)). See [[Agent Laziness]].
- **The single-file framing.** [[Nate Herk]] describes skills as reusable prompt files such as techdebt.md or codereview.md in .claude/skills ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [05:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=328s)–[05:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=341s)). The current format is one folder per skill, each with a SKILL.md; see Beyond the source.

This illustration of the full shape is the vault's own, based on the docs cited under Beyond the source:

```
.claude/skills/brand-pdf/
├── SKILL.md          # name + description frontmatter; short steps that point to the files below
├── references/
│   ├── brand.html    # fonts and palette (Jay E's visual-reference idea)
│   └── layouts.md
└── scripts/
    └── check_pdf.py  # deterministic check; only its output enters context
```

### Progressive disclosure: why a skill costs little until it's used

- **Only the metadata is loaded.** Ras Mic says the whole skill isn't in context, only its title and description. Ask for a Notion report, and the agent notices it has a matching skill and only then reads the full file ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)–[04:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=247s)).
- **The cost comparison.** A 1,000-line CLAUDE.md of about 7,000 tokens is paid on every run, and most of it probably belongs in a skill ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)–[04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s)).
- **His demo.**
  - His 116-line code-structure skill ([29:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1786s)) counts 944 tokens in full, against 53 for the name and description alone ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)–[30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s)).
  - He counted with OpenAI's tokenizer, not Claude's ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)), so treat the numbers as approximate.
- **It's about quality too.** Beyond cost, he says the model gets dumber as the context window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)). See [[Context Window Management]].
- **The description does the triggering.** His skill's description names the situation it handles, workflows duplicating the same operational logic. That is why a request to clean up code structure loads it ([30:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1802s)–[30:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1824s)).
- **Precision over coverage.** Nate's rules for descriptions:
  - Two vague ones, like general content help and marketing assets, leave Claude guessing, because neither says when it should run ([[Nate Herk - Build Skills Instead of Agents]] [03:54](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=234s)).
  - Give each skill one job, describe it in the words users actually say, and don't let two skills compete for the same request ([04:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=257s)).
  - Test each one with an obvious request, a reworded one and an unrelated one ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)).
  - Build it: [[Audit Skill Descriptions and Triggers]].

### Skills vs CLAUDE.md

- **Ras Mic.** Procedures belong in skills, not in an always-loaded file. His examples are how you generate a report or structure your code ([05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s)). He says 95% of people don't need AGENTS.md or CLAUDE.md at all ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)). His exception is proprietary or personal information that every conversation needs ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
- **The Coding Sloth.** CLAUDE.md isn't make-or-break, because skills can give similar or better results ([05:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=300s)).
- **Nate and Jay E.** Both keep a lean always-loaded file that points at skills instead of replacing them.
  - Nate: once you've made new skills, update CLAUDE.md ([06:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=396s)), and have it route to other files ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)).
  - Jay E: each department's router file is simply a list of skills and reference files ([12:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=765s)).
- **Simon Pittman.** He shows the opposite habit. He pastes his rules into Cowork's global instructions, and suggests adding a trigger-phrase rule there too, defining what "downloads" should mean ([[Simon Pittman - Set Up Claude Cowork]] [11:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=717s)–[12:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=734s)). *Vault reading:* by Ras Mic's rule, that procedure would be a skill.
- See [[CLAUDE.md as a Router]] and [[Keep CLAUDE.md Lean]].

### Skills vs MCP and connectors

- **The Coding Sloth.** An MCP server earns its place only when Claude must reach something beyond your codebase. Best practices, patterns and how to implement something belong in skills ([10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s)–[10:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=631s)). The discipline is the same for both: don't pile them up ([10:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=633s)).
- **Jay E.** A skill can drive the connecting. His search-connectors skill looks for an official connector first, then for community-made CLIs, APIs or MCPs ([19:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1146s)). Before setup, he asks Claude Code to scan the recommended repo for safety ([19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)).
- **Pair a skill with an MCP server.** For shadcn, AI LABS use the skill for rules and project context, and the MCP server for live registry access ([[AI LABS - Design Skills from Landing Pages to Mobile Apps]] [04:52](https://www.youtube.com/watch?v=Ot582-E61ac&t=292s)). They also argue that MCP always sits in context while a skill loads on demand ([04:41](https://www.youtube.com/watch?v=Ot582-E61ac&t=281s)). That point is dated, because Claude Code now defers MCP tools (Beyond the source). See [[Build Product UI from a Component Registry]].
- **MCP can deliver skills.** UI Skills lets the agent search a library of skills and fetch only the instructions that match ([[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] [05:10](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=310s)).
- See [[Connecting Claude to External Tools]].

### Skills vs plugins

- **Simon, in [[Claude Cowork]].** Built-in skills handle standard, single jobs. Plugins teach Cowork something no one else has ([38:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=2288s)). His metaphor: skills are tools in the toolbox, while a plugin is closer to taking on an expert who arrives with a kit and methods of their own ([40:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2437s)–[40:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=2450s)).
- **Customising a plugin.** He installed Anthropic's customer support plugin, clicked Customize and described his business. Claude then read up on who he is and what he does, and ran its plugin-customizer skill to tailor the plugin ([39:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2377s)–[40:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=2417s)).

### When to make one

| Trigger | Source |
|---|---|
| You've prompted Claude for the same task twice | [[Jay E - The ARMS Framework for a Claude Agentic OS]] [05:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=332s) |
| A vague instruction failed and the model clearly needs a step-by-step guide | [[Ras Mic - How AI Agents and Claude Skills Work]] [08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s) |
| An audit of your recurring outputs, domain by domain, turns up a task that isn't a skill yet | [[Chase AI - The Agentic OS Setup for Claude Code]] [04:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=289s), [06:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=368s)–[06:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=398s) |
| A team SOP that everyone should run the same way | [[Nate Herk - 32 Tricks to Level Up Claude Code]] [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s) |
| Any repeatable workflow, best practice or research method | [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [05:15](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=315s) |
| An output came back the way you like it, such as an ad or a carousel style | [[Nate Herk - Claude as a One-Person Marketing Team]] [25:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1507s) |

- **Finding candidates.** [[Chase AI]] gives three routes:
  1. Describe a task you know you do, and have skill-creator build it ([06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s)–[07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s)).
  2. Have Claude review your last 3–20 sessions and chart the repeated tasks, their outputs and a proposed skill for each ([07:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=459s)–[08:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=525s)).
  3. Let Claude interview you about your days and weeks and call out your blind spots ([08:56](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=536s)).
- **The experimental /init.** The Coding Sloth notes that an interview-style version of /init also recommends skills and hooks ([03:45](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=225s)).
- **What not to make.** Ras Mic says a description of your tech stack, such as "React + Convex", needs neither a skill nor an AGENTS.md line, because the code is already context ([19:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1173s)–[20:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1202s)).
- **Build it:** [[Workflow Audit into Skills]].

### How to build one

- **Run it before you write it.** Ras Mic calls jumping from "I have a workflow" straight to writing the skill the worst thing you can do ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)).
  - Walk the agent through the workflow step by step ([09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s)). After a few successful runs, have it review what it did and write the skill ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s), [12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)).
  - A skill written up front, by hand or by AI, lacks the context of a run that worked ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)).
  - Chase agrees: confirm the manual version works, then convert it ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)–[07:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=456s)).
  - Build it: [[Build a Skill from a Successful Run]].
- **Let Claude write it.**
  - Ras Mic doesn't handwrite skills, and points out there's even a skill for creating skills ([12:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=747s)–[12:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=752s)).
  - Jay E and Simon both point to Anthropic's skill-creator ([05:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=354s); [32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)). Simon's tip: ask skill-creator to build in clarifying steps that use AskUserQuestion ([33:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2010s)).
  - Two of the design skills AI LABS tested, Emil Kowalski's design-engineering skill and elayadesign's landing-page skill, also ask questions before they build ([02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s); [06:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=387s)).
- **Keep improving it.**
  - Even with a SKILL.md, the agent will fail wherever the skill has gaps ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s)). Ask it why and what error it got ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)).
  - Feed the failure back. Once it gets the task right, tell it to update the skill ([21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s)–[22:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1332s)).
  - Five rounds of this made his eight-source YouTube report run reliably ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s)–[22:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1356s)).
  - Nate's version: when pushing back gets a better second attempt, tell Claude to update the skill ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
  - **Skills go stale.**
    - A newer model may already do what a skill says, leaving only its token cost ([[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] [09:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=580s)).
    - AI LABS updated even Anthropic's frontend-design prompt for Opus 4.8 and Fable 5 ([[AI LABS - Design Skills from Landing Pages to Mobile Apps]] [02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s)).
    - `/skill-doctor` shows a skill's cost and usage, not its value ([10:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=601s)). To judge value, compare runs with and without the skill, for example with Caliper ([10:15](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=615s)).
  - Build it: [[Skill Improvement Loop]] and [[Audit Skill Descriptions and Triggers]].
- **Enrich it.** Jay E shows an on-screen starter prompt that finds "thick" skills and refactors them to use reference files ([08:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=531s)). The prompt text isn't in the captions. Build it: [[Build a Reference-Rich Skill]].
- **Split or bundle?** Both work. elayadesign's landing-page skill sits entirely in one file ([05:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=327s)). Jakub Krehel gives typography, colour, accessibility and other areas a skill each ([08:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=536s)).

### Installing skills: beginner routes

| Route | Example | Source |
|---|---|---|
| Drag a skill file into the chat and ask Claude to install it in the project | Grill Me, a single markdown file | [[Nate Herk - Claude as a One-Person Marketing Team]] [10:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=653s) |
| Paste a public repo's URL and tell Claude to use it | Scroll World | Same video [17:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1047s) |
| Install it as a plugin, or copy its folders in | [[Scrollcraft]] | [[Nate Herk - The Scrollcraft Website Design Skill]] [02:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=177s) |
| Send the creator's install prompt; Claude confirms what it can now do | GPT Image 2 skill | [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] [06:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=406s) |
| Install a plugin in one click, then call it by command or in plain language | [[Higgsfield]] Motion Designer, in Codex | [[Chase AI - GPT-6 Astra Motion Design in After Effects]] [01:08](https://www.youtube.com/watch?v=C8dWdic-oK4&t=68s), [01:14](https://www.youtube.com/watch?v=C8dWdic-oK4&t=74s) |

- **"Just a markdown file."** Jay E and Nate both say this (see Where sources disagree). Claude Code looks for a `SKILL.md` inside a skill folder, though, so "install it" means Claude creating that folder (Beyond the source).
- **No vetting.** None of these routes includes reading the files first. See [[Build vs Install Third-Party Skills]].

### Running skills

- **By name or automatically.**
  - You can invoke a skill in plain language or with its slash command ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [05:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=344s)).
  - In [[Claude Design]], type a slash plus the skill's name, then describe what you want ([02:09](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=129s)).
  - [[Unlazy]] takes its arguments on the same line: the skill name, the tree depth, then the request ([11:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=678s)).
- **Headless.**
  - Jay E runs skills outside a chat with claude -p. It sends a single prompt such as /cleanup, with the model and effort level you choose ([09:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=582s)). That lets skills sit behind dashboard buttons or inside internal team apps ([10:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=604s)).
  - Chase's dashboard buttons work the same way ([27:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1636s)–[27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s)).
  - Build it: [[Build an Agentic OS Dashboard]].
- **Scheduled.** Once a task is a skill, Chase asks whether it should become an automation ([10:57](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=657s)). See [[Routines and Scheduled Tasks]] and [[Schedule Recurring Claude Tasks]].

### Portability

- **Across Claude surfaces and other agents.** AI LABS says skills added in Claude settings are the same ones available in Claude Design ([00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s)). They claim the same skills give the same result in [[Claude Code]], [[OpenAI Codex]] or any other agent ([01:02](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=62s)), but they assert this rather than show it. They do use Emil Kowalski's set in both Claude Code and Claude Design ([01:17](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=77s)).
- **One install, several agents.** Unlazy's installer asks which agents you use ([09:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=563s)). The skill lives once, in the .agents folder that Codex reads ([09:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=567s)). The .claude folder gets a shortcut to it, so Claude Code finds it without a duplicate copy ([09:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=598s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- **The advice is harness-neutral.** Ras Mic's sponsor-vetting agent runs on [[OpenClaw]] ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)), yet nothing in his skills advice depends on it.
- **A portable process doesn't give portable results.**
  - Nate says no skill can make a weaker model perform like a stronger one, and different models interpret the same skill differently ([[Nate Herk - Build Skills Instead of Agents]] [06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)).
  - The skills folder itself is an open format that works in compatible harnesses such as Codex or [[Hermes Agent]] ([06:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=386s)).
  - Test important skills in a second agent. If the results fall apart, look for hidden assumptions or instructions only one model understands ([06:34](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=394s)).
- See [[Tool-Agnostic Context Files]] and [[Port a Claude Code Brain to Other Agents]].

### How many

- **The Coding Sloth.** Don't install hundreds. Many skills are opinions about what good code looks like, so stick to one set that matches your style ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)–[08:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=506s)).
- **Ras Mic.** Setting up 30 skills and 15 subagents before you've built a single workflow gets things backwards ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)). Start with one agent and build up its skills first ([15:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=928s)). See [[Subagents and Agent Teams]].
- **AI LABS.** From a large collection, install only the skills that fit how you work ([11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)).

## When to use it — and when not to

- **Make it a skill** when it's a procedure you repeat, especially one with your own decision rules, output format or house style.
- **Keep it in CLAUDE.md** only if it must hold on every turn and the agent can't discover it itself. This is Ras Mic's proprietary-information exception ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
- **Use an MCP server or connector** when the job needs a live outside system ([10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s)). A skill can still describe how to use that system well.
- **Don't write the skill first** for a workflow you haven't yet completed with the agent at least once. Ras Mic and Chase both make this point ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s); [07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)).
- **Don't rely on skill prose alone** to make the agent finish its work deep into a long session. Put the checks in files or scripts ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)). See [[Verification Before Done]] and [[Evidence-Gated Completion Ledger]].
- **Don't install skills in bulk.** Whether to install someone else's skill at all is its own debate: [[Build vs Install Third-Party Skills]].

## Perspectives from sources

- [[Ras Mic - How AI Agents and Claude Skills Work]]: calls himself a skills maxi ([04:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=247s)). His approach is minimal context files, progressive disclosure, and skills built from successful runs, then refined after every failure ([22:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1377s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: skills are the first ARMS layer and "shortcuts" to your SOPs ([05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s)). He grows thin skills into reference-rich folders, then runs them headless ([09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: skills matter because they get a specific output done a specific way ([04:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=289s)). Audit your recurring work, convert validated tasks, and treat the results as workflows you can inspect and edit ([10:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=640s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: rates skills A tier, S if used smartly ([05:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=307s)). He favours a curated community set ([05:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=339s)), and reserves MCP for outside systems ([10:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=620s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: skills let you automate your SOPs, and committing them to GitHub shares them with your team ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)–[05:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=355s)).
- [[Simon Pittman - Set Up Claude Cowork]]: covers Cowork's built-in file skills ([32:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1931s)), creating, writing or uploading skills ([32:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1956s)), and plugins as the specialist layer ([38:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=2288s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]: skills made by designers steer models away from their recognisable default look ([00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s)). Some of the tested skills build a design, while others refine one, like Animate for animations ([02:38](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=158s)), or review one, like Jakub Krehel's review skill ([09:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=556s)). Skills added in Claude settings carry into Claude Design ([00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s)). See [[Escaping the Default AI Design Look]] and [[Build a Distinctive Site with Design Skills]].
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: a skill that enforces its own completion rules through files ([07:19](https://www.youtube.com/watch?v=c47uqR7XB_c&t=439s)). It installs once for several agents, and AI LABS edited it to fix slow one-at-a-time dispatch ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)).
- [[Anthropic - What Is Claude Managed Agents]]: skills also run in hosted API agents. The demo agent builds its spreadsheet deliverable with an Excel skill and adds an executive summary ([02:03](https://www.youtube.com/watch?v=NLWiIj47IdI&t=123s)). See [[Claude Managed Agents]].
- [[Nate Herk - Build Skills Instead of Agents]]: one general agent plus skills, kept reliable by saved scripts, precise descriptions, corrections written back and built-in checks ([09:01](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=541s)). He relays Anthropic's "guarantee" that whatever Claude records, later versions of Claude can reuse efficiently ([05:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=330s)). Anthropic's post only *hopes* agents will create and edit their own skills (Beyond the source).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: one skill per job, official skills first, and skills that hand off to each other ([00:24](https://www.youtube.com/watch?v=Ot582-E61ac&t=24s), [09:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=561s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: fetch skills from a registry ([05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s)), and re-test them after model updates ([09:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=580s)).

## Where sources disagree

- **Do you need CLAUDE.md at all?**
  - Ras Mic says mostly no; use skills instead ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)).
  - Nate keeps one, capped at 150–200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).
  - Simon puts rules, and even a trigger phrase, in his global instructions ([12:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=731s)).
  - Their settings differ. Ras Mic is mostly talking about codebases, where the code is already context ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
- **Write first or run first?**
  - Jay E pasted an X post into skill-creator, then tested the skill it produced ([06:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=372s)–[06:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=388s)).
  - Ras Mic says a skill drafted without a successful run lacks the context it needs ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)).
  - *Vault reading:* Jay's route still ends in testing, which is exactly where Ras Mic's improvement loop begins.
- **How many to add?** AI LABS says you can add as many of Emil Kowalski's skills as you like ([03:42](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=222s)), but install only what fits from bigger collections ([11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)). The Coding Sloth warns against installing hundreds ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)).
- **Install or build?** See [[Build vs Install Third-Party Skills]].
- **One file or a folder?** Nate frames skills as files like techdebt.md ([05:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=334s)). Jay E says a skill isn't just the markdown file ([06:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=406s)). The docs side with folders (below).
  - Nate has since described skills as folders: frontmatter up front, with scripts and references that stay in the folder until needed ([[Nate Herk - Build Skills Instead of Agents]] [03:33](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=213s)).
  - Jay E and Nate's marketing video still call a skill just a markdown file ([06:12](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=372s); [10:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=622s)).
- **Same result in every agent?** AI LABS claim the same skills give the same result in Claude Code, Codex or any agent ([01:02](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=62s)). Nate says only the process carries over, because models interpret skills differently ([06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)). Anthropic's guide sides with Nate (below).

## Beyond the source

- **The post and talk behind Nate's video.**
  - **The post.** Anthropic's Agent Skills engineering post (16 October 2025) is by Barry Zhang, Keith Lazuka and Mahesh Murag. It backs saving code in skills: pre-written scripts run without loading into context and behave consistently. It describes agents creating, editing and evaluating their own skills as something Anthropic *hopes* to enable, which is not a guarantee. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
  - **The talk.** Summaries place "Don't Build Agents, Build Skills Instead" at the AI Engineer Code Summit (19–22 November 2025), about ten months before Nate's video. One summary records the "future version of itself" line as said in the talk, so that part isn't Nate's invention. <https://lilys.ai/en/notes/agent-skills-20251225/build-skills-not-agents> <https://www.youtube.com/watch?v=CEvIs9y1uog>, <https://www.ai.engineer/code/2025>, <https://cobusgreyling.medium.com/anthropic-says-dont-build-agents-build-skills-instead-47e1a88435ab>
- **Test with each model.** Anthropic's authoring guide says a skill's effect depends on the model underneath. Check that Haiku gets enough guidance and that Opus isn't over-explained. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **MCP tool search.** Claude Code defers MCP tool definitions by default and finds them through tool search. Setups with a custom `ANTHROPIC_BASE_URL` or `ENABLE_TOOL_SEARCH=false` load them upfront. <https://code.claude.com/docs/en/mcp>
- **Three loading levels.** Name and description, roughly 100 tokens per skill, load at startup. The SKILL.md body loads when the skill triggers; the docs put this under 5k tokens. Bundled files cost nothing until they're read, and when scripts run, only their output enters context. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
- **Frontmatter rules.**
  - `name`: at most 64 characters, lowercase letters, numbers and hyphens only, and it can't contain "anthropic" or "claude".
  - `description`: must be non-empty and at most 1,024 characters. It should say what the skill does and when to use it, written in the third person.
  - <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **Folder format and locations.** In Claude Code a skill lives at `~/.claude/skills/<name>/SKILL.md` (personal) or `.claude/skills/<name>/SKILL.md` (project), and the folder name becomes the slash command. A single markdown file in `.claude/commands/` is the older format and still works. That older format is closer to what Nate describes. <https://code.claude.com/docs/en/skills>
- **Size and structure.** Keep the SKILL.md body under 500 lines. Move detail into reference files linked directly from SKILL.md, one level deep, and give long reference files a table of contents. Prefer bundled scripts for deterministic operations. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **Listing cost and cleanup.** Every skill in the listing adds its description to context on every turn, and the combined description and `when_to_use` text is cut off at 1,536 characters. `/skill-doctor` (v2.1.252 or later) reports each skill's context cost and how often it's used, so you can switch off the ones you don't use. <https://code.claude.com/docs/en/skills>
- **Manual-only skills.** `disable-model-invocation: true` stops Claude loading a skill automatically. Use it for workflows with side effects that you want to trigger yourself. It also keeps the skill's description out of context until you invoke it. <https://code.claude.com/docs/en/skills>
- **Anthropic's authoring process echoes Ras Mic.**
  1. Complete a task with Claude without a skill, and notice the context you keep supplying.
  2. Ask Claude to capture that context as a skill.
  3. Test the skill with a fresh Claude instance on real tasks.
  4. Bring what you observe back to refine it.

  The same guide also recommends building a few evaluations before writing extensive documentation. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **No sync between surfaces.** Custom skills in claude.ai, the API and Claude Code are managed separately. Uploads to claude.ai are zip files and belong to one user. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
- **Skills in Managed Agents.** Anthropic's pre-built `pptx`, `xlsx`, `docx` and `pdf` skills, or your uploaded ones, are attached through the agent's `skills` array, up to 500 per session. Skills in a mounted repo's `.claude/skills/<name>/SKILL.md` load automatically at session start with no review step, which puts that repo inside the agent's trust boundary. <https://platform.claude.com/docs/en/managed-agents/skills>
- **Open standard.** Claude Code skills follow the Agent Skills open standard, which Anthropic originally developed. Its site lists clients including Codex, Cursor, Gemini CLI, OpenClaw and Hermes Agent. <https://agentskills.io>, <https://code.claude.com/docs/en/skills>
- **Plugins.**
  - In Claude Code, plugins bundle skills, agents, hooks and MCP servers, and plugin skills are namespaced as `/plugin-name:skill-name`. <https://code.claude.com/docs/en/discover-plugins>
  - In the Claude apps, a plugin bundles skills, connectors and sub-agents. It works in chat and in Cowork, but hooks and sub-agents run only in Cowork. <https://support.claude.com/en/articles/13837440-use-plugins-in-claude>
- **Team sharing.** Commit `.claude/skills/` to version control, ship skills inside a plugin, or deploy them organisation-wide through managed settings. <https://code.claude.com/docs/en/skills>
- **Shared-install caveat.** The `npx skills add` installer that Unlazy uses has an open bug report from June 2026. Project-scope installs for Claude Code land in `.agents/skills/` without creating the `.claude/skills/` link, so Claude Code can't see the skill. After installing, check the link exists. <https://github.com/vercel-labs/skills/issues/1355>
- **MCP tools inside skills.** Refer to them by their fully qualified name (`ServerName:tool_name`), or Claude may fail to find the tool. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **Security.** Covered in [[Build vs Install Third-Party Skills]].

## Related

- **Concepts:** [[Build vs Install Third-Party Skills]], [[CLAUDE.md as a Router]], [[Context Window Management]], [[Connecting Claude to External Tools]], [[Tool-Agnostic Context Files]], [[Agent Laziness]], [[Verification Before Done]], [[Escaping the Default AI Design Look]], [[Subagents and Agent Teams]], [[Routines and Scheduled Tasks]], [[Agentic OS]], [[Loop Engineering]]
- **Techniques:** [[Audit Skill Descriptions and Triggers]], [[Build Product UI from a Component Registry]], [[Generate On-Brand Images from Claude Code]], [[Build a Scroll-Driven Landing Page]], [[Workflow Audit into Skills]], [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]], [[Build a Reference-Rich Skill]], [[Grill Me Interview Skill]], [[Build a Distinctive Site with Design Skills]], [[Evidence-Gated Completion Ledger]], [[Build an Agentic OS Dashboard]], [[Schedule Recurring Claude Tasks]], [[Keep CLAUDE.md Lean]], [[Set Up Claude Cowork]], [[Port a Claude Code Brain to Other Agents]]
- **Tools:** [[Claude Code]], [[Claude Cowork]], [[Claude Design]], [[OpenAI Codex]], [[Unlazy]], [[OpenClaw]], [[Claude Managed Agents]]
- **People:** [[Ras Mic]], [[Jay E]], [[Chase AI]], [[The Coding Sloth]], [[Nate Herk]], [[Simon Pittman]], [[AI LABS]]
