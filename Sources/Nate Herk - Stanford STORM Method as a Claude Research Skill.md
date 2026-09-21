---
type: source
title: "Stanford's Method Turns Claude Into a PHD Level Research Team"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=Tj3018n5MVg
video_id: Tj3018n5MVg
published: 2026-06-29
duration: "12:05"
ingested: 2026-09-21
topics: [STORM, multi-perspective research, subagents, agent teams, contradiction mapping, citation verification, deep research, dynamic workflows, HTML briefing, skills]
tags: [source/youtube, topic/subagents, topic/agents, topic/skills, topic/verification, topic/retrieval, topic/claude-code, topic/loops, topic/models]
---

# Nate Herk - Stanford STORM Method as a Claude Research Skill

> **Creator:** [[Nate Herk]] · **Published:** 2026-06-29 · **Length:** 12:05 · [Watch on YouTube](https://www.youtube.com/watch?v=Tj3018n5MVg)

## TL;DR

Nate rebuilds Stanford's **STORM** research method as a free Claude skill. Instead of one prompt with one angle, it runs a topic through five expert lenses — practitioner, academic, skeptic, economist, historian — maps where they contradict, synthesizes one self-contained HTML briefing, then adversarially peer-reviews itself and verifies every citation against its primary source (confirming, correcting or demoting each) before delivering.

He runs it against Claude Code's built-in **Deep Research** (which spun up ~100 agents and hit rate limits) and has [[OpenAI Codex]] judge the two; Codex prefers STORM's briefing on all six axes. Along the way he explains **subagents vs agent teams** and argues the real takeaway is the *principle*: borrow expertise, kill your blind spots.

## Key takeaways

- **More perspectives beat one prompt.** A single prompt has blind spots; five lenses each catch a hole the others miss ([00:44](https://www.youtube.com/watch?v=Tj3018n5MVg&t=44s)). See [[Multi-Perspective Research]].
- **Verification is baked in.** It peer-reviews its own output and checks every citation against the primary source, marking sources confirmed / corrected / demoted, so V2 earns more trust ([05:43](https://www.youtube.com/watch?v=Tj3018n5MVg&t=343s)). See [[Verification Before Done]] and [[Grounding Research in Real Sources]].
- **Subagents work for the main session and can't talk to each other; agent teams can — and are pricier.** ([08:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=514s)). See [[Subagents and Agent Teams]].
- **Fixed five personas beat a 100-agent fan-out on cost and reliability** here: ~12 agents total, "100% cheaper," and no rate limits ([04:04](https://www.youtube.com/watch?v=Tj3018n5MVg&t=244s)). See [[Claude Deep Research]].
- **The theory travels further than the skill.** Add or swap lenses for your own work; the durable lesson is borrowing subject-matter expertise you lack ([11:16](https://www.youtube.com/watch?v=Tj3018n5MVg&t=676s)).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=0s) What STORM builds

- Stanford's STORM has been shown in peer-reviewed testing to produce articles 25% more organized than the next-best method ([00:02](https://www.youtube.com/watch?v=Tj3018n5MVg&t=2s)). He put those principles into a free Claude skill ([00:09](https://www.youtube.com/watch?v=Tj3018n5MVg&t=9s)).
- Output is an HTML briefing assembled by five perspectives and verified ([00:13](https://www.youtube.com/watch?v=Tj3018n5MVg&t=13s)). At the bottom, sources are marked confirmed, corrected or demoted; on the first pass the briefing held some wrong info, so V2 is more trustworthy ([00:26](https://www.youtube.com/watch?v=Tj3018n5MVg&t=26s)).

### [00:42](https://www.youtube.com/watch?v=Tj3018n5MVg&t=42s) Why five perspectives beat one

- One prompt = one angle = blind spots ([00:44](https://www.youtube.com/watch?v=Tj3018n5MVg&t=44s)). STORM uses five: practitioner, academic, skeptic, economist, historian, each finding a hole the others miss ([00:56](https://www.youtube.com/watch?v=Tj3018n5MVg&t=56s)).
- He ties it to his "roast" skill and to using agent teams as a council to surface different perspectives ([01:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=74s)).

### [01:28](https://www.youtube.com/watch?v=Tj3018n5MVg&t=88s) STORM vs Claude's Deep Research

- Claude Code natively has a **Deep Research** feature that launched with dynamic workflows ([01:28](https://www.youtube.com/watch?v=Tj3018n5MVg&t=88s)); a deep-research command spins up a dynamic workflow kicking off hundreds of background agents — 103 in his example ([01:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=95s)).
- It internalized everything and gave no output until asked; the resulting markdown was decent but not thorough, with few sources ([01:51](https://www.youtube.com/watch?v=Tj3018n5MVg&t=111s)).
- He fed the same prompt to the STORM skill, which ran the five agents, converged their findings, flagged disagreements, then ran six more agents to verify the facts ([02:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=134s)).
- The HTML report: a 60-second summary and key findings **ranked by reliability** ([02:29](https://www.youtube.com/watch?v=Tj3018n5MVg&t=149s)) — e.g. "reliability high, 9/10", supported by the academic and skeptic, challenged by the practitioner and economist ([02:42](https://www.youtube.com/watch?v=Tj3018n5MVg&t=162s)).
- It also names the briefing's assumptions and the **missing sixth lens**: all five sat in the owner's chair (adoption, productivity, ROI), none in the customer's or frontline employee's seat ([03:01](https://www.youtube.com/watch?v=Tj3018n5MVg&t=181s)). You can then ask it to spin up that sixth lens and run V3 ([03:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=186s)).
- Unlike Deep Research's stat brain-dump, STORM can be **tailored to you** — put your business and goals in the skill so every run answers "what should *we* do differently" ([03:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=194s)).
- **Independent judge.** He put both into [[OpenAI Codex]] and asked which was better; Codex picked the HTML briefing on evidence quality, source diversity, thesis, actionability, risk control, and fit for video/content — all six ([03:38](https://www.youtube.com/watch?v=Tj3018n5MVg&t=218s)).
- **Cost.** STORM was faster and "100% cheaper": ~12 agents vs 100+ ([04:04](https://www.youtube.com/watch?v=Tj3018n5MVg&t=244s)). Deep Research also got hit by API rate limits — a risk of spinning up that many agents at once; STORM is always five personas ([04:20](https://www.youtube.com/watch?v=Tj3018n5MVg&t=260s)).

### [04:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=276s) The four prompts behind it

- **Prompt 1:** spin up the five angles for your research topic ([04:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=276s)).
- **Prompt 2 — contradiction map:** where do the perspectives contradict, which has strong vs weak evidence; makes them analyze each other's outputs ([04:49](https://www.youtube.com/watch?v=Tj3018n5MVg&t=289s)).
- **Prompts 3–4:** chain into synthesis, then peer review ([05:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=300s)).
- He ran the four-prompt chain manually, it worked, then packaged it into a skill so one topic triggers the whole thing and returns a consistent HTML template every time ([05:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=306s)).
- **SKILL.md summary:** turns one topic into a verified multi-perspective HTML briefing — simulates five expert lenses, maps contradictions, synthesizes one self-contained HTML report, **adversarially peer-reviews its own outputs, and verifies every citation against its primary source before delivering** ([05:31](https://www.youtube.com/watch?v=Tj3018n5MVg&t=331s)). A `report-template.html` in the skill keeps output consistent ([05:50](https://www.youtube.com/watch?v=Tj3018n5MVg&t=350s)).

### [06:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=366s) How to get the skill

- The skill + HTML template are free in his Skool community, under Classroom → all YouTube resources ([06:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=366s)).
- Install: give the markdown and HTML files to Claude and say "put this in the .claude folder" ([06:23](https://www.youtube.com/watch?v=Tj3018n5MVg&t=383s)).
- **"A skill is basically just a prompt"** — a master prompt; say "do storm research" and it reads the whole thing and runs it ([06:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=394s)).
- Works with Codex or any agent; in Claude it must live in `.claude`, but `.codex` / `.agents` folders serve other coding agents ([06:48](https://www.youtube.com/watch?v=Tj3018n5MVg&t=408s)).
- **Pipeline:** phase zero scopes the topic (it may ask questions first), then spins up the five lenses in parallel, maps contradictions, synthesizes, and runs adversarial peer-review verification to the output ([07:07](https://www.youtube.com/watch?v=Tj3018n5MVg&t=427s)).

### [07:26](https://www.youtube.com/watch?v=Tj3018n5MVg&t=446s) Live run: voice AI agents

- In the desktop app: "run a storm research for me on voice AI agents" ([07:30](https://www.youtube.com/watch?v=Tj3018n5MVg&t=450s)). No slash command, but the skill still invokes ([07:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=456s)).
- It restates the topic and the reader (he's an AI educator deciding whether voice AI agents are worth a video or just hype) ([07:55](https://www.youtube.com/watch?v=Tj3018n5MVg&t=475s)).
- The pipeline kicks off the five agents; clicking the economist shows the exact prompt the main session sent that subagent, and the subagent browsing the web and using tools ([08:15](https://www.youtube.com/watch?v=Tj3018n5MVg&t=495s)).

### [08:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=514s) Subagents vs agent teams

- **Subagents:** one main session (the Claude you talk to); all subagents work for it. The main session talks to the five, but the five can't talk to each other ([08:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=514s)).
- **Agent teams:** teams/councils that talk to the main session *and* to each other ([08:57](https://www.youtube.com/watch?v=Tj3018n5MVg&t=537s)). He likes spinning up a team to decide on ideas and having them debate and argue until they reach consensus ([09:05](https://www.youtube.com/watch?v=Tj3018n5MVg&t=545s)). Agent teams are much more expensive than subagents ([09:19](https://www.youtube.com/watch?v=Tj3018n5MVg&t=559s)).
- These subagents ran on **Opus 4.8**; you can run them on Haiku or Sonnet instead ([09:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=574s)).
- With all five lenses in, it maps contradictions, reads the report-template file, and verifies the citations and stats the first-pass agents produced ([09:45](https://www.youtube.com/watch?v=Tj3018n5MVg&t=585s)).
- Aside: he switched between the desktop app and VS Code; Claude works the same in both, just different UI — he used the desktop app to show the agents running ([10:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=600s)). The V2 report comes back verified, sources demoted/corrected/confirmed, with the reliability-ranked findings ([10:22](https://www.youtube.com/watch?v=Tj3018n5MVg&t=622s)).

### [10:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=635s) Final takeaways

- Grab the skill, put it in your own Claude, tailor it, and run it on a topic you know well so you can spot where to improve it ([10:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=635s)). Consider adding a sixth or seventh lens — for him, a "beginner in AI" or a "content creator" ([11:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=660s)).
- **The real point:** it's less about this specific skill or Stanford method than the theory — more perspectives contradicting each other yield more holistic research ([11:16](https://www.youtube.com/watch?v=Tj3018n5MVg&t=676s)). If you lack subject-matter expertise, borrow it: use agents to build little experts and a council that has your back ([11:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=696s)).

## Caveats & disagreements

- **The 25% claim is unverified in the video.** He cites "peer-reviewed testing" for "25% more organized" ([00:02](https://www.youtube.com/watch?v=Tj3018n5MVg&t=2s)) without naming the paper. See Beyond the source for what STORM's actual paper measured.
- **His skill ≠ Stanford's STORM system.** Stanford STORM is a specific research pipeline (perspective-guided question-asking + retrieval to write Wikipedia-style articles). Nate's skill borrows the multi-perspective *principle*; it isn't the Stanford codebase.
- **The Codex "judge" is a single, informal comparison.** One prompt, one run, an LLM grading two outputs — suggestive, not a benchmark. It also compares against a Deep Research run he admits he may have been hard on (rate-limited) ([04:20](https://www.youtube.com/watch?v=Tj3018n5MVg&t=260s)).
- **"A skill is just a prompt"** ([06:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=394s)) is the beginner framing. Skills are folders with frontmatter, references and scripts; see [[Agent Skills]] Beyond the source.
- **Same-model personas share blind spots.** Five lenses on the same Opus model can agree for the wrong reasons; [[Multi-Agent Review and Scoring Loops]] warns that critics on one model miss the same things. The citation-verification pass partly offsets this.

## Build from this

1. **The STORM skill itself** — five lenses, contradiction map, synthesis, adversarial verification, HTML template, tailored to you: [[Build a STORM Multi-Perspective Research Skill]].
2. **A citation-verification gate** for any research output, marking each source confirmed / corrected / demoted: [[Grounding Research in Real Sources]], [[Build Verification into Every Task]].
3. **A persona council** you can reuse beyond research (scripts, ads, strategy): [[Multi-Agent Review and Scoring Loops]], [[Subagents and Agent Teams]].

## Resources mentioned

- **Stanford STORM** research method ([00:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=0s)); **Claude Code Deep Research / dynamic workflows** ([01:28](https://www.youtube.com/watch?v=Tj3018n5MVg&t=88s)) → [[Claude Deep Research]]; **[[OpenAI Codex]]** as judge ([03:38](https://www.youtube.com/watch?v=Tj3018n5MVg&t=218s)); his free Skool community and tagged agent-teams/subagents videos (not reproduced); sponsor tools Glaido and Hostinger VPS (skipped).

## Beyond the source

*Not from the video. Checked 2026-09-21.*

- **What STORM actually is.** STORM ("Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking"), Shao et al., Stanford, NAACL 2024, generates Wikipedia-like articles by discovering perspectives on a topic and simulating perspective-guided question–answer conversations grounded in retrieved sources, then writing from the outline. The paper's human evaluation reported gains in organization and breadth over a baseline; the exact "25%" figure should be traced to the paper before quoting it as fact. — [arXiv 2402.14207](https://arxiv.org/abs/2402.14207), [github.com/stanford-oval/storm](https://github.com/stanford-oval/storm)
- **Deep Research and dynamic workflows** are Claude Code features; details and the subagent/agent-teams mechanics live in [[Claude Deep Research]] and [[Subagents and Agent Teams]] (both have doc-verified Beyond-the-source sections).
- **Opus 4.8** is the current top Claude model as of this ingest; running cheaper lenses on Haiku/Sonnet is the standard cost lever, echoed across the vault ([[Route Tasks to the Right Claude Model]]).

## Transcript notes

- Captions were clean. "storm" is consistently the STORM method. "steep research" ([04:19](https://www.youtube.com/watch?v=Tj3018n5MVg&t=259s)) → "deep research". "passive agents" ([09:58](https://www.youtube.com/watch?v=Tj3018n5MVg&t=598s)) → "first-pass agents". No product-name garbling of note.

## Related

- **People:** [[Nate Herk]]
- **Concepts:** [[Multi-Perspective Research]] · [[Subagents and Agent Teams]] · [[Verification Before Done]] · [[Grounding Research in Real Sources]] · [[Agent Skills]]
- **Techniques:** [[Build a STORM Multi-Perspective Research Skill]] · [[Multi-Agent Review and Scoring Loops]]
- **Tools:** [[Claude Deep Research]] · [[OpenAI Codex]] · [[Claude Code]]
- **Same creator:** [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[Nate Herk - Build Skills Instead of Agents]] · [[Nate Herk - Every Level of a Claude Second Brain]]
- **Compare:** [[David Stuckler - Claude Connectors and Skills for Academic Research]] (research grounding via connectors)
- [[Home]]
