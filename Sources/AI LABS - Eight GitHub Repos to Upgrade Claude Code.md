---
type: source
title: "Insane GitHub Repos That 10x Your Codex And Claude Code Setup"
creator: "[[AI LABS]]"
channel: "AI LABS"
url: https://www.youtube.com/watch?v=Ua0APTMVcb8
video_id: Ua0APTMVcb8
published: 2026-09-14
duration: "12:39"
ingested: 2026-09-15
topics: [runtime verification, three-way verdicts, held-out acceptance checks, self-interview planning, skill evals, token reduction, tool-output compression, design skill registry, MCP vs CLI, iOS design skills, lint rules for AI code, Three.js models from images]
tags: [source/youtube, topic/claude-code, topic/skills, topic/verification, topic/planning, topic/context, topic/mcp, topic/design, topic/loops]
---

# AI LABS - Eight GitHub Repos to Upgrade Claude Code

> **Creator:** [[AI LABS]] · **Published:** 2026-09-14 · **Length:** 12:39 · [Watch on YouTube](https://www.youtube.com/watch?v=Ua0APTMVcb8)

## TL;DR

[[AI LABS]] run through eight free community repos, each fixing one thing [[Claude Code]] (and [[OpenAI Codex]]) handles badly alone. Three ideas outlast the list:

1. Loading isn't working: check runtime behaviour, and treat "couldn't tell" as its own verdict (Reticle).
2. Hide the acceptance checks from the builder (Ouroboros).
3. After a model update, test whether each skill still improves results (Caliper).

The rest cover terse output, on-demand design skills, native iOS UI, anti-slop lint rules and 3D models from a photo. Nothing is measured, and several claims differ from the repos' docs (Beyond the source).

## Key takeaways

- **Loading and looking right isn't working.** Agents stop at those two checks while failures hide behind them [01:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=100s). Let the checker see inside the running app, with a third verdict for "not enough information" [02:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=146s). See [[Verification Before Done]].
- **Hide the grading from the builder.** The build instructions never say how checks run or what they expect [07:58](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=478s). Failures come back as targeted fixes, and every check reruns [08:02](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=482s).
- **Ask only about behaviour-changing decisions.** The agent fills small gaps itself if they're reversible and in scope, and logs them as assumptions [07:29](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=449s). See [[Plan Before Executing]].
- **Skills go stale.** A newer model may already do what a skill says, leaving only its token cost [09:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=580s). Cost and usage can't show value; with/without runs can [10:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=601s). See [[Agent Skills]] and [[Skill Improvement Loop]].
- **Look skills up instead of hoarding them.** A registry loads the design skill that fits the brief [05:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=337s). They chose MCP because its tools stay visible; a CLI must be named in the prompt or project instructions [05:15](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=315s). See [[Connecting Claude to External Tools]].
- **Output affects context too.** Terse replies and hook-trimmed tool output save tokens [04:11](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=251s). See [[Context Window Management]].
- **Put newer platform APIs in a skill.** Agents fake Liquid Glass with blur and call it real [08:45](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=525s); a skill with Apple's real patterns gets much closer to native [09:27](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=567s).

## The eight repos

| Repo | Gap it patches | How it works (as narrated) | When |
|---|---|---|---|
| **img2threejs** | 3D visuals need 3D software | Rebuilds an object from an image as Three.js code in stages, checking against the image | [00:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=35s) |
| **Reticle** | Agents call unfinished apps done | Watches the running app; verdict per check: worked / didn't / not enough information | [01:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=115s) |
| **Chisle** | Long replies, noisy tool output | Plugin (four skills, three hooks): terse prose, no unneeded code, trimmed tool output | [03:14](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=194s) |
| **UI Skills** | Too many design skills | Multi-author library the agent searches over MCP or CLI | [04:59](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=299s) |
| **Ouroboros** | Agent silently decides unstated details | Self-interview, reviewed plan, build, hidden checks, fix and recheck | [06:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=415s) |
| **fwc-swiftui-skills** | Fake Liquid Glass, no iPhone Duo layouts | SwiftUI skills for Liquid Glass and iPhone Duo | [08:51](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=531s) |
| **Caliper** | Unknown whether a skill still helps | With/without evals for skills or MCP servers, weighed against tokens | [10:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=605s) |
| **anti-slop** | Bad patterns agents write | Author's lint rules, findings sent to the agent | [11:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=695s) |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=0s) Intro

- They kept eight repos that held up in their own work, and say two are trending on GitHub [00:09](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=9s). One targets the scroll-style product landing pages now common [00:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=13s) (compare [[Scrollcraft]]).

### [00:36](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=36s) img2threejs

- Because the model is plain code, it can sit on a landing page, animate and respond to visitors [00:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=40s). The agent changes colours and lighting when asked [00:52](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=52s).
- To use it, give the agent the image and name the skill [01:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=65s). It builds in stages and fixes mismatches with the image before adding detail [01:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=73s).
- Expect a long, token-heavy run and a rough first result; iterate on specific parts [01:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=83s). See [[Build a Scroll-Driven Landing Page]].

### [01:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=97s) Reticle

- They argue hidden failures only surface if the agent can see more of what happens in the browser [01:47](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=107s). Reticle lets the agent follow the app's internals while it runs [02:00](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=120s).
- They say that once it's installed, the agent uses it after every build even if you don't ask [02:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=125s), and operates the app the way you would [02:12](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=132s).
- Failures come with explanations the agent can act on [02:31](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=151s). They also describe a corner pop-up that keeps a history of past checks [02:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=157s). See Beyond the source.

### [02:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=175s) Chisle

- End-of-task summaries have become long and oddly laid out, especially in Claude models [03:00](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=180s).
- On the author's own test, a search-box change fell from about 1,500 answer tokens to about 600 [03:29](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=209s), and total tokens came in below caveman and ponytail [03:41](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=221s).
- Hooks, which fire automatically at set points [03:52](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=232s), run at session start, on each prompt and after each tool call [03:56](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=236s).
- Replies come in a fixed order: what it did overall, the key changes, then what it skipped [04:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=277s).

### [04:44](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=284s) UI Skills

- Matching a design skill to your style takes real effort [04:53](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=293s).
- Once connected, the MCP shows in the agent's tools [05:27](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=327s). Asked to use it, the agent narrows to relevant skills and reads their instructions while building [05:41](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=341s). See [[Build a Distinctive Site with Design Skills]].

### [06:52](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=412s) Ouroboros

- Unspecified details get decided by the agent [06:53](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=413s). Setup wires a terminal command into your agent [07:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=425s).
- It writes questions about your request and answers them from your description and the project [07:20](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=440s).
- The answers become a plan of what the finished app must do. The plan is reviewed and fixed, and building waits until it passes [07:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=466s).
- A dashboard shows the work live [08:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=493s). If progress stalls or attempts run out, it tells you why [08:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=497s). See [[Loop Engineering]] and [[Plan-First Workflow]].

### [08:22](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=502s) SwiftUI Skills

- Few design skills target iPhone apps [08:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=506s), and agents miss Apple's functional changes [08:47](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=527s).
- The Liquid Glass skill covers iOS 26's built-in buttons and menus and common mistakes [09:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=544s). The iPhone Duo skill covers layouts for the Duo's wider size [09:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=553s). Install the one you need and tell the agent to follow it [09:22](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=562s).

### [09:34](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=574s) Caliper

- Claude Code's new `/skill-doctor` shows each skill's token cost and which skills go unused [09:57](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=597s).
- Caliper ships two skills. grill-skill interviews you so the tests match what you meant [10:25](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=625s); evaluate-skill writes and runs the evals [10:31](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=631s).
- An eval is a prompt plus a description of the expected result. Evals are saved next to the skill, and runs are logged in `.caliper` [10:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=637s).
- evaluate-skill runs first; grill-skill takes over if it gets stuck [10:59](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=659s). Prompts run with and without the skill [11:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=665s), and the report shows where it's reliable [11:18](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=678s).
- It can compare MCP servers and other instructions the same way [11:27](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=687s). See [[Audit Skill Descriptions and Triggers]].

### [11:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=697s) anti-slop

- It reports specific mistakes to the agent, so nobody has to read the code [11:43](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=703s). Some rules catch wasted work that slows the app; others encode the author's style [11:53](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=713s).
- They say the agent then checks every task [12:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=724s), and you can ask for a final review [12:10](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=730s).

## Caveats & disagreements

**About the video**

- **Promotion omitted:** a Manufact sponsor read (05:52–06:49), subscribe requests, a paid-community pitch and a Super Thanks request.
- **Nothing measured.** The only figures come from Chisle's author [03:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=206s). [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] records JetBrains measuring caveman at about 8.5% savings, against a claimed 65%.
- **No security warning.** All eight are unreviewed third-party installs, and some run code in your session (Chisle's hooks). UI Skills also pulls other authors' instructions in at runtime [05:41](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=341s).

**Conflicts with existing vault notes (both sides)**

| Vault note | Vault says | This video | Reading |
|---|---|---|---|
| [[Build Verification into Every Task]] | Screenshots plus Chrome DevTools ([[Nate Herk - 32 Tricks to Level Up Claude Code]] [04:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=247s)) | Runtime internals [02:00](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=120s) | They complement each other: internals catch failures a screenshot can't show |
| [[Evidence-Gated Completion Ledger]] | The agent writes its own checks ([[AI LABS - The Unlazy Skill for Lazy Agents]]) | Checks are withheld from the builder [07:58](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=478s) | Add held-out checks as a variation |
| [[Plan Before Executing]] | Ask the user until 95% confident (Nate [03:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=226s)) | Answer its own questions; escalate only behaviour changes [07:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=455s) | Different rule for asking vs assuming; choose by stakes |
| [[Agent Skills]] | Use `/skill-doctor` cost and usage figures for cleanup | Cost says nothing about value [10:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=601s) | A refinement: run both checks |
| [[Build vs Install Third-Party Skills]] | Read others' skills before installing; Ras Mic won't install them at all ([[Ras Mic - How AI Agents and Claude Skills Work]] [12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)) | Installs without review; fetches skills at runtime [05:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=337s) | The vault's caution stands: keep local copies of skills you've checked |
| [[Claude Code]] | Behaviour that must always happen belongs in hooks | Says installing the skill makes linting run on every task [12:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=724s) | Only a hook guarantees it; Chisle uses hooks |

## Build from this

- **Runtime check:** [[Build Verification into Every Task]].
- **Held-out checks** in a folder the builder can't read: [[Evidence-Gated Completion Ledger]], [[Multi-Agent Review and Scoring Loops]], [[Permissions and Approval Gates]].
- **Skill audit per model release:** `/skill-doctor`, then with/without evals ([[Skill Improvement Loop]]).
- **Token trial:** Chisle on vs off on your tasks; its README caveats are in [[Context Window Management]].

*Vault starter content* (not from the video):

```markdown
## Definition of done
- Every feature gets a runtime check of its main flow: PASS, FAIL or UNKNOWN.
  UNKNOWN is not done. Add logging or a probe and re-run.
- Acceptance checks live in checks/. Builder subagents never read or edit it;
  a separate evaluator runs them and reports failing requirement IDs only.
- Before planning, list open questions. Settle small, reversible, in-scope ones
  yourself and log them in plans/assumptions.md. Ask me about behaviour changes.
- Lint changed files before reporting; fix findings rather than suppressing them.
```

## Resources mentioned

- The eight repos (links under Beyond the source); caveman and ponytail [03:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=217s).

## Beyond the source

*Not in the video. Verified 2026-09-15.*

| Repo | Verified details |
|---|---|
| [img2threejs](https://github.com/img2threejs/img2threejs) | Apache-2.0, about 16k stars; Claude Code, Codex, OpenCode. Eight gated passes with Python validation and visual review; outputs TypeScript. One image can't show hidden sides |
| [Reticle](https://github.com/reticlehq/reticle) | `npx @reticlehq/server init` adds a dev-only SDK and MCP server. Pass / fail / couldn't tell, with file:line. React, Vue, Svelte, Next.js, Electron, Tauri. SDK Apache-2.0; server FSL-1.1-ALv2 |
| [Chisle](https://github.com/JayPokale/Chisle) | Jay Pokale, MIT. `claude plugin install chisle@chisle`. Skills chisle, chisle-audit, chisle-help, chisle-review; SessionStart, UserPromptSubmit and PostToolUse hooks. 20-task author benchmark: 52% of baseline output tokens, one task at 173%. Tool-output trimming in Claude Code and Pi only |
| [UI Skills](https://github.com/ibelick/ui-skills) | By ibelick, MIT. MCP endpoint `https://www.ui-skills.com/mcp` with tools `list_skills` and `get_skill`; CLI `npx ui-skills list` / `get`. Includes third-party publisher skills ([PR #70](https://github.com/ibelick/ui-skills/pull/70), merged 2026-09-13) |
| [Ouroboros](https://github.com/Q00/ouroboros) | MIT. `claude plugin marketplace add Q00/ouroboros`, then `claude plugin install ouroboros@ouroboros`. Interview → locked Seed spec → run → three-stage evaluation (mechanical, semantic, multi-model) → evolve. Ambiguity gate at 0.2; stagnation detection; 30-generation cap |
| [fwc-swiftui-skills](https://github.com/FloWritesCode/fwc-swiftui-skills) | MIT. `npx skills add FloWritesCode/fwc-swiftui-skills`. Liquid Glass needs Xcode with the iOS 26 SDK |
| [Caliper](https://github.com/edonadei/caliper) | MIT. `pipx install caliper-eval`. YAML tasks judged by `expect` (LLM), `assert` (Python) or `activates`; `--ablate <skill>` for the without run; `--k` default 3. MCP blocks on Claude Code, Codex, Hermes |
| [anti-slop](https://github.com/dmmulroy/anti-slop) | Dillon Mulroy, MIT. Oxlint plugin: 20 generic plus 5 Effect rules. `install-anti-slop` copies them into your repo to vendor and edit |

- **`/skill-doctor`** (v2.1.252+) reports each skill's context cost and how often it's invoked, not output quality. For with-and-without testing, the docs point to the skill-creator plugin: https://code.claude.com/docs/en/skills
- **Narration vs the repos** (checked 2026-09-15; links in the table):
  - *img2threejs:* the video warns of heavy token use [01:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=83s); the README calls it token-efficient, with Python scripts doing the mechanical checks.
  - *Reticle:* the docs describe reading the app from inside (network, store, console, DOM), not browser automation as at [02:12](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=132s). The [site](https://www.reticle.sh/) mentions kept run history and automatic re-checks of already-verified flows, and an [issue](https://github.com/reticlehq/reticle/issues/783) an in-app HUD overlay, so the pop-up, history and auto-run claims [02:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=157s) roughly hold; new checks start with `/reticle` or a request.
  - *Chisle:* its ruleset adds about 1.6k tokens at session start, plus short per-turn reminders.
  - *Ouroboros:* the self-answering interview [07:20](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=440s) is closest to `ooo auto`; `ooo interview` questions you instead.
  - *anti-slop:* the README doesn't back the "every task" claim [12:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=724s); it ships only an install skill.
- **iPhone Duo**, "just launched" in the video [09:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=557s): Apple's first foldable iPhone, announced 2026-09-09 and shipping 2026-10-23. https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/

## Transcript notes

| Caption | Corrected |
|---|---|
| "image to 3js" | img2threejs |
| "Reticule" | Reticle |
| "Chisel" | Chisle |
| "Oroboros", "Uura Borus" | Ouroboros |
| "Swift UI skills" | fwc-swiftui-skills |
| "skill doctor command" | `/skill-doctor` |
| "{dot} Caliper" | `.caliper` |
| "or add without having to use" (01:00) | a word is missing, probably "animation" *(unclear in captions)* |

## Related

- **Concepts:** [[Verification Before Done]] · [[Plan Before Executing]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Context Window Management]] · [[Connecting Claude to External Tools]] · [[Loop Engineering]]
- **Techniques:** [[Build Verification into Every Task]] · [[Evidence-Gated Completion Ledger]] · [[Skill Improvement Loop]] · [[Audit Skill Descriptions and Triggers]] · [[Plan-First Workflow]] · [[Context Hygiene Routine]] · [[Build a Distinctive Site with Design Skills]] · [[Build a Scroll-Driven Landing Page]] · [[Build Product UI from a Component Registry]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]] · [[Scrollcraft]]
- **Sources:** [[AI LABS - The Unlazy Skill for Lazy Agents]] · [[AI LABS - Types of Claude Loops Explained]] · [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] · [[Nate Herk - Build Skills Instead of Agents]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]
- **People:** [[AI LABS]] · [[Nate Herk]] · [[Ras Mic]]
