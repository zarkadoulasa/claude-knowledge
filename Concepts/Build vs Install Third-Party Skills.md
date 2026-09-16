---
type: concept
aliases: ["Third-Party Skills", "Installing Community Skills"]
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]"]
tags: [topic/skills, topic/privacy, topic/claude-code, topic/cowork, topic/design, topic/teams, topic/mcp]
---

# Build vs Install Third-Party Skills

## In one sentence

The sources genuinely disagree about installing skills other people wrote. [[Ras Mic]] reads them but builds his own from runs that worked, while [[The Coding Sloth]], [[AI LABS]] and [[Simon Pittman]] install curated skills and plugins (AI LABS also build their own for product work). The right call depends on whose expertise the skill encodes and what it can do on your machine.

## How it works

A skill is instructions, often with scripts, that your agent follows using whatever access it already has (see [[Agent Skills]]). So installing one raises two separate questions: can you trust it, and does it fit your work?

### Position A: build your own, and treat other people's skills as reading material

[[Ras Mic - How AI Agents and Claude Skills Work]]:

- **He doesn't install skills.** He reviews them, or hands one to his AI and asks what they can learn from it ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)).
- **Reason 1: fit.** Your agent needs the context of its own successful run, and a downloaded skill can't carry that ([12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)–[12:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=775s)).
  - Skills written without that context fail in practice: the agent botches the API call or pulls the wrong data ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)–[11:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=693s)).
  - The agent will copy what you do very closely, but only if you've given it something to copy ([11:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=701s)).
- **Reason 2: security.** Skill marketplaces are an easy way to attack someone, so be very careful with a random person's skills ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)).
- **Reason 3: your edge.** What you have that models don't is your own workflow, taste and strategy. Skills pay off when you codify those yourself, not when you download his ([29:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1751s)–[29:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1767s)). He even tells viewers not to download the code-structure skill he put on GitHub ([29:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1769s)–[29:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1776s)).
- **His own tension.**
  - He predicts that if skill marketplaces take off, people will sell well-defined, step-by-step skills. That demand exists because most people write skills without first working the workflow through with an agent ([22:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1361s)–[22:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1377s)).
  - So his objection is to skills that are unvalidated and carry none of your context. It isn't to using someone else's expertise as such.

Other sources partly back him:

- **[[Jay E - The ARMS Framework for a Claude Agentic OS]].**
  - He advises creating your own skills, because everyone's work is custom ([05:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=358s)–[06:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=369s)).
  - When a post on X gave him a useful tip, he pasted the post into skill-creator so Claude Code would build the skill, then tested it ([06:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=372s)–[06:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=388s)).
  - When his connector-search skill recommends a community repo, he has Claude Code scan it for safety before setting it up ([19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)).
- **[[Chase AI - The Agentic OS Setup for Claude Code]].** Validate a skill by doing the task by hand first, then convert it ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)–[07:36](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=456s)). He means your own skills, but it's the same instinct.

### Position B: install curated skills from people who know more than you

- **[[The Coding Sloth - 1000 Hours of Claude Code Lessons]].**
  - **Why install.** Community skills are companies and top engineers packaging their best practices. They help the agent, and reading them teaches you ([05:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=339s)–[05:54](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=354s)).
  - **Where he finds them.** skills.sh is his go-to for finding and installing skills ([05:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=355s)).
  - **His stack.**
    - [[Matt Pocock]]'s grill-with-docs, to refine requirements ([06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)), and improve-codebase-architecture ([06:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=377s)).
    - Cursor's thermo-nuclear code quality review, which he runs alongside improve-codebase-architecture to strip AI slop ([06:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=384s)–[06:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=401s)).
    - shadcn's improve, which audits a codebase and writes plans for other agents ([06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s)).
    - Claude Code's built-in code review and security review skills, which he rates B to A tier ([05:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=327s)).
  - **His guardrail is about fit, not security.** Don't install hundreds; stick to one set that matches your coding style ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)–[08:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=506s)).
- **[[AI LABS - Claude Design Skills for Beautiful Sites]].**
  - An impressive workflow is no proof: many design skills still produce a generic site, and only a few deliver ([00:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=7s), [00:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=13s)). Judge a skill by its output.
  - Every model follows its own recognisable design pattern ([00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s)–[00:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=30s)). The skills that counter it come from experienced designers who packaged workflows they had tested ([00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s)–[00:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=41s)). In other words, they are someone else's successful runs.
  - The video walks through seven collections AI LABS tested ([00:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=45s)). From a large collection, it says to install only the skills that fit how you work ([11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)). Yet of Emil Kowalski's set they say to add as many as you want ([03:42](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=222s)).
  - **Not purely installers.** For real product work they use skills they built and refined through testing, alongside open-source ones ([12:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=738s)–[12:25](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=745s)).
  - See [[Escaping the Default AI Design Look]].
- **[[AI LABS - The Unlazy Skill for Lazy Agents]]: install, read, adapt.**
  - They installed [[Leon Lin]]'s [[Unlazy]] with its installer ([09:08](https://www.youtube.com/watch?v=c47uqR7XB_c&t=548s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
  - As shipped, it was very slow ([10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)). Reading its instructions showed why: it handed out subagent tasks one at a time ([10:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=644s)–[10:58](https://www.youtube.com/watch?v=c47uqR7XB_c&t=658s)).
  - So they edited the skill itself ([11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)).
- **[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: prefer the tool maker's skill.**
  - Many of the best design skills come from the teams behind the tools ([00:24](https://www.youtube.com/watch?v=Ot582-E61ac&t=24s)), such as GSAP ([08:33](https://www.youtube.com/watch?v=Ot582-E61ac&t=513s)) and Expo ([13:20](https://www.youtube.com/watch?v=Ot582-E61ac&t=800s)).
  - An official skill isn't finished, though: they reworked Anthropic's frontend-design skill for newer models ([02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s)).
  - Pick one taste preset rather than stacking several ([10:15](https://www.youtube.com/watch?v=Ot582-E61ac&t=615s)). *Vault reading:* that is stricter than their later August video, which says to add as many of Emil Kowalski's skills as you like ([03:42](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=222s)).
- **[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: fetch on demand.** UI Skills pulls in only the instructions of the skills that match, so you don't install every design skill up front ([05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s)). *Vault reading:* instructions no one has read then enter the session at run time.
- **[[Simon Pittman - Set Up Claude Cowork]].**
  - He turns on Anthropic's example skills and customises them ([32:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1964s)), and recommends skill-creator ([32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)).
  - He uses frontend-slides, a skill he downloaded online ([37:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=2222s)), and installs Anthropic's plugins, such as legal ([38:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2307s)).
  - His answer to the "doesn't fit" objection is customisation. When he clicked Customize on the customer support plugin and described what he sells, Claude read up on who he is and tailored the plugin to his business ([39:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2377s)–[40:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=2417s)).
- **[[Nate Herk - 32 Tricks to Level Up Claude Code]].** Commit skills to GitHub so your whole team can use them ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)–[05:55](https://www.youtube.com/watch?v=jqoFP9QapXI&t=355s)). *Vault reading:* a colleague's skill sits between the two positions, since you know the author and they share your context.

### Creators handing out skills and plugins

Four recent videos hand viewers a ready-made package, usually the creator's own. None of them suggests reading the files first, and most run local tools, call paid services, or both.

| Creator and package | Install route | What it runs or calls | Source |
|---|---|---|---|
| Nate Herk, [[Scrollcraft]] | Plugin, or copy the folders in ([02:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=177s)); download from his free community ([16:23](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=983s)) | Generates missing images and video through Kie.ai with your API key ([05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s)) | [[Nate Herk - The Scrollcraft Website Design Skill]] |
| Nate Herk passes on Grill Me (a prompt file) and Scroll World (another developer's public repo) | Drag the markdown file into the chat ([10:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=653s)); paste the repo URL ([17:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1047s)) | Scroll World builds 3D scroll-driven sites ([16:03](https://www.youtube.com/watch?v=yCACmFTiCto&t=963s)) | [[Nate Herk - Claude as a One-Person Marketing Team]] |
| Jay E, GPT Image 2 skill | Send his install prompt ([06:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=406s)) | Calls the model through fal.ai, a model aggregator ([07:00](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=420s)) | [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] |
| Chase AI, [[Higgsfield]] Motion Designer | One-click plugin install ([01:08](https://www.youtube.com/watch?v=C8dWdic-oK4&t=68s)) | Scripts and computer use drive After Effects ([01:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=100s)) | [[Chase AI - GPT-6 Astra Motion Design in After Effects]] |

- *Vault reading:* Scrollcraft and the Motion Designer package craft. Jay E's skill is mostly API wiring, which he extends by pasting in a provider's docs ([11:51](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=711s)), and wiring is easy to rebuild yourself.
- Chase calls the plugin free, open source and credit-free ([00:21](https://www.youtube.com/watch?v=C8dWdic-oK4&t=21s)). Higgsfield's page doesn't back the open-source claim (Beyond the source).
- The marketing video also leans towards Position A: turn outputs you like into your own skills ([25:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1507s)).

### Where they really disagree, and where they don't

| Question | Ras Mic | Sources that install |
|---|---|---|
| Is it safe? | An easy attack vector ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)) | The Coding Sloth, AI LABS and Simon don't discuss vetting in these videos. Jay E scans a community repo before setting it up ([19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)) |
| Will it fit my work? | No: it lacks the context of your own successful run ([12:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=770s)) | Make it fit: pick one set that matches your style (Sloth [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s)), customise it (Simon [39:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=2385s)), or edit it (AI LABS [11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)) |
| Is reading them worthwhile? | Yes: read them and pull out lessons ([12:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=766s)) | Yes: reading them teaches you (Sloth [05:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=350s)) |
| How many? | 30 skills before you've built any workflow is backwards ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)) | Don't install hundreds (Sloth [08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)); install only what fits (AI LABS [11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)), though AI LABS would add all of Emil Kowalski's ([03:42](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=222s)) and build their own for products ([12:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=738s)) |
| What kind of skill? | Personal business workflows, such as vetting sponsors or an eight-source report ([07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s), [22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s)) | General craft: requirements, code quality, design taste (Sloth [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s); AI LABS [00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s)) |
| Where should it come from? | Your own successful run ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)) | The tool's maker (AI LABS [00:24](https://www.youtube.com/watch?v=Ot582-E61ac&t=24s)); a registry at run time (AI LABS [05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s)); a creator's free download (Nate [02:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=177s), Jay E [06:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=406s)) |

*Vault reading of the "What kind of skill?" row:* the sources partly talk past each other because they install different kinds of skills. Nobody else has Ras Mic's sponsor-vetting rules. A veteran designer, though, does know more about layout than a model's defaults.

## When to use it — and when not to

**This decision table is this note's synthesis, not any single source's view.** Each row cites the source evidence it rests on; the security points rest on Beyond the source.

| Situation | Choice | Basis |
|---|---|---|
| The skill encodes expertise you lack (design, code review, requirements) and comes from a known author or company | **Install.** Read every file first, and keep to one coherent set | Sloth [05:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=339s), [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s); AI LABS [00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s); Anthropic's audit advice |
| It comes from Anthropic (built-in skills, official plugins) or from a teammate's repo | **Install.** Still read a teammate's skill before enabling it | Simon [38:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2307s); Nate [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s); Anthropic counts only skills you wrote or got from Anthropic as trusted, and its Help Center says to review even skills a colleague shares |
| The workflow depends on your own accounts, data, rules or house style | **Build** it from a successful run, then refine it after each failure | Ras Mic [11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s), [21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s); Chase [07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s). See [[Build a Skill from a Successful Run]] and [[Skill Improvement Loop]] |
| It will run headless, on a schedule, or with broad permissions | **Build it, or audit it fully.** Don't let unread third-party scripts run unattended | Headless runs: Jay E [09:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=582s), Chase [27:16](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1636s); Claude Code's allowed-tools warning |
| A public skill comes close but isn't tuned to you | **Mine and adapt.** Have your agent read it and fold the lessons into your own skill, or fork it and note what you changed | Ras Mic [12:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=766s); AI LABS [11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s) |
| The package has a customise step | **Install, then customise** it with your own context files | Simon [39:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2377s) |
| The idea comes from a post, thread or video | **Rebuild it** with skill-creator, then test it where mistakes can't do much damage | Jay E [06:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=372s) |
| The tool's maker publishes an official skill (for example GSAP or Expo) | **Install that one first**, and re-test it after model updates | AI LABS [00:24](https://www.youtube.com/watch?v=Ot582-E61ac&t=24s), [02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s) |
| You'd otherwise install a pack to cover many visual styles | **Pick one preset**, or fetch from a registry and look at what it pulled in | AI LABS [10:15](https://www.youtube.com/watch?v=Ot582-E61ac&t=615s), [05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s) |
| A creator's free skill calls a paid API with your key | **Read it, check where the key goes and what a run costs**, then try one small job | Nate [05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s); Jay E [07:00](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=420s) |
| You're about to add a pack of dozens of skills before you have working workflows | **Don't** | Ras Mic [14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s); Sloth [08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s) |
| The author is unknown and the files include scripts, network calls or credential handling | **Don't**, or audit it against Anthropic's checklist first | Beyond the source |

Vault starter checklist before installing a third-party skill (original wording, based on the Anthropic guidance below):

- [ ] I know who wrote it and where it's maintained.
- [ ] I've read SKILL.md, every reference file and every script.
- [ ] Nothing fetches URLs, sends data out or asks for keys without a reason I accept.
- [ ] I'd approve its allowed-tools, and any hooks or MCP servers it brings, if they asked me directly.
- [ ] It doesn't overlap or contradict a skill I already have.
- [ ] I've run it once on a throwaway task and watched what it did.

## Perspectives from sources

- [[Ras Mic - How AI Agents and Claude Skills Work]]: build your own skills ([18:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1133s)), and read other people's instead of installing them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: install a small, style-matched set of skills from engineers and companies you respect ([05:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=339s), [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]: designer-made skills beat a model's default look; install the ones that fit ([00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s), [11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: install a promising skill, find where it falls short, and edit it ([10:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=644s), [11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)).
- [[Simon Pittman - Set Up Claude Cowork]]: use Anthropic's skills and plugins, then customise them with your own context ([38:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2307s), [39:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2377s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: create your own skills, and have Claude check a community repo for safety before using it ([05:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=358s), [19:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1185s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: validate a workflow by hand before turning it into a skill ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: share team skills through GitHub ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] and [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: start with the tool maker's skill, choose a single preset, or let a registry fetch skills per job ([00:24](https://www.youtube.com/watch?v=Ot582-E61ac&t=24s); [05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]], [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] and [[Chase AI - GPT-6 Astra Motion Design in After Effects]]: creators' own packages. [[Nate Herk - Claude as a One-Person Marketing Team]]: his version of Grill Me plus another developer's public repo, Scroll World. None adds a vetting step (see the table above).

## Beyond the source

- **Anthropic says to use trusted sources only.** That means skills you created yourself or got from Anthropic. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
  - A malicious skill can direct Claude to call tools or run code in ways that don't match its stated purpose.
  - Audit every bundled file.
  - Be wary of skills that fetch external URLs: fetched content can carry instructions, and a trusted skill's external dependencies can change later.
  - Treat installing a skill like installing software.
- **Enterprise vetting checklist.** <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise>
  - High-concern signs: scripts, instructions to ignore safety rules or hide actions, references to MCP tools, network calls, and hardcoded credentials.
  - Medium-concern signs: file paths outside the skill folder, and instructions to invoke tools.
  - The review steps include reading every file, running scripts in a sandbox, and checking for data-exfiltration patterns. Authors shouldn't review their own skills.
- **Automated scanning.** Claude Enterprise organisations can turn on skill and plugin security scanning for skills uploaded in claude.ai and Cowork. A skill that fails the scan is blocked. Scanning doesn't cover skills uploaded through the Skills API or the Claude Console, or skills already in the organisation when scanning was turned on. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise>
- **Help Center advice.** Review downloaded skills before enabling them, don't hardcode secrets, and take care when adding scripts (<https://support.claude.com/en/articles/12512198-creating-custom-skills>). It names prompt injection and data exfiltration as the main risks, and says to review a skill's contents before enabling it even when a colleague shared it (<https://support.claude.com/en/articles/12512180-using-skills-in-claude>).
- **Skills checked into a repo.** In Claude Code, a project skill's `allowed-tools` apply whenever the skill is invoked. That includes folders you've never marked as trusted and `-p` runs. Check the allowed-tools of any skills checked into someone else's repo before running Claude Code there. <https://code.claude.com/docs/en/skills>
- **Plugins are code.**
  - Claude Code's docs call plugins and marketplaces highly trusted components that can run arbitrary code with your user privileges. Anthropic doesn't control what third-party plugins contain. <https://code.claude.com/docs/en/discover-plugins>
  - Anthropic's community marketplace lists only third-party plugins that passed its automated validation, and pins each one to a specific commit. <https://code.claude.com/docs/en/discover-plugins>
  - In the Claude apps, plugins may include local MCP servers that run with your permissions. <https://support.claude.com/en/articles/13837440-use-plugins-in-claude>
- **Even Anthropic's examples are just examples.** The anthropics/skills repo says its skills are for demonstration and education, and that you should test them before relying on them. <https://github.com/anthropics/skills>
- **The risk is real.** Snyk's ToxicSkills research (February 2026) scanned thousands of public skills from ClawHub and skills.sh, the registry The Coding Sloth uses, and confirmed malicious payloads among them. It recommends auditing the skills you've installed, rotating any credentials they handled, and checking agent memory files for tampering. *Vault reading:* being listed on a registry is not the same as being vetted. <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>
- **Some third-party skills run commands by design.** Unlazy's README warns that its CHECK lines are shell code, to be read before you approve them, and its checker only runs them when you pass `--approve`. <https://github.com/Leonxlnx/unlazy>
- **UI Skills.** It's a registry you query with `npx ui-skills` or through an MCP server, whose tools are `list_skills` and `get_skill`. Its README describes no review of contributed skills, so the warning above about fetched content applies. <https://github.com/ibelick/ui-skills>
- **Higgsfield Motion Designer.** Higgsfield presents it as a ChatGPT plugin that Claude can also reach through Higgsfield's MCP, invoked with `@Higgsfield /use-after-effects`. The page doesn't mention open source, and it mentions credit pricing without saying whether the plugin uses credits. <https://higgsfield.ai/ai-motion-designer>
- **Anthropic's authoring advice supports building your own.** Its recommended process starts by completing the task with Claude without a skill, then capturing the context you kept supplying. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>

## Related

- **Concepts:** [[Agent Skills]], [[Permissions and Approval Gates]], [[Escaping the Default AI Design Look]], [[Agent Laziness]], [[Connecting Claude to External Tools]], [[Tool-Agnostic Context Files]]
- **Techniques:** [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]], [[Workflow Audit into Skills]], [[Build a Reference-Rich Skill]], [[Build a Distinctive Site with Design Skills]], [[Evidence-Gated Completion Ledger]], [[Configure Safe Autonomy Permissions]], [[Grill Me Interview Skill]], [[Audit Skill Descriptions and Triggers]], [[Build a Scroll-Driven Landing Page]], [[Generate On-Brand Images from Claude Code]], [[Build Product UI from a Component Registry]], [[Storyboard-First AI Video and Motion Graphics]]
- **Tools:** [[Claude Code]], [[Claude Cowork]], [[Claude Design]], [[Unlazy]], [[OpenClaw]], [[Scrollcraft]], [[Higgsfield]], [[shadcn]], [[OpenAI Codex]]
- **People:** [[Ras Mic]], [[The Coding Sloth]], [[AI LABS]], [[Simon Pittman]], [[Jay E]], [[Chase AI]], [[Nate Herk]], [[Matt Pocock]], [[Leon Lin]]
