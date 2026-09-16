---
type: technique
goal: "Add two chat modes to a markdown second brain: a journal that saves each exchange and answers from your wiki and past entries, and a personal CRM with one file per person, both routed by trigger words in CLAUDE.md"
difficulty: beginner
time_to_build: "About an hour on top of a working wiki (vault estimate, not from the video)"
sources: ["[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Nate Herk - Every Level of a Claude Second Brain]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]", "[[Obsidian]]"]
tags: [topic/second-brain, topic/memory, topic/claude-code, topic/privacy, topic/prompting]
---

# Add a Journal and Personal CRM to a Second Brain

## Goal

[[Matt Wolfe - Second Brain Wiki with Journal and CRM]] builds this in [[OpenAI Codex]]. On top of a Karpathy-style [[LLM Wiki]] he adds two layers:

- **A journal.** Each entry is saved, and the replies draw on everything you've saved.
- **A personal CRM.** You update and query it in plain chat.

One instruction file sends each message to the right layer, based on how the message starts. This note adapts the build for [[Claude Code]].

**Why he built it.** Most second brains are storage where information goes to die [00:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=55s). The journal is the layer where you actually use what you've saved [03:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=207s).

## Use when

- **Your saved material never comes back to you.** Matt wants journal replies to cite videos you saved weeks ago, not give generic chatbot advice [04:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=287s).
- **You journal regularly.** He journals nearly every day [01:57](https://www.youtube.com/watch?v=yke4fLQUsh4&t=117s).
- **You forget where you met people and what you talked about** [01:26](https://www.youtube.com/watch?v=yke4fLQUsh4&t=86s).
- **Your contact list is personal-sized.** [[Nate Herk - Every Level of a Claude Second Brain]] thinks a large CRM across many businesses would justify a graph [20:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1203s) (see [[Knowledge Graphs]]).

Matt expects the wiki and journal to help most people, so the CRM is optional [02:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=156s).

## Prerequisites

- **A working wiki with an index and a log, opened as the Claude Code project.** Matt's has raw/, wiki/, index.md, log.md and an instruction file [11:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=707s). To build one, see [[Bootstrap an LLM Wiki from the Karpathy Gist]] or [[Ingest Sources into an LLM Wiki]].
- **Optionally, [[Obsidian]] on the same folder** for checking results.
- **A decision about where this data may go.** Read the next section and the Pitfalls first.

## Settle the conflict first

**Nate's rule, from [[Context vs Connections]].** Don't ingest volatile data such as customer data; keep it reachable instead [27:31](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1651s). Only keep what will still help in a year [27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s).

**Matt does the opposite.** Contact details and what he knows about each person [23:15](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1395s) live in the vault, along with every journal exchange.

*This note's way to reconcile them (not either creator's):*

| Kind of data | What to do |
|---|---|
| How you met, shared history, what someone cares about | Passes the one-year test. Keep it in the person file |
| Job titles, open deals, anything your contacts app or a real CRM already holds | Fails it. Note where it lives instead of copying it |
| Journal entries | Dated records, but noise for general questions. Read them only in journal mode |

## Steps

1. **Create the folders.** Matt adds journal/ and CRM/ beside the wiki [21:43](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1303s). *Vault layout:* `journal/` and `crm/`, each with its own `index.md`.
2. **Add the journal rules.** Matt asks the agent to write them into its instruction file [21:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1309s):
   - **What gets saved.** A chat that starts with "journal" becomes a new file [21:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1315s) containing the entire conversation [22:03](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1323s).
   - **Naming and indexing.** The agent picks a short title and names the file date plus title [22:11](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1331s). It adds that to the journal's own index [22:19](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1339s) and a summary to log.md [22:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1344s).
   - **What replies draw on.** The wiki [22:29](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1349s), the model's own knowledge [22:40](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1360s), past entries and the CRM [22:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1367s).
3. **Add the CRM rules.**
   - **Trigger.** Tell the agent something is for the CRM, and it updates or adds that person [23:05](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1385s).
   - **Files.** Each file is named after the person [23:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1392s).
   - **Index.** People are listed alphabetically with a short bio [23:30](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1410s), so you can ask questions about your contacts [23:35](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1415s).
4. **Keep plain questions as the default.** One chat now has three modes. A normal question queries the wiki, "journal" as the first word starts an entry, and saying it's for the CRM updates the CRM [23:42](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1422s).
5. **Port the rules to Claude Code.** Matt says Claude Code or Cowork also works [32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s), but his rules live in AGENTS.md. *Vault step:* either put the modes block below into `CLAUDE.md`, or import AGENTS.md (see Beyond the source).
6. **Test the CRM.**
   - Send "add to CRM", a name and where you met [24:47](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1487s). Leave out real contact details while testing; Matt skipped them on camera [25:08](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1508s).
   - Expect a person file with summary, contact details, how you met and relationship context [25:26](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1526s), plus an index row [25:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1536s).
   - Then ask where you met them [25:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1549s).
7. **Test the journal.** Start a new chat with "journal" and a brain dump [26:07](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1567s).
   - **Before answering,** Matt's agent read the indexes [27:04](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1624s).
   - **The reply** cited wiki pages [27:36](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1656s) and mixed in general advice [27:50](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1670s).
   - **The file** held the entry, the reply, a synthesis and related content [28:06](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1686s).
8. **Tune the rules, not the outputs.** Edit the instruction file; in his words, it's all just prompts [31:55](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1915s).
9. **Optional: add the pattern pass he promised.** Matt wanted the journal to spot struggles that keep coming back [05:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=321s), but his demo had no earlier entries [27:15](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1635s). *Vault step:* use the weekly prompt below.

## Starter files & prompts

*Vault starter content written for this note, not Matt's wording.*

**CLAUDE.md modes block**

```markdown
## Modes (decide from the first line of my message)
- Starts with `journal` → Journal mode.
- Says it's for the CRM, or starts with `crm:` → CRM mode.
- Anything else → Wiki query: read wiki/index.md, answer from linked pages, cite them.
  Don't open journal/ or crm/ unless I ask.

## Journal mode
1. Read wiki/index.md, journal/index.md and crm/index.md; open only relevant pages.
2. Before replying, create journal/YYYY-MM-DD-short-title.md with my entry verbatim.
3. Reply: what seems to be going on; advice grounded in wiki pages and past entries
   (link each); then general advice, labelled as general.
4. Append your reply and later turns of this chat to the same file.
5. Add a row to journal/index.md: date | [[title]] | one-sentence summary.
6. Append to log.md: date, "journal", title. No entry text in the log.
7. Never copy journal content into wiki/ pages.

## CRM mode
1. Check crm/index.md for the person (nicknames, spellings). Update if found;
   otherwise create crm/Firstname Lastname.md from crm/_template.md.
2. Add new facts under the right heading, dated. Mark superseded facts; don't delete.
3. Store only what I tell you. Don't look people up on the web.
4. Keep crm/index.md alphabetical: [[Name]] | one-line bio | last updated.
5. Append to log.md: date, "crm", name, created or updated.
6. For recall questions, cite the file, and say when it doesn't cover the question.
```

**Person template: `crm/_template.md`**

```markdown
---
type: person
aliases: []
first_met: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
# Firstname Lastname

## Summary
Who they are to me, in one or two lines.

## How we met
- YYYY-MM-DD · event or call · context

## Relationship context
- What they care about, what we discussed, what I offered or promised.

## Contact
- Where current details live (e.g. phone contacts). Copy here only if nothing else holds them.

## Open threads
- YYYY-MM-DD · follow-up. Delete when done.
```

**Weekly pattern prompt**

```text
Read the eight newest entries in journal/index.md. List up to three themes that appear
in at least two, each with the entry links and one wiki page that speaks to it.
Write no files unless I reply "save".
```

## Done when

- [ ] A plain question gets a wiki answer and opens nothing in journal/ or crm/.
- [ ] A "journal" chat makes one dated file, one index row and one log line, and the reply links a wiki page.
- [ ] Adding the same person twice updates one file instead of creating a second.
- [ ] "Where did I meet X?" names the right event and cites the person file.
- [ ] `/context` lists CLAUDE.md under Memory files.
- [ ] You've decided how journal/ and crm/ are handled in backups and in other projects that read this vault.

## Pitfalls

- **Personal data leaves your machine without a decision.** Matt sends contact details and journals through a hosted model and never mentions it. Nate warns that whatever you process through Claude goes to Anthropic [21:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1293s). See Beyond the source.
- **Hourly jobs over everything.**
  - Matt's hourly job [29:34](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1774s) ends by pushing the whole vault to main [31:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1888s).
  - Limit any scheduled prompt to raw/.
  - Add `journal/` and `crm/` to `.gitignore`, or back them up somewhere else.
- **Journal leaking into answers.** Journal mode reads the wiki and CRM by design. Only an explicit rule keeps ordinary queries out of the journal.
- **Duplicate people.** Files are named by person (step 3), so a nickname and a full name become two files unless the agent checks the index first.
- **Slide features that were never built.** Matt's slides promise more than the video builds:
  - meeting-note import [03:18](https://www.youtube.com/watch?v=yke4fLQUsh4&t=198s)
  - pattern detection (step 9)
  - linking people to ideas [05:37](https://www.youtube.com/watch?v=yke4fLQUsh4&t=337s)
- **Other people's data.** Your contacts never agreed to be in the CRM. *Vault advice:* store only what you'd be comfortable showing them.

## Variations

- **Skills instead of router rules** (vault suggestion). Move each mode's steps into a `/journal` or `/crm` skill and keep one routing line in CLAUDE.md. See [[Agent Skills]].
- **A different third layer.** Matt suggests clients, workouts, research papers, recipes or sales calls [02:21](https://www.youtube.com/watch?v=yke4fLQUsh4&t=141s).

## Beyond the source

*Not in the videos. Checked 2026-09-15 at the links given.*

- **CLAUDE.md, not AGENTS.md.**
  - Claude Code reads CLAUDE.md. To reuse Matt's AGENTS.md, start CLAUDE.md with `@AGENTS.md` and put Claude-only rules below it. A symlink also works.
  - The docs advise keeping CLAUDE.md under about 200 lines and moving multi-step procedures into skills.
  - https://code.claude.com/docs/en/memory
- **Where journal chats go.**
  - **Consumer plans** (Free, Pro, Max, including Claude Code): a setting decides whether your data trains models. Retention is 5 years with it on, 30 days with it off.
  - **Team, Enterprise and API:** no training under commercial terms, and 30-day standard retention.
  - **On your machine:** Claude Code keeps session transcripts in plaintext under `~/.claude/projects/` for 30 days by default (`cleanupPeriodDays`).
  - https://code.claude.com/docs/en/data-usage
- **Fence off the private folders from other projects.**
  - In a project that reads this vault, add deny rules such as `Read(//Users/you/brain/journal/**)`. Deny is checked before allow.
  - They cover Claude's file tools and shell commands it recognises, such as `cat`. They don't stop scripts that open files themselves; use the sandbox for that.
  - https://code.claude.com/docs/en/permissions

## Sources

- [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]: the build, the rules, the three modes and both demos.
- [[Nate Herk - Every Level of a Claude Second Brain]]: the context-vs-connections objection, the privacy warning and his point that a big CRM needs a graph.

## Related

- **Concepts:** [[Context vs Connections]] · [[LLM Wiki]] · [[CLAUDE.md as a Router]] · [[Design for Retrieval]] · [[Tool-Agnostic Context Files]] · [[Agent Skills]] · [[Knowledge Graphs]]
- **Techniques:** [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Ingest Sources into an LLM Wiki]] · [[Schedule Recurring Claude Tasks]] · [[Port a Claude Code Brain to Other Agents]]
- **Tools and people:** [[Claude Code]] · [[OpenAI Codex]] · [[Obsidian]] · [[Matt Wolfe]] · [[Nate Herk]]
- [[Home]]
