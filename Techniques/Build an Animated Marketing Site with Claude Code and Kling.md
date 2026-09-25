---
type: technique
goal: "Build a high-end animated marketing/landing site with Claude Code — a design-taste skill for the site, Kling/Nano Banana for assets, then Claude Code integrates, optimizes and deploys"
difficulty: intermediate
time_to_build: "an hour or two"
sources: ["[[Nick Saraev - Animated Sites with Claude Code and Kling]]"]
tools: ["[[Claude Code]]", "[[Higgsfield]]"]
tags: [topic/design, topic/media, topic/claude-code, topic/marketing]
---

# Build an Animated Marketing Site with Claude Code and Kling

## Goal

Ship a luxury-looking animated landing page — a hero background video, a scroll-scrubbed exploded-view section — in a short sitting, then optimize and deploy it.

- **The three-step pipeline.** [[Nick Saraev - Animated Sites with Claude Code and Kling]] frames it as: (1) one-shot the site in [[Claude Code]] with a design "taste" skill, (2) generate assets (a still seeds a video), (3) have Claude Code integrate, optimize and deploy them [00:51](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=51s). He argues most tutorials overcomplicate what is really three steps [13:20](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=800s).
- **The split that matters.** Claude Code writes the site code and wires the finished clips in, but the images/videos come from **external models via [[Higgsfield]]** — a Nano Banana Pro still fed into Kling 3.0 video — and in this video Nick writes those generation prompts himself [04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s). Claude has no image/video model of its own; see [[Generating Images and Video with Claude]]. (In [[Vibe-Code an Animated Mobile App with Claude]], by contrast, Claude writes the asset prompts too via the Higgsfield MCP.)

## Use when

- **You need a fast, high-end animated landing page** with 3D-feel scroll effects [00:00](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=0s).
- **You're running a productized web-design service** and want a repeatable pipeline (he pitches these as premium client deliverables) [00:33](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=33s).
- **Not for a static-content site** where heavy hero video and preloaded frame sequences add cost without payoff — this page runs two asset systems and is deliberately heavy [10:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=658s).

## Prerequisites

- **[[Claude Code]] running inside an IDE.** Nick runs it in the Antigravity IDE and links a separate setup guide [02:18](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=138s).
- **A design-taste skill.** He uses [[Leon Lin]]'s open-source "taste" skill — a public GitHub repo encoding high-end web-design principles and schematics [01:15](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=75s). *Vault:* read a third-party skill before running it; it can run scripts.
- **[[Higgsfield]] with credits** to reach Kling 3.0 (video) and Nano Banana Pro (images). His basis: the ~$29–30 Pro plan / 600 credits [03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s).
- **A Netlify account** (free tier) for hosting [12:17](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=737s).

## Steps

### Step 1 — One-shot the site with the taste skill

1. **Point Claude Code at Leon Lin's skill and prompt for your niche.** Copy the repo link into the IDE and prompt, roughly, "use this skill to design a high-end website about interior design" [02:41](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=161s). Claude Code fetches the repo to learn what it provides; give it ~2 minutes to build the full design [03:01](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=181s). The skill standardises spacing and the luxury look, which is what makes a one-shot prompt produce a high-quality site [01:15](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=75s).

### Step 2 — Generate the assets (still → video)

2. **Generate a hero clip in Kling.** Prompt for a 3D-render-style video panning through your scene, white background, high quality, reading "like something you'd see on a website or a landing page" [03:14](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=194s). Settings: **Kling 3.0, 5 seconds, 16:9** (wider suits a landing page), **1080p** [03:29](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=209s).
3. **Seed a controlled animation from a Nano Banana still.** For the rotating globe he generated a globe image on Nano Banana Pro, fed it into Kling, and constrained the motion: rotate in place, "center of mass should not move" [04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s). You can also one-shot a clip with no seed image.
4. **Generate 2–3× and pick the best** — with enough credits, run them simultaneously to raise the odds of a usable result [04:05](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=245s), [07:24](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=444s). Cost math: 7.5 credits ÷ 600 × $29 ≈ **36 cents per clip** [03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s).

### Step 3 — Integrate, optimize, deploy in Claude Code

5. **Wire the hero video in.** Download the clip, rename it in Finder (e.g. `interior_design.mp4`), and hand Claude Code the exact filename: make it the hero-header background, centre the header so it looks clean, and apply "some sort of inward masking gradient" so the video doesn't clash with the site background [05:27](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=327s). You have to tell it the file is in the Downloads folder so it can find it [05:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=358s).
6. **Add a scroll-scrubbed exploded-view section.** Generate an exploded/blow-up clip (prompt: explode in all directions, no text, white background, nothing leaving the frame) [06:54](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=414s). Rename it, then ask Claude Code to create a scroll animation immediately under the hero that steps through 2–3 text sections and shows the exploded view frame by frame as you scroll [07:53](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=473s). It builds a locomotive-scroll sequence and adds scroll-reveal logic [08:21](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=501s).
7. **Optimize performance.** The first result is choppy and the background colour mismatches [08:35](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=515s). A two-part fix — strengthen the top/bottom gradient, and "make it load significantly faster" — makes Claude Code extract the video frames as optimized JPEGs, tie each image to scroll position, and add preloading [09:43](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=583s). Repeat "make it faster" a few times and accept the quality/speed tradeoff [10:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=658s). Compress the hero asset too — his went from **5.3 MB to 252 KB** [11:37](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=697s).
8. **Fix legibility with screenshot feedback.** Paste a screenshot and describe the problem — small/hard-to-read text [06:35](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=395s), or text that collides with the animation and needs an overlay behind it [10:13](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=613s).
9. **Deploy to Netlify.** Prompt "make it live on Netlify," then click the deploy button; the site goes live on a `*.netlify.app` URL with a global CDN [12:12](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=732s). His demo is live at atelieramerin.netlify.app [12:53](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=773s).
10. **Mobile-optimize.** He didn't do it in the demo but says to prompt "mobile optimize the site" three or four times [13:11](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=791s).

## Starter files & prompts

*Vault starter content: original wording, distilled from the video's prompts, not quoted from it.*

**Prompt skeletons (paraphrased from the build)**

```text
1 One-shot site: paste the taste-skill repo link, then
  "Use this skill to design a high-end website about <niche>."

2 Hero clip (in Kling): "High-quality 3D-render-style video panning through a
  <scene>. White background, super high-quality, reads like a landing page."
  Settings: Kling 3.0 · 5s · 16:9 · 1080p. Generate 2-3x, pick the best.

3 Seeded motion: make a still in Nano Banana Pro, feed it to Kling, constrain:
  "<subject> rotating in the exact same place; center of mass should not move."

4 Hero wire-in: "Take <file>.mp4 in downloads/ and make it the hero-header
  background. Center the header. Apply an inward masking gradient so the
  animation background doesn't interfere with the site background."

5 Scroll section: "Take <file>_exploding_view.mp4 in downloads/ and create a
  scroll animation under the hero. Step through 2-3 text sections and show the
  exploding view frame by frame as I scroll."

6 Optimize: "Two problems: the fuzzy gradient is too weak (dividing colors top
  vs bottom) — make it stronger top and bottom; and it's laggy — make it load
  significantly faster." Repeat "make it faster" 3-4x.

7 Deploy: "This looks awesome. Make it live on Netlify."
```

## Done when

- [ ] The taste skill produced a styled site from one prompt
- [ ] A hero clip (Kling 3.0, 5s, 16:9, 1080p) is generated, with 2–3 takes to choose from
- [ ] Any seeded animation uses a Nano Banana Pro still plus a motion-constraint prompt
- [ ] The hero video is set as the header background with an inward masking gradient
- [ ] A scroll-scrubbed exploded-view section runs under the hero (locomotive scroll)
- [ ] Frames are extracted to optimized JPEGs tied to scroll, with preloading, and the hero asset is compressed
- [ ] Text is legible over the animation (overlay / larger type)
- [ ] The site is deployed to Netlify, and mobile-optimized if it's going to real users

## Pitfalls

- **The cost/time figures are optimistic.** "$2–$5 total, under 10 minutes, one-shot" [00:38](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=38s) excludes the Higgsfield and Claude Code/Antigravity subscriptions, the recommended 2–3× regenerations, and the many correction rounds actually shown (text size, gradient, lag, overlay, colour, compression). Budget more.
- **Asset-heavy by default.** The page runs two video/JPEG systems and still had residual lag [10:58](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=658s); expect to repeat "make it faster" and trade quality for speed.
- **Not mobile-optimized out of the box** — a separate pass you must not skip for a real site [13:11](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=791s).
- **Third-party dependencies shift.** A solo teenager's GitHub skill plus fast-moving proprietary models/platforms (Kling 3.0, Nano Banana Pro, Higgsfield, Antigravity) may change, break, or reprice; the Higgsfield link is affiliate.
- **The "$15K / $5K–$10K" pricing is aspirational.** It's his recollection of past resale prices and a title label ($15K appears only in the title; he says $5K–$10K on camera) [00:33](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=33s) — no client, invoice or sale is shown.
- **Keep the model names straight.** Claude Code orchestrates; Kling 3.0 and Nano Banana Pro are external, non-Claude models reached via Higgsfield. The title's "Nano Banana 2" is a label — the model is Nano Banana Pro.

## Variations

- **Skill-driven site, own it fully.** For the taste-skill and design-skill route in general, see [[Build a Distinctive Site with Design Skills]] and [[Escaping the Default AI Design Look]].
- **Scroll storytelling with owned assets and review.** For a scroll-driven page built from an intake with a verification pass, see [[Build a Scroll-Driven Landing Page]].
- **Mobile app instead of a site.** The same "Claude writes the code and prompts; external models make the media" split, applied to an animated app, is [[Vibe-Code an Animated Mobile App with Claude]].

## Sources

- [[Nick Saraev - Animated Sites with Claude Code and Kling]]: the three-step pipeline — taste-skill one-shot, Kling 3.0 clips seeded by Nano Banana Pro stills, hero wire-in with masking gradient, locomotive-scroll exploded view, JPEG-frame optimization and hero compression, screenshot feedback, and Netlify deploy.

## Related

- **Concepts:** [[Generating Images and Video with Claude]] · [[Escaping the Default AI Design Look]]
- **Techniques:** [[Build a Scroll-Driven Landing Page]] · [[Build a Distinctive Site with Design Skills]] · [[Vibe-Code an Animated Mobile App with Claude]]
- **Tools:** [[Claude Code]] · [[Higgsfield]]
- **People:** [[Leon Lin]] · [[Nick Saraev]]
- [[Home]]
