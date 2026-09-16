---
type: technique
goal: "Stand up a working LLM Wiki from an empty folder: have the agent scaffold it from Karpathy's gist, prune it to the minimum, feed it with Obsidian Web Clipper, query it with answers filed back, and keep it healthy with a hot cache, lint and (optionally) scheduled ingest with a Git backup."
difficulty: beginner
time_to_build: "About an hour to a first ingested source (the videos show ~5 minutes to scaffold and 3–10 minutes per ingest); scheduled ingest and backup add about 30 minutes (estimate, not from the videos)"
sources: ["[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]"]
tools: ["[[Claude Code]]", "[[Obsidian]]", "[[OpenAI Codex]]"]
tags: [topic/second-brain, topic/retrieval, topic/memory, topic/claude-code, topic/automation, topic/scheduling]
---

# Bootstrap an LLM Wiki from the Karpathy Gist

## Goal

Get a working [[LLM Wiki]] without designing the structure yourself. Give the agent Karpathy's idea file and a short wrapper prompt, then prune what it builds.

[[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] points out there is no repo to copy. You ask Claude Code to read the idea and implement it ([05:11](https://www.youtube.com/watch?v=sboNwYmH3AY&t=311s)).

## Use when

- **You're starting from an empty folder.** If you're extending an existing Level 1 brain, use [[Ingest Sources into an LLM Wiki]] instead.
- **What you save never comes back to you.** Matt says most second brains are just where information goes to die ([00:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=53s)).
- **You expect hundreds of pages, not millions of documents** ([17:10](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1030s)).

## Prerequisites

- **[[Obsidian]]**, which is free. Nate calls it optional ([06:03](https://www.youtube.com/watch?v=sboNwYmH3AY&t=363s)). Matt treats it as his "visibility layer" ([31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s)).
- **An agent that works inside a folder.** Nate uses [[Claude Code]]. Matt uses [[OpenAI Codex]] and says Claude Code or Cowork also work ([32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s)).
- **Karpathy's gist.**
- **A privacy decision.** Anything you ingest goes to the model provider. [[Nate Herk - Every Level of a Claude Second Brain]] suggests open-source models for client data ([21:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1305s)).

## Steps

1. **Create the vault.**
   - Nate uses Manage Vaults → create new → name → location ([06:32](https://www.youtube.com/watch?v=sboNwYmH3AY&t=392s)).
   - Matt also notes the folder path and deletes the welcome note ([10:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=607s)).
2. **Open the folder in your agent.**
   - Nate runs `claude` in VS Code's terminal so he can see the status line ([07:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=424s)).
   - Matt adds a Codex project on the existing folder ([10:22](https://www.youtube.com/watch?v=yke4fLQUsh4&t=622s)).
3. **Say what the wiki is for** before you ingest anything: a personal second brain or a research dump ([09:37](https://www.youtube.com/watch?v=sboNwYmH3AY&t=577s)). Nate's two vaults came out in different shapes because their purposes differed ([05:34](https://www.youtube.com/watch?v=sboNwYmH3AY&t=334s)).
4. **Hand over the gist with a wrapper.**
   - Nate pastes the full gist plus a wrapper telling Claude to implement it as his second brain, guide him step by step and create the CLAUDE.md schema ([07:31](https://www.youtube.com/watch?v=sboNwYmH3AY&t=451s)).
   - Matt gives the URL and says the folder is the empty vault ([11:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=663s)).
   - A starter wrapper is below.
5. **Prune to the minimum.**
   - Matt's first build came out at 51 files. He told Codex to keep only what Karpathy's plan explicitly calls for ([11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s)). That left raw/, wiki/, the schema file, index.md and log.md ([11:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=713s)). Nate's unpruned scaffold had the same core files ([08:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=505s)).
   - It also added default wiki/ subfolders (analysis, concepts, entities, sources), which he says to revisit once content arrives ([07:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=474s)). His personal wiki is flat; his YouTube wiki uses subfolders ([08:04](https://www.youtube.com/watch?v=sboNwYmH3AY&t=484s)).
6. **Point Web Clipper at raw/.**
   - Change its location from "Clippings" to raw ([10:22](https://www.youtube.com/watch?v=sboNwYmH3AY&t=622s)).
   - Matt's template settings:
     - the vault name must match Obsidian exactly ([13:02](https://www.youtube.com/watch?v=yke4fLQUsh4&t=782s))
     - properties for source title, URL, clip date and a web-clip tag ([13:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=801s))
     - note location set to raw ([13:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=822s))
   - It captures YouTube transcripts ([09:16](https://www.youtube.com/watch?v=yke4fLQUsh4&t=556s)) but not the channel name ([14:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=893s)).
7. **Watch the first ingest.**
   - Nothing happens until you ask ([14:20](https://www.youtube.com/watch?v=yke4fLQUsh4&t=860s)).
   - Nate's agent first asked what to emphasise and how granular to be ([10:35](https://www.youtube.com/watch?v=sboNwYmH3AY&t=635s)). One long article became 23 linked pages in about 10 minutes ([11:59](https://www.youtube.com/watch?v=sboNwYmH3AY&t=719s)).
   - Matt's two sources took about 3 minutes ([15:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=934s)).
8. **Fix the schema while it's small.** Matt's changes:
   - move processed files to raw/processed ([20:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1218s))
   - put source metadata on the source page ([20:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1259s))
   - link every new page back to its source ([21:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1268s))
   - then reprocess raw/ under the new rules ([28:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1727s))

   Details are in [[Ingest Sources into an LLM Wiki]].
9. **Query, and file answers back.** Matt's agent checks the index, answers, and saves the reusable part as a page linked to its sources, updating the index and log ([18:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1109s)). The starter rule below adds an approval step.
10. **Add a hot cache, for assistant-style vaults only.** Nate's personal brain keeps hot.md, roughly 500 words or characters covering the latest material ([14:44](https://www.youtube.com/watch?v=sboNwYmH3AY&t=884s)). His YouTube wiki doesn't need one ([14:57](https://www.youtube.com/watch?v=sboNwYmH3AY&t=897s)). He doesn't show how the file is updated.
11. **Lint regularly.** Nate relays Karpathy's checks: inconsistent data, gaps filled by web search, and new article candidates, run daily or weekly ([15:08](https://www.youtube.com/watch?v=sboNwYmH3AY&t=908s)). A pass may ask you for more sources ([15:25](https://www.youtube.com/watch?v=sboNwYmH3AY&t=925s)).
12. **Optional: schedule ingest and backup.**
    - Matt's hourly local Codex automation processes any unprocessed raw files ([29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s)). It uses the strongest model at high reasoning ([29:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1789s)).
    - It then commits and pushes to main in a private GitHub repo ([31:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1884s)).
    - Vault suggestion: in Claude, use a Desktop local scheduled task (see Beyond the source), and only after a week of supervised ingests.
13. **Point other projects at the wiki.**
    - Another project can crawl the wiki because the vault's CLAUDE.md explains how it works ([13:23](https://www.youtube.com/watch?v=sboNwYmH3AY&t=803s)).
    - Nate's assistant reads the hot cache, then the index, then a domain sub-index, then searches. It's told not to read the wiki unless it needs to ([13:50](https://www.youtube.com/watch?v=sboNwYmH3AY&t=830s)–[14:13](https://www.youtube.com/watch?v=sboNwYmH3AY&t=853s)).
    - He says this cut tokens compared with in-project context files, but gives no figures ([14:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=866s)).

## Starter files & prompts

*Vault starter content. Neither video shows the full text of its prompts or schema.*

**Wrapper prompt:**

```text
Below is an idea file describing the LLM Wiki pattern. Build a minimal version in this folder,
which is my Obsidian vault and is currently empty. Purpose: <research on ... | second brain>.
- Create only what the idea file explicitly calls for: raw/, wiki/, index.md, log.md and a
  CLAUDE.md describing ingest, query and lint. No example pages, scripts or extra folders.
- Propose any wiki/ subfolders and wait for my OK.
- raw/ is read-only for you, except moving processed files into raw/processed/.
- Finish by listing every file you created and how I add my first source.

<full gist text>
```

**Target tree:**

```text
my-wiki/
├── CLAUDE.md        # schema (or just `@AGENTS.md` if Codex shares the vault)
├── index.md         # one line per page
├── log.md           # ingests, queries, lint passes
├── raw/             # Web Clipper lands here; never edited
│   └── processed/
└── wiki/
    └── hot.md       # optional, assistant-style vaults only
```

**Schema additions:**

```markdown
## Query
- Read wiki/hot.md (if present), then index.md, then only matching pages.
- If the answer is reusable, propose a page (title, source links, index line); write it after I agree, and log it.

## Hot cache
- After each ingest or substantial conversation, rewrite wiki/hot.md: at most ~400 words, newest first,
  each line linking the page it touched. Drop items older than 14 days or already captured in a page.
```

**Lint prompt:** "Lint the wiki. Report only; don't fix anything. List: contradictions; superseded claims; pages with no source link or no inbound links; index lines pointing at missing files; topics that appear on three or more pages but have no page of their own. List anything you need from me. Append a summary to log.md."

**Scheduled task prompt:** "If raw/ (excluding raw/processed/) has files, ingest up to five, oldest first, following CLAUDE.md. Leave volatile material (chat threads, email, statuses) in raw/ and note it in log.md. Commit as `ingest: <titles>`. If raw/ is empty, do nothing."

**Consuming project block:**

```markdown
## External wiki: ~/vaults/my-wiki
- Use only for facts about <domains> this project lacks. Read wiki/hot.md → index.md → matching pages.
- Don't open it for: <tasks>. Never write to it from here.
```

## Done when

- [ ] The vault matches the target tree, with nothing extra
- [ ] A Web Clipper save lands in raw/, not Clippings
- [ ] One supervised ingest produced linked pages, index lines and a log entry
- [ ] Every generated page links to its source page
- [ ] A test question opens index.md first, and a reusable answer becomes a page only after you approve it
- [ ] A lint report is logged
- [ ] If Codex and Claude Code share the vault, CLAUDE.md imports AGENTS.md
- [ ] (Optional) A scheduled run processed a new clip, and the vault is committed to a private repo

## Pitfalls

- **Over-building.** Matt's first build had 51 files ([11:31](https://www.youtube.com/watch?v=yke4fLQUsh4&t=691s)). Prune before the first ingest.
- **Clips in the wrong folder.** The clipper saves to Clippings by default, so ingest never sees them ([10:26](https://www.youtube.com/watch?v=sboNwYmH3AY&t=626s)).
- **Metadata on the wrong page.** Codex put the channel name on the generated page until Matt fixed the rule ([20:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1234s)).
- **Noise from unattended ingestion.** Matt's hourly run has no review step. [[Nate Herk - Every Level of a Claude Second Brain]] controls ingest by hand because too much context can do more harm than good ([26:17](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1577s)). Vault note: hourly runs on the strongest model cost money, and pushing straight to main leaves nothing to review.
- **Scale.** Nate's April chart says wikis don't scale to enterprise size and millions of documents need RAG ([16:51](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1011s)). By June he says wikis start to degrade at some point ([11:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=707s)). [[Chase AI - The Three-Step Claude Code Agentic OS]] claims 99.9% of people need no vector database ([11:02](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=662s)). None of them measures it.
- **A schema Claude Code can't see.** If the rules live only in AGENTS.md, Claude Code won't read them (see Beyond the source).

## Variations

- **Journal and CRM layers.** Matt adds modes that a chat's opening words select ([23:44](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1424s)). See [[Add a Journal and Personal CRM to a Second Brain]].
- **One folder per domain, or raw/wiki/output.** Chase allows either ([10:35](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=635s)). The stage-split build is in [[Ingest Sources into an LLM Wiki]].
- **A channel's back catalogue in one batch.** 36 transcripts took Nate about 14 minutes ([11:54](https://www.youtube.com/watch?v=sboNwYmH3AY&t=714s)); see [[Ingest Sources into an LLM Wiki]].

## Beyond the source

*Not from the videos. Checked at the linked pages on 2026-09-15.*

- **The gist** calls itself deliberately abstract. It:
  - recommends Web Clipper
  - files good answers back into the wiki
  - calls the wiki a git repo of markdown
  - allows batch ingest
  - suggests adding search (qmd) beyond about 100 sources and hundreds of pages

  Neither it nor Karpathy's post covers flat versus nested folders or a hot cache; the flat preference Nate credits to Karpathy is unverified. [Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **Karpathy's post** gives about 100 articles and 400K words. Nate said half a million ([02:58](https://www.youtube.com/watch?v=sboNwYmH3AY&t=178s)). [FxTwitter readout](https://api.fxtwitter.com/karpathy/status/2039805659525644595).
- **Web Clipper** is a free, official extension for Chromium browsers, Firefox, Safari and Edge ([help](https://obsidian.md/help/web-clipper)).
  - Templates set the vault and note location, which defaults to "Clippings" ([obsidian.md/clipper](https://obsidian.md/clipper)).
  - Official variables have no transcript field, but a community YouTube template adds `{{transcript}}` and fills a channel property from the page's structured data ([template](https://github.com/obsidian-community/web-clipper-templates/blob/main/templates/youtube-with-transcript-clipper.json)).
- **AGENTS.md in Claude Code.** Claude Code reads CLAUDE.md. A CLAUDE.md containing `@AGENTS.md` imports that file at session start ([memory docs](https://code.claude.com/docs/en/memory)).
- **Claude equivalent of Matt's automation** ([docs](https://code.claude.com/docs/en/desktop-scheduled-tasks)):
  - *Desktop local scheduled tasks.* Hourly preset; model, permission mode and worktree set per task. They run only while the app is open and the computer is awake. Missed runs are skipped, with one catch-up when the computer wakes.
  - *Cloud routines.* Start from a fresh clone with no local files. The minimum interval is 1 hour.
- **Codex today.** "Automations" are now scheduled tasks; ones that need local files require the computer on and the app running ([OpenAI docs](https://learn.chatgpt.com/docs/automations?surface=app)).

## Sources

- [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] ([01:02](https://www.youtube.com/watch?v=sboNwYmH3AY&t=62s)–[17:22](https://www.youtube.com/watch?v=sboNwYmH3AY&t=1042s))
- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] ([00:53](https://www.youtube.com/watch?v=yke4fLQUsh4&t=53s)–[32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s))
- [[Nate Herk - Every Level of a Claude Second Brain]] · [[Chase AI - The Three-Step Claude Code Agentic OS]] (cautions only)

## Related

- [[LLM Wiki]] · [[Ingest Sources into an LLM Wiki]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Agent Memory Patterns]] · [[Routines and Scheduled Tasks]] · [[Schedule Recurring Claude Tasks]] · [[Port a Claude Code Brain to Other Agents]] · [[Tiered Lookup Routing]]
- [[Obsidian]] · [[Claude Code]] · [[OpenAI Codex]] · [[Andrej Karpathy]] · [[Nate Herk]] · [[Matt Wolfe]]
- [[Home]]
