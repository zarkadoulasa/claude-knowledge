---
type: source
title: Claude Opus 5.5 Might Be The Best!!! (3D, Web Design, Animation)
creator: "[[Codex Community]]"
channel: Codex Community
url: https://www.youtube.com/watch?v=Da7ZuhyWACg
video_id: Da7ZuhyWACg
published: 2026-09-23
duration: 9:01
ingested: 2026-09-24
topics: [opus-5-5, web-design, 3d, model-review, delegate-and-wait]
tags: [source/youtube, topic/models, topic/design, topic/claude-code]
---

# Claude Opus 5.5 Might Be The Best!!! (3D, Web Design, Animation)

> **Creator:** [[Codex Community]] · **Published:** 2026-09-23 · **Length:** 9:01 · [Watch on YouTube](https://www.youtube.com/watch?v=Da7ZuhyWACg)

> **Note on the channel name:** Despite being called "Codex Community" (a name that evokes OpenAI Codex), this video is entirely about **Claude Opus 5.5** — a single-reviewer hands-on test of the Claude model on web design, 3D, and animation. OpenAI Codex is only mentioned in passing as one CLI a connector SDK supports.

## TL;DR

A single reviewer runs Claude Opus 5.5 through his personal set of design prompts in the Claude app and judges the visual output the best he has seen — near professional-designer level for web UI, micro-animation, and 3D. The catch is speed: complex prompts take roughly an hour each (one 3D build ran 51 minutes), which he reframes as a "takes time to think" delegate-and-wait tradeoff. He opens with third-party community demos of Opus 5.5 driving Blender, Unreal Engine, and Unity, then shows four of his own prompts: an award-winning site about Opus 5.5, a redesign of the live site typeui.sh, a 3D space-agency site, and a personal daily dashboard wired through the Zapier SDK (the sponsor). Pricing and efficiency figures quoted in the video were read off the marketing page Opus 5.5 generated about itself, not verified Anthropic specs.

## Key takeaways

- **Best design/3D output he's seen, but slow.** Opus 5.5's web and 3D output looks near professional, at the cost of ~1 hour per complex prompt — a delegate-and-wait workflow, not instant turnaround [08:20](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=500s).
- **Always-on thinking.** Reasoning can't be toggled off; his read of the model-generated page is that old Opus on "high" ≈ new Opus on "medium" [02:03](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=123s).
- **Reusable benchmark prompts.** He keeps a fixed set of personal prompts (award site, live-site redesign, 3D space agency) and re-runs them on each new model to compare qualitatively [01:18](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=78s).
- **Efficiency figures are model-produced.** The prices and savings he cites came from the site Opus 5.5 wrote about itself — treat as claims, not specs (see Caveats) [01:52](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=112s).
- **Connector SDK + Opus 5.5 for personal dashboards.** He builds a daily aggregation dashboard over the Zapier SDK, wiring Notion, Gmail, YouTube, Webflow, Wix, and Discord [06:49](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=409s).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=0s) Intro

He introduces Opus 5.5 as, in his view, the most powerful model available right now, and claims it beats competitors on many benchmarks and is 30% faster and 40% cheaper than previous Opus models — no benchmark names or sources are shown [00:06](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=6s). The stated goal is to test it on coding and web design [00:15](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=15s). The competitor names he says (heard as "Fable 5.1" and "ChatGPT Astra 6") are garbled or ambiguous — "Fable" is itself a Claude model codename, so treat these references as unclear.

### [00:19](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=19s) 3D and game community demos

Third-party demos he did not reproduce, all cited from social posts (unverified):

- A user he names "Stefan" showing Opus 5.5 jump into Blender and build a 3D mockup scene with animation from scratch [00:20](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=20s).
- Higgsfield showing Opus 5.5 in Unreal Engine building an underwater game level [00:29](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=29s).
- The model building an octopus from scratch in Blender, then rigging it with bones, animating, and texturing — framed as a leap in 3D asset generation [00:40](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=40s).
- A single-prompt claymorphism animation in Blender credited to "Alex" [00:57](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=57s).

He says the Blender/Unreal work is impressive but not his focus — he cares about real web design: UI/UX, micro-animation, interaction — and that he has a set of prompts he tests every new model against [01:06](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=66s). (Unity appears in the video description as another engine Opus 5.5 reportedly handles; it is not shown in the transcript.)

### [01:23](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=83s) Example 1 — award-winning site about Opus 5.5

**Own prompt #1:** in the Claude app with Opus 5.5 selected, create an interactive, award-winning website about Opus 5.5 itself, with micro-animations, using GSAP or Three.js, as an experience that teaches about the model [01:27](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=87s). The run took about an hour — far longer than earlier models on similar builds [01:40](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=100s). The result, headlined "Opus that never stops thinking," surfaces the model's own claimed facts (all read off the generated page — see Caveats): $4 per million input tokens and $20 per million output tokens, 20% cheaper than prior Opus [01:52](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=112s); thinking that can't be toggled off, with old-Opus-"high" ≈ new-Opus-"medium" [02:03](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=123s); ~20% lower pricing, cache reads down ~60%, and possibly about half the tokens for agentic coding [02:23](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=143s); and less verbose output, fixing prior Opus over-commenting he found annoying [02:35](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=155s). His verdict on the page: no complaints on typography, color, or visual hierarchy [02:47](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=167s).

### [02:59](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=179s) Example 2 — typeui.sh redesign

**Own prompt #2:** redesign the existing live site typeui.sh with better micro-animation, stronger visual hierarchy, more Framer Motion, and a more visually stimulating result [02:59](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=179s). The model worked section by section, and this run also took about an hour [03:16](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=196s). After showing the original, he highlights the redesign: a "Build better UI with AI" hero, and a "Same prompt, different taste" section that swaps one layout across multiple color schemes with a couple of clicks [03:50](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=230s). It also generated self-produced noise effects he can't account for, plus sections for design skills, clickable UI prompts, animation toggles, brand kits, UI audits, and analytics [04:07](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=247s). Verdict: micro-animations and hover effects on every part, with visual hierarchy at a level he'd expect from a professional graphic designer [04:53](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=293s).

### [04:57](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=297s) Example 3 — 3D space-agency site

**Own prompt #3:** build a 3D website for a space agency — a prompt he has reused across many models [04:57](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=297s). This run took 51 minutes [05:16](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=316s). The output opens on a hero ("Built on Earth, bound for anywhere else") with Earth and the sun; scrolling expands the Earth with scroll-jacking, builds a rocket as a 3D element (he thinks Three.js), reaches a launchpad, blasts off, and flies through the planets [05:34](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=334s). Referencing his earlier video on a competitor model, he judges Opus 5.5 roughly 10x better on this single prompt [06:07](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=367s).

### [06:18](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=378s) Example 4 — Zapier SDK dashboard (sponsor)

**Own prompt #4:** test Opus 5.5 with CLIs, SDKs, and MCP tool calls by building a personal daily dashboard that aggregates his usual checks — emails, YouTube analytics, Webflow/Wix contact-form submissions — instead of visiting each site manually [06:26](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=386s). He uses the Zapier SDK (the sponsor), describing its CLI as working with Codex, Claude Code, and the app itself, connecting Notion, Gmail, YouTube, Webflow, Wix, and Discord [06:49](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=409s). The prompt ran well past the "9 minutes" shown because he chatted with it to steer the result [07:18](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=438s). The dashboard shows 26 emails, ~100k YouTube views, a (falling) subscriber count, a calendar, video activity, and his connected sites — in both dark and light versions [07:29](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=449s). He muses it could be extended to surface Slack and to talk to his other agents (names garbled) in one place [07:56](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=476s).

### [08:10](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=490s) Final thoughts

After a full day with it, his verdict: the model excites him. It is slow — better framed as taking time to think — with most tasks around an hour, so five prompts cost roughly five hours [08:20](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=500s). But the outputs were "stunning" each time, so he appreciates the extra time [08:35](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=515s). You have to be patient with it — like handing a task to a person and waiting for them to return with an answer [08:43](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=523s). If this quality is the new baseline for AI models, he doesn't mind the extra wait — the transcript cuts off mid-sentence here (~08:59) [08:54](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=534s).

## Caveats & disagreements

- **Pricing/efficiency figures are unverified.** Most of the numbers — $4/M input, $20/M output, ~20% cheaper, ~60% cheaper cache reads, ~half the tokens for agentic coding — were read off the marketing site **Opus 5.5 generated about itself** [01:52](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=112s) [02:23](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=143s), so they are model output, not confirmed Anthropic figures. The intro's "30% faster / 40% cheaper" is separate — his own unsourced assertion before any page is shown [00:06](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=6s). See "Beyond the source" for the verified launch facts.
- **Single-reviewer, subjective.** "Most powerful," "best I've ever seen," "10x better," "professional graphic designer" are one person's impressions on a handful of visual prompts [04:53](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=293s) [06:07](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=367s) — not benchmarked or blind-tested. The "beats [competitors] on a lot of benchmarks" claim shows no numbers or sources.
- **Community 3D demos are unverified third-party posts.** The Blender/Unreal/Unity/octopus/claymorphism demos are attributed to others via social media and were not reproduced on camera [00:19](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=19s).
- **Runtime numbers are anecdotal.** "Ran for an hour" and "51 minutes" come from single runs; Example 4 was also stretched by manual back-and-forth, so its "9 minutes" shown vs. actual time isn't a clean measurement [07:18](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=438s).
- **Competitor model names are garbled/unclear.** Heard as "Fable 5.1," "ChatGPT Astra 6," "Astra," "Kimmy" — flag as *(unclear in captions)*; "Fable" is also a Claude codename, adding ambiguity.
- **Zapier is the sponsor** (per the video's description; not stated aloud in the captured audio). The Example 4 segment [06:18](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=378s) reads as paid promotion, so its framing ("connects to everything," ease of use) should be treated as sponsor content.
- **Transcript truncation.** The closing sentence is cut off around 08:59, so the final thought is incomplete.

## Build from this

- [[Build a Scroll-Driven Landing Page]] — his 3D space-agency prompt (Three.js + scroll-jacking, Earth → rocket → launch → planet flythrough) is a concrete scroll-driven build to reuse.
- [[Build a Distinctive Site with Design Skills]] — his "redesign a live site" pattern (point the model at a real URL and ask for a restyled version with stronger hierarchy and Framer Motion) is a design-eval build.

## Resources mentioned

- **Claude Opus 5.5** (`claude-opus-5-5`) — the subject of the video.
- **Claude app** — the interface where he ran all four prompts.
- **Claude Code** and **Codex** — named as CLIs the Zapier SDK works with.
- **Three.js**, **GSAP**, **Framer Motion** — the web animation/3D libraries used across the design prompts.
- **Blender**, **Unreal Engine**, **Unity** — 3D/game tools in the community demos.
- **typeui.sh** — the live site used as the redesign target (also plugged in the description as "TypeUI, design skills for your agents").
- **Zapier SDK / CLI** — the video's sponsor; used to build the daily dashboard (connecting Notion, Gmail, YouTube, Webflow, Wix, Discord).
- **EnhanceUI** — the creator's own web-design course, plugged in the description (not in the transcript body).

## Beyond the source

The video's pricing and efficiency numbers were produced by the model itself, so they are not a reliable specification. The verified Claude Opus 5.5 launch facts are on Anthropic's announcement, [Introducing Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5) — the vault's [[Choosing a Claude Model]] already records them under its own "Beyond the source" (default effort medium, lower prices than Opus 5, and a 30%+ speed improvement on Terminal-Bench). Cross-reference that note rather than treating the on-screen figures as authoritative.

## Transcript notes

Non-obvious caption fixes applied silently in the prose above:

- "Clawed app" → **Claude app**
- "cloud code" → **Claude Code**
- "3JS" → **Three.js**
- "frame motion" → **Framer Motion**
- "topography" → **typography** (used repeatedly to mean fonts/type)
- "case reads" → **cache reads**
- "Zap year SDK" → **Zapier SDK**
- "Higsfield" → **Higgsfield**
- "codeex" → **Codex**
- Competitor model names ("Fable 5.1," "ChatGPT Astra 6," "Astra," "Kimmy") and the agent names near the end ("Hermes," "OpenClaw") are garbled and left as *(unclear in captions)*.

## Related

- [[Choosing a Claude Model]]
- [[Escaping the Default AI Design Look]]
- [[Generating Images and Video with Claude]]
- [[Claude Code]]
