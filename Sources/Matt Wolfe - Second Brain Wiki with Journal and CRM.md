---
type: source
title: "Build An AI Second Brain Knowledge Base (Step-By-Step)"
creator: "[[Matt Wolfe]]"
channel: "Matt Wolfe"
url: https://www.youtube.com/watch?v=yke4fLQUsh4
video_id: yke4fLQUsh4
published: 2026-05-06
duration: "33:56"
ingested: 2026-09-15
topics: [LLM Wiki, Karpathy gist bootstrap, Obsidian Web Clipper, raw inbox, journal, personal CRM, trigger-word modes, scheduled ingest, GitHub backup, OpenAI Codex]
tags: [source/youtube, topic/second-brain, topic/memory, topic/retrieval, topic/automation, topic/scheduling, topic/privacy, topic/portability]
---

# Matt Wolfe - Second Brain Wiki with Journal and CRM

> **Creator:** [[Matt Wolfe]] · **Published:** 2026-05-06 · **Length:** 33:56 · [Watch on YouTube](https://www.youtube.com/watch?v=yke4fLQUsh4)

> [!note] Built in OpenAI Codex, not Claude
> Everything here runs in [[OpenAI Codex]], with GPT-5.5 picked for the scheduled job. [[Claude Code]] and [[Claude Cowork]] get one sentence saying they work too ([32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s)). The system is just folders plus an instruction file, so it ports to Claude Code almost unchanged, with one catch he never mentions. His rules live in AGENTS.md, but Claude Code reads CLAUDE.md. Add a CLAUDE.md that imports `@AGENTS.md` (see *Beyond the source* and [[Port a Claude Code Brain to Other Agents]]). Codex Automations map to Claude Code Desktop scheduled tasks or cloud routines (see [[Routines and Scheduled Tasks]]).

## TL;DR

Matt Wolfe builds an [[LLM Wiki]] second brain in the style of [[Andrej Karpathy]], live and click by click.

- **Setup.** An empty [[Obsidian]] vault becomes a Codex project. The agent scaffolds it from Karpathy's gist.
- **Growth.** Obsidian Web Clipper feeds the vault. The wiki grows by processing raw clips and by saving answers back as pages.
- **His additions.** A journal whose replies draw on the wiki, past entries and contacts, and a markdown personal CRM. Cue words in a chat message decide which one runs.
- **Automation.** An hourly unattended job ingests new clips, then commits and pushes the vault to a private GitHub repo.

Some features on his opening slides are never built (see Caveats).

## Key takeaways

- **Storage alone doesn't help; resurfacing does.** Saved content just sits there unless something brings it back, and the grounded journal is his way of doing that [00:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=55s). See [[Design for Retrieval]].
- **Put the knowledge base at the centre and add layers around it.** Swap the CRM for clients, workouts, recipes or sales calls [02:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=141s).
- **Treat the gist as a spec and keep the build minimal.** Handing Codex the gist link produced 51 files. One prompt to build only what the gist explicitly calls for pruned it back [11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s). See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **Questions grow the wiki.** With no extra setup, the agent read the index, answered, and saved the reusable part as a new linked page [18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s).
- **Fix the schema, not each output.** Raw files piling up, metadata in the wrong place and orphan pages were all fixed by editing the ingest steps in AGENTS.md and then reprocessing [20:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1218s). See [[CLAUDE.md as a Router]].
- **One project chat has three modes.** A plain question queries the wiki, "journal" as the first word runs the journal procedure, and saying it's for the CRM updates the CRM [23:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1422s). See [[Add a Journal and Personal CRM to a Second Brain]].

## The system at a glance

| Layer | Files | Trigger | What the agent does | Shown |
|---|---|---|---|---|
| Capture | raw/ | Web Clipper, note location "raw" | Nothing yet: files wait | [12:56](https://www.youtube.com/watch?v=yke4fLQUsh4&t=776s) |
| Ingest | raw/ → wiki/, index.md, log.md, raw/processed/ | "process the files in raw", or the hourly job | Create or update pages, cross-link them to the source, add the channel name to the source's frontmatter, update the index and log, move the source to processed | [20:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1202s) |
| Query | wiki/, index.md | Any ordinary question | Read the index, answer from pages, save the reusable answer as a page | [18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s) |
| Journal | journal/ + its own index | Chat starts with "journal" | Save the whole exchange as a date-plus-title file, add an index row and a log line, and reply using the wiki, past entries, the CRM and model knowledge | [21:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1315s) |
| CRM | CRM/ (one file per person) + index | Say the info is for the CRM | Create or update the person's file; keep an alphabetical index with short bios; log the change | [23:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1387s) |
| Automation | Codex automation | Hourly | Process unprocessed raw files, then commit and push to main | [29:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1752s), [31:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1888s) |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=yke4fLQUsh4&t=0s) Intro

- He shows a second brain you can chat with. It holds saved videos, articles, tweets and podcasts, and has a CRM and a journal that draws on the wiki [00:00](https://www.youtube.com/watch?v=yke4fLQUsh4&t=0s).
- Most second brains are dumping grounds you never go back to [00:41](https://www.youtube.com/watch?v=yke4fLQUsh4&t=41s).

### [01:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=67s) The System Overview

- **Three pillars** [01:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=68s):
  - a wiki of web content
  - a CRM of people he meets: how and where, what they discussed, and contact details such as email, phone and address [01:46](https://www.youtube.com/watch?v=yke4fLQUsh4&t=106s)
  - a daily journal about good days, bad days and business dilemmas [01:57](https://www.youtube.com/watch?v=yke4fLQUsh4&t=117s)
- Inputs differ from person to person. The wiki and journal help the most people, and the CRM is optional [02:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=156s).
- **Architecture sketch** [02:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=167s):
  - knowledge lives in Obsidian, and web content arrives through a clipper
  - CRM notes and Granola meeting notes also flow in [03:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=198s)
  - the journal is where you interact with it all [03:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=207s)
- **Planned AI layer:**
  - summarise each source into key points [03:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=233s)
  - extract people, companies, tools, ideas and themes into their own pages [04:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=245s)
  - auto-link related notes, Zettelkasten style [04:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=267s)
- **Planned journal behaviour:**
  - replies cite specific saved videos instead of giving generic chatbot advice [04:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=287s)
  - spot struggles that keep coming up across entries [05:23](https://www.youtube.com/watch?v=yke4fLQUsh4&t=323s)
  - link people to ideas, companies and conversations [05:37](https://www.youtube.com/watch?v=yke4fLQUsh4&t=337s)

### [08:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=483s) Karpathy LLM Wiki Concept

- He credits the LLM knowledge-base idea to Karpathy, including using Obsidian as the front end. His own additions are the journal and CRM [08:10](https://www.youtube.com/watch?v=yke4fLQUsh4&t=490s).

### [08:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=507s) Tools Needed

- **Codex:** his current tool of choice. The free ChatGPT plan gives some usage, and a paid plan gets more out of it [08:35](https://www.youtube.com/watch?v=yke4fLQUsh4&t=515s).
- **Obsidian:** a free markdown organiser [08:45](https://www.youtube.com/watch?v=yke4fLQUsh4&t=525s).
- **Obsidian Web Clipper:** linked at the bottom of obsidian.md [08:56](https://www.youtube.com/watch?v=yke4fLQUsh4&t=536s). On a YouTube page it pulls in the full transcript [09:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=556s).

### [09:41](https://www.youtube.com/watch?v=yke4fLQUsh4&t=581s) The Buildout

1. **Vault.** Create a vault called "second brain" in a folder of the same name, note where it lives, and delete the welcome note [09:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=582s).
2. **Project.** In Codex, add a new project, choose "use an existing folder" and pick the vault folder. The vault and the project are now the same directory [10:19](https://www.youtube.com/watch?v=yke4fLQUsh4&t=619s).
3. **Scaffold.** Ask Codex to build the architecture from Karpathy's LLM Wiki gist link, saying this empty folder is the Obsidian vault [11:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=663s). It ran about five minutes and made 51 files [11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s). A follow-up prompt told it to strip the extras [11:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=698s).
4. **Result** [11:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=707s):
   - raw/ holds the immutable sources, with raw/assets for optional attachments
   - wiki/ holds the AI-written pages
   - AGENTS.md defines the ingest and query operations [12:22](https://www.youtube.com/watch?v=yke4fLQUsh4&t=742s)
   - index.md is the catalogue and log.md the change record [12:39](https://www.youtube.com/watch?v=yke4fLQUsh4&t=759s)
5. **Clipper settings** [12:56](https://www.youtube.com/watch?v=yke4fLQUsh4&t=776s):
   - the vault name must match Obsidian's exactly
   - the default template must point at that vault
   - properties: source title, URL, created date and a web-clip tag. The created date is when you clip, not when the piece was published [13:26](https://www.youtube.com/watch?v=yke4fLQUsh4&t=806s)
   - note location: raw [13:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=822s)
6. **First clips.** He starts with Karpathy's page itself, on purpose [13:52](https://www.youtube.com/watch?v=yke4fLQUsh4&t=832s), then adds a discipline video. Nothing happens until you tell the agent to process raw [14:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=858s).
7. **Metadata gap.** The clipper misses the YouTube channel name, so he tells Codex to add it to frontmatter during processing [15:04](https://www.youtube.com/watch?v=yke4fLQUsh4&t=904s).
8. **First ingest.** Two sources took about three minutes. The raw files stay put, and the wiki gains concept pages [15:32](https://www.youtube.com/watch?v=yke4fLQUsh4&t=932s). The agent renamed the clickbait-titled source "Discipline without willpower" [16:25](https://www.youtube.com/watch?v=yke4fLQUsh4&t=985s).
9. **Seeding.** More videos from his watch history took about six minutes [17:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1058s). Pages link across sources, for example to a Riley Brown video on Codex [18:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1083s).

### [18:19](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1099s) Querying the Wiki

- He opens a new chat and asks for motivation tips on hard tasks [18:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1101s). The agent says it will read the index first, answer from what's captured, and add the reusable part back [18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s).
- The grounded answer came with edits to index.md and log.md [18:54](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1134s), plus a new "motivation for hard tasks" page that links to its sources [19:15](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1155s).

### [19:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1168s) Manually Updating the Agent

- **Processed queue.** Processed files were piling up in raw/ [19:35](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1175s). He creates raw/processed [19:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1184s).
  - The existing ingest steps: read the source, create or update pages, update related entity, concept, topic, overview, synthesis and comparison pages, update the index, append to the log [20:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1202s).
  - He adds a sixth step that moves the source to processed [20:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1218s).
- **Channel name.** Codex had put the channel name on the generated wiki page. He rewrites the rule so it goes on the original source page [20:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1234s).
- **No orphans.** A new step after step 3 cross-links every generated or updated page back to its source [21:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1268s).
- **Two ways to edit.** Edit AGENTS.md by hand, or prompt the agent to change it [21:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1281s).

### [21:25](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1285s) Letting AI Update the Agent & Building Journal / CRM

He creates journal/ and CRM/ folders [21:43](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1303s) and prompts Codex to add rules to AGENTS.md.

- **Journal rules:**
  - A chat that starts with "journal" is saved [21:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1315s), and the entire conversation goes into the file [22:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1322s).
  - The journal folder gets its own index [22:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1325s).
  - The agent picks a short title, and the filename is the date plus that title [22:11](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1331s).
  - The title and a summary go into log.md [22:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1344s).
  - Replies are grounded in the wiki [22:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1349s) and also draw on past entries, the CRM and the model's own knowledge [22:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1367s).
- **CRM rules:**
  - When he says information is for the CRM, the agent creates or updates that person [23:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1387s).
  - Each file is named after the person [23:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1392s) and holds contact details, how and where they met, and what he knows about them [23:17](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1397s).
  - An index lists people alphabetically with a short bio [23:30](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1410s).
- **Result.** AGENTS.md now has wiki, journal and CRM sections. The journal index has date, entry and summary columns; the CRM index has person and summary [24:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1461s).

### [24:46](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1486s) Testing the CRM

- He types "add to CRM" with a name and three meetings: a Qualcomm event in 2024, CES 2025 and a lunch at TechCrunch Disrupt 2025 [24:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1487s). He leaves contact details out on camera [25:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1508s).
- The agent makes a person file with sections for summary, contact details, how they met and relationship context [25:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1524s). It also adds an index row and a log entry [25:38](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1538s).
- Asked where they first met, it checks the CRM records and answers correctly [25:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1549s).

### [26:01](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1561s) Testing the Journal

- **Entry.** A new chat starts with "journal", followed by a brain dump: he skips video ideas for fear of low views and is torn between clickbait and literal titles [26:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1567s).
- **Before replying.** The agent reads the indexes and writes the journal file first [27:04](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1624s). It finds creator-strategy pages, no earlier entries and nothing relevant in the CRM [27:13](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1633s).
- **Reply.** It names two fears tangled together, creative integrity and channel safety [27:22](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1642s). It cites wiki pages that treat visible metrics as lagging indicators [27:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1656s) and mixes in general model advice [27:50](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1670s).
- **Saved.** The file holds the entry, the reply, a synthesis and related content [28:06](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1686s). The index row has the date, title and a one-paragraph summary [28:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1696s).

### [29:11](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1751s) Automating The Wiki Linking

Despite the title, this chapter is about scheduled processing, not linking.

- **Reprocess first.** He has Codex reprocess everything in raw/ under the new rules [28:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1727s). Files move to processed and sources gain channel names [29:06](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1746s).
- **New automation** [29:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1752s):
  - title "process second brain raw files"
  - worktree set to local, so it runs directly in the project [29:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1767s)
  - schedule: hourly [29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s)
  - prompt: process any unprocessed files in raw [29:41](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1781s)
  - model: GPT-5.5. He advises the strongest model you have [29:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1789s), with reasoning set to high [29:52](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1792s)
- **Daily routine.** Clip something and it's ingested within the hour. For CRM notes or journaling, open a new chat [30:04](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1804s).

### [30:30](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1830s) Backing it all up to GitHub

1. Create a private repo [30:39](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1839s).
2. Ask Codex to commit the current version to that repo's URL [30:48](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1848s). This needs the GitHub plugin attached in Codex [30:58](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1858s). His push worked [31:11](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1871s).
3. Extend the automation prompt: after processing, commit and push to main. The result is an hourly backup [31:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1888s).

### [31:41](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1901s) Recap and Final Thoughts

- To change how it behaves, open Obsidian, which he calls the "visibility layer", and edit AGENTS.md. In the end it's all just prompts [31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s).
- The graph view shows the growth. After the first ingest he says he likes watching it spread and interconnect as the vault grows [16:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1004s). By the recap it's visibly more connected [32:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1927s), and he shows a much denser vault as what a few days or weeks of use produce [32:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1936s).
- A possible refinement: separate folders, with instructions to break people and companies out of each piece of content [32:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1962s).
- He says it's simpler than it looks and gets smarter over time [33:15](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1995s).

## Caveats & disagreements

- **Promised but not built.**
  - Granola meeting import [03:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=198s).
  - Category pages for people, companies and tools [04:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=245s). Concept pages and a Hermes Agent page do appear [17:52](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1072s), but breaking people and companies out into their own folders is later offered only as an idea [32:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1962s).
  - Journal pattern detection [05:23](https://www.youtube.com/watch?v=yke4fLQUsh4&t=323s). The demo had no earlier entries to find patterns in [27:13](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1633s).
- **No lint pass.** Karpathy's gist includes a lint health check (see *Beyond the source*). The video never runs one; the orphan rule covers only part of it [21:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1268s).
- **Unattended ingest vs staying in control.**
  - Matt ingests whatever lands in raw/ every hour, with no review [29:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1752s).
  - [[Nate Herk - Every Level of a Claude Second Brain]] warns that auto-ingesting risks too much context [26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s). Nate likes being in full control of what goes in [26:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1583s). [[Ingest Sources into an LLM Wiki]] builds that stance in with a propose-then-wait step.
  - Matt's approach makes capture effortless; Nate's keeps noise out.
  - *This note's middle path:* schedule the job, but have it log every page it writes so you can review the log.
- **CRM data in the vault vs [[Context vs Connections]].**
  - Nate says to leave volatile data such as customer records in its own system and only reach for it [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s). His test is whether it will still be useful in a year [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s).
  - Matt stores contact details and relationship notes as markdown [23:17](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1397s) and plans to pipe in meeting notes [03:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=198s).
  - *This note's reconciliation:* where and how you met someone passes the one-year test. Fast-changing client details and meeting logs look more like connections.
  - Nate also thinks a large business CRM would justify a graph [20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s). Matt's small personal CRM works as flat files. See [[Knowledge Graphs]].
- **Privacy.** Contact details and personal journal entries all pass through OpenAI, and he never raises it. Nate flags that hosted models receive your data [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s).
- **Cost.** He runs the strongest model at high reasoning every hour [29:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1789s). [[Schedule Recurring Claude Tasks]] advises the cheapest model that does the job; see also [[Choosing a Claude Model]].
- **Git.** Every hour the job pushes straight to main with no review [31:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1888s). He doesn't discuss .gitignore or secrets.
- **What Obsidian is for.** Matt works in Obsidian, even editing the schema there [31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s). Nate calls it only a viewer [09:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s) that he rarely opens [10:13](https://www.youtube.com/watch?v=DTCyvo6cC54&t=613s). See [[Obsidian]].
- **Scaffold method.** [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] pastes the gist's full text into Claude Code [07:14](https://www.youtube.com/watch?v=sboNwYmH3AY&t=434s). Matt pastes only the link, and Codex over-builds.
- **Promotions omitted.** A sponsor segment for a hosting company's managed OpenClaw plan (06:14–08:01) and an end-of-video channel plug are left out.

## Build from this

- **Scaffold from the gist, then prune:** [[Bootstrap an LLM Wiki from the Karpathy Gist]]
- **Raw inbox with a processed queue, source metadata, orphan-free links and answers filed back:** [[Ingest Sources into an LLM Wiki]]
- **Journal and CRM layers with trigger words and an index per layer:** [[Add a Journal and Personal CRM to a Second Brain]]
- **Hourly ingest and backup with Claude:** [[Schedule Recurring Claude Tasks]]. A local vault suits a Desktop scheduled task.
- **One vault for both Claude Code and Codex:** [[Port a Claude Code Brain to Other Agents]], [[Tool-Agnostic Context Files]]
- **Move the three modes into skills so the router file stays short:** [[Workflow Audit into Skills]]

Vault starter content for a Claude Code port:

```markdown
@AGENTS.md

## Claude Code
- First word "journal" → journal procedure. "For the CRM" → CRM procedure. Otherwise → wiki query.
- Scheduled runs: commit to a claude/ branch, never push to main.
```

## Resources mentioned

- Karpathy's announcement post: https://x.com/karpathy/status/2039805659525644595
- Karpathy's LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Obsidian: https://obsidian.md/
- Obsidian Web Clipper: https://obsidian.md/clipper
- Codex app: https://chatgpt.com/codex/
- **Named only:** the Codex GitHub plugin [30:58](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1858s) and Granola [03:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=198s).

## Beyond the source

*Not in the video. Checked 2026-09-15 at the links given.*

- **CLAUDE.md vs AGENTS.md.** Claude Code reads CLAUDE.md, not AGENTS.md. The docs recommend a CLAUDE.md that imports `@AGENTS.md`, optionally with Claude-specific rules below it, or a symlink. https://code.claude.com/docs/en/memory
- **The gist's operations.** It defines three operations: ingest, query and lint. It explicitly suggests filing good query answers back as pages, which Matt's agent did. Lint checks for contradictions, stale claims and orphan pages. The gist also recommends Obsidian Web Clipper. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Codex Automations today.** OpenAI's docs now call the feature scheduled tasks.
  - Local tasks need the computer on and the app running.
  - Local mode runs in your main checkout and can change files you're editing. Worktrees keep a task's changes separate.
  - Model and reasoning can stay at defaults or be set per task.
  - https://learn.chatgpt.com/docs/automations?surface=app
- **Codex models today.** GPT-5.5 is now listed as the previous-generation flagship. The GPT-5.6 family and Astra are listed above it. https://learn.chatgpt.com/docs/models
- **Claude equivalents.**
  - *Desktop scheduled tasks* run locally with access to your files, but only while the app is open and the machine is awake. You can choose the permission mode, model and an isolated worktree for each task. https://code.claude.com/docs/en/desktop-scheduled-tasks
  - *Cloud routines* run while your computer is off, from a fresh clone of a GitHub repo. The minimum interval is one hour. Claude pushes to `claude/`-prefixed branches, and pushes to protected branches are rejected. https://code.claude.com/docs/en/routines
  - *This note's reading:* clips saved locally never reach a cloud routine unless they're committed first, so a Desktop task fits Matt's setup better.
- **Capturing the channel at clip time.** Web Clipper templates support variables such as `{{author}}`, `{{published}}`, schema.org and meta-tag values. These could fill the missing channel field when you clip. Whether `{{author}}` returns the channel on YouTube wasn't tested here. https://obsidian.md/help/web-clipper/variables
- **Transcript clipping can break.** A third-party write-up reports that YouTube UI changes in early 2026 broke transcript extraction in Web Clipper templates (unverified beyond that report). https://noahkarsky.com/2026/04/11/obsidian-youtube-clipper-breakdown.html

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "Carpathy", "Andre Karpathy", "Carpathys'" | Andrej Karpathy |
| "agents.md" | AGENTS.md |
| "Anthropic's co-work", "Claude code" (32:59) | Claude Cowork, Claude Code |
| "Chrome web clipper" | Obsidian Web Clipper (browser extension) |
| "Aaron Miller study" / "Aaron Merrill study" (15:56–16:03) | channel of the discipline video; *unclear in captions* |
| "Creator, update the contact record" (23:21) | create or update the contact record |
| "YouTube value of death" (27:36) | probably a wiki page titled "YouTube Valley of Death" (likely) |
| "moved to process" (29:06) | moved to raw/processed |
| "automations" (29:14) | Codex app Automations, now documented as scheduled tasks |
| "Hermes agent", "TechCrunch disrupt" | Hermes Agent, TechCrunch Disrupt |

## Related

- **Home:** [[Home]]
- **Concepts:** [[LLM Wiki]] · [[Second Brain Levels]] · [[Design for Retrieval]] · [[Context vs Connections]] · [[Agent Memory Patterns]] · [[CLAUDE.md as a Router]] · [[Tool-Agnostic Context Files]] · [[Routines and Scheduled Tasks]] · [[Always-On Brain OS]] · [[Knowledge Graphs]] · [[Agentic OS]] · [[Choosing a Claude Model]]
- **Techniques:** [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Ingest Sources into an LLM Wiki]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Schedule Recurring Claude Tasks]] · [[Port a Claude Code Brain to Other Agents]] · [[Workflow Audit into Skills]]
- **Tools:** [[OpenAI Codex]] · [[Obsidian]] · [[Claude Code]] · [[Claude Cowork]] · [[Hermes Agent]] · [[OpenClaw]]
- **People:** [[Matt Wolfe]] · [[Andrej Karpathy]] · [[Nate Herk]]
- **Sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] · [[Chase AI - The Agentic OS Setup for Claude Code]]
