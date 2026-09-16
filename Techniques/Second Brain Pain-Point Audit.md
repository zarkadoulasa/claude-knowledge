---
type: technique
goal: "Audit any Claude project folder by folder and choose the lowest second-brain level that fixes a pain you can actually observe, with no architecture added where nothing hurts"
difficulty: beginner
time_to_build: "30 to 90 minutes per project (vault estimate)"
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tools: ["[[Claude Code]]"]
tags: [topic/second-brain, topic/retrieval, topic/claude-code, topic/memory, topic/rag, topic/knowledge-graph]
---

# Second Brain Pain-Point Audit

> **Provenance.** The principles, symptoms and level mapping come from [[Nate Herk]]'s video, with timestamp links. The audit procedure, questionnaire, test prompts, scoring rules and report template are **original scaffolding written for this vault** to put those principles into practice. Where a test copies an example from the video, it links to that moment. Claude Code facts are verified under **Beyond the source** at the end.

## Goal

A repeatable audit Claude can run on any project, answering one question per folder: **what is the lowest level of [[Second Brain Levels|second brain]] that fixes a pain this folder actually has?** The output is a report table (folder | current level | pain observed | recommended level | change). Nothing changes until you approve it.

The rule behind it: find the simplest level that meets your needs, and if nothing hurts, don't build anything new ([04:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=242s)–[04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)).

## Use when

- You're tempted to add a vector database, a knowledge graph or an always-on system and want proof you need it.
- Claude keeps asking you for information that already lives in the project ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)–[05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)).
- A new kind of data is arriving and you need to decide how that folder should be structured ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)).
- As a periodic check-up on a brain that has grown.

**Skip it when** nothing is broken. No pain means no reason to add architecture ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)–[04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)).

## Principles the audit enforces

| # | Principle | What it means for the audit | Timestamp |
|---|---|---|---|
| 1 | No pain, no new architecture | "No change" is a valid, often correct result for a folder | [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)–[04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s) |
| 2 | Choose the lowest level that fits | Recommend the smallest step that fixes the observed pain | [04:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=242s)–[04:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=246s) |
| 3 | Higher is not better | Level 5 is not the target, and Nate gives reasons he doesn't sit there. Moving up only helps if it fixes a pain | [03:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=233s)–[03:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=239s), [19:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1156s)–[19:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1167s) |
| 4 | Levels are per folder | Score each folder separately. A project doesn't need to be one style throughout | [17:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1069s)–[18:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1091s), [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)–[28:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1736s) |
| 5 | Levels stack | The Level 3 and Level 4 example setups still keep context, decision and project files (and, at Level 4, the wiki and memory) as plain markdown with routing | [17:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1049s)–[17:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1056s), [23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s)–[23:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1403s) |
| 6 | Design for retrieval | Start from the questions you'll ask. How data is recalled should decide how it's stored | [02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)–[02:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=164s), [15:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=950s)–[15:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=957s) |
| 7 | The findability test | Can the agent find it again, and could *you*? If not, routing or folder structure is wrong | [02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s)–[02:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=140s) |
| 8 | The accuracy test | Does the brain know where data lives and where to look, and does it answer accurately? | [28:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1722s)–[28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s) |
| 9 | Capture before retrieval | Before blaming retrieval, check whether the files hold the nuance in your head | [22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s) |
| 10 | Context vs connections | Store evergreen data. Reach volatile data live instead of ingesting it | [27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s)–[28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s) |
| 11 | No single right structure | Don't grade a folder layout against someone else's. What counts is routing that makes sense to you and to the AI | [06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)–[07:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=428s) |
| 12 | Visuals aren't the value | A graph view is optional. Only retrieval quality counts | [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s)–[10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s) |
| 13 | When unsure, ask Claude | Describe the data and how you'll use it, then ask whether markdown or semantic search fits better | [18:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1139s)–[19:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1150s) |

Nate applies principle 1 to himself. His Herk2 project sits almost entirely at Level 2 because he hasn't felt enough pain to move up ([12:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=750s)–[12:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=760s)). *(The captions say "switch over to level two" there, but he has just said he sits at Level 2, so he means Level 3.)* He doesn't use knowledge graphs day to day either, because routing files and wikis cover his project-based, content-heavy work ([19:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1183s)–[20:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1201s)).

## The level map: symptom → level → change

| Level | Question it answers ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)) | Pain that justifies it (Finding Your Level) | Change to make | Watch-outs from the video |
|---|---|---|---|---|
| **1 · Router** | Can you find a file or fact by an exact word or name? ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)) | Claude needs your setup explained again and again, and your lookups are by exact word or file name ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s)–[29:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1740s)). Claude asks for info that exists in the project ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)) | Add or repair routing rules in CLAUDE.md / AGENTS.md that say which folder holds what ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)–[04:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=289s)). See [[Build a Level 1 Second Brain]], [[CLAUDE.md as a Router]] | A router that grows too big gets messy and starts being ignored. Lookups lean on exact words ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)–[05:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=329s)) |
| **2 · LLM Wiki** | Can you pull everything on a topic together? ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)) | You have 30+ notes and keep forgetting what's in them ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)–[29:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1748s)) | Ingest that folder into an indexed, interlinked wiki. Add routes to wiki, references and memory ([10:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=626s)–[10:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=647s)). See [[Ingest Sources into an LLM Wiki]], [[LLM Wiki]] | Wikis start to degrade a little at a certain point ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)). The agent reads whole pages even when it needs one detail ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)–[24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)). Links work like "see also", not typed relationships ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)–[12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)) |
| **3 · Semantic search** | You search with different words than you wrote. Can it match on meaning? ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)) | The project keeps missing notes you know exist, and your routing isn't working ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)–[29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s)). *(This audit tries a routing fix and re-tests before recommending L3.)* | Put a vector index on **that one folder** (e.g. transcripts) and keep context, projects and decisions as markdown ([17:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1056s)–[17:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1068s)). See [[Add Semantic Search to One Folder]], [[Semantic Search]] | Chunks lose whole-document context, so summaries miss things ([16:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=986s)–[16:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=998s)). Aggregate questions come back wrong ([16:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1013s)–[17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)). A vector DB is not magic ([16:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1007s)–[16:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1012s)) |
| **4 · Knowledge graph** | Can you ask about topic X and trace a chain back to topic A? ([03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s)) | You need relationships and want to follow chains of questions and thoughts ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)–[29:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1765s)). Nate says a graph would probably make more sense if he had a massive CRM spanning many businesses and clients, which he doesn't ([19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s)–[20:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1206s)) | Add a graph layer of entities and typed relationships next to the wiki ([23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s), [23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)–[23:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1423s)). See [[Build a Knowledge Graph Layer]], [[Knowledge Graphs]] | Usually the most complex level and sometimes the most expensive ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s)–[19:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1177s)). Only as good as the data you feed it ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)). If you don't need relationship chains, you probably don't need a graph ([25:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1517s)–[25:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1525s)) |
| **5 · Always-on brain OS** | Can the whole thing run without you thinking about it? ([03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s)) | Agents run without you (captioned "offline"), there's a lot of data, and several [[Hermes Agent]] instances need to stay in sync ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)–[29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)) | An always-on system such as [[GBrain]] that keeps syncing and refreshing memory ([25:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1529s)–[25:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1548s)). See [[Always-On Brain OS]] | In Claude Code you'd have to set up and manage the cron jobs yourself ([25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)–[25:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1558s)). Too much context can do more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)–[26:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1582s)). You lose hands-on control of what gets ingested ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)–[26:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1596s)) |

### Classifying a folder's *current* level (vault rubric)

| Current level | What you'll find in the folder |
|---|---|
| **Unrouted** | Files exist but CLAUDE.md / AGENTS.md never mentions the folder. Claude won't search the whole project on its own ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=313s)) |
| **L1** | Plain markdown files plus a routing rule saying what lives there and when to look ([04:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=277s)–[04:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=289s)) |
| **L2** | Ingested wiki pages with an index the agent starts from before drilling down, plus cross-links ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)–[12:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=733s)) |
| **L3** | A vector index or "smart lookup" over the folder's chunks (chunking, embedding, hybrid search, re-ranking) ([18:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1092s)–[18:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1101s)) |
| **L4** | Entity records with typed relationships (a graph folder or a graph tool such as [[LightRAG]]) ([23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)–[23:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1423s), [24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s)) |
| **L5** | Scheduled or continuous syncing and memory refresh that runs without you ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)–[26:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1568s)) |

## Prerequisites

- [[Claude Code]] (or another harness, since the brain is just files and folders that [[OpenAI Codex]] and Hermes Agent can read too) ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)–[01:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=112s)).
- Read access to the project, and 30 to 60 minutes of your time for the questionnaire and tests.
- **10 to 20 real questions** you have asked or expect to ask the brain. The audit works backwards from these ([02:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=156s)).
- A list of the live systems the brain should be able to reach but not store (e.g. ClickUp, Slack, email) ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)).

## Steps

1. **Set guardrails.** The audit is read-only. The only file it writes is the report (e.g. `audits/brain-audit-YYYY-MM-DD.md`). No restructuring until you approve.
2. **Inventory.** List the top-level folders, plus any sub-folder holding a different kind of data (transcripts inside projects, for example). For each, record the file count, the kind of data, whether it's evergreen or volatile, and the mechanism in use. Classify its current level with the rubric above.
3. **Check the router.** Go through the router checklist below: routing coverage, router size, AGENTS.md drift, memory routing, and whether live sources have a lookup order.
4. **Run the questionnaire.** Ask the user the questions below **one at a time** and skip any the files already answer. Note which folder each pain belongs to.
5. **Draft test prompts per folder.** Use the templates below with real names from the project. Test each folder at its **current** level, and at the **next level up** only if the questionnaire suggests pain there.
6. **Run the tests in a fresh session** (so earlier conversation doesn't leak answers) and don't mention file paths in the prompts. For each test, record: pass / partial / fail, which files were read, whether Claude asked you for something that exists, and whether it searched far more than needed.
7. **Check capture.** For the 1 to 3 topics that matter most, ask for a new-hire briefing and have the user mark what's missing. If the files were found but nuance is missing, the problem is capture, not level ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)). Fix it with [[Grill Me Interview Skill]].
8. **Check context vs connections.** Flag stored items that fail the one-year test or will change next week, and confirm the brain has a route to each live source ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)–[28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)).
9. **Apply the decision rules** (below) folder by folder. Every recommendation must cite evidence: a failed test or a pain the user confirmed.
10. **Write the report** from the template, with actions ordered cheapest first.
11. **Get approval, then change one folder at a time.** Use the matching technique note for each change.
12. **Re-test.** Re-run every test that failed. A change only counts if the test that motivated it now passes.

## Starter files & prompts

### Router checklist

| Check | Pass looks like | Why (source) |
|---|---|---|
| Every folder has a routing rule | CLAUDE.md names each folder, what's in it, and when to look there | Claude won't search everything by itself, so an unrouted file is effectively invisible ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=313s)) |
| The router isn't bloated | Short, scannable, no duplicated or conflicting rules | An overgrown router gets messy and ignored ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)–[05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)) |
| Other agents get the same routing | AGENTS.md matches CLAUDE.md, or one imports the other | Codex reads AGENTS.md. Nate keeps both files with the same content ([11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s)–[11:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=692s)) and notes CLAUDE.md can reference AGENTS.md instead ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)–[23:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1385s)). See [[Port a Claude Code Brain to Other Agents]] |
| Memory is routed | Auto memory is on and other agents are told where memory lives | Claude Code maintains memory itself. Other agents need a routing line pointing to it ([10:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=647s)–[11:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=661s), [11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s)–[11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)). See [[Claude Code Auto Memory]] |
| Live sources have a lookup order | The router says where to look first, next and last, ending at the live tool | His example: quarterly project file, then the wiki and meeting transcripts together, then ClickUp ([28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)–[28:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1711s)). See [[Tiered Lookup Routing]] |
| You can find things by hand | You can drill down to a known file in a few clicks | Nate finds a specific slide deck through projects → YouTube videos → the dated video folder, and his agent can too ([07:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=429s)–[07:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=467s)) |

### Questionnaire (ask one at a time)

| # | Question | Signal it measures | Points to |
|---|---|---|---|
| 1 | In the last two weeks, what did you have to re-explain to Claude that already lives in the project? | Re-explaining ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s), [05:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=314s)) | L1 routing |
| 2 | When Claude last asked you for more info, did that info already exist in a file? Which folder? | Routing gap ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)–[05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)) | L1 routing |
| 3 | Can *you* find a specific old file by drilling down without searching? | Human findability ([02:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=133s), [07:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=436s)) | L1 structure |
| 4 | Do you mostly look things up by exact names, file names or phrases? | Exact-word lookup ([29:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1740s)) | L1 is enough |
| 5 | Which folders have 30+ notes whose contents you've forgotten? | Note volume ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)) | L2 for those folders |
| 6 | Do you ask for everything on one topic, pulled together from many notes? | Topic synthesis ([03:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=209s)) | L2 |
| 7 | Have searches failed because you used different words than the note does? | Vocabulary mismatch ([03:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=213s)) | L3 candidate |
| 8 | Does Claude still miss notes you know exist after routing was fixed? | Missing known notes while routing isn't working ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)–[29:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1755s)) | L3 for that folder |
| 9 | Do you ask needle-in-a-haystack questions over a big body of text (one rule out of a thousand)? | Needle lookups ([18:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1101s)–[18:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1131s)) | L3 fits well |
| 10 | Do you ask for summaries of whole documents, or highest/lowest/total across tables? | Whole-document and aggregate questions ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s)–[17:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1047s)) | Keep as markdown, don't chunk |
| 11 | Do you need to follow chains, like who works where and which companies partner or compete? Do you manage many clients or businesses? | Relationship chains ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s), [20:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1201s)–[20:06](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1206s)) | L4 candidate |
| 12 | Do agents need the brain while you're away, with lots of data and several agents in sync? | Autonomy ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)–[29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)) | L5 candidate |
| 13 | Do you want to keep hands-on control of what gets ingested? | Ingestion control ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)) | If yes, weighs against L5 |
| 14 | Is anything stored that you'd delete within a year: Slack threads, emails, customer records? | Noise ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)–[27:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1671s)) | Hygiene: remove it, add a route |
| 15 | For recent events ("what did X and I discuss last week"), can the brain reach the live tool, and in what order does it look? | Connections ([28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)–[28:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1711s)) | Tiered lookup |
| 16 | What important knowledge exists only in your head? | Capture gap ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)) | Grill Me |
| 17 | Is there client or sensitive data here you shouldn't send to Anthropic? | Privacy ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1312s)) | Move it, or use a different model for that folder |
| 18 | Do you actually use a graph view, or does it just look good? | Visual appeal vs value ([09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s)–[10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)) | Don't upgrade for visuals |
| 19 | Which agents read this brain (Claude Code, Codex, Hermes)? | Portability ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s), [11:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=663s)) | AGENTS.md, memory routing |
| 20 | Does a team need to share it? | Team scope ([29:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1780s)–[30:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1838s)) | Defer until your own brain works |

### Test prompts per level

Fill the placeholders with real names from the project. Run each in a fresh session and don't mention paths.

**Level 1: routing and exact-word finds**

| Test prompt | Pass | Fail signals |
|---|---|---|
| "What's my current `<role / stack / top priority this quarter>`?" | Answers from the context file without asking you | Asks you for it although a file has it ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)) |
| "Find the notes about `<exact client or project name>`." | Goes straight to the routed folder | Searches the whole project or can't find it ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)) |
| "Open the `<artifact>` I made for `<project>`." (the video's slide-deck example: [07:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=438s)–[07:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=467s)) | Drills down through the folders to the file | Wrong file, or gives up |
| "What did we decide about `<decision>` and when?" | Reads the decision log with its date | Makes up a date, or has no route to the log |

**Level 2: pulling a topic together**

| Test prompt | Pass | Fail signals |
|---|---|---|
| "Pull together everything we know about `<topic>` across all notes, and list each note you used." | Starts from an index, drills into relevant pages, and covers notes you know exist ([11:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=712s)–[12:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=733s)) | Misses notes you've forgotten about, in a folder of 30+ ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)) |
| "How has my thinking on `<topic>` changed over time?" | Connects dated notes and decisions | Answers from a single note |
| "Which notes on `<topic>` contradict each other?" | Names specific pages | Can't compare across notes |
| Degradation check: ask for one small fact that sits inside a long wiki page | Finds it without reading many whole pages | Reads several full pages to get one detail ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)–[24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)) |

**Level 3: matching on meaning** (run only after the Level 1 routing tests pass)

| Test prompt | Pass | Fail signals |
|---|---|---|
| Synonym test ×5: pick five notes and ask about each **without using its key words** (note says "churn", you ask "which customers stopped paying?") | Finds the right note. The video's version: keyword search for "feedback" only shows where that word appears, while the smart lookup returns content that means feedback, such as live test results and a Claude Code skills item on evaluations ([14:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=882s)–[15:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=907s)) | Finds only exact-word matches, or nothing ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)) |
| Needle test: "Remind me what `<item 17 of a long list>` says." ([18:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1112s)–[18:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1131s)) | Returns just the snippet | Reads the entire large file every time |
| **Counter-test** (must pass whatever the level): "Summarise the `<date>` meeting." ([15:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=959s)–[16:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=998s)) | Reads the whole transcript | Summarises a handful of chunks and misses key points. That folder should stay markdown ([17:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1036s)–[17:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1047s)) |
| **Counter-test:** "Which `<week / month>` had the highest `<metric>`?" ([16:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1013s)–[17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)) | Scans the full table | Picks the highest value within one retrieved chunk |

**Level 4: following relationship chains**

| Test prompt | Pass | Fail signals |
|---|---|---|
| "Who do I know at `<company>`, and what's our history with them?" | Links person → company → interactions | Lists only files that mention the company |
| "`<Person>` works at `<company>`. Which of that company's partners or competitors have we dealt with?" (the shape of the video's fictional chain: a person works at a company, the company is endorsed by a third entity, and that entity is a competitor of a fourth, [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s)–[23:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1423s)) | Answers the multi-hop question and shows the path | Stops after one hop |
| "Trace how `<topic X>` connects back to `<topic A>`." ([03:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=218s)–[03:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=226s)) | Names each link and what kind of relationship it is | Returns see-also links with no relationship type ([12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s)–[12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)) |
| "If `<tool / decision / person>` changed, what else would be affected?" | Lists the things that depend on it | Can't reason across files |

**Level 5: autonomy** (these are operating questions for the user, not prompts)

| Question | Points to L5 when… | Points away when… |
|---|---|---|
| Do agents need current brain data while you're not there? | Yes, and it happens often ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)) | You run every session yourself |
| Are several agents (e.g. Hermes) working from copies that drift apart? | Yes ([29:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1769s)) | One agent, or one shared folder |
| Is manual ingestion falling behind the volume of data? | Yes, a lot of data ([29:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1767s)) | A weekly ingest keeps up ([26:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1588s)) |
| Are you willing to run and monitor scheduled jobs? | Yes, or your harness handles them ([25:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1551s)–[25:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1558s)) | No: in Claude Code you'd own the crons |

**Cross-cutting tests**

| Test prompt | Pass | Fail signals |
|---|---|---|
| Connections: "What did `<colleague>` and I discuss last week about `<project>`?" (his example: [28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)–[28:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1711s)) | Looks in his three tiers, in order: the project file, then the wiki and meeting transcripts together, then the live tool | Gives up without trying the live source, or answers from a stale stored copy |
| Capture: "Brief me on `<client>` as if I'm a new hire." | You'd hand this briefing to a new hire without corrections | Files were found but important nuance is missing ([22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)) |

### Decision rules

Apply these top to bottom for each folder. The first matching rule gives the recommendation.

1. **No failed test and no confirmed pain → no change** ([04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)–[04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)).
2. **Private data in the wrong place → handle privacy before anything else** ([21:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1303s)–[21:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1312s)).
3. **Volatile data stored in the brain → remove it and add a route to the live source** ([27:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1653s)–[28:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1687s)).
4. **Right file found but the answer lacks nuance → fix capture, not the level** ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)). Use [[Grill Me Interview Skill]].
5. **Claude asks for things that exist, or hunts everywhere → fix routing (L1)** ([04:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=292s)–[05:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=313s)).
6. **Router ignored or messy → trim and split the router (still L1)** ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)).
7. **30+ forgotten notes and weak topic answers → L2 wiki for that folder** ([29:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1743s)).
8. **Synonym tests fail after routing is fixed, and the folder's questions are needle lookups → L3 for that folder only**, keeping whole-document and aggregate data as markdown ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)–[29:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1755s), [17:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1032s)–[17:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1068s)). If unsure, describe the data and its use to Claude and ask ([18:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1139s)).
9. **Multi-hop tests fail and relationships matter to the work → L4**, but only after capture gives the graph enough data ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s), [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).
10. **Unattended agents (captioned "offline"), lots of data and several agents needing sync → L5**, after weighing cron overhead and context overload ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s), [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s), [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)).
11. **Never upgrade the whole project at once.** Recommend per folder ([17:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1078s)).

### Report template

```markdown
# Second brain audit: <project>, YYYY-MM-DD

## Summary
- Folders audited: <n> | Changes recommended: <n> | No change: <n>
- Biggest observed pain: <one line, with the failed test>
- Top actions, cheapest first:
  1. <e.g. add routing rules for meetings/ and references/>
  2. <e.g. grill-me session on client A>
  3. <e.g. ingest meetings/ into a wiki>

## Router check
| Check | Result | Evidence |
|---|---|---|
| Every folder routed | | |
| Router size / ignored rules | | |
| AGENTS.md in sync | | |
| Memory routed for all agents | | |
| Live sources + lookup order | | |
| Manual drill-down works | | |

## Folder levels
| Folder | Current level | Pain observed (evidence) | Recommended level | Change |
|---|---|---|---|---|
| context/ | L1 | None: L1 tests 4/4 pass | L1 | No change |
| decisions.md | Unrouted | Claude asked for a decision that is logged (test L1-4 fail) | L1 | Add routing rule |
| meetings/ | L1 | 45 transcripts; topic pull-together missed 3 of 5 known notes (L2-1 fail) | L2 | Ingest into wiki with index |
| references/ | L2 | 5/5 synonym tests fail after routing fix; needle questions dominate | L3 | Vector index on this folder only; keep whole-doc summaries in markdown |
| clients/ | L1 | Briefing missing pricing history and contacts (capture fail) | L1 | Grill Me per client, then re-test |

## Test results
| ID | Folder | Level | Prompt | Result | Evidence (files read / questions asked back) |
|---|---|---|---|---|---|

## Capture gaps
| Topic | Missing nuance | Fix |
|---|---|---|

## Context vs connections
| Item or folder | Evergreen? | One-year test | Action (keep / remove + route) |
|---|---|---|---|

## Privacy
- <client or sensitive data locations and decision>

## Not recommended (and why)
- <e.g. no knowledge graph: no multi-hop test failed>

## Re-test plan
- <which failed tests to re-run after each change, and when>
```

*(The example rows are illustrative, not from the video.)*

### Paste-in audit prompt

Paste it into a session, or save it as `.claude/skills/brain-audit/SKILL.md` with the frontmatter below. The prompt relies on the router checklist, questionnaire, test prompts, decision rules and report template above. Either paste those sections under it, or save them as files next to `SKILL.md` (the file names below are suggestions) so the links resolve. Without them, Claude will improvise its own versions.

```markdown
---
name: brain-audit
description: Read-only second brain pain-point audit. Scores each folder of this project against Levels 1-5, runs test prompts, and writes a report recommending the lowest level that fixes an observed pain. Use when the user asks to audit the second brain or decide how a folder should be structured.
---

Run a second brain pain-point audit on this project.

Rules
- Read-only. Do not create, move, rename or delete anything except the report at
  audits/brain-audit-<today>.md.
- Goal: for each folder, the LOWEST level that fixes a pain I actually have.
  "No change" is a valid result. Never recommend one level for the whole project.
- Every recommendation must cite evidence: a failed test or a pain I confirmed.

Levels
- Unrouted: files exist but CLAUDE.md/AGENTS.md never points to them.
- L1 Router: plain markdown folders + routing rules in CLAUDE.md/AGENTS.md.
- L2 LLM wiki: ingested, indexed, interlinked pages; memory routed.
- L3 Semantic search: vector index over one folder; everything else stays markdown.
- L4 Knowledge graph: entities + typed relationships next to the wiki.
- L5 Always-on: scheduled syncing/refreshing of memory across agents.

Procedure
1. Inventory top-level folders (and sub-folders with a different kind of data): file counts,
   data type, evergreen or volatile, mechanism in use, current level.
2. Router check: unrouted folders, bloated or conflicting rules, AGENTS.md drift,
   memory routing for non-Claude agents, live sources without a lookup order.
3. Ask me the questionnaire one question at a time. Skip anything the files already answer.
4. Write test prompts per folder: current level, plus the next level up only where my answers
   show pain. Give them to me as a numbered list to run in a fresh session; I will paste results.
5. Capture check on my top 3 topics: new-hire briefing, then I mark what is missing.
6. Context vs connections: flag anything that fails the one-year test or changes weekly,
   and propose a route to the live source instead.
7. Apply the decision rules in order, fill in the report template, order actions cheapest
   first, and list what you are NOT recommending and why.
8. Stop and wait for my approval before changing anything.

Reference material (files next to this one)
- Router checklist and questionnaire: [questionnaire.md](questionnaire.md)
- Test prompts per level: [test-prompts.md](test-prompts.md)
- Decision rules: [decision-rules.md](decision-rules.md)
- Report template: [report-template.md](report-template.md)
```

## Done when

- [ ] Every top-level folder, and every sub-folder with a different kind of data, has a row in the folder table.
- [ ] Every row has a current level, observed pain (or "none") with evidence, a recommended level and a change (or "No change").
- [ ] The router check is complete, including AGENTS.md, memory routing and live-source lookup order.
- [ ] Each folder has at least one test at its current level. Higher-level tests ran only where pain pointed there.
- [ ] The Level 3 counter-tests (whole-document summary, aggregate) were run on any folder proposed for semantic search.
- [ ] Capture was checked on the top 1 to 3 topics, and gaps have a Grill Me follow-up.
- [ ] Volatile data is flagged, with a route to the live source proposed instead.
- [ ] The report lists what is **not** recommended and why.
- [ ] The user approved changes before any restructuring, and failed tests were re-run afterwards.

## Pitfalls

- **Climbing for its own sake.** Level 5 isn't "best", and neither is a graph view you won't use ([03:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=233s)–[03:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=239s), [09:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=593s)–[10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s)).
- **One level for the whole project.** A brain doesn't need GraphRAG or an LLM Wiki everywhere ([17:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1078s)–[18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s)).
- **Chunking data that needs whole-document reads.** Meeting summaries and "highest week" questions get worse with vectors ([16:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=986s)–[17:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1047s)). Metadata can help, but a vector store is not a magic fix ([16:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1000s)–[16:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1012s)).
- **Treating wiki links as a knowledge graph.** Backlinks don't carry relationship types, so they aren't the same as graph edges ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)–[13:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=782s)).
- **Blaming retrieval for a capture problem** ([22:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1349s)–[22:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1366s)).
- **Jumping to semantic search before fixing routing.** The video's Level 3 trigger is missed notes *and* routing that isn't working ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)–[29:15](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1755s)).
- **Ingesting connections.** Slack, email and customer data become noise and a monthly clean-up job ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)).
- **Always-on without guardrails.** More context can do more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)–[26:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1582s)).
- **Grading against someone else's folder structure.** There's no proven standard layout yet ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)–[07:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=422s)).
- **Forgetting other agents.** Claude-specific memory is invisible to Codex unless routed ([11:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=663s)–[11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)).
- **Solving the team brain first.** Get your own brain working, then deal with adoption and change management across the team ([30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)–[30:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1838s)).
- **Contaminated tests.** Running tests in a session that already discussed the answer, or naming file paths in the prompt, produces false passes.

## Variations

- **Ten-minute version.** Ask only the five Finding Your Level questions (re-explaining, 30+ notes, whiffing despite routing, relationship chains, unattended (captioned "offline") synced agents), one per folder ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s)–[29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)).
- **Single-folder decision.** When new data arrives, run only step 2 and the Level 3 tests and counter-tests for that folder, then ask Claude whether markdown or semantic search fits ([18:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1139s)–[19:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1150s)).
- **Multi-agent audit.** Run the same test prompts through Claude Code and Codex, or Hermes. Differences in the answers usually point to AGENTS.md or memory-routing drift ([01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)–[01:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=112s), [11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s)–[11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)).
- **Team audit (later).** Add questions on whether process owners keep docs current and whether colleagues use the brain instead of pinging people ([30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s)–[30:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1817s)).

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]]: the five levels overview ([03:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s)–[04:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=257s)), per-folder levels ([17:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1069s)–[18:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1091s)), capture ([22:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1340s)–[22:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1367s)), context vs connections ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s)–[28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s)), Finding Your Level ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)–[29:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1771s)).
- *Transcript notes:* his quarterly projects are captioned "OTAs", and the exact term is unclear in the captions. The Level 5 trigger is captioned as running agents "offline". At [12:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=757s) the captions say "level two" where context means Level 3.

## Beyond the source

Not from the video. Each item was checked on 2026-09-15 at the linked page.

- **Where Claude Code auto memory lives.** The video shows a `memory.md` inside the example project folder ([10:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=635s)). Claude Code's own auto memory is stored per project **outside the repo**, at `~/.claude/projects/<project>/memory/`, with a `MEMORY.md` index loaded at the start of each session (the first 200 lines or 25KB). It is machine-local. When auditing memory routing, check that folder, and remember that other agents and machines can't see it unless you copy or route it. Source: [Claude Code docs: How Claude remembers your project](https://code.claude.com/docs/en/memory).
- **Checking what actually loaded.** Run `/context` in a session to see which CLAUDE.md and memory files loaded. `/memory` lists memory files and toggles auto memory. This makes a quick first router check. Source: [Claude Code docs: memory](https://code.claude.com/docs/en/memory).
- **Router size.** Anthropic suggests keeping each CLAUDE.md under about 200 lines, because longer files use more context and reduce adherence. `@path` imports don't reduce context, since imported files still load at launch. Path-scoped rules in `.claude/rules/` and skills load only when relevant, which makes them the documented way to slim a bloated router. Source: [Claude Code docs: memory](https://code.claude.com/docs/en/memory).
- **AGENTS.md parity.** Claude Code reads CLAUDE.md, not AGENTS.md. The documented options are a CLAUDE.md that imports it (`@AGENTS.md`) or a symlink, so both tools read one set of instructions. This matches the video's tip at [22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s). Source: [Claude Code docs: memory, AGENTS.md section](https://code.claude.com/docs/en/memory).
- **Saving the audit as a skill.** Project skills live at `.claude/skills/<skill-name>/SKILL.md` and can be run as `/skill-name`. A skill folder can also hold supporting files that `SKILL.md` links to, which Claude reads only when needed, and `description` is what Claude uses to decide when to apply the skill. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).

## Related

- Concepts: [[Second Brain Levels]] · [[Design for Retrieval]] · [[Context vs Connections]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[CLAUDE.md as a Router]] · [[Claude Code Auto Memory]] · [[LLM Wiki]] · [[Semantic Search]] · [[Knowledge Graphs]] · [[Always-On Brain OS]] · [[Tool-Agnostic Context Files]]
- Techniques: [[Build a Level 1 Second Brain]] · [[Ingest Sources into an LLM Wiki]] · [[Add Semantic Search to One Folder]] · [[Build a Knowledge Graph Layer]] · [[Tiered Lookup Routing]] · [[Grill Me Interview Skill]] · [[Port a Claude Code Brain to Other Agents]]
- Tools & people: [[Claude Code]] · [[OpenAI Codex]] · [[Hermes Agent]] · [[GBrain]] · [[LightRAG]] · [[Nate Herk]]
- [[Home]]
