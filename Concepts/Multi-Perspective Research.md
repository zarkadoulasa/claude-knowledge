---
type: concept
aliases: ["STORM", "Multi-Lens Research", "Persona Research Council", "Five Perspectives"]
sources: ["[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]"]
tags: [topic/retrieval, topic/subagents, topic/agents, topic/verification, topic/skills, topic/loops]
---

# Multi-Perspective Research

## In one sentence

Run a research topic through several expert lenses instead of one prompt, map where they contradict each other, and let the disagreements surface the blind spots a single angle would miss — Stanford's STORM idea, rebuilt as a Claude skill.

## How it works

Based on [[Nate Herk - Stanford STORM Method as a Claude Research Skill]], who adapts Stanford's STORM method.

- **One prompt has blind spots.** Send off a single research prompt and you get one angle, with a bunch of holes in the plan ([00:44](https://www.youtube.com/watch?v=Tj3018n5MVg&t=44s)).
- **Five lenses, each catching a different hole.** His STORM skill simulates a practitioner, an academic, a skeptic, an economist and a historian; each finds a gap the others miss ([00:56](https://www.youtube.com/watch?v=Tj3018n5MVg&t=56s)). Having agents role-play their own backgrounds and areas of expertise is the point ([01:03](https://www.youtube.com/watch?v=Tj3018n5MVg&t=63s)).
- **The pipeline** (four chained prompts, then packaged as a skill):
  1. **Spin up the lenses** on the topic, in parallel ([04:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=276s), [07:15](https://www.youtube.com/watch?v=Tj3018n5MVg&t=435s)).
  2. **Contradiction map** — where do perspectives disagree, which side has strong vs weak evidence; the lenses analyze each other's outputs ([04:49](https://www.youtube.com/watch?v=Tj3018n5MVg&t=289s)).
  3. **Synthesize** everything into one self-contained report ([05:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=300s)).
  4. **Adversarial peer review + citation verification** before delivering ([05:31](https://www.youtube.com/watch?v=Tj3018n5MVg&t=331s)). See [[Verification Before Done]] and [[Grounding Research in Real Sources]].
- **Findings ranked by reliability.** Each key finding shows a reliability score and *which* lenses supported vs challenged it — e.g. 9/10, backed by the academic and skeptic, challenged by the practitioner and economist ([02:42](https://www.youtube.com/watch?v=Tj3018n5MVg&t=162s)). The disagreement is data, not noise.
- **It names its own gaps.** The report calls out the assumptions the briefing rests on and the *missing* lens — in his run, all five looked from the owner's chair, none from the customer or frontline employee, so he added a sixth lens and re-ran ([03:01](https://www.youtube.com/watch?v=Tj3018n5MVg&t=181s)).
- **Lenses are editable.** Add or swap them for your domain — a "beginner in AI" or a "content creator" lens for his work ([11:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=660s)).

### The durable principle

The specific skill matters less than the theory: the more perspectives you have researching and contradicting each other, the more holistic the result ([11:16](https://www.youtube.com/watch?v=Tj3018n5MVg&t=676s)). If you lack subject-matter expertise, **borrow it** — use agents to spin up little experts and a council that covers your blind spots ([11:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=696s)).

## When to use it — and when not to

**Use it when:**

- A topic is broad or contested and one angle would obviously miss something ([00:44](https://www.youtube.com/watch?v=Tj3018n5MVg&t=44s)).
- You're the decider but not the expert, and want the gaps in your own knowledge surfaced ([11:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=696s)).
- You want a repeatable, tailored briefing rather than a one-off stat dump ([03:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=194s)). Compare [[Claude Deep Research]].

**Hold off / watch out:**

- **Same-model lenses share blind spots.** Five personas on one Opus model can agree for the wrong reasons; [[Multi-Agent Review and Scoring Loops]] warns critics on one model miss the same things. The citation-verification pass partly offsets this, but agreement among personas is weaker evidence than it looks.
- **Fixed personas can under-cover a topic** whose key stakeholder isn't among your lenses — which is exactly why the "missing lens" call-out and editable lenses matter ([03:01](https://www.youtube.com/watch?v=Tj3018n5MVg&t=181s)).
- **The default five are generic.** Tailor them to a topic you actually know before trusting the output ([10:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=635s)).

## Perspectives from sources

- **[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]** — the full method above. He frames it as subagents doing the research (not agent teams), so the five lenses report to the main session but don't talk to each other ([08:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=514s)); an agent-team version would let them debate to consensus ([09:05](https://www.youtube.com/watch?v=Tj3018n5MVg&t=545s)). See [[Subagents and Agent Teams]].
- **Related in the vault:** persona/critic panels appear in [[Multi-Agent Review and Scoring Loops]] (AI LABS' orchestrator + critics) and in [[Nate Herk - Build Skills Instead of Agents]] (beginner / skeptical-buyer / audience-member subagents reviewing a script). [[AI LABS - Types of Claude Loops Explained]] likens agents-arguing to [[Andrej Karpathy]]'s LLM Council. STORM applies the same idea to *research generation*, not just review.

## Beyond the source

*Not from the video. Checked 2026-09-21.*

- **STORM's origin.** STORM ("Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking"), Shao et al., Stanford OVAL, NAACL 2024. It discovers perspectives on a topic, simulates perspective-guided question–answer conversations grounded in retrieved sources, builds an outline, then writes a long article. A later variant, Co-STORM, adds a collaborative human-in-the-loop discourse. — [arXiv 2402.14207](https://arxiv.org/abs/2402.14207), [github.com/stanford-oval/storm](https://github.com/stanford-oval/storm)
- **The "25% more organized" figure** ([00:02](https://www.youtube.com/watch?v=Tj3018n5MVg&t=2s)) comes from STORM's human/automated evaluation vs a retrieval-augmented baseline; trace it to the paper's tables before quoting it as a hard number.

## Related

- **Concepts:** [[Subagents and Agent Teams]] · [[Verification Before Done]] · [[Grounding Research in Real Sources]] · [[Agent Skills]] · [[Loop Engineering]]
- **Techniques:** [[Build a STORM Multi-Perspective Research Skill]] · [[Multi-Agent Review and Scoring Loops]]
- **Tools:** [[Claude Deep Research]] · [[OpenAI Codex]]
- **Sources:** [[Nate Herk - Stanford STORM Method as a Claude Research Skill]]
- **People:** [[Nate Herk]] · [[Andrej Karpathy]]
- [[Home]]
