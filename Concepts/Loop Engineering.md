---
type: concept
aliases: ["Agent Loops", "Ralph Loop"]
sources: ["[[AI LABS - Types of Claude Loops Explained]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tags: [topic/loops, topic/verification, topic/subagents, topic/agents, topic/claude-code, topic/automation, topic/scheduling, topic/skills, topic/memory]
---

# Loop Engineering

## In one sentence

You stop steering the agent one prompt at a time and instead design a loop (do the work, check it, decide what's next) that runs until a stop condition holds. The skill lies in choosing the loop that fits the job: what it remembers between passes, who or what judges "done", and what it costs. [[AI LABS - Types of Claude Loops Explained]] defines the idea at [00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s) and argues that loops only waste tokens when the loop type is wrong for the job ([00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s)).

## How it works

### Three parts of every loop (vault framing)

The sources describe loops in different vocabularies. The vault reads them as three dials. This framing is ours, not any one creator's:

| Dial | Question | Examples from the sources |
|---|---|---|
| **Trigger** | What starts the next pass? | The previous turn ending (`/goal`), a time interval (`/loop`), a schedule or event (routines) |
| **Judge** | Who decides the work is done or good enough? | A small model reading the conversation, a test suite, specialist critic agents, a score-only reviewer, a checker script |
| **Memory** | What carries over from one pass to the next? | Nothing (stateless), a lessons journal, a JSON score log, run logs in a vault |

[[AI LABS - Types of Claude Loops Explained]] mostly varies the judge and the memory. [[Nate Herk - 32 Tricks to Level Up Claude Code]] and [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] mostly talk about the trigger (`/loop`). [[Chase AI - The Agentic OS Setup for Claude Code]] is about memory: logging runs so later runs improve.

### Deterministic vs non-deterministic loops

AI LABS splits loops by whether the outcome can be checked ([01:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=73s)):

- **Deterministic.** You know the target in advance, so the agent has a reliable way to test its own work and keeps going until it passes ([01:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=79s)).
- **Non-deterministic.** No reliable self-check exists, so something else has to judge the work ([01:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=87s)).

They call this split broad: each type can be built many ways, and the build changes what it can do ([01:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=96s)). In practice a deterministic job can run in a simple loop anchored to tests, while a non-deterministic one needs reviewers, rubrics or scorers.

### The five loop types (AI LABS)

"Cost" appears only where the video gives it.

| Type | Memory between passes | Who judges | Best use | Cost, as stated | Build it |
|---|---|---|---|---|---|
| **Stateless** (Ralph, `/goal`) | None; nothing is learned ([01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s)) | With `/goal`, a smaller model (Haiku) checks the work against the prompt and reprompts ([02:26](https://www.youtube.com/watch?v=8wsM0euQOvc&t=146s)) | Features with hard, checkable requirements such as tests ([02:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=168s)) | Not stated | [[Tests-First Goal Loop]] |
| **Learning** | A `learning.md` journal inside the skill folder ([06:41](https://www.youtube.com/watch?v=8wsM0euQOvc&t=401s)) | A skill-improver agent comparing runs with and without the skill ([06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s)) | Improving a reusable skill or workflow ([05:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=307s)) | Not stated | [[Skill Improvement Loop]] |
| **Multi-agent review** | The orchestrator's own context across rounds ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)) | Four specialist critics (factual, domain, safety, style), fixes applied each round ([08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s), [08:54](https://www.youtube.com/watch?v=8wsM0euQOvc&t=534s)) | Any review, coding or not, that needs several perspectives ([08:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=513s)) | Not stated | [[Multi-Agent Review and Scoring Loops]] |
| **Verification** | Findings saved to a JSON file ([10:45](https://www.youtube.com/watch?v=8wsM0euQOvc&t=645s)) | A reviewer with no edit tools that only returns a score; the implementer tries to raise it ([09:34](https://www.youtube.com/watch?v=8wsM0euQOvc&t=574s), [10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s)) | A thorough quality pass on a large finished app ([11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s)) | Fan-out version: very slow and token-hungry. Single reviewer: far cheaper ([10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s), [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s)) | [[Multi-Agent Review and Scoring Loops]] |
| **Workflow improvement** | A JSON file of scores per round ([12:47](https://www.youtube.com/watch?v=8wsM0euQOvc&t=767s)) | A rubric scorer out of 100, plus a process optimizer that critiques the loop itself ([12:10](https://www.youtube.com/watch?v=8wsM0euQOvc&t=730s), [12:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=740s)) | Building an app part by part while refining the workflow ([12:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=756s), [13:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=782s)) | Not stated | [[Multi-Agent Review and Scoring Loops]] |

Two distinctions from the video are worth holding onto:

- **Stateless is the base layer.** Every other type is built on it ([01:44](https://www.youtube.com/watch?v=8wsM0euQOvc&t=104s)).
- **Learning ≠ workflow improvement.** The learning loop improves one skill, one part of the process. The workflow loop improves the process as a whole ([11:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=706s)).

### The judge is the weak point

Every source that goes into detail ends up arguing about who gets to say "done".

- **A model with no yardstick.** `/goal` leaves completion entirely to a model with no standard to measure against. That is why AI LABS writes tests before asking Claude to build anything ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s), [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s)).
- **Tests have to come first.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] says that if Claude implements before it writes tests, the tests are shaped to pass its own code ([09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)). He adds type checkers and linters as extra checks ([09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)).
- **The same channel's later critique.** In [[AI LABS - The Unlazy Skill for Lazy Agents]], AI LABS names the weakness of each earlier fix:
  - Ralph's finish line is just text the agent writes ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)).
  - `/goal`'s judge reads the conversation rather than the work, so it can drift from what you needed ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)).
  - Their own task-list loops had real checks, but the agent graded them itself ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)).

  All three hold up in a fresh context and weaken deep into a long session ([04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)). Their fix is a gates file: a checker script runs each proof command and records the evidence ([07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s)), and the parent re-runs each subagent's checks ([08:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=515s)). See [[Evidence-Gated Completion Ledger]] and [[Agent Laziness]].
- **A lightweight in-session loop.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] uses no extra agents. Claude designs a site, screenshots it, fixes it, and repeats for about three passes before showing him a first version ([09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s), [09:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=559s)). He also puts verification steps into the to-do list, with a rule not to move on until Claude is 95% confident ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s), [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)).
- **A benchmark as the yardstick.** [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] gives a design loop a reference screenshot ([09:54](https://www.youtube.com/watch?v=NAumQObJEwM&t=594s)); three critic subagents judge against it until the output hits the mark ([10:19](https://www.youtube.com/watch?v=NAumQObJEwM&t=619s)). He calls it his version of the Gauntlet Loop ([08:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=522s)); for the published pattern, see "The Gauntlet Loop as published" in [[Multi-Agent Review and Scoring Loops]]. Build it with [[Benchmark-Driven Design Critique]].
- **Evidence from outside the draft, ideally a metric.** [[Nate Herk - Build Skills Instead of Agents]] wants evidence beyond Claude rereading its own work, such as a test result, a source or persona feedback ([08:02](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=482s)). Better still is an objective success metric the agents iterate towards ([08:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=510s)).

*Vault reading:* the judges form a ladder of trust:

1. The agent's own claim
2. A text marker (Ralph)
3. A judge model reading the transcript (`/goal`)
4. The agent grading real checks
5. A separate agent or script that runs the checks and records the evidence

Climb only as far as the job needs. See [[Verification Before Done]].

### Time-triggered loops: `/loop`, reminders and schedules

- **[[Nate Herk - 32 Tricks to Level Up Claude Code]]:**
  - `/loop` re-runs a prompt on an interval in the same session, e.g. checking a deployment every five minutes ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s), [12:03](https://www.youtube.com/watch?v=jqoFP9QapXI&t=723s)).
  - Other uses: watching a PR, checking error logs or polling a build. It runs in the background and speaks up only when something needs you ([12:08](https://www.youtube.com/watch?v=jqoFP9QapXI&t=728s), [12:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=732s)).
  - Plain-language one-off reminders work too ([12:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=736s)).
  - His caveat: loops last three days ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)). The current docs say seven (Beyond the source). For longer schedules he uses desktop scheduled tasks, where each run is a fresh session without the conversation's context ([12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s)).
- **[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]:**
  - He calls `/loop` an AI cron job ([18:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1080s)) and uses it to keep side projects moving while he's away ([18:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1092s)).
  - His automations:
    - A daily pick of an open GitHub issue, implemented and left as a PR ([18:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1106s))
    - A security and bug sweep that files what it finds as issues ([18:36](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1116s))
    - Feature brainstorming from the code, PRs and issues ([18:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1126s))
  - Automations can also fire on events ([18:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1135s)).
  - *Vault note:* multi-day unattended work fits routines or desktop tasks better than a session-scoped `/loop` (Beyond the source).
- **[[Chase AI - The Agentic OS Setup for Claude Code]]:** once a skill repeats, turn it into an automation. You can simply ask Claude Code, or set up a Routine in Claude Desktop that runs the skill on a schedule ([11:25](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=685s), [11:31](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=691s)).

See [[Routines and Scheduled Tasks]] and [[Schedule Recurring Claude Tasks]].

### Self-improving loops: learning from past runs

- **AI LABS's two self-improving types.**
  - *Learning loop:* runs a skill, observes, improves it and records every lesson, so real use later avoids past failures ([05:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=316s), [05:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=325s)).
  - *Workflow-improvement loop:* adds a process optimizer that reviews each iteration and suggests how to make the loop better ([12:24](https://www.youtube.com/watch?v=8wsM0euQOvc&t=744s)).
  - *Safety gap:* each learning-loop round launches a separate background Claude session that doesn't stop to ask for permission ([06:20](https://www.youtube.com/watch?v=8wsM0euQOvc&t=380s)). The video doesn't discuss that risk. Current docs reserve permission-free runs for isolated containers and VMs (Beyond the source).
- **Chase's definition.** In [[Chase AI - The Agentic OS Setup for Claude Code]], loop engineering *is* the self-improving part: record what happened, and let loops see past iterations to improve future runs ([02:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=154s)).
  - His order: audit your work, turn it into skills, automate what repeats, then ask whether a loop makes sense for that use case ([13:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=801s)).
  - The loop is a self-improvement step added to an automation, tied to memory and state ([12:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=725s), [12:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=733s)).
  - So outputs have to be logged in one place where the loop can see past runs ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s), [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s)).
  - He closes on the same point: log everything so Claude can reference it and improve ([30:44](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1844s)).
- **Tension (vault).** Nothing in either video shows a person reviewing what the agent writes into its own memory. Unreviewed lessons can bloat context or lock in wrong conclusions. See [[Agent Memory Patterns]] and [[Skill Improvement Loop]].

### Orchestrator or direct agent communication

- **AI LABS chose an orchestrator.** [[AI LABS - Types of Claude Loops Explained]] says agent teams, where agents message each other, give more of an LLM Council feel. They still use an orchestrator, because one agent must hold the earlier rounds' context to coordinate ([09:09](https://www.youtube.com/watch?v=8wsM0euQOvc&t=549s), [09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)). They cite [[Andrej Karpathy]]'s LLM Council as the idea behind multi-agent review ([07:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=466s)), but describe it as agents arguing, which isn't how the repo works (Beyond the source).
- **Nate on agent teams.** In [[Nate Herk - 32 Tricks to Level Up Claude Code]]:
  - Teammates share a task list, message each other and hand out work, and you can talk to any of them directly ([14:44](https://www.youtube.com/watch?v=jqoFP9QapXI&t=884s), [14:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=892s)).
  - Teams cost more and run longer, but give a more cohesive result on big projects ([14:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=899s)).
  - He says plain subagents can't talk to each other ([14:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=881s)). That's out of date (Beyond the source).
- **Unlazy's orchestrated mode.** In [[AI LABS - The Unlazy Skill for Lazy Agents]], each leaf task goes to a fresh subagent that knows only the plan and its own gates ([08:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=507s)). That keeps attention narrow, which matters because a growing history dilutes focus ([02:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=123s), [02:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=142s)).

See [[Subagents and Agent Teams]].

### Cost: pick the loop for the job

- **AI LABS.** Loops burn tokens when the type is wrong for the job ([00:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=7s), [00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s)). Keep fan-out review for a large, finished app; otherwise a single reviewer takes less time and far fewer tokens ([11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s), [11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s)).
- **The Coding Sloth.** `/goal` is B tier on lower plans and A tier with high limits ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)). Every subagent runs as its own complete conversation, so on the $20 plan a modest multi-agent run can exhaust the limit before the work finishes ([20:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1212s)).
- **Unlazy run.** Dispatching one task at a time ran 3–4 hours and produced only a login page ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s), [10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s)). With parallel dispatch, 10 agents built the app in about two hours ([12:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=720s)). At that scale they suggest routing easy tasks to a cheaper model ([12:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=733s)).
- **Iteration cost decides autonomous loop or human in the loop.** In [[Chase AI - GPT-6 Astra Motion Design in After Effects]], a 15–20 second motion graphic can take 10–20 minutes to render ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)), so he aligns on a storyboard first ([02:47](https://www.youtube.com/watch?v=C8dWdic-oK4&t=167s)). He advises against looping these videos unless you really know what you're doing ([07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s)); a human reviews each pass instead of the agent checking every iteration against the storyboard ([07:42](https://www.youtube.com/watch?v=C8dWdic-oK4&t=462s)).
- **Stop and say why when a loop stalls.** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] describes Ouroboros re-running its checks after each fix so working parts stay intact ([08:08](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=488s)). If the agent stops making progress or hits its attempt limit, the tool reports why the work stopped ([08:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=497s)). Stall patterns are under Beyond the source.

## When to use it — and when not to

| Situation | Loop to reach for | Basis |
|---|---|---|
| A feature whose requirements you can express as tests | Stateless: `/goal` with tests written first. See [[Tests-First Goal Loop]] | AI LABS [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s); Coding Sloth [19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s) |
| Watching a deploy, PR or build during a session | `/loop` on an interval | Nate [11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s) |
| Recurring work that must run for days without you | A routine or desktop scheduled task, not `/loop` | Nate [12:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=748s); docs (Beyond the source) |
| A skill you reuse but don't trust | Learning loop. See [[Skill Improvement Loop]] | AI LABS [05:35](https://www.youtube.com/watch?v=8wsM0euQOvc&t=335s) |
| A review that needs several lenses (code, docs, content) | Multi-agent critic loop | AI LABS [07:36](https://www.youtube.com/watch?v=8wsM0euQOvc&t=456s), [08:33](https://www.youtube.com/watch?v=8wsM0euQOvc&t=513s) |
| A quality bar on a large, finished codebase | Verification loop; fan-out only at this scale | AI LABS [11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s) |
| A multi-part build process you'll repeat | Workflow-improvement loop | AI LABS [13:02](https://www.youtube.com/watch?v=8wsM0euQOvc&t=782s) |
| An automation whose outputs should get better over time | Log runs, then add a self-improvement step | Chase [22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s) |
| Long, many-part work where the agent claims "done" too early | Evidence-gated ledger with fresh subagents. See [[Evidence-Gated Completion Ledger]] | Unlazy [08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s) |
| Design that should match an admired reference | Benchmark-anchored critic loop, with a round cap. See [[Benchmark-Driven Design Critique]] | Jack [10:19](https://www.youtube.com/watch?v=NAumQObJEwM&t=619s) |
| Subjective copy such as a script or an ad | Persona panel; revise only recurring issues. See [[Multi-Agent Review and Scoring Loops]] | Nate [07:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=472s) |
| Slow, taste-judged creative output (renders of 10–20 minutes) | No autonomous loop. Storyboard first, then a few human-reviewed passes | Chase [07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s), [06:51](https://www.youtube.com/watch?v=C8dWdic-oK4&t=411s) |
| A long run that could spin without progress | A stall rule and an attempt cap that stop and say why | AI LABS repos [08:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=497s) |
| A small change, or a tight usage plan | No loop. One specific prompt plus a check | *Vault inference* from the Coding Sloth's plan-dependent tiers ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)) and AI LABS's cost warning |

## Where sources disagree

- **Real engineering or hype?**
  - [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] mocks the loop trend as people rediscovering the for loop ([15:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=939s)) and reinventing old ideas with new labels ([16:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=968s)). Yet he rates `/loop` and `/goal` well.
  - AI LABS frames loop engineering as moving from writing prompts to building a system that runs the loop ([00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s)).
  - Chase names loop engineering as one of five under-the-hood fundamentals ([00:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=14s)), but calls skills arguably the most powerful thing in Claude Code ([04:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=289s)) and builds loops on the foundation of skills and automations ([12:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=740s)–[12:28](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=748s)).
  - *Vault reading:* all three agree the value comes from ordinary engineering (tests, checks, logs), not the label.
- **Is `/goal` a good judge?**
  - [[AI LABS - Types of Claude Loops Explained]] (July 2026) calls `/goal` the best stateless loop once tests exist ([02:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=137s), [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)).
  - Six weeks later, [[AI LABS - The Unlazy Skill for Lazy Agents]] says its judge reads the conversation, not the work, and can drift ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)).
  - The docs back up the mechanism: the evaluator only reads what's in the transcript. They also say a condition with a stated command check puts real output there for it to read. Both videos are right in part (docs details under Beyond the source).
- **What "loop engineering" means.**
  - AI LABS: let the system run the loop itself ([00:48](https://www.youtube.com/watch?v=8wsM0euQOvc&t=48s)), in five types.
  - Chase: record runs so future runs improve ([02:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=154s)).
  - Anthropic sorts loops by trigger instead (Beyond the source).
- **How long `/loop` lasts.**
  - Nate: three days ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)).
  - The Coding Sloth runs daily automations with it ([18:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1106s)).
  - The docs: session-scoped, and recurring tasks expire after seven days (Beyond the source).
- **Can subagents coordinate?**
  - Nate says subagents can't talk to each other ([14:41](https://www.youtube.com/watch?v=jqoFP9QapXI&t=881s)).
  - AI LABS routes everything through an orchestrator on purpose ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)).
  - Current docs let named subagents message each other, so the orchestrator is now a design choice, not a constraint (Beyond the source).
- **Orchestrator or team for big work?** AI LABS prefers an orchestrator for continuity across rounds ([09:19](https://www.youtube.com/watch?v=8wsM0euQOvc&t=559s)). Nate finds teams more cohesive on big projects, at higher cost ([14:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=899s)).
- **Loop creative work, or keep a human judging?**
  - [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] lets critics loop on a design until it hits the benchmark ([10:19](https://www.youtube.com/watch?v=NAumQObJEwM&t=619s)). His "one shot" email ([10:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=638s)) was one prompt, with the rounds inside the skill (vault reading).
  - [[Nate Herk - Build Skills Instead of Agents]] automates persona review but stays the final judge on taste ([08:45](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=525s)).
  - [[Chase AI - GPT-6 Astra Motion Design in After Effects]] keeps a human on each slow render ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)), though in [[Chase AI - The Agentic OS Setup for Claude Code]] he layers loops on automations ([12:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=733s)).
  - *Vault reading:* pass cost and a concrete bar decide it. An HTML email with a reference screenshot is cheap to redo and has a bar; a 20-minute render judged on taste has neither.

## Perspectives from sources

- [[AI LABS - Types of Claude Loops Explained]]: the main taxonomy.
  - The loop type decides the token bill ([00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s)).
  - Deterministic vs non-deterministic split ([01:13](https://www.youtube.com/watch?v=8wsM0euQOvc&t=73s)).
  - Five types: stateless, learning, multi-agent review, verification and workflow improvement ([01:52](https://www.youtube.com/watch?v=8wsM0euQOvc&t=112s)–[13:06](https://www.youtube.com/watch?v=8wsM0euQOvc&t=786s)).
  - For unattended runs: tests first, plus a CLAUDE.md rule to save each working version ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)).
  - No agent, command or rubric files are shown on screen, and no results are measured.
- [[AI LABS - The Unlazy Skill for Lazy Agents]]: a critique of how completion gets judged.
  - Ralph, `/goal` and self-graded task lists all leave the agent or its transcript as the judge ([03:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=224s)–[04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)).
  - Their answer: gates proven by commands, and fresh subagents with parallel dispatch ([07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s), [12:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=720s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: a skeptic with a budget.
  - Mocks the hype ([15:39](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=939s)).
  - Uses `/loop` for daily side-project automations ([18:26](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1106s)).
  - Gives `/goal` a condition such as all tests passing with no type errors ([19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s)).
  - Rates `/goal` and subagents by how many tokens your plan allows ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s), [20:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1223s)).
- [[Chase AI - The Agentic OS Setup for Claude Code]]: loops are the self-improving layer.
  - It sits on top of skills and automations ([11:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=708s)).
  - It depends on logging past runs in one place ([22:47](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1367s)).
  - He covers it only briefly and points to his previous video for details ([11:53](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=713s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: small, practical loops.
  - `/loop` monitors and reminders ([11:57](https://www.youtube.com/watch?v=jqoFP9QapXI&t=717s)–[12:16](https://www.youtube.com/watch?v=jqoFP9QapXI&t=736s)).
  - A screenshot-and-fix pass inside one session ([09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s)).
  - Agent teams for big, cohesive work ([14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)).
  - A dated three-day loop limit ([12:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=742s)).
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: three benchmark-anchored design critics ([10:08](https://www.youtube.com/watch?v=NAumQObJEwM&t=608s)); no stop rule or cost shown.
- [[Nate Herk - Build Skills Instead of Agents]]: persona review, or better an objective metric; your first look should come after several agent passes ([08:55](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=535s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]]: slow, taste-judged renders get a human, not a loop ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: Ouroboros hides its checks from the builder ([07:58](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=478s)) and explains stalled stops.

## Beyond the source

*Not from the videos. Each item was checked at the linked page on 2026-09-15.*

- **Anthropic's own loop taxonomy.** A Claude blog post (30 June 2026, Delba de Oliveira and Michael Segner) defines loops as agents repeating cycles of work until a stop condition is met. It sorts them by trigger:
  - turn-based: you prompt;
  - goal-based: `/goal`;
  - time-based: `/loop` and `/schedule`;
  - proactive: events or schedules with no person in real time.

  It favours deterministic completion criteria such as tests passed or a score threshold. It recommends a reviewer with fresh context because it isn't swayed by the main agent's reasoning. It advises starting simple and piloting before scaling. That complements AI LABS's split by memory and judge. Source: [Getting started with loops](https://claude.com/blog/getting-started-with-loops).
- **How `/goal` actually judges.** `/goal` wraps a session-scoped prompt-based Stop hook.
  - After every turn, a small fast model (Haiku by default on the Claude API) reads the condition and the conversation. It returns *not yet met*, *met* or *impossible*.
  - The evaluator calls no tools, so it can only judge what Claude has surfaced.
  - The docs advise one measurable end state, a stated check (e.g. a test command exiting 0), constraints, and an optional turn cap such as "or stop after 20 turns".
  - `/goal` doesn't change the permission mode; run it in auto mode for unattended turns.

  Source: [Claude Code docs: /goal](https://code.claude.com/docs/en/goal).
- **The gating ladder in Anthropic's guide.** The best-practices page lists increasingly strict ways to gate the stop:
  1. Ask for the check in the prompt.
  2. Set it as a `/goal` condition.
  3. Enforce it with a Stop hook script. Claude Code overrides the hook after 8 consecutive blocks.
  4. Have a verification subagent or workflow try to refute the result.

  It also warns that a reviewer asked to find gaps usually finds some even in sound work. Tell reviewers to flag only gaps that affect correctness or requirements. Sources: [best practices](https://code.claude.com/docs/en/best-practices), [hooks guide](https://code.claude.com/docs/en/hooks-guide).
- **`/loop` today.**
  - Tasks are session-scoped and restored on `--resume` or `--continue`. A self-paced `/loop` isn't restored.
  - Recurring tasks expire seven days after creation. A session holds up to 50 scheduled tasks.
  - Leaving out the interval lets Claude pick a delay between one minute and one hour each time. A bare `/loop` runs a built-in maintenance prompt, or your `loop.md` (`.claude/loop.md`, else `~/.claude/loop.md`) if you've written one.
  - For durable schedules the docs point to cloud routines (no machine needed, 1-hour minimum interval), Desktop scheduled tasks, or GitHub Actions.

  Source: [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks).
- **Ralph.** Geoffrey Huntley described the technique on 14 July 2025 as a shell `while` loop that feeds the same prompt file to the agent over and over. His guidance is one task per loop and tests as backpressure. Source: [ghuntley.com/ralph](https://ghuntley.com/ralph/). Anthropic's `ralph-wiggum` plugin does the same with a Stop hook: the loop ends when a `--completion-promise` phrase appears, and `--max-iterations` is the recommended safety cap. Source: [plugin README](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md).
- **LLM Council, accurately.** Karpathy's project runs three stages. Several models answer independently, each ranks the others' anonymised answers, and a chairman model writes the final answer. The models don't argue directly. He describes it as an unsupported weekend project. Source: [github.com/karpathy/llm-council](https://github.com/karpathy/llm-council).
- **Subagents vs agent teams now.**
  - Subagents that Claude names when it spawns them can message each other with `SendMessage`.
  - Agent teams are experimental and off by default (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). They use significantly more tokens, and the docs suggest starting with 3–5 teammates.

  Sources: [subagents](https://code.claude.com/docs/en/sub-agents), [agent teams](https://code.claude.com/docs/en/agent-teams).
- **Dynamic workflows for big fan-outs.** Claude writes a JavaScript script that orchestrates subagents in the background. Limits: up to 16 concurrent agents and 1,000 per run. Saved workflows live in `.claude/workflows/`, and a "Large workflow" warning appears past 25 agents or 1.5M projected tokens. Source: [dynamic workflows](https://code.claude.com/docs/en/workflows).
- **The older pattern names.** Anthropic's December 2024 "Building effective agents" names two patterns:
  - *evaluator-optimizer:* one model generates while another critiques in a loop. It fits when clear evaluation criteria exist and refinement measurably helps.
  - *orchestrator-workers:* a central model splits the work and hands it to workers.

  It notes that agentic systems trade extra latency and cost for better task performance, and advises adding complexity only when it demonstrably improves outcomes. Source: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- **Skipping permissions.** `bypassPermissions` (`--dangerously-skip-permissions`) is intended only for isolated containers and VMs. For hands-off runs elsewhere, the docs point to auto mode, where a classifier model reviews actions instead of prompting. Source: [permission modes](https://code.claude.com/docs/en/permission-modes).
- **Ouroboros stall detection.** The README lists four stagnation patterns: spinning, oscillation, no drift and diminishing returns. A generation that repeats the one two steps earlier counts as oscillation, and there is a hard cap of 30 generations. Source: [github.com/Q00/ouroboros](https://github.com/Q00/ouroboros).
- **Rollback isn't free.** Claude Code checkpoints cover only Claude's file-tool edits. Changes made through bash aren't tracked, and subagent edits usually aren't restored, so use git for real rollback. Source: [checkpointing](https://code.claude.com/docs/en/checkpointing).

## Related

- Build it: [[Tests-First Goal Loop]] · [[Multi-Agent Review and Scoring Loops]] · [[Benchmark-Driven Design Critique]] · [[Skill Improvement Loop]] · [[Evidence-Gated Completion Ledger]] · [[Build Verification into Every Task]] · [[Schedule Recurring Claude Tasks]] · [[Workflow Audit into Skills]] · [[Configure Safe Autonomy Permissions]]
- Concepts: [[Verification Before Done]] · [[Routines and Scheduled Tasks]] · [[Agent Laziness]] · [[Subagents and Agent Teams]] · [[Agent Memory Patterns]] · [[Agent Skills]] · [[Context Window Management]] · [[Permissions and Approval Gates]] · [[Agentic OS]] · [[Plan Before Executing]]
- Tools and people: [[Claude Code]] · [[AI LABS]] · [[The Coding Sloth]] · [[Chase AI]] · [[Nate Herk]] · [[Andrej Karpathy]] · [[Jack Roberts]]
- Sources: [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Chase AI - The Agentic OS Setup for Claude Code]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] · [[Nate Herk - Build Skills Instead of Agents]] · [[Chase AI - GPT-6 Astra Motion Design in After Effects]] · [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]
- [[Home]]
