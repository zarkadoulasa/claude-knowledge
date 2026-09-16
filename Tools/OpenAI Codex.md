---
type: tool
category: AI coding agent / agent harness (OpenAI)
website: https://github.com/openai/codex
sources: ["[[Nate Herk - Every Level of a Claude Second Brain]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Matt Wolfe - Second Brain Wiki with Journal and CRM]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tags: [topic/portability, topic/agents, topic/second-brain, topic/memory, topic/skills, topic/automation, topic/scheduling, topic/media]
---

# OpenAI Codex

## What it is

OpenAI's coding agent. The official description is under *Beyond the source*. In this vault it's the second harness [[Nate Herk]] runs his markdown second brain through, alongside [[Claude Code]]. That makes it the practical test of whether a brain is really tool-agnostic. Newer sources give it two more roles. For [[The Coding Sloth]] it's a day-to-day alternative to Claude Code with roomier usage limits. For [[AI LABS]] it's a second target for skills that are installed once and shared. Two later sources make it the main harness: [[Matt Wolfe]] builds a whole second brain in it, and [[Chase AI]] drives After Effects from it with GPT-6 Astra.

## How sources use it

### [[Nate Herk - Every Level of a Claude Second Brain]]

#### Same brain, different harness

- He mostly talks about Claude Code, but says the approach works with any AI model ([01:42](https://www.youtube.com/watch?v=DTCyvo6cC54&t=102s), [01:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=103s)).
- He uses his second brain with Codex all the time ([01:46](https://www.youtube.com/watch?v=DTCyvo6cC54&t=106s)).
- Different agent harnesses can share it because the brain is only files and folders ([01:50](https://www.youtube.com/watch?v=DTCyvo6cC54&t=110s)).

#### Codex's entry file is AGENTS.md

- A Claude Code brain starts with CLAUDE.md. If you're on Codex or something similar, you start with AGENTS.md instead ([04:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=263s), [04:26](https://www.youtube.com/watch?v=DTCyvo6cC54&t=266s)).
- Either way, the file plays the same router role. See [[CLAUDE.md as a Router]].

#### Why porting takes a little work

- He wants second brains to be tool-agnostic ([11:05](https://www.youtube.com/watch?v=DTCyvo6cC54&t=665s)).
- Two pieces are Claude Code-specific ([11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s)):
  - CLAUDE.md itself.
  - The memory file that Claude Code keeps updated on its own ([11:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=671s)).

#### His steps to make a Claude Code brain work in Codex

| Step | What to do | Where |
|---|---|---|
| 1 | Copy CLAUDE.md into a new file named AGENTS.md | [11:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=676s), [11:21](https://www.youtube.com/watch?v=DTCyvo6cC54&t=681s) |
| 2 | Keep both side by side. In his Herk2 project they're essentially the same file, so Codex reads one and Claude Code reads the other | [11:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=683s), [11:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=689s), [11:30](https://www.youtube.com/watch?v=DTCyvo6cC54&t=690s) |
| 3 | Make sure the memory file exists. Claude Code maintains it through auto memory | [11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s), [11:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=697s) |
| 4 | Tell Codex to look in that memory file whenever it needs memories | [11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s) |

- In his words, the whole bridge comes down to routing ([11:43](https://www.youtube.com/watch?v=DTCyvo6cC54&t=703s)).
- Full playbook: [[Port a Claude Code Brain to Other Agents]]. Concept: [[Tool-Agnostic Context Files]].

#### Avoiding two copies of the router

- His Level 4 example project includes an AGENTS.md that matches its CLAUDE.md ([22:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1373s), [22:55](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1375s)).
- Instead of maintaining both, you can reference AGENTS.md with an `@` inside CLAUDE.md and delete the duplicated text ([22:58](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1378s), [23:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1381s)). The reference effectively injects the file ([23:03](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1383s)).
- Net effect (my reading; he doesn't spell this out): AGENTS.md becomes the single real router file. Codex reads it directly, and Claude Code pulls it in through CLAUDE.md.

### [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]

#### His most-used agent right now

- **First on his list.** When he gets to alternatives to Claude Code, Codex comes first. He calls it OpenAI's version, says he loves it, and says it's the one he's used most ([21:00](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1260s)–[21:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1270s)).
- **The reason is usage limits.** He finds Codex's limits generous and says someone he calls Tibo keeps resetting them, which has let him make a lot of progress ([21:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1270s)–[21:18](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1278s)).
- **The contrast.** His opening complaint is Claude Code's limits on the $20 plan, where a prompt or two can use up the allowance and leave him waiting hours ([00:03](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=3s)–[00:09](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=9s), [00:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=19s)).

#### Other points

- **Mixing models.** In Claude Code he would plan with Opus and implement with Sonnet. He lists Cursor, OpenCode and Codex as tools where you can mix models more freely ([08:02](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=482s)–[08:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=490s)).
- **AGENTS.md.** His gripe is that other agents keep project memory in AGENTS.md and Claude doesn't. His workaround is to import AGENTS.md into CLAUDE.md ([03:21](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=201s)–[03:41](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=221s)). See [[Tool-Agnostic Context Files]].
- **Several subscriptions.** If you pay for Claude Code, Codex, OpenCode and Cursor, he suggests T3 Code, which lets you use all of them from one app ([22:04](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1324s)–[22:13](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1333s)).

### [[AI LABS - The Unlazy Skill for Lazy Agents]]

- **Supported agent.** Unlazy is presented as working with popular agents, Codex included ([01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s)).
- **Codex is the installer's default case.** It needs no change at the "which agent" prompt, because the skill installs into the `.agents` folder Codex already reads ([09:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=567s)–[09:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=570s)). Claude Code has to be selected ([09:34](https://www.youtube.com/watch?v=c47uqR7XB_c&t=574s)), and it only gets a shortcut in `.claude` pointing to that copy ([10:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=605s)–[10:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=614s)).
- **Parallel subagents.** Codex and Claude Code can both run several agents at once. That's why a skill handing out one task at a time wasted hours, and why they edited the skill to dispatch work in parallel ([10:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=648s)–[11:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=665s)).
- Build steps for sharing skills this way: [[Port a Claude Code Brain to Other Agents]] (Extension A).

### [[AI LABS - Claude Design Skills for Beautiful Sites]]

- They demo design skills in Claude Design but say the same skills would work in Claude Code, Codex or any other agent, with the same result ([01:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=63s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s)). No Codex run is shown, so treat this as a claim.

### [[Jay E - The ARMS Framework for a Claude Agentic OS]]

- **Same housekeeping problem.** He had Claude Code turn a speed-up tip he found on X into a cleanup skill, using the skill-creator skill ([06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s)–[06:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=388s)). He suggests trying it if Claude Code, or even Codex, is clogging up your computer and slowing it down ([06:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=392s)–[06:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=396s)).
- **No extra tooling.** With tools like Claude Code or Codex, he says, you don't need extra technical tooling to wire skills into your own dashboard, as long as you know the headless feature. The one he names is `claude -p` ([10:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=616s)–[10:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=624s)).
- **The VPS option.** For routines that never stop, some people install Claude Code on a VPS so that everything lives in one place. He says Codex works there too, and no sync tool is needed ([17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)). He expects OpenAI and Anthropic to offer something like this eventually ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)).

### [[Ras Mic - How AI Agents and Claude Skills Work]]

- **Compaction.** He names Codex alongside Claude Code as harnesses that compact the conversation when the context window fills ([06:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=416s)–[07:01](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=421s)).
- **Harness matters.** He cites a benchmark, without fully endorsing it, that found different output quality from Cursor, Claude Code and Codex ([27:05](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1625s)–[27:15](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1635s)). His takeaway is that the harness, tools and context will matter even more as models improve ([27:27](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1647s)).

### [[Matt Wolfe - Second Brain Wiki with Journal and CRM]]

- **The whole build runs in Codex,** his IDE of choice lately ([08:30](https://www.youtube.com/watch?v=yke4fLQUsh4&t=510s)). The Obsidian vault is added as an existing-folder project ([10:22](https://www.youtube.com/watch?v=yke4fLQUsh4&t=622s)). Given Karpathy's gist, Codex made 51 files, and a follow-up prompt pruned them back to the plan ([11:24](https://www.youtube.com/watch?v=yke4fLQUsh4&t=684s), [11:37](https://www.youtube.com/watch?v=yke4fLQUsh4&t=697s)). See [[Bootstrap an LLM Wiki from the Karpathy Gist]].
- **AGENTS.md holds the rules** for ingest, journal and CRM ([24:12](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1452s)). Edit it by hand in Obsidian or ask Codex to update it ([21:23](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1283s)). See [[Add a Journal and Personal CRM to a Second Brain]].
- **Automations.** A local, hourly automation processes new files in raw on GPT-5.5 at high reasoning, and he advises the strongest model available ([29:27](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1767s), [29:49](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1789s)). With the GitHub plugin attached, he added a commit-and-push to main after each run ([30:58](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1858s), [31:28](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1888s)).
- **Other harnesses.** He says Claude Code or Cowork also works ([32:59](https://www.youtube.com/watch?v=yke4fLQUsh4&t=1979s)); a Claude port needs the AGENTS.md bridge in [[Tool-Agnostic Context Files]].

### [[Chase AI - GPT-6 Astra Motion Design in After Effects]]

- **Creative-app control.** GPT-6 Astra drives After Effects from Codex through Higgsfield's Motion Designer plugin ([00:12](https://www.youtube.com/watch?v=C8dWdic-oK4&t=12s), [01:14](https://www.youtube.com/watch?v=C8dWdic-oK4&t=74s)). [[Higgsfield]] checks his claim that the plugin is free and open source.
- **Built-in image generation** makes storyboards easy; Claude Code would need an MCP such as Higgsfield's ([02:52](https://www.youtube.com/watch?v=C8dWdic-oK4&t=172s)).
- **Self-checking but slow.** Codex writes the build prompt from the storyboard ([04:18](https://www.youtube.com/watch?v=C8dWdic-oK4&t=258s)), then checks, renders and reviews its own output. A 15-second clip took almost 23 minutes ([05:56](https://www.youtube.com/watch?v=C8dWdic-oK4&t=356s), [06:04](https://www.youtube.com/watch?v=C8dWdic-oK4&t=364s)). He keeps a human reviewing iterations ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)). See [[Storyboard-First AI Video and Motion Graphics]].

### [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]

- **Codex appears only in the title.** The narration names Claude Code, and Chisle's tool-output trimming works only there ([04:03](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=243s)). Check each repo's README for Codex support.

## Notes

- **What the video doesn't cover** (Nate Herk). It never shows Codex running, Codex configuration, or any memory feature Codex has. The only guidance is the file-level bridge above.
- **What the newer sources don't cover.** None of them shows Codex configuration. The closest is the Unlazy installer's agent menu, and the design-skills video's Codex claim isn't demonstrated.
- **Usage limits are one person's experience.** The Coding Sloth's preference for Codex rests on his own plans and usage, not a measured comparison.
- **Who owns memory in his setup.** Claude Code is the one keeping memory current, and Codex is pointed at what Claude Code wrote ([11:33](https://www.youtube.com/watch?v=DTCyvo6cC54&t=693s), [11:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=699s)). He doesn't say whether Codex should write to that file.
- **Caption fixes.** "agents.md" → AGENTS.md, "claw.md" → CLAUDE.md, "Herc 2" → Herk2. Newer sources: "CodeX", "Code X" and "Codeex" → Codex; "open AI codex" → OpenAI Codex; "{dot} agents" → `.agents`. From the second-brain, motion-design and repos sources: "Carpathy" → Karpathy, "Higsfield" → Higgsfield, "Chisel" → Chisle, and "Cloud Code" → Claude Code.
- **Configuration is now shown.** Matt Wolfe (project, automation, GitHub plugin) and Chase AI (plugin install) cover app-level setup in their sections above, though neither shows `config.toml`.

## Beyond the source

*Not from the video. Each item was checked on 2026-09-15 at the linked page.*

- **What it is.** Codex CLI is OpenAI's open-source coding agent that runs locally on your computer, in the terminal. You can install it with `npm install -g @openai/codex` or `brew install --cask codex`. <https://github.com/openai/codex>
- **How Codex finds AGENTS.md.** Source: <https://learn.chatgpt.com/docs/agent-configuration/agents-md>. The older link <https://developers.openai.com/codex/guides/agents-md> redirects there.
  - **Global file.** In the Codex home directory (`~/.codex`, or wherever `CODEX_HOME` points), Codex reads `AGENTS.override.md` if it exists. Otherwise it reads `AGENTS.md`.
  - **Project files.** Codex starts at the project root, usually the Git root, and walks down to the current working directory. In each directory it checks `AGENTS.override.md`, then `AGENTS.md`, then any fallback names.
  - **Precedence.** Files closer to the current directory come later in the combined prompt, so they override earlier guidance.
  - **Other filenames.** You can add alternative instruction filenames under `project_doc_fallback_filenames` in `~/.codex/config.toml`.
  - **Size cap.** Codex skips empty files and stops adding files once the combined size reaches `project_doc_max_bytes`, which defaults to 32 KiB.
  - **No `@` imports.** The guide doesn't describe any `@` import syntax. Keep the real content in AGENTS.md and have CLAUDE.md import it, not the other way round. That matches the direction of his Level 4 trick.
- **Implication (my synthesis).** A router that grows large could hit the 32 KiB cap. That's one more reason to keep AGENTS.md lean and send detail out to folders, as the video's routing approach already does.
- **AGENTS.md is an open format.** It's described as "a README for agents" and is supported by many tools besides Codex, including Cursor, Gemini CLI and GitHub Copilot's coding agent. <https://agents.md/>
- **The Claude Code side.** Claude Code reads CLAUDE.md, not AGENTS.md. Its docs recommend a CLAUDE.md that imports `@AGENTS.md`, or a symlink. <https://code.claude.com/docs/en/memory#agents-md>
- **Where the memory file really is.** Claude Code's auto memory lives outside the project, at `~/.claude/projects/<project>/memory/`, with a `MEMORY.md` index, and it stays on that machine.
  - "Tell Codex to read the memory file" means routing Codex to that path.
  - Alternatively, move the memory into the project with Claude Code's `autoMemoryDirectory` setting.

  <https://code.claude.com/docs/en/memory#storage-location>

### Added with the newer sources

*Not from the videos. Checked 2026-09-15.*

- **Where Codex finds skills.** <https://learn.chatgpt.com/docs/build-skills> (redirected from <https://developers.openai.com/codex/skills>)
  - **Folders it scans:** `.agents/skills` in the working directory, in its parent directories, and at the repo root. Also `$HOME/.agents/skills` for personal skills and `/etc/codex/skills` for machine-wide ones.
  - **Symlinks:** Codex follows symlinked skill folders.
  - **Invoking:** type `$` to mention a skill or run `/skills`. Codex can also pick a skill itself when a task matches its description.
  - That's why the Unlazy installer needs no Codex-specific step.
- **Global path mismatch.** The `npx skills` CLI's compatibility table and Unlazy's README give `~/.codex/skills` as Codex's global folder, but OpenAI's current docs name `$HOME/.agents/skills`. After a global install, check that Codex lists the skill. <https://github.com/vercel-labs/skills>, <https://github.com/Leonxlnx/unlazy>
- **Shared format.** Codex skills follow the Agent Skills open standard, which Anthropic originally developed. Claude Code, Hermes Agent and many other agents support it too, so one `SKILL.md` folder can serve all of them. <https://agentskills.io/>
- **Headless Codex.** `codex exec` runs Codex from scripts without the interactive interface. Progress goes to stderr, and only the final message goes to stdout. It's the Codex counterpart to the `claude -p` feature Jay E uses. <https://learn.chatgpt.com/docs/non-interactive-mode>

### Added with the second-brain and motion-design sources

*Not from the videos. Checked 2026-09-15.*

- **Scheduled tasks** (the app's Automations) run on a schedule or on app events, in your local checkout or a background worktree, with default or chosen model and effort. Tasks that need local files need the computer on and the app running, and the docs advise the narrowest access for unattended runs. So Matt's hourly push to main runs only while his machine is up, and unreviewed (my synthesis). <https://learn.chatgpt.com/docs/automations?surface=app>
- **Plugins** can bundle skills, MCP servers, browser extensions and hooks. Install them from the Plugins tab, or with `/plugins` in the CLI; GitHub is an official one. <https://learn.chatgpt.com/docs/plugins>
- **Image generation.** gpt-image-2 has been available in Codex since 2026-04-21. Chase never names the image model, so linking it to his built-in generation is my inference. <https://community.openai.com/t/introducing-gpt-image-2-available-today-in-the-api-and-codex/1379479>

## Related

- **Concepts:** [[Tool-Agnostic Context Files]], [[CLAUDE.md as a Router]], [[Claude Code Auto Memory]], [[Second Brain Levels]]
- **More concepts:** [[Agent Skills]], [[Subagents and Agent Teams]], [[Context Window Management]]
- **Techniques:** [[Port a Claude Code Brain to Other Agents]], [[Build a Level 1 Second Brain]]
- **More techniques:** [[Sync a Workspace to an Always-On Cloud Agent]], [[Route Tasks to the Right Claude Model]]
- **Tools:** [[Claude Code]], [[Hermes Agent]], [[GBrain]]
- **More tools:** [[Unlazy]], [[Claude Design]], [[OpenClaw]], [[Obsidian]], [[Higgsfield]]
- **Second-brain and media builds:** [[LLM Wiki]], [[Routines and Scheduled Tasks]], [[Generating Images and Video with Claude]], [[Bootstrap an LLM Wiki from the Karpathy Gist]], [[Add a Journal and Personal CRM to a Second Brain]], [[Storyboard-First AI Video and Motion Graphics]]
- **People:** [[Nate Herk]]
- **More people:** [[The Coding Sloth]], [[AI LABS]], [[Jay E]], [[Ras Mic]], [[Matt Wolfe]], [[Chase AI]]
- **Source:** [[Nate Herk - Every Level of a Claude Second Brain]]
- **More sources:** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]], [[AI LABS - The Unlazy Skill for Lazy Agents]], [[AI LABS - Claude Design Skills for Beautiful Sites]], [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[Ras Mic - How AI Agents and Claude Skills Work]], [[Matt Wolfe - Second Brain Wiki with Journal and CRM]], [[Chase AI - GPT-6 Astra Motion Design in After Effects]], [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]
- [[Home]]
