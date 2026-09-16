---
type: technique
goal: Audit an always-loaded instruction file (CLAUDE.md, AGENTS.md or Cowork global instructions) down to routes, habit-correcting rules and facts the model can't infer; move everything else to files, routers or skills; measure the token saving; and keep it lean with a correction loop
difficulty: beginner
time_to_build: 30-90 minutes for the first audit, then about 10 minutes a month (estimate, not from the videos)
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tools: ["[[Claude Code]]", "[[Claude Cowork]]", "[[OpenAI Codex]]"]
tags: [topic/claude-code, topic/context, topic/skills]
---

# Keep CLAUDE.md Lean

## Goal

End up with an always-loaded instruction file that holds only three kinds of line:

1. **Routes**: where things live.
2. **Habit rules**: corrections for mistakes you have actually seen the model make.
3. **Facts specific to you** that the model can't work out on its own.

Everything else is deleted or moved somewhere that loads only when needed: a reference file, a department router, a folder index or a skill. The file stays under roughly 200 lines. You know its token cost before and after the audit, and a standing correction loop stops it creeping back up.

Two sources agree on why this matters, from different angles:
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] says the file loads into every conversation and everything in it eats context ([06:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=414s), [07:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=420s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]] frames it as a standing cost: a 1,000-line file of about 7,000 tokens is paid on every run ([04:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=260s), [04:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=264s)).

The concept behind the file is in [[CLAUDE.md as a Router]]. Its "Where sources disagree" section covers whether you need one at all.

## Use when

- **The file is past 150–200 lines.** That is the range Nate keeps his within before he trims ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), [07:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=429s)).
- **`/context` shows memory files eating a noticeable share.** Nate uses `/context` to find what is consuming tokens and then restructure ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)).
- **`/init` produced a codebase dump you never trimmed.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] grades `/init` a C or D and still calls it mid a month later ([04:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=242s), [04:11](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=251s)).
- **Procedures or reference material have crept in**, such as a report format, code-structure rules or a pasted style guide. Ras Mic says a long file probably should be a skill, and names a report format and a way of structuring code as examples ([04:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=272s), [05:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=348s)). Nate routes style guides out to separate files ([07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s)).
- **You're moving to AGENTS.md or [[Claude Cowork]] global instructions.** The same audit applies to whatever text loads every session.

**Don't bother** if you have no file and nothing is going wrong. Ras Mic says most people don't need one ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)), and the Coding Sloth says you could manage without one ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s)).

## Prerequisites

- A project with an existing `CLAUDE.md`, `AGENTS.md` or Cowork global instructions.
- A backup: git, or a copy of the file.
- Somewhere to move procedures: a `.claude/skills/` folder. See [[Agent Skills]] and [[Build a Skill from a Successful Run]].
- 5–10 questions you really ask. The test prompts in [[Build a Level 1 Second Brain]] work for a knowledge project.
- Optional: an Anthropic API key, if you want exact token counts (see Beyond the source).

## What the sources say to cut, keep and move

| Line type (audit tag) | Example | Verdict | Source |
|---|---|---|---|
| Things the model already knows (`KNOWN`) | "write clean code", "use a dollar sign for money" | **Cut** | Ras Mic: don't tell the model things it already knows ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s), [32:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1956s)) |
| Things readable from the code (`DERIVABLE`) | "this codebase uses React", stack lists | **Cut** (code repos) | Ras Mic: Claude Code can check the code ([02:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=147s), [02:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=152s)). No stack lines, because the code is now the context ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)) |
| Facts specific to you, needed most sessions (`UNIQUE`) | a proprietary method, a non-default currency | **Keep** | Ras Mic's exception: proprietary or you-specific information needed every conversation ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)), or a specific currency ([32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)) |
| Rules countering an observed habit (`HABIT`) | no ALL-CAPS UI text, PR language | **Keep** | Coding Sloth: after months you learn the model's habits, and the file is where you counter them ([04:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=258s), [04:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=277s), [04:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=290s)) |
| Volatile state (`STATUS`) | a project's exact progress | **Move to a file, keep a route** | Nate: the always-loaded file needs to know where the status is, not what it is ([07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s)) |
| Reference detail (`REFERENCE`) | style guide, business context, reference docs | **Move to files, keep routes** | Nate: link out to separate files ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s), [07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s)) |
| Multi-step procedures (`PROCEDURE`) | report format, code-structure rules | **Move to a skill** | Ras Mic: load it progressively when needed ([05:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=348s)). Only the name and description sit in context ([03:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=217s)) |
| Lists for one area of work (`AREA`) | every file and skill used for content work | **Move to a department router** | Jay E: one router file per department that lists its skills and reference files ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s)) |
| What a folder contains | long folder-by-folder descriptions | **Move to that folder's `index.md`** | Chase: an index.md at every level says what that level holds ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s), [20:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1245s)) |
| Guardrails (`SAFETY`) | save every working version; never send without checking | **Keep, and back with a real mechanism** | AI LABS adds a save-every-working-version line for unattended loops ([03:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=217s)). Simon puts never-delete/send/publish rules in his instructions ([10:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=617s)). See Beyond the source |
| Pointers (`ROUTE`) | "status lives in `docs/status.md`" | **Keep, never cut without a test** | Nate: routing lets you keep the file lean without losing information ([07:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=435s), [07:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=453s)) |

## Steps

1. **Back up and measure.**
   - Commit or copy the file.
   - Record the line count (`wc -l CLAUDE.md`) and the token cost.
   - In Claude Code, run `/context` and note what the memory files take. That is Nate's tool for finding token bloat ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)).
   - For an exact count, use the script below. Ras Mic measured with OpenAI's tokenizer ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)), which only approximates Claude's count.
   - Write both numbers in the audit log.
2. **Tag every line.** Run the audit prompt below. Claude proposes one tag per line from the table above; you approve. Nothing gets deleted in this pass.
3. **Cut the `KNOWN` lines.** Ras Mic's rule: rely on what the model is already good at, and give it what's unique about you, your workflow and your business ([32:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1933s)).
4. **Cut the `DERIVABLE` lines, but only in code repos.** Stack and framework lines go, because the code already says them ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)). *Vault reading, not a source claim:* in a non-code second brain, the tools you use outside the folder aren't readable from any file, so a short routed note about them can stay. See Variations in [[Build a Level 1 Second Brain]].
5. **Turn each `PROCEDURE` block into a skill.**
   - Ras Mic asks why a report format or code-structure rule would live in the always-on file when the agent can pull it in when needed ([05:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=348s)). In his demo, a 944-token skill costs 53 tokens until it's used ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s), [30:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1857s)).
   - The Coding Sloth says skills can give similar or better results than the file ([05:01](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=301s)).
   - Create `.claude/skills/<name>/SKILL.md` with a description that says when to use it. Claude finds skills by their description, so CLAUDE.md doesn't need to mention them (Beyond the source).
6. **Move `STATUS` and `REFERENCE` detail out, leaving one route line each.**
   - Nate points Claude at separate files so it knows where to look without spending tokens on content it doesn't always need ([07:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=433s), [07:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=453s)). A project's exact status belongs in its own file ([07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s)).
   - Write routes as plain paths in backticks, not `@` imports. Imports load at launch and save nothing (Beyond the source).
7. **If the routes pile up, add a second tier.**
   - **Department routers** ([[Jay E - The ARMS Framework for a Claude Agentic OS]]): CLAUDE.md names the departments so Claude stays inside the relevant files ([12:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=750s)). Each department has its own router listing its skills and reference files ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s), [12:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=773s)). He says routers get the agent to the right file in the fewest steps ([13:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=797s)).
   - **Folder indexes** ([[Chase AI - The Agentic OS Setup for Claude Code]]): an `index.md` per folder, plus a navigation-pattern section in CLAUDE.md that tells Claude which path to follow ([19:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1171s), [22:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1327s)). An index for a folder holding a single file is overkill ([20:29](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1229s)).
8. **Rewrite what stays as one concrete line each.**
   - A `HABIT` line names the habit and what to do instead.
   - A `UNIQUE` fact is stated once.
   - `SAFETY` lines stay, but a line in CLAUDE.md is a request, not a guarantee. See Beyond the source for hooks and git.
9. **Re-measure.** Get under 200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)). Record the new token cost and the saving.
10. **Regression-test routing in a fresh session.**
    - Ask your real questions without naming files. Claude should open the routed file first.
    - Simon's check works on any surface: start a new task and ask how Claude is meant to work with you, then confirm it read the right files ([19:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1175s), [19:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=1190s)).
    - If anything regresses, restore that route line first.
11. **Install the correction loop.** Paste the maintenance block below into the file.
    - Nate's version: when a pushed-back output comes back better, tell Claude to update the skill or CLAUDE.md so the mistake doesn't repeat ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)). He wants new patterns, gotchas and conventions logged over time ([06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s)), with the file trimmed once it passes his cap ([07:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=429s)).
    - Ras Mic's version: when a skill run fails and you've fixed it, have the agent update the skill so it doesn't happen again ([22:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1329s)). Five of those loops made his eight-source report skill reliable ([22:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1354s)).
    - This technique combines the two: Claude proposes a destination before writing anything, and CLAUDE.md gets a line only for a repeated habit.
    - **A tension in Nate's own advice.** In [[Nate Herk - Claude as a One-Person Marketing Team]] he says you'll likely change CLAUDE.md daily or weekly as you learn ([12:43](https://www.youtube.com/watch?v=yCACmFTiCto&t=763s)), and to just tell Claude to add anything important to it ([12:52](https://www.youtube.com/watch?v=yCACmFTiCto&t=772s)). He gives no cap there, unlike his 150–200-line cap in 32 Tricks ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)).
    - **How to reconcile them.** The file his Claude generated was already a lean router: project, owner, and read the context files before writing ([12:31](https://www.youtube.com/watch?v=yCACmFTiCto&t=751s)). Keep his habit of capturing what you learn, but let the maintenance block pick the destination: most lessons go to a context file or skill, and CLAUDE.md only gets what every session needs. Note that "add this to CLAUDE.md" edits the file, while "remember this" goes to auto memory (Beyond the source). → [[Build a Brand-Aware Marketing Project]]
12. **Re-audit on a schedule.** Do it monthly, or whenever the file passes 150 lines. *(Vault suggestion.)* [[Schedule Recurring Claude Tasks]] can run the audit prompt as a reminder.

## Starter files & prompts

> [!note] Vault starter content
> Everything in this section is original wording written for this vault. None of it is a file shown in the videos. Adapt paths and names.

### Audit prompt

```text
Audit CLAUDE.md for leanness. Do not edit any file in this pass.

1. Report its line count, and tell me how to see its token cost with /context.
2. Label every line or block with exactly one tag:
   KNOWN      general knowledge any capable model already has
   DERIVABLE  something you could learn by reading this repo (stack, framework, visible layout)
   UNIQUE     a fact specific to me or this project you could not infer and need in most sessions
   HABIT      a rule that corrects a mistake you have actually made here
   STATUS     state that changes (progress, current sprint, owners, open bugs)
   REFERENCE  detail only some tasks need (style guide, API notes, business background)
   PROCEDURE  a multi-step workflow or an output format
   AREA       a list of files or skills that matters for one area of work only
   SAFETY     a guardrail (commit before risky changes, never send without asking)
   ROUTE      a pointer to where something lives
3. Output a table: line range | tag | proposed action (cut / keep / move to <path> /
   new skill <name> / department router <name>) | one-line reason.
4. For each block you propose moving, draft the one-line route or skill description
   that replaces it.
5. List every ROUTE line and check that its target path exists. Flag broken routes.
   Never propose cutting a ROUTE line.
6. If this folder is not a code repository, do not tag anything DERIVABLE unless it is
   literally written in another file here.
7. Estimate the line count after the changes. Flag anything you are unsure about.
```

### Apply prompt (after you've reviewed the table)

```text
Apply the audit rows I approved: <row numbers>.
- Create each moved file or skill first, then replace the block with its one-line route.
- Use plain paths in backticks for routes, never @imports.
- Leave HABIT, UNIQUE, SAFETY and ROUTE lines untouched unless I approved a rewrite.
- Show me the final CLAUDE.md and its line count, then list the files you created.
```

### Audit log: `docs/claude-md-audit.md`

```markdown
# CLAUDE.md audit log

| Date | Lines before | Lines after | Tokens before | Tokens after | New skills | New routed files | Routing test |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD |  |  |  |  |  |  | pass / fail: <which question> |

## Decisions
- <block> → cut / moved to `<path>` / skill `<name>` — <why>

## Lines restored after the routing test
- <line> — <what broke without it>
```

### Maintenance block to paste into CLAUDE.md

```markdown
## Keeping this file lean
- This file loads every session. Keep it under 200 lines: routes, habit rules and
  facts about this project you can't infer. Nothing else.
- When I correct you and the better version works, propose where the lesson belongs
  before writing anything:
  - how to do a task → the relevant skill
  - reference detail or changing status → the routed file
  - this file → only for a habit that has now happened more than once
  Show me the one-line change and wait for a yes.
- Don't add stack descriptions, general best practice or project status here.
- If an edit takes this file past 180 lines, say so and suggest what to move out.
- Never remove a line under "Where things live" without asking me.
```

### Before and after (fictional project)

**Before**, an excerpt from a 140-line file:

```markdown
# Project: Shopfront

## Tech stack
- Next.js with the App Router, React, TypeScript
- Supabase for auth and Postgres
- Tailwind CSS, deployed on Vercel

## General rules
- Write clean, readable, well-commented code
- Follow accessibility best practices
- Use a dollar sign for prices

## Current status
- Checkout about 70% done; Stripe webhooks failing in staging
- Sprint ends Friday; Maria owns search

## How to write the weekly report
1. Pull merged PRs from the last 7 days
2. Group them by area: checkout, search, admin
3. Write a short friendly summary per area
4. Add a risks section and a next-week section
... (18 more lines)

## Brand voice
... (35 lines pasted from the brand guide)

## Rules
- Never use ALL CAPS in customer-facing text
- PR descriptions in English, even when the issue is written in Greek
- Prices are integers in cents; show them in EUR with the € sign after the number
```

**After** (24 lines):

```markdown
# Shopfront — router

## Where things live
- Status, owners, current sprint → `docs/status.md` (read before planning work)
- Brand voice for any customer-facing copy → `docs/brand-voice.md`
- Payment and webhook notes → `docs/payments.md`
- Weekly report → use the `weekly-report` skill

## Habits to avoid here
- No ALL CAPS in customer-facing text.
- PR descriptions in English, even when the issue is written in Greek.

## Facts you can't infer
- Prices are integers in cents; display as EUR with the € sign after the number.

## Keeping this file lean
(maintenance block from above)
```

**What changed, and why:**
- **Stack deleted** (`DERIVABLE`): the repo shows it ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s)).
- **"Clean code" and "accessibility best practices" deleted** (`KNOWN`) ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).
- **Dollar-sign rule deleted.** It was default behaviour, and it also contradicted the EUR fact, which stays as `UNIQUE` ([32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)).
- **Status moved to a routed file** ([07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s)).
- **Brand guide moved to a routed file** ([07:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=445s)).
- **Report steps became a skill** ([05:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=348s)).
- **ALL-CAPS and PR-language rules kept** (`HABIT`) ([04:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=277s), [04:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=290s)).

### Optional department router (after Jay E)

```markdown
<!-- departments/content.md — read this first for any content work -->
# Content — router
Skills: `youtube-script`, `newsletter-draft`, `thumbnail-brief`
Reference: `content/voice.md`, `content/audience.md`, `content/top-videos.md`
Save outputs to: `content/outputs/YYYY-MM/`
```

In CLAUDE.md, the whole department becomes one line: ``- Content work → `departments/content.md` first, then only the files it lists``.

### Optional token-count script

```python
# count_claude_md.py — estimate the always-on token cost of an instruction file
# usage: python count_claude_md.py CLAUDE.md   (needs ANTHROPIC_API_KEY)
import pathlib, sys
import anthropic

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "CLAUDE.md")
text = path.read_text()
client = anthropic.Anthropic()
result = client.messages.count_tokens(
    model="claude-opus-5",  # count with the model you actually use
    messages=[{"role": "user", "content": text}],
)
print(f"{path}: {len(text.splitlines())} lines, about {result.input_tokens} input tokens")
```

The count includes a few tokens of message wrapping, so treat it as an estimate. Run it before and after, with the same model.

## Done when

- [ ] A backup exists, and the audit log shows lines and tokens before and after.
- [ ] The file is under 200 lines ([07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s)), and every remaining line is a route, a habit rule, a fact you can't infer or a guardrail.
- [ ] In a code repo, no line restates the stack or general best practice ([19:37](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1177s), [32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)).
- [ ] Every multi-step procedure is a skill, and asking for that task in a fresh session loads it.
- [ ] Status and reference detail live in files, each with exactly one route line, and every route path exists.
- [ ] The routing test passes in a fresh session: questions get answered from the routed files without you naming them. The "how are you meant to work with me?" check shows the right files being read ([19:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1175s)).
- [ ] The maintenance block is in place, and the next correction produced a proposed destination rather than a silent append.
- [ ] Guardrails that must always hold are also enforced outside the file, by a hook, a permission rule or git (Beyond the source).

## Pitfalls

| Pitfall | What goes wrong | Fix | Source |
|---|---|---|---|
| **Deleting routing the agent needs** | Claude asks you for background or goes looking everywhere. Vague direction makes Claude read everything, burning tokens | Tag routes `ROUTE` and never cut them in the audit. Run the step 10 test and restore any line whose removal broke a question | Coding Sloth [14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s); Nate [07:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=457s) |
| **Cutting habit rules because "the model is good now"** | The ugly habit comes straight back | Keep anything that corrects a habit you've actually seen | Coding Sloth [04:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=258s), [04:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=277s) |
| **Applying "the code is the context" to a non-code brain** | Claude loses facts it can't read anywhere, such as which CRM you use | Ras Mic's argument is about building software projects. Outside a repo, keep short routed notes on outside tools | Ras Mic [19:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1173s) |
| **Moving an every-session fact into a skill** | The skill doesn't trigger, so the fact is missing when it matters | Facts needed in most sessions stay. That is Ras Mic's own exception | Ras Mic [03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s) |
| **"Moving" content into `@` imports** | Line count drops, but the token cost doesn't | Use plain paths as routes (Beyond the source) | — |
| **Required-reading lists that keep growing** | Simon has global instructions make three files read every session, one of them a memory.md Claude keeps appending to. *(Our inference: a file that grows every session becomes always-on bloat.)* | Keep required reading short. Cap or roll up memory files, and route to history instead of loading it | Simon [13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s), [15:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=901s) |
| **An append-only correction loop** | Logging every gotcha into CLAUDE.md without the cap slowly rebuilds the bloat | Propose a destination first, and trim at the cap | Nate [06:38](https://www.youtube.com/watch?v=jqoFP9QapXI&t=398s), [07:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=429s) |
| **Trusting one line as the safety net for an unattended run** | The agent may not follow it, and nothing else protects the working version | Keep the line, but commit on green or add a hook (Beyond the source) | AI LABS [03:37](https://www.youtube.com/watch?v=8wsM0euQOvc&t=217s) |
| **Measuring with the wrong tokenizer** | The before/after numbers don't match what Claude actually uses | Use `/context` or Anthropic's count endpoint with your model | Ras Mic used OpenAI's tokenizer [30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s) |
| **Keeping instructions only in an app settings box** | Simon pastes the generated CLAUDE.md into Cowork settings, and the chat raises deleting the old file copy. *(Our inference: nothing is left to diff or audit, and agents reading the folder can't see it)* | Keep a file copy as the source of truth, and paste from it | Simon [11:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=700s), [11:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=710s) |

## Variations

- **No CLAUDE.md, skills only.** In a code repo, you can follow Ras Mic: no AGENTS.md unless you have something proprietary ([18:50](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1130s)), minimal context and your own skills ([20:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1230s)). The Coding Sloth agrees the file isn't make-or-break ([04:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=295s)). The audit then reduces to "does anything here pass the `UNIQUE` test?"
- **Department routers** ([[Jay E - The ARMS Framework for a Claude Agentic OS]]). The trigger is a workspace that has grown until retrieval slows and plan usage drains. His held about 60,000 files ([11:17](https://www.youtube.com/watch?v=8NSyI-npJCU&t=677s), [11:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=692s)). See the router starter above.
- **Folder indexes plus a navigation pattern** ([[Chase AI - The Agentic OS Setup for Claude Code]]). The vault CLAUDE.md describes the structure and how to navigate it, and each folder's `index.md` holds the detail ([21:52](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1312s), [22:07](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1327s)). Chase says you can ask Claude Code what structure suits your data ([21:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1294s)).
- **Cowork global instructions** ([[Simon Pittman - Set Up Claude Cowork]]). Run the same audit on the settings text.
  - Folder-specific rules can go in a secondary CLAUDE.md in that folder ([12:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=728s)).
  - A context-map file is a route to an outside system: with it, Claude found his Notion tasks database straight away ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s), [30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)).
  - See [[Set Up Claude Cowork]] and [[Build a Context Map for a Connected Tool]].
- **Bootstrap, then audit.** The Coding Sloth points to an experimental `/init` that interviews you and recommends skills and hooks ([03:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=233s), [03:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=236s)). Run this audit on whatever it writes. The flag is in Beyond the source.
- **AGENTS.md projects.** The Coding Sloth imports AGENTS.md from inside CLAUDE.md instead of symlinking ([03:33](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=213s)). Audit the imported file, because that's what actually loads. See [[Tool-Agnostic Context Files]].
- **Second brains.** Apply the audit to the router in [[Build a Level 1 Second Brain]]. Keep `context/` files routed, not imported.

## Beyond the source

*Not from the videos. Each item was checked on 2026-09-15 against the linked page.*

- **The docs' size guidance.** Aim for under 200 lines per CLAUDE.md, because longer files use more context and reduce adherence. For growing instructions, use path-scoped rules in `.claude/rules/` with `paths:` frontmatter, which load only when Claude reads matching files. Claude Code loads a CLAUDE.md of up to 4 MiB in full and skips anything larger. [Claude Code docs: write effective instructions](https://code.claude.com/docs/en/memory#write-effective-instructions), [My CLAUDE.md is too large](https://code.claude.com/docs/en/memory#my-claude-md-is-too-large)
- **Imports don't reduce context.** `@path` imports expand into context at launch. Import parsing skips code spans, so a path in backticks stays a plain route. [Claude Code docs: import additional files](https://code.claude.com/docs/en/memory#import-additional-files)
- **When to add a line, per the docs:**
  - A mistake repeats.
  - Code review flags something Claude ought to have known.
  - You find yourself retyping last session's correction.
  - A newcomer to the project would need the same background.

  Multi-step procedures, and anything that matters for only one part of the codebase, belong in a skill or a path-scoped rule. This matches the correction loop above. [Claude Code docs: when to add to CLAUDE.md](https://code.claude.com/docs/en/memory#when-to-add-to-claude-md)
- **An automated trim check.** The `/doctor` checkup (Claude Code v2.1.206 or later) proposes trims for a checked-in CLAUDE.md:
  - It cuts content Claude can derive from the codebase, such as directory layouts, dependency lists and architecture overviews.
  - It keeps pitfalls, rationale and conventions that differ from tool defaults.

  This is essentially steps 3–4 for code repos, and it lines up with Ras Mic's argument. [Claude Code docs: troubleshoot memory issues](https://code.claude.com/docs/en/memory#troubleshoot-memory-issues)
- **A third destination for corrections.** Claude Code's auto memory saves corrections you give Claude as `feedback` notes, and skips anything your CLAUDE.md already says. Asking Claude to "remember" something goes to auto memory. Asking it to "add this to CLAUDE.md" edits the file. See [[Claude Code Auto Memory]]. [Claude Code docs: auto memory](https://code.claude.com/docs/en/memory#auto-memory)
- **Why skills are cheaper.** The costs guide says CLAUDE.md is loaded at session start, so workflow-specific instructions cost tokens even during unrelated work. Skills load only when invoked, so it recommends moving specialised instructions into skills and keeping CLAUDE.md under 200 lines. Before invocation only the skill's description is in context (Claude uses it to decide when to apply the skill), and `description` plus `when_to_use` is truncated at 1,536 characters. Once a skill is invoked, its body stays in context for the rest of the task. [Claude Code docs: move instructions from CLAUDE.md to skills](https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills), [Claude Code docs: skills](https://code.claude.com/docs/en/skills)
- **"Every turn," precisely.** Ras Mic says the file is added at every turn. The file isn't re-appended each turn, but Claude Code sends the whole conversation, including the loaded file, with every request. Prompt caching lowers the cost of re-reading content that hasn't changed, so the cost is ongoing rather than repeated. [Claude Code docs: why usage climbs in a long session](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)
- **Exact token counts.** Anthropic's token-counting endpoint (`POST /v1/messages/count_tokens`, or `messages.count_tokens` in the SDKs) returns `input_tokens` for a message. It is free but rate-limited, and the result is an estimate. Claude Opus 4.7 and later, and the Fable models, use a newer tokenizer that produces roughly 30% more tokens for the same text than earlier models, so always count with the model you run. [Claude API docs: token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- **Guardrails need enforcement.** CLAUDE.md content arrives as a user message after the system prompt, and strict compliance isn't guaranteed. Anything that must run at a fixed point belongs in a hook. [Claude Code docs: troubleshoot memory issues](https://code.claude.com/docs/en/memory#troubleshoot-memory-issues)
- **Save points for unattended loops.** Claude Code's checkpoints capture edits made with Claude's file-editing tools before each prompt. They don't track files changed by bash commands, usually don't restore subagent edits, and the docs say they don't replace version control. For a save-every-working-version rule, a git commit after each passing test run is the durable version. [Claude Code docs: checkpointing limitations](https://code.claude.com/docs/en/checkpointing#limitations)
- **The interview-style `/init` is documented.** Setting `CLAUDE_CODE_NEW_INIT=1` turns `/init` into an interactive flow:
  - It asks whether to set up CLAUDE.md files, skills and hooks.
  - It explores the codebase with a subagent and asks follow-up questions.
  - It shows a reviewable proposal before writing anything.

  If a CLAUDE.md already exists, `/init` suggests improvements instead of overwriting it. [Claude Code docs: set up a project CLAUDE.md](https://code.claude.com/docs/en/memory#set-up-a-project-claude-md)

## Sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: `/context` ([01:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=109s)), keeping CLAUDE.md refreshed, capped and routed ([06:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=389s)–[07:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=461s)), and updating the skill or CLAUDE.md after a correction ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)). Video: https://www.youtube.com/watch?v=jqoFP9QapXI
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the case against always-loaded files ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)–[05:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=357s)), no stack lines ([19:33](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1173s)), recursive skill fixes ([22:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1329s)), and the token demo plus what belongs in context ([30:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1826s)–[32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)). Video: https://www.youtube.com/watch?v=S_oN3vlzpMw
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: `/init` and his quirk-driven CLAUDE.md ([03:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=186s)–[05:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=303s)), and specific prompts ([14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)). Video: https://www.youtube.com/watch?v=YAsxyoTWFDA
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: memory levels and router files ([10:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=635s)–[13:41](https://www.youtube.com/watch?v=8NSyI-npJCU&t=821s)). Video: https://www.youtube.com/watch?v=8NSyI-npJCU
- [[Chase AI - The Agentic OS Setup for Claude Code]]: folder indexes and a vault CLAUDE.md with a navigation pattern ([19:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1162s)–[22:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1333s)). Video: https://www.youtube.com/watch?v=HRw-vP0j8OM
- [[Simon Pittman - Set Up Claude Cowork]]: global instructions and required reading ([08:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=492s)–[19:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=1190s)), and the context map ([29:46](https://www.youtube.com/watch?v=pl90LATQlHI&t=1786s)). Video: https://www.youtube.com/watch?v=pl90LATQlHI
- [[AI LABS - Types of Claude Loops Explained]]: the CLAUDE.md save-point line for unattended loops ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)). Video: https://www.youtube.com/watch?v=8wsM0euQOvc
- [[Nate Herk - Claude as a One-Person Marketing Team]]: a generated router-style CLAUDE.md, and advice to keep adding to it daily or weekly ([12:31](https://www.youtube.com/watch?v=yCACmFTiCto&t=751s)–[12:52](https://www.youtube.com/watch?v=yCACmFTiCto&t=772s)). Video: https://www.youtube.com/watch?v=yCACmFTiCto

## Related

- Concepts: [[CLAUDE.md as a Router]] · [[Agent Skills]] · [[Context Window Management]] · [[Claude Code Auto Memory]] · [[Tool-Agnostic Context Files]] · [[Agentic OS]]
- Techniques: [[Build a Level 1 Second Brain]] · [[Build a Skill from a Successful Run]] · [[Skill Improvement Loop]] · [[Context Hygiene Routine]] · [[Set Up Claude Cowork]] · [[Build a Context Map for a Connected Tool]] · [[Tests-First Goal Loop]] · [[Schedule Recurring Claude Tasks]] · [[Build a Brand-Aware Marketing Project]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[OpenAI Codex]]
- People: [[Nate Herk]] · [[Ras Mic]] · [[The Coding Sloth]] · [[Jay E]] · [[Chase AI]] · [[Simon Pittman]] · [[AI LABS]]
- [[Home]]
