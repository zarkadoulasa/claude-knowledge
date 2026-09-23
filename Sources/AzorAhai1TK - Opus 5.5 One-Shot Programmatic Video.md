---
type: source
title: "Opus 5.5 One Shot Video Generation"
creator: "u/AzorAhai1TK"
channel: "r/ClaudeAI (Reddit, Built with Claude flair)"
url: https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/
published: 2026-09-22
ingested: 2026-09-23
topics: [programmatic video, Opus 5.5, numpy raycasting, cairo, Piper TTS, FFmpeg, usage cost, AI video editing, Premiere XML, local scripts for sensitive data]
tags: [source/reddit, topic/media, topic/models, topic/claude-code, topic/prompting, topic/privacy]
---

# AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video

> **Creator:** u/AzorAhai1TK · **Published:** 2026-09-22 (the day Opus 5.5 launched) · **Format:** Reddit post with a 1-minute video + comment thread · [Read the post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/)

This source is a Reddit post, not a video, so there are no timestamps. Provenance links point to the post or to individual comment permalinks. The user pasted the post text; the video itself couldn't be viewed. The publish date is inferred from comment ages ("19h ago" on 2026-09-23) and matches the Opus 5.5 launch.

## TL;DR

On launch day, the OP gave Opus 5.5 in [[Claude Code]] a single prompt: make a one-minute, creepy, surreal "average day at work" video about their small housing company, coded and rendered with any tools it wanted to download. There was no image or video model involved.

Claude wrote Python that:

- drew the frames itself, including a 3D corridor raycast in numpy and everything else drawn with cairo,
- synthesised the sound with numpy and scipy,
- voiced a script it wrote itself with Piper TTS,
- assembled the result with [[FFmpeg]].

It took about 45 minutes at Extra-High (`xhigh`) effort and used about 4% of a $20 plan's weekly limit.

The thread adds two useful workflows:

- A commenter had Claude learn their editing style from Premiere Pro XML project files and transcripts, then cut about 800 GB of travel footage with FFmpeg. See [[Auto-Edit Footage from Your Editing History]].
- Another had Claude write a local Python script to check sensitive payroll PDFs instead of uploading them.

## Key takeaways

- **Claude can make video with no media model at all.** Code draws every frame and sound, so there's no generation credit to pay and the render stays on your machine ([OP on tools](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbeygbh/); [OP on method](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexf59/)). See [[Render a Video Entirely in Code with Claude Code]].
- **It's an agentic job, not a chat reply.** It ran in Claude Code, which installed its own tools, wrote the script, downloaded a TTS voice and rendered ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfq62e/); [OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfwutc/)).
- **Cost varies a lot with the brief.** The OP's run took 45 minutes and about 4% of the weekly limit on the $20 plan ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/)). A commenter reusing the prompt with a heavier theme needed over 3 hours and about 14% ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbgoj3r/)). A filmmaker got a rendered short in about 10 minutes ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbk0peg/)).
- **The prompt pattern carries over.** State the length, say "coded and rendered programmatically", grant permission to download tools, name the theme and tone, and ask for detailed visuals and programmed audio. Others reused it for different subjects with similar results ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbhrlpa/)).
- **This isn't new to 5.5.** The OP says Claude could do simpler versions of this since the first Fable model ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfwutc/)).
- **Escalate your asks.** One commenter's demo prep grew from a speech into hero images, then an interactive web animation, then a short film. Their advice: keep raising the ambition instead of settling for what a human could make in two weeks ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf90lp/)).

## Notes by section

### The run (post and OP replies)

- **Prompt.** About 90 words. The OP pasted it in full in the post ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/); [OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf7z4x/)). In outline it asks for:
  - a 1-minute video made programmatically, with freedom to download any tools,
  - a theme: an ordinary workday at the OP's housing company, turned creepy and surreal and hinting at horror,
  - loud, detailed visuals,
  - audio programmed however Claude sees fit.
- **Tools used.** FFmpeg, numpy, scipy, cairo and Piper TTS ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbeygbh/)).
- **How the visuals were made.** The corridor scene is a 3D raycaster written in numpy. Everything else was drawn with cairo, with effects added on top ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexf59/)). A five-year numpy user was surprised numpy could do that ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexzbd/)).
- **How the audio was made.** Sound effects come from numpy and scipy. Claude wrote its own dialogue script and downloaded a TTS model to voice it ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexf59/); [OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfwutc/)).
- **Setup.** Claude Code, not the desktop app, on Opus 5.5 at Extra-High effort ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfq62e/); [post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/)).
- **Is it really one prompt?** A sceptic asked for proof ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf1icp/)). The OP posted a scroll through the Claude Code terminal ([OP](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfbbm9/)), and the sceptic accepted it ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbflolp/)).

### Reception

- **Criticism.** The only critique in the thread: the result feels a bit mechanical ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf7nvy/)).
- **Next steps suggested.**
  - A filmmaker thinks proper scripting plus visual references made with another model could make it genuinely good ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbk0peg/)).
  - Another commenter points to OpenMontage as a richer toolkit ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8ten/)).
- **Where the render ran.** One commenter asked why the OP didn't have Claude hand over the files and render locally ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbjsxyt/)). In Claude Code, the render already runs on your own machine. See Beyond the source.

### Workflow: editing footage in your own style (u/RedditorsGetChills)

- **What happened.** They opened Claude in the parent folder of their Premiere Pro projects. Claude offered to read the project XML files to learn their editing style, then cut two 25–30 minute demo videos, and afterwards the rest of a three-month trip. That was about 800 GB, on Opus 5 ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8sni/); [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).
- **Tools.** It cut with FFmpeg, not the Adobe connector, following cut rules it took from the XMLs ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbh9qmt/)).
- **Transcripts do the heavy lifting.** It transcribed all the narration. It then used the transcripts to:
  - add fades and J-cuts where the editor usually puts them,
  - cut in footage of whatever was being talked about, even from a different day or country,
  - build themed shorts, such as food across five countries ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbhi545/); [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).
- **Checking.** They still intend to review most of the output before posting.
- **Nothing more to share.** They say there's no further secret: Claude being curious plus a "let it cook" attitude ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbj8p4z/)).

Built out in [[Auto-Edit Footage from Your Editing History]].

### Workflow: check sensitive data with a local script (u/BloodSteyn)

About 400 employees had been migrated to a new payroll system, with bank details in PDFs in two different formats. Rather than upload personal data, they had Claude write a Python script that ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbj2tfr/)):

- matched employee codes across the two systems,
- inferred each bank from the account-number prefix,
- produced per-organisation spreadsheets with a linked summary sheet.

The script can be rerun for future checks.

The lesson: **for sensitive data, have Claude write code you run, instead of pasting the data into the chat.** See [[Permissions and Approval Gates]].

## Caveats & disagreements

- **One run is one data point.** Run time and usage swung from 10 minutes to 3+ hours, and from 4% to 14% of the weekly limit, across the thread.
- **The 4% figure is from launch day.** Opus 5.5 launched with raised five-hour limits and a rate-limit reset for subscribers (Beyond the source), so it may not hold for you.
- **Code-rendered vs generated video.** Code-drawn frames are stylised, which suits analog-horror and motion-graphic looks, and one commenter found it mechanical. Photoreal footage still needs an image or video model. See [[Generating Images and Video with Claude]].
- **Style-learning is one person's anecdote.** It isn't reproducible from the thread. The commenter says they have no further details to give.
- **Security.** Letting an agent download and run arbitrary tools is a real permission grant. Run it in a scratch project. See [[Configure Safe Autonomy Permissions]].

## Build from this

- **A code-rendered short** from one prompt → [[Render a Video Entirely in Code with Claude Code]]
- **Style-matched rough cuts** from your own project files and transcripts → [[Auto-Edit Footage from Your Editing History]]
- **A rerunnable local checker for sensitive documents:** Claude writes the script, and the data never leaves your machine.

## Resources mentioned

- FFmpeg, numpy, scipy, cairo (pycairo), Piper TTS
- OpenMontage: <https://github.com/calesthio/OpenMontage>
- Two Minute Papers (the "what a time to be alive" meme): <https://www.youtube.com/channel/UCbfYPyITQ-7l4upoX8nvctg>

## Beyond the source

*Checked 2026-09-23.*

- **Opus 5.5 launched 2026-09-22.**
  - Its default effort is medium. Anthropic's charts run low, medium, high, xhigh and max, so the OP's "Extra-High" is `xhigh`, two steps above the default.
  - The launch also raised five-hour usage limits on Pro, Max, Team and seat-based Enterprise plans, and gave subscription users a rate-limit reset.
  - <https://www.anthropic.com/news/claude-opus-5-5>
- **Piper TTS** is a fast, local neural text-to-speech engine, installed with `pip install piper-tts`. The original `rhasspy/piper` repo is archived; development continues at `OHF-Voice/piper1-gpl`. <https://github.com/OHF-Voice/piper1-gpl>
- **OpenMontage** calls itself an open-source agentic video production system for coding assistants. It has 12 pipelines, 100+ tools and 700+ skill and knowledge files, and is AGPLv3. <https://github.com/calesthio/OpenMontage>
- **Claude Code runs commands on your machine.** Tool installs and FFmpeg renders happen locally, so the files are already yours. That answers the "why not render locally" question. <https://code.claude.com/docs/en/overview>

## Transcript notes

- "higginsfield" in a comment means [[Higgsfield]].
- "Extra-High" is the app's label for the `xhigh` effort level.
- "Ffmpeg" / "ffmpeg" means FFmpeg; "piper tts" means Piper TTS.
- The OP is u/AzorAhai1TK. They answer as the author ("I pasted my exact prompt in the post"). The company name in the prompt is left out of the notes.

## Related

- **Concepts:** [[Generating Images and Video with Claude]] · [[Choosing a Claude Model]] · [[Permissions and Approval Gates]]
- **Techniques:** [[Render a Video Entirely in Code with Claude Code]] · [[Auto-Edit Footage from Your Editing History]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Configure Safe Autonomy Permissions]]
- **Tools:** [[FFmpeg]] · [[Claude Code]] · [[Higgsfield]]
