---
type: tool
category: AI research search engine / Claude connector
website: https://consensus.app/
sources: ["[[David Stuckler - Claude Connectors and Skills for Academic Research]]"]
tags: [topic/retrieval, topic/rag, topic/mcp, topic/verification]
---

# Consensus

## What it is

An AI-powered academic search engine that surfaces findings from peer-reviewed papers, available to Claude as a connector. In the vault it's [[David Stuckler]]'s primary research connector — the tool he reaches for to pull real, citable sources instead of hallucinated references. See [[Grounding Research in Real Sources]].

## How sources use it

- **[[David Stuckler - Claude Connectors and Skills for Academic Research]]** — his most-used research connector ([02:02](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=122s)).
  - **Why he trusts it despite the hallucination worry:** Consensus has brokered agreements with publishing houses, so it returns full-text sources, some a university may not even have ([02:10](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=130s)).
  - **Not sponsored.** He takes no kickbacks and warns about influencers who do; Consensus gives up to ~10 free searches, then paid ([02:19](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=139s), [02:30](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=150s)).
  - **Where it sits:** on the same pedestal as Google Scholar in his search strategy, but as a *complement* — coverage is partial, so don't rely on it alone ([02:37](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=157s), [05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)).
  - **How he queries it:** "Check the Consensus connector for studies" + map the gaps; it returns real studies with citations he can open and verify — e.g. a meta-analysis of 62 studies ([04:39](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=279s), [04:52](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=292s)).
  - **Add it:** Customize → Connectors → Add → Browse connectors → Consensus ([02:44](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=164s)). Setup steps: [[Set Up Claude Research Connectors]].

## Notes

- **Forensic vs browsing.** He uses Consensus/PubMed when he knows exactly what he wants; Google Scholar when he wants to browse a literature by relevance and citation count ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)).
- **Grounding ≠ correctness.** Consensus prevents invented citations, not misreadings. Keep a verify-the-source step: [[Verification Before Done]].

## Beyond the source

*Not from the video. Checked 2026-09-21.*

- **What it is officially.** Consensus is an AI search engine over ~200M+ academic papers (built on the Semantic Scholar corpus) that extracts and summarizes findings and shows a "consensus meter" on yes/no questions. It offers a connector/MCP integration for Claude. Free-tier feature caps (advanced searches, AI summaries per month) change over time; verify current limits before quoting the "10 free searches" figure. — [consensus.app](https://consensus.app/), [Anthropic connectors](https://www.anthropic.com/connectors)
- **Trust.** As with any connector that fetches external content, vet it and grant least privilege — see [[Connecting Claude to External Tools]].

## Related

- **Concepts:** [[Grounding Research in Real Sources]] · [[Connecting Claude to External Tools]] · [[Verification Before Done]]
- **Techniques:** [[Set Up Claude Research Connectors]] · [[Build a STORM Multi-Perspective Research Skill]]
- **Sources:** [[David Stuckler - Claude Connectors and Skills for Academic Research]]
- **People:** [[David Stuckler]]
- [[Home]]
