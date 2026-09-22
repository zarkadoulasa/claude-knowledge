---
type: tool
category: Claude Code feature (research via dynamic workflows)
website: https://code.claude.com/docs/en/
sources: ["[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]"]
tags: [topic/retrieval, topic/subagents, topic/loops, topic/claude-code, topic/agents]
---

# Claude Deep Research

## What it is

A built-in Claude Code research feature that launched alongside **dynamic workflows**. A deep-research command spins up a dynamic workflow that kicks off many background agents to research a topic. In the vault it's the baseline [[Nate Herk]] compares his STORM skill against. See [[Multi-Perspective Research]] and [[Subagents and Agent Teams]].

## How sources use it

- **[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]** runs it head-to-head with his STORM skill:
  - **What it does.** A deep-research command spins up a dynamic workflow that kicks off hundreds of background agents — 103 in his example ([01:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=95s)).
  - **The weak spots he hit.** It internalized everything and gave no output until asked; the resulting markdown was "decent but not that thorough," with few sources — two confirmed up top and a handful unconfirmed ([01:51](https://www.youtube.com/watch?v=Tj3018n5MVg&t=111s)).
  - **It's a stat brain-dump, not tailored.** Unlike STORM, it can't easily be steered toward your business and goals ([03:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=194s)).
  - **Cost and rate limits.** Running 100+ agents at once made it slower and pricier, and it got hit by API rate limits — a risk of spinning up that many agents ([04:04](https://www.youtube.com/watch?v=Tj3018n5MVg&t=244s), [04:20](https://www.youtube.com/watch?v=Tj3018n5MVg&t=260s)). His STORM run used ~12 agents and avoided that.
  - **Judged by [[OpenAI Codex]].** He asked Codex which output was better; Codex picked STORM's HTML briefing on all six axes (evidence quality, source diversity, thesis, actionability, risk control, content fit) ([03:38](https://www.youtube.com/watch?v=Tj3018n5MVg&t=218s)).

## Notes

- **He may have been unfair to it.** He concedes the Deep Research run got rate-limited and he "should take it easy" on that comparison ([04:18](https://www.youtube.com/watch?v=Tj3018n5MVg&t=258s)). Treat the head-to-head as one informal run, not a benchmark.
- **The distinction that matters** isn't STORM-vs-Deep-Research so much as *fixed, verified personas* vs *large uncontrolled fan-out*. STORM trades breadth of agents for consistency, tailoring and citation verification ([[Multi-Perspective Research]]).

## Beyond the source

*Not from the video. Checked 2026-09-21.*

- **Dynamic workflows** are Claude Code's mechanism for fanning one task out across many subagents at once; the vault's [[Subagents and Agent Teams]] note documents them (and `/batch`, agent view, cross-session messaging) with doc links. Deep Research is a research-oriented use of that machinery.
- **Rate limits on large fan-outs are expected** — spinning up 100+ concurrent agents can exhaust API/usage limits, which is the practical case for a smaller fixed-persona pipeline. See [[Subagents and Agent Teams]] (cost) and [[Route Tasks to the Right Claude Model]].
- Feature names and commands evolve; check the current Claude Code docs for the exact deep-research / dynamic-workflow invocation.

## Related

- **Concepts:** [[Multi-Perspective Research]] · [[Subagents and Agent Teams]] · [[Verification Before Done]] · [[Loop Engineering]]
- **Techniques:** [[Build a STORM Multi-Perspective Research Skill]] · [[Multi-Agent Review and Scoring Loops]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]]
- **Sources:** [[Nate Herk - Stanford STORM Method as a Claude Research Skill]]
- [[Home]]
