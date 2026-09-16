---
type: technique
goal: "Put a lookup order in CLAUDE.md so vague questions get answered from the right layer: curated context first, then the wiki and meeting transcripts, then the live system through a connector. Volatile data stays reachable but is never ingested."
difficulty: intermediate
time_to_build: "About an hour for the routing block and tests, plus connector setup (estimate, not from the video)"
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]", "[[Claude Cowork]]"]
tags: [topic/second-brain, topic/retrieval, topic/claude-code, topic/prompting, topic/mcp, topic/cowork]
---

# Tiered Lookup Routing

## Goal

Let the brain answer a vague question without you pointing it at a file. Your CLAUDE.md holds an **ordered list of places to look**. It starts with the most curated, stable layer and ends with live data pulled from the tool where work actually happens.

[[Nate Herk]] still counts this as a second brain. He can ask a vague question, and the brain knows which places to check, in which order, to reach up-to-date data ([28:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1713s)–[28:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1717s)). His yardstick is simple. Does the system understand where your data lives and where to look? Does it give accurate answers ([28:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1724s))?

## The pattern from the video

### His worked example

The question: what did he and a colleague (John) discuss last week about quarterly project number seven ([28:09](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1689s)–[28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s))?

| Tier | Where the agent looks | What lives there | Timestamp |
|---|---|---|---|
| 1 | The quarterly projects file (captioned "OTAs"; *exact term unclear in captions*) | This quarter's projects, the decisions locked in for them, and statuses he keeps updating ([27:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1621s)–[27:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1639s)) | [28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s) |
| 2 | The wiki and meeting transcripts, named together as one fallback | Ingested, cross-linked knowledge ([[Ingest Sources into an LLM Wiki]]) and what was said in meetings | [28:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1701s)–[28:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1705s) |
| 3 | ClickUp itself, live | The actual conversation between him and John, pulled in as real data | [28:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1706s)–[28:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1709s) |

The agent only moves down a tier when the one above doesn't have the answer ([28:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1701s), [28:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1706s)).

*This note's suggestion, not his:* split his second tier in two, checking the wiki before the meeting transcripts, so the curated summaries get a chance before the meeting records. The starter block below uses that split. Its tiers run 1–4, with the live system as tier 4.

### The rule underneath: context vs connections

His AI OS videos use four Cs: context, connections, capabilities and cadence. For a second brain he mostly thinks about the first two ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s)–[26:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1607s)). That split decides which tiers are files and which is live. See [[Context vs Connections]].

| | Context: ingest it | Connections: reach it, don't ingest it |
|---|---|---|
| What it is | What the business has done ([26:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1613s)): quarterly projects, locked-in decisions, statuses ([27:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1636s)) | Real data that isn't evergreen and keeps changing ([27:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1647s)): Slack threads, emails, customer data ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)) |
| His test | Will this be good to have in a year? ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)) Evergreen, holistic data ([27:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1678s)) | Will it change next week? ([28:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1680s)) |
| Why it's handled this way | His brain is the stuff he won't delete ([27:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1663s)) | Ingesting it is noise, and you end up clearing old material every month ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)) |
| How the brain uses it | Reads the files (tiers 1–2 in his example) | Don't pull it in, but make sure the brain can go and get it (tier 3 in his example, tier 4 in the starter) ([28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)) |

### Why an explicit order at all

- **No route, no retrieval.** Claude won't search your whole project on its own, and you wouldn't want it to, because that wastes time and tokens. If it doesn't know something lives somewhere, it probably won't find it ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)).
- **Once routing is set up, you stop re-explaining.** The agent knows where to look and why ([05:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=314s)).
- **His Level 1 routing already has the seed.** Rules like "for quarter-one priorities, look in this folder" ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)–[04:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=288s)). This technique turns one route per topic into an ordered chain of fallbacks. (That framing is this note's, not his wording.) See [[CLAUDE.md as a Router]].

## Making the live tier navigable: a context map (Simon Pittman)

Nate's example ends with "then ClickUp" and doesn't say how the agent finds the right list or thread once it's there. [[Simon Pittman - Set Up Claude Cowork]] offers one answer, in [[Claude Cowork]] with Notion as the live system.

| Step | What Simon does | Timestamp |
|---|---|---|
| The problem | Notion is connected through its MCP server, which can query, read and write. Even so, his first search for a named project page took several attempts | [28:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1717s)–[28:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1736s) |
| Build the map | He asks Claude to read a top-level Notion page that links all his databases and create a context map of the workspace. On screen he drops in a `my-context-map.md` he had built that way earlier | [29:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1760s)–[29:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1789s), [30:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1814s) |
| Make it load every time | The map goes into his About Me folder, and he asks Claude for updated global instructions so it's always read | [29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s)–[30:05](https://www.youtube.com/watch?v=pl90LATQlHI&t=1805s) |
| The result | Asked which tasks are due this week, Claude went straight to the right database | [30:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1823s)–[30:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1838s) |
| Generalise | Make a map for whatever system holds your plans, projects, notes or knowledge base | [30:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1844s)–[30:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=1855s) |
| Side benefit | Claude stops burning tokens hunting for things | [31:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1863s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s) |

- **How it fits this technique.** His global instructions list required reading for the start of every session, moved to the top of the instructions ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)–[18:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1133s)). His weekly scheduled briefer is told to read his About Me files first and then use the Notion MCP ([42:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2538s)–[42:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2542s)). *This note's framing:* the map is a set of directions for the live tier. The lookup order says *when* to go live, and the map says *where to go* once you're there.
- **A live tool can hold context, not just chatter.** Simon separates Notion from email and calendar because it holds context: projects, knowledge and meeting notes ([27:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1661s)–[28:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1698s)). That's a reason to decide where each connected tool belongs in the order rather than putting all of them last. See [[Context vs Connections]].
- **Safety on the live tier.** He sets permissions per tool; Notion's can be allowed, need approval or be blocked ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)). He also tells Claude to create email drafts rather than send, and to record that rule ([26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s)–[26:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1598s)).
- **Where to go next.** The full build is [[Build a Context Map for a Connected Tool]]. Connector setup across Claude surfaces is in [[Connecting Claude to External Tools]].

## Use when

- You ask vague questions that span several sources, like his "what did we discuss last week about project seven" ([28:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1713s)).
- Claude asks you for more information even though the files exist ([04:51](https://www.youtube.com/watch?v=DTCyvo6cC54&t=291s)).
- Some answers live in fast-changing tools you shouldn't ingest ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)).
- You keep re-explaining your setup, which is his signal to fix Level 1 routing ([28:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1737s)).

**Not the fix when:**
- Claude keeps missing notes you know exist and routing isn't working. His pointer there is semantic search, which doesn't rely on exact-word matches. Look at [[Add Semantic Search to One Folder]] ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)).
- You need to follow chains of relationships. Look at [[Build a Knowledge Graph Layer]] ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)).

## Prerequisites

- **A Level 1 router.** See [[Build a Level 1 Second Brain]].
- **A curated tier 1 worth checking first.** For example, a file of this quarter's projects with the decisions made and statuses you actually keep current ([27:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1628s)–[27:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1639s)).
- **Optional middle tiers.** A wiki ([[Ingest Sources into an LLM Wiki]]) and a folder of meeting transcripts.
- **Access to the live system through a connector.** Claude Code setup is under *Beyond the source*.
- **A privacy check.** Data you process through Claude goes to Anthropic ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)), and that includes whatever it pulls from live systems. For client data you may prefer open-source models ([21:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1304s)–[21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).

## Steps

1. **List and classify your sources.** Write down every place answers live. Label each as *context* or *connection* using his test: useful in a year, or changing next week ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s), [27:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1678s)–[28:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1680s)).
2. **Collect the vague questions you really ask.** Aim for 5–10. Design from how the data will be recalled ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s), [02:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=162s)).
3. **Map each question to where its answer lives, and let the order fall out of that.**
   - His order is the quarterly file, then the wiki and meeting transcripts together, then ClickUp ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s)–[28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)).
   - The starter below splits his middle step into a wiki tier and a meeting-transcript tier, so the live system becomes tier 4. That split is this note's choice.
   - There's no proven standard layout, so adapt it to your data ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)).
4. **Keep tier 1 current.**
   - It works because he treats its decisions as locked in and updates the statuses ([27:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1636s)–[27:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1639s)).
   - *Suggestion (not from the video):* store each project's live-system list or task link in tier 1. Then a tier 4 lookup goes straight to the right place.
5. **Write the lookup-order block in CLAUDE.md** (starter below). It should have:
   - numbered tiers with paths
   - a stop-at-first-answer rule
   - a read-only rule for tier 4
   - a "name the tier you used" rule
   - what to do when nothing is found
6. **Connect tier 4.** Add a connector for the live system (ClickUp in his example ([28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s))). Commands, authentication and read-only permission rules are under *Beyond the source*.
   - **Set permissions per tool before the first live query.** Simon does this for Notion, where each permission can be allowed, need approval or be blocked ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)).
   - **Map the live system.** Do this if it has more than a handful of lists, databases or spaces. Have Claude read its top-level page or list and write a short context map. Then have CLAUDE.md load it or point to it from tier 4. His first Notion search took several attempts; with the map, Claude went straight to the right database ([28:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1733s), [29:20](https://www.youtube.com/watch?v=pl90LATQlHI&t=1760s)–[30:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1838s)). There's a starter below; the full build is in [[Build a Context Map for a Connected Tool]].
7. **Add a do-not-ingest rule.**
   - Data fetched in tier 4 is used for the answer, not saved into the brain ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)).
   - *Suggestion:* when a lasting decision comes out of a thread, record it as one dated line in the decision log. His Level 1 example already appends decisions with dates ([06:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=370s)).
8. **Mirror the block for other agents.** Copy CLAUDE.md to AGENTS.md ([11:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=679s)), or reference AGENTS.md from CLAUDE.md ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)). See [[Port a Claude Code Brain to Other Agents]].
9. **Test with the prompts below.** Have Claude name every tier it checked.
10. **Revisit when something hurts.**
    - Different folders can sit at different levels ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)). Add a semantic or graph tier only for the folder that is failing ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s), [29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)).
    - If answers lack nuance, the gap is often capture rather than routing: the knowledge never got out of your head ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)–[22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s)). See [[Grill Me Interview Skill]].

## Starter files & prompts

*Original examples written for this vault. The video describes the order of lookup but doesn't give the routing text he uses. Paths follow the vault's shared starter layout: the base tree in [[Build a Level 1 Second Brain]] plus `wikis/` from [[Ingest Sources into an LLM Wiki]].*

### CLAUDE.md lookup-order block

```markdown
## Lookup order
For questions about projects, people, decisions, or "what happened with X",
check these tiers in order. Stop at the first tier that fully answers.
End the answer with: `Found in: tier N (<file or system>)`.

1. **Curated context**: `projects/priorities.md`, then `decisions.md`.
   This quarter's projects, owners, locked decisions, current status, live-system links.
2. **Wiki**: `wikis/<name>/index.md` (e.g. `wikis/youtube/`), then only the pages the index points to.
3. **Meeting transcripts**: `wikis/meetings/meetings/`, one page per meeting, named `YYYY-MM-DD-<people>-<topic>.md`.
   Narrow by date and people from the filename first; read matching files in full.
4. **Live systems (read-only)**: ClickUp via the `clickup` connector.
   Use the links from tier 1 to go straight to the right list or task.
   Only for what tiers 1–3 don't answer, or anything asked as "latest", "current", "right now".

### Lookup rules
- Resolve names first: use tier 1 to turn "project 7" or a first name into the exact
  project, people and links before searching lower tiers.
- If a tier-1 status is older than two weeks, confirm it in tier 4 before relying on it.
- If tiers disagree, prefer the most recent dated source and tell me about the conflict.
- Tier-4 data is for answering, not saving. Never copy threads, emails, customer records
  or statuses into the brain. If a lasting decision shows up, propose a one-line dated
  entry for `decisions.md` and wait for my OK.
- If no tier has the answer, say so and list what you checked. Don't guess.
```

### Tier 1 file skeleton

```markdown
# Quarterly priorities: Q3 2026
_Updated 2026-09-14_

| # | Project           | Owner  | Status      | Live link           | Last decision |
|---|-------------------|--------|-------------|---------------------|---------------|
| 7 | Onboarding revamp | <name> | In progress | <ClickUp list URL>  | 2026-09-02    |

## 7: Onboarding revamp
- Goal: …
- Locked decisions
  - 2026-08-11: …
  - 2026-09-02: …
- Status (overwrite, don't append; update the date above): …
- Meetings: wikis/meetings/meetings/2026-09-08-<name>-onboarding.md
- Wiki pages: wikis/<name>/concepts/<page>.md
```

### Tier 4 context map (add-on, after Simon Pittman's idea)

*Vault starter content. Simon's own map isn't shown on screen, so this is not his file. Save it as `context/clickup-context-map.md`, one file per live system, alongside the Level 1 `context/` files. Then add this line to tier 4 of the lookup block: "Read `context/clickup-context-map.md` first; use its links instead of searching."*

```markdown
# ClickUp context map
_Built 2026-09-15 from the workspace home. Rebuild when spaces or lists change._

## What lives here (and what doesn't)
- Live: task statuses, comments, assignees, due dates. Fetch them; never copy them into the brain.
- Not here: locked decisions (decisions.md), meeting notes (wikis/meetings/).

## Structure
| Space    | List            | What it holds                                   | Link       |
|----------|-----------------|-------------------------------------------------|------------|
| Delivery | Q3 projects     | One task per quarterly project (same # as projects/priorities.md) | <list URL> |
| Delivery | Client requests | Inbound asks, triaged weekly                    | <list URL> |
| Ops      | Recurring admin | Invoices, renewals                              | <list URL> |

## How to query
- "Status of project N": open the task linked in projects/priorities.md. Don't search.
- "What's due this week": filter the Q3 projects list by due date. Don't scan every space.
- People: comments use first names; resolve them with context/about-me.md.

## Rules
- Read-only. Write tools are denied in settings (see Beyond the source).
```

**Prompt to build the map** *(vault starter content)*:

```text
Using the clickup connector, read only. Don't create or edit anything in ClickUp.
List the spaces, folders and lists I can see. Then write context/clickup-context-map.md with:
a date line; one table row per list (what it holds, its URL); a "how to query" section
covering my five most common questions; and a line saying what must never be copied
into the brain. Keep it under 60 lines. Show me the file before saving.
```

### Test prompts

| Prompt | Should stop at | Pass if |
|---|---|---|
| "What's the status of project 7?" | Tier 1 | Answers from the priorities file without opening the wiki or ClickUp |
| "What do my notes say about <a concept you ingested>?" | Tier 2 | Opens the wiki index, then a few pages |
| "What did we agree in Monday's meeting with <person>?" | Tier 3 | Narrows by filename and reads the matching meeting in full |
| "What did <person> and I discuss last week about project 7?" (the shape of his example) | Tier 3 or 4 | Checks the tiers in order and names each one checked |
| "What's the latest comment on the project 7 task?" | Tier 4 | Uses the link from tier 1; nothing is written into the brain afterwards |
| "What's due this week in <live system>?" (the shape of Simon Pittman's test, [30:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1823s)) | Tier 4 | Reads the context map, then queries the right list or database first time with no trial searches |
| "What did we decide about <something that never happened>?" | None | Says it wasn't found and lists the tiers checked |
| Any prompt above, in Codex with AGENTS.md | Same tier | Same path as in Claude Code |

## Done when

- [ ] CLAUDE.md has a numbered lookup order with real paths, a stop rule and a not-found rule
- [ ] Every path in tiers 1–3 exists and holds real content
- [ ] Tier 1 lists each project's live-system link and a last-updated date
- [ ] The tier-4 connector is connected and authenticated, and any write tools are blocked
- [ ] If the live system has more than a handful of lists or databases, a dated context map exists and CLAUDE.md loads it or points to it
- [ ] The first tier-4 query in a fresh session reaches the right list or database without trial searches
- [ ] Every test prompt stops at the expected tier and names it
- [ ] A question shaped like his example gets answered without you mentioning a file or tool
- [ ] After tier-4 answers, `git status` (or a folder diff) shows nothing ingested
- [ ] If you use other agents, AGENTS.md carries the same block

## Pitfalls

- **Missing routes.** Without a route, Claude probably won't find the data ([05:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=303s)–[05:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=310s)).
- **Router bloat.** A CLAUDE.md that grows too big gets messy and feels ignored ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)). Keep the lookup block short, and put long procedures in skills (see *Beyond the source*).
- **Ingesting connection data.** It becomes noise and needs monthly cleanup ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s)–[27:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1661s)). He also worries about reaching a point where more context does more damage than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)).
- **A tension in the video.**
  - Early on, he lists ClickUp threads among the things he saves into his brain ([02:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=122s)).
  - Later, he says threads and similar volatile data should be reachable, not ingested ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)–[28:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1684s)).
  - A workable reading (this note's, not his): ingest the lasting outcome of a thread, such as a decision or a spec, and fetch the thread itself live.
- **A stale tier 1 cuts the search short.** Tier 1 is trustworthy only because he keeps its statuses updated ([27:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1639s)). If it goes stale, Claude can "fully answer" from an old status and never reach the live tier. The starter's freshness rule guards against this; the rule is this note's suggestion.
- **Exact-word misses.** Level 1-style routing mostly finds things by exact words ([05:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=325s)). If Claude keeps missing notes you know exist, add semantic search to that folder ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)).
- **Chunked transcripts in tier 3.** If meeting transcripts are stored as vector chunks, a summary only covers the chunks retrieved ([16:28](https://www.youtube.com/watch?v=DTCyvo6cC54&t=988s)). A whole markdown file per meeting gives more accurate summaries ([17:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1038s)).
- **One order for everything.** Your whole project doesn't have to sit at one level ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)), and no layout has been proven the standard ([06:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=402s)). Different question types can use different orders.
- **Privacy of live pulls.** His warning that data processed through Claude goes to Anthropic applies to Slack, email or task-tool data too ([21:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1289s)–[21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- **Write-capable connectors.** A connector that can change data turns a lookup into a risk. Check the tool list and block write tools (see *Beyond the source*). Simon Pittman's Notion connector can query, read *and* write ([28:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1720s)–[28:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=1723s)). He controls it with per-tool permissions and a drafts-only rule for email ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s), [26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s)–[26:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1598s)).
- **No map for a sprawling live system.** Without one, Simon's first Notion lookup took several attempts, and he says a map stops Claude burning tokens on searches ([28:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1733s)–[28:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1736s), [31:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1863s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s)).
- **A stale or bloated map.** *This note's suggestion:* a map loaded every session costs context every time. If it lags behind renamed lists, it sends Claude to the wrong place. Keep it short and dated, and rebuild it when the structure changes. The router-bloat warning above applies here too ([05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)).
- **Team brains go stale.** A shared lookup order only works if process owners keep their docs updated and people pull from them. He sees adoption and change management as the bigger problem than the tech ([30:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1807s)–[30:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1818s)).

## Variations

- **Another live system.** He names Slack threads, emails and customer data as connection-type data ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s)). Any of them can be tier 4 once the brain has access.
- **A semantic tier.** Put a meaning-based search over one large folder between tiers 2 and 3 ([29:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1750s)). See [[Add Semantic Search to One Folder]] and [[Semantic Search]].
- **A graph tier** for questions that follow relationship chains ([29:20](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1760s)). See [[Build a Knowledge Graph Layer]] and [[Knowledge Graphs]].
- **Always-on sync (Level 5).** [[GBrain]] keeps syncing and refreshing memories ([25:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1544s)). He points to it for running agents "offline" (as captioned; likely meaning unattended) and syncing many [[Hermes Agent]] instances over lots of data ([29:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1766s)). He himself prefers to control what gets ingested ([26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s)). See [[Always-On Brain OS]].
- **A wiki in a separate vault.** In [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]], Herk2's CLAUDE.md gives the path to his Herk Brain vault. For facts it lacks, it reads the hot cache, the index and the domain sub-index, or searches ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s)). A "don't read the wiki unless needed" rule lists tasks that skip it ([14:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=850s)). Replacing in-project context files with this cut tokens, though he gives no figures ([14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s)). See [[CLAUDE.md as a Router]] and [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **Lookup order in a skill or rule file** instead of CLAUDE.md, if the block grows. See *Beyond the source*.
- **In Claude Cowork.** Simon Pittman keeps his rules in Cowork's own global instructions (Settings, then Cowork, then Global instructions). Cowork reads them at the start of every conversation ([08:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=521s)–[08:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=537s)). Any folder can also carry its own CLAUDE.md ([12:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=726s)–[12:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=728s)). The lookup block and the context-map reference can go there. He pastes the CLAUDE.md text into the settings box, after asking Claude whether to delete the old file ([11:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=684s)–[12:04](https://www.youtube.com/watch?v=pl90LATQlHI&t=724s)). *This note's caveat:* instructions that exist only in that box are invisible to Claude Code and to other agents that read the folder. Keep a file copy if you use more than one agent.
- **A context-holding live tool placed higher.** Some live tools hold curated knowledge, as Simon's Notion does ([28:09](https://www.youtube.com/watch?v=pl90LATQlHI&t=1689s)–[28:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1698s)). Such a tool can sit above the meeting-transcript tier instead of last. Keep the read-only rule. *(This note's suggestion.)*

## Beyond the source

*None of this comes from the videos. Each item was checked at the linked page.*

- **Connectors in Claude Code are MCP servers.** Verified: [Claude Code MCP docs](https://code.claude.com/docs/en/mcp).
  - Add a remote server with `claude mcp add --transport http <name> <url>`. For a local stdio server, put the command after `--`.
  - Scopes: *local* (the default, this project only, stored in `~/.claude.json`), *project* (stored in `.mcp.json` at the project root and shareable through version control) and *user* (all your projects). Set the scope with `--scope`.
  - `/mcp` inside a session shows server status and runs OAuth sign-in. `claude mcp list` lists your servers.
- **ClickUp's hosted MCP server.** ClickUp documents the endpoint `https://mcp.clickup.com/mcp` and this Claude Code command: `claude mcp add --transport http clickup https://mcp.clickup.com/mcp`. After adding it, run `/mcp` in a session to complete authentication. Verified: [ClickUp developer docs](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1). The setup page doesn't list the server's tools, so check them under `/mcp` before trusting it as read-only.
- **Keeping tier 4 read-only with permission rules.** Verified: [Claude Code permissions docs](https://code.claude.com/docs/en/permissions).
  - Rules match MCP tools as `mcp__<server>` (every tool on that server), `mcp__<server>__*` (same, as a wildcard) or `mcp__<server>__<tool>` (one tool).
  - Put any tool that creates, edits or deletes into `permissions.deny` in your settings. Use the real tool names shown under `/mcp`.

  ```json
  {
    "permissions": {
      "deny": ["mcp__clickup__<write_tool_name>"]
    }
  }
  ```
- **CLAUDE.md guides Claude but doesn't enforce anything.** Verified: [Claude Code memory docs](https://code.claude.com/docs/en/memory).
  - CLAUDE.md loads as context each session, and Claude isn't guaranteed to follow it, especially vague or conflicting instructions. So test the lookup order instead of assuming it works.
  - Anything that must run at a fixed point, or be blocked whatever Claude decides, belongs in a hook or a permission rule.
  - `/context` lists which memory files actually loaded.
- **Keeping the block small.** The docs suggest staying under about 200 lines per CLAUDE.md. `@imports` still load at launch, so they don't save context. Rules in `.claude/rules/` with `paths` frontmatter load only when matching files are read, and skills load only when invoked or judged relevant. Both are options if the lookup procedure grows. Verified: [memory docs](https://code.claude.com/docs/en/memory) and [skills docs](https://code.claude.com/docs/en/skills).
- **Auto memory has a "reference" type.** Verified: [memory docs](https://code.claude.com/docs/en/memory).
  - Claude Code's auto memory can save *reference* notes about where to find information outside the project, such as an issue tracker or dashboard.
  - It's stored per project outside the repo, at `~/.claude/projects/<project>/memory/`.
  - This note's view: such notes can supplement an explicit lookup order but shouldn't replace it. Claude decides for itself what goes into auto memory, and it isn't visible to other agents.
- **A connected tier 4 costs little context until it's used, but its results can be large.** Verified: [Claude Code MCP docs](https://code.claude.com/docs/en/mcp).
  - Tool search is on by default. MCP tool definitions are deferred, and only tool names and server instructions load at session start.
  - Claude Code warns when a single MCP tool result is over 10,000 tokens. The default cap is 25,000 tokens, adjustable with `MAX_MCP_OUTPUT_TOKENS`.
  - This note's view: a context map helps on both counts. Claude calls the right tool with a precise target instead of running broad searches whose results flood the context window.
- **Scheduled lookups in Cowork.** Verified: [Claude Help Center — Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).
  - Cowork scheduled tasks now run remotely, so they keep to schedule while the computer sleeps or the app is closed, using connectors.
  - A task that needs local files or apps runs only locally.
  - This note's inference: a scheduled briefing that reads a context map from a local folder, as Simon Pittman's briefer reads his About Me files ([42:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2538s)), depends on an awake machine. Put the map somewhere a remote task can reach, or accept that the task runs locally.

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]]. The key sections are context vs connections and the lookup-order example ([26:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1603s)–[28:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1727s)), plus the Level 1 routing rules ([04:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=283s)–[05:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=321s)).
- [[Simon Pittman - Set Up Claude Cowork]]. The connectors and context-map section ([23:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=1402s)–[31:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1871s)), the session-start reading list in his global instructions ([18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)–[18:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1133s)), and the scheduled weekly briefer ([42:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2521s)–[42:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2542s)).
- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]. The external-vault wiki path in Herk2's CLAUDE.md ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s)–[14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s)).

## Related

- Concepts: [[Context vs Connections]] · [[CLAUDE.md as a Router]] · [[Design for Retrieval]] · [[Second Brain Levels]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[LLM Wiki]] · [[Claude Code Auto Memory]] · [[Tool-Agnostic Context Files]] · [[Always-On Brain OS]]
- Techniques: [[Build a Level 1 Second Brain]] · [[Ingest Sources into an LLM Wiki]] · [[Port a Claude Code Brain to Other Agents]] · [[Add Semantic Search to One Folder]] · [[Build a Knowledge Graph Layer]] · [[Second Brain Pain-Point Audit]] · [[Grill Me Interview Skill]]
- More: [[Connecting Claude to External Tools]] · [[Build a Context Map for a Connected Tool]] · [[Set Up Claude Cowork]] · [[Permissions and Approval Gates]]
- Tools: [[Claude Code]] · [[OpenAI Codex]] · [[Hermes Agent]] · [[GBrain]] · [[Claude Cowork]]
- People: [[Nate Herk]] · [[Simon Pittman]]
- Sources: [[Nate Herk - Every Level of a Claude Second Brain]] · [[Simon Pittman - Set Up Claude Cowork]]
- [[Home]]
