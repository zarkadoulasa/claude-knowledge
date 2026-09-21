---
type: source
title: "How To Use Claude For Academic Research (My Actual AI Stack)"
creator: "[[David Stuckler]]"
channel: "Prof. David Stuckler"
url: https://www.youtube.com/watch?v=GWtx-d3dALQ
video_id: GWtx-d3dALQ
published: 2026-07-22
duration: "9:13"
ingested: 2026-09-21
topics: [research connectors, Consensus, PubMed, hallucinated citations, productivity connectors, skills as SOPs, topic validation, academic research]
tags: [source/youtube, topic/mcp, topic/retrieval, topic/skills, topic/claude-code, topic/verification, topic/context]
---

# David Stuckler - Claude Connectors and Skills for Academic Research

> **Creator:** [[David Stuckler]] · **Published:** 2026-07-22 · **Length:** 9:13 · [Watch on YouTube](https://www.youtube.com/watch?v=GWtx-d3dALQ)

## TL;DR

A publishing academic opens up his research stack in the Claude apps. The core move: add research **connectors** — [[Consensus]], PubMed, bioRxiv, clinical trials — so Claude pulls real peer-reviewed sources you can click through to, instead of hallucinating references. He then adds productivity connectors (Canva, Gmail/Outlook, Calendar, Todoist, Zoom, Miro), and packages his repeat workflows as **skills** (standard operating procedures), demoing a topic-validation skill.

It's a beginner-facing screen-share with a strong ethics-of-AI framing. Nothing technical is configured on screen; the topic-validation skill is proprietary and only shown running, not built.

## Key takeaways

- **Connectors give Claude "vision" into tools you already use** ([01:15](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=75s)), for two jobs: real sources, and productivity ([01:23](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=83s)). See [[Connecting Claude to External Tools]].
- **Research connectors are his answer to hallucinated citations.** Consensus, PubMed and friends return real studies with links you can open and verify ([04:56](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=296s)). See [[Grounding Research in Real Sources]].
- **Consensus sits beside Google Scholar, not above it.** Use Consensus/PubMed for forensic searches where you know what you want; keep Google Scholar for browsing a literature by relevance and citation count ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)).
- **Skills capture SOPs.** Turn a repeated procedure into a customized prompt Claude runs every time; ask Claude to build the skill for you ([06:29](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=389s)). See [[Agent Skills]].

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=0s) Intro

- Framing hook: if you're not using Claude skills and connectors for research, you're "living in the Stone Age" ([00:00](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=0s)). He's published 400+ peer-reviewed papers and reviews for a living ([00:06](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=6s)).
- Ethics note up front: he'll show practical things he actually does, staying on the right side of ethical AI use ([00:20](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=20s)).

### [00:51](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=51s) Why he switched to Claude

- He shifted from ChatGPT to Claude and says you'll see why by the end ([00:53](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=53s)). No head-to-head is actually shown; it's an assertion.

### [01:00](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=60s) Setting up connectors

- Open Claude, go to the left sidebar → Customize → Connectors ([01:04](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=64s)).
- **The mental model:** connectors give Claude "vision" into the tools and software you already use ([01:15](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=75s)).
- **Two purposes** ([01:23](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=83s)):
  1. Vision into real peer-reviewed sources, which "massively helps solve the hallucination problem" of AI inventing references ([01:31](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=91s)).
  2. Sync into email, to-do lists and other productivity tasks, so you can act in dead time from your phone ([01:40](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=100s)).
- **How to add one:** top right → Add, on any connector he shows; they're valuable and free ([01:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=115s)).

### [02:02](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=122s) The best research connectors

- **[[Consensus]]** — the one he uses most ([02:02](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=122s)). He was skeptical over hallucination, but Consensus has brokered agreements with publishing houses, so it gets full-text sources, some your university may not even have ([02:10](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=130s)).
- **No sponsorship.** He warns about influencers peddling AI products for kickbacks; he takes none, and isn't sponsored by Consensus or Claude ([02:19](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=139s)). Consensus gives up to 10 free searches, then it's paid ([02:30](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=150s)).
- It now sits on the same pedestal as Google Scholar in his search strategy ([02:37](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=157s)). Add it via Add → Browse connectors → Consensus ([02:44](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=164s)).
- **PubMed** — for health research; search and retrieve PubMed articles directly in Claude queries ([02:51](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=171s)).
- **bioRxiv and clinical trials** — other current picks; he's constantly curating the list ([03:01](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=181s)).

### [03:10](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=190s) Productivity connectors

- **Canva** — academic presentations. Claude can produce PowerPoint PDFs, but syncing to Canva makes them more beautiful and easier to modify ([03:11](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=191s)).
- **Gmail / Outlook** — check email, draft responses, load drafts and send; check tone, and with the right prompting get emails written in his own voice ([03:33](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=213s)).
- **Google Calendar** for scheduling on the go ([03:49](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=229s)); **Todoist** as a to-do app ([03:54](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=234s)); **Zoom** ([04:02](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=242s)); and **Miro** whiteboard, because many researchers he works with are visual ([04:08](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=248s)).

### [04:15](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=255s) Live example: real sources, no hallucinations

- Real case: why community college students flunk out at four-year universities, and what transition plans help ([04:19](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=259s)).
- **The prompt pattern:** "Check the Consensus connector for studies," then ask it to map out gaps ([04:39](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=279s)).
- Claude pulls real studies with citations — e.g. a meta-analysis of 62 studies ([04:52](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=292s)). You can open the actual paper and go to the source, so it's checkable, not hallucinated ([04:56](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=296s)). Sometimes full text is there; otherwise pop it into Google Scholar.

### [05:13](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=313s) Consensus vs Google Scholar

- **Google Scholar for browsing.** Like walking library shelves, you bump into papers you didn't know mattered ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)).
- **Consensus/PubMed for forensic search.** When he knows exactly what he wants — e.g. how much autism prevalence has risen over 20 years — Claude goes forensically into PubMed and pulls real sources faster than Google Scholar can ([05:25](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=325s)).
- He still likes Google Scholar's relevance sort and citation counts ([05:46](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=346s)). Consensus is partial coverage — a complement, not a replacement ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)).

### [06:03](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=363s) What Claude skills are

- Researchers need leverage, or you get one project, one paper and one burnt-out researcher ([06:03](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=363s)). You end up repeating the same tasks.
- **Skills capture SOPs** — set up a standard operating procedure and load it as a customized prompt to run every time ([06:29](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=389s)).
- **Claude can make the skill for you:** ask it to make a skill following your set of instructions ([06:37](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=397s)). He's made skills for peer review and topic validation that integrate with his course material ([06:48](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=408s)). Upload the skill, then invoke it later in a normal chat ([06:59](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=419s)).

### [07:05](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=425s) Topic validation skill demo

- His topic procedure has three phases: get in the topic neighborhood, test/validate the topic, then human judgment and vetting ([07:05](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=425s)).
- Typing `/` lets you pick which skill to use ([07:41](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=461s)). The skill first asks what kind of work it is — systematic review, dissertation, quantitative or qualitative — because the algorithm to find a topic differs ([07:47](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=467s)).
- It's wired to his own system, using a "convergence method" ([08:11](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=491s)) and steps like finding a nearest-neighbour paper, PICO to crystallize the topic, and duplication and feasibility tests ([08:16](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=496s)). It diagnoses the problem and tells you how to fix it.

### [08:28](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=508s) Get the free skill

- The topic-validator skill is linked in the description; download it and upload via Customize → Add a skill ([08:34](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=514s)).
- Closes on ethics again: he keeps testing and vetting these workflows so you stay "on the right side of angels" ([08:53](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=533s)), then promotes his mentorship community.

## Caveats & disagreements

- **No configuration shown.** He never opens a skill file, shows a SKILL.md, or configures a connector's permissions. "Connectors give Claude vision" is a good intuition, not a how-to.
- **The topic-validation skill is proprietary.** It's shown running, tied to his paid course's "convergence method", PICO, duplication and feasibility tests. The free download is a stripped "topic validator". You can't rebuild the full thing from the video — so the vault treats it as a build *idea*, not a buildable Technique.
- **"Switched from ChatGPT to Claude" is unbacked.** No comparison is shown ([00:53](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=53s)).
- **Free-tier limits shift.** "Up to 10 free Consensus searches" ([02:30](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=150s)) is a product detail that can change; see [[Consensus]] Beyond the source.
- **Coverage is partial.** He's explicit that Consensus doesn't cover everything and shouldn't be relied on alone ([05:55](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=355s)) — a healthy caveat that most connector demos skip.

## Build from this

1. **A research-connector setup** that grounds citations in real sources and a prompt habit for querying it: [[Set Up Claude Research Connectors]].
2. **A peer-review or topic-validation SOP skill** distilled from a procedure you already run by hand: [[Build a Skill from a Successful Run]] and [[Workflow Audit into Skills]]. His convergence/PICO/feasibility phases are a template for the *shape* of such a skill, not its contents.
3. **A verify-the-citation step** for any research answer, matching claims to primary sources and cutting the unverifiable: [[Grounding Research in Real Sources]], [[Build Verification into Every Task]].

## Resources mentioned

- **Research connectors:** [[Consensus]], PubMed, bioRxiv, clinical trials ([02:02](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=122s)–[03:08](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=188s)).
- **Productivity connectors:** Canva, Gmail, Outlook, Google Calendar, Todoist, Zoom, Miro ([03:11](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=191s)–[04:13](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=253s)).
- **Google Scholar** as his ongoing lit-review tool ([05:12](https://www.youtube.com/watch?v=GWtx-d3dALQ&t=312s)).
- **Free topic-validator skill** in the description; his consulting/course links (not reproduced here).

## Beyond the source

*Not from the video. Checked 2026-09-21.*

- **Consensus is a real research connector.** Consensus is an AI academic-search engine over ~200M+ papers (Semantic Scholar corpus) and offers a Claude/MCP connector. Its free tier historically caps advanced/AI features per month; exact numbers change. — [consensus.app](https://consensus.app/), [Anthropic connectors directory](https://www.anthropic.com/connectors)
- **PubMed, bioRxiv and ClinicalTrials.gov** are public databases; connectors to them are typically community or third-party MCP servers rather than first-party Anthropic connectors. Treat any connector's source as something to vet before installing. See [[Connecting Claude to External Tools]] (least-privilege, trust) and [[Build vs Install Third-Party Skills]].
- **Hallucinated citations are a documented risk.** Multiple 2023–2025 studies found general LLMs fabricate plausible-looking references; grounding answers in a retrieval connector with clickable sources is the standard mitigation, which is exactly his workflow.

## Transcript notes

- Captions were clean. Minor spoken repetitions ("the risen over the past 20 years") were smoothed in the prose. "To Doist" → Todoist. No product-name garbling of note.

## Related

- **People:** [[David Stuckler]]
- **Concepts:** [[Grounding Research in Real Sources]] · [[Connecting Claude to External Tools]] · [[Agent Skills]] · [[Verification Before Done]]
- **Techniques:** [[Set Up Claude Research Connectors]] · [[Build a Skill from a Successful Run]] · [[Workflow Audit into Skills]]
- **Tools:** [[Consensus]]
- **Compare:** [[Nate Herk - Stanford STORM Method as a Claude Research Skill]] (the other research-workflow source, focused on multi-perspective depth rather than source grounding)
- [[Home]]
