---
type: person
role: "Creator — YouTube channel on startup ideas and AI app building"
links: []
sources: ["[[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]"]
tags: [topic/design, topic/media, topic/claude-code]
---

# Jason Lee

## Who

Creator and host of the source video below, a walkthrough of vibe-coding an animated mobile app. He frames himself as someone building AI-assisted apps and covering startup ideas, and presents the whole build in plain English and voice dictation rather than hand-written code. No further biographical detail is established by the video itself.

## In this vault

- [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]] — creator; vibe-codes a Finch clone ("Chewy") using Claude's Fable 5.1, with assets generated via Higgsfield (GPT Image 2.5 / Seedance 2.5) through an MCP connector inside Claude Code.

## Ideas associated with them

- **Context is king — feed the model screen recordings.** He records the target app (main flow and onboarding) and hands Claude the videos plus a reference image so it infers pages, buttons and features.
- **Claude writes the asset prompts.** The user only describes intent by voice; Claude authors the image/video generation prompts and calls Higgsfield itself.
- **Clone to ~90%, then differentiate.** Recreate a proven app's skeleton, then swap the character and customize — he explicitly warns against copying a live app exactly.
- **Parallelize slow generation with back-end work.** Since video generation takes ~10+ minutes, he has Claude build the React Native + Expo back end while assets render.

## Related

- [[Generating Images and Video with Claude]]
- [[Vibe-Code an Animated Mobile App with Claude]]
