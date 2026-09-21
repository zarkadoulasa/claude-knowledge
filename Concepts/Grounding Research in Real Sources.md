---
type: concept
aliases: ["Citation Grounding", "No Hallucinated References", "Source Verification", "Anti-Hallucination Research"]
sources: ["[[David Stuckler - Claude Connectors and Skills for Academic Research]]", "[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]", "[[Nate Herk - Build Skills Instead of Agents]]"]
tags: [topic/retrieval, topic/rag, topic/verification, topic/mcp, topic/skills]
---

# Grounding Research in Real Sources

## In one sentence

To stop Claude inventing references, tie every research claim to a real, retrievable source — pull from a research connector that returns clickable papers, and verify each citation against its primary source before you trust it.

## How it works

Two sources attack the same problem from opposite ends: getting real sources *in*, and checking sources *out*.

### 1. Retrieve from a real database, not the model's memory

[[David Stuckler - Claude Connectors and Skills for Academic Research]]:

- **The problem.** Over the past few years AI has become prone to making up references that look real but aren't ([01:31](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=91s)).
- **The fix is a connector with real coverage.** Research connectors give Claude "vision" into real peer-reviewed sources ([01:25](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=85s)). [[Consensus]] has brokered agreements with publishing houses, so it returns full-text sources — some a university may not even have ([02:10](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=130s)). PubMed retrieves real articles for health queries ([02:51](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=171s)).
- **The prompt habit.** Tell it where to look: "Check the Consensus connector for studies," then ask it to map gaps ([04:39](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=279s)).
- **The checkable output.** Claude returns real studies with citations you can open and read — go right to the source and confirm it isn't a hallucination ([04:56](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=296s)).
- **Coverage is partial.** Consensus is a complement to Google Scholar, not a replacement; don't rely on it alone ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)). See [[Set Up Claude Research Connectors]].

### 2. Verify the citations you already have

[[Nate Herk - Stanford STORM Method as a Claude Research Skill]] builds verification into the pipeline:

- **A dedicated verification pass.** After the first-pass agents produce findings, six more agents verify the facts ([02:26](https://www.youtube.com/watch?v=Tj3018n5MVg&t=146s)). The skill verifies **every citation against its primary source before delivering** ([05:43](https://www.youtube.com/watch?v=Tj3018n5MVg&t=343s)).
- **Confirm / correct / demote.** Each source is marked, so the first pass's wrong information gets caught and V2 is more trustworthy ([00:26](https://www.youtube.com/watch?v=Tj3018n5MVg&t=26s), [10:22](https://www.youtube.com/watch?v=Tj3018n5MVg&t=622s)).
- **Findings ranked by reliability**, showing which lenses supported vs challenged each ([02:42](https://www.youtube.com/watch?v=Tj3018n5MVg&t=162s)).

[[Nate Herk - Build Skills Instead of Agents]] states the rule this concept rests on: for research, match claims to primary sources and cut anything unverifiable ([07:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=446s)); self-approval isn't verification — the evidence must come from outside the draft ([07:59](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=479s)).

### The two halves fit together

Stuckler keeps hallucinated citations from entering (retrieve real sources); Nate catches the ones that slipped in (verify against primary sources). A robust research workflow does both. The vault's framing.

## When to use it — and when not to

- **Any factual or academic output** where a wrong citation costs you: add a real-source connector *and* a verification step.
- **Forensic vs browsing** (Stuckler's distinction): use a connector like Consensus/PubMed when you know what you're looking for; keep a relevance-ranked tool like Google Scholar for discovering adjacent work you didn't know to ask for ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)).
- **Don't over-trust a single connector.** Coverage is partial ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)); and don't trust a self-graded verification either — see the same-model caveat in [[Verification Before Done]].

## Perspectives from sources

- **[[David Stuckler - Claude Connectors and Skills for Academic Research]]** — grounding via connectors ([[Consensus]], PubMed, bioRxiv, clinical trials), with clickable sources as the proof of no hallucination.
- **[[Nate Herk - Stanford STORM Method as a Claude Research Skill]]** — grounding via a verification pass that confirms/corrects/demotes every citation against its primary source.
- **[[Nate Herk - Build Skills Instead of Agents]]** — the general principle: cut the unverifiable, and get evidence from outside the draft.

## Related

- **Concepts:** [[Connecting Claude to External Tools]] · [[Verification Before Done]] · [[Multi-Perspective Research]] · [[Semantic Search]] · [[Agent Skills]]
- **Techniques:** [[Set Up Claude Research Connectors]] · [[Build a STORM Multi-Perspective Research Skill]] · [[Build Verification into Every Task]]
- **Tools:** [[Consensus]] · [[Claude Deep Research]]
- **Sources:** [[David Stuckler - Claude Connectors and Skills for Academic Research]] · [[Nate Herk - Stanford STORM Method as a Claude Research Skill]]
- [[Home]]
