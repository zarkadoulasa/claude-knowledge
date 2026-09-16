---
type: concept
aliases: ["Plan Mode"]
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[Sergei Chyrkov - Claude Design Full Tutorial]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/planning, topic/claude-code, topic/prompting, topic/models, topic/verification, topic/context, topic/design, topic/media]
---

# Plan Before Executing

## In one sentence

Before Claude edits anything, have it research the task and write a plan you can check. Use its questions to fill the gaps and build the checks into the plan. Only then approve execution. In [[Claude Code]] the switch for this is plan mode ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)–[03:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=191s); [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] [06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)).

## How it works

### 1. Plan mode: research now, edit later

Both videos describe the same feature from slightly different angles.

| | [[Nate Herk]] | [[The Coding Sloth]] |
|---|---|---|
| Getting there | Shift+Tab cycles through the modes, or you pick plan mode by hand ([02:50](https://www.youtube.com/watch?v=jqoFP9QapXI&t=170s)) | Shift+Tab ([06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s)) |
| What Claude does | Still reads and researches, but changes nothing ([02:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=174s)–[02:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=178s)). It lays out the steps, asks clarifying questions and maps the approach before writing any code ([02:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=178s)–[03:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=183s)) | Reads the code more thoroughly than usual, writes a full plan and shows it to you before doing anything ([06:56](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=416s)–[07:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=424s)) |
| Your part | When you're happy with the plan, leave plan mode and tell Claude to execute ([03:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=185s)–[03:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=188s)) | Approve or reject the plan ([07:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=424s)) |
| Why it helps | He says this step alone sharply cuts how often you have to correct Claude ([03:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=188s)). He also says planning "has been shown" to improve quality, but cites nothing ([03:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=183s)) | The model takes time to explore and think before it acts ([07:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=427s)–[07:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=433s)). A mistake is far easier to catch in a plan than in thousands of lines spread over a dozen files ([07:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=434s)–[07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)) |
| How strongly | Hack 7: *always* start in plan mode ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)) | S tier (the rating is garbled in the captions) and "a must" for Claude models, **but only for big tasks** ([06:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=413s), [07:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=425s), [07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)) |

### 2. Give Claude problems, not orders

- Nate's hack 8 is to treat Claude like a junior developer ([03:13](https://www.youtube.com/watch?v=jqoFP9QapXI&t=193s)). Instead of a direct order such as "write a function that does X" ([03:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=196s)), ask how something *should be handled* and let Claude work out the approach ([03:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=198s)–[03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s)). His example question is about handling "growth tracking" *(the topic is unclear in the captions)*.
- Because Claude then makes its own assumptions and decisions, you can ask it to explain them ([03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s)–[03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s)). That puts the hidden choices in front of you before any code exists.
- He calls this plan mode with deeper thinking, and again says reasoning first gives better output, again without a source ([03:29](https://www.youtube.com/watch?v=jqoFP9QapXI&t=209s)–[03:36](https://www.youtube.com/watch?v=jqoFP9QapXI&t=216s)).

### 3. Close the gaps with questions

- Nate's hack 9 is to make Claude ask questions ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)). Plan mode often does this without being told ([03:39](https://www.youtube.com/watch?v=jqoFP9QapXI&t=219s)), but you can explicitly tell it to use its **AskUserQuestion** tool ([03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s)) and to keep asking until it is 95% confident it understands what you need and what it has to do ([03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)).
- His payoff: this upfront alignment saves three or four rounds of revisions ([03:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=233s)).
- The Coding Sloth does the same job with a skill. He uses [[Matt Pocock]]'s grill-with-docs skill to refine his requirements ([06:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=364s), [06:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=373s)); the captions render it as "grow with doc". For a full interview skill that writes to a file, see [[Grill Me Interview Skill]].
- *Vault reading, not from either video:* "95% confident" is a prompt device, not a measurement you can check. A more useful sign that you're done is when new questions stop surfacing new decisions.

### 4. Write the checks into the plan

- Nate's hack 10 puts verification inside the plan. After each build to-do, add a checking to-do: screenshot the site and check that it looks right, then open Chrome DevTools and confirm nothing is functionally broken ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)–[04:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=260s)). He adds a gate: tell Claude not to move to the next to-do until it's 95% confident the current one is good ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)). One-shotting is hard, but landing 90% of the way beats 60–65% ([04:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=277s)–[04:40](https://www.youtube.com/watch?v=jqoFP9QapXI&t=280s)).
- The Coding Sloth rates verification S tier, "if anything" double or triple S, calling it plain software-engineering fundamentals that AI makes more important ([08:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=511s)–[08:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=527s)). The point is that Claude gets some means of proving the work correct before declaring it finished ([08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s)). His rules:
  - Tests come first and implementation second, because tests written after the code just pass that code ([09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)–[09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s)).
  - Test only what matters, since strong models over-test ([09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)).
  - Run type checkers and linters before calling the task done ([09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)).
- See [[Verification Before Done]] and [[Build Verification into Every Task]].

### 5. Plan on the strongest model, build on a cheaper one

- The Coding Sloth describes shadcn's improve skill (captioned "Shatien's improved"): it audits your codebase and writes plans for *other* agents to carry out ([06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s)–[06:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=409s)).
- He expects the idea behind it to become the default approach ([07:32](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=452s)). A smart model writes the plan and a cheaper, faster model implements it ([07:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=455s)–[07:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=461s)).
- Cheaper doesn't mean dumb, he says. Today's fast models are capable enough, which is why the approach works, and it saves money ([07:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=462s)–[07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s)).
- In Claude Code he would once have planned with Fable. He then corrects his month-old footage: Fable isn't gone, but it needs usage credits now, which in his view amounts to the same thing ([07:52](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=472s)–[08:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=480s)), so he plans with **Opus** and implements with **Sonnet** ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)). Tools such as Cursor, OpenCode or [[OpenAI Codex]] let you mix models more freely ([08:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=485s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s)).
- Nate splits models along a different line, by volume rather than by phase. Subagents on Haiku do simple or heavy reading and pass short summaries to an Opus main thread ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s), [06:00](https://www.youtube.com/watch?v=jqoFP9QapXI&t=360s)–[06:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=385s)). See [[Choosing a Claude Model]] and [[Route Tasks to the Right Claude Model]].

### 6. Why this saves tokens as well as rework

- Nate: every token Claude spends heading the wrong way is wasted context, so press Esc, correct course and re-prompt early ([07:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=463s)–[07:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=474s)). A plan is that correction made before any tokens are spent.
- The Coding Sloth, writing from a $20 plan ([00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s)), makes these points:
  - Usage is counted in tokens, not prompts ([12:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=773s)).
  - A medium or big task takes at least about 50K tokens ([14:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=853s)).
  - Vague prompts make Claude read everything to work out what you mean ([14:47](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=887s)).
- See [[Context Window Management]].

### 7. Planning outside plan mode

- **Self-interview with an assumption log.** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] demos Ouroboros. It generates questions about your request and answers them from your description and the project ([07:20](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=440s)). It fills a small gap alone only when the choice is easy to reverse and in scope; anything that could change what the app does pauses for you, and assumptions are logged ([07:27](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=447s)–[07:38](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=458s)). Building starts only after the resulting plan passes review ([07:43](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=463s)–[07:51](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=471s)).
- **A storyboard when each build is slow.** [[Chase AI - GPT-6 Astra Motion Design in After Effects]] has the model storyboard first instead of sending one prompt straight to After Effects ([01:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=110s)–[02:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=124s)). His trigger is execution cost: a 15–20 second graphic can take 10–20 minutes to build, so agreeing up front avoids hours of re-prompting ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)–[02:49](https://www.youtube.com/watch?v=C8dWdic-oK4&t=169s)). The storyboard's beats then feed the build prompt ([04:46](https://www.youtube.com/watch?v=C8dWdic-oK4&t=286s)). See [[Storyboard-First AI Video and Motion Graphics]].
- **A spec file drafted in chat.** [[Sergei Chyrkov - Claude Design Full Tutorial]] gives regular Claude chat a few words about the project and has it write a detailed prompt as a markdown file ([01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s)–[01:18](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=78s)), which he loads into [[Claude Design]] ([01:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=106s)). He shows no interview step; chat Claude fills in the detail.
- **An intake interview inside the skill.** [[Nate Herk - The Scrollcraft Website Design Skill]] keeps his first prompt short because the skill opens by interviewing him ([04:01](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=241s)) about the scroll journey, the one belief a visitor should leave with, which real assets exist and a signature move ([05:29](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=329s)–[07:06](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=426s)). See [[Scrollcraft]].
- **Counterexample: no plan at all.** In [[Nate Herk - Claude as a One-Person Marketing Team]] he fires four large generation prompts into one chat, with no plan mode or questions ([22:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1322s)). *This note's reading:* project brand context and the storyboard frames Claude made before the UGC videos ([31:50](https://www.youtube.com/watch?v=yCACmFTiCto&t=1910s)) did part of a plan's job. It cuts against his always-plan advice in [[Nate Herk - 32 Tricks to Level Up Claude Code]] ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)) and suits only cheap, reversible work.

## When to use it — and when not to

| Situation | Plan first? | Basis |
|---|---|---|
| Big feature, many files | Yes | The Coding Sloth ([07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)); spotting a bad plan beats reviewing a 12-file diff ([07:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=434s)) |
| Requirements are fuzzy or you'd expect several revision rounds | Yes, with questions | Nate ([03:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=217s)–[03:56](https://www.youtube.com/watch?v=jqoFP9QapXI&t=236s)) |
| You want a cheaper model to do the building | Yes: the plan is the hand-off | The Coding Sloth ([07:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=455s)–[07:50](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=470s)) |
| Typos, variable renames, small design tweaks | No. It's a waste and doesn't improve the result | The Coding Sloth ([07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)) |
| Tight usage limits, small or medium task | Usually no, or a light version: frame the problem and ask for a short outline without switching modes | *Vault inference:* exploring and planning also spend tokens, which matters most on the $20-plan budget the Coding Sloth works within ([00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s), [12:53](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=773s)). Anthropic says plan mode adds overhead (Beyond the source) |
| Exploratory poking around, where you want to see how Claude reads the problem | Often no | Anthropic's guide says exploratory tasks are a case for skipping the plan (Beyond the source) |
| Each run is slow or costly to redo (renders, long generations), even for a small change | Yes, ideally as a visual plan such as a storyboard | Chase AI ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)) |
| A domain with recurring decisions (site structure, feel, assets) | Build the interview into the skill | Scrollcraft ([04:01](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=241s)) |

## Where sources disagree

- **"Always" vs "big tasks only."** Nate says to always start in plan mode ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)). The Coding Sloth says to keep it for big tasks and skip it for typos, renames and small design changes ([07:20](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=440s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)). Anthropic's best-practices guide is closer to the Coding Sloth (see Beyond the source).
- **Open-ended problems vs very specific prompts.** Nate wants you to pose a problem and let Claude reason out the approach ([03:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=198s)–[03:25](https://www.youtube.com/watch?v=jqoFP9QapXI&t=205s)). The Coding Sloth wants prompts that are "stupidly specific", naming the files and sources to use, because vague prompts make Claude read everything ([14:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=879s)–[14:51](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=891s)). *Vault reading:* the two fit together if you are specific about goal, constraints, files and done criteria, and open about the approach.
- **Two different model splits, not a clash.** Nate tiers by workload: Haiku readers under an Opus lead ([05:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=319s)). The Coding Sloth tiers by phase: Opus plans, Sonnet builds ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)). You can combine them.
- **"Changes nothing."** Nate's description ([02:54](https://www.youtube.com/watch?v=jqoFP9QapXI&t=174s)–[02:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=178s)) holds for source edits in normal sessions. The current docs add exceptions (see Beyond the source).
- **Ask the user, or answer your own questions?** Nate's 32 Tricks has Claude keep asking you until it's 95% confident ([03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)). Ouroboros answers its own questions and escalates only decisions that change what the app does ([07:27](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=447s)). Scrollcraft asks you domain questions and can suggest answers; Nate takes its recommended opening for the scroll journey ([05:42](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=342s)).
- **What triggers a plan: size of change or cost of a run?** The Coding Sloth skips planning for small design tweaks ([07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s)). Chase AI storyboards even a graphic he later cut to 10 seconds ([02:16](https://www.youtube.com/watch?v=C8dWdic-oK4&t=136s)), because one build can take 10–20 minutes ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)).

## Perspectives from sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: planning as four linked beginner hacks. Start in plan mode, pose problems, have Claude ask questions until it's confident, and write checks into the to-do list ([02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s)–[04:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=285s)). The payoff he claims is fewer correction rounds, and his support for it is anecdotal.
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: plan mode is S tier, but for big tasks only ([07:07](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=427s)–[07:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=450s)). Plan on a strong model and build on a cheaper one ([07:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=455s)–[08:05](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=485s)). He looks at all of it through tight token limits. He also mentions Ultraplan, which is now gone ([02:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=130s), [02:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=137s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: Ouroboros's self-interview and assumption log ([07:20](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=440s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]]: a storyboard before slow builds ([01:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=110s)).
- [[Sergei Chyrkov - Claude Design Full Tutorial]]: a markdown spec written in chat ([01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]]: an interview inside the skill ([04:01](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=241s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]]: the no-planning counterexample ([22:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1322s)).

## Beyond the source

*Not from the videos. Each item was checked at the linked page on 2026-09-15.*

- **What plan mode actually blocks.** Claude reads files, runs shell commands to explore, and writes a plan, but doesn't edit your source until you approve. Shell commands aren't frozen, though:
  - When auto mode is available (with `useAutoModeDuringPlan`, on by default), a classifier approves or blocks commands during planning.
  - Otherwise, commands outside the read-only set ask for permission.
  - In sessions where bypass permissions are available, the edit block isn't enforced. Claude is only told to plan, and an edit it attempts runs without a prompt.

  Source: [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes).
- **Getting in and out.** `Shift+Tab` cycles modes, `/plan` applies plan mode to a single prompt, and `claude --permission-mode plan` starts a session in it. `defaultMode: "plan"` in `.claude/settings.json` makes it the project default. At approval you choose auto or manual edits, or **No, keep planning**, and `Ctrl+G` opens the plan in your editor. Step-by-step use is in [[Plan-First Workflow]]. Source: [permission modes](https://code.claude.com/docs/en/permission-modes).
- **Claude can switch modes itself.** The `EnterPlanMode` tool needs no permission. `ExitPlanMode`, which presents the plan, does. `AskUserQuestion` asks multiple-choice questions with an "Other" free-text row and needs no permission. Questions stay open until answered unless you set `askUserQuestionTimeout`, and plan approval never auto-resolves. Source: [tools reference](https://code.claude.com/docs/en/tools-reference).
- **Anthropic's own guidance.** The recommended loop is explore → plan → implement → commit. Plan mode "adds overhead": for small, clear fixes, ask directly, and skip the plan if you could describe the diff in one sentence. Planning pays most when the approach is uncertain, several files change, or the code is unfamiliar. For larger features, have Claude interview you with `AskUserQuestion` and write a spec file, then run it in a fresh session. The guide says strong specs name the files involved, state what's out of scope and end with an end-to-end check. Its closing advice also allows skipping the plan when a task is exploratory, and a looser prompt when you want to see how Claude reads the problem first. Source: [Claude Code best practices](https://code.claude.com/docs/en/best-practices).
- **Two-model planning is built in.** The `opusplan` model alias uses Opus in plan mode and switches to Sonnet for execution. `/model` changes models mid-session, and `opus` and `sonnet` currently resolve to Opus 5 and Sonnet 5 on the Anthropic API. Fable is never a default. Source: [model configuration](https://code.claude.com/docs/en/model-config).
- **The Fable remark, checked.** Pro plans and standard seats on Team or seat-based Enterprise plans need usage credits for Fable models. A promotion covering Fable 5 on those tiers ended on 19 July 2026, and Fable 5.1 was never part of it. Max plans and premium seats include Fable, capped at up to half of the weekly usage limit. "Basically gone" is true for Pro, not for Max. Source: [Claude Help Center: Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan).
- **Multi-model isn't automatically cheaper.** Anthropic describes an *advisor* pattern (a cheap executor consults a frontier model on hard calls) and an *orchestrator* pattern (a frontier model plans and hands work to cheaper workers). It recommends first sweeping effort on your current model, and pricing the stronger model alone at low effort. It notes the orchestrator doesn't pay off when the work is one dependent chain or fits in one context. Source: [Optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence).
- **shadcn's improve skill.** It is read-only apart from `plans/`. It writes one self-contained plan per finding, and `/improve execute <plan>` hands a plan to a cheaper executor subagent in an isolated git worktree, then re-runs the plan's done criteria; merging stays with you. Source: [github.com/shadcn/improve](https://github.com/shadcn/improve).
- **Ultraplan is gone.** Anthropic removed the research preview (the `/ultraplan` command and keyword). It points to plan mode locally, or Claude Code on the web for cloud sessions. Source: [Ultraplan is no longer available](https://code.claude.com/docs/en/ultraplan).
- **Ouroboros, per its README.** The interview ends on a computed gate: the "Seed" spec can't be generated until an ambiguity score is at most 0.2, unless you force it. The README calls the interview Socratic questioning that exposes hidden assumptions, and its terminal demo shows the CLI asking the user about ordering and scope, which is more user-facing than the video's "interviews itself". Source: [github.com/Q00/ouroboros](https://github.com/Q00/ouroboros).

## Related

- Build it: [[Plan-First Workflow]] · [[Grill Me Interview Skill]] · [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Route Tasks to the Right Claude Model]] · [[Context Hygiene Routine]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Build a Scroll-Driven Landing Page]]
- Concepts: [[Verification Before Done]] · [[Choosing a Claude Model]] · [[Context Window Management]] · [[Permissions and Approval Gates]] · [[Subagents and Agent Teams]] · [[Agent Skills]]
- Tools and people: [[Claude Code]] · [[OpenAI Codex]] · [[Claude Design]] · [[Scrollcraft]] · [[Nate Herk]] · [[The Coding Sloth]] · [[Matt Pocock]] · [[AI LABS]] · [[Chase AI]] · [[Sergei Chyrkov]]
- Sources: [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] · [[Chase AI - GPT-6 Astra Motion Design in After Effects]] · [[Sergei Chyrkov - Claude Design Full Tutorial]] · [[Nate Herk - The Scrollcraft Website Design Skill]] · [[Nate Herk - Claude as a One-Person Marketing Team]]
- [[Home]]
