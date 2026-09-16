---
type: technique
goal: "Turn a workflow you have walked the agent through by hand into a SKILL.md written from that real, successful run, prove it works in a fresh session, and check what it costs in always-on context compared with pasting the procedure into CLAUDE.md"
difficulty: beginner
time_to_build: "30 to 90 minutes for the guided run, skill draft and fresh-session test; then a few fix-and-update rounds as real use exposes gaps (vault estimate)"
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]"]
tools: ["[[Claude Code]]", "[[Claude Cowork]]", "[[OpenClaw]]"]
tags: [topic/skills, topic/claude-code, topic/context, topic/prompting, topic/cowork, topic/loops]
---

# Build a Skill from a Successful Run

> **Provenance.** The method is [[Ras Mic]]'s, from his conversation with [[Greg Isenberg]] in [[Ras Mic - How AI Agents and Claude Skills Work]]. He explains it on a whiteboard, runs it in [[OpenClaw]] rather than Claude Code, and never shows the sponsor-vetting skill he built this way. The only skill file he puts on screen is an unrelated 116-line code-structure skill ([29:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1780s)). The steps below translate his method to Claude Code and Cowork. Supporting and contrasting points from [[Chase AI - The Agentic OS Setup for Claude Code]], [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[Simon Pittman - Set Up Claude Cowork]] and [[Nate Herk - 32 Tricks to Level Up Claude Code]] are credited by name. So are later additions from [[Nate Herk - Claude as a One-Person Marketing Team]], [[Nate Herk - Build Skills Instead of Agents]] and [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]. **The prompts, SKILL.md skeleton, worked example, test plan and token script are original vault starter content.** The skeleton's frontmatter was checked against Anthropic's docs and the Agent Skills spec (see Beyond the source).

## Goal

A skill in `.claude/skills/<name>/SKILL.md` that the agent wrote **after** it completed the workflow correctly with you. That way it captures the steps, decision rules, tool calls and failure points that actually worked. You then test it in a fresh session and confirm that keeping it as a skill costs far less always-on context than keeping it in CLAUDE.md.

Ras Mic's core claim: a skill written up front, by you or by AI, lacks the context of what a successful run looks like. Agents then fail at API calls or fetch the wrong data ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)–[11:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=692s)). The agent copies what you show it very faithfully, but only if you have shown it something to copy ([11:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=701s)).

## Use when

- **A vague instruction produced confident, shallow work.** His first sponsor-screening prompt told the agent to check every 15 minutes, research each sponsor and say whether it was worth it ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)). It approved every sponsor and never did real research ([08:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=487s)–[08:20](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=500s)). That told him the model needed a step-by-step guide ([08:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=502s)).
- **A [[Workflow Audit into Skills]] nominated a task** and its *Validated run?* column still says "no".
- **You keep repeating a procedure in chat, or it's sitting in CLAUDE.md.** Ras Mic says report formats and code-structure rules belong in skills, not in an always-loaded file ([05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s)).
- **The workflow spans several tools or data sources.** His YouTube report pulls from about eight sources, and he says no single prompt could do it ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s)–[22:25](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1345s)).

**Don't use it for:**
- General knowledge the model already has. He says not to tell it to use React, or that money takes a dollar sign; tell it only what's specific to you ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)–[32:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1961s)).
- A task you can't yet define as right or wrong. Greg's summary of the method starts with mapping the workflow and defining right and wrong ([13:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=831s)–[13:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=838s)).

## What the sources say

### Ras Mic's method

| Step | What he says | Timestamp |
|---|---|---|
| The anti-pattern | People identify a workflow, then jump straight to creating the skill, which he calls the worst thing you can do | [08:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=509s)–[08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s) |
| Mental model | Mentor it like a new hire: tell it what to do, let it fail, correct it. Learning by experience | [08:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=537s)–[09:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=555s) |
| Walk it step by step | His method, which he claims now works every time: do the workflow together, one step at a time | [09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s)–[09:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=563s) |
| Give criteria as you go | For each sponsor: tell me about the company, check its X, YouTube, Trustpilot and whether it raised money | [09:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=572s)–[09:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=581s) |
| Hard rule | If two of those four are missing or in bad standing, reject automatically | [09:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=584s) |
| Record the result | Rejected companies go into a Google Sheet as "No contact" (he was using Opus) | [09:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=589s)–[09:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=596s) |
| Why it works | The walkthrough becomes part of the conversation's context | [10:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=659s)–[11:03](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=663s) |
| Define good and the hand-off | Say what a good company looks like, and email him when one is really good | [11:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=665s)–[11:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=669s) |
| Repeat before codifying | Only after a successful run, done again and again, did he convert it into a skill | [11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s) |
| Ask its opinion, correct it | Mid-run he asks what it thinks of a result, then tells it where to record the verdict | [12:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=724s)–[12:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=727s) |
| Codify from the run | After the back-and-forth, tell the AI to review what it did and create the skill. It now has real context to write from | [12:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=731s)–[12:22](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=742s) |
| Don't handwrite | He doesn't write skills by hand. AI can, and there's even a skill for creating skills | [12:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=747s)–[12:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=750s) |
| Keep using it, and fix gaps | The skill will still fail at some point because it has gaps ([21:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1267s)–[21:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1274s)). Ask why it failed and what error it got ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)), tell it to fix the problem ([21:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1316s)), and once it succeeds, have it update the skill so it doesn't happen again | [22:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1325s)–[22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s) |
| Payoff | Five such loops made his 8-source report skill run cleanly in about 10 minutes | [22:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1350s)–[22:34](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1354s) |
| Full loop recap | Do it by hand, create the SKILL.md once it completes, keep using it, and treat each failure as a prompt to update the skill, not a reason to complain | [22:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1377s)–[23:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1398s) |
| Expectations | Expect an unpleasant early investment period; he suggests about two weeks, and at first he thought OpenClaw was garbage | [23:51](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1431s)–[24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s) |

### Why a skill, not CLAUDE.md: his context-cost argument

| Point | Detail | Timestamp |
|---|---|---|
| Progressive disclosure | Only a skill's name and description sit in context. When a request matches, such as a Notion report, the agent reads the full skill | [03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)–[03:45](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=225s) |
| Anatomy | A skill is a name, a description and a body. Only the first two are added up front: a couple of hundred tokens instead of thousands | [05:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=305s)–[05:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=340s) |
| Cost of a big context file | A 1,000-line CLAUDE.md of about 7,000 tokens is paid on every run, and most of it should probably be a skill | [04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)–[04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s) |
| The exception | Proprietary company information, or a personal methodology needed in every conversation, can justify a context file | [03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s) |
| The demo | His 116-line code-structure skill reorganises AI-written code so he can review it. Its description names when to use it, so asking to clean up code structure loads it | [29:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1780s)–[30:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1818s) |
| The measurement | In OpenAI's web tokenizer, the whole skill is 944 tokens, which you'd pay every chat if it were an AGENTS.md. Name plus description alone is 53 tokens | [30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)–[30:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1857s) |
| Not just money | The model gets worse as the window fills. He aims to stay between a fresh window and about 70% full | [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)–[31:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1887s) |

### Other sources on creating skills

- **[[Chase AI - The Agentic OS Setup for Claude Code]]** agrees on the ideal. Do the task manually, confirm it works, then tell Claude to turn what you just did into a skill ([07:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=448s)–[07:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=451s)). He names skill-creator as the tool ([07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s)), and adds that skills are editable workflows you tune until the outputs are right ([10:40](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=640s)).
- **[[Jay E - The ARMS Framework for a Claude Agentic OS]]** builds skills from content he finds. He pasted an X post, invoked skill-creator, let Claude Code write the skill, then tested it ([06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s)–[06:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=386s)). His next level is the reference-rich skill, where SKILL.md routes to files such as a brand HTML page ([06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s)–[08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)). See [[Build a Reference-Rich Skill]].
- **[[Simon Pittman - Set Up Claude Cowork]]** shows the Cowork route. Customize, Skills, + offers create with Claude, write skill instructions, or upload a skill ([32:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1958s)–[32:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1961s)), and he says skill-creator is worth turning on ([32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)). His tip is to ask skill-creator to build the AskUserQuestion clarifying step into your skills ([33:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2010s)), as the docx skill does in his demo ([33:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1998s)–[33:28](https://www.youtube.com/watch?v=pl90LATQlHI&t=2008s)).
- **[[Nate Herk - 32 Tricks to Level Up Claude Code]]** gives the same fix-forward habit. When pushback produces a better output, tell Claude to update the skill or CLAUDE.md so it doesn't repeat the mistake ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
- **[[Nate Herk - Claude as a One-Person Marketing Team]]** turns creative outputs into skills, not just procedures.
  - **Skills as recipes.** He describes skills as recipes, so a carousel or UGC ad is made the same way each time ([03:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=187s)–[03:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=196s)).
  - **Promote what you liked.** When a reel or ad comes back and you like it, make it a skill ([25:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1502s)–[25:13](https://www.youtube.com/watch?v=yCACmFTiCto&t=1513s)).
  - **Feedback both ways.** A loved carousel becomes a skill, and a disliked style gets ruled out ([29:59](https://www.youtube.com/watch?v=yCACmFTiCto&t=1799s)–[30:09](https://www.youtube.com/watch?v=yCACmFTiCto&t=1809s)).

  The "run" here is an output you judged good, and he admits he added no subject-matter expertise ([27:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=1642s)–[27:31](https://www.youtube.com/watch?v=yCACmFTiCto&t=1651s)).

### Where sources disagree

- **Can you create a skill without a prior run?** Jay E generates one from a pasted post ([06:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=380s)). Simon's first option is creating a skill conversationally with Claude ([32:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1961s)). Chase lists a describe-it-to-skill-creator route but warns it may be unvalidated ([06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s)–[07:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=444s)). Ras Mic rejects writing up front outright ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). *(Vault reconciliation:)* treat pasted content or a conversational draft as **input to the guided run**, not a finished skill. A draft counts only after it has completed a real task.
- **Install other people's skills?** Ras Mic doesn't. He reads them, or asks his AI what to learn from them, because his agent needs its own run's context and marketplaces are an easy attack route ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[13:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=787s)). Simon happily uses a downloaded frontend-slides skill ([37:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=2222s)), and Jay E starts beginners on Anthropic's pre-built skills ([05:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=339s)). See [[Build vs Install Third-Party Skills]].
- **How much CLAUDE.md costs.** Ras Mic describes a context file as added on every turn ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)). Per the docs, CLAUDE.md loads once at session start and then stays in the conversation that each request carries, with prompt caching lowering the repeat cost. His practical point, that it permanently occupies context in a way skills don't, holds (Beyond the source).
- **Extend a skill before the new part has run?** [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] pastes fal.ai's Kling 3.0 docs into the session and has Claude add the model to the ready-made GPT Image 2 skill he shares ([11:36](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=696s)–[12:21](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=741s)). The first Kling call comes afterwards ([12:31](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=751s)–[12:54](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=774s)), the order Ras Mic rejects ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). *(Vault reconciliation:)* docs are fine for API wiring. Mark the addition unvalidated until one real call works, then fix forward with Prompt 3.

## Prerequisites

- [[Claude Code]] (or [[Claude Cowork]]) and a project folder. The skill will live in `.claude/skills/`.
- One workflow with a clear pass or fail, and 2–3 real inputs to run it on (for example, three real sponsor emails).
- Access to the tools the workflow needs, such as connectors, CLIs or API keys, **set up before the run**, so the run records the tool calls that actually work.
- Optional: skill-creator. Ras Mic mentions an unnamed skill for creating skills ([12:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=750s)); it's named by Chase ([07:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=432s)), Jay E ([05:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=354s)) and Simon ([32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)). Install paths are under Beyond the source.
- Optional, for the cost check: an Anthropic API key (token counting is free), or just `/context` inside Claude Code.

## Steps

### Phase A: the guided run

1. **Write down "right and wrong" first.** In 3–6 bullets, say what a correct result looks like and what must never happen, following Greg's summary of the method ([13:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=835s)). Keep it open; you'll paste it in step 3.
2. **Start a fresh session** in the project, so the transcript contains only this workflow.
3. **Open with Prompt 1.** It tells Claude you'll teach the task step by step and that it must not write a skill yet.
4. **Walk it through one step at a time.** Give each instruction and each criterion as it becomes relevant, in the order you'd actually work ([09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s)–[09:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=584s)). State hard rules explicitly, like his two-of-four rejection rule.
5. **Ask for its judgement and correct it on the spot** ([12:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=724s)). When something breaks, ask what the error was before you fix anything ([21:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1287s)). The correction phrases below help.
6. **Define the output and hand-off**: where the result goes, what format, and who gets told ([11:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=665s)–[11:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=669s)).
7. **Run it again on a second real input** in the same session, with fewer instructions from you. Ras Mic repeated the successful run before converting it ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)). If run two needs new corrections, do a third.

### Phase B: write the skill from the run

8. **Ask Claude to review what it did and write the skill** with **Prompt 2**, using skill-creator if you have it ([12:16](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=736s)–[12:30](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=750s)). Prompt 2 asks for corrections written as rules, run-specific details turned into inputs, and long material moved to `references/`.
9. **Review the draft yourself.** Check the frontmatter against the skeleton below. Remove one-off details and anything secret. Read every command it will run. Make sure the description names the phrases you'd naturally use. Keep SKILL.md short (Beyond the source).
10. **Measure the context cost**, the way Ras Mic compared 944 and 53 tokens ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)–[30:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1857s)). Run the token script below, which uses Claude's own counter, or compare `/context` before and after. Record both numbers in the skill's metadata or changelog.

### Phase C: prove it in a fresh session

11. **Open a brand-new session** (`/clear` or a new terminal) and work through the **fresh-session test plan**. It checks that a natural request triggers the skill, that `/skill-name` works, that a different input and an edge case both work, and that an unrelated request doesn't load it.
12. **On any failure, fix forward** with **Prompt 3**. Ask why, have it fix the problem and finish the task, then update SKILL.md and add a changelog line ([21:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1278s)–[22:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1327s); Nate at [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)). Rerun the failed test in another fresh session. Ongoing hardening lives in [[Skill Improvement Loop]].
13. **Put it into service.** Commit it so the team gets it (Nate, [05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)). Mark it `built` in your skills backlog, and consider the automation pass in [[Workflow Audit into Skills]] once it has run cleanly for a while.

## Starter files & prompts

*All of this section is original vault starter content.*

### Folder layout

```text
your-project/
└── .claude/
    └── skills/
        └── sponsor-vetting/              # folder name = skill name
            ├── SKILL.md                  # short: steps, rules, output, failures, changelog
            ├── references/
            │   ├── criteria.md           # long checklists, scoring tables
            │   └── examples.md           # one good and one bad worked example from the run
            └── scripts/                  # optional helpers the skill runs
```

### Prompt 1: open the guided run

```text
I'm going to teach you a workflow I do regularly: <workflow in one line>.
We'll do it together on a real case, one step at a time. Don't write a skill, plan or
checklist yet. Just do each step I give you, show me the result, and wait for my next
instruction.

What "right" looks like:
- <criterion>
- <criterion>
What must never happen:
- <rule>

When you're unsure, ask me instead of guessing. When a tool call or API fails, stop and tell
me the exact error before trying anything else.

The first case is <input: email, file, link>. Step 1: <first instruction>.
```

**Mid-run phrases that give the future skill something to learn from:**

| Situation | Say |
|---|---|
| It skipped a check | "You didn't check <X>. Always check <X> before deciding. Do it now." |
| You want its reasoning | "Before I tell you, what's your verdict and why?" |
| A threshold | "Rule: if <condition>, then <action>. No exceptions." |
| A failure | "What exactly failed, at which step, and what error did you get?" |
| Output format | "Save the result as <format> in <place>. This is the format every time." |
| A good result | "That's correct. This is what good looks like for this step." |

### Prompt 2: write the skill from this run

```text
That worked. Review everything you did in this conversation, from my first instruction to
the final output, and turn it into a skill. Use the skill-creator skill if it's available.

- Write the steps in the order that worked. Turn each correction I made into a rule in the
  steps, not a story about what went wrong.
- Keep every decision rule and threshold I gave you exactly.
- Record the tools, commands, API calls, file paths and output formats that succeeded, and
  every failure we hit with its fix.
- Turn anything specific to this case (names, dates, numbers) into an input.
- Write a description that says what the skill does and the phrases I'd naturally use to
  ask for it, in under 200 characters.
- Keep SKILL.md short. Put long criteria, examples or templates in references/ and link them.
- Save to .claude/skills/<name>/SKILL.md. The name uses lowercase letters, numbers and
  hyphens and matches the folder.
- Don't include any secrets, tokens or personal data.
Show me the full draft before saving, and list anything you weren't sure how to generalise.
```

### SKILL.md skeleton

```markdown
---
name: skill-name
description: Does <outcome> from <input>. Use when the user asks to <phrase>, <phrase> or <phrase>.
metadata:
  built-from-run: "YYYY-MM-DD"
  always-on-tokens: "NN"
  full-tokens: "NNN"
# Optional Claude Code fields, uncomment only if needed:
# argument-hint: "[input]"
# disable-model-invocation: true   # you trigger it by hand only; Claude and scheduled tasks can't use it
# allowed-tools: Read Grep Bash(gh *)
---

# <Skill title>

## Inputs
- <input 1>: where it comes from, if missing ask the user

## Steps
1. <step from the successful run>
2. <step> (rule: <correction from the run>)
3. <step>

## Decision rules
- If <condition>, then <action>.

## Output
- Format: <format>. Location: <path or tool>. Notify: <who, when>.

## Known failure points and fixes
- <symptom> → <cause> → <fix that worked>

## References
- [Criteria](references/criteria.md): read before step <n>
- [Examples](references/examples.md): one pass and one fail from the original run

## Changelog
- YYYY-MM-DD: built from guided run on <case>.
```

### Worked example: a sponsor-vetting skill based on Ras Mic's criteria

*His criteria and outcomes ([09:32](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=572s)–[11:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=669s)). The file structure, wording and sheet columns are the vault's. He never shows his skill.*

```markdown
---
name: sponsor-vetting
description: Vets an inbound sponsorship email by checking the company's X, YouTube, Trustpilot and funding, then logs a verdict. Use when a sponsor or brand-deal email arrives.
metadata:
  built-from-run: "2026-09-15"
---

# Sponsor vetting

## Inputs
- The forwarded sponsor email (company name, product, offer).

## Steps
1. Summarise the company in 3 lines: what it sells, where it's based, how old it is.
2. Check four signals, and give a link and one-line status for each:
   X account · YouTube presence · Trustpilot rating · funding raised.
3. Apply the rejection rule (below) before forming any other opinion.
4. If not rejected, compare against references/criteria.md and give a verdict: strong / maybe.
5. Log the row in the sponsors sheet: Date | Company | Signals (4) | Verdict | Link to email.
6. If the verdict is strong, email me a 5-line summary with the offer and the four links.

## Decision rules
- If two or more of the four signals are missing or in bad standing: verdict "No contact".
  Log it and don't email me.
- Never approve a company whose Trustpilot page you couldn't open. Mark that signal "missing".

## Known failure points and fixes
- Search returned a different company with a similar name → confirm the domain in the email matches.

## Changelog
- 2026-09-15: built from guided run on three real emails.
```

### Fresh-session test plan

Run each test in a **new** session. Tick it only if the skill loaded (Claude says it's using the skill, or you see it in the tool activity) **and** the output passes your right-and-wrong list.

| # | Test | Type exactly | Expect |
|---|---|---|---|
| T1 | Natural trigger | A realistic request that doesn't name the skill, e.g. "a brand just emailed about a sponsorship, is it worth it?" | Skill loads, full workflow runs |
| T1b | Reworded trigger | The same ask in different words, e.g. "can you check whether this sponsor is legit?" | Skill still loads |
| T2 | Direct call | `/sponsor-vetting` plus the input | Same result as T1 |
| T3 | New input | A different real case | Rules applied, no leftovers from the original run |
| T4 | Edge case | A case that should trip a rule (e.g. two signals missing) | The rule fires, correct hand-off |
| T5 | Negative | An unrelated request that shares a keyword | Skill does **not** load |

T1, T1b and T5 are the three trigger tests from [[Nate Herk - Build Skills Instead of Agents]] ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)–[04:44](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=284s)). He first has Claude audit every description for overlap ([04:25](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=265s)–[04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)); see [[Audit Skill Descriptions and Triggers]].

### Prompt 3: fix forward after a failure

```text
That run failed. Before fixing anything: at which step did it go wrong, what exactly
happened, and what error or output did you get?
```

Then, once you agree on the cause:

```text
Fix it and finish the task.
```

Then, once the output is correct:

```text
That's right now. Update .claude/skills/<name>/SKILL.md so this can't happen again:
change the step or rule that allowed it, add a line under "Known failure points and fixes",
and add a dated Changelog entry. Keep SKILL.md short. Show me the diff before saving.
```

### Context-cost check (Claude token counter)

Save as `count_skill_cost.py`. It needs `pip install anthropic` and `ANTHROPIC_API_KEY`. It assumes the description fits on one line, as in the skeleton.

```python
# count_skill_cost.py: vault starter. Usage: python count_skill_cost.py .claude/skills/<name>/SKILL.md
import re, sys
import anthropic

path = sys.argv[1]
model = sys.argv[2] if len(sys.argv) > 2 else "claude-opus-5"
text = open(path, encoding="utf-8").read()

m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
front = m.group(1) if m else ""
meta = "\n".join(l for l in front.splitlines() if l.startswith(("name:", "description:")))

client = anthropic.Anthropic()

def tokens(s: str) -> int:
    return client.messages.count_tokens(
        model=model, messages=[{"role": "user", "content": s}]
    ).input_tokens

baseline = tokens(".")  # subtract the fixed overhead of a one-character message
always_on = tokens(meta) - baseline
full = tokens(text) - baseline
print(f"As a skill, always in context (name + description): ~{always_on} tokens")
print(f"When the skill runs (whole SKILL.md):               ~{full} tokens")
print(f"If pasted into CLAUDE.md instead: ~{full} tokens held in every session")
```

Without an API key, open Claude Code, run `/context`, add the skill, start a new session and run `/context` again to see the difference.

## Done when

- [ ] One guided session contains at least one full, correct run, ideally two, with your corrections and rules stated explicitly.
- [ ] `.claude/skills/<name>/SKILL.md` exists, and Claude wrote it from that session, not from scratch.
- [ ] The frontmatter has a valid `name` (lowercase and hyphens, same as the folder) and a description that says what it does and when to use it.
- [ ] SKILL.md is short, and any long criteria or examples sit in `references/`.
- [ ] You've recorded always-on vs full token counts for the skill.
- [ ] Fresh-session tests T1–T5 pass, and any failures were fixed forward with a changelog entry.
- [ ] No secrets or one-off case details remain in the skill folder.
- [ ] It's committed (for a team) and marked `built` in your backlog.

## Pitfalls

- **Writing the skill before the run.** This is the anti-pattern the whole technique exists to avoid ([08:43](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=523s)). A skill-creator draft from a description alone is still "up front".
- **Codifying after one lucky pass.** Repeat on a second input first ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)).
- **Baking in the case.** Company names, dates and numbers from the teaching run turn into false rules. Prompt 2 tells Claude to turn them into inputs. Check anyway.
- **A description that never fires.** Ras Mic's skill loads because its description names when to use it ([30:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1802s)–[30:11](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1811s)). Test T1 and T5 rather than assuming.
- **One giant SKILL.md.** Jay E's strongest skills route to reference files instead ([08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)). The spec and docs suggest keeping SKILL.md under 500 lines (Beyond the source).
- **Moving the procedure into CLAUDE.md instead.** It then sits in every session ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)–[04:29](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=269s)). Keep CLAUDE.md for what the agent can't know and needs every time ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). See [[Keep CLAUDE.md Lean]].
- **Getting angry at failures instead of updating the skill.** Ras Mic treats each failure as the moment to improve the skill ([23:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1389s)–[23:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1398s)).
- **Trusting pasted or downloaded procedures.** Marketplace skills are an attack route ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)), and a tip copied from social media can hide a destructive command. Read every command before the first run (Beyond the source has the Snyk findings).
- **Reading his token numbers as Claude's.** He used OpenAI's tokenizer ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)). Claude counts differently, so measure with the script or `/context`.
- **Side-effect skills firing on their own.** For anything that sends, posts or deletes and that you only ever trigger by hand, set `disable-model-invocation: true`. Note that scheduled tasks can't use such a skill (Beyond the source).
- **Scaling before it works.** Don't build dozens of skills and subagents before one workflow is reliable ([14:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=863s)).

## Variations

- **Cowork or the Claude apps.** Use Customize, Skills, + and **Create with Claude** *after* doing the task in a normal chat, then point it at that chat's steps ([32:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1958s)–[32:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1961s)). Ask skill-creator to include an AskUserQuestion step for missing inputs ([33:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=2010s)). Keep the description under 200 characters for the apps (Beyond the source).
- **From a past session, not a live one.** Chase's version is "see how we just did that task, now turn it into a skill" ([07:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=451s)). You can resume an earlier successful session and run Prompt 2 there. To find such sessions in bulk, run [[Workflow Audit into Skills]].
- **From found content** (Jay E, [06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s)–[06:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=386s)). Paste the post or doc as the *starting instructions* in Prompt 1, run it on a real case with corrections, then write the skill from that run.
- **Learn from someone else's skill without installing it.** Give it to Claude and ask what your own skill should borrow, as Ras Mic does ([12:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=766s)). Then apply those ideas during your guided run.
- **Reference-rich design or brand skill.** Put visual references such as fonts and palettes in the folder, as Jay E does ([07:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=466s)–[08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)). See [[Build a Reference-Rich Skill]].
- **Formal evals.** Once the skill is stable, have skill-creator generate test cases and compare runs with and without the skill (Beyond the source).
- **From a creative output you liked** (Nate; see Other sources above).
  - **Where.** Stay in the session that made it.
  - **Examples.** Keep the winner in `references/examples.md`, and list the rejects as things to avoid.
  - **Rules.** A liked output doesn't say why it worked, so add your own expertise as rules.

  Prompt (vault starter content):

  ```text
  Carousel <N> is what I want every time; <M> is what I never want. Review how
  you made <N> here (prompt, model, settings, layout, copy structure, brand
  files) and write a skill that repeats that process for new topics. Save <N>
  as the reference example and list <M>'s traits to avoid. Keep <N>'s topic and
  wording out of the steps. Show the draft, then test it in a fresh session.
  ```
- **Run it from a button.** Jay E triggers finished skills headlessly from a dashboard ([09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s)). See [[Build an Agentic OS Dashboard]].

## Sources

- [[Ras Mic - How AI Agents and Claude Skills Work]]: progressive disclosure and context files ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)–[05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s)), sponsor-vetting walkthrough and method ([07:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=430s)–[13:31](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=811s)), recursive improvement ([20:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1242s)–[24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s)), tokenizer demo and context budget ([29:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1780s)–[31:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1887s)). Caption fixes: "Ross Mike" is Ras Mic, "open cloud" is OpenClaw, "agent.md" is AGENTS.md, "scale out MD file" is SKILL.md.
- [[Chase AI - The Agentic OS Setup for Claude Code]]: validate manually, then codify with skill-creator ([06:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=413s)–[07:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=451s)).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: skill-creator from pasted content ([05:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=354s)–[06:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=390s)), reference files ([06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s)–[08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)). Caption fix: "skill.mmd" is SKILL.md.
- [[Simon Pittman - Set Up Claude Cowork]]: creating skills in Cowork and the AskUserQuestion tip ([32:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1956s)–[33:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2015s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: update the skill after a better output ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)), commit skills for the team ([05:51](https://www.youtube.com/watch?v=jqoFP9QapXI&t=351s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]]: turning liked outputs into skills ([03:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=187s), [25:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1502s), [29:59](https://www.youtube.com/watch?v=yCACmFTiCto&t=1799s)). Caption fix: "make a scale" is "make a skill".
- [[Nate Herk - Build Skills Instead of Agents]]: the three trigger tests ([04:25](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=265s)–[04:48](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=288s)).
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]: extending a skill from pasted fal.ai docs ([11:36](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=696s)–[12:54](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=774s)). Caption fix: "file.ai" is fal.ai.

## Beyond the source

Not from the videos. Each item was checked at the linked page on 2026-09-15.

- **Where skills live in Claude Code.** Project: `.claude/skills/<skill-name>/SKILL.md` (commit it to share). Personal: `~/.claude/skills/<skill-name>/SKILL.md`. Plugin skills are invoked as `/plugin-name:skill-name`. Edits to SKILL.md reload within the running session. Personal skills don't sync to Cowork or cloud sessions. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **Frontmatter in Claude Code.** Frontmatter must start on line 1. `name` is optional in Claude Code, where the command name comes from the folder. `description` is recommended and is what Claude uses to decide when to load the skill; together with the optional `when_to_use`, it is truncated at 1,536 characters in the skill listing. `disable-model-invocation: true` limits a skill to `/name`, and such skills aren't used by scheduled tasks. `allowed-tools` pre-approves tools only until your next message. `metadata` is a free-form map that Claude Code doesn't act on, and it drops a value that isn't a map. The docs suggest keeping SKILL.md under 500 lines, with detail in supporting files. Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **The portable Agent Skills spec.** Both `name` and `description` are required. `name`: 1–64 characters, lowercase letters, numbers and hyphens, no leading, trailing or double hyphens, and it must match the folder name. `description`: 1–1,024 characters, saying what the skill does and when to use it. The optional directories are `scripts/`, `references/` and `assets/`. Disclosure is staged: about 100 tokens of metadata at startup, the body (under 5,000 tokens recommended) on activation, files as needed. Keep references one level deep. Validate with `skills-ref validate ./my-skill`. The skeleton above fills both required fields so it works outside Claude Code too. Source: [Agent Skills specification](https://agentskills.io/specification).
- **Skills in the Claude apps.** Skills are under Customize, Skills. Uploads are a ZIP with the skill folder at its root. The Help Center gives a 200-character maximum for the description and a 64-character maximum for the name, which is why Prompt 2 asks for under 200 characters. It also advises reviewing downloaded skills before enabling them and not hardcoding API keys. Source: [Claude Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
- **skill-creator does what Ras Mic describes.** Anthropic's skill-creator instructions say that when the workflow already happened in the conversation, it should first pull the tools used, step order, corrections and formats from that history. It then interviews for gaps, writes SKILL.md, runs test prompts with and without the skill, and tunes the description for triggering. In Claude Code, install it with `/plugin install skill-creator@claude-plugins-official`, then ask it to evaluate a skill. The docs also describe a manual baseline test: run a few realistic prompts, each in a fresh session, once with the skill available and once with it disabled. Sources: [anthropics/skills: skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **CLAUDE.md loading, corrected.** Claude Code loads CLAUDE.md into context at session start, not again on each turn. Each request then carries the full conversation, and prompt caching re-reads repeated content at a lower rate. The docs recommend moving specialised workflow instructions from CLAUDE.md into skills, which load on demand, and keeping CLAUDE.md under 200 lines. `/context` shows what's using space. Source: [Claude Code docs: Manage costs effectively](https://code.claude.com/docs/en/costs).
- **Counting Claude tokens.** The token-counting endpoint (`POST /v1/messages/count_tokens`) is free, subject to rate limits, and returns an estimate. Claude Opus 4.7 and later models, including Fable 5 and 5.1, use a newer tokenizer that produces roughly 30% more tokens for the same text than earlier Claude models. That's another reason not to reuse Ras Mic's OpenAI-tokenizer figures. Source: [Claude Platform docs: Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting).
- **Why the security warning is real.** Snyk's ToxicSkills study scanned 3,984 skills from ClawHub and skills.sh (as of 2026-02-05) and confirmed 76 malicious payloads by human review, aimed at credential theft, backdoors and data exfiltration. It advises auditing installed skills and rotating credentials that affected skills could reach. Source: [Snyk: ToxicSkills study](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/).

## Related

- Concepts: [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Context Window Management]] · [[CLAUDE.md as a Router]] · [[Verification Before Done]] · [[Loop Engineering]]
- Techniques: [[Workflow Audit into Skills]] · [[Skill Improvement Loop]] · [[Build a Reference-Rich Skill]] · [[Keep CLAUDE.md Lean]] · [[Grill Me Interview Skill]] · [[Build an Agentic OS Dashboard]]
- Tools & people: [[Claude Code]] · [[Claude Cowork]] · [[OpenClaw]] · [[Ras Mic]] · [[Greg Isenberg]] · [[Chase AI]] · [[Jay E]] · [[Simon Pittman]] · [[Nate Herk]]
- [[Home]]
