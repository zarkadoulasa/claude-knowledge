---
type: source
title: "Anthropic Engineer Explains: What to Build Instead of AI Agents"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=HIRDzMtuWFk
video_id: HIRDzMtuWFk
published: 2026-09-13
duration: "9:47"
ingested: 2026-09-15
topics: [agent skills, skills vs agents, scripts inside skills, skill descriptions and triggering, progressive disclosure, skill improvement, verification, persona review, portability]
tags: [source/youtube, topic/skills, topic/agents, topic/claude-code, topic/verification, topic/loops, topic/subagents, topic/portability, topic/context, topic/agentic-os]
---

# Nate Herk - Build Skills Instead of Agents

> **Creator:** [[Nate Herk]] · **Published:** 2026-09-13 · **Length:** 9:47 · [Watch on YouTube](https://www.youtube.com/watch?v=HIRDzMtuWFk)

## TL;DR

[[Nate Herk]] retells the Anthropic talk "Don't Build Agents, Build Skills Instead" by [[Barry Zhang]] and [[Mahesh Murag]]: keep one general agent and add skills to it, the way a phone keeps its processor and OS and adds apps.

He then adds four practices (table below): save working scripts, write sharp non-overlapping descriptions, fix corrections where they'll stick, and verify with outside evidence.

It's talk to camera, with no files shown, and the "news" framing is off (see Caveats).

## Key takeaways

- **One agent runtime, many skills.** Model = processor, runtime = operating system, skills = apps ([00:58](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=58s)). See [[Agent Skills]] and [[Agentic OS]].
- **Portability has limits.** The process travels between agents, but quality doesn't: models read skills differently, and no skill makes a weaker model match a stronger one ([06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)).
- **Let the agent look first.** Your first look should be the agent's fourth to sixth ([08:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=537s)). See [[Verification Before Done]].

## The four practices at a glance

| # | Practice | What to do | Where | Vault note |
|---|---|---|---|---|
| 1 | Save proven code | Move a chat script into `scripts/`; SKILL.md runs it; run twice to confirm | [01:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=86s) | [[Build a Reference-Rich Skill]] |
| 2 | Sharp descriptions | One job per skill, users' words, what + when; obvious / reworded / unrelated tests | [02:58](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=178s) | [[Audit Skill Descriptions and Triggers]] |
| 3 | Fix the process | Classify the cause, fix it in the smallest lasting place, rerun | [04:55](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=295s) | [[Skill Improvement Loop]] |
| 4 | Built-in verification | Criteria, inspect, fix, repeat; report what's unverified | [06:43](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=403s) | [[Build Verification into Every Task]] |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=0s) They stopped building

- The hook: Anthropic engineers "just said" they stopped building agents. He promises four practices behind a system that improves on its own ([00:00](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=0s)).

### [00:23](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=23s) Why your phone?

- **Agents aren't dead.** Zhang and Murag stopped building a separate agent per job because the underlying agent turned out more general than expected ([00:24](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=24s)).
- **Phone analogy.** A few companies make the processor and OS, and you pick the apps. The AI stack is starting to look similar ([00:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=36s)).
- **Add, don't rebuild.** [[Claude Code]] already reads files, writes code and calls tools. Give it a skill with the job's process, context, scripts and examples ([01:15](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=75s)).

### [01:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=86s) Stop repeating this

- **Anthropic's example.**
  - **Problem:** Claude kept rewriting a nearly identical Python script to style slides. That wasted tokens and gave different results from run to run ([01:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=90s)).
  - **Fix:** the team had Claude save the script in the skill as a tool for its future self ([01:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=106s)). This is DRY, "don't repeat yourself" ([01:58](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=118s)).
- **Nate's version.** His carousel skill points Claude at renderers and templates that already work, so only the text changes ([02:13](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=133s)).
- **Prompt (paraphrased).** Save that script in the skill's scripts folder, make SKILL.md run it, then rerun and verify ([02:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=149s)).
- **Test.** Run the same task twice and confirm the saved file is the one being called ([02:42](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=162s)). Compare the key parts: the AI text around the script can still vary, but one fresh guess is now proven code ([02:44](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=164s)).

### [03:03](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=183s) Claude's guessing game

- **Progressive disclosure.** His picture is a mechanic who takes out only the tools the job needs ([03:04](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=184s)).
  - **At startup:** only names and descriptions load ([03:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=209s)).
  - **On a match:** SKILL.md loads.
  - **When needed:** references and scripts load, which limits context rot ([03:33](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=213s)).
- **Descriptions.** Overlapping vague ones ("help with content" vs "create marketing assets") leave Claude guessing ([03:54](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=234s)). A good one names the output, the inputs and the trigger phrases, as in his LinkedIn carousel example ([04:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=245s)). Give each skill one job, use users' words, and keep two skills from competing for the same request ([04:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=257s)).
- **Audit (paraphrased).** Claude Code lists each skill's job, its trigger and its overlaps, then rewrites only the ambiguous descriptions ([04:25](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=265s)).
- **Three tests** ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)):
  1. An obvious request should fire the skill.
  2. A reworded request should still fire it.
  3. An unrelated request must not.

### [04:56](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=296s) You lost it

- **Lessons die with the chat.** Close the chat after a correction and the lesson is probably lost. "Fix it" repairs the output, not the process ([05:07](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=307s)).
- **Retracing.** When an agent misses a file that exists, he has it retrace its search and explain the miss, then fixes the routing or the skill ([05:14](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=314s)). See [[CLAUDE.md as a Router]].
- **Procedural memory.** He relays Anthropic's continuous-learning framing: a "guarantee" that a future Claude can reuse whatever Claude writes down ([05:28](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=328s)). Skills hold procedural knowledge, not conversation history ([05:37](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=337s)). See [[Agent Memory Patterns]].
- **Where each fix goes** ([05:44](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=344s)):

  | Cause | Fix goes to |
  |---|---|
  | Wrong process | SKILL.md |
  | Missing voice, brand or examples | A reference file |
  | Repeated mistake | An explicit rule |

- **Retro (paraphrased).** Classify the cause as process, missing context, weak rule or unreliable code. Update the smallest lasting place, then rerun and verify ([05:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=357s)).

### [06:14](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=374s) Model proof?

- **Portable, not model-proof.** Agent Skills is an open format, so the same folder works in [[OpenAI Codex]] or [[Hermes Agent]] ([06:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=390s)).
- **Cross-harness test.** If a skill falls apart elsewhere, look for hidden assumptions, missing examples or model-specific instructions ([06:34](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=394s)).

### [06:43](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=403s) 70% problem

- **Don't ship the first attempt.** He calls this the most important practice ([06:43](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=403s)). AI does 70–80% of the job and leaves you the rest ([07:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=425s)). Build your own checks into the skill instead ([07:11](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=431s)):
  - **Slides:** render them as images, fix anything cropped or unreadable, and rerender ([07:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=437s)).
  - **Research:** match claims to primary sources and cut anything unverifiable ([07:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=446s)).
  - **Script or ad:** have a beginner, a skeptical-buyer and an audience-member subagent review it ([07:38](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=458s)). Act only on issues raised more than once, then review again ([07:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=472s)).
- **Outside evidence.** Self-approval isn't verification. Evidence must come from outside the draft: screenshots, tests, sources, reference examples or other agents ([07:59](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=479s)).
- **Instruction (paraphrased).** Define acceptance criteria, then draft, inspect, fix and repeat. Return with what was checked and what remains unverified ([08:11](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=491s)).
- **Better still: an objective metric.** Agents iterate until they hit it ([08:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=510s)). See [[Loop Engineering]]. You still judge taste and strategy ([08:45](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=525s)).

### [09:01](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=541s) What now?

- A recap of the four practices, then promotion.

## Caveats & disagreements

**About the video**

- **Not news.** "Just said" ([00:00](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=0s)) refers to a November 2025 talk (see Beyond the source).
- **Attribution.** The recap credits everything to Anthropic engineers ([09:01](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=541s)), but only some of it is theirs.
  - **From the talk:** the analogy, the slide-script example, progressive disclosure, continuous learning and the "guarantee" line.
  - **Nate's own:** the audit prompt, trigger tests, cause taxonomy, retracing, persona panel and acceptance criteria.
- **"The two people who created agent skills"** ([00:24](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=24s)). Anthropic's post lists three authors (see Beyond the source).
- **"Guarantee"** ([05:28](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=328s)). The word is the talk's, about the standard format keeping notes reusable, not skills improving themselves (Anthropic's post calls that a hope).
- **No demo, and the 70–80% figure is anecdotal.**
- **Promotion:** a paid course, communities and affiliate links. None are reproduced here.

**Versus existing vault notes**

- **[[Agent Skills]] and [[Tool-Agnostic Context Files]].** Both cite [[AI LABS - Claude Design Skills for Beautiful Sites]] claiming the same result in any agent ([01:02](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=62s)). Nate says only the process ports ([06:16](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=376s)), and Anthropic's authoring guide agrees (see Beyond the source).
- **[[Verification Before Done]].** It records his earlier 95%-confidence self-check from [[Nate Herk - 32 Tricks to Level Up Claude Code]] ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)). Here he rejects self-approval ([07:59](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=479s)).
- **[[Multi-Agent Review and Scoring Loops]].** It warns that critics on the same model share blind spots. That makes agreement among personas ([07:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=472s)) weaker evidence than Nate implies.
- **[[Skill Improvement Loop]].** It writes lessons to Gotchas and learning.md, using a different taxonomy. Nate names four causes ([05:57](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=357s)) but only three fix destinations, and his "add a rule" pulls against that note's advice to edit rather than append.
- **[[Build a Skill from a Successful Run]].** Its T1 and T5 tests matched two of his three. His reworded test ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)) is now its T1b, with a pointer to his library-wide audit.
- **[[Nate Herk - 32 Tricks to Level Up Claude Code]].** It treated skills as single files ([05:34](https://www.youtube.com/watch?v=jqoFP9QapXI&t=334s)). Here they're folders ([03:33](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=213s)).

## Build from this

1. **Script promotion**, checked by two runs and the tool log: [[Build a Reference-Rich Skill]], [[Build a Skill from a Successful Run]].
2. **Description audit** with three trigger tests per skill: [[Audit Skill Descriptions and Triggers]].
3. **Post-run retro** that routes each cause to SKILL.md, `references/`, rules or `scripts/`: [[Skill Improvement Loop]].
4. **Verification block** that ends in "checked / not verified": [[Build Verification into Every Task]], [[Evidence-Gated Completion Ledger]].
5. **Persona panel** that keeps only recurring issues: [[Multi-Agent Review and Scoring Loops]].
6. **Cross-harness check:** [[Port a Claude Code Brain to Other Agents]].

## Resources mentioned

- **The talk** by Zhang and Murag ([00:24](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=24s)); **harnesses** [[Claude Code]], [[OpenAI Codex]], [[Hermes Agent]] ([06:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=390s)).

## Beyond the source

*Not from the video. Checked 2026-09-15.*

- **The talk.** AI Engineer Code Summit, New York, 19–22 Nov 2025; posted by AI Engineer on 2025-12-08 (16:22). Its captions confirm the analogy, the slide-script example and the "guarantee" line. Trigger testing appears there only as future tooling. <https://www.ai.engineer/code/2025>, <https://www.youtube.com/watch?v=CEvIs9y1uog>, <https://lilys.ai/en/notes/agent-skills-20251225/build-skills-not-agents>
- **Anthropic's Agent Skills post** (2025-10-16), by Zhang, Keith Lazuka and Murag.
  - Names and descriptions load first, and SKILL.md loads when relevant.
  - Agents creating and evaluating their own skills is framed as a hope.
  - Skills became an open standard on 2025-12-18.

  <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- **The open standard.**
  - `name`: up to 64 characters (lowercase letters, digits, hyphens), matching the folder name.
  - `description`: up to 1,024 characters, saying what the skill does and when to use it.
  - Listed clients include Claude Code, Codex and Hermes Agent.
  - Codex reads skills from `.agents/skills` and `~/.agents/skills`.

  <https://agentskills.io/specification>, <https://learn.chatgpt.com/docs/build-skills>
- **Anthropic's authoring guide** backs Nate:
  - Write descriptions in third person, covering what and when.
  - Utility scripts beat generated code for reliability, tokens and consistency.
  - Test with every model you plan to use.
  - Build at least three evaluations.

  <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
- **Claude Code triggering.**
  - `description` plus `when_to_use` is capped at 1,536 characters in the skill listing.
  - If the listing overflows its budget, the least-invoked skills lose their descriptions first.
  - `/skill-doctor` (v2.1.252+) reports each skill's context cost and usage.
  - `claude plugin eval` can trigger-test plugin skills.

  <https://code.claude.com/docs/en/skills>

## Transcript notes

| Caption | Corrected |
|---|---|
| "Enthropic", "adanthropic" | Anthropic, at Anthropic |
| "Barry Jien", "Mahesh Marog" | Barry Zhang, Mahesh Murag |
| "cloud code", "cla", "clawed" | Claude Code / Claude |
| "And team kept watching" | Anthropic's team (likely) |
| "dry or dr" | DRY |
| "skill.mmd", "skills script folder" | SKILL.md, the skill's `scripts/` folder |
| "context rod", "codeex", "sub aents" | context rot, Codex, subagents |
| [music] at 04:26, 04:35, 06:08, 07:27, 07:39, 08:05 | Prompts reconstructed *(partly unclear in captions)* |

## Related

- **People:** [[Nate Herk]], [[Barry Zhang]], [[Mahesh Murag]]
- **Same creator:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **Compare:** [[Ras Mic - How AI Agents and Claude Skills Work]], [[AI LABS - Types of Claude Loops Explained]], [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- [[Home]]
