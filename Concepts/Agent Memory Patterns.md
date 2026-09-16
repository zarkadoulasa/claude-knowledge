---
type: concept
aliases: ["Agent Memory", "Memory Approaches", "Skill Learning Journal"]
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]"]
tags: [topic/memory, topic/agents, topic/claude-code, topic/cowork, topic/managed-agents, topic/skills, topic/loops, topic/context, topic/portability]
---

# Agent Memory Patterns

## In one sentence

An agent only "remembers" what gets written to a file or store and read back later. The sources' approaches differ in who writes that memory, where it lives, and how much of it loads every session.

## How it works

### The shared loop: read before, write after

- **The loop.** [[Anthropic - What Is Claude Managed Agents]] shows it most clearly. A weekly pricing agent checks last week's findings before it starts ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s)) and stores what changed when it finishes ([02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)).
- **No loop.** Without that loop you get what [[AI LABS - Types of Claude Loops Explained]] calls a stateless loop. The Ralph loop kept no memory; it reran the task until the task was done ([02:08](https://www.youtube.com/watch?v=8wsM0euQOvc&t=128s)).
- **Fresh sessions forget.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] notes that each desktop scheduled task runs as its own session, with no memory of earlier runs ([12:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=751s)).

### The patterns at a glance

| Pattern | Who writes it | Where it lives | What gets read, and when | Source |
|---|---|---|---|---|
| Claude Code auto memory | Claude, on its own once the feature is on ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)) | A memory file Claude Code maintains (location under Beyond the source) | Not covered in the video | [[Nate Herk - Every Level of a Claude Second Brain]] |
| Instruction-maintained `memory.md` | Claude, because global instructions tell it to append or update entries ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)) | An About Me folder in the Cowork workspace, plus one memory file per project ([35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s)) | The whole file, at the start of every session ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)) | [[Simon Pittman - Set Up Claude Cowork]] |
| CLAUDE.md as a lessons file | Claude, when you ask it to log patterns, gotchas and conventions ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)) | CLAUDE.md | The whole file, in every conversation ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s)) | [[Nate Herk - 32 Tricks to Level Up Claude Code]]; [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)) |
| Per-skill `learning.md` journal | A skill-improver agent, every round ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)) | Inside the skill's own folder ([06:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=408s)) | Past failures inform later runs of the skill ([05:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=327s)) | [[AI LABS - Types of Claude Loops Explained]] |
| Corrections pushed into skills or instructions | Claude or the agent, when you tell it to after a fix ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)) | The skill, CLAUDE.md, or Cowork memory or instructions ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)) | A skill's name and description are always in context; the full skill loads when needed ([03:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=212s)) | [[Nate Herk - 32 Tricks to Level Up Claude Code]], [[Simon Pittman - Set Up Claude Cowork]], [[Ras Mic - How AI Agents and Claude Skills Work]] |
| Managed Agents memory store | The agent, after each run ([02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)) | A memory store the agent reads and writes ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)) | Last run's findings or past incidents, before work starts ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s)) | [[Anthropic - What Is Claude Managed Agents]] |
| Always-on synced memory | A background system that keeps syncing and refreshing memories ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)) | [[GBrain]] | Not covered in the video | [[Nate Herk - Every Level of a Claude Second Brain]] |
| Hot cache file (`hot.md`) | The wiki agent, keeping the most recent thing he gave it or discussed ([14:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=884s)) | Inside his Herk Brain wiki vault ([14:40](https://www.youtube.com/watch?v=sboNwYmH3AY&t=880s)) | Only when another project needs the wiki; that route lists it ahead of the index and domain sub-index ([14:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=843s), [14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s)) | [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] |
| Skills as procedural memory | Claude, when you turn a correction into a skill or routing update ([05:22](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=322s)) | SKILL.md instructions, a reference file or an explicit rule, depending on the failure ([05:45](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=345s)) | Name and description at startup; SKILL.md when a prompt matches; references and scripts only when needed ([03:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=209s), [03:35](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=215s), [03:38](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=218s)) | [[Nate Herk - Build Skills Instead of Agents]] |
| Journal layer | The agent, when a chat starts with "journal": the whole conversation becomes a dated, indexed, logged entry ([21:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1315s), [22:15](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1335s)) | `journal/` in the vault, with its own index ([22:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1325s)) | Past entries, with the wiki and CRM, before each new journal reply ([22:54](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1374s)) | [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] |

### Pattern details

**1. Claude Code auto memory.**
- [[Nate Herk - Every Level of a Claude Second Brain]] explains that once auto memory is on, Claude writes and updates this memory itself ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)).
- Because it belongs to Claude Code, other agents such as Codex have to be told where it is ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)).
- None of the other videos here mention it. The full treatment is in [[Claude Code Auto Memory]].

**2. An instruction-maintained `memory.md`.** [[Simon Pittman - Set Up Claude Cowork]] builds memory from an ordinary file plus rules.
- **The file.** An About Me folder holds a memory file where Claude logs its conversations ([13:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=781s)).
- **The write rule.** Claude adds new entries at the bottom, or updates an entry the new information relates to ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)). The point is that it never loses track of where projects stand ([15:09](https://www.youtube.com/watch?v=pl90LATQlHI&t=909s)).
- **The read rule.** The global instructions must reference the file ([15:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=918s)), and the required reading for every session was moved to the top, with his go-ahead ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)).
- **The shape.** The generated file had sections for a session log, active projects, key decisions and preferences ([17:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1069s)).
- **Per project.** A `projects/` folder gives each project its own CLAUDE.md and memory ([35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s), [35:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=2155s)).
- **Unprompted writes.** Claude also updates memory without being asked in that prompt, for example while triaging his overdue Notion tasks ([31:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1911s)).

Build steps are in [[Set Up Claude Cowork]].

**3. CLAUDE.md as a lessons file.**
- **Log what Claude learns.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] has Claude write new patterns, gotchas and conventions into CLAUDE.md ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)) so it stops repeating mistakes ([06:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=407s)).
- **Watch the size.** The file loads into every conversation ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s)). He caps it at 150–200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)) and routes detail out to other files ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)). See [[Keep CLAUDE.md Lean]].
- **Permanent vs short-term memory.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] calls CLAUDE.md Claude's "permanent memory" ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)) and the context window its short-term memory ([13:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=790s)).
- **Useful but optional.** He uses the file to counter the models' bad habits ([04:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=254s)), but says it isn't make-or-break and skills can do as well or better ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s), [05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s)).

**4. A per-skill `learning.md` journal.** In [[AI LABS - Types of Claude Loops Explained]], a learning loop improves a reusable skill instead of just finishing a task ([05:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=303s)).
- **The loop.** A skill-loop command keeps calling an improver agent ([05:49](https://www.youtube.com/watch?v=8wsM0euQOvc&t=349s)). The agent runs the task both with and without the skill ([06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s)).
- **The journal.** They call `learning.md` the most important part; it lives inside the skill ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s), [06:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=408s)). It records each attempt, the results with and without the skill, and the lessons from every round ([06:57](https://www.youtube.com/watch?v=8wsM0euQOvc&t=417s), [07:01](https://www.youtube.com/watch?v=8wsM0euQOvc&t=421s)).
- **The payoff.** Later runs of the skill can steer clear of past failures ([05:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=327s)).

Build steps are in [[Skill Improvement Loop]].

**5. Corrections pushed into skills or instructions.** Here the fix becomes a rule rather than a record.
- **Nate Herk.** In [[Nate Herk - 32 Tricks to Level Up Claude Code]], when pushback gets a better result, he tells Claude to update the skill or CLAUDE.md ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
- **Simon Pittman.** In [[Simon Pittman - Set Up Claude Cowork]], he tells Claude to always create email drafts from now on ([26:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=1582s)). He also asks it to update its memory or instructions so the change sticks ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)).
- **Ras Mic.** In [[Ras Mic - How AI Agents and Claude Skills Work]], he hands the failure back to the agent ([21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s)). Once the task works, he has the agent update the skill ([22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)).
  - He notes that OpenClaw has a memory layer, but the agent still needs proper context ([13:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=796s)).
  - He builds skills from successful runs ([13:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=811s)). See [[Build a Skill from a Successful Run]].

**6. Managed Agents memory stores.** Both demos are from [[Anthropic - What Is Claude Managed Agents]].
- **Weekly deltas.** With a memory store, the pricing agent's weekly report shows what changed rather than repeating the same figures ([02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s)). It still searches live pricing pages on every run ([01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s)).
- **Past incidents.** An incident coordinator checks the store for past incidents ([03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s)). It matches a DNS issue caused by a misconfigured TTL ([03:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=197s)), so the next similar alert starts with that context ([03:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=201s)).

See [[Claude Managed Agents]] and [[Build an Event-Triggered Managed Agent]].

**7. Always-on synced memory.** [[Nate Herk - Every Level of a Claude Second Brain]] describes GBrain as the lower levels of his second brain plus constant syncing and memory refresh ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)). He holds back because too much context can do more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)). See [[Always-On Brain OS]].

**8. A hot cache in front of the wiki.** [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] keeps a `hot.md` in his personal Herk Brain wiki: a short cache (about 500 words or characters; he isn't sure which) of the latest thing he gave the agent or discussed with it ([14:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=884s)). For his executive assistant it can save crawling wiki pages; his YouTube-transcript wiki doesn't need one ([14:55](https://www.youtube.com/watch?v=sboNwYmH3AY&t=895s)). *Vault reading:* it's a recency layer, so give it a size cap and overwrite it rather than append, or it turns into the bloated always-read file other sources warn about.

**9. Skills as procedural memory.** [[Nate Herk - Build Skills Instead of Agents]] says skills aren't recordings of past chats; they hold the procedural knowledge one job needs ([05:40](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=340s)). Correct Claude and then close the chat, and that lesson is probably lost ([04:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=297s)). This sharpens pattern 5 by sending each fix to a specific place (table above). See [[Skill Improvement Loop]] and [[Audit Skill Descriptions and Triggers]].

**10. A journal layer the agent reads back.** [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] saves each journal chat in full as a dated file, adds it to a journal index and logs a summary ([22:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1322s), [22:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1344s)). Before replying to a new entry, the agent reads the indexes and looks for relevant prior notes ([27:04](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1624s)). His slides also promise that the agent will spot struggles that recur across entries and factor them into replies ([05:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=321s)), but that was never built or shown; his demo had no earlier entries to draw on ([27:13](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1633s)). See [[Add a Journal and Personal CRM to a Second Brain]].

## When to use it — and when not to

### Control vs automation

From most human control to least:

1. **You curate.** Nate Herk works through the material with Claude before anything is ingested ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
2. **You tell Claude what to write.** Examples are Simon's write rules ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)), Nate's lesson logging ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)) and the correction loops above.
3. **The agent decides.** Examples are auto memory ([10:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=650s)), the improver's `learning.md` ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)) and memory stores ([02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)). The improver's test sessions run in the background without asking permission ([06:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=380s)). The video shows no human reviewing the lessons.
4. **A background system writes continuously**, as GBrain does ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)).

*Vault synthesis, not a claim from the videos:* each step down saves effort but lets more unreviewed content into what the agent will read later.

### Portability

- **Plain files move with the folder.** That covers `memory.md`, CLAUDE.md and `learning.md`. Auto memory, by contrast, is tied to Claude Code ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s)), so other agents need a route to it ([11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)). See [[Tool-Agnostic Context Files]].
- **One instruction file for two agent families.** Coding Sloth notes you can import AGENTS.md inside CLAUDE.md, so both read the same file without a symlink ([03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)).
- **Hosted stores.** The Managed Agents video doesn't say where a store lives or how to move it. Per the docs under Beyond the source, it is hosted on the platform rather than kept in your repo, so portability depends on exporting it.

### Noise and context cost

- **Nate Herk's caution.** In [[Nate Herk - Every Level of a Claude Second Brain]], fast-changing data like Slack threads and emails becomes noise you have to prune every month ([27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s)).
  - Keep only what will still be useful a year from now ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)).
  - For everything else, give the agent access rather than copies ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)).
  - See [[Context vs Connections]].
- **Always-loaded files cost tokens on every run.** Ras Mic's example is a 1,000-line CLAUDE.md, which is roughly 7,000 tokens each run ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s)). He says most of it should be a skill ([04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s)).
- **Simon's file has no pruning rule.** His `memory.md` holds a session log and project status ([17:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1069s)) and is read every session ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)). The video gives no rule for pruning it, so, by the vault's reading, it risks collecting the volatile state the one-year test excludes.
- **A middle path.** The pricing agent fetches raw data live ([01:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=114s)) and stores only the changes ([02:25](https://www.youtube.com/watch?v=NLWiIj47IdI&t=145s)).

## Perspectives from sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: auto memory comes in at Level 2 and always-on memory at Level 5, with a warning against too much context ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s), [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: log lessons and corrections into CLAUDE.md, but keep it to 150–200 lines ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).
- [[Simon Pittman - Set Up Claude Cowork]]: global instructions make Claude read and update a `memory.md`, and each project gets its own memory ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s), [35:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=2155s)).
- [[AI LABS - Types of Claude Loops Explained]]: a learning journal lives inside the skill ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)). Separately, a CLAUDE.md rule has the agent save every working version, so an unattended run can roll back instead of undoing changes from memory ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s), [03:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=226s)).
- [[Anthropic - What Is Claude Managed Agents]]: memory stores follow a read-before, write-after routine, for both recurring and alert-triggered agents ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s), [03:12](https://www.youtube.com/watch?v=NLWiIj47IdI&t=192s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: CLAUDE.md is permanent memory and the context window is short-term memory ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s), [13:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=790s)). Some of his footage is about a month old ([00:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=13s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: keep always-on context minimal and put lessons into skills ([20:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1225s), [22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s)). He allows that new memory research could change this, but for now he says less is more ([28:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1709s)).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]: a small `hot.md` recency cache in front of the wiki (pattern 8).
- [[Nate Herk - Build Skills Instead of Agents]]: skills as procedural memory, with each fix in its own place (pattern 9).
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]: a journal the agent writes in full and reads back (pattern 10).

## Where sources disagree

- **Is CLAUDE.md memory?**
  - Coding Sloth ([03:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=198s)) and Nate Herk's tips video ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)) treat it as memory.
  - Nate Herk's second-brain video routes to a separate memory file instead ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). Simon keeps `memory.md` apart from his instructions ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s)).
  - The Claude Code docs keep the two apart (see Beyond the source).
- **Do you need CLAUDE.md at all?**
  - Ras Mic says about 95% of people don't ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)) and calls these files a farce ([32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).
  - Nate Herk and Simon build their memory setups around them ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s), [08:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=531s)).
  - Coding Sloth finds the file useful but optional ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s)).
- **Load memory every time, or only on demand?**
  - Simon has Claude read its memory at the start of every session ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)).
  - Nate Herk routes detail out of CLAUDE.md ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s)).
  - Ras Mic prefers skills, which load in full only when needed ([03:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=212s)).
  - Nate Herk's April wiki video is on demand with a shortcut. The consuming project is told not to read the wiki unless the task needs it, and its route lists a small hot cache ahead of the index ([14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s), [14:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=843s)).
- **Who writes the memory?**
  - In the loops and Managed Agents videos, the agent writes on every round or run ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s), [02:21](https://www.youtube.com/watch?v=NLWiIj47IdI&t=141s)).
  - Nate Herk keeps a human in control of what goes in ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)).
- **Keep whole conversations, or only the lesson?**
  - Matt Wolfe saves the entire journal conversation to the vault ([22:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1322s)).
  - Nate Herk's skills video says skills aren't recordings of conversations; they keep only the procedure ([05:35](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=335s)). His second-brain filter keeps only what will still be useful in a year ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)).
  - *Vault reading:* they're doing different jobs. A journal is reflective memory about you, where the raw entry is the point. A skill records how a job gets done, where transcripts are noise.

## Beyond the source

*Not from the videos. Checked 2026-09-15 at the links given.*

- **Claude Code keeps instructions and memory separate.** <https://code.claude.com/docs/en/memory>
  - **Who writes what.** You write CLAUDE.md, which holds rules. Claude writes auto memory, which holds learnings and corrections.
  - **Which request goes where.** "Remember this" goes to auto memory. "Add this to CLAUDE.md" makes it a standing instruction.
  - **When CLAUDE.md is the right place.** The docs suggest adding to it when Claude makes the same mistake twice, which fits Nate Herk's correction loop. Multi-step procedures belong in skills.
- **CLAUDE.md size and loading.** <https://code.claude.com/docs/en/memory>
  - **Size.** Keep each file under 200 lines. Files pulled in with `@imports` still load at launch, so splitting a file doesn't save context.
  - **Delivery.** CLAUDE.md is delivered as a user message after the system prompt. Nate Herk's "basically the system prompt" ([06:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=416s)) is an analogy for its every-session cost, not how it's actually loaded. Claude isn't guaranteed to follow it. For steps that must always happen, such as the loops video's save-every-working-version rule, the docs point to hooks instead.
  - **AGENTS.md.** Claude Code doesn't read AGENTS.md. The documented fix is an `@AGENTS.md` line in CLAUDE.md, or a symlink, which confirms Coding Sloth's workaround.
- **Auto memory lives outside the repo and trims itself.** It is stored at `~/.claude/projects/<project>/memory/` and is machine-local, so it isn't shared across machines or cloud environments. Only the first 200 lines or 25KB of the `MEMORY.md` index load at startup. Near that limit, Claude Code prompts Claude to merge or drop stale entries. Subagents can keep their own memory through a `memory` field. <https://code.claude.com/docs/en/memory>, <https://code.claude.com/docs/en/sub-agents>
- **Managed Agents memory stores.** <https://platform.claude.com/docs/en/managed-agents/memory>
  - **Structure.** A store is a workspace-scoped set of text documents hosted on the platform, not files in your repo. Self-hosted sandboxes get a synced local copy. It is mounted under `/mnt/memory/` and read and written with normal file tools. Up to 8 stores can be attached when a session is created.
  - **Read-before instruction.** A per-session `instructions` field can tell the agent to check the store before any task. That is the docs' own example, and it matches the video's read-before habit.
  - **Access.** Access defaults to `read_write`. The docs warn that prompt injection can plant content that later sessions will trust, so use `read_only` for reference material.
  - **Limits.** Each memory is capped at 100 kB and each store at 10,000 memories. The docs recommend many small files.
  - **Versioning and cleanup.** Every change creates an immutable version. Past versions may be deleted after 30 days, though a live memory's recent versions are always kept. Memories can be exported through the API or Console. A "dreaming" session can consolidate a store into a new one.
- **Cowork has built-in memory that Simon doesn't mention.**
  - **Cloud only.** It is shared with chat only when Cowork runs in the cloud, not in local sessions. You manage it in Settings > Memory. <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
  - **Per project.** Cowork projects keep memory scoped to the project. <https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork>
  - *My inference:* in a local session like Simon's, an instruction-maintained file is how you get memory that carries across sessions.
- **GBrain specifics** are verified in [[Always-On Brain OS]]. <https://github.com/garrytan/gbrain>
- **Quick chooser.** *My synthesis of the above, not advice from any one video.*

| Your situation | Start with |
|---|---|
| Solo in Claude Code and want low effort | Auto memory, reviewed now and then with `/memory` |
| Local Cowork, or several agents sharing one folder | An instruction-maintained `memory.md` with dated entries and a periodic pruning pass that applies the one-year test |
| You keep giving the same correction | Make it a rule in the skill or CLAUDE.md, not a memory |
| Improving one reusable skill | A `learning.md` inside the skill, with lessons reviewed before they're kept |
| A recurring or alert-triggered hosted agent | A Managed Agents store plus a read-before, write-after instruction; `read_only` for reference stores |
| Several agents sharing one continuously refreshed brain | [[Always-On Brain OS]], weighing Nate Herk's warning about too much context |

## Related

- [[Claude Code Auto Memory]], [[Always-On Brain OS]], [[Context vs Connections]]
- [[Skill Improvement Loop]], [[Build a Skill from a Successful Run]], [[Agent Skills]]
- [[Keep CLAUDE.md Lean]], [[CLAUDE.md as a Router]], [[Context Window Management]]
- [[Set Up Claude Cowork]], [[Build an Event-Triggered Managed Agent]], [[Loop Engineering]], [[Tool-Agnostic Context Files]]
- Tools: [[Claude Code]], [[Claude Cowork]], [[Claude Managed Agents]], [[GBrain]]
- [[Add a Journal and Personal CRM to a Second Brain]], [[Bootstrap an LLM Wiki from the Karpathy Gist]], [[Audit Skill Descriptions and Triggers]]
- People: [[Nate Herk]], [[Simon Pittman]], [[AI LABS]], [[The Coding Sloth]], [[Ras Mic]], [[Matt Wolfe]]
- [[Home]]
