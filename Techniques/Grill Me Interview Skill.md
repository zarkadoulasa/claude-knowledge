---
type: technique
goal: "Get what you know about a client, business, project or process out of your head and into the second brain, by letting Claude interview you one topic at a time and write a brainstorm file"
difficulty: beginner
time_to_build: "About 15 minutes to install the skill, then 20 to 60 minutes per interview (vault estimate)"
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tools: ["[[Claude Code]]"]
tags: [topic/skills, topic/claude-code, topic/second-brain, topic/prompting, topic/knowledge-graph, topic/privacy, topic/planning]
---

# Grill Me Interview Skill

> **Provenance.** Points with a timestamp link come from the source videos. The core material is from [[Nate Herk - Every Level of a Claude Second Brain]]. *Perspectives from other sources* adds six more, and names the source of every point. The starter `SKILL.md`, output template, prompts and checklists below are **original scaffolding written for this vault**, based on how he describes the skill. They are not his customised version and not [[Matt Pocock]]'s original. Facts about Claude Code and Matt Pocock's published skill are verified under **Beyond the source** at the end of this note.

## Goal

A Claude Code skill that **interviews you relentlessly about one topic**, writes what it learns to a brainstorm file, and doesn't stop until it has the whole picture. You can hand it files (transcripts, contracts) during the interview. The output becomes raw material for context files, the [[LLM Wiki]] or a [[Knowledge Graphs|knowledge graph]].

The reason it exists: a second brain often fails because the knowledge **never made it out of your head**, not because retrieval is weak ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).

## Use when

- **You're about to build a knowledge graph** and the entities and relationships aren't written down anywhere yet. Graph software builds the relationships well; your job is to give it enough data ([20:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1224s), [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)). See [[Build a Knowledge Graph Layer]].
- **The brain finds the right file but the answer is thin.** Before you blame the AI, check whether your files are complete and carry the nuance you hold in your head ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s), [22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s)).
- **You're onboarding a new client, business or project** into the brain. His example is one interview per entity: client A, then client B, then business A ([21:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1265s)–[21:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1270s)).
- **A [[Second Brain Pain-Point Audit]] reports capture gaps** rather than a retrieval problem.

**Don't use it for:**
- Volatile data that will change next week, such as Slack threads, emails or customer records. That belongs to connections the brain can reach, not content it stores ([27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s)–[28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)). See [[Context vs Connections]].
- Client or sensitive data you aren't comfortable sending to Anthropic. See the privacy point below ([21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)–[21:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1312s)).

## What the video says (Nate Herk, second-brain video)

| Point | Detail | Timestamp |
|---|---|---|
| Where it fits | It comes up in the Level 4 (knowledge graph) section. If you decide you need a graph (for all your projects, say), the data probably already exists in your files | [20:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1208s)–[20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s) |
| The real bottleneck | Graph tools are usually good at embedding data and creating relationships. The problem you have to solve is feeding them enough data | [20:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1224s)–[20:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1230s) |
| How Nate does it | He runs brainstorm sessions, and his project has a set of brainstorm files from them (the transcript doesn't give the folder name) | [20:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1233s) |
| Origin | The skill is called Grill Me. He got it from [[Matt Pocock]] and customised it a little | [20:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1237s)–[20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s) |
| Where to get his version | In his free [Skool community](https://www.skool.com/ai-automation-society/about), under Classroom → All YouTube resources, alongside his other skills | [20:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1243s)–[20:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1253s), [30:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1842s) |
| What it does | It questions him relentlessly about one topic and writes a brainstorm file | [20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s)–[21:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1260s) |
| When it stops | Only once it knows everything about the topic | [21:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1262s) |
| How to invoke | Per entity, in plain language, e.g. "Grill me about client A" | [21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)–[21:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1270s) |
| Inputs | It asks you questions, and you can also give it files such as transcripts and contracts | [21:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1272s)–[21:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1276s) |
| Outcome | This is how you build up a large body of data to work from | [21:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1278s) |
| Capture vs retrieval | People assume the system's retrieval is the problem. Sometimes it is, but sometimes the bigger problem is moving what you know from your head into the system | [22:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1342s)–[22:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1356s) |
| Self-check | Look at your folders and files: are they holistic, and do they carry the nuance you have in your head? | [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s) |

### Privacy aside (added while editing, right after the Grill Me segment)

- Anything you process through Claude models goes to Anthropic, so it isn't private ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s)).
- Nate is comfortable putting his own business data in and does so knowingly ([21:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1296s)–[21:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1301s), [21:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1318s)).
- If you don't want to send client data, consider open-source models, and maybe don't keep the everything-about-your-clients brain in Claude Code at all ([21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)–[21:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1312s)). Other options exist, and he plans future videos on local and open-source AI ([22:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1327s)–[22:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1333s)).
- *(Vault note, not from the video.)* This matters more for Grill Me than for most skills, because its whole job is to extract detailed, often client-specific knowledge.

### Related points that shape how you use the output

- **Keep control of ingestion.** Nate decides what the brain takes in. For example, he runs a skill to collect the week's meeting transcripts, and when he adds something he talks it through with Claude and they ingest it together (part of that sentence is unclear in the captions) ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)–[26:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1596s)). He worries about the point where more context does more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)–[26:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1582s)). Treat brainstorm files as material you review, not as something that flows straight into the brain.
- **Only store evergreen material.** Store things you won't delete. Ask whether this memory will still be useful in a year; if not, it's noise ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)–[27:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1671s)).
- **Careful ingestion is what makes a wiki feel relational.** Nate's LLM Wiki gives him enough sense of how things relate *because* he put time into ingesting it properly and giving it context ([23:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1427s)–[24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)). *(Vault inference:)* good capture can delay the point where you need a graph.
- **Relationship data looks like triples.** The example graph uses entities and typed links: a person works at a company, that company is endorsed by a third entity, and that entity is a competitor of a fourth ([23:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1408s)–[23:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1423s)). *(The names in that demo, Jordan, Acme, Postpilot and Cadently, are fictional.)* The starter template below records relationships in the same shape.
- **Design for how it will be used.** Decide how the captured knowledge will be looked up before deciding how to store it ([02:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=156s)–[02:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=164s)). See [[Design for Retrieval]].

## Perspectives from other sources

Six more sources deal with the same move: getting Claude to question you before it acts. Only the last one, Nate's marketing video, comes close to his knowledge-capture use, so read the rest as neighbouring uses, not verdicts on this skill.

### Ras Mic: don't write the skill first

From [[Ras Mic - How AI Agents and Claude Skills Work]]. [[Ras Mic]] was a guest on [[Greg Isenberg]]'s podcast. He works in OpenClaw rather than Claude Code, but the way he builds skills applies to [[Agent Skills]] in general.

- **Don't draft the skill first.** People spot a workflow and jump straight to creating a skill; he calls this the worst thing you can do ([08:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=520s), [08:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=526s)). A skill written up front, by you or by AI, has no record of what a successful run looks like ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)). The agent copies you closely, but only if it has something to copy ([11:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=701s)).
- **Walk it through by hand first.** Take the agent through the workflow one step at a time, correcting it as you go, the way you'd train a new hire ([08:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=537s), [09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s)).
- **Then distil.** He turned the workflow into a skill only after it had succeeded, more than once ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)). He asked the agent to review what it had just done and write the skill ([12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)). He doesn't handwrite skills, and a skill-creating skill is fine for this step ([12:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=747s), [12:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=750s)).
- **Greg's summary:** map the workflow, define right and wrong, iterate, then codify ([13:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=831s)–[14:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=842s)).
- **Keep improving it.** A finished skill will still fail where it has gaps ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s)). When it does:
  1. Ask the agent why it failed ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)).
  2. Have it fix the problem.
  3. Tell it to update the skill so the failure doesn't recur ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).

  Five rounds of this made his eight-source report skill dependable ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s), [22:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1354s)).
- **Don't install other people's skills.** Marketplace skills are an easy way to attack someone, and they don't carry your successful-run context. He reads them, or asks his AI what to learn from them ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)).
- → [[Build a Skill from a Successful Run]], [[Skill Improvement Loop]], [[Build vs Install Third-Party Skills]]

### Nate Herk: a one-line version for aligning on a task

From [[Nate Herk - 32 Tricks to Level Up Claude Code]].

- Plan mode often asks clarifying questions by itself. You can also tell Claude outright to keep using its AskUserQuestion tool until it is 95% confident it understands what you need and what it has to do ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s), [03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)). He says this saves three or four rounds of revisions ([03:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=233s)).
- It goes with starting in plan mode ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)) and with posing problems instead of giving orders ([03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s)).
- **How it differs from this note:** it aligns Claude on one task before building. It needs no skill and writes no brainstorm file.
- → [[Plan Before Executing]], [[Plan-First Workflow]]

### Chase AI: interview yourself to find workflows

From [[Chase AI - The Agentic OS Setup for Claude Code]].

- **Audit first.** Before building skills, work out what you actually do over and over ([04:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=281s)). He gives three ways to find candidates: explain a task you already know, have Claude mine your past sessions, or have Claude interview you ([13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s)).
- **The interview route** ([08:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=539s), [09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s)–[09:58](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=598s)):
  1. Talk freely to Claude about your daily and weekly work.
  2. Ask it to turn that into an interview and point out blind spots.
  3. Aim for as much context as possible on your work and the outcomes you want.
  4. Have it pull out specific tasks to turn into skills, and later into automations.
- **Treat it like onboarding.** Brief Claude as you would a new personal assistant you want to hand tasks to ([10:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=619s)). The skills that come out are workflows you can read and keep editing until the outputs are right ([10:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=640s)).
- **Same point as Ras Mic.** On the manual route, ideally you've already done the task by hand and confirmed it works, then you tell Claude to turn what you just did into a skill ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s), [07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s)).
- → [[Workflow Audit into Skills]]

### The Coding Sloth: Matt Pocock's grill-with-docs for requirements

From [[The Coding Sloth - 1000 Hours of Claude Code Lessons]].

- His favourite skills are [[Matt Pocock]]'s. He uses grill-with-docs (captioned "grow with doc") to refine his requirements ([06:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=364s), [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)).
- He installs skills, mostly found on skills.sh ([05:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=355s)). He warns against installing a hundred of them: they're opinionated, so stick to one group ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s), [08:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=502s)).
- **How it differs from this note:** grill-with-docs is aimed at plans and requirements in a code repo, not at capturing knowledge into a brainstorm file. What it writes is verified under *Beyond the source*.
- → [[Plan Before Executing]]

### AI LABS: design skills that ask before they build

From [[AI LABS - Claude Design Skills for Beautiful Sites]], working in [[Claude Design]].

- Three build skills question you before generating anything. emil-design-eng asks about the app first, as Claude Design does on its own ([02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s)). web-design-engineer works through your requirements with you until they're clear ([04:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=254s)). landing-page-design also asks first ([06:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=387s)).
- **How it differs from this note:** the questions scope one build rather than capture lasting knowledge. The Source note reads this as a general pattern: build skills benefit from an intake step.
- → [[Build a Distinctive Site with Design Skills]]

### Nate Herk: interviewing for marketing context

From [[Nate Herk - Claude as a One-Person Marketing Team]]. Of these sources, this is the closest to the note's own knowledge-capture use.

- **New topic: how you market your product.** While setting up a brand project, he suggests running Grill Me on your product and marketing so Claude understands how you think about marketing it ([11:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=665s)). It asks one question at a time and saves the interview as context for later ([11:13](https://www.youtube.com/watch?v=yCACmFTiCto&t=673s)).
- **Install route.** He calls his version basically a prompt in one big markdown file ([10:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=622s)) and installs it by dragging the file into the chat and asking Claude to install it in the project ([10:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=653s)). *(Vault note:)* the documented format is a folder containing `SKILL.md` (see Beyond the source), so check where Claude saved it and read it first.
- → [[Build a Brand-Aware Marketing Project]] (step 4)

## Where sources disagree

| Question | One side | Other side | What this note does |
|---|---|---|---|
| Write the skill before running it? | This note's original build (step 2) saves a pre-written starter `SKILL.md` before any interview has run | [[Ras Mic - How AI Agents and Claude Skills Work]]: writing a skill before a successful run is the worst move. Walk the agent through by hand, then have it write the skill ([08:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=526s), [11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s), [12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)). [[Chase AI - The Agentic OS Setup for Claude Code]] leans the same way ([07:26](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=446s)) | **Recommends the distil-first route:** run one interview by hand with the prompts below, then have Claude write `SKILL.md` from that session, using the starter as a checklist. The pre-written starter stays as a fallback |
| Install someone else's grilling skill? | Nate points people to his customised version in his Skool community ([20:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1243s)). [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] installs and recommends Matt Pocock's grill-with-docs ([06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)) | [[Ras Mic - How AI Agents and Claude Skills Work]] won't install others' skills. They are an attack route and lack your context, so read them and borrow the lessons ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s), [13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)) | Read any third-party version in full before installing. Treat it as reference material for your own |
| A skill, or a one-liner? | This note: a dedicated skill with a coverage checklist and an output file | [[Nate Herk - 32 Tricks to Level Up Claude Code]]: a single instruction to keep using AskUserQuestion until about 95% confident ([03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)) | They do different jobs. The one-liner aligns a single task; the skill captures knowledge that lasts. Both are listed under Variations |

## Prerequisites

- [[Claude Code]] with a project folder that acts as your brain. A Level 1 setup (a CLAUDE.md router plus context, projects and decisions folders) is enough. See [[Build a Level 1 Second Brain]].
- A decision on what you're willing to send to Anthropic, especially client data ([21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)).
- Optional input files for the topic, such as call or meeting transcripts and contracts ([21:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1275s)–[21:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1276s)).
- A list of the topics to capture, one entity per interview (client A, client B, business A) ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)).

## Steps

1. **Choose the first topic and its future questions.** Pick one entity or process, then write 3 to 5 questions you'll want the brain to answer about it later. You'll check these once the interview is done ([02:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=156s)).
2. **Create the skill.** Make the folder `.claude/skills/grill-me/` in the project and save the starter below as `SKILL.md`. To use it in every project, put it under your personal skills folder instead (paths verified under Beyond the source).
   - **Recommended: the distil-first route.** Don't save the starter yet. First run steps 5–8 once by hand, using *Prompt A* below instead of `/grill-me`, and correct Claude out loud whenever it goes wrong. Then use *Prompt B* in the same session so Claude writes `SKILL.md` from that run, with the starter as a checklist. This follows [[Ras Mic - How AI Agents and Claude Skills Work]] ([08:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=526s), [12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s)); see *Where sources disagree*. It is the same approach as [[Build a Skill from a Successful Run]].
3. **Create the output folder.** Add `brainstorms/` at the project root. The skill also creates it if it's missing.
4. **Route to it.** Add a line to CLAUDE.md (and AGENTS.md if you use other agents) saying what `brainstorms/` contains and how much to trust it (snippet below). Claude won't look in a folder it hasn't been told about ([05:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=300s)–[05:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=313s)). See [[CLAUDE.md as a Router]].
5. **Gather inputs.** Put transcripts, contracts and notes for the topic somewhere in the project so you can name their paths.
6. **Start the interview.** Type `/grill-me client A` or just say "grill me about client A" (more examples below). Name any files it should read first.
7. **Answer one question at a time.** Give real examples, names and numbers. Say `skip`, `don't know`, `pause` or `wrap up` whenever you need to. Paste or name extra files mid-interview when a question is better answered by a document.
8. **Review the brainstorm file.** Fix anything wrong, answer open questions you can, and confirm the summary.
9. **Promote the content, deliberately.** Use the promotion table (below) to move confirmed content into context files, the decision log, the wiki or the graph layer. You stay in control of what gets ingested ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
10. **Test.** In a fresh session, ask the questions from step 1. The brain should know where the data lives, where to look, and give an accurate answer ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s)–[28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s)).
11. **Repeat per entity.** Client B, business A, and so on ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)–[21:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1270s)).

## Starter files & prompts

### Folder layout

```text
your-brain/
├── CLAUDE.md                      # router: add a line for brainstorms/
├── AGENTS.md                      # optional, same routing for other agents
├── .claude/
│   └── skills/
│       └── grill-me/
│           └── SKILL.md           # the starter below
├── brainstorms/                   # raw interview output, one file per topic
│   ├── client-a.md
│   ├── client-b.md
│   └── business-a.md
├── context/                       # evergreen facts about you and the business
├── decisions.md                   # dated decision log
├── projects/
├── wikis/                         # Level 2+, optional, one folder per wiki
├── transcripts/                   # optional: original call and meeting transcripts
├── references/                    # optional: contracts, specs and other documents
└── knowledge-graph/               # Level 4, optional
```

### `.claude/skills/grill-me/SKILL.md` (original starter)

````markdown
---
name: grill-me
description: Relentless one-question-at-a-time interview that pulls everything the user knows about a single topic (a client, business, project, process, person or decision) out of their head and into brainstorms/<topic>.md. Use when the user says "grill me about X", "interview me about X", or wants to capture what they know about something for the second brain.
argument-hint: "[topic] [optional: files to read first]"
---

# Grill Me

Interview the user until everything they know about the topic below is written down.
You ask; the user answers. Do not give advice, plans or opinions during the interview.

Topic and inputs: $ARGUMENTS

If no topic was given, ask "What should I grill you about?" and wait.

## 1. Before the first question

1. Make a short kebab-case slug from the topic (for example `client-a`). The output file is
   `brainstorms/<slug>.md`. Create `brainstorms/` if it does not exist.
2. If the file already exists, read it and resume from its Open questions and unchecked
   Coverage items. Never re-ask something already answered.
3. Read every file the user named or attached (transcripts, contracts, notes, exports).
   Then follow the CLAUDE.md routing rules to read what the project already holds on this
   topic (context, projects, decisions, wiki, knowledge graph). Write what is already known
   under "Already on file" so you do not ask for it.
4. Tailor the Coverage checklist (section 3) to this topic and write the file skeleton
   (section 5) straight away.
5. In at most three lines, tell the user what you read, which areas you will cover, and that
   they can say "skip", "don't know", "pause" or "wrap up" at any time. Then ask question 1.

## 2. Interview rules

- One question per message. Never bundle questions or send a list of questions.
- Keep questions short and concrete. When it helps, give an example of the kind of answer you want.
- Do not ask what a file already answers. Read the file, then ask about what it leaves out:
  exceptions, reasons, history, what actually happens in practice.
- Push for specifics. When an answer is vague ("they're slow", "it went okay"), follow up once
  or twice for a name, number, date, amount, frequency or real example before moving on.
- Chase new threads. When an answer mentions a new person, company, product, tool, project or
  decision, ask at least one follow-up about it and add it to Entities.
- Ask about relationships explicitly: who works for or with whom, who decides, who pays, what
  depends on what, who competes with whom, what replaced what. Record each as a
  From / Relationship / To row.
- Ask why and when. For every decision or rule, capture the reason and the date or rough period.
- Capture the user's own words: nicknames, acronyms, internal names and synonyms go in Vocabulary.
- Sort evergreen from volatile. If something will be different next week (an open thread, this
  week's numbers), record where that live data lives and how to reach it, not the data itself.
- Accept "skip" and "don't know" immediately. Log them as Open questions and move on.
- When the user pastes or attaches something mid-interview, read it, say in one sentence what you
  took from it, update the file, and ask about what it does not cover.
- Never invent or assume an answer. If you infer something, turn it into a question to confirm.
- After roughly every five answers, save the file and show one progress line:
  "Covered: ... | Still open: ...".

## 3. Coverage checklist (adapt to the topic; delete what does not apply)

- [ ] Basics: what it is, one-sentence description, since when, current status
- [ ] People: who is involved, their roles, who decides, who to contact for what
- [ ] Relationships: links to other people, companies, products, projects and tools
- [ ] History: how it started, key events, what changed and why
- [ ] Decisions and rules: what has been decided, the reasons, dates, unwritten rules
- [ ] Goals and success: what good looks like, the numbers that matter
- [ ] How work happens: processes, cadence, handoffs, tools used
- [ ] Preferences and sensitivities: likes, dislikes, tone, things to never do
- [ ] Money and terms: pricing, contracts, renewals, obligations (if relevant)
- [ ] Problems and risks: what has gone wrong, what could, open issues
- [ ] Live sources: where the changing data lives and how to reach it
- [ ] Vocabulary: names, acronyms and synonyms the user uses

Tick an item only when it has specific answers, is confirmed not applicable, or its gaps are
logged as Open questions.

## 4. When to stop

Keep going until ALL of these are true:
1. Every Coverage item is ticked.
2. The last three answers added no new entity, relationship, decision or fact.
3. You have asked "What would someone get wrong about this if they only read this file?"
   and recorded the answer.
4. The user has read the Summary and confirmed it is accurate and complete.

Stop early only when the user says "wrap up" or "stop" (finalise the file with what you have
and list the gaps) or "pause" (save, set status to paused, note where to resume).

## 5. Output file: brainstorms/<slug>.md

```
---
type: brainstorm
topic: <Topic>
status: in-progress        # in-progress | paused | complete
started: YYYY-MM-DD
updated: YYYY-MM-DD
inputs: []                 # every file you read, as paths
---

# <Topic> brainstorm

## Summary
<5-10 sentences a new teammate could act on. Written last and confirmed by the user.>

## Coverage
<the tailored checklist, ticked as you go>

## Already on file
- <fact> (from <path>)

## Key facts
- <fact> (user, YYYY-MM-DD) or (from <path>)

## Entities
| Entity | Type | Notes |
|---|---|---|

## Relationships
| From | Relationship | To | Source |
|---|---|---|---|

## Decisions and rules
| When | Decision or rule | Why | Source |
|---|---|---|---|

## How work happens

## Preferences and sensitivities

## Problems and risks

## Live sources (reach, don't ingest)
| What changes | Where it lives | How to reach it |
|---|---|---|

## Vocabulary
| Term the user uses | Meaning | Also called |
|---|---|---|

## Open questions
- [ ] <question> (why it matters)

## Suggested promotions
| Content | Promote to | Reason |
|---|---|---|

## Interview log
1. Q: <question> | A: <one-line gist>
```

## 6. Hand-off

After the final save, reply with: the file path; counts of facts, entities, relationships and
open questions; and a filled "Suggested promotions" table (which content should go to context
files, the decision log, project files, the wiki or the knowledge graph).
Do not move, ingest or rewrite any other project file unless the user approves.
````

### CLAUDE.md routing snippet

```markdown
## Where things live
- `brainstorms/`: raw interview captures from the grill-me skill, one file per topic.
  Unreviewed source material. Prefer context/, decisions.md and projects/ when they disagree,
  and suggest promoting confirmed facts out of here.
- To capture what the user knows about a new client, project or process, use /grill-me.
```

### Example invocations

| You type | What should happen |
|---|---|
| `/grill-me client A` | New interview. Creates `brainstorms/client-a.md` and asks question 1 |
| `Grill me about business A` | Plain-language trigger, as in the video ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)). The skill's `description` makes Claude load it |
| `/grill-me client B. Read transcripts/2026-09-02-client-b-call.md and references/contracts/client-b-msa.md first` | Reads the files, notes what's already known, and asks only about gaps and nuance (feeding files: [21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s)) |
| `/grill-me how we onboard new clients` | Process capture: steps, owners, handoffs, exceptions |
| `/grill-me our Q3 priorities and why we chose them` | Decision capture, feeding the decision log |
| `Continue grilling me about client A` | Resumes from the file's open questions and unticked coverage |
| `wrap up` (mid-interview) | Finalises the file with what it has and lists the gaps |

### How brainstorm output feeds the brain

| Brainstorm section | Where it goes | Level / how | See |
|---|---|---|---|
| Summary, Key facts, Preferences | `context/` file or `projects/<client>/README.md` (the per-client folder the base router routes) | Level 1: plain markdown with a routing rule ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)) | [[Build a Level 1 Second Brain]] |
| Decisions and rules | Dated decision log (in the Level 1 example, CLAUDE.md can have Claude append new decisions with dates, [06:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=368s)) | Level 1 | [[Build a Level 1 Second Brain]] |
| Topic knowledge that spans many notes | Ingest the brainstorm file as a source into the wiki | Level 2 | [[Ingest Sources into an LLM Wiki]] |
| Entities and Relationships tables | Knowledge-graph layer, as entity plus typed-relationship records ([23:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1408s)–[23:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1423s)) | Level 4 | [[Build a Knowledge Graph Layer]] |
| Live sources | Routing and lookup-order entries only. Don't ingest the data itself ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)–[28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)) | Any level | [[Tiered Lookup Routing]] |
| Open questions | Stay in the brainstorm file. Re-run `/grill-me` later to resume | — | — |

### Distil-first route: vault starter prompts

Written for this vault, following the method in [[Ras Mic - How AI Agents and Claude Skills Work]] ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s), [12:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=737s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)). The wording is not his.

**Prompt A: hand-run interview** (in a fresh session, before any skill exists)

```text
I want everything I know about <topic> captured in brainstorms/<slug>.md.
Interview me. One question per message. Push for names, numbers, dates and real examples,
ask how the people, companies and projects involved relate to each other, and log anything
I skip as an open question. Read <files> first and don't ask about what they already answer.
Don't give advice and don't guess answers. Update the file every few answers.
Keep going until I say "wrap up".
```

While it runs, correct it the moment it does something you don't want, such as bundling questions, offering opinions or filling in an answer for you. Those corrections are what the skill has to learn.

**Prompt B: turn the run into the skill** (same session, once you're happy with the brainstorm file)

```text
Look back over this whole session: the questions you asked, every place I corrected you,
what made the useful answers useful, and the final shape of brainstorms/<slug>.md.
Write .claude/skills/grill-me/SKILL.md so that a fresh session runs this same interview.
Keep every rule that came from one of my corrections, and say which correction it came from.
Then check the draft against this list and tell me what's missing: <paste the Coverage
checklist and "When to stop" rules from the starter above>.
Show me the file before you save it.
```

**Prompt C: after an interview goes wrong**

```text
This interview went wrong: <what happened>. Tell me why you think it happened,
fix brainstorms/<slug>.md, then update .claude/skills/grill-me/SKILL.md so it
doesn't happen next time. Show me the diff to the skill.
```

### One-line alignment prompt (vault wording of Nate Herk's idea)

For a single build task, not knowledge capture ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)). Use it in plan mode.

```text
Before planning or building, use the AskUserQuestion tool to clear up anything unclear
about this task. Stop asking once you're roughly 95% sure of the goal and the steps.
Then list your assumptions and wait for my go-ahead.
```

### Workflow-discovery prompt (vault wording of Chase AI's idea)

Points the interview at your own recurring work instead of an entity ([09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s)).

```text
I want to find the recurring work I could turn into skills and, later, scheduled automations.
I'll start by talking through what a normal day and week look like for me.
Then interview me: dig into gaps and blind spots, and ask what a good result looks like for each task.
Finish with a table: task | how often | what the output is | proposed skill name | automate later? (yes / no / maybe)
```

## Done when

- [ ] `.claude/skills/grill-me/SKILL.md` exists and `/grill-me` shows up as a command in Claude Code.
- [ ] A trial interview asked **one question per message**, followed up on at least one vague answer, and asked about relationships.
- [ ] `brainstorms/<topic>.md` exists with a confirmed summary, entities, relationships, decisions, live sources and open questions, and lists the files it read.
- [ ] CLAUDE.md (and AGENTS.md, if used) routes to `brainstorms/`.
- [ ] You reviewed the file and promoted confirmed content, with approval, to context, decisions, wiki or graph.
- [ ] In a fresh session, the questions from step 1 get specific, accurate answers from the promoted files ([28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s)).
- [ ] You've made a deliberate call about client or sensitive data ([21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)).
- [ ] If you took the distil-first route, `SKILL.md` was written from a hand-run interview you were happy with, and it keeps the rules that came from your corrections.
- [ ] After any interview that went wrong, the fix was folded back into `SKILL.md` (per [[Ras Mic - How AI Agents and Claude Skills Work]], [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).

## Pitfalls

- **Skipping capture and jumping to a higher level.** A vector store or graph can't return nuance that was never written down. Check completeness first ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)).
- **Topics that are too broad.** "Grill me about my business" never finishes. Split it the way the video does: client A, client B, business A ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)).
- **Capturing volatile data.** Interview answers about this week's threads or numbers turn into noise and a monthly clean-up job ([27:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1653s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)). Record where that data lives instead.
- **Auto-ingesting the output.** Putting brainstorm files straight into the brain gives up the ingestion control Nate relies on and risks the too-much-context problem ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)–[26:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1585s)).
- **Forgetting privacy.** Detailed client interviews processed through Claude go to Anthropic ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s)).
- **Leaving brainstorm files unrouted.** If CLAUDE.md never mentions `brainstorms/` or the files they were promoted into, the agent won't look there ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=313s)).
- **Assuming this starter, Nate's version and Matt Pocock's original are the same skill.** Nate says he customised Matt's ([20:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1242s)) but doesn't show what he changed. Matt's published version is aimed at sharpening plans and designs (see Beyond the source).
- **Letting the model answer for you.** Interview output should record only what you said or what a named file says. Inferences go in as questions to confirm.
- **Writing the skill before any real run.** [[Ras Mic - How AI Agents and Claude Skills Work]] warns that a skill drafted up front has no example of success to copy ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)). Even a distilled skill will hit gaps, so fold each failure back in instead of abandoning it ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).
- **Installing a grilling skill without reading it.** Ras Mic calls downloaded skills an easy attack route ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)). [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] does install skills, but warns against piling up many opinionated ones ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)).
- **Using the one-liner for knowledge capture.** Nate's AskUserQuestion prompt is for aligning on a task before building ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)). *(Vault inference:)* it won't leave you a reviewed brainstorm file to promote into the brain.

## Variations

- **Slash-command only.** Add `disable-model-invocation: true` to the frontmatter so the skill runs only when you type `/grill-me`, and never because a conversation happens to mention interviewing (field verified below).
- **Personal skill.** Install it once in your user-level skills folder so every project can use it (path verified below).
- **Document-first grilling.** Give it a contract or transcript and tell it to ask *only* about what the document doesn't say (inputs: [21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s)–[21:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1276s)).
- **Graph-first grilling.** Stress the Entities and Relationships sections when the target is a knowledge-graph layer ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).
- **Weekly gap-filling.** After a weekly transcript ingest like Nate's ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)), run a short grill on anything the transcripts left unclear.
- **Team process owners.** For a team brain, one question he raises is how to make sure process owners keep their docs updated ([30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s)–[30:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1810s)), and he rates adoption and change management as a bigger problem than the tech ([30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)). *(Vault suggestion:)* a grill session with each owner is one way to seed those docs. Get your own brain working first ([30:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1826s)–[30:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1838s)).
- **Private data.** Run the same interview with an open-source or local model for client data you won't send to Anthropic ([21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- **Task alignment one-liner (Nate Herk).** For a single build task, skip the skill. Use the one-line alignment prompt above in plan mode, as in [[Nate Herk - 32 Tricks to Level Up Claude Code]] ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s), [03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)). Nothing is written to `brainstorms/`. → [[Plan Before Executing]]
- **Workflow discovery (Chase AI).** Interview yourself about your recurring work instead of an entity, using the workflow-discovery prompt above. The result is a list of tasks that could become skills and then automations, as in [[Chase AI - The Agentic OS Setup for Claude Code]] ([09:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=571s), [13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s)). → [[Workflow Audit into Skills]]
- **Requirements grilling in a code repo (The Coding Sloth).** For requirements rather than knowledge capture, use Matt Pocock's grill-with-docs as [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] does ([06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)). Read it before installing.
- **Recursive hardening (Ras Mic).** After each interview that goes wrong, run Prompt C so the skill learns the fix ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)). → [[Skill Improvement Loop]]

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: the skill ([20:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1208s)–[21:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1279s)), the privacy aside ([21:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1282s)–[22:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1338s)), capture vs retrieval ([22:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1340s)–[22:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1367s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: don't write skills up front, and distil them from a successful run ([08:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=520s)–[14:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=842s)); don't install other people's skills ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s)); improve skills recursively ([20:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1242s)–[23:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1400s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: have Claude ask questions with AskUserQuestion until it is 95% confident ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)–[03:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=236s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: the workflow audit and its interview route ([04:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=281s)–[10:43](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=643s)), and his recap ([13:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=792s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: grill-with-docs for requirements ([06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)), and advice on how many skills to install ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]: design build skills ask questions before generating ([02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s), [04:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=254s), [06:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=387s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]]: installing Grill Me by drag-and-drop and running it on your product and marketing ([10:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=618s)–[11:17](https://www.youtube.com/watch?v=yCACmFTiCto&t=677s)).
- *Transcript note:* the auto-captions render the community as "school community". It is Skool.
- *Transcript notes (other sources):* The Coding Sloth's captions render grill-with-docs as "grow with doc skill". Ras Mic's captions render SKILL.md as "scale out MD file" and OpenClaw as "Open Cloud".

## Beyond the source

Not from any of the videos. Each item was checked at the linked page on 2026-09-15.

- **Matt Pocock's published skill.** Matt Pocock's public `mattpocock/skills` repo includes a user-invoked `grill-me` skill in its productivity section. Its frontmatter sets `disable-model-invocation: true`, and its short body hands off to a sibling, model-invoked `grilling` skill that holds the method. Source: [mattpocock/skills: grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me), [mattpocock/skills: grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling).
- **How Matt's method differs.** The `grilling` skill is aimed at stress-testing a plan, decision or idea, mapped as a tree of decisions. It works in rounds: each round it asks every question that can be answered now as a numbered batch, each with a recommended answer, then recomputes what can be asked next. It looks up facts from the environment itself (via a sub-agent) rather than asking the user, and the session ends when no open branches remain and the user confirms a shared understanding. That is decision-oriented and batches its questions, whereas the use in the video is knowledge capture into a brainstorm file, and the starter above deliberately asks one question per message. The README lists `/grill-me` as the option for non-code uses. The grill-me docs also say one line in your global CLAUDE.md switches grilling back to one question at a time ([docs/productivity/grill-me.md](https://github.com/mattpocock/skills/blob/main/docs/productivity/grill-me.md)). The same repo also has a `grill-with-docs` engineering skill that pairs grilling with building a domain model. Source: [mattpocock/skills (README)](https://github.com/mattpocock/skills), [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md). *(Not reproduced here. Read it at the link.)*
- **Installing Matt's skills.** They are listed as `mattpocock-skills` in Anthropic's official plugin marketplace. In Claude Code, which this build targets, run `/plugin install mattpocock-skills@claude-plugins-official` inside a session, or `claude plugin install mattpocock-skills@claude-plugins-official` from the shell. The README spells the shell command `claude plugins install` (plural), but the Claude Code docs only document the singular `claude plugin install`. For Codex and other agents, the README gives `npx skills@latest add mattpocock/skills`. Source: [mattpocock/skills](https://github.com/mattpocock/skills), [official marketplace catalog](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json), [Claude Code docs: Discover plugins](https://code.claude.com/docs/en/discover-plugins).
- **Skill locations.** Project skills live at `.claude/skills/<skill-name>/SKILL.md` (commit them to share with a team). Personal skills live at `~/.claude/skills/<skill-name>/SKILL.md` and work in every project. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **Frontmatter and arguments.** `description` is what Claude uses to decide when to load a skill automatically. `name` defaults to the folder name. `disable-model-invocation: true` limits a skill to `/skill-name`. `argument-hint` shows during autocomplete. `$ARGUMENTS` is replaced by whatever you type after the command. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **Why this is a skill rather than a CLAUDE.md rule.** Anthropic's docs say CLAUDE.md should hold facts needed in every session, and multi-step procedures belong in a skill, which loads only when invoked or relevant. Source: [Claude Code docs: How Claude remembers your project](https://code.claude.com/docs/en/memory).
- **AskUserQuestion is a structured, multiple-choice tool.** Claude Code's tools reference lists it as a built-in tool for gathering requirements or clearing up ambiguity. It needs no permission. So Nate's one-liner ([03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)) produces multiple-choice questions, whereas this note's starter asks open questions one at a time. The open format suits knowledge capture; multiple choice suits quick task alignment. Source: [Claude Code docs: Tools reference](https://code.claude.com/docs/en/tools-reference).
- **What grill-with-docs writes.** Its docs describe:
  - **Scope:** planning in a single session inside an existing repo.
  - **Glossary:** agreed terms go into a `CONTEXT.md` glossary as they are settled.
  - **Decisions:** only hard-to-reverse decisions become ADRs under `docs/adr/`.
  - **Format:** questions come in rounds.
  - **Alternative:** the docs point to grill-me when you aren't working in a repo.

  So it covers the Coding Sloth's requirements use, not brainstorm capture. Source: [mattpocock/skills: grill-with-docs docs](https://github.com/mattpocock/skills/blob/main/docs/engineering/grill-with-docs.md). More detail on [[Matt Pocock]].

## Related

- Concepts: [[Knowledge Graphs]] · [[LLM Wiki]] · [[Context vs Connections]] · [[Design for Retrieval]] · [[Second Brain Levels]] · [[CLAUDE.md as a Router]] · [[Plan Before Executing]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]]
- Techniques: [[Second Brain Pain-Point Audit]] · [[Build a Knowledge Graph Layer]] · [[Ingest Sources into an LLM Wiki]] · [[Build a Level 1 Second Brain]] · [[Tiered Lookup Routing]] · [[Build a Skill from a Successful Run]] · [[Workflow Audit into Skills]] · [[Skill Improvement Loop]] · [[Plan-First Workflow]] · [[Build a Brand-Aware Marketing Project]]
- People & tools: [[Matt Pocock]] · [[Nate Herk]] · [[Ras Mic]] · [[Greg Isenberg]] · [[Chase AI]] · [[The Coding Sloth]] · [[Claude Code]]
- [[Home]]
