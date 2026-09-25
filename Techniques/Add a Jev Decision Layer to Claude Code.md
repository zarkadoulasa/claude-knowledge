---
type: technique
goal: "Use Jev as a fast, cheap decision layer inside Claude Code for model routing and skill selection"
difficulty: intermediate
time_to_build: "an afternoon"
sources: ["[[Jay E - Pairing Jev with Claude Code]]", "[[Zubair Trabzada - What Jev Actually Is]]"]
tools: ["[[Jev]]", "[[Claude Code]]"]
tags: [topic/claude-code, topic/models, topic/skills]
---

# Add a Jev Decision Layer to Claude Code

## Goal

Put [[Jev]] — a fast, cheap [[System 1 and System 2 AI Models|System 1]] decision model — in front of Claude inside [[Claude Code]] so that quick, repetitive routing choices (which model handles a task, which skill to load) are made by Jev in milliseconds instead of by a slow, expensive Claude call. Claude stays the System 2 reasoner that actually does the work; Jev just decides.

## Use when

- You use Claude Code heavily and a lot of tokens/time go to *routing overhead* — Claude deciding which model to use or hunting through a large skill library — rather than the task itself.
- You have an agentic workspace with many skills (Jay E has ~145) where skill lookup is slow. [Jay E, [07:46](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=466s)]
- You want cheaper sessions without hand-picking a model for every prompt. [Jay E, [05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s)]

Don't reach for this for one-off tasks, or when the routing decision is trivial to hardcode — the win comes from *volume* of routing decisions.

## Prerequisites

- Claude Code installed and a workspace you actively use (ideally with a skill library).
- A Jev API key. Get one from TypeSafe (waitlist was removed around the Sept 2026 launch), or reach Jev through OpenRouter or the Vercel AI Gateway. [Jay E, [03:08](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=188s); Zubair, [07:42](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=462s)]
- Basic familiarity with Claude Code skills/slash commands.

## Steps

### 1. Connect Jev to Claude Code

Both creators describe setup as high-level and short — "one prompt away" — and neither shows the exact config file or env-var name, so treat the exact wiring as your own to fill in.

1. Get an API key (TypeSafe console → **API keys** → create; or an OpenRouter / Vercel key). [Zubair, [06:51](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=411s)]
2. Store the key in an **environment variable** rather than pasting it into files — Zubair's recommended, safest route, especially for non-technical users. Pasting the key directly is called out as acceptable only for local use on your own machine. [Zubair, [07:07](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=427s)]
3. Give Claude Code one setup prompt telling it it now has a Jev key and how to call Jev. Jay E ships a free PDF of the exact prompts; the videos don't show the prompt text on screen in full. [Jay E, [03:39](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=219s)]
4. **Confirm access:** ask Claude to verify it can reach Jev before you rely on it. [Jay E, [03:59](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=239s)]

### 2. Build a `/jev on` toggle command

Make a skill/slash command that flips Jev-based routing on or off for a session, so you stay in control of when the decision layer is active. Jay E types `/jev on` (captions render it `/jv on`) and for that whole session Claude uses Jev to pick the model per task. [Jay E, [06:28](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=388s)]

Shape of the command (the video shows the behaviour, not the file):
- `on` → Claude consults Jev before choosing a model / skill for each task.
- `off` → Claude reverts to its session default.

### 3. Use case A — model routing

Let Jev pick the cheapest adequate Claude model per task instead of running Fable/Opus for everything. Rationale: using the top model everywhere drains usage when Sonnet/Haiku would do, and until Jev there was no quick, cheap way to automate the choice. [Jay E, [05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s)]

- Frame each task to Jev as a **Choice** decision over your model menu (e.g. Haiku / Sonnet / Opus / Fable); Jev returns the pick, Claude runs it.
- Jay E's small test: ~12 prompts with Jev routing vs Fable 5.1 every time gave roughly **70% savings**, because 9 of 12 tasks never needed the top model. Example: asked to find a file path, Jev assigned a Haiku helper (cheapest) where the default would have used Opus 5. [Jay E, [05:48](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=348s), [06:49](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=409s)]
- He explicitly warns: **validate on your own work** that the cheaper model's output is still good enough for the tokens saved. [Jay E, [06:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=372s)]

For the standalone version of this idea, see [[Route Tasks to the Right Claude Model]] and [[Choosing a Claude Model]].

### 4. Use case B — skill selection

Turn skill lookup into a Jev **Choice**: the task is the input, your skills are the options, Jev returns the one skill for Claude to load. [Jay E, [07:35](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=455s)]

- Jay E's test: 14 prompts asking Claude to find a specific skill in a ~145-skill workspace. Jev returned the right skill in ~5 seconds total vs ~30 seconds for Opus 5. [Jay E, [07:29](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=449s)]
- Include a sensible catch-all in the option list so unusual tasks don't force a bad pick.

### 5. Apply the same pattern to assistant file-routing

The identical idea works outside Claude Code. Zubair's "Jarvis" second brain previously used a slow model (he says Opus 5) to think through *which* note or client file to retrieve; swapping that fast "which file / when to use what" decision to Jev makes the assistant respond quicker while the LLM still does the reasoning and writing. [Zubair, [08:03](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=483s), [08:31](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=511s)]

The general architecture across both videos: **LLM orchestrates and reasons; Jev sits in the middle as the cheap, fast router.** [Zubair, [06:08](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=368s)]

## Starter files & prompts

The videos don't expose full prompt/config text (Jay E gates his prompts behind a PDF), so build these yourself:

- **Setup prompt** (one-time): tell Claude it now has a Jev API key (in env var `X`), that Jev is a System 1 model returning structured decisions, and how to call it; then have Claude confirm access.
- **`/jev on` skill**: a toggle that, while on, routes model-choice and skill-choice through Jev as **Choice** questions.
- **Routing Choice**: state = the task; options = your Claude model tiers (+ a default); read Jev's selected option.
- **Skill Choice**: state = the task; options = your skill names (+ "none/other"); Claude loads the returned skill.

Jev's mechanics (state + named questions, Choice/Score/Noul) are covered in [[Build a Jev Classification Pipeline]].

## Done when

- [ ] Claude confirms it can reach Jev (step 1 verification passes).
- [ ] `/jev on` / `/jev off` reliably toggles Jev routing for a session.
- [ ] With Jev on, a cheap task (e.g. a file lookup) is routed to Haiku/Sonnet, not the session-default top model.
- [ ] Skill selection returns the correct skill on your own test prompts, noticeably faster than the LLM doing the lookup.
- [ ] You have measured cost/quality on *your* workload, not just trusted the demo numbers.

## Pitfalls

- **Validate output quality yourself.** The savings only count if the cheaper routed model is still good enough; Jay E stresses testing on your own tasks. [Jay E, [06:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=372s)]
- **Savings are workload-specific.** The ~70% figure and 5s-vs-30s come from small, informal tests (12 and 14 prompts) on one person's workspace — not benchmarks. Expect different numbers.
- **Vendor speed/cost claims are marketing.** "20–200× faster, 40–400× cheaper," "24× cheaper than Haiku," "230× cheaper than Fable 5.1" come from TypeSafe's rate card and a viral post, not independent testing. [Jay E, [00:42](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=42s)]
- **Don't hardcode secrets.** Prefer an env var; direct pasting is local-only. [Zubair, [07:07](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=427s)]
- **Model/version names** (Opus 5, Fable 5.1) are as spoken in the videos; treat capitalization/versioning as unverified.

## Variations

- **Model routing as its own workflow** — see [[Route Tasks to the Right Claude Model]] and pair with [[Choosing a Claude Model]] for the human-judgment version of the same decision.
- **Assistant / second-brain routing** — Zubair's Jarvis file-routing case; use Jev for the "which file / when to use what" step in any personal-assistant setup.
- **Skill-library router as a shared service** — expose the skill-selection Choice as a reusable step other agents call.

## Sources

- [[Jay E - Pairing Jev with Claude Code]] — connecting Jev to Claude Code, the `/jev on` toggle, model routing and skill selection (Levels 1). `https://www.youtube.com/watch?v=tTnUcSj-QPA`
- [[Zubair Trabzada - What Jev Actually Is]] — API-key access, env-var setup, and the Jarvis assistant routing case. `https://www.youtube.com/watch?v=fMV6JKkQVfE`

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Build a Jev Classification Pipeline]]
- [[Route Tasks to the Right Claude Model]]
- [[Choosing a Claude Model]]
