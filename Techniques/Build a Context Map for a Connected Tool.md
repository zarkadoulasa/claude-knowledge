---
type: technique
goal: "Have Claude explore a connected tool once and write a short map of what exists and where things live. Then point your instructions at that map, so Claude goes straight to the right place instead of searching blind."
difficulty: beginner
time_to_build: "30–60 minutes for a first map and tests (estimate, not from the video)"
sources: ["[[Simon Pittman - Set Up Claude Cowork]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]"]
tools: ["[[Claude Cowork]]", "[[Claude Code]]", "[[Obsidian]]"]
tags: [topic/mcp, topic/context, topic/retrieval, topic/cowork, topic/prompting]
---

# Build a Context Map for a Connected Tool

## Goal

A connector gives Claude access to a tool, but it doesn't tell Claude how your workspace is organised. A context map fills that gap. It's a small markdown file that lists:

- which databases, folders or lists exist
- what each one holds
- how to reach the things you usually ask about

Your instructions tell Claude to read the map before it searches that tool.

In [[Simon Pittman - Set Up Claude Cowork]] the map is `my-context-map.md`, covering his Notion workspace. When he loads it, Claude describes it as a sat nav for the workspace ([30:09](https://www.youtube.com/watch?v=pl90LATQlHI&t=1809s)).

## What the video shows

| | Before the map | After the map |
|---|---|---|
| Setup | Notion connected through its MCP server, which can query, read and write ([28:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1717s)) | `my-context-map.md` in the About Me folder, referenced from global instructions ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s), [29:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1796s)) |
| Test | Find a named project in the projects database ([28:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=1706s)) | List tasks due this week from the tasks database ([30:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1823s)) |
| Result | Found it, but only after quite a few attempts ([28:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1733s)) | Went straight to the right database ([30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)) |

How he builds it:

- **Why Notion needs a map.** Notion is where he keeps projects, knowledge, meeting notes and specialist knowledge bases ([27:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=1663s)). Email and calendar hold messages and meetings; Notion holds context ([28:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=1692s)).
- **Entry point.** Copy the link to a top-level Notion page that contains all your databases. Ask Claude to read it and create a context map of the system ([29:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=1766s), [29:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1775s)).
- **Where it lives.** In the About Me folder with his other context files ([29:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1763s)). The map breaks down his workspace so Claude can find things more easily ([29:52](https://www.youtube.com/watch?v=pl90LATQlHI&t=1792s)).
- **Wiring it in.** He asks Claude for updated CLAUDE.md text that references the map, so the map is always consulted and kept up to date ([29:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1796s), [30:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=1802s)). He says you'd then paste that text into global instructions ([30:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1818s)); the demo doesn't show it before the retest.
- **Other tools.** Make a map for whatever system holds your plans, projects, notes or knowledge ([30:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1844s), [30:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1849s)). The same approach works for Google Docs or Obsidian ([31:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=1894s)).
- **Fewer tokens.** Claude stops burning credits hunting for things ([31:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=1866s)).

**How strong is the evidence?** The demo map was one he'd made earlier with a previous version ([29:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1780s), [30:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=1816s)). The before/after is one query each.

## Use when

- Claude needs several searches in a tool you've connected, or keeps asking where something lives ([28:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1733s)).
- The tool's structure isn't obvious from names alone: many databases, nested folders, spaces and lists, or house naming conventions.
- Scheduled tasks or requests sent from your phone need to find things while you're away.

**Not the fix when:**

- **The content is local files Claude can already list and read.** [[Ras Mic - How AI Agents and Claude Skills Work]] makes the same point about code: don't describe what the agent can check for itself ([02:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=147s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). A router in your instructions file is enough there. See [[CLAUDE.md as a Router]].
- **The answer lives in a thread or record that changes weekly.** The map should say where that lives, not store it. See [[Context vs Connections]].
- **You need an ordered fallback across several sources.** Combine the map with [[Tiered Lookup Routing]].

## Prerequisites

- **The tool is connected.** In Cowork, use Customize › Connectors. In Claude Code, add an MCP server. See [[Connecting Claude to External Tools]].
- **You have read access to everything you want mapped.** The connector only sees what your account can see (*Beyond the source*).
- **One entry point exists**, or you're willing to create one: a hub page, a root folder or a top-level space.
- **You have somewhere to keep context files and instructions you can edit.** Simon uses an `about-me/` folder; see [[Set Up Claude Cowork]].

## Steps

1. **Take a baseline.** Ask three questions you really ask about this tool. For each, note how many searches it took and whether Claude found the right place. Simon's baseline: several attempts to find one project page ([28:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1733s)).
2. **Check permissions.** Building a map only needs read access. If the connector can also write, as Notion's can ([28:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1720s)), put its write tools behind approval where your plan allows. See [[Permissions and Approval Gates]].
3. **Pick the entry point.** Simon uses a Notion hub page linking every database ([29:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=1766s)). He says to map whatever system you use ([30:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1844s)). This note's suggestions for other tools:
   - **Google Drive:** the top-level shared folders.
   - **ClickUp:** the workspace's spaces, folders and lists.
   - **Obsidian:** the vault root or its index note.
4. **Have Claude explore and draft.** Use the map-building prompt below. It records structure and purpose, not content.
5. **Review the draft by hand.** Correct wrong descriptions. Add naming conventions and "for X, look in Y" rules that only you know. Remove anything sensitive.
6. **Save it with your other context.** Use `about-me/my-context-map.md` as Simon does ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s)). If you map several tools, use `context/maps/<tool>.md`.
7. **Wire it into your instructions.** Ask Claude to write the instruction lines, as Simon did ([29:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1796s)). Paste them into global instructions or CLAUDE.md. The starter block below loads the map only when that tool is in use.
8. **Retest in a fresh session.** Ask the baseline questions again. It passes when the first search lands in the right database or folder, as his tasks query did ([30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)).
9. **Add a refresh rule.** Put a "Last checked" date in the map. Tell Claude to flag it whenever the tool no longer matches the map. Optionally, schedule a monthly check ([[Schedule Recurring Claude Tasks]]).

## Starter files & prompts

*Vault starter content written for this note. Simon's own prompt and full map aren't shown on screen.*

### Map-building prompt (Notion)

```text
Here's the link to my Notion hub page: <link>. Using the Notion connector, read it and every
database and page it links to, one level down. Don't change anything.

Write about-me/my-context-map.md using the template below. For each database or top-level page,
record: name, link or ID, what it holds, the properties that matter for finding things
(status, owner, dates, tags), how items are named, and 2–3 example questions it answers.
Record structure only: no task contents, client details or statuses.
List anything you couldn't open under "Couldn't access".
Finish by suggesting the lines I should add to my instructions so you read this map before
searching Notion.
```

### Generic version (Drive, ClickUp, Obsidian, SharePoint…)

```text
Explore <tool> through its connector, starting at <entry point>. Read only.
Map the top two levels: what each <folder / space / list / database> is for, how things inside
are named, and where the things I ask about most live: <3–5 examples>.
Save it as context/maps/<tool>.md using the template. Mark anything you're unsure of with (?)
so I can check it.
```

### Map template

```markdown
# Context map: <Tool> (<workspace name>)
_Last checked: yyyy-mm-dd · Entry point: <link or path> · Connector: <name>_

## How to use this map
- Read this before searching <Tool>. Go straight to the location below; search only if it isn't listed.
- If the tool doesn't match this map (renamed, moved, missing), tell me and propose an edit.
  Don't quietly work around it.

## Quick routes
| When I ask about…          | Go to                       | Find by                             |
|----------------------------|-----------------------------|-------------------------------------|
| My tasks this week         | Tasks database <link>       | Due date = this week, Assignee = me |
| A project's status         | Projects database <link>    | Name; Status property               |
| Meeting notes with <name>  | Meetings database <link>    | Attendees; Date                     |
| How we do <process>        | Knowledge › SOPs <link>     | Title starts with "SOP –"           |

## Locations
### Projects (database) <link>
- Holds: one row per client or internal project
- Key properties: Status (Not started / Active / Done), Owner, Deadline
- Naming: `<Client> – <Project>`
- Related: Tasks, via the Project relation

### Tasks (database) <link>
- …

## Conventions
- Dates are … · Archive lives in … · <Old database> is retired; don't use it

## Couldn't access
- …
```

### Instruction block

```markdown
## Connected tools
- Before searching Notion, read `about-me/my-context-map.md` and use its Quick routes.
- Search the tool only when the map has no route, then suggest a route to add.
- The map describes structure. Never copy records, statuses or messages into it.
- If the map looks out of date, tell me and propose the edit.
```

### Refresh prompt

```text
Check about-me/my-context-map.md against Notion now, read only. List what's new, renamed, moved
or gone. Show me the edited map for approval, then update the Last checked date.
```

### Test prompts

| Prompt | Pass if |
|---|---|
| "What tasks do I have due this week?" (Simon's test, [30:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1823s)) | The first call goes to the tasks location named in the map |
| "What's the status of <project>?" | Claude opens the projects location directly, with no workspace-wide search |
| "Where do we keep <process> docs?" | Claude answers from the map without calling the tool |
| "Find <something not in the map>" | Claude says it isn't mapped, searches, then offers to add a route |
| The first question again, in a new session | Same direct route, which shows the instruction loaded |

## Done when

- [ ] The map file has a Last checked date, an entry point and a Quick routes table
- [ ] You have opened every mapped link or path yourself
- [ ] The map holds no record contents, client personal data or statuses
- [ ] Your instructions tell Claude to read the map before searching that tool
- [ ] In a fresh session, the baseline questions hit the right place on the first search
- [ ] The connector's write tools are blocked or need approval, where your plan allows
- [ ] A refresh date or reminder exists

## Pitfalls

- **Stale maps.** Workspaces get reorganised. A wrong route is worse than none, because Claude trusts it. Simon reuses a map he built with an earlier version ([30:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=1816s)); that's fine if you've checked it, risky if not. Keep the Last checked date and the rule to speak up when things don't match.
- **The map turns into a data dump.** An instruction to keep the map updated ([30:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=1802s)) can drift into logging task details. Keep contents in the tool and only routes in the map. After his task triage, Claude also wrote what it learned into memory ([31:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1911s)), which is the same kind of drift. See [[Context vs Connections]].
- **Always loaded means always paid for.** Simon's instructions make the map something Claude always looks at ([30:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=1802s)). [[Ras Mic - How AI Agents and Claude Skills Work]] points out that always-loaded text goes along on every turn ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)). He also says output quality drops as the context window fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)). So read the map only when that tool is in play, and keep it to routes. See [[Context Window Management]].
- **Mapping what you can't see.** The connector acts with your permissions (*Beyond the source*). Pages that aren't shared with you won't appear, and Claude may not mention the gap. The template's "Couldn't access" section is there to catch this.
- **Write access while exploring.** Notion's connector can write ([28:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1720s)). Say "read only" in the prompt, and require approval for write tools.
- **Sensitive structure.** Database names, client names and links are information too. Keep the map inside your private workspace, not in a shared repo.
- **Proof from one query.** His before/after is a single demo using a map made in advance ([29:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1780s), [30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)). Run your own baseline so you know the map actually helped.
- **Maps of things Claude can read directly.** For local files and code, a map repeats what Claude can check for itself ([02:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=147s)), and it's one more file to go stale.

## Variations

- **One map per tool.** Keep `context/maps/notion.md`, `drive.md` and `clickup.md`, each loaded only when that tool is used.
- **Map inside a lookup chain.** Put the map's Quick routes into tier 1 of [[Tiered Lookup Routing]], so lookups in the live tool go straight to the right list.
- **Map as a skill.** Wrap the map in a skill whose description names the tool, so it loads only when relevant. This follows Ras Mic's point that only a skill's name and description sit in context until it's needed ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s), [05:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=319s)). See [[Agent Skills]].
- **Scheduled refresh.** A monthly task runs the refresh prompt and leaves the proposed edits for you to review. See [[Schedule Recurring Claude Tasks]] and [[Routines and Scheduled Tasks]].
- **Obsidian or local vaults.** Simon names Obsidian as another fit ([31:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=1894s)). If the vault already sits inside your workspace, a short index note is often enough. Build a full map when Claude reaches the vault through a connector.
- **Claude Code.** Use the same file, referenced from CLAUDE.md, with the tool connected as an MCP server.

## Where the sources meet

- **Simon adds a map because Claude can't see the layout.** In [[Simon Pittman - Set Up Claude Cowork]], the map records where things live in a tool that Claude otherwise has to search ([29:52](https://www.youtube.com/watch?v=pl90LATQlHI&t=1792s), [30:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1844s)).
- **Ras Mic wants only what's unique to you in context.** In [[Ras Mic - How AI Agents and Claude Skills Work]], he argues the model should get what's specific to you, not general knowledge ([32:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1929s), [32:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1933s)). Always-loaded context files are for information that's specific to you ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
- **Read together (this note's view):**
  - A map of your own workspace is exactly that specific-to-you information, because the model can't guess your Notion layout.
  - Ras Mic's point about cost is the reason to keep the map short and load it only when the tool is in use.

## Beyond the source

*Not from either video. Checked 2026-09-15 at the linked pages.*

- **Connectors act with your access.** Claude's access through a connector follows each person's permissions in the connected service. Team and Enterprise owners can set each tool to Always allow, Needs approval or Blocked, for example allowing reads while blocking writes. [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- **Notion's MCP server.**
  - It's hosted by Notion and connected through OAuth.
  - It can search, read, create and update content, limited to content you can access.
  - Workspace admins manage connected MCP clients under Settings › Connections.

  [Notion MCP docs](https://developers.notion.com/docs/mcp)
- **Cowork folder instructions** add project context when you select a local folder, and Claude can update them during a session. They're another place to put the map's "read this first" line. [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)

## Sources

- [[Simon Pittman - Set Up Claude Cowork]]: the Notion connector and context map ([27:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=1650s)–[31:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=1899s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: what belongs in context, and what it costs ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)–[05:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=357s), [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)–[32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).

## Related

- **Techniques:** [[Tiered Lookup Routing]] · [[Set Up Claude Cowork]] · [[Schedule Recurring Claude Tasks]] · [[Build a Level 1 Second Brain]] · [[Keep CLAUDE.md Lean]]
- **Concepts:** [[Connecting Claude to External Tools]] · [[Context vs Connections]] · [[CLAUDE.md as a Router]] · [[Design for Retrieval]] · [[Permissions and Approval Gates]] · [[Context Window Management]] · [[Agent Skills]] · [[Agent Memory Patterns]]
- **Tools:** [[Claude Cowork]] · [[Claude Code]] · [[Obsidian]]
- **People:** [[Simon Pittman]] · [[Ras Mic]]
- [[Home]]
