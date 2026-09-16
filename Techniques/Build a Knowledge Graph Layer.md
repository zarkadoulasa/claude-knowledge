---
type: technique
goal: Add a layer of typed entities and relationships on top of an existing markdown brain so Claude can trace multi-hop relationship chains between people, companies, projects and decisions
difficulty: advanced
time_to_build: 1–3 days including data capture (estimate, not stated in the source)
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]"]
tools: ["[[Claude Code]]", "[[LightRAG]]", "[[Obsidian]]"]
tags: [topic/second-brain, topic/knowledge-graph, topic/retrieval, topic/rag, topic/privacy, topic/claude-code]
---

# Build a Knowledge Graph Layer

> Level 4 of [[Second Brain Levels]]. The routing, wiki and markdown underneath stay as they are. You add a `knowledge-graph/` layer of entities and typed relationships, so relationship questions can follow chains instead of reading whole files.

## Goal

Let the brain answer questions that need several hops, like "how does X trace back to A?" ([03:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=221s)). The layer records typed connections, such as a person working at a company or one company being a competitor of another. It sits next to the existing wiki and context folders ([23:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1391s), [23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)). See [[Knowledge Graphs]] for the concept.

### Wiki links vs graph relationships vs semantic similarity

| | LLM Wiki links (Level 2) | Semantic similarity (Level 3) | Knowledge graph (Level 4) |
|---|---|---|---|
| Kind of connection | "See also" / backlinks. The link says the pages are related, not how ([12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s), [12:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=776s)) | Chunks sit near each other because their meaning is similar ([15:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=947s)) | Typed edges that say how two things relate, e.g. "endorsed by" ([12:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=768s)) |
| How the agent uses it | Follows a trail and reads each page in full ([12:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=742s)) | Retrieves the chunks most similar to the query ([16:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=982s)) | Follows relationships from entity to entity ([24:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1497s)) |
| Cost of a narrow question | Reads whole files. His example: a question that only needed ElevenLabs still meant reading an entire page on AI video production ([24:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1444s)) | Returns just a snippet, which saves time and tokens ([18:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1125s)), but can miss key information ([16:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=997s)) | Sometimes more lightweight in that respect ([24:12](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1452s)) |
| His verdict | Similar effect in practice, but not the same thing ([12:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=778s)) | — | Same data as his Obsidian view, but showing a level of relationships between entities that the Obsidian view doesn't ([24:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1499s)) |

The video opens with this idea as a progression. Notes start forming nodes and entities, then scale into clusters, and finally become "relationship mapping", where you can see how everything fits together ([00:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=4s), [00:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=21s), [00:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=34s)).

## Use when

- **You need to follow chains of relationships or reasoning.** That is his test for Level 4 ([29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s)).
- **Your work is CRM-heavy, with many businesses and clients.** He says a knowledge graph would probably make a lot more sense for that kind of work ([19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s), [20:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1205s)).
- **Narrow questions keep forcing the agent to read whole wiki pages** just to reach one related fact ([24:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1440s)).

### Don't use when

- **Your work is project-based and content-heavy, and routing plus wikis already work.** That describes [[Nate Herk]]'s own work. He has experimented with knowledge graphs a lot but doesn't use them day to day ([19:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1183s), [19:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1192s)).
- **You don't need relationship chains or semantic relationships.** Then you probably don't need a graph ([25:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1516s)).
- **Nothing hurts yet.** Pick the lowest level that fits ([04:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s), [04:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=248s)).
- **You can't justify the cost.** Knowledge graphs are usually the most complex level, and on some platforms the most expensive. Open-source software is an alternative ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s), [19:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1178s)).

## Prerequisites

- **A Level 1–2 foundation.** His Level 4 example project keeps the same shape: a CLAUDE.md with "where things live" routing, a wiki, plain markdown folders and a growing memory file. The knowledge-graph layer is added on top ([23:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1388s), [23:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1399s)). He calls this plain markdown "boring", and says boring is beautiful ([23:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1396s)). See [[Build a Level 1 Second Brain]], [[LLM Wiki]] and [[CLAUDE.md as a Router]].
- **Enough data.** This is the real bottleneck. Graph software is usually good at building the relationships. The problem you have to solve is giving it enough data ([20:24](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1224s), [20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)).
- **The Grill Me skill.** It interviews you relentlessly about a topic, writes a brainstorm file, and only stops once it knows everything ([20:56](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1256s), [21:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1262s)). He got it from [[Matt Pocock]] and customised it ([20:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1240s)). He shares his version in his free Skool community under Classroom → YouTube resources ([20:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1246s)): https://www.skool.com/ai-automation-society/about. See [[Grill Me Interview Skill]].
- **A privacy decision about client data** (step 3).
- **A choice of graph software.** He demos [[LightRAG]] and mentions Logseq and what is probably Graphiti (unclear in captions) as other options ([25:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1508s)).

## Steps

1. **Justify it with real multi-hop questions.** Write down five relationship questions you actually ask that the current brain gets wrong, or can only answer by reading many whole files. If you can't find five, stay at Level 2 or 3. His rule: build a graph when you need to follow chains ([29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s)), and skip it otherwise ([25:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1516s)). See [[Second Brain Pain-Point Audit]].

2. **Scope one domain.** Levels apply per folder: one folder can be Level 2 while another is Level 4 ([28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s), [28:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1734s)). Start with the domain that's heaviest on relationships, usually clients and businesses ([19:59](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1199s)). Not everything needs GraphRAG ([18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s)).

3. **Make the privacy decision before any client data goes to a cloud model.** Sending this data through Claude models means it goes to Anthropic, so it isn't private ([21:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1290s), [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s)). Record it as a dated entry in `decisions.md`.

   | Option | What the video says |
   |---|---|
   | Accept cloud processing, knowingly | Nate does this with his own business data and is aware it goes to Anthropic ([21:36](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1296s), [21:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1318s)) |
   | Keep client data out of the Claude-based brain | Maybe Claude Code shouldn't hold the brain that contains every detail about you, your business and your clients ([21:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1309s)) |
   | Open-source or local models | Suggested for anyone uncomfortable sending client data ([21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)). He plans more coverage of local AI ([22:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1330s)) |

4. **Inventory what already exists.** If you decide some area needs a graph, the data is probably already in your project files ([20:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1216s)). List the wiki pages, project files, meeting transcripts and contracts that cover the chosen domain.

5. **Fill the gaps with Grill Me sessions, one per client or business.** Ask it to grill you about client A, then client B, then business A ([21:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1268s)). Feed it files during the interview, such as transcripts and contracts ([21:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1273s), [21:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1276s)). Save each session as a brainstorm file ([21:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1260s)). Then review the files and ask whether they capture all the nuance you carry in your head. Only then blame the AI ([22:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1358s), [22:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1363s)).

6. **Separate lasting facts from data that changes.** Graph long-lived facts, such as who works where, who referred whom, and which company competes with which. Leave Slack threads, emails and live customer records in their own systems. They change constantly and would turn into noise that needs regular cleanup ([27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s), [27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s)). His test: will this still be worth having in a year? ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)). The brain should know where to fetch that data when needed ([28:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1685s)). See [[Context vs Connections]].

7. **Create the `knowledge-graph/` folder: entities plus relationships.** This mirrors his example, where the entities include Jordan (a person) and Acme (a company). Relationships connect them: Jordan works at Acme, Acme is endorsed by Postpilot, and Postpilot is a competitor of Cadently ([23:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1409s), [23:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1414s), [23:40](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1420s)). Those names are fictional demo data. Use the format below.

8. **Optionally, run graph software over the existing files.** He shows LightRAG running over his real second brain. Zooming in reveals typed edges such as "collaborates with" and "builds" ([24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s), [24:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1474s)). He then follows the relationships around one node, a challenge program: it came from YouTube, connects to a community's onboarding process, and was developed by a named person ([24:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1488s), [24:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1494s)). Setup details are under *Beyond the source*.

9. **Route relationship questions to the graph in CLAUDE.md.** Keep the "where things live" routing, which his Level 4 example still has ([23:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1393s)), and add a relationship route. Summaries still go to full files, and live status still goes to the source tool. In his tiered-lookup example he checks his quarterly projects file first (captioned "OTA"; the exact term is unclear), then the wiki and meeting transcripts, and only then ClickUp itself ([28:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1697s), [28:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1707s)). See [[Tiered Lookup Routing]].

10. **Test with multi-hop questions, then keep ingestion deliberate.** Run the test set below. Update the graph as part of each ingest rather than letting it sync automatically. Nate prefers full control over what goes in, and worries that too much context can do more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s), [26:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1585s)). For the always-on alternative, see [[Always-On Brain OS]].

## Starter files & prompts

### Folder layout (example)

The shape follows his Level 4 example project ([22:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1369s), [23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)). The file names are illustrative. The other paths follow the vault's shared starter layout: the base tree in [[Build a Level 1 Second Brain]], `wikis/` and `references/` from [[Ingest Sources into an LLM Wiki]], and `transcripts/` from [[Add Semantic Search to One Folder]].

```text
my-brain/
├── CLAUDE.md                 ← router; gains the relationship-routing block below
├── AGENTS.md                 ← his L4 example includes this copy for other agents (see note below)
├── context/
├── decisions.md              ← step 3 privacy decision goes here as a dated entry
├── projects/
├── wikis/
├── transcripts/
│   └── 2026-08-14-northwind-kickoff.md
├── references/
│   └── contracts/northwind-sow.md
├── brainstorms/              ← Grill Me output, one file per client/business
│   └── client-northwind-bakery.md
└── knowledge-graph/
    ├── README.md             ← schema: entity types + allowed relation verbs
    ├── relationships.md      ← canonical edge list, one row per relationship
    └── entities/
        ├── people/priya-shah.md
        ├── people/tom-okafor.md
        ├── companies/northwind-bakery.md
        ├── companies/crumb-and-co.md
        └── projects/spring-launch-2027.md
```

About `AGENTS.md`: his Level 4 example adds an `AGENTS.md` identical to CLAUDE.md. He notes you can instead reference `@AGENTS.md` inside CLAUDE.md and delete the duplicated text, because the reference pulls that file in ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s), [22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s)). See [[Port a Claude Code Brain to Other Agents]].

### Entity and relationship format

This is an original format for this vault, not the one shown in the video. It uses plain markdown so any agent can read it. The entities below are fictional.

**`knowledge-graph/README.md`** (schema)

```markdown
# Knowledge graph schema

Entity id = <type>/<kebab-name>, e.g. person/priya-shah. One file per entity in entities/<type-plural>/.

Entity types: person, company, project, product, decision, document

Allowed relations (src → tgt). Propose new ones here before using them.
| relation        | from     | to               | meaning                                  |
|-----------------|----------|------------------|------------------------------------------|
| works_at        | person   | company          | current employer                         |
| reports_to      | person   | person           | line manager                             |
| client_of       | company  | company          | src pays tgt                             |
| competitor_of   | company  | company          | symmetric; record once                   |
| endorsed_by     | company  | company/person   | public endorsement or testimonial        |
| referred_by     | company  | person/company   | who introduced src to us                 |
| owns            | person   | project/decision | accountable owner / decision-maker       |
| part_of         | project  | project/company  | sub-project, or project for a client     |
| depends_on      | project  | project/product  | blocked without tgt                      |
| governed_by     | project  | document         | contract/SOW that defines the work       |

Rules: every edge needs evidence (a file path). Mark inferred edges confidence: low.
No volatile facts (open tickets, this week's threads) — link to the live system instead.
```

**`knowledge-graph/entities/people/priya-shah.md`**

```markdown
---
id: person/priya-shah
type: person
name: Priya Shah
aliases: [Priya, P. Shah]
first_seen: 2026-08-14
evidence:
  - transcripts/2026-08-14-northwind-kickoff.md
  - brainstorms/client-northwind-bakery.md
---
# Priya Shah

Head of Marketing at Northwind Bakery. Signs off creative and holds the launch budget.
Prefers async updates; escalates through her CEO only for budget changes.

Edges: see knowledge-graph/relationships.md (search for `person/priya-shah`).
```

**`knowledge-graph/relationships.md`** (one row per edge, easy to grep)

```markdown
# Relationships

| src                        | relation      | tgt                          | since   | confidence | evidence                                          |
|----------------------------|---------------|------------------------------|---------|------------|---------------------------------------------------|
| person/priya-shah          | works_at      | company/northwind-bakery     | 2024    | high       | brainstorms/client-northwind-bakery.md      |
| company/northwind-bakery   | client_of     | company/our-studio           | 2026-08 | high       | references/contracts/northwind-sow.md       |
| company/northwind-bakery   | referred_by   | person/tom-okafor            | 2026-07 | high       | brainstorms/client-northwind-bakery.md      |
| person/priya-shah          | owns          | project/spring-launch-2027   | 2026-08 | high       | transcripts/2026-08-14-northwind-kickoff.md |
| project/spring-launch-2027 | part_of       | company/northwind-bakery     | 2026-08 | high       | references/contracts/northwind-sow.md       |
| project/spring-launch-2027 | governed_by   | document/northwind-sow       | 2026-08 | high       | references/contracts/northwind-sow.md       |
| company/northwind-bakery   | competitor_of | company/crumb-and-co         | —       | low        | brainstorms/client-northwind-bakery.md      |
```

### Grill Me session prompt (step 5)

```text
Use my Grill Me skill. Grill me about client Northwind Bakery.
Goal: capture everything a relationship graph needs about this client.
Cover: every person involved (role, who they report to, who decides what); related companies
(partners, competitors, vendors, who referred them); projects and how they depend on each other;
key decisions and why; contracts and what they govern.
I'm attaching: transcripts/2026-08-14-northwind-kickoff.md and references/contracts/northwind-sow.md.
Ask one question at a time. Don't stop until you could brief a new hire on how everything
about this client connects. Save the result to brainstorms/client-northwind-bakery.md.
```

### Extraction prompt (step 7)

```text
Read brainstorms/client-northwind-bakery.md and every file it references.
Update knowledge-graph/ following knowledge-graph/README.md:
- Create or update one entity file per person, company, project, decision and document. Check aliases
  first so you merge duplicates instead of creating them.
- Add one row per relationship to knowledge-graph/relationships.md using ONLY the allowed relations.
  If you need a new relation, stop and propose it.
- Every row needs an evidence path. Use confidence: low for anything inferred rather than stated.
- Skip volatile facts (open tasks, this week's email or Slack threads). Those stay in their tools.
Report: entities added/changed, edges added, conflicts found, and the gaps I should be grilled on next.
```

### CLAUDE.md routing block (step 9)

```markdown
## Relationship questions → knowledge-graph/

Use the graph when a question is about how people, companies, projects, decisions or documents
connect: "who…", "how is X connected to Y", "what else is affected if…", "which clients share…".

1. Resolve every named thing to an entity id via knowledge-graph/entities/ (check aliases).
2. Follow edges in knowledge-graph/relationships.md hop by hop (max 3 hops unless asked).
   [If graph software is running: query it in its entity/relationship mode instead, then verify here.]
3. Open the evidence files for the edges you rely on before answering. Cite the path of each hop.
4. If no path exists, say "no recorded connection". Never invent an edge.

Not for: summaries of a meeting or document (read the full file in transcripts/, references/ or wikis/);
live status (check the source tool directly); counts or aggregates (use structured data).
```

### Multi-hop test questions (step 10)

| # | Question | Hops | Pass if |
|---|---|---|---|
| 1 | "Who referred Northwind Bakery to us, and have they referred anyone else?" | client → `referred_by` → person → other `referred_by` edges | Names Tom Okafor, lists every other company with that edge, and cites the evidence paths |
| 2 | "If Priya Shah leaves Northwind, which projects lose their owner, and what contract governs them?" | person → `owns` → project → `governed_by` → document | Returns the project and the SOW, with each hop cited |
| 3 | "How is Tom Okafor connected to the spring launch project?" | person ← `referred_by` ← company ← `part_of` ← project | Gives the full path. This is the same kind of chain he follows in LightRAG ([24:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1497s)) |
| 4 | "Do any of our clients compete with each other?" | company → `client_of` / `competitor_of` | Lists the pairs and flags low-confidence edges as such |
| 5 | "Is Crumb & Co connected to Tom Okafor?" (no path exists) | Negative test | Says no recorded connection. No invented edge |
| 6 | "Summarise the Northwind kickoff call." | Routing control | Reads the full transcript file, not the graph |

## Done when

- [ ] Five real multi-hop questions are written down, and the current brain fails them or only answers by reading many whole files
- [ ] The privacy decision (which data, which model) is recorded as a dated entry in `decisions.md`
- [ ] A Grill Me brainstorm file exists for each client or business in scope, with supporting files attached
- [ ] `knowledge-graph/README.md` defines entity types and the allowed relations
- [ ] Entity files and `relationships.md` are populated, and every edge has an evidence path
- [ ] If you use graph software: it has indexed the existing files and shows typed relationships, not just "related to"
- [ ] CLAUDE.md sends relationship questions to the graph, and summaries, live status and aggregates elsewhere
- [ ] Test questions 1–6 pass, each hop is cited, and the negative test returns no invented edge
- [ ] The ingest routine updates the graph whenever new client material arrives

## Pitfalls

- **Cost and complexity.** This is usually the most complex level, and on some platforms the most expensive ([19:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1174s)). Nate, who has experimented with graphs a lot, still runs his day-to-day on routing and wikis ([19:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1187s)).
- **Not enough data.** Graph software builds relationships well, but only from what you give it ([20:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1229s)). Sometimes the bigger problem isn't retrieval but getting what's in your head into the system ([22:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1354s)).
- **Privacy.** Client data processed through Claude goes to Anthropic. Decide before you ingest, and consider open-source models ([21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s), [21:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1308s)).
- **Assuming wiki backlinks already make a graph.** Links show that pages relate, not how they relate ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s), [12:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=774s)).
- **Graphing data that changes often.** Emails, Slack threads and live customer data turn into noise and create monthly cleanup work ([27:35](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1655s), [27:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1659s)).
- **Too much automatically ingested context.** Nate worries that past some point extra context does more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)).
- **Visualisation overload.** Loading his whole brain into the LightRAG view slowed his computer, and he admits he probably used too much data for the demo ([24:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1466s), [24:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1472s)). A striking graph isn't the goal. What matters is whether the system can find the data and give it back to you ([10:00](https://www.youtube.com/watch?v=DTCyvo6cC54&t=600s)).
- **Graphing the whole brain.** Decide per folder ([18:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1085s), [28:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1729s)). In his Level 3 example, context, projects and decisions stay plain markdown ([17:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1058s)), and summaries are more accurate from full files ([17:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1039s)).

## Variations

- **Markdown-only graph.** Claude maintains the entity and relationship files, with no extra infrastructure (this note's suggestion). It resembles the knowledge-graph folder in his Level 4 example ([23:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1405s)).
- **LightRAG over the whole brain.** The approach he demos with his real data ([24:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1456s)).
- **Other graph tools.** He names Logseq and what is probably Graphiti (unclear in captions) as other options, and offers to cover them if viewers want ([25:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1508s)).
- **Always-on (Level 5).** [[GBrain]] by [[Garry Tan]] combines wikis, routing, relationships and tools, and keeps syncing and refreshing memories. He sees it pairing well with [[Hermes Agent]]. In Claude Code you'd have to manage the cron jobs yourself ([25:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1532s), [25:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1541s), [25:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1554s)). See [[Always-On Brain OS]].

## Beyond the source

*Not from the video. Each item was checked against the linked page on 2026-09-15.*

- **What LightRAG is.** It describes itself as a lightweight knowledge-graph RAG framework and an efficient alternative to Microsoft GraphRAG. Install with `pip install "lightrag-hku[api]"` (or `uv tool install "lightrag-hku[api]"`) and start it with `lightrag-server`.
  - Query modes are `naive`, `local` (specific entities), `global` (themes across documents), `hybrid` and `mix`. `mix` is the default.
  - Graph storage options include NetworkX, Neo4j and Memgraph. Vector storage options include NanoVectorDB, Milvus and Qdrant. PostgreSQL is recommended for production.
  - Source: [LightRAG README](https://github.com/HKUDS/LightRAG)
- **LightRAG server and local models.** The server listens on port 9621, with the web UI at `http://localhost:9621/webui` for uploading documents and exploring the graph.
  - Files in the `./inputs` directory can be picked up with the `/documents/scan` endpoint.
  - For fully local processing, set `LLM_BINDING=ollama` and `EMBEDDING_BINDING=ollama` with the matching model and host variables. The docs set `OLLAMA_LLM_NUM_CTX=16384` and say it must exceed `MAX_TOTAL_TOKENS` + 2000.
  - It also exposes an Ollama-compatible chat endpoint (model `lightrag:latest`), where message prefixes such as `/local`, `/hybrid` and `/mix` pick the query mode.
  - Source: [LightRAG API server docs](https://github.com/HKUDS/LightRAG/blob/main/docs/LightRAG-API-Server.md)
- **LightRAG model guidance.** A fast, inexpensive model is enough for entity and relationship extraction, but the query model should be stronger. For local deployment, the README calls Qwen3-30B-A3B-Instruct a reasonable minimum. Pick the embedding model before indexing: changing it later means re-embedding everything, and LightRAG has no re-embedding tool. [LightRAG README](https://github.com/HKUDS/LightRAG)
- **Loading a curated markdown graph into LightRAG.** `rag.insert_custom_kg(custom_kg)` accepts a dict with `entities` (`entity_name`, `entity_type`, `description`, `source_id`), `relationships` (`src_id`, `tgt_id`, `description`, `keywords`, `weight`, `source_id`) and `chunks` (`content`, `source_id`, …). The `relationships.md` columns above map onto these fields: src→`src_id`, tgt→`tgt_id`, evidence→`source_id`, relation→`keywords`. [insert_custom_kg example](https://github.com/HKUDS/LightRAG/blob/main/examples/insert_custom_kg.py)
- **Graphiti.** A framework from Zep for building and querying temporal context graphs for AI agents. It tracks how facts change over time, keeps provenance back to source data, and supports both prescribed and learned ontologies. It needs a graph database: Neo4j, FalkorDB or Amazon Neptune (Kuzu support is deprecated). OpenAI is the default LLM provider, and Anthropic, Gemini, Groq and OpenAI-compatible local servers such as Ollama are also supported. It ships an MCP server. Install with `pip install graphiti-core`. [Graphiti on GitHub](https://github.com/getzep/graphiti)
- **Logseq.** An open-source, privacy-first outliner that works on local Markdown or Org-mode files. It has bidirectional links, a graph view and advanced queries. [Logseq on GitHub](https://github.com/logseq/logseq)
- **GraphRAG** (the term the video uses at [18:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1081s)). Microsoft's GraphRAG is a structured, hierarchical approach to RAG, aimed at private data the model was never trained on. Indexing splits the corpus into TextUnits, extracts entities, relationships and key claims, clusters the graph into communities with the Leiden technique, and writes bottom-up community summaries. [Microsoft GraphRAG docs](https://microsoft.github.io/graphrag/)
- **Querying the markdown graph in Obsidian.** The Dataview plugin treats a vault as a queryable database. It reads YAML frontmatter and inline `Key:: Value` fields and renders TABLE or LIST queries. That lets you browse entity files by type or relation without separate graph software. [Dataview on GitHub](https://github.com/blacksmithgu/obsidian-dataview)
- **Local models.** Ollama runs open models locally. It's the backend LightRAG's server docs use for fully local extraction and embeddings. [ollama.com](https://ollama.com/)
- **Anthropic data use.** On consumer plans (Free, Pro, Max), Claude Code data is used for training only if the model-improvement setting is on. Retention is 5 years with the setting on and 30 days with it off. Under commercial terms (Team, Enterprise, API), Anthropic doesn't train on your prompts or code unless you opt in, and standard retention is 30 days. Either way, prompts and outputs are sent over the network to be processed. That's the core of his privacy point. [Claude Code docs: data usage](https://code.claude.com/docs/en/data-usage)

## Sources

- [[Nate Herk - Every Level of a Claude Second Brain]], mainly the Level 4 chapter ([19:27](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1167s)–[25:25](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1525s)), the Level 2 wiki-vs-graph aside ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)) and Finding Your Level ([29:19](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1759s))

## Related

- Concepts: [[Knowledge Graphs]] · [[Second Brain Levels]] · [[Keyword vs Semantic vs Graph Retrieval]] · [[LLM Wiki]] · [[Context vs Connections]] · [[CLAUDE.md as a Router]] · [[Always-On Brain OS]] · [[Design for Retrieval]]
- Techniques: [[Grill Me Interview Skill]] · [[Second Brain Pain-Point Audit]] · [[Tiered Lookup Routing]] · [[Add Semantic Search to One Folder]] · [[Ingest Sources into an LLM Wiki]] · [[Port a Claude Code Brain to Other Agents]]
- Tools: [[LightRAG]] · [[Claude Code]] · [[Obsidian]] · [[GBrain]] · [[Hermes Agent]]
- People: [[Nate Herk]] · [[Matt Pocock]] · [[Garry Tan]]
- [[Home]]
