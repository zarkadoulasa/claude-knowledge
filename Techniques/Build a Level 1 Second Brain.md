---
type: technique
goal: Set up a plain-markdown second brain where CLAUDE.md acts as a router, so Claude knows who you are, how you work and which folder to open without being told
difficulty: beginner
time_to_build: 1-3 hours (estimate, not from the video)
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]", "[[Obsidian]]", "[[Claude Cowork]]"]
tags: [topic/second-brain, topic/claude-code, topic/retrieval, topic/context, topic/cowork]
---

# Build a Level 1 Second Brain

## Goal

Build the first level of [[Nate Herk]]'s five-level model ([[Second Brain Levels]]). You need one CLAUDE.md that says who you are, how you work and where things live, plus a few folders: background context, a decision log and projects. At Level 1, that file and a few folders are the whole second brain ([05:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=347s)).

It works when you no longer have to re-explain things: you ask, and Claude knows where to look and why ([05:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=316s)).

## Use when

- You're starting from scratch. Level 1 is where everyone starts ([04:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=262s)).
- You keep re-explaining your setup, and you mostly look things up by exact words or file names ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s)).
- Claude asks you for background you know is already in the project folder. That usually means it was never told where to look ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)).
- Don't build higher than you need. Pick the lowest level that fixes your problem ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)). If nothing is causing pain, there's no reason to build a more complex system ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).

## How Level 1 works (from the video)

- **The question Level 1 answers:** can you find a file or a fact by searching for an exact word or name? ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s))
- **CLAUDE.md loads every session.** For that project it acts almost like a system prompt ([04:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=272s)). The example file notes that it loads automatically whenever Claude Code opens in that folder ([05:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=341s)). Codex users start with AGENTS.md instead ([04:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=263s)).
- **CLAUDE.md is a router** ([[CLAUDE.md as a Router]], [04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)). Besides the role and what matters, it holds routing rules. His examples: information about him personally lives in one folder ([04:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=285s)), and the quarter-one priorities live in another ([04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s)).
- **Claude won't search everything on its own.** You wouldn't want it to, because that wastes time and tokens ([05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)). If Claude doesn't know something exists somewhere, it probably won't find it ([05:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=311s)).
- **Design for retrieval** ([[Design for Retrieval]]). Work backwards from the questions you'll ask ([02:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=150s)): how data will be looked up should decide how it's stored ([02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)). His analogy: you know the shape of the basketball hoop, so you wouldn't make a square ball ([02:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=166s)).
- **The test:** can your agent find it again, and can you? If either answer is no, your routing or folder setup probably needs work ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)).
- **Known limits.** As the router grows it gets messy ([05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s)) and its instructions start to feel ignored ([05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)). Depending on how you route, lookup is mostly by exact words ([05:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=327s)).
- **There's no standard layout.** Apart from common pieces like a context folder and CLAUDE.md, no structure has been proven best ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)). Don't assume his setup, or any creator's, is the only right one ([06:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=415s)). What matters is that routing exists and makes sense to both you and the AI ([07:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=423s)).

## The example layout shown in the video

From the Level 1 folder of his example project, shown at [05:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=334s):

| Piece | What it holds | Where |
|---|---|---|
| `CLAUDE.md` | Who you are, how you work, where things live ([05:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=344s)). A short "where things live" section comes after the basics ([05:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=355s)) | Project root |
| `context/` | Background about you and how you work that is always true. The router tells Claude to read it first ([05:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=358s)) | Folder |
| Files in `context/` | An about-me file you can keep expanding ([06:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=364s)), a stack file, and a second file captioned "conversations", possibly "conventions" *(unclear in captions)* ([06:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=366s)). Their contents aren't opened on screen | Folder contents |
| Decisions | A decision log ([06:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=368s)). You can have CLAUDE.md tell Claude to always append new decisions with dates whenever you make a big change to a project, your business or your life ([06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)). The captions don't say whether it's one file or a folder | Root |
| `projects/` | One markdown file or sub-folder per ongoing project or client, organised however you like ([06:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=379s)) | Folder |
| Date grouping (optional) | Projects can also be grouped by date, for example a May folder and a June folder ([06:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=391s)) | Inside `projects/` |

**The drill-down test in his real project, Herk2** ([07:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=431s)). Suppose he can't ask the AI and needs to find an HTML slide deck by hand. It's easy because he knows his top-level folders ([07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s)). He opens projects, then the YouTube-videos project ([07:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=447s)), then the dated folder for that video, where the deck sits. His agent can find it the same way, because the structure is logical and the routing rules exist ([07:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=464s)).

## Prerequisites

- [[Claude Code]] installed.
- One dedicated folder that you always open Claude Code in.
- Time to write honestly about yourself and your work. He says the bigger problem is sometimes getting what's in your head into the files, not the AI's retrieval ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).
- A privacy decision. Whatever Claude processes goes to Anthropic ([21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s)). He's fine with that for his own business data. If you can't send something, such as client data, consider open-source models for that part ([21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- Optional: [[Obsidian]]. It only displays your markdown files visually ([09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)), and he rarely opens it ([10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).

## Steps

1. **Write down your questions first.** He says to work backwards from how you'll use the data ([02:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=150s)). So list 5–10 questions you'll really ask, such as "what are my priorities this quarter?" or "why did we drop that tool?". Every question should have an obvious file where the answer lives. *(The list is a suggested exercise based on his principle.)*
2. **Create the folder skeleton** (tree below) and open Claude Code in that folder. The example CLAUDE.md notes that it loads automatically whenever Claude Code opens in that folder ([05:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=341s)).
3. **Fill in `context/`** with background that is always true: an about-me file, a stack file and a third file ([06:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=364s)). Include the details you usually end up re-explaining. Before blaming the AI for a bad answer, check that your files really hold the nuance in your head ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)). A shortcut is to have Claude interview you. His [[Grill Me Interview Skill]] (originally from [[Matt Pocock]], [20:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1240s)) questions him relentlessly on a topic and saves the results to a file ([20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s)). He demos it for gathering knowledge-graph data; using it to fill about-me is an adaptation.
4. **Create the decision log**, and add a CLAUDE.md rule telling Claude to append dated entries whenever you make a big change ([06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)).
5. **Create `projects/`** with one file or folder per project or client ([06:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=379s)). Group by month if that suits you ([06:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=391s)). Give priorities their own file so priority questions have a clear answer. His example router sends quarter-one priorities to a specific folder ([04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s)); the file name below is our suggestion.
6. **Write CLAUDE.md** with who you are, how you work and where things live ([05:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=344s)), plus explicit routing rules ([04:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=285s)). Adapt the starter below.
7. **Keep fast-changing data out.** His split is between context (evergreen) and connections (data that changes). Slack threads, emails and customer data change ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)). If you copy them into the brain they become noise ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)) that you'd have to clear out every month ([27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s)). His test: will this still be worth having in a year? ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)) See [[Context vs Connections]]. Leave live data where it is, but make sure the brain can reach it ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)). That's the job of [[Tiered Lookup Routing]], which you can add later.
8. **Test with vague questions** that don't name any file (prompts below). If Claude asks you for background or opens the wrong file, it probably was never told where to look, so fix the route ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)).
9. **Browse the tree yourself.** Find a specific file by opening folders from the top, the way he finds his slide deck ([07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s)). His point is that a structure you can navigate is one your agent can navigate too ([07:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=464s)).
10. **Keep the router short** as the brain grows ([05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s)). Add a routing line for each new area, and keep the content itself in the folders. When it starts to sprawl, run the line-by-line audit in [[Keep CLAUDE.md Lean]].

## Starter files & prompts

> [!note] Suggested starter content
> Everything in this section is original wording written for this vault. It follows the structure he shows at [05:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=344s)–[06:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=391s). These are not his actual files. Replace every `<placeholder>`.

### Folder tree

```text
my-brain/
├── CLAUDE.md                 # router: who I am, how I work, where things live
├── decisions.md              # append-only, dated decision log
├── context/                  # always-true background — read first
│   ├── about-me.md
│   ├── stack.md              # tools and services I use, and what for
│   └── conventions.md        # see note below
└── projects/
    ├── priorities.md         # this quarter's priorities, one line each
    ├── client-a/
    │   └── README.md         # overview + links to everything else in the folder
    └── 2026-06/              # optional month grouping
        └── launch-video/
            ├── README.md
            └── deck.html
```

The video's third context file is captioned "conversations" (possibly "conventions"; unclear in captions). `conventions.md` is our choice here. Name the file after what it actually contains.

**Stack file caveat.** [[Ras Mic - How AI Agents and Claude Skills Work]] argues against describing your tech stack in context files, because the code already shows it ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). Drop `stack.md` if the brain lives next to a codebase. Keep it short and routed if it covers tools that exist outside the folder. See Variations from other sources.

This tree is the base layout the vault's other starters build on, so their routing blocks point at the same paths. *(A shared layout is this vault's convention, not his; he stresses there's no proven standard, [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s).)*
- [[Ingest Sources into an LLM Wiki]] adds `references/`, `memory/MEMORY.md`, `inbox/` and `wikis/<name>/`, including `wikis/meetings/`.
- [[Add Semantic Search to One Folder]] adds `transcripts/`, `vector-index/` and `data/`.
- [[Grill Me Interview Skill]] and [[Build a Knowledge Graph Layer]] add `brainstorms/` and `knowledge-graph/`.

### `CLAUDE.md`

```markdown
# <Your name>'s Second Brain — Router

This folder is my second brain: plain markdown, organised so both of us can find things.
Read this file first. It says who I am, how I work with you, and where everything lives.

## Who I am
- <Name>, <role> at <business>. <One line on what I do and for whom.>
- Focus this year: <one line>.
- Full background: `context/about-me.md`.

## How to work with me
- Before asking me for background, check the routing table below. Ask only if the answer isn't there.
- Open files by following the table. Don't scan the whole folder.
- When you answer from a file, name the file.
- If something isn't in the brain, say so plainly. Don't guess.

## Where things live
| Path | What's in it | Open it when |
|---|---|---|
| `context/about-me.md` | Who I am, goals, preferences, key people | Anything about me personally |
| `context/stack.md` | Tools and services I use and what for | "What do I use for…", setup questions |
| `context/conventions.md` | How I like work done: formats, naming, tone | Before producing anything for me |
| `projects/priorities.md` | This quarter's priorities, one line each, linked to projects | Focus, planning, "what matters now" |
| `projects/<name>/README.md` | One folder per project or client; the README links the rest | Any named project or client |
| `decisions.md` | Dated log of big decisions and the reasons | "Why did we…", "when did we decide…" |

## Routing rules
1. Questions about me → `context/` first. It's always-true background; read it before anything else when context matters.
2. Priorities or "what should I work on" → `projects/priorities.md`, then the project files it links to.
3. A named project or client → that project's `README.md`, then drill down.
4. Past choices and the reasons behind them → `decisions.md`.
5. If no row fits, tell me. Suggest where the information should live and offer to add a row here.

## Decision log rule
When I make a big change to a project, the business, or my own plans, append an entry to `decisions.md`:
`## YYYY-MM-DD — <decision in a few words>`, then what changed, why, and what it affects.
Append only. Never rewrite old entries. If a new decision replaces an old one, say which.

## Keep out of this folder
Fast-changing data such as chat threads, email, and CRM records. Note where it lives instead of copying it in.
```

### `context/about-me.md`

```markdown
# About me
_Last reviewed: YYYY-MM-DD_

## Snapshot
- Name / role / business:
- Location and time zone:
- What I do, for whom, and how I make money:

## Goals
- This quarter:
- This year:
- Long term:

## How I think and decide
- What I optimise for:
- What I avoid / red lines:

## Working preferences
- Communication style I want from you:
- Formats I like (length, structure, tone):

## People who matter to my work
- <Name> — <relationship> — <what they own>

## Always true
- <Facts about me or the business that rarely change>
```

### `decisions.md`

```markdown
# Decision log
Append-only. Newest entry at the bottom. One entry per big decision.

## YYYY-MM-DD — Started a Level 1 second brain
- **Decision:** Keep my personal and business context as plain markdown in this folder, routed by CLAUDE.md.
- **Why:** I was re-explaining the same background in every session.
- **Affects:** Every session. Review the routing table monthly.
- **Replaces:** —
```

### `projects/priorities.md`

```markdown
# Priorities — <YYYY> Q<n>
_Updated: YYYY-MM-DD_

1. <Priority> — why it matters — link: `projects/<name>/README.md`
2. <Priority> — why it matters — link: `projects/<name>/README.md`
3. <Priority> — why it matters — link: `projects/<name>/README.md`

## Not doing this quarter
- <Thing deliberately parked>
```

### Test prompts

Run each one in a fresh Claude Code session, without naming any file:

1. "What should I focus on this quarter? Tell me which file you used."
2. "What tools do I use for <task>?"
3. "Why did I decide to <past decision>?"
4. "I've just decided to <big change>. Log it." Then check that `decisions.md` has a new dated entry.
5. "Where's the deck for <project>?"
6. "Based only on CLAUDE.md, which file would you open first for each of these: my background, my working style, client A, last month's big decision?" This checks the router without letting Claude open anything.
7. "What's my <something you never wrote down>?" Claude should say it isn't in the brain, not make something up.

## Done when

- [ ] Asked about your priorities without being pointed to a file, Claude opens the priorities file and answers correctly. It doesn't come back with "can you give me more info?" ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s), [05:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=316s)).
- [ ] For background questions, Claude names the file the router points to, not one it stumbled on ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)).
- [ ] After you describe a big change, a dated entry appears in the decision log ([06:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=371s)).
- [ ] You can find any file by hand, starting from the top-level folders, the way he finds his slide deck ([07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s)–[07:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=464s)).
- [ ] "Can my agent find it again? Can I?" gets a yes to both halves ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)).
- [ ] The structure makes sense to you. You didn't just copy someone else's ([07:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=423s)).

## Pitfalls

| Pitfall | What goes wrong | Fix | Source |
|---|---|---|---|
| **Router bloat** | CLAUDE.md grows until it's messy and its instructions feel ignored | Keep CLAUDE.md to routing lines and short rules. Put the content in folders | [05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s) |
| **Copying someone else's structure** | You adopt a layout that fits their work, not yours, and can't find things in it | Build around your own questions. No layout has been proven best | [06:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=415s) |
| **Putting fast-changing data in** | Slack threads, emails and customer data go stale, add noise, and need monthly cleanup | Keep evergreen context only. Note where live data lives instead | [27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s), [27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s) |
| **Missing routes** | Claude asks you for information that already exists in the folder | Add a routing rule saying where it lives | [04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s), [05:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=311s) |
| **Expecting Claude to search everything** | It won't read the whole folder unprompted, and doing so would waste time and tokens | Route explicitly | [05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s) |
| **Blaming retrieval when the files are thin** | Answers lack nuance because the nuance was never written down | Check the files are complete before changing the system | [22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s) |
| **Moving up a level without a real problem** | You add complexity that fixes nothing. Higher isn't automatically better | Move up only when a specific problem shows up | [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s), [19:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1161s) |
| **Chasing the graph view** | Many people get hooked on the visual view, but what matters is whether the system can fetch the answer | Treat Obsidian as optional | [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s), [10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s) |
| **Forgetting privacy** | Everything Claude reads is sent to Anthropic | Keep data you can't share out, or use open-source models for it | [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s) |

## Move to Level 2 when

- **You have 30+ notes and keep forgetting what's in them** ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)). This is the Level 2 signal in his Finding Your Level checklist.
- **You need to pull everything on one topic together.** That's the question Level 2 answers ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)).
- **Files pile up and take on a different shape** that suits topic-based organisation ([08:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=504s)), such as research on one project ([08:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=512s)) or a set of transcripts that deserves its own wiki ([08:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=516s)). See [[LLM Wiki]] and [[Ingest Sources into an LLM Wiki]].
- **You want Claude to keep its own notes**: turn on auto memory ([10:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=648s)). See [[Claude Code Auto Memory]].
- **The router is getting too big and messy**, the Level 1 weakness he names ([05:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=323s)). Treating that as a reason to move up is our inference.

Level 2 keeps everything from Level 1. It has the same shape ([10:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=624s)), and the router simply gains routes to a wiki, references and a memory file ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). Upgrade folder by folder, not the whole project at once ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)).

For perspective, he runs almost all of Herk2 at Level 2 ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)) and hasn't hit a problem big enough to go further ([12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s)). The captions say "level two" at that point, but from context he means level three. To decide whether your problem is real, use [[Second Brain Pain-Point Audit]].

## Variations

- **Codex or other agents.** Start with AGENTS.md instead of, or alongside, CLAUDE.md ([04:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=263s)). See [[Port a Claude Code Brain to Other Agents]].
- **Nested project folders**, as in Herk2: projects → YouTube videos → one dated folder per video ([07:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=447s)).
- **Month-based grouping** inside projects ([06:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=391s)).
- **A quarterly-priorities area.** Herk2 has a section for the quarter's projects, captioned "OTAs" (the exact term is unclear in the captions), with separate Q1 and Q2 sets ([27:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1621s)). Later he calls it "our OTA file" ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s)), so it isn't clear whether it's one file or a folder. Each holds its decisions and status ([27:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1628s)). He treats them as settled context the brain can rely on ([27:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1636s)).
- **A visual layer.** Install Obsidian if you're a visual person ([10:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=606s)).
- **Let Claude help design the structure.** Describe your data and how you'll use it, then ask Claude what setup fits. He suggests this for choosing between markdown and semantic search ([19:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1140s)). Applying it to Level 1 folders is our adaptation.
- **Downloads.** He says the free Skool community ([link](https://www.skool.com/ai-automation-society/about)) has his skills, including Grill Me ([20:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1246s)), and the slide deck ([30:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1848s)).

### Variations from other sources

- **Department router files instead of one long routing table.** From [[Jay E - The ARMS Framework for a Claude Agentic OS]].
  - **How it works.** His CLAUDE.md is the central router. It describes his departments (content, community and so on) so Claude works inside the relevant set of files for each ([12:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=745s), [12:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=750s)). Each department has its own router file, such as `content.md`, which is just a list of that area's skills and reference files ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s)).
  - **When he adds routers.** He treats them as a later step: his first memory level is a plain workspace of files ([10:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=642s)). He moves to routers once retrieval slows and plan usage drains. His workspace had grown to about 60,000 files ([11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s), [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)). This technique builds routing in from day one.
  - **Naming.** He says human-friendly naming matters less when agents operate on the files ([12:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=726s)). That cuts against this note's "can you find it too?" check ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)); see "Where sources disagree" in [[CLAUDE.md as a Router]].
  - His router set-up prompt appears only on screen ([13:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=814s)).
  - An adaptation for this layout (vault starter content, not his files):

  ```text
  my-brain/
  ├── CLAUDE.md               # who I am, how I work, one routing line per department
  ├── departments/
  │   ├── content.md          # list: skills + reference files for content work
  │   └── clients.md          # list: skills + reference files for client work
  ├── context/ …              # unchanged
  └── projects/ …             # unchanged
  ```

  In CLAUDE.md, add a row per department, for example: ``Content work → `departments/content.md` first, then only the files it lists``. Switch to this when the routing table stops fitting comfortably inside the file. See [[Keep CLAUDE.md Lean]].

- **A Cowork About Me folder made required reading.** From [[Simon Pittman - Set Up Claude Cowork]].
  - **Where the router's job goes.** In [[Claude Cowork]] it is split between global instructions (Settings, Cowork tab; [08:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=525s)) and an About Me folder holding `about-me.md`, `writing-rules.md` and `memory.md` ([12:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=776s)).
  - **Required reading.** He has Claude update the global instructions so it reads all three at the start of every session ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)), with that list moved to the top ([18:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=1127s)).
  - **What the files cover.** `about-me.md` covers what a smart new team member would need on day one, including audience and current projects ([14:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=859s)). `memory.md` is a log Claude appends to or updates so it doesn't lose track of projects ([15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s), [15:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=912s)), recording preferences, decisions and context after each session ([15:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=935s)). So it covers both this note's `decisions.md` and project status. `writing-rules.md`, which he has Claude build partly by researching anti-AI writing style ([14:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=879s)), has no equivalent here.
  - **Context map.** A `my-context-map.md` describing his Notion workspace joins the folder, so Claude finds databases on the first try ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s), [30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)).
  - **Projects and outputs.** `projects/` holds a CLAUDE.md, memory and brief per project, and `outputs/` holds deliverables ([35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s), [35:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=2155s)).
  - **Trade-off against this note** *(our reading)*: required reading loads every session instead of being opened on demand, and the memory file keeps growing. Keep those files short, and route to history rather than loading it.
  - Mapping *(ours)*: `context/` ≈ About Me folder, `decisions.md` + `projects/priorities.md` ≈ `memory.md`, CLAUDE.md ≈ global instructions.
  - Full walkthrough: [[Set Up Claude Cowork]].

- **Caveat: think twice before documenting your tech stack.** From [[Ras Mic - How AI Agents and Claude Skills Work]]. This disagrees with the `context/stack.md` file in the starter above.
  - **His argument.** For software projects you don't need context-file lines saying you use React and Convex, or Next.js and Supabase ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1186s)), because the code itself is now the context ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). Only tell the model what it won't know on its own ([32:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1971s)). He goes further: 95% of people don't need a CLAUDE.md or AGENTS.md at all ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)).
  - **Applying it here** *(vault reading, not his words)*:
    - If the brain sits inside or next to a codebase, drop the stack file; the agent can read the code.
    - In a personal brain with no code, the tools you use (CRM, calendar, where invoices live) aren't visible in any file. A short `stack.md` still earns its place there.
    - Either way, limit it to what the agent can't discover, and keep it as a route (a plain path) rather than something loaded every session.
  - The line-by-line audit is [[Keep CLAUDE.md Lean]].

## Beyond the source

Not from the video. Each item was checked against the linked documentation on 2026-09-15.

- **CLAUDE.md is context, not enforced configuration.** He calls it almost a system prompt. The docs say its content is delivered as a user message after the system prompt, so strict compliance isn't guaranteed, especially when instructions are vague or contradictory. Keep routing rules concrete. [Claude Code docs: troubleshoot memory issues](https://code.claude.com/docs/en/memory#troubleshoot-memory-issues)
- **Size target.** The docs recommend keeping each CLAUDE.md under about 200 lines, because longer files use more context and reduce adherence. This is a concrete limit for the router-bloat pitfall. [Claude Code docs: write effective instructions](https://code.claude.com/docs/en/memory#write-effective-instructions)
- **Write routes as plain paths, not `@` imports.** `@path/to/file` imports are expanded into context at launch, so they don't save any context. A path written without `@` (for example in backticks, which the import parser skips) is left for Claude to open when it needs it, which keeps the router light. [Claude Code docs: import additional files](https://code.claude.com/docs/en/memory#import-additional-files)
- **Location and load check.** A project CLAUDE.md can sit at `./CLAUDE.md` or `./.claude/CLAUDE.md`. Personal instructions for all projects go in `~/.claude/CLAUDE.md`. Run `/context` in a session and look under "Memory files" to confirm the file loaded. [Claude Code docs: choose where to put CLAUDE.md files](https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files)
- **The decision-log rule is a request, not a guarantee.** For anything that must happen at a fixed point, the docs recommend hooks, which run shell commands at lifecycle events whatever the model decides. [Claude Code docs: memory troubleshooting](https://code.claude.com/docs/en/memory#troubleshoot-memory-issues)
- **Private notes in the router.** Block-level HTML comments (`<!-- ... -->`) are removed before CLAUDE.md is added to context, so you can leave notes for yourself without spending tokens. [Claude Code docs: how CLAUDE.md files load](https://code.claude.com/docs/en/memory)
- **`/init` suits code projects.** It analyses a codebase and generates build commands, test instructions and conventions. Our suggestion: a personal second brain has no codebase, so its router is usually simpler to write by hand. [Claude Code docs: set up a project CLAUDE.md](https://code.claude.com/docs/en/memory)
- **Where auto memory actually lives.** Auto memory is on by default, and the `/memory` command toggles it. It's stored per project *outside* your folder, at `~/.claude/projects/<project>/memory/`. That folder holds a `MEMORY.md` index, whose first 200 lines or 25KB load every session, plus topic files that Claude reads when needed. It stays on one machine. The video shows a memory.md *inside* the example project folder ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)) and says auto memory writes and updates that file ([10:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=652s)). By default, though, nothing appears in your brain folder. To put it there, set `autoMemoryDirectory` to a path inside the brain; the value must be absolute or start with `~/`. (Default location also confirmed in this environment.) [Claude Code docs: auto memory](https://code.claude.com/docs/en/memory#auto-memory)

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]], mainly the Level 1 chapter ([04:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=259s)). Supporting points come from the intro ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)), Level 2 ([10:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=624s)), Level 4 ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)), Level 5 ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)) and Finding Your Level ([28:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1728s)). Video: https://www.youtube.com/watch?v=DTCyvo6cC54
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: memory levels and department router files ([10:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=635s)–[13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)). Used in Variations from other sources. Video: https://www.youtube.com/watch?v=8NSyI-npJCU
- [[Simon Pittman - Set Up Claude Cowork]]: global instructions, the About Me folder, the context map and projects/outputs ([08:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=492s)–[19:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=1190s), [29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s), [35:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=2113s)). Used in Variations from other sources. Video: https://www.youtube.com/watch?v=pl90LATQlHI
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the case against always-loaded files and stack descriptions ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s), [19:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1173s)–[20:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1202s), [32:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1971s)). Used in Variations from other sources. Video: https://www.youtube.com/watch?v=S_oN3vlzpMw

## Related

- Concepts: [[Second Brain Levels]] · [[CLAUDE.md as a Router]] · [[Design for Retrieval]] · [[Context vs Connections]] · [[Tool-Agnostic Context Files]] · [[Claude Code Auto Memory]] · [[LLM Wiki]] · [[Agent Skills]] · [[Agentic OS]]
- Techniques: [[Port a Claude Code Brain to Other Agents]] · [[Ingest Sources into an LLM Wiki]] · [[Tiered Lookup Routing]] · [[Grill Me Interview Skill]] · [[Second Brain Pain-Point Audit]] · [[Keep CLAUDE.md Lean]] · [[Set Up Claude Cowork]] · [[Build a Context Map for a Connected Tool]]
- Tools: [[Claude Code]] · [[OpenAI Codex]] · [[Obsidian]] · [[Claude Cowork]]
- People: [[Nate Herk]] · [[Matt Pocock]] · [[Jay E]] · [[Simon Pittman]] · [[Ras Mic]]
- [[Home]]
