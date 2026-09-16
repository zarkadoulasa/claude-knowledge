---
type: technique
goal: "Make a short AI video (a UGC-style ad or a motion graphic) by agreeing a visual storyboard before any slow render, having the agent write the build prompt from it, and finishing in two or three human-judged revision passes instead of an autonomous loop"
difficulty: intermediate
time_to_build: "1–2 hours for a first 10–15 second piece; a single render can take 10–23 minutes (Chase's timings), plus review"
sources: ["[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]"]
tools: ["[[Claude Code]]", "[[Higgsfield]]", "[[OpenAI Codex]]"]
tags: [topic/media, topic/marketing, topic/planning, topic/prompting, topic/verification, topic/loops]
---

# Storyboard-First AI Video and Motion Graphics

> **Provenance.** This note combines two flows.
>
> - **[[Nate Herk - Claude as a One-Person Marketing Team]]:** Claude, connected to [[Higgsfield]], makes UGC-style ads from one prompt. It produces characters, then storyboards, then clips, then runs a QA pass on itself.
> - **[[Chase AI - GPT-6 Astra Motion Design in After Effects]]:** GPT-6 Astra in [[OpenAI Codex]] drives After Effects in three steps: storyboard, agent-written build prompt, targeted revisions. Chase doesn't use Claude. He notes that [[Claude Code]] would need image generation added through an MCP such as Higgsfield's ([02:58](https://www.youtube.com/watch?v=C8dWdic-oK4&t=178s)).
>
> **The folder layout, storyboard template and prompts are original vault starter content.** Neither creator shows his prompt files.

## Goal

One finished 10–15 second clip that meets three conditions:

- you approved its storyboard before the first render;
- its build prompt names every beat, duration and transition;
- it reached "done" in at most three passes that you reviewed.

## Use when

- **Each pass is slow or expensive.** Chase's builds take 10–20 minutes for 15–20 seconds ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)). Nate's UGC run was his priciest ([31:12](https://www.youtube.com/watch?v=yCACmFTiCto&t=1872s)), and slower because it also made images, boards and QA passes ([34:26](https://www.youtube.com/watch?v=yCACmFTiCto&t=2066s)).
- **Quality is a matter of taste** that no script can test: pacing, feel, whether the result looks organic.
- **Not needed for one animated still.** Jay's single prompt to Kling, keeping the text fixed and the aspect ratio unchanged ([12:41](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=761s)), is enough; see [[Generate On-Brand Images from Claude Code]].

## The principle: a human judges a few passes

- **Why storyboard.** Chase does it to avoid spending hours re-prompting the same build ([02:47](https://www.youtube.com/watch?v=C8dWdic-oK4&t=167s)).
- **No loops.** Unless you know what you're doing, don't wrap these renders in a loop ([07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s)).
- **A human stays involved.** Creative work needs someone hands-on ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)), not an agent checking itself against the storyboard on every pass ([07:44](https://www.youtube.com/watch?v=C8dWdic-oK4&t=464s)).
- **Few passes.** He usually finished in two or three iterations ([06:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=410s)).
- **Agent checks still help as a filter.** Nate's run rejected at least one clip before reporting ([32:30](https://www.youtube.com/watch?v=yCACmFTiCto&t=1950s)).

*Vault reading:* loop when a pass is cheap and there's an objective check. Otherwise put a human gate between passes. See [[Loop Engineering]] and [[Permissions and Approval Gates]].

## Prerequisites

- **Claude route:**
  - Claude Code plus a video-capable generator. Nate bought a Higgsfield plan ([16:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=987s)) and added it as a custom connector ([16:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1001s)).
  - For motion graphics rendered from code, see HyperFrames (Beyond the source).
- **Chase's route:**
  - GPT-6 Astra, After Effects and Higgsfield's Motion Designer plugin ([00:55](https://www.youtube.com/watch?v=C8dWdic-oK4&t=55s)).
  - The plugin bridges the model to After Effects and bundles skills for using it ([01:25](https://www.youtube.com/watch?v=C8dWdic-oK4&t=85s)).
- **A brief** giving pain, person and promise, plus length, channel and aspect ratio. See [[Build a Brand-Aware Marketing Project]].
- **A spending cap**, and an `ask` rule on the generation tools (starter rule in [[Generate On-Brand Images from Claude Code]]).

## Steps

1. **Collect references.**
   - **A reference video.** Chase gives the agent a post link; it watches the video, takes screenshots and uses them as a guide ([03:48](https://www.youtube.com/watch?v=C8dWdic-oK4&t=228s)). The result isn't an exact copy ([03:55](https://www.youtube.com/watch?v=C8dWdic-oK4&t=235s)).
   - **An effects library.** If you're not a designer, have the agent build a library of motion effect types ([05:43](https://www.youtube.com/watch?v=C8dWdic-oK4&t=343s)).
   - **Real UGC.** For UGC, Nate suggests having Claude study real examples first ([33:34](https://www.youtube.com/watch?v=yCACmFTiCto&t=2014s)).
2. **Approve scripts (UGC).** This is Nate's other fix in the same breath ([33:34](https://www.youtube.com/watch?v=yCACmFTiCto&t=2014s)). His run skipped it, and the ads came out realistic but still salesy ([33:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=2004s)).
3. **Create reusable characters (UGC).** Nate's run began with character images, which you can keep as a consistent brand avatar ([31:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=1905s)).
4. **Storyboard.**
   - **See the plan first.** Chase has the agent draw a storyboard so he can see its thinking before anything is built ([02:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=124s)). Discussing a visual plan was far easier than editing afterwards ([02:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=142s)).
   - **Expect cuts.** He eventually cut the piece from 18 seconds to 10 ([02:16](https://www.youtube.com/watch?v=C8dWdic-oK4&t=136s)). *Vault note:* cutting at the board is cheaper than after a render.
   - **Boards give control.** Nate says planning shots as images first gave the video model more control over the story ([32:14](https://www.youtube.com/watch?v=yCACmFTiCto&t=1934s)).
5. **Gate 1: approve the board and a cost estimate.** This is a vault step. Nate's one-prompt run had no gate.
6. **Have the agent write the build prompt.** Chase gets Codex to write it ([04:18](https://www.youtube.com/watch?v=C8dWdic-oK4&t=258s)). It includes:
   - duration and tool;
   - reference files ([04:36](https://www.youtube.com/watch?v=C8dWdic-oK4&t=276s));
   - beats taken from the storyboard ([04:48](https://www.youtube.com/watch?v=C8dWdic-oK4&t=288s));
   - what the motion should look like ([04:55](https://www.youtube.com/watch?v=C8dWdic-oK4&t=295s)).

   He has the agent fill prompt templates from the storyboard ([05:23](https://www.youtube.com/watch?v=C8dWdic-oK4&t=323s)). **Spell out pacing now:** left alone, scenes hold for 2.5–3 seconds and the piece drags ([07:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=424s)).
7. **Render.** A 15-second build took Chase almost 23 minutes ([05:58](https://www.youtube.com/watch?v=C8dWdic-oK4&t=358s)). Nate's brief allowed some edited clips and some raw takes ([24:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1481s)), yet every clip he showed came back in one- to two-second cuts, which he says Claude chose ([34:20](https://www.youtube.com/watch?v=yCACmFTiCto&t=2060s)). Name the edit style for each variant (e.g. one raw 15-second take) rather than asking loosely for a mix.
8. **Run agent QA as a filter.**
   - **What it checks.** Chase's plugin compares the build to the storyboard and reviews the render ([06:07](https://www.youtube.com/watch?v=C8dWdic-oK4&t=367s)). Nate's run kept a QA folder of screenshots ([32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s)).
   - **What it misses.** A wrong logo still reached Nate's sizzle reel ([28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s)).
9. **Gate 2: watch it yourself, then send targeted revisions.**
   - **Everything is a prompt away.** Edits cover the sound design and music too ([06:43](https://www.youtube.com/watch?v=C8dWdic-oK4&t=403s)).
   - **Say when and what.** Name exactly when and what should change ([07:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=442s)).
   - **Cap it.** Stop after three passes. If it's still wrong, fix the storyboard rather than rendering again.
10. **Codify what worked.** Nate makes skills from outputs he liked and rules against ones he didn't ([30:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1802s)). Keep the characters, templates and final prompts together.

## Starter files & prompts

*Original vault starter content.*

```text
output/video/<campaign>/
├── brief.md        # pain, person, promise, length, channel, ratio, cap
├── refs/           # links, screenshots, effects-library.md
├── creators/       # reusable character stills (UGC)
├── boards/         # one still per beat + storyboard.md
├── prompts/        # build-v1.md, revise-v2.md ...
├── renders/        # v1.mp4, v2.mp4 ...
├── qa/             # agent frame grabs and notes
└── log.md          # pass, time, cost, verdict
```

### boards/storyboard.md

```markdown
# <title> — <length> s, <ratio>, <channel>
| Beat | Time (s) | On screen | Motion / transition in | Text or VO | Audio |
|---|---|---|---|---|---|
| 1 | 0.0–1.5 | | hard cut | | |
| 2 | 1.5–3.0 | | whip pan | | |
Rules: no beat longer than 2 s unless marked HOLD. Logo and product must match refs/.
```

### Prompts

```text
PROMPT 1 (storyboard): Read brief.md and refs/. Render no video yet. Draw one still per
beat into boards/ and fill storyboard.md with timings that add up to <length> s.
Then give the render plan: tool, model, expected passes, estimated cost. Wait for me.

PROMPT 2 (build prompt): Storyboard approved. Write prompts/build-v1.md for <tool>:
duration, ratio, reference files, then one section per beat with exact start/end
seconds, what's on screen, motion, transition in, text and audio. Show me before building.

PROMPT 3 (QA): Before reporting done, save a frame from the middle of each beat to qa/.
Per beat, check timing against storyboard.md, logo and product against refs/, spelling,
and warped hands or faces. List every failure; don't call it finished if any remain.

PROMPT 4 (revision v<N>): Change only these and keep everything else identical:
| When (s) | Problem | Change to |
| 2.0–4.5 | lingers | cut at 3.2, whip into beat 3 |
| 7.0 | music stops | keep bed to the end, duck under VO |
Update storyboard.md, add the pass to log.md, then render.
```

## Done when

- [ ] You approved `storyboard.md` before the first render.
- [ ] The build prompt lists every beat with exact times and transitions.
- [ ] Every beat has a QA frame, and you watched the final render yourself.
- [ ] Logo, product and on-screen text match the references.
- [ ] It took three passes or fewer, each logged with time and cost.
- [ ] For UGC-style ads, scripts were approved and the disclosure question below was checked.

## Pitfalls

- **Cost creep.** Video costs far more than stills. Nate's sizzle reel came to about $17.55 ([29:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1746s)), while 18 ad images cost $3.43 ([27:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=1656s)). Estimate before every pass.
- **Default pacing.** Leave timings unstated and scenes drift to 2.5–3 seconds ([07:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=424s)).
- **Vague revisions.** "Make it snappier" buys another full render. Give time ranges and exact changes ([07:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=442s)).
- **Self-graded sign-off.** Agent QA is a filter, not approval (step 8).
- **Choppy edits from a loose brief.** Nate asked for a mix of edited and raw takes ([24:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1481s)), but every clip shown came back fast-cut, which he says the run chose ([34:14](https://www.youtube.com/watch?v=yCACmFTiCto&t=2054s)). Name the edit style per variant (step 7).
- **AI "customers."** Nate's generated people review the product ([24:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1467s)). In US ads, testimonials from people who don't exist can breach FTC rules (Beyond the source).
- **Plugin claims.** Chase calls the plugin free and says it uses no credits ([00:21](https://www.youtube.com/watch?v=C8dWdic-oK4&t=21s)). Higgsfield's blog lists paid subscriptions and says Higgsfield generations use credits (Beyond the source).

## Where sources disagree

- **One prompt, or a gate at each step?**
  - **Nate:** one UGC prompt runs from characters to QA unattended ([24:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1450s)).
  - **Chase:** agrees the storyboard first ([02:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=142s)).
  - **Resolution:** Nate later suggests approving scripts before scripts and boards go to video ([33:34](https://www.youtube.com/watch?v=yCACmFTiCto&t=2014s)), so this note follows Chase.
- **Who decides it's done?**
  - **Nate:** credits the agent for checking everything before calling it finished ([32:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=1977s)).
  - **Chase:** a human judges each pass ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)).
- **Loops or not?**
  - **Here:** Chase avoids loops ([07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s)).
  - **[[Chase AI - The Agentic OS Setup for Claude Code]]:** he adds self-improvement loops to automations ([12:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=728s)).
  - **Reading:** a boundary, not a reversal. See the principle above.

## Sources

- [[Chase AI - GPT-6 Astra Motion Design in After Effects]]:
  - storyboard ([01:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=110s))
  - build prompt ([04:13](https://www.youtube.com/watch?v=C8dWdic-oK4&t=253s))
  - editing and pacing ([06:23](https://www.youtube.com/watch?v=C8dWdic-oK4&t=383s))
  - Caption fixes: "Codeex" is Codex; "GBT6 Astro" is GPT-6 Astra.
- [[Nate Herk - Claude as a One-Person Marketing Team]]:
  - UGC prompt ([24:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1450s))
  - characters, boards and QA ([31:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1867s))
  - verdict ([33:19](https://www.youtube.com/watch?v=yCACmFTiCto&t=1999s))
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]:
  - animating a still ([12:41](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=761s))

## Beyond the source

*Checked 2026-09-15.*

- **Higgsfield for agents.**
  - In Claude, add `https://mcp.higgsfield.ai/mcp` as a custom connector.
  - For Claude Code, Higgsfield points to its CLI (`npm i -g @higgsfield/cli`, `higgsfield auth login`) plus `npx skills add higgsfield-ai/skills`.
  - Needs a paid plan; every agent generation uses credits.
  - Source: [Higgsfield help](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent).
- **Motion Designer.**
  - Run it with `/use-after-effects` in ChatGPT, or through Higgsfield's MCP from Claude.
  - The blog lists Higgsfield, ChatGPT and After Effects subscriptions as required, and says Higgsfield generations use credits at web rates.
  - Open source isn't mentioned.
  - Sources: [product page](https://higgsfield.ai/ai-motion-designer), [blog](https://higgsfield.ai/blog/ai-motion-designer-after-effects-gpt).
- **HyperFrames.**
  - HeyGen's Apache-2.0 framework renders HTML to MP4 with the same result every time, using headless Chrome and FFmpeg.
  - Install with `npx skills add heygen-com/hyperframes`.
  - Source: [GitHub](https://github.com/heygen-com/hyperframes).
- **Kling 3.0 standard image-to-video on fal.**
  - Clips run 3–15 s, with audio on by default.
  - Costs $0.084/s silent, $0.126/s with audio.
  - Source: [fal docs](https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video/llms.txt).
- **FTC rule (2024).** It bans testimonials that falsely appear to come from a real person, AI-generated ones included, or that misstate the reviewer's experience. Source: [FTC](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials).

## Related

- [[Generating Images and Video with Claude]] · [[Plan Before Executing]] · [[Verification Before Done]] · [[Build a Skill from a Successful Run]] · [[Escaping the Default AI Design Look]]
- [[Chase AI]] · [[Nate Herk]] · [[Jay E]] · [[Home]]
