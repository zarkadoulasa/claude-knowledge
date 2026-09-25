---
type: technique
goal: "Vibe-code an animated mobile app in Claude Code — Claude (Fable 5.1) writes the code and asset prompts, external models via Higgsfield make the art/animation"
difficulty: intermediate
time_to_build: "a day"
sources: ["[[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]"]
tools: ["[[Claude Code]]", "[[Claude Design]]", "[[Higgsfield]]"]
tags: [topic/design, topic/media, topic/claude-code, topic/mcp]
---

# Vibe-Code an Animated Mobile App with Claude

## Goal

Rebuild a "feels alive" mobile app — an animated mascot, an onboarding funnel, a paywall — by describing what you want in plain English, and preview it on a real iPhone.

- **The split that matters.** [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]] runs the whole build in [[Claude Code]] on the Claude model **Fable 5.1**, chosen for design-heavy work [02:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=150s). But Claude has no image or video model of its own [02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s), so **Claude writes the code and the asset prompts; the actual images and videos come from external models** (GPT Image 2.5 stills, Seedance 2.5 animation) reached through the [[Higgsfield]] MCP connector [02:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=173s). Jason describes assets by voice and never hand-writes an image prompt [08:31](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=511s). See [[Generating Images and Video with Claude]].
- **The demo.** He clones the mental-health app Finch as a baby-alligator mascot named "Chewy" [05:48](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=348s), then animates it.

## Use when

- **You want a gamified, animated app** whose mascot drives retention, like Duolingo or Finch [01:52](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=112s) — not a plain utility.
- **You can supply a reference character and a recording of the flow you're recreating.** Context is what lets Claude infer the pages and buttons [09:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=593s).
- **You have design taste but not illustration/After Effects skills** [00:40](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=40s).
- **Not for cloning a live commercial app to ship as-is** — see the IP/App Store pitfall below.

## Prerequisites

- **[[Claude Code]] set up**, working in a project folder (his is called Chewy) [04:32](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=272s). *Vault:* use git so you can diff correction rounds.
- **A Claude model for design work** — he prefers **Fable 5.1**; he says GPT-6 Astra also works and the workflow is model-agnostic [02:33](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=153s). See [[Choosing a Claude Model]].
- **[[Higgsfield]] connected via its MCP** so Claude can generate stills and video from the chat session [03:00](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=180s). Assets cost credits (external, not Claude).
- **A reference character image** (he grabbed a baby alligator from Pinterest) [04:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=294s).
- **Screen recordings of the target app** — both the main flow and the onboarding — plus the App Store URL [05:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=302s).
- **For device preview:** an Expo account (free) and an **Apple Developer account (~$99/yr)** for Expo EAS Build [16:32](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=992s).

## Steps

1. **Fill a context folder before prompting.** Save into the project folder: the reference character image [04:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=294s); a screen recording of the real app so Claude learns the pages and how buttons behave [05:07](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=307s); and the App Store URL so it can read features and reviews [05:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=329s). Record the onboarding flow too — you'll need it in step 5.

2. **Prompt plan-first.** Dictate: check the linked app, build a similar iOS app with your own character, break down the features and screens, and plan before building anything [05:48](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=348s). Because the files are already in the folder, nothing needs attaching [06:11](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=371s). Claude comes back confirming it watched the recording and listing what it saw [06:24](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=384s).

3. **Build the home screen and main tabs, asset generation routed through Higgsfield.** Prompt: build the home screen and main tabs first, and use the Higgsfield MCP for all image/video generation, especially the backdrop and the character [06:44](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=404s). Specify the scene, illustration style and colour theme to match the character — e.g. an outdoor garden with a lake/swamp [07:12](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=432s).

4. **Build the mockup with `/design`, previewed in localhost.** Invoke [[Claude Design]] inside Claude Code: `/design` to build the app mockup, previewable in localhost in a phone mockup [07:29](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=449s). Ask Claude to **isolate the character from the reference sticker** — strip extra stars/hearts and the sticker outline for clean art [07:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=473s). In Higgsfield you can see the images and the prompt Claude wrote automatically [08:23](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=503s). The first build lands in localhost looking right on the first try [08:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=525s), though the back end isn't wired (the shop shows "not enough shells") [09:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=583s).

5. **Recreate the onboarding from its recording.** Onboarding is the ~17–18 pages after download, ending in a paywall [11:05](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=665s). Prompt: build the onboarding, watch the recorded flow in the folder, recreate the same pages and wording, use your character, and pick a fitting expression per page [11:53](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=713s). Claude calls Higgsfield again for the egg-hatching illustrations [12:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=734s). Aim for ~90% of the skeleton, then customise rather than copying exactly [11:47](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=707s).

6. **Animate with Seedance 2.5, then swap static for animated.** Prompt: animate the character from onboarding through the home screen; on the home screen have it walk around ("give me your best shot" — deliberately vague) [14:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=854s); animate the background water, plants and trees for a moving backdrop [14:37](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=877s); reference the character and background in Higgsfield, use **Seedance 2.5** to animate, and swap the static version for the animated one [14:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=885s). First passes are glitchy — the alligator scaled big↔small, the cloud didn't loop [19:16](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1156s). Fix with a specific motion prompt plus a screenshot: walk left→right→back to centre, pick up a coffee cup, drink, put it down, return; keep the cloud still while leaving everything else unchanged; then update the mockup [19:48](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1188s). The re-preview walks and does the coffee sequence correctly [20:42](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1242s).

7. **Build the React Native + Expo back end while assets render.** Higgsfield generation takes ~10 min or more, so Claude sits idle — use that time for the back end [15:12](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=912s). Stack: React Native (so the same codebase can later target Android) with Expo [15:41](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=941s). Expo Go is a quick preview but no database or Google sign-in [15:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=954s); **Expo EAS Build** previews as if App-Store-approved (app icon, Google sign-in) but needs the Apple Developer + Expo accounts [16:18](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=978s). Prompt: build the functionality with React Native + Expo EAS Build; state that you have the accounts; ask Claude to guide the connection and request any API keys or credentials it needs [17:00](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1020s). That prompt is enough to make Claude ask setup questions and walk you through Expo [17:28](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1048s).

8. **Drop in Lottie micro-animations.** For UI touches like confetti, don't build from scratch — grab a free animation from LottieFiles, filter by "success" [21:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1303s), recolour it to your theme and leave speed at 1x [21:57](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1317s), then download. Drag the file into Claude and ask for it centred on the home screen when a goal is selected and the user presses "complete" [22:25](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1345s). Applied in ~2 min; you can specify size and placement in plain English [22:46](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1366s).

9. **Preview on a real iPhone.** Once the back end finishes, open the app on the device — same as the browser preview, but now you can feel real taps and swipe gestures [23:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1410s). The app icon was also generated with Higgsfield [23:14](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1394s).

**Feedback throughout:** for a single fix, drop a screenshot of the broken element into Claude [13:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=825s); for many at once, record a narrated Loom walkthrough with the mouse pointing — Claude watches it and understands what you're pointing at, faster than annotating screenshots [18:36](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1116s).

## Starter files & prompts

*Vault starter content: original wording, distilled from the video's prompts, not quoted from it.*

**Project folder before you start**

```text
project/
  reference-character.png      # the mascot reference (isolated in step 4)
  app-main-flow.mov            # screen recording of the target app's main flow
  app-onboarding.mov           # screen recording of its onboarding, for step 5
  APPSTORE-URL.txt             # store link, for feature + review research
```

**Prompt skeletons (paraphrased from the build)**

```text
1 Plan-first: "Check the app at <URL>. I want a similar iOS app but with
  <character>. Break down the features and screens. Plan before building."

2 Home + tabs: "Build the home screen and main tabs. Use the Higgsfield MCP
  for all image/video. Backdrop: <scene>, illustration style and colours
  matching the character."

3 Mockup: "/design build the mobile-app mockup, previewable in localhost in a
  phone mockup. Isolate the character from the reference sticker (drop the
  stars/hearts and the outline)."

4 Onboarding: "Build the onboarding. Watch app-onboarding.mov and recreate the
  same pages and wording with <character>; pick a fitting expression per page."

5 Animate: "Animate <character> from onboarding to home. On home, have it walk
  around. Animate the background water/plants. Reference the character and
  background in Higgsfield, animate with Seedance 2.5, swap static for animated."

6 Back end (while assets render): "Build the functionality in React Native +
  Expo EAS Build so I can preview on my phone. I have Apple Developer + Expo
  accounts — guide the connection and ask for any keys/credentials you need."
```

## Done when

- [ ] The context folder holds a reference character, main-flow and onboarding recordings, and the store URL
- [ ] Claude planned the screens before building
- [ ] Home screen and tabs render in a localhost phone mockup with a Higgsfield-generated character and backdrop
- [ ] The character is cleanly isolated from its reference sticker
- [ ] The onboarding flow through the paywall is recreated to ~90%, then customised
- [ ] The character and backdrop are animated (Seedance 2.5) and the animated versions replace the static ones
- [ ] Glitchy first-pass motion has been corrected with a specific motion prompt
- [ ] Lottie micro-animations trigger on the right actions
- [ ] The app opens and is navigable on a physical iPhone via Expo EAS Build

## Pitfalls

- **Claude has no native image/video model.** All art and animation are external, reached through Higgsfield — they cost credits and each pass can take ~10+ min [15:12](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=912s). Parallelise: build the back end while assets render.
- **First animation passes are glitchy.** Expect correction rounds — the alligator scaled and the cloud wouldn't loop until re-prompted (step 6).
- **The back end isn't automatically production-ready.** During the demo it wasn't wired (the shop shows "not enough shells") [09:43](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=583s), and it's only said to finish near the end; the auto-built React Native/Expo stack isn't shown working end-to-end beyond opening the app.
- **Cloning a live app carries IP and App Store risk.** The build copies Finch's screens, wording and mechanics from recordings; the creator himself warns not to copy exactly for a real app [11:26](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=686s). Recreate the skeleton, then make it your own.
- **Promo figures are marketing.** "Finch makes ~$1M/month" is asserted with no source [00:02](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=2s), and Higgsfield's pricing/credit claims are sponsor framing — Higgsfield is the video's sponsor. Verify current pricing yourself. The Apple Developer account is a real ~$99/yr cost.
- **Model-name confusion.** Fable 5.1 is the Claude model; GPT Image 2.5 and Seedance 2.5 are Higgsfield-hosted, non-Claude models. Keep them distinct.

## Variations

- **Static-only build.** Stop after step 5 for a non-animated mockup if you don't want to spend on video generation.
- **Model swap.** Use GPT-6 Astra instead of Fable 5.1 — the workflow is the same [02:47](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=167s).
- **Quick device preview.** Use Expo Go (no Apple Developer account) if you only need to swipe through the UI and don't need a database or Google sign-in [15:54](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=954s).
- **Web equivalent.** For a marketing/landing site rather than a mobile app, see [[Build an Animated Marketing Site with Claude Code and Kling]].

## Sources

- [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]: the full build — context folder, plan-first prompt, `/design` mockup, character isolation, onboarding recreation, Seedance 2.5 animation, React Native + Expo EAS Build back end, Lottie micro-animations, iPhone preview, and the screenshot/Loom feedback loops.

## Related

- **Concepts:** [[Generating Images and Video with Claude]]
- **Techniques:** [[Build an Animated Marketing Site with Claude Code and Kling]]
- **Tools:** [[Claude Code]] · [[Claude Design]] · [[Higgsfield]]
- **Model choice:** [[Choosing a Claude Model]]
- [[Home]]
