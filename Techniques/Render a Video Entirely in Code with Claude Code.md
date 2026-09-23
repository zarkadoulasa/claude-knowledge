---
type: technique
goal: Get a finished short video (visuals, music, sound effects and voiceover) from one prompt, with Claude Code writing and rendering everything in Python, no image or video model involved
difficulty: beginner
time_to_build: "10 minutes to 3+ hours of unattended run time per video (reports in the source thread)"
sources: ["[[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]"]
tools: ["[[Claude Code]]", "[[FFmpeg]]"]
tags: [topic/media, topic/claude-code, topic/prompting, topic/models]
---

# Render a Video Entirely in Code with Claude Code

## Goal

Give Claude Code one brief and get back an `.mp4` it wrote and rendered itself:

- frames drawn with numpy and cairo, including 3D scenes via raycasting,
- audio synthesised with numpy and scipy,
- a voiceover from a local TTS model,
- everything assembled with FFmpeg.

The source's run produced a one-minute surreal horror short in about 45 minutes ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/); [tools](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbeygbh/)).

## Use when

- You want stylised video: motion graphics, analog horror, explainers, title sequences, data animations.
- You don't want per-generation media credits, or the content must stay local.
- **Not** when you need photoreal people or footage. Use a media model for that. See [[Generating Images and Video with Claude]].

## Prerequisites

- Claude Code with a strong model. The source used Opus 5.5 at `xhigh` effort ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/)). The OP says simpler versions have worked since the first Fable model ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfwutc/)).
- Python 3 and FFmpeg on the machine, or permission for Claude to install them.
- A fresh, empty project folder. Claude will install packages and download a voice model.
- Usage headroom: 4–14% of a $20 plan's weekly limit per run in the thread ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/); [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbgoj3r/)).

## Steps

1. **Make a scratch project.** `mkdir ~/video-lab && cd ~/video-lab && git init`. Keep it separate from real work, because Claude will be installing things.
2. **Set permissions deliberately.** Allow `pip`, `python` and `ffmpeg`, and deny anything touching other folders. See [[Configure Safe Autonomy Permissions]].
3. **Pick the model and effort.** `/model` for Opus, and `/effort xhigh` for a first attempt. Try `medium` (the Opus 5.5 default) once you know what a good run looks like; see [[Choosing a Claude Model]].
4. **Send one brief** with the five parts the source's prompt had (template below): length, "coded and rendered programmatically", permission to download tools, a theme and tone, and a request for detailed visuals plus programmed audio.
5. **Let it run.** Expect it to install libraries, write a render script, synthesise audio, download a TTS voice (Piper in the source), render frames and mux with FFmpeg ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexf59/)).
6. **Watch the result and give one round of notes.** Name timestamps and scenes ("0:20–0:30 too dark; slow the corridor"). The code is in the repo, so revisions only re-render what changed.
7. **Keep the pipeline.** Ask Claude to split the script into `scenes/`, `audio/` and `render.py`, and to save the brief as `BRIEF.md`. The next video then starts from working code.

## Starter files & prompts

Brief template (vault paraphrase of the source's structure):

```
Create a <60-second> video programmatically — write the code and render it yourself,
using whatever tools you need (you may install/download anything required).
Theme: <subject>, but <tone twist: e.g. surreal, ominous, hinting at something deeper>.
Visuals: detailed and <loud / minimal / retro>, with <any must-have scenes>.
Audio: program the soundtrack, effects and any voiceover yourself.
Output: final MP4 at 1080p, 30 fps, in ./out/. Keep all source code in the repo.
```

Layout Claude tends to converge on (vault suggestion):

```
video-lab/
  BRIEF.md
  render.py          # orchestrates scenes -> frames -> ffmpeg
  scenes/            # one module per scene (numpy raycast, cairo drawings, effects)
  audio/             # synth.py (numpy/scipy), tts.py (Piper), mix.py
  out/final.mp4
```

## Done when

- [ ] `out/final.mp4` plays with synced picture and sound at the requested length.
- [ ] All visuals and audio come from code or local models in the repo, with no paid media API.
- [ ] Re-running `python render.py` reproduces the video.
- [ ] You checked it by eye and ear, and gave at least one round of notes.

## Pitfalls

- **Runs vary a lot.** Similar prompts took 10 minutes, 45 minutes and over 3 hours ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbk0peg/); [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbgoj3r/)). Photoreal or crowded briefs push towards the long end.
- **It can look mechanical.** That was the thread's one critique ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf7nvy/)). Give reference images or a storyboard for more craft. See [[Storyboard-First AI Video and Motion Graphics]].
- **Launch-week usage isn't typical.** The 4% figure came on a day with raised limits (see the Source note).
- **Downloads are code execution.** Keep it in a scratch folder with scoped permissions.
- **Rights.** TTS voices and fonts carry their own licences. Check them before publishing.

## Variations

- **Hybrid.** Generate key stills with an image model, then animate and composite them in code. See [[Generate On-Brand Images from Claude Code]].
- **A bigger toolkit.** OpenMontage offers ready-made agentic video pipelines (Beyond the source in the Source note).
- **Data or explainer videos.** Swap the horror theme for charts that animate from a CSV.

## Sources

- [[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]

## Related

- [[Generating Images and Video with Claude]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Auto-Edit Footage from Your Editing History]] · [[FFmpeg]] · [[Choosing a Claude Model]]
