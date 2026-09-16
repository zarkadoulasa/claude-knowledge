---
type: person
role: "Creator — runs the RoboNuggets YouTube channel and community; author of the ARMS framework for an agentic OS"
links: ["https://www.youtube.com/@RoboNuggets", "https://www.skool.com/@robo", "https://www.linkedin.com/in/j-enri/", "https://www.twitter.com/robonuggets"]
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/agentic-os, topic/skills, topic/memory, topic/scheduling, topic/mcp, topic/claude-code, topic/media, topic/design, topic/marketing]
---

# Jay E

## Who

- **Background:** Jay, of the "Jay E | RoboNuggets" channel. Over a decade working with brands and a data science master's; now runs an AI business and a large AI community ([00:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=29s)).
- **Routines setup:** most of his scheduled tasks run on a [[Hermes Agent]] on a cloud computer ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)). [[Syncthing]] keeps it in sync with his Claude Code workspace ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)).

## In this vault

- [[Jay E - The ARMS Framework for a Claude Agentic OS]] — creator.
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] — creator (April 2026, the day after GPT Image 2 launched). Claude Code drives OpenAI's image model through his own skill. He also shows RUBRIC, his AI command centre, where he stores references ([08:27](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=507s)).

## Ideas associated with him

- **ARMS: Applications, Routines, Memory, Skills** ([04:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=241s)), learned bottom-up ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)). → [[Agentic OS]]
- **The dashboard is about 20–30% of the value;** the rest is the workspace underneath ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s)). → [[Build an Agentic OS Dashboard]]
- **Prompt-twice rule:** if you ask Claude for the same task twice, make it a skill ([05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s)).
- **Reference-rich skills.** The strongest skills use reference files ([06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s)); his /robo SKILL.md points Claude to the other files in its folder ([07:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=436s)). → [[Build a Reference-Rich Skill]]
- **Headless runs** with `claude -p`, using a chosen model and effort level ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)).
- **Organise for the agent, not for browsing** ([11:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=702s)). → [[CLAUDE.md as a Router]]
  - A CLAUDE.md router describes his departments ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)).
  - Each department has its own router file ([12:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=763s)).
- **Routines ladder.** → [[Routines and Scheduled Tasks]], [[Sync a Workspace to an Always-On Cloud Agent]]
  - Local routines need the computer on ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)).
  - Next comes an always-on cloud agent ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)).
  - Then Claude Code on a VPS ([17:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1063s)), which he thinks Anthropic and OpenAI will likely offer in the near future, though not yet ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)).
- **Connectors.** → [[Connecting Claude to External Tools]]
  - His search-connectors skill looks for official connectors, then community CLIs, APIs or MCPs ([19:06](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1146s)).
  - He builds missing ones with Matt Van Horn's CLI Printing Press ([20:01](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1201s)).
- **Let Claude write the image prompts.** Connect GPT Image 2 to an agent like Claude so you don't write the prompts yourself ([04:26](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=266s)). His skill calls the model on fal.ai, a model aggregator ([07:00](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=420s)). → [[Generate On-Brand Images from Claude Code]], [[Generating Images and Video with Claude]]
  - Pass the brand book as a reference, converted to JPEG first because the model won't take PDFs ([08:20](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=500s)).
  - A numbered 5x5 grid costs one image; pick a cell and have it regenerated at top quality ([10:09](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=609s), [10:22](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=622s)).
  - To add Kling 3.0, paste fal's LLM docs into the same session and ask Claude to extend the skill ([11:47](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=707s)).
- **Image mockups for UI.** An image reference gets Claude about 50–60% of the way to the UI you want, and it doesn't translate cleanly into HTML ([13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s)). Generate several variants and pick by human taste ([14:26](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=866s)).

## Where sources agree and disagree

- **Agree:** [[Chase AI - The Agentic OS Setup for Claude Code]] also puts most value below the UI ([02:45](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=165s)).
- **Agree (generation):** [[Nate Herk - Claude as a One-Person Marketing Team]] also has Claude do all the prompting ([05:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=316s)). The routes differ: Jay wires a skill to fal.ai, while Nate connects [[Higgsfield]] as a custom connector.
- **Disagree:**
  - Jay built a skill straight from a pasted X post ([06:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=360s)).
  - [[Ras Mic - How AI Agents and Claude Skills Work]] writes skills only after a successful run ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)).

## Beyond the source

- **Cloud routines already exist.** Claude Code's cloud routines run with the machine off, on a fresh clone without local files. — [Claude Code docs: scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks)
- **Profile:** his Skool profile says he founded the ROBO Group and is based in Sydney. — [skool.com/@robo](https://www.skool.com/@robo)
- **CLI Printing Press** (captioned "Matt VH") is Matt Van Horn's tool that generates agent-ready CLIs for apps and APIs. — [GitHub](https://github.com/mvanhorn/cli-printing-press)
- **GPT Image 2 skill** (checked 2026-09-15). The video points to his community for the skill, but it is also public on GitHub:
  - MIT licence; calls fal.ai and needs a `FAL_KEY`.
  - About $0.02, $0.05 or $0.18 per image at low, medium or high quality.
  - Reference images must be public URLs. The video passes local file paths instead.
  - — [robonuggets/gpt-image-2-skill](https://github.com/robonuggets/gpt-image-2-skill)

## Related

- [[Home]]
- [[Chase AI]]
- [[Nate Herk]]
- [[Generate On-Brand Images from Claude Code]]
