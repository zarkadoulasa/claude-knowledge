---
type: source
title: "Claude Code + Nano Banana 2 + Kling = $15K Animated Sites"
creator: "[[Nick Saraev]]"
channel: Nick Saraev
url: https://www.youtube.com/watch?v=ZfYvv-0l9NA
video_id: ZfYvv-0l9NA
published: 2026-03-16
duration: 13:58
ingested: 2026-09-24
topics: [animated marketing sites, image-to-video, design skills, performance optimization, deployment]
tags: [source/youtube, topic/design, topic/media, topic/claude-code, topic/marketing]
---

# Claude Code + Nano Banana 2 + Kling = $15K Animated Sites

> **Creator:** [[Nick Saraev]] · **Published:** 2026-03-16 · **Length:** 13:58 · [Watch on YouTube](https://www.youtube.com/watch?v=ZfYvv-0l9NA)

## TL;DR

A three-step pipeline for high-end, animated marketing/landing-page sites that Nick Saraev says used to sell for thousands. (1) [[Claude Code]] — run inside the Antigravity IDE — one-shots a luxury site by fetching Leon Lin's open-source "taste" skill ([[Leon Lin]]). (2) Generate short animated assets with Kling 3.0 video, optionally seeded by Nano Banana Pro stills, accessed through [[Higgsfield]]. (3) Claude Code wires the assets into the page (hero background video with a masking gradient, plus a scroll-scrubbed exploded-view section using locomotive scroll), optimizes performance (video frames → preloaded JPEGs tied to scroll; hero compressed 5.3 MB → 252 KB) and deploys free to Netlify. He frames the whole build as roughly $2–$5 and about ten minutes ([00:38](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=38s)) — a claim the Caveats section pushes back on.

## Key takeaways

- Claude Code is the orchestrator across the whole build: it fetches the skill, one-shots the site, integrates the media by filename, writes the scroll logic, optimizes assets, and deploys ([02:13](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=133s)).
- Claude never generates the images or video. It writes code and asset prompts; the actual media comes from external models (Kling 3.0, Nano Banana Pro) reached via [[Higgsfield]] — the pattern in [[Generating Images and Video with Claude]].
- A community-authored design "taste" skill turns a one-line prompt into a styled, high-end site ([01:15](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=75s)).
- You seed controlled motion by making a still first, then feeding it to the video model with a motion-constraint prompt ([04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s)).
- Vague natural-language optimization ("make it load significantly faster") gets Claude Code to convert a heavy scroll video into preloaded per-frame JPEGs ([09:43](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=583s)).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=0s) Animated Website Creations

Opens by showing four sites he says he built in about 15 minutes, all with 3D scroll effects: a headphones site, a "restore our forest" site with a rotating 3D globe, an interior-design site with a house blow-up, and a rotating space-station look ([00:00](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=0s)). All the visuals were AI-generated ([00:20](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=20s)). He claims sites like these would have cost $5K–$10K "a few years back," citing his own past as a website seller ([00:33](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=33s)), and that they now take under ten minutes for roughly $2–$3 in tokens with no need to hop across dozens of platforms — "really just three steps" ([00:38](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=38s)).

### [00:51](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=51s) Workflow overview

The flow in a nutshell: write a few bullet points into Claude Code, apply a skill made by a "cracked 16-year-old" shared on Twitter, generate an animated asset with Kling 3.0, then integrate onto the site and push live ([00:51](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=51s)). The "taste" skill is an open GitHub repo that instills high-end web-design principles and schematics — how you get one-shot quality from a simple prompt ([01:15](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=75s)). He shows a private-jet interior-design site he one-shotted without editing anything; the skill standardizes spacing and the luxury look ([01:29](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=89s)). For video he uses Kling 3.0 via [[Higgsfield]], making a batch of animations (rotating globes, spaceships) in about three minutes and then combining them with Claude Code ([01:48](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=108s)).

### [02:13](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=133s) Using Claude Code

Reiterates the build is roughly $5 in tokens and not complicated ([02:13](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=133s)). Prerequisite: Claude Code running inside an IDE — he uses Antigravity and links a separate setup guide ([02:18](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=138s)). Step one is telling the model about Leon's skill: copy the repo link, paste it into Antigravity, and prompt it to use the skill to design a high-end interior-design website ([02:41](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=161s)). Claude Code fetches the skill repository to understand what it provides, and he gives it about two minutes to do the full design ([03:01](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=181s)).

### [03:14](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=194s) Setting Up the Design

Moves to Kling and prompts for a 3D-render-style video panning through an interior scene, white background, high quality, reading like a landing page ([03:14](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=194s)). Settings: Kling 3.0, 5 seconds, 16:9, 1080p ([03:29](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=209s)). Cost math: the clip cost 7.5 credits; on Higgsfield's ~$29–$30 Pro plan (600 credits), 7.5/600 × $29 ≈ 36 cents per generation ([03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s)). He recommends generating two or three times to pick the best output ([04:05](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=245s)), and rough-budgets ~$3–$4 for video plus ~$1 of Claude Code usage, hosting free ([04:17](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=257s)). For the rotating-globe site he generated a globe still on Nano Banana, fed it into Kling, and constrained the motion — rotate in place, center of mass shouldn't move — noting you can also one-shot without a seed image ([04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s)). He downloads the panning interior clip, renames it `interior_design` in Finder, and prompts Claude Code to set it as the hero-header background, center the header, and apply an inward masking gradient so the animation doesn't clash with the site background ([05:27](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=327s)). He has to tell Claude Code the file is in the Downloads folder before it can find it ([05:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=358s)). Result: a clean hero, subtly tied to mouse position ([06:09](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=369s)).

### [06:24](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=384s) Enhancing the Animation

He wants a scroll-triggered "blow-up" 3D interior animation as you scroll down ([06:24](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=384s)). First he fixes small, hard-to-read text by pasting a screenshot into Claude Code and asking for more prominent type — the screenshot-as-feedback loop ([06:35](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=395s)). In Kling he prompts for an exploding-view animation of a home: no text, white background, exploding in all directions but staying inside the frame ([06:54](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=414s)). Tip: with enough credits, generate two or three simultaneously to raise the odds of a good final result ([07:24](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=444s)). He downloads the clip, renames it `interior_design_exploding_view` ([07:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=464s)), and asks Claude Code to build a scroll animation beneath the hero that steps through two or three text sections and reveals the exploded view frame by frame ([07:53](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=473s)). Claude Code builds a locomotive-scroll sequence, copies the video, and adds scroll-reveal logic ([08:21](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=501s)).

### [08:35](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=515s) Optimizing the Experience

The scroll animation works but is choppy, and the background color mismatches the site ([08:35](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=515s)). He sends a two-part fix: strengthen the top/bottom masking gradient so the dividing colors disappear, and "make it load significantly faster" ([09:30](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=570s)). Claude Code's optimization extracts the video frames as optimized JPEGs, ties each image to scroll position, and adds preloading ([09:43](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=583s)). As a former web developer he says this "blows my mind" — three days of work in about 30 seconds ([09:57](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=597s)). He then asks for a text overlay for readability ([10:13](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=613s)). He notes the page runs two heavy assets — a top video plus the preloaded JPEG sequence below — so it's asset-heavy, but says you can just repeat "make it faster" and trade quality for speed ([10:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=658s)). Finally he compresses the hero asset from 5.3 MB down to 252 KB ([11:37](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=697s)).

### [12:00](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=720s) Making It Live

He tells the agent to make the site live on Netlify ([12:12](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=732s)). He explains Netlify: free on the free plan, deploy from AI, Git, or API, unlimited deploy previews, a ~300 build-credit monthly limit, and a global CDN ([12:17](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=737s)). The CDN caches files at edge nodes worldwide so the site loads fast regardless of visitor location ([12:33](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=753s)). One button click and the site is live at `atelieramerin.netlify.app`, which he leaves up as a demo ([12:53](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=773s)). Caveat he states himself: he did not mobile-optimize it, but claims telling the model to "mobile optimize the site" three or four times will handle it ([13:11](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=791s)).

### [13:20](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=800s) Simplifying Web Design

Argues that "website design framework" hype and 35,000-step tutorials overcomplicate what is really a simple workflow ([13:20](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=800s)). Standard outro: a subscribe ask (he says ~73% of viewers aren't subscribed) and a note that all prompts and resources are free in the description and his community ([13:38](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=818s)).

## Caveats & disagreements

- **"$15K" is title-only.** On camera he says $5K–$10K, and only as a recollection of past resale prices — no client, invoice, or sale is shown ([00:33](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=33s)). The title's $15K exceeds even the figure he states.
- **"$2–$5 / under 10 minutes / one-shot" is optimistic.** The framing excludes subscription costs, the recommended 2–3× regenerations, and the many correction rounds actually shown (text size, gradient strength, lag, overlay, background color, hero compression). He also admits the site is not mobile-optimized and is asset-heavy, running two heavy media systems ([10:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=658s)) — these are demos, not shipped client-grade sites.
- **Affiliate conflict.** The [[Higgsfield]]/Kling link in the description is an affiliate link, so the "pretty affordable" pricing framing is not disinterested.
- **"Nano Banana 2" is a title label.** The image model is Nano Banana Pro; the transcript itself just says "Nano Banana" ([04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s)). Do not read the title as a distinct newer model.
- **Third-party dependency risk.** The workflow hinges on a solo teenager's open GitHub skill ([[Leon Lin]]'s taste repo) plus fast-moving proprietary models and platforms (Kling 3.0, Nano Banana Pro, [[Higgsfield]], Antigravity) whose pricing, versions, and availability may change or break.
- **Older video.** Published 2026-03-16; the metadata tags reference Claude Opus 4.6, so treat model behavior as of that era, not the newest Claude models.
- Self-reported income and client claims in the description are an unverified creator bio, not substantiated in the video.

## Build from this

- [[Build an Animated Marketing Site with Claude Code and Kling]] — the buildable playbook distilled from this pipeline.

## Resources mentioned

- **[[Claude Code]]** — the orchestration agent, run inside the Antigravity IDE.
- **taste skill ([[Leon Lin]])** — open GitHub repo of high-end web-design principles, loaded as a Claude Code skill ([01:15](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=75s)).
- **[[Higgsfield]]** — platform used to access Kling 3.0; ~$29–$30 Pro plan / 600 credits is the pricing basis ([03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s)).
- **Kling 3.0** — video-generation model for the animated assets (plain text; not a Claude model).
- **Nano Banana Pro** — image-generation model used to seed stills (plain text; not a Claude model).
- **Antigravity** — the IDE Nick runs Claude Code inside ([02:18](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=138s)).
- **Netlify** — free static hosting with a global CDN; the deploy target ([12:17](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=737s)).
- **locomotive scroll** — the scroll-animation approach Claude Code implements ([08:21](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=501s)).
- Finder / Downloads folder — used to rename and locate the mp4 assets before handing filenames to Claude Code.

## Beyond the source

Leon Lin's taste skill is credited in the video's description as living at github.com/Leonxlnx/taste-skill (verify at [github.com](https://github.com/Leonxlnx/taste-skill)). This URL is from the description, not stated in the spoken video.

## Transcript notes

- "Cloud Code" (recurring, e.g. [00:55], [01:31], [02:11]) → Claude Code.
- "Hexfield" ([03:46]) → [[Higgsfield]].
- Title "Nano Banana 2" → the model is Nano Banana Pro; the spoken transcript says only "Nano Banana" ([04:46]).
- Title "$15K" vs spoken "$5,000 to $10,000" ([00:33]) — a headline-vs-content discrepancy, not a caption error.

## Related

- [[Generating Images and Video with Claude]]
- [[Higgsfield]]
- [[Claude Code]]
- [[Build an Animated Marketing Site with Claude Code and Kling]]
- [[Build a Scroll-Driven Landing Page]]
- [[Build a Distinctive Site with Design Skills]]
- [[Escaping the Default AI Design Look]]
- [[Leon Lin]]
