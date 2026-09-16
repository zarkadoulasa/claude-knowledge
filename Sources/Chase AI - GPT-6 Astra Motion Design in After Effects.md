---
type: source
title: "GPT-6 Astra Just Unlocked Motion Design + After Effects"
creator: "[[Chase AI]]"
channel: "Chase AI"
url: https://www.youtube.com/watch?v=C8dWdic-oK4
video_id: C8dWdic-oK4
published: 2026-09-14
duration: "8:36"
ingested: 2026-09-15
topics: [motion graphics, After Effects, storyboarding, reference videos, build prompts, revision prompts, pacing, human in the loop, Higgsfield plugin]
tags: [source/youtube, topic/media, topic/design, topic/planning, topic/prompting, topic/loops, topic/verification, topic/mcp, topic/skills]
---

# Chase AI - GPT-6 Astra Motion Design in After Effects

> **Creator:** [[Chase AI]] · **Published:** 2026-09-14 · **Length:** 8:36 · [Watch on YouTube](https://www.youtube.com/watch?v=C8dWdic-oK4)

## TL;DR

Chase has never used After Effects. He makes short motion graphics by letting OpenAI's GPT-6 Astra drive After Effects from [[OpenAI Codex]] through [[Higgsfield]]'s Motion Designer plugin. He works in three steps: storyboard; have the agent write a beat-by-beat build prompt and build; then revise with specific prompts while a human judges each pass.

**Claude barely features.** In the tutorial, [[Claude Code]] comes up once, as a harness that would need something like the Higgsfield MCP to generate storyboard images [02:58](https://www.youtube.com/watch?v=C8dWdic-oK4&t=178s). Its only other mention is in the outro course plug. The description says the video combines GPT-6 Astra with Claude Fable 5.1, but Fable is never mentioned. What transfers is the workflow.

## Key takeaways

- **Plan by execution cost, not task size.** A 15–20 second graphic can take 10–20 minutes to build [02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s), so agree a storyboard before rendering rather than re-prompting for hours. See [[Storyboard-First AI Video and Motion Graphics]] and [[Plan Before Executing]].
- **The storyboard feeds the prompt.** Its beats go into the build prompt, and Codex pulls them across itself [04:46](https://www.youtube.com/watch?v=C8dWdic-oK4&t=286s).
- **Let the agent write the build prompt** [04:18](https://www.youtube.com/watch?v=C8dWdic-oK4&t=258s). It should cover duration and tool, reference files, one beat per scene [04:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=280s), and how the motion should look.
- **Reference videos stand in for vocabulary you lack.** Given a post link, the agent watched the video, took screenshots and used them as a guide [03:48](https://www.youtube.com/watch?v=C8dWdic-oK4&t=228s). See [[Escaping the Default AI Design Look]].
- **Have the agent map your unknown unknowns.** Ask it to build a library of effect types [05:43](https://www.youtube.com/watch?v=C8dWdic-oK4&t=343s).
- **The default pacing tell.** Left alone, it holds each scene for 2.5–3 seconds and the piece drags, so specify transitions and beat speed [07:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=424s).
- **Revise with when and what** [07:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=442s). Audio can be revised by prompt too [06:43](https://www.youtube.com/watch?v=C8dWdic-oK4&t=403s).
- **Slow, taste-judged work gets a human, not a loop** [07:32](https://www.youtube.com/watch?v=C8dWdic-oK4&t=452s). He usually needed 2–3 iterations per video [06:51](https://www.youtube.com/watch?v=C8dWdic-oK4&t=411s). See [[Loop Engineering]].

## The three steps at a glance

| Step | You | Agent | Watch for |
|---|---|---|---|
| 1 Storyboard [01:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=110s) | Review the board (the piece was eventually cut from 18 s to 10 s [02:18](https://www.youtube.com/watch?v=C8dWdic-oK4&t=138s)) | Draws frames with built-in image generation [02:56](https://www.youtube.com/watch?v=C8dWdic-oK4&t=176s) | Skipping it means hours of re-prompting |
| 2 Build [04:13](https://www.youtube.com/watch?v=C8dWdic-oK4&t=253s) | Review the prompt | Writes the prompt, builds, self-checks, renders | 23 min for 15 s [05:58](https://www.youtube.com/watch?v=C8dWdic-oK4&t=358s) |
| 3 Edit [06:26](https://www.youtube.com/watch?v=C8dWdic-oK4&t=386s) | Send specific revisions | Re-edits graphics and audio | Lingering beats; loops |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=C8dWdic-oK4&t=0s) Intro

- He claims the plugin is free and open source, and uses no Higgsfield credits [00:21](https://www.youtube.com/watch?v=C8dWdic-oK4&t=21s) (see Caveats). He says Blender works too [00:32](https://www.youtube.com/watch?v=C8dWdic-oK4&t=32s), but doesn't show it.

### [00:47](https://www.youtube.com/watch?v=C8dWdic-oK4&t=47s) Step 1

- **Prerequisites:** Astra, After Effects and the plugin [00:55](https://www.youtube.com/watch?v=C8dWdic-oK4&t=55s). Invoke it with the Higgsfield use-after-effects command, or ask in plain language [01:14](https://www.youtube.com/watch?v=C8dWdic-oK4&t=74s).
- **The plugin** is a bridge to the app plus bundled skills that teach the model how to use it [01:25](https://www.youtube.com/watch?v=C8dWdic-oK4&t=85s). Astra controls After Effects through scripts and computer use [01:38](https://www.youtube.com/watch?v=C8dWdic-oK4&t=98s). See [[Connecting Claude to External Tools]] and [[Agent Skills]].
- Talking over a visual plan was far easier than editing afterwards [02:20](https://www.youtube.com/watch?v=C8dWdic-oK4&t=140s).
- **His repo** holds the demos with their prompts, plus storyboard, build and revision templates [03:07](https://www.youtube.com/watch?v=C8dWdic-oK4&t=187s).
- His whiteboard piece closely follows a video posted on X by Higgsfield's head designer [03:36](https://www.youtube.com/watch?v=C8dWdic-oK4&t=216s). The result wasn't a one-for-one copy [03:55](https://www.youtube.com/watch?v=C8dWdic-oK4&t=235s).

### [04:05](https://www.youtube.com/watch?v=C8dWdic-oK4&t=245s) Step 2

- His example asks for a 12-second whiteboard animation using the Higgsfield integration [04:27](https://www.youtube.com/watch?v=C8dWdic-oK4&t=267s).
- Non-designers struggle to describe motion. Two fixes: have Codex fold reference videos into the prompt [05:11](https://www.youtube.com/watch?v=C8dWdic-oK4&t=311s), or have it fill his templates from your storyboard [05:16](https://www.youtube.com/watch?v=C8dWdic-oK4&t=316s). It can also research After Effects best practices on the web [05:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=330s).
- Codex checks its work, usually against the storyboard [06:05](https://www.youtube.com/watch?v=C8dWdic-oK4&t=365s), then reviews the render and presents the video with project and asset links [06:14](https://www.youtube.com/watch?v=C8dWdic-oK4&t=374s).
- **Hands-off claim.** He calls the build completely hands-off [06:22](https://www.youtube.com/watch?v=C8dWdic-oK4&t=382s), and says he didn't click a single After Effects button for anything shown [01:46](https://www.youtube.com/watch?v=C8dWdic-oK4&t=106s).

### [06:23](https://www.youtube.com/watch?v=C8dWdic-oK4&t=383s) Step 3

- Every change is a prompt away [06:36](https://www.youtube.com/watch?v=C8dWdic-oK4&t=396s). If you know After Effects, you can edit the project directly in the app instead [06:28](https://www.youtube.com/watch?v=C8dWdic-oK4&t=388s).
- For creative work, keep a human hands-on [07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s). Don't let the storyboard become the autonomous reference for every iteration [07:45](https://www.youtube.com/watch?v=C8dWdic-oK4&t=465s). See [[Permissions and Approval Gates]].

### [07:52](https://www.youtube.com/watch?v=C8dWdic-oK4&t=472s) Final Thoughts

- Remotion and HyperFrames already existed [08:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=484s), but he says After Effects used to demand real expertise [08:11](https://www.youtube.com/watch?v=C8dWdic-oK4&t=491s).

## Caveats & disagreements

### Limits of this video

- **Promotion omitted:** a Higgsfield referral link in the description and a paid-community pitch [08:26](https://www.youtube.com/watch?v=C8dWdic-oK4&t=506s).
- **Plugin claims.** He says it's free and open source [01:06](https://www.youtube.com/watch?v=C8dWdic-oK4&t=66s) and repeats "no credits" [06:00](https://www.youtube.com/watch?v=C8dWdic-oK4&t=360s). Higgsfield's own pages contradict this (see Beyond the source).
- **Not recoverable from the transcript:** full prompt and template text, or how the plugin works inside. The self-check is asserted, not demonstrated. The repo isn't linked in the description.
- **Anecdotal numbers.** The 12-second prompt and the 15-second timed build [05:56](https://www.youtube.com/watch?v=C8dWdic-oK4&t=356s) may be different videos. He doesn't discuss the safety of computer use.

### Conflicts with existing vault notes

- **[[Loop Engineering]].** In [[Chase AI - The Agentic OS Setup for Claude Code]], Chase layers self-improvement loops on top of automations [12:08](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=728s). Here he steers away from loops for slow creative renders [07:32](https://www.youtube.com/watch?v=C8dWdic-oK4&t=452s). *This note's reading:* that's a boundary, not a reversal. Loop when a pass is cheap and an objective check exists.
- **[[Escaping the Default AI Design Look]].** [[AI LABS - Claude Design Skills for Beautiful Sites]] reruns scoring until the score is perfect [05:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=307s). Chase usually needed two or three human-judged iterations [06:51](https://www.youtube.com/watch?v=C8dWdic-oK4&t=411s), and steers away from loops because renders take a long time [07:32](https://www.youtube.com/watch?v=C8dWdic-oK4&t=452s).
- **[[Plan Before Executing]].** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] skips planning for small design tweaks [07:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=442s). Chase storyboards even a short graphic (an 18-second storyboard, later cut to 10), because building it is slow [02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s).
- **[[Verification Before Done]].** The plugin checks its work against the storyboard [06:05](https://www.youtube.com/watch?v=C8dWdic-oK4&t=365s). That's the agent grading itself, the bottom rung of that note's "who judges done" spectrum. Chase makes the human the judge instead.
- **[[Build vs Install Third-Party Skills]].** He installs the plugin in one click [01:06](https://www.youtube.com/watch?v=C8dWdic-oK4&t=66s) with no vetting. The vault says to read every file first.

## Build from this

- [[Storyboard-First AI Video and Motion Graphics]]: storyboard, then an agent-written beat prompt, then human-gated renders.
- [[Generate On-Brand Images from Claude Code]] and [[Generating Images and Video with Claude]]: storyboard frames through an image MCP.
- *Vault ideas:* a pre-render check that flags overlong beats or missing transitions, and a three-pass cap before a human decides. For loops where passes are cheap, see [[Multi-Agent Review and Scoring Loops]] and [[Build Verification into Every Task]].

## Resources mentioned

- Higgsfield AI Motion Designer: https://higgsfield.ai/ai-motion-designer
- Higgsfield MCP, GPT-6 Astra, OpenAI Codex, Adobe After Effects
- His prompt and template repo (not linked); Blender, Remotion, HyperFrames

## Beyond the source

Checked 2026-09-15.

- Higgsfield documents the Motion Designer as a ChatGPT plugin for After Effects and Premiere Pro, invoked with `/use-after-effects`. It can also be triggered from Claude through Higgsfield's MCP. The page shows generated After Effects scripts and doesn't mention computer use. https://higgsfield.ai/ai-motion-designer
- It requires Higgsfield, ChatGPT and After Effects subscriptions, and generations use your normal credits. Open source isn't mentioned. https://higgsfield.ai/blog/ai-motion-designer-after-effects-gpt
- Integrations bill at platform rates, and free generations apply only on higgsfield.ai. A Blender Bridge is listed. https://higgsfield.ai/creator-hub/help-center/integrations/external-integrations-higgsfield
- HyperFrames is HeyGen's Apache-2.0 HTML-to-MP4 framework, with skills that work in Claude Code. https://github.com/heygen-com/hyperframes
- For Claude Code plugins specifically, the docs say plugins can run arbitrary code with your user privileges. https://code.claude.com/docs/en/discover-plugins
- A possibly related repo, a Codex and Claude Code motion-design skill using Higgsfield, doesn't mention this video (unconfirmed link). https://github.com/cth9191/motion-design

## Transcript notes

- "Codeex" → Codex; "Higsfield" → Higgsfield; "GBT6 Astro / Aster" → GPT-6 Astra; "Cloud Code" → Claude Code; "12se secondond" → 12-second.
- "higsfield/use after effects" → `/use-after-effects`. The exact syntax in Codex is *(unclear in captions)*.

## Related

- [[Chase AI]] · [[Higgsfield]] · [[OpenAI Codex]] · [[Claude Code]] · [[Benchmark-Driven Design Critique]] · [[Plan-First Workflow]]
- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: an agent finds an Adobe Premiere connector [19:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1172s).
