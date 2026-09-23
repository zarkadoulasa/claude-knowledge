---
type: tool
category: Open-source command-line tool for recording, converting, cutting and encoding audio and video
website: https://ffmpeg.org
sources: ["[[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]"]
tags: [topic/media, topic/claude-code]
---

# FFmpeg

## What it is

FFmpeg is the standard free command-line toolkit for working with audio and video: converting formats, cutting, concatenating, mixing and encoding. Coding agents reach for it by default, because Claude can drive the whole thing through shell commands without any connector.

## How sources use it

- [[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]:
  - **Final assembly.** It assembled the frames and audio Claude generated in Python (numpy, scipy, cairo, Piper TTS) into a one-minute video ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbeygbh/)). See [[Render a Video Entirely in Code with Claude Code]].
  - **Cutting real footage.** A commenter's style-matched travel edits were cut with FFmpeg rather than through the Adobe connector ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbh9qmt/)). See [[Auto-Edit Footage from Your Editing History]].

## Notes

- Install it with `brew install ffmpeg` on macOS or `winget install Gyan.FFmpeg` on Windows. Or let Claude Code install it in a scratch project, with scoped permissions.
- **Code-rendered media vs generative models.** FFmpeg-based pipelines cost no generation credits and run locally, but only produce what code or your own footage can supply. For generated imagery see [[Generating Images and Video with Claude]] and [[Higgsfield]].

## Related

- [[Generating Images and Video with Claude]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Claude Code]]
