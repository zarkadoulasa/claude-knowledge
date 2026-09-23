---
type: technique
goal: Have Claude Code learn your cutting style from past NLE project files, transcribe new footage, and produce style-matched rough cuts and themed shorts with FFmpeg
difficulty: intermediate
time_to_build: "An afternoon to set up; long unattended runs for large footage libraries"
sources: ["[[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]"]
tools: ["[[Claude Code]]", "[[FFmpeg]]"]
tags: [topic/media, topic/claude-code, topic/automation]
---

# Auto-Edit Footage from Your Editing History

## Goal

Turn hours of raw, narrated footage into edits that look like you cut them:

- Claude reads the XML of projects you've already edited to learn your cutting rules.
- It transcribes the new footage.
- It uses FFmpeg to cut full episodes and topic-based shorts.

Built from one commenter's account of editing about 800 GB of travel video this way ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8sni/); [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).

## Use when

- You have a backlog of similar footage and a consistent editing style.
- The footage has narration or dialogue, because transcripts drive most of the smart choices.
- Rough cuts are good enough to start from, and you'll review before publishing.

## Prerequisites

- Claude Code on a strong model. The commenter used Opus 5 ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8sni/)).
- FFmpeg, and a local speech-to-text tool (Claude can install one; see Beyond the source).
- A few projects you've finished, exported as XML. Premiere Pro produces these, per the commenter ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8sni/)).
- Raw footage organised by day in subfolders.
- Plenty of disk space. The output roughly matches the input size.

## Steps

1. **Open Claude Code in the parent folder** that contains the edited projects and the raw footage ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).
2. **Ask it to study your style.** Have it read the project XMLs and write the rules it finds to `STYLE.md`: typical shot length, where you cut, fades, J-cuts, how you open and close. Review and correct that file. *Writing the rules to a file is the vault's addition, so you can check what it learned.*
3. **Transcribe everything.** Have it produce timestamped transcripts for every clip into `transcripts/`. The commenter calls this the step that matters most ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).
4. **Cut two demo episodes first.** Have it use FFmpeg and follow `STYLE.md` ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbh9qmt/)). Watch them all the way through before scaling up.
5. **Let the transcript pick the b-roll.** When the narration mentions something from elsewhere, cut in that footage. The commenter's run did this even across countries, and added J-cuts where the speaker ran long ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbhi545/)).
6. **Scale up.** Run the rest of the backlog in batches, one day or episode per batch, logging each output.
7. **Make themed shorts from the transcripts.** For example: "every food moment across all five countries" or "every time a stranger started a conversation" ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).
8. **Review before posting.** The commenter still plans to check all or most outputs ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfj8mp/)).

## Starter files & prompts

```
footage-root/
  projects/           # past edits exported as XML
  raw/day-01/ ...     # raw clips by day
  STYLE.md            # rules Claude extracted, corrected by you
  transcripts/        # one timestamped transcript per clip
  out/episodes/ out/shorts/
  edit-log.md         # batch → outputs → notes
```

First prompt:

```
Read the project XMLs in ./projects and describe my editing style as concrete rules in STYLE.md
(shot lengths, cut points, transitions, J/L-cuts, openings/closings). Don't edit anything yet.
Then transcribe every clip in ./raw with timestamps into ./transcripts.
```

## Done when

- [ ] `STYLE.md` describes your cutting habits, and you agree with it.
- [ ] Every raw clip has a timestamped transcript.
- [ ] Two demo episodes pass your full watch-through.
- [ ] The batch runs are logged, and each output is reviewed before publishing.

## Pitfalls

- **One anecdote.** The commenter says there's nothing more to their method than what they described ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbj8p4z/)). Test on a small batch first.
- **Plain cuts only.** It worked for a style of fairly simple cuts, fades and J-cuts. Complex grades, effects and titles are beyond FFmpeg rules. For those, the commenter would try the Adobe connector ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbh9qmt/)).
- **Scale.** Hundreds of GB of renders take hours and disk space. Batch the work and keep the originals untouched.
- **Silent footage** gives the transcript nothing to work with. Expect weaker b-roll choices.

## Variations

- **CapCut or other editors.** A commenter who edits in CapCut asked about this ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbff027/)). Any editor that exports a readable project or timeline format (XML, EDL, JSON) can seed `STYLE.md`. *Vault suggestion; not tested in the source.*
- **Transcript-only.** Without past projects, write `STYLE.md` yourself and keep the transcript-driven steps.

## Beyond the source

- **Local transcription.** OpenAI's open-source Whisper runs speech recognition locally, and Claude Code can install and script it (`pip install -U openai-whisper`, which also needs FFmpeg). The thread doesn't say which tool the commenter's run used. <https://github.com/openai/whisper>

## Sources

- [[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]: u/RedditorsGetChills' comments

## Related

- [[Render a Video Entirely in Code with Claude Code]] · [[Generating Images and Video with Claude]] · [[FFmpeg]] · [[Build a Skill from a Successful Run]]
