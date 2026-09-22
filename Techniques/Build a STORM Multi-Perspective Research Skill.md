---
type: technique
goal: "A Claude skill that researches a topic through five expert lenses, maps their contradictions, verifies every citation, and returns a consistent HTML briefing"
difficulty: intermediate
time_to_build: "An afternoon (run the four prompts once, then package)"
sources: ["[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]"]
tags: [topic/skills, topic/subagents, topic/retrieval, topic/verification, topic/loops, topic/claude-code]
---

# Build a STORM Multi-Perspective Research Skill

## Goal

Turn one research topic into a verified, multi-perspective HTML briefing: five expert lenses research in parallel, a contradiction map surfaces where they disagree, everything synthesizes into one self-contained report, and an adversarial pass verifies every citation before delivery. From [[Nate Herk - Stanford STORM Method as a Claude Research Skill]]. Concept: [[Multi-Perspective Research]].

## Use when

- You research broad or contested topics and a single-prompt answer would miss angles.
- You want a repeatable, house-styled briefing you can tailor to your business or reader.
- You're the decider but not the domain expert and want your blind spots surfaced ([11:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=696s)).

## Prerequisites

- [[Claude Code]] (desktop app or VS Code — Nate notes they behave the same, [10:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=600s)), or any agent that reads the Agent Skills format (`.codex` / `.agents` folders for other harnesses, [06:48](https://www.youtube.com/watch?v=Tj3018n5MVg&t=408s)).
- Understanding of skills as folders: [[Agent Skills]]. Build-from-a-run method: [[Build a Skill from a Successful Run]].
- Optionally web/research access for the lenses to browse (the subagents browse the web and use tools, [08:15](https://www.youtube.com/watch?v=Tj3018n5MVg&t=495s)). For grounded citations, pair with [[Set Up Claude Research Connectors]].

## Steps

1. **Run the four prompts by hand first** ([05:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=300s)). Prove the chain before packaging (the vault's standing rule: [[Build a Skill from a Successful Run]]):
   1. **Spin up the five lenses** on your topic — practitioner, academic, skeptic, economist, historian — each researching from its own background ([04:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=276s)).
   2. **Contradiction map:** ask where the perspectives contradict, which side has strong vs weak evidence, and have them analyze each other's outputs ([04:49](https://www.youtube.com/watch?v=Tj3018n5MVg&t=289s)).
   3. **Synthesize** the lenses and the contradictions into one report ([05:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=300s)).
   4. **Adversarial peer review + citation verification:** re-check the synthesis and verify every citation against its primary source ([05:31](https://www.youtube.com/watch?v=Tj3018n5MVg&t=331s)).
2. **Package the chain into a skill.** Ask Claude to capture the whole flow so one topic triggers it end to end and always returns the same HTML template ([05:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=306s)). Nate's SKILL.md summary: *"turns one topic into a verified multi-perspective HTML briefing; simulates five expert lenses, maps where they contradict, synthesizes one self-contained HTML report, then adversarially peer-reviews its own outputs and verifies every citation against its primary source before delivering."*
3. **Add a report template.** Put a `report-template.html` in the skill and reference it from SKILL.md so output is consistent every run ([05:50](https://www.youtube.com/watch?v=Tj3018n5MVg&t=350s)). The briefing should carry a 60-second summary and key findings **ranked by reliability**, each showing which lenses supported vs challenged it ([02:29](https://www.youtube.com/watch?v=Tj3018n5MVg&t=149s)).
4. **Add phase zero (scoping).** If the topic is vague, the skill should ask a few questions before kicking off — it should also capture the *reader* (who this is for and the decision they face) ([07:07](https://www.youtube.com/watch?v=Tj3018n5MVg&t=427s), [07:55](https://www.youtube.com/watch?v=Tj3018n5MVg&t=475s)).
5. **Make it self-critical about coverage.** Have the report name its assumptions and any *missing* lens (e.g. everyone reasoned from the owner's chair, no one from the customer's), so you can spin up that lens and run V3 ([03:01](https://www.youtube.com/watch?v=Tj3018n5MVg&t=181s)).
6. **Install it.** In Claude, put the markdown + HTML in the `.claude` folder — give the files to Claude and say "put this in the .claude folder" ([06:23](https://www.youtube.com/watch?v=Tj3018n5MVg&t=383s)). Invoke by name or in plain language ("run a storm research on X"); it triggers without a slash command ([07:36](https://www.youtube.com/watch?v=Tj3018n5MVg&t=456s)).
7. **Tailor it to you.** Add your business, goals and reader to the skill so every run answers "what should *we* do differently" ([03:14](https://www.youtube.com/watch?v=Tj3018n5MVg&t=194s)). Run it first on a topic you know well, so you can spot where to improve it ([10:35](https://www.youtube.com/watch?v=Tj3018n5MVg&t=635s)). Add or swap lenses (a "beginner in AI", a "content creator") ([11:00](https://www.youtube.com/watch?v=Tj3018n5MVg&t=660s)).

## Starter files & prompts

Folder shape (the vault's reconstruction from the video; the exact SKILL.md isn't shown):

```
.claude/skills/storm-research/
├── SKILL.md              # scope → 5 lenses in parallel → contradiction map → synthesis → verify citations → render template
└── report-template.html  # 60-sec summary, reliability-ranked findings, assumptions, missing-lens call-out, source ledger
```

- **Choosing the model per lens:** the subagents can run on Opus, or on Haiku/Sonnet to cut cost ([09:34](https://www.youtube.com/watch?v=Tj3018n5MVg&t=574s)). See [[Route Tasks to the Right Claude Model]].
- **Cross-check the output** by having a *different* model judge it, as Nate did with [[OpenAI Codex]] ([03:38](https://www.youtube.com/watch?v=Tj3018n5MVg&t=218s)).

## Done when

- [ ] One plain-language request runs the full pipeline and returns the templated HTML.
- [ ] The briefing ranks findings by reliability and shows supporting vs challenging lenses.
- [ ] Every citation is verified against its primary source and marked confirmed / corrected / demoted.
- [ ] The report names its assumptions and at least one missing lens.
- [ ] Lenses and the template are yours to edit, and the skill is tailored to your reader.

## Pitfalls

- **Packaging before the manual run works.** Prove the four prompts first ([05:06](https://www.youtube.com/watch?v=Tj3018n5MVg&t=306s)); a skill written cold lacks the context of a working run ([[Build a Skill from a Successful Run]]).
- **Same-model lenses agreeing for the wrong reasons.** Five personas on one model share blind spots ([[Multi-Agent Review and Scoring Loops]]); lean on the citation-verification pass and treat unanimous agreement cautiously.
- **Trusting V1.** The first pass carries wrong info by design; the value is in the verified V2 ([00:26](https://www.youtube.com/watch?v=Tj3018n5MVg&t=26s)).
- **Fixed lenses under-covering your topic.** Use the missing-lens call-out and edit the roster to fit the domain.

## Variations

- **Agent-team version.** Instead of subagents that can't talk to each other, run the lenses as an agent team that debates to consensus — richer, but "much more expensive" ([09:05](https://www.youtube.com/watch?v=Tj3018n5MVg&t=545s), [09:19](https://www.youtube.com/watch?v=Tj3018n5MVg&t=559s)). See [[Subagents and Agent Teams]].
- **Grounded-source version.** Point the lenses at research connectors so citations come from real databases, not the model's memory: [[Set Up Claude Research Connectors]], [[Grounding Research in Real Sources]].
- **Reusable council beyond research.** The same persona-council idea reviews scripts, ads or strategy: [[Multi-Agent Review and Scoring Loops]].

## Sources

- [[Nate Herk - Stanford STORM Method as a Claude Research Skill]] — the whole build.

## Related

- **Concepts:** [[Multi-Perspective Research]] · [[Subagents and Agent Teams]] · [[Verification Before Done]] · [[Grounding Research in Real Sources]] · [[Agent Skills]]
- **Techniques:** [[Build a Skill from a Successful Run]] · [[Multi-Agent Review and Scoring Loops]] · [[Set Up Claude Research Connectors]] · [[Route Tasks to the Right Claude Model]]
- **Tools:** [[Claude Deep Research]] · [[OpenAI Codex]]
- [[Home]]
