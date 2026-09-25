---
type: source
title: "Watch Me Vibe Code an Animated App with Claude Fable 5.1 + Seedance 2.5"
creator: "[[Jason Lee]]"
channel: Jason Lee
url: https://www.youtube.com/watch?v=29Vto7o2I2Q
video_id: 29Vto7o2I2Q
published: 2026-09-18
duration: 24:25
ingested: 2026-09-24
topics: [animated mobile apps, vibe coding, Claude Design, media generation, MCP]
tags: [source/youtube, topic/design, topic/media, topic/claude-code, topic/mcp]
---

# Watch Me Vibe Code an Animated App with Claude Fable 5.1 + Seedance 2.5

> **Creator:** [[Jason Lee]] · **Published:** 2026-09-18 · **Length:** 24:25 · [Watch on YouTube](https://www.youtube.com/watch?v=29Vto7o2I2Q)

## TL;DR

Jason Lee vibe-codes a clone of the mental-health app Finch inside [[Claude Code]], renaming the mascot to a baby alligator called "Chewy". The Claude model driving the build is **Fable 5.1**, which he prefers for design-heavy work. Because Claude has no native image or video model, all character art and backdrops come from **Higgsfield** — [[Higgsfield]] hosts GPT Image 2.5 (stills) and Seedance 2.5 (animation) and exposes an MCP connector inside Claude Code, so Claude writes the asset prompts and calls generation directly from the session. The `/design` command ([[Claude Design]]) builds a phone mockup in localhost; the back end is React Native + Expo EAS Build. Free Lottie micro-animations from LottieFiles supply the confetti effects. Context is fed to Claude as a Pinterest reference image plus screen recordings of the real app.

## Key takeaways

- Fable 5.1 is the Claude model; Higgsfield's GPT Image 2.5 and Seedance 2.5 are separate, external media models reached through an MCP connector — do not conflate them. [02:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=150s), [02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s)
- Context is king: screen recordings of the target app plus a reference character image let Claude infer pages, buttons and features. [05:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=302s), [09:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=593s)
- Claude writes the image/video prompts itself; the user only describes intent by voice. [08:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=510s), [20:56](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1256s)
- Clone the proven skeleton to ~90%, then differentiate rather than copying exactly. [11:47](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=707s)
- Parallelize: video generation takes ~10+ minutes, so build the back end while assets render. [15:12](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=912s)

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=0s) Intro

Goal: rebuild Finch, a mental-health app he says makes ~$1M/month, using Claude's latest model, Fable 5.1. [00:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=2s) The app isn't a simple habit tracker — it has a fully animated character with interactive buttons that makes it "feel alive," the way million-dollar apps like Duolingo do. [00:09](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=9s) Normally such animation needs a team of illustrators and motion designers; here every character and animation is made by describing it to Claude in plain English — something he says wasn't possible a few months ago without Illustrator/After Effects. [00:24](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=24s)

### [00:56](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=56s) App Breakdown

Finch (also called "Self-Care Pet") looks like a game but is a mental-health app, a high-demand App Store category. [00:57](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=57s) Its hook is gamification: complete a small real-world self-care task, log it, and your pet gains energy for adventures — you level up and unlock products. [01:20](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=80s) He cites Duolingo as the model for using animated characters to keep users returning. [01:52](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=112s) The video focuses on the design side: animated characters, confetti pages, strong mobile visuals. [02:18](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=138s)

### [02:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=149s) Tools Needed

He uses **Fable 5.1** as the driving Claude model, saying GPT-6 Astra is also capable but Fable has a slight edge on design, so he prefers it for design-heavy builds; the workflow is model-agnostic. [02:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=150s) Because Claude has no native image/video model, he uses Higgsfield, which hosts the latest models (he names GPT Image 2.5 and Seedance 2.5) and has a direct MCP connector to Claude, so he can control generation from the chat session. [02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s) Sponsor plug: Higgsfield just released pay-as-you-go API pricing (vs a subscription), claimed ~30–50% cheaper than competitor Fal AI, plus a 7-day promo of $15 free credits with a business email. [03:07](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=187s) (Treat pricing as promotional — see Caveats.)

### [04:32](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=272s) Start Prompting

Works in Claude Code (setup assumed) in a folder called "Chewy". [04:32](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=272s) Step 1: pick a character — he grabs a baby-alligator image from Pinterest as the mascot reference and saves it in the folder. [04:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=294s) Step 2: context — he screen-records the real Finch app and drops it in the folder so Claude learns every page and how buttons behave. [05:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=302s) He also pastes the App Store URL so Claude can research features and read reviews. [05:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=329s) Prompt 1 (dictated by voice): check the linked app, build a similar iOS app with a baby alligator named Chewy, break down the features/screens, and plan before building. [05:48](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=348s) Claude returns a breakdown of Finch, confirms it watched the screen recording, and suggests features. [06:24](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=384s) Prompt 2: build the home screen and main tabs first, using the Higgsfield MCP for all image/video generation, especially the backdrop (an outdoor garden with a lake/swamp) and the alligator, matching the character's style and color theme. [06:44](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=404s) He then invokes `/design` inside Claude Code to build the mockup, previewable in localhost inside a phone mockup. [07:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=449s) Claude isolates the character from the reference sticker image — stripping stars, hearts and the sticker outline — and produces the requested swamp backdrop. [07:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=473s) In Higgsfield he can see the generated images and the prompt Claude wrote automatically; he never wrote the image prompt himself. [08:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=510s)

### [08:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=523s) First Version

The first build sits in localhost inside a phone mockup — alligator on the backdrop, styling matching the reference — and looks good on the first try. [08:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=525s) Interactions work: completing a task shows confetti; check-off and skip buttons respond. [09:16](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=556s) Other pages (Quest, Shop, Friends, Profile) are all generated; the shop shows "not enough shells," so the back end isn't wired yet — but Claude inferred the flow from the screen recording. [09:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=583s) Takeaway: give Claude as much context as possible, and a screen recording is the easiest way. [09:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=593s) The static visuals feel "dead," so animation is coming — but onboarding is the next priority. [10:11](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=611s)

### [10:22](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=622s) Onboarding Flow

Onboarding is the set of screens shown right after download; he supplies a screen recording of Finch's onboarding (hatch a pet or log in, pick an egg, egg cracks, pet hatches). [10:27](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=627s) It's a series of questions (what you're struggling with, areas of support) leading to a paywall (free trial/subscribe), about 17–18 pages total. [11:05](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=665s) The rationale is to get the user bought into the concept before the paywall; he won't cover the marketing psychology in depth. His advice: recreate the skeleton to ~90%, then customize rather than copying exactly. [11:47](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=707s)

### [11:52](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=712s) Adding Onboarding Pages

Prompt 3: build the onboarding, watch the recorded flow in the folder, recreate the same pages and wording, use the Chewy alligator, and choose a fitting expression per page. [11:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=713s) Claude calls Higgsfield again to generate egg-hatching mockup illustrations (tap → egg cracks → alligator inside). [12:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=734s) The result mirrors Finch's flow with slightly different buttons (good — not identical): eight egg colors, pick and tap to hatch, then gender, naming, paywall, day-one streak, goal commit and an add-widget prompt. The hatched character is slightly cut off at the sides — easily fixable. Whole onboarding generation took ~10–15 minutes. [13:38](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=818s) Fix technique: send a screenshot of a broken image or an egg with an unwanted outline and ask Claude to correct it. [13:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=825s)

### [14:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=842s) Animating the App

Prompt 4 (pasted, long): animate the alligator from onboarding through the home screen; on the home screen have it walk around (deliberately vague — "give me your best shot"); animate the background water, plants and trees for a moving backdrop. [14:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=854s) He instructs Claude to reference the character and background in Higgsfield and animate the assets with Seedance 2.5, then swap the static version for the animated one. [14:51](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=891s) Higgsfield video generation takes ~10 minutes or more, leaving Claude idle — so he uses that time to build the back end. [15:12](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=912s) Stack: React Native (so the codebase can later target Android) plus Expo. [15:41](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=941s) Expo Go gives a quick iPhone preview but no database or Google sign-in — too basic. [15:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=954s) Expo EAS Build previews the app as if App-Store-approved (app icon, Google sign-in) but needs an Apple Developer account (~$99/yr) and a free Expo account; he uses EAS Build. [16:18](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=978s) Prompt 5: while images generate, build the functionality with React Native + Expo EAS Build, using his existing Apple Developer and Expo accounts, and ask him for any API keys or credentials needed. [17:00](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1020s) The animation returns: the alligator wiggles, looks left/right and blinks, far better than a static image. [17:51](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1071s) Feedback technique: instead of screenshots, record a narrated Loom walkthrough with the mouse pointing, which Claude watches to understand what you're referencing — faster than annotating screenshots. [18:36](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1116s) First home-screen pass is glitchy: the alligator scales big↔small while walking and the cloud doesn't loop cleanly. [19:16](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1156s) Prompt 6 (with screenshot): make the alligator walk left→right→center, pick up a coffee cup, drink, put it down, walk back; keep the cloud still; update the mockup. [19:48](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1188s) The re-preview works — the coffee sequence plays, the cloud is stationary, the water/plants animation untouched. [20:42](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1242s) His point: you create any animation by describing what's in your head — Claude writes the prompt and generates the assets in Higgsfield. [20:56](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1256s)

### [21:23](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1283s) Adding Lottie Animations

For UI micro-animations (loading screens, confetti on tapping a goal), don't build from scratch — use LottieFiles, a library of free Lottie animations. [21:23](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1283s) Filter by "success" to find check-marks and confetti, then pick one. Lottie lets you recolor elements (not baked in) to match the app theme and change playback speed (he leaves it at 1x), then download. [21:57](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1317s) Prompt 7: drag the downloaded Lottie file into Claude and ask to show it centered on the home screen when a goal is selected and the user presses "complete." [22:25](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1345s) Applied in ~2 minutes; tapping a check-mark triggers the confetti, and you can specify size and placement in plain English. [22:46](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1366s)

### [23:08](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1388s) Preview on iPhone

Claude finished the back end, so he previews on a physical phone: the iPhone is mirrored on the left, the Chrome preview on the right, and the app icon was also generated with Higgsfield. [23:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1394s) Opening the app on the iPhone shows the same UI as the browser, but now with real button taps and swipe gestures. He kept the video quick on purpose and invites questions on design, back end, Expo setup or App Store publishing for a follow-up. [23:55](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1435s)

## Caveats & disagreements

- **"Finch makes ~$1M/month"** is asserted with no source — treat as an unverified claim. [00:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=2s)
- **IP / clone / App Store risk.** The build recreates Finch's screens, onboarding wording and mechanics directly from screen recordings. The creator himself warns not to copy exactly for a real app. [11:26](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=686s) Cloning a live commercial app's UI and flow carries IP exposure and App Store review risk.
- **Back end not shown working end-to-end.** During most of the demo it isn't wired (the shop shows "not enough shells"), and it's said to finish only near the end; on-device it's shown only opening the app, not exercising a database or sign-in. [09:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=583s), [23:08](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1388s)
- **Glitchy first animation pass.** The initial Seedance animation had the alligator scaling and the cloud failing to loop, needing a correction round — gen-video output often needs several passes. [19:16](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1156s)
- **Higgsfield is the sponsor.** The pricing claims ("~30–50% cheaper than Fal AI", "$15 free credits", 7-day promo) are promotional/affiliate; verify current pricing independently. [03:07](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=187s)
- **"Fable 5.1 has a slight edge on design over GPT-6 Astra"** is the creator's subjective preference, not a benchmark. [02:39](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=159s)
- **Time and cost are glossed over.** Repeated ~10–15 min generation waits, Higgsfield credits and the ~$99/yr Apple Developer account are downplayed by fast-forwarding.

## Build from this

- [[Vibe-Code an Animated Mobile App with Claude]]

## Resources mentioned

- **Fable 5.1** — the Claude model driving the build; preferred for design-heavy work. [02:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=150s)
- [[Claude Code]] — the environment the build runs in; hosts the Higgsfield MCP connector and the `/design` command. [04:32](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=272s)
- [[Claude Design]] (`/design`) — invoked inside Claude Code to build the phone mockup in localhost. [07:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=449s)
- [[Higgsfield]] — external media platform with an MCP connector to Claude; hosts GPT Image 2.5 and Seedance 2.5 and generated the app icon. Video sponsor. [02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s)
- Seedance 2.5 — video model (via Higgsfield) used to animate the alligator and backdrop. [14:51](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=891s)
- GPT Image 2.5 — image model (via Higgsfield) for still generation. [02:55](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=175s)
- GPT-6 Astra — named as a viable alternative model to Fable 5.1. [02:33](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=153s)
- React Native + Expo (Expo Go / Expo EAS Build) — the app framework and build/preview tooling; EAS Build for a store-like device preview. [15:41](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=941s), [16:18](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=978s)
- Apple Developer account (~$99/yr) — required for EAS Build. [16:18](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=978s)
- LottieFiles / Lottie — free, recolorable micro-animations for confetti/success effects. [21:23](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1283s)
- Pinterest — source of the reference alligator mascot image. [04:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=294s)
- Loom — narrated screen-recording used for feedback to Claude. [18:36](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1116s)
- Finch / "Self-Care Pet" (the app being cloned) and Duolingo (engagement exemplar) — reference apps, not build tools. [00:57](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=57s), [01:52](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=112s)

## Beyond the source

- Claude has no first-party image or video generation model; media in this workflow comes entirely from external models reached through Higgsfield's MCP connector. See [[Generating Images and Video with Claude]] for the general pattern of Claude as prompt-writer/orchestrator for outside media models.

## Transcript notes

Non-obvious caption fixes applied silently in the prose above:
- "Claw" / "Claw's" / "cloud" / "Cloud Code" → **Claude** / **Claude Code** (e.g. "Claw's latest model" [00:09], "Cloud Code" [04:32]).
- "claw design" → **Claude Design**, invoked as the `/design` command. [07:34](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=454s)
- "Hicksfield" / "Higsfield" / "Hickfield" / "Pixfield" → **Higgsfield**. [02:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=173s), [23:22](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1402s)
- "Cance 2.5" → **Seedance 2.5**. [02:58](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=178s), [14:51](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=891s)
- "GPD image 2.5" → **GPT Image 2.5**. [02:55](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=175s)
- "GP6 Astra" / "GPD 6 Astra" → **GPT-6 Astra**. [02:33](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=153s)
- "File AI" → **Fal AI** (the competitor in the sponsor comparison). [03:20](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=200s)
- "Li Files" → **LottieFiles**; "Lotty" → **Lottie**. [21:38](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1298s)
- "EAS built" → **EAS Build**; "Dualingo" → **Duolingo**; "payw wall" → **paywall**; "BB alligator" → **baby alligator**.

## Related

- [[Generating Images and Video with Claude]]
- [[Higgsfield]]
- [[Claude Code]]
- [[Claude Design]]
- [[Choosing a Claude Model]]
- [[Vibe-Code an Animated Mobile App with Claude]]
