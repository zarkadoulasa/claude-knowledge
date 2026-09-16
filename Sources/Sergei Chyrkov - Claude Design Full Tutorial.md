---
type: source
title: "NO MORE AI SLOP | Claude Design Full Tutorial"
creator: "[[Sergei Chyrkov]]"
channel: "Sergei Chyrkov"
url: https://www.youtube.com/watch?v=T96O8dTzi2Q
video_id: T96O8dTzi2Q
published: 2026-07-30
duration: "14:47"
ingested: 2026-09-15
topics: [claude design, design systems, generic ai design look, design-to-code handoff, model choice, brand assets, spec-first prompting]
tags: [source/youtube, topic/design, topic/claude-code, topic/models, topic/marketing, topic/planning]
---

# Sergei Chyrkov - Claude Design Full Tutorial

> **Creator:** [[Sergei Chyrkov]] · **Published:** 2026-07-30 · **Length:** 14:47 · [Watch on YouTube](https://www.youtube.com/watch?v=T96O8dTzi2Q)

## TL;DR

Designer [[Sergei Chyrkov]] takes one project, a pizza-ordering landing page called Pizzalio, from spec to code. His thesis: design process, more than a better prompt, closed the gap between [[Claude Design]]'s first draft and the final site [00:06](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=6s).

Chat Claude writes a markdown spec; Claude Design builds a baseline with no template or design system on Opus 5; one Pinterest screenshot becomes a Claude Design design system, applied with a short layout prompt; he adds ChatGPT images, hands off to [[Claude Code]] on Sonnet 5, and reuses the system for a menu and Instagram posts.

It is the vault's first route off the default look that leans on Claude Design's own design system rather than skills or screenshots, and its first walkthrough of the Claude Design to Claude Code handoff. Everything is judged by eye, with no review step, and the build itself isn't shown.

## Key takeaways

- **See the default first.** A baseline with no template or design system shows what generic looks like for your brief [02:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=127s). See [[Escaping the Default AI Design Look]].
- **The design system is the lever**, more than site generation, which other tools also do well [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s). See [[Design Systems for Claude]].
- **One reference image seeds the system**; he chose his mainly for its typography [04:22](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=262s).
- **SVG-style illustrations read as generic** [02:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=160s); photos help.
- **Design on the expensive surface, build on the cheap one.** Claude Design burns tokens, so stop there once the layout is right [09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s) and build on a cheaper model [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s). See [[Choosing a Claude Model]].
- **Build the system once, reuse it everywhere**: consistency across site, menu and posts is the payoff [13:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=782s).

## The workflow at a glance

"Screen only" = visible in the video, absent from the captions.

| # | Step | Where | What he does | Captions? | When |
|---|---|---|---|---|---|
| 1 | Spec | Claude chat | Brief description → detailed MD file, downloaded | Request and spec screen only | [01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s) |
| 2 | Baseline | Claude Design, Opus 5 | "implement" + the MD; no template or system | Yes | [01:39](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=99s) |
| 3 | Inspiration | Pinterest or Mobbin | Downloads one site screenshot | Yes | [03:56](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=236s) |
| 4 | Design system | Claude Design | Dropdown → create → visual assets → "Pizzalio" | Contents partly narrated | [05:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=305s) |
| 5 | Apply | Claude Design project | + → design system → Done; layout prompt | Prompt read aloud | [07:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=431s) |
| 6 | Tune, add images | Claude Design | Tweaks; ChatGPT photos replace illustrations | Image prompts not shown | [08:23](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=503s) |
| 7 | Handoff | Claude Code, Sonnet 5 | Share → Claude Code; paste prompt in a new folder | Handoff prompt screen only | [10:16](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=616s) |
| 8 | Menu | Document template | Answers intake questions | Answers yes; prompt screen only | [11:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=679s) |
| 9 | Instagram | Claude Design | Photo + request for post layouts | Partly | [12:23](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=743s) |
| 10 | Final site | Browser | Preview after extra hero fixes | Build not shown | [13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s) |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=0s) Introduction

- Plan: a reusable design system, every section refined with it, a Claude Code build, then brand assets from the same system [00:18](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=18s).

### [00:51](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=51s) Creating the prompt

- In ordinary chat he described the project in a few words and had Claude write a detailed prompt as an MD file [01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s) covering how it should look and work [01:18](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=78s). See [[Plan Before Executing]].

### [01:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=100s) Claude Design — implementing from the markdown

- Claude Design sits at the bottom of the desktop app's sidebar and opens its own window [01:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=92s); he types "implement", attaches the MD and picks Opus [01:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=106s).
- He notes templates (documents, animations, UI mockups, research, resume) that tested well for him [01:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=112s), but skips them and design systems to see what a prompt plus a file gives [02:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=127s).

### [02:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=150s) Testing the generic version

- Fine for most people, generic to a designer [02:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=160s).
- Builder test: size choice and the price calculator work [02:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=172s); crust choice does nothing [02:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=178s); cheese drag-and-drop fails [03:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=187s); a review-your-pizza step exists [03:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=220s).

### [03:53](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=233s) Finding design inspiration

- Pinterest search [04:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=242s); Mobbin and similar tools also work [04:08](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=248s). Find one website image; he stresses inspiration, not copying [04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s).

### [04:33](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=273s) Creating a design system

- Sites can be built well elsewhere (Cursor worked about 80% of the time for him) [04:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=292s); the design-system tool is what stands out [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s).
- Path: design system dropdown, then the create icon [05:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=305s). Inputs: a GitHub project, good for an existing project [05:20](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=320s); a local codebase, a Figma file, or visual assets [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s). He drags in the image [05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s) and names it Pizzalio [05:48](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=348s).

### [06:00](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=360s) Exploring the design system

- Contents: navigation, fonts, numbers, structure [06:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=373s); references and ideas [06:25](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=385s); colours, blobs and shapes, a wordmark [06:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=392s); animation, elevations, radii [06:39](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=399s); a landing-page style [06:51](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=411s). He estimates days of Figma work [06:45](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=405s).

### [07:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=427s) Applying the design system to the site

- Attach: + icon, design system, Pizzalio, Done [07:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=431s).
- Prompt, paraphrased: restyle the layout with the design system, make the hero full viewport rather than half the page, add scroll parallax with pizzas and ingredients [07:34](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=454s). He hits his usage limit mid-run [07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s).

### [08:10](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=490s) Reviewing the redesign

- Full-screen hero and custom cursor [08:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=495s); parallax speed and colours adjustable in Tweaks without prompting [08:23](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=503s); a horizontal-scroll section [08:35](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=515s); restyled builder still works [08:51](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=531s); text animations and a full-screen footer [08:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=538s).

### [09:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=545s) Adding AI-generated images

- Three people photos and a pizza photo from ChatGPT (model not named) [09:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=544s); Claude Design places the people and swaps the pizza illustration for the photo [09:14](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=554s). The footer ends up too big [09:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=586s).

### [10:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=615s) Sending to Claude Code

- Share, more formats and apps, Claude Code [10:16](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=616s). Targets: local agent or a web session in the cloud or GitHub [10:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=630s); save locally; or a zip for another tool such as Cursor [10:38](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=638s).
- He pastes the copied prompt into a new local folder [10:53](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=653s) and picks Sonnet 5, since the designs already exist [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s).

### [11:20](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=680s) Reusing the design system: menu

- System attached [11:25](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=685s), document template [11:33](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=693s); prompt wording is screen only.
- Intake questions [11:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=700s). His answers: single page; pizzas, drinks, salads; 20 items [11:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=706s); no photos, styles only; draft [11:56](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=716s). The result is simple but matches the site [12:03](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=723s).

### [12:25](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=745s) Reusing the design system: social posts

- A photo plus a request for several Instagram layouts, same system [12:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=750s). Simple by his standard, but a big help for non-designers [12:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=778s).

### [13:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=795s) Final build in Claude Code

- He polished the hero with extra Claude Code edits first [13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s). Browser check: animations and parallax [13:48](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=828s); he'd still swap SVG illustrations for photos [14:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=842s); ordering works [14:12](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=852s).

## Caveats & disagreements

**About the video**

- **No verification**: no critique, responsive or accessibility pass; verdicts are by eye, such as calling Claude Design's systems the best [06:08](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=368s). See [[Benchmark-Driven Design Critique]] and [[Verification Before Done]].
- **Loose ends**: the crust [02:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=178s) and drag-and-drop [03:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=187s) bugs are never revisited; the big footer stays [14:18](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=858s).
- **Not a pure handoff**: extra hero edits [13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s), and the build isn't shown.
- **Unmeasured claims**: days in Figma [06:45](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=405s), hours saved [12:17](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=737s), Cursor at 80% [04:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=292s).
- **Usage limits bite**: near the limit [07:03](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=423s) and over it [07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s) in one session.
- **Inspiration vs copying**: one screenshot of someone else's site [04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s) is the system's only input. Use the referencing line in [[Escaping the Default AI Design Look]]: take traits, not identity, assets or copy.
- **Generated people** [09:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=544s): *vault reading*, realistic AI people on a commercial site may warrant disclosure.
- **UI labels drift**; Anthropic's docs describe setup and controls differently (Beyond the source).
- **Omitted**: a plug for his 1:1 sessions and newsletter, a subscribe request, and the description's referral and affiliate links.

**Conflicts with existing vault notes (both sides kept)**

- **[[Escaping the Default AI Design Look]].** *Vault:* designer-written skills ([[AI LABS - Claude Design Skills for Beautiful Sites]], [00:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=28s)) or screenshots plus a self-check loop ([[Nate Herk - 32 Tricks to Level Up Claude Code]], [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)); tastemaker argues image summaries lose detail. *Video:* no skills or loop; Claude Design interprets one image into a system [05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s), fidelity untested.
- **[[Claude Design]].** *Vault (Anthropic help):* systems are set up in organisation settings with a Published toggle, and Figma isn't a listed input. *Video:* created from a project dropdown with Figma among the inputs [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s). Also, AI LABS call layout Claude Design's weak spot ([09:50](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=590s)); Chyrkov only faults the footer [09:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=586s).
- **[[Build a Distinctive Site with Design Skills]].** *Vault:* review rounds, two-width screenshots, a pass bar, `/design-sync`. *Video:* stops when it looks good, to save tokens [10:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=604s), and hands off via the Share menu.
- **[[Choosing a Claude Model]].** A refinement: [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] splits by phase, Opus plans and Sonnet builds ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)); here it's by surface, Opus 5 designing and Sonnet 5 building [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s).
- **[[Build a Reference-Rich Skill]].** *Vault:* brand consistency via a SKILL.md with a brand HTML reference ([[Jay E - The ARMS Framework for a Claude Agentic OS]], [07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s)). *Video:* the same from Claude Design's built-in system, no skill files [13:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=782s). Vault reading: that system doesn't travel to other agents as a skill folder does.
- **[[Plan Before Executing]].** *Vault:* interview, spec, fresh session. *Video:* a spec with no interview [01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s); intake questions appear only for the menu [11:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=700s).

## Build from this

- **Full pipeline**: [[Create and Reuse a Claude Design System]]; background in [[Design Systems for Claude]].
- **Add the missing review** before handoff and after the build: [[Benchmark-Driven Design Critique]] or [[Build a Distinctive Site with Design Skills]].
- **Spec and model split**: [[Plan-First Workflow]], [[Route Tasks to the Right Claude Model]].
- **Clean handoff** (vault): zip export if the local-agent prompt fails; a fresh folder for clean context ([[Context Window Management]]); a permission mode chosen before it writes files ([[Permissions and Approval Gates]]).
- **More collateral**: [[Build a Brand-Aware Marketing Project]].

Vault starter content for step 1 (not his wording, which is screen only):

```text
I want to build: <product, audience, the one action visitors should take>.
Write a detailed build spec as a downloadable Markdown file for a design tool.
Cover: sections in order, each interactive feature and its states, placeholder copy,
required behaviour (e.g. live prices), and how to tell each feature works.
Leave visual style open; a design system comes later.
Ask up to five questions first if anything important is unclear.
```

## Resources mentioned

- **Demo site and repo** (from the description): https://pizza-project-claude-design.vercel.app · https://github.com/chyrkov/pizza-project
- **Pinterest** [04:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=242s) and **Mobbin** [04:08](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=248s) for inspiration (Mobbin affiliate link not reproduced); **ChatGPT** for images [09:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=544s); **Cursor** [04:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=292s)

## Beyond the source

*Not said in the video. Checked on 2026-09-15 at the links given.*

- **Design system setup.** Anthropic places it in onboarding or later in organisation settings, for users an admin permits. Inputs: codebases, screenshots or design files, decks, logos and type specimens. Output: colours, typography, components, layout patterns. A Published toggle makes it the org default; Remix updates it. https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- **Usage and export.** Claude Design shares the usage limits of the rest of Claude. Handoff: local coding agent, Claude Code on the web, or zip; exports also include PDF, PPTX, HTML and Canva. https://support.claude.com/en/articles/14604416-get-started-with-claude-design
- **Tweaks.** The launch post (2026-04-17) doesn't use that name; it describes adjustment knobs for live spacing, colour and layout changes, plus a handoff bundle for Claude Code. https://www.anthropic.com/news/claude-design-anthropic-labs
- **Local handoff bug.** Issue #69246 (opened 2026-06-18, closed): the local-agent prompt relied on a Claude Design connector local Claude Code lacked. Workaround: unzip the download into the project and point Claude Code at it. https://github.com/anthropics/claude-code/issues/69246
- **Price gap.** API prices per million tokens: Opus 5 $5 in / $25 out; Sonnet 5 $2 / $10. https://platform.claude.com/docs/en/about-claude/models/overview
- **Demo repo.** Vanilla HTML, CSS and JS, styles split into tokens, components and layout, with a `.claude` folder. The description's live link loads; the README's Vercel link asks for a login. https://github.com/chyrkov/pizza-project

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "claw/cloth/clo/cloud design" | Claude Design |
| "cloud code", "clo code" | Claude Code |
| "go to our cloud and we go to cloud code" (10:44) | open Claude Code in the desktop app (likely) |
| "it's alio" (05:48), "pitalio" (07:18) | Pizzalio (per the repo) |
| "set 5" (10:59) | Sonnet 5 (likely) |
| "share more formats and apps" (10:16) | Share menu export/handoff options *(exact label unverified)* |
| "web session ... on our cloud or in our GitHub" (10:30) | Claude Code on the web (likely) |

## Related

- **Concepts:** [[Design Systems for Claude]] · [[Escaping the Default AI Design Look]] · [[Choosing a Claude Model]] · [[Plan Before Executing]] · [[Context Window Management]] · [[Permissions and Approval Gates]] · [[Verification Before Done]]
- **Techniques:** [[Create and Reuse a Claude Design System]] · [[Benchmark-Driven Design Critique]] · [[Build a Distinctive Site with Design Skills]] · [[Route Tasks to the Right Claude Model]] · [[Plan-First Workflow]] · [[Build a Reference-Rich Skill]] · [[Build a Brand-Aware Marketing Project]]
- **Tools:** [[Claude Design]] · [[Claude Code]]
- **Sources:** [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] · [[Nate Herk - The Scrollcraft Website Design Skill]] · [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]
- **People:** [[Sergei Chyrkov]] · [[Jack Roberts]]
- [[Home]]
