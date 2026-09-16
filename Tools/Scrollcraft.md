---
type: tool
category: Claude Code skill (plugin) for scroll-driven landing pages
website: https://github.com/nateherkai/scroll-craft
sources: ["[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/design, topic/skills, topic/claude-code, topic/media]
---

# Scrollcraft

## What it is

[[Nate Herk]]'s free agent skill for landing pages where scrolling drives what happens on screen ([[Nate Herk - The Scrollcraft Website Design Skill]] [00:54](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=54s)).

- **Get it.** He points to his free Skool community [02:32](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=152s); a public repo also exists (Beyond the source).
- **Install.** Add it as a plugin, or copy its folders into your setup [02:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=177s).
- **Run.** Type "scroll" in [[Claude Code]] and the skill comes up [03:05](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=185s).

## How sources use it

- **[[Nate Herk - The Scrollcraft Website Design Skill]].** Nate redesigns his community's site in the Claude Code desktop app [02:43](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=163s).
  - **Interview:** journey order, the one belief, owned assets, a signature move, and calm vs intense sections ([05:29](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=329s) to [08:08](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=488s)).
  - **Assets.** Your photos first; Kie.ai (API key in the project's environment variables) fills gaps, turning images into stitched video [05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s).
  - **Taste.** Spacing, typography and feel are built in [01:05](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=65s), and the interview keeps sites from looking alike [01:16](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=76s).
  - **Self-check.** After building, it screenshots keyframes along the scroll [08:48](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=528s), yet missed a wrong caption [11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s) and a link that needed fixing.
  - **Iteration.** One section-by-section feedback message produced version 2 [12:19](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=739s). Playbook: [[Build a Scroll-Driven Landing Page]].

## Notes

- **It isn't [[Claude Design]]**, despite the video's title.
- **It isn't Scroll World,** a different third-party skill used in [[Nate Herk - Claude as a One-Person Marketing Team]] [16:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=961s).
- **Read it before installing.** It runs scripts and can call a paid API. See [[Build vs Install Third-Party Skills]].

## Beyond the source

*Checked 2026-09-15 at https://github.com/nateherkai/scroll-craft.*

- **Licence and version:** MIT, v0.3.0 (released 2026-09-04; the video shows an earlier build).
- **Install in Claude Code:** run `/plugin marketplace add nateherkai/scroll-craft`, then `/plugin install nateherk-design`.
- **Other agents:** copy `plugins/nateherk-design/skills/scroll-craft/` into the agent's skills folder.
- **Requirements:** Node 18+, a full ffmpeg build, and playwright-core with Chrome.
- **Cost:** `KIE_AI_API_KEY` is optional. Generated video costs money; your own assets don't.
- **Testing:** the README says the ten example sites were built with [[OpenAI Codex]], and the skill has only been run on Windows.

## Related

[[Build a Scroll-Driven Landing Page]] · [[Build a Distinctive Site with Design Skills]] · [[Escaping the Default AI Design Look]] · [[Generating Images and Video with Claude]] · [[Higgsfield]] · [[Nate Herk]]
