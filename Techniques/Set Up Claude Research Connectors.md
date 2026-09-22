---
type: technique
goal: "Add research connectors so Claude pulls real, clickable peer-reviewed sources instead of hallucinating citations"
difficulty: beginner
time_to_build: "15–30 minutes"
sources: ["[[David Stuckler - Claude Connectors and Skills for Academic Research]]"]
tools: ["[[Consensus]]"]
tags: [topic/mcp, topic/retrieval, topic/verification, topic/claude-code]
---

# Set Up Claude Research Connectors

## Goal

Give Claude "vision" into real research databases so it returns sources you can open and verify, killing the hallucinated-reference problem. From [[David Stuckler - Claude Connectors and Skills for Academic Research]]. Concept: [[Grounding Research in Real Sources]]; the connector mechanics live in [[Connecting Claude to External Tools]].

## Use when

- You do literature searches, evidence reviews or any factual research with Claude.
- You've been burned by, or worry about, invented citations ([01:31](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=91s)).
- You want a forensic search — you know what you're looking for and want the real paper fast ([05:25](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=325s)).

## Prerequisites

- A Claude account (the Claude apps; Stuckler demos in the desktop/web UI, not the CLI).
- Accounts for any gated database you add (e.g. a Consensus login for its free searches).
- Judgement about connector trust — vet third-party/community connectors before installing: [[Connecting Claude to External Tools]] (least-privilege) and [[Build vs Install Third-Party Skills]].

## Steps

1. **Open the connector settings.** Left sidebar → Customize → Connectors ([01:04](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=64s)).
2. **Add [[Consensus]] first.** Top right → Add → Browse connectors → Consensus ([02:44](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=164s)). It brokers full-text access from publishing houses and gives up to ~10 free searches before paid ([02:10](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=130s), [02:30](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=150s)).
3. **Add the databases your field needs.** PubMed for health/biomedical work ([02:51](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=171s)); bioRxiv and clinical trials as needed ([03:01](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=181s)). Curate this list over time.
4. **Query by naming the connector.** Tell Claude where to look: "Check the Consensus connector for studies on X," then ask it to map the gaps ([04:39](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=279s)). For a forensic PubMed pull: "find me a study on \<specific question\>" ([05:25](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=325s)).
5. **Verify before you cite.** Open the actual paper it returns and confirm the claim is real — the whole point is that you *can* go to the source ([04:56](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=296s)). Fall back to Google Scholar for full text when a connector only shows an abstract.
6. **Keep Google Scholar for browsing.** Use it to discover adjacent, highly-cited work you didn't know to ask for; use connectors for targeted retrieval ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)). Treat Consensus as a complement, since coverage is partial ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)).

## Starter files & prompts

- **Grounding prompt:** *"Check the Consensus connector for peer-reviewed studies on \<topic\>. Summarize what they find, map the gaps in the literature, and give me a clickable citation for each claim so I can verify it. Don't include anything you can't source."*
- **Forensic prompt:** *"Using PubMed, find real studies on \<specific question\> and link the sources."*

## Done when

- [ ] At least one research connector (Consensus and/or PubMed) is added under Customize → Connectors.
- [ ] A test query returns real studies with citations you can open.
- [ ] You've confirmed one returned source actually says what Claude claimed.

## Pitfalls

- **Relying on one connector.** Coverage is partial; cross-check with Google Scholar ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)).
- **Assuming grounding = correctness.** A connector stops *invented* sources; it doesn't stop misreading a real one. Keep a verification step — see [[Grounding Research in Real Sources]] and [[Verification Before Done]].
- **Trusting an unvetted connector.** Community MCP connectors to PubMed/bioRxiv can fetch external content; treat them with least-privilege ([[Connecting Claude to External Tools]]).
- **Free-tier surprises.** Search caps (e.g. Consensus' ~10 free) change; check current limits.

## Variations

- **Pair with a research skill.** Feed grounded sources into a multi-perspective briefing: [[Build a STORM Multi-Perspective Research Skill]].
- **Package the prompt habit as an SOP skill.** If you run the same grounded-search-and-verify flow repeatedly, make it a skill: [[Build a Skill from a Successful Run]], [[Workflow Audit into Skills]].

## Sources

- [[David Stuckler - Claude Connectors and Skills for Academic Research]] — the connector setup and query habits.

## Related

- **Concepts:** [[Grounding Research in Real Sources]] · [[Connecting Claude to External Tools]] · [[Verification Before Done]] · [[Agent Skills]]
- **Techniques:** [[Build a STORM Multi-Perspective Research Skill]] · [[Build a Skill from a Successful Run]] · [[Configure Safe Autonomy Permissions]]
- **Tools:** [[Consensus]]
- [[Home]]
