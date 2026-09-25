---
type: source
title: Zubair Trabzada - What Jev Actually Is
creator: "[[Zubair Trabzada]]"
channel: "Zubair Trabzada | AI Workshop"
url: https://www.youtube.com/watch?v=fMV6JKkQVfE
video_id: fMV6JKkQVfE
published: 2026-09-21
duration: 9:29
ingested: 2026-09-24
topics: [jev, system-1-models, decision-layer, claude-code, ai-assistant]
tags: [source/youtube, topic/models, topic/claude-code]
---

# Zubair Trabzada - What Jev Actually Is

> **Creator:** [[Zubair Trabzada]] · **Published:** 2026-09-21 · **Length:** 9:29 · [Watch on YouTube](https://www.youtube.com/watch?v=fMV6JKkQVfE)

## TL;DR

A hype-debunk explainer: [[Jev]] is being wildly overhyped online, and the core correction is that you cannot build anything *with* it. Jev is not a large language model — it is a fast, cheap decision layer that, given a situation and a fixed set of choices, returns odds, a yes/no, a pick-one, or a rating, and writes no text. Zubair walks through why that makes it fast and cheap, demos a traffic-control simulation where Jev makes sub-100ms intersection decisions, contrasts it with the slower evaluate-then-generate path of an LLM, shows how to get access and wire in an API key, and closes with a Jarvis-style assistant where Jev replaces a slow Opus 5 call for the quick "which file" routing step. See [[System 1 and System 2 AI Models]] for the underlying pattern.

## Key takeaways

- Jev "decides but does not write" — it is a decision layer, not a generator [01:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=76s).
- You give Jev a situation plus fixed-answer questions and get back percentages, a yes/no, a multiple-choice pick, or a 1–10 rating — never prose [01:43](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=103s).
- The right architecture is LLM-as-builder + Jev-as-decision-layer: [[Claude Code]] or GPT-6 Astra builds the app, and Jev sits in the middle for choice-type decisions [06:08](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=368s).
- Jev's sweet spot is latency-critical decisioning — trading, air or ground traffic control — where milliseconds decide the outcome [04:48](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=288s).
- Access is via TypeSafe.ai (account → playground → API keys), or Vercel / OpenRouter if still waitlisted [06:24](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=384s).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=0s) Jev AI Hype Debunked

- Opens with the hook that people are "lying to you about Jev" and that much of the Jev content on Twitter and YouTube is fake [00:00](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=0s).
- Calls out specific viral claims — people saying they built an app with Jev, and one who claimed to have rebuilt Tesla's self-driving with it — as completely wrong [00:06](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=6s). These are presented as unnamed strawman examples.
- Core correction: you can't build anything with Jev; it is not an LLM, not Claude Code, not GPT-6 Astra — but it is an important piece of AI technology [00:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=16s).
- Sets the goal: explain in simple terms what Jev is, when to use it, and how to use it alongside Claude Code and GPT-6 Astra [00:27](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=27s).
- Promises demos he built with GPT-6 Astra plus a free PDF guide (in the description) with details and example prompts [00:39](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=39s).

### [01:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=76s) What Jev AI Actually Is

- Simplest definition: Jev is the type of AI that decides but does not write [01:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=76s).
- Contrast with ChatGPT / Claude / Claude Code: those take an input, think, and return text or a solution; Jev does not [01:23](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=83s).
- Jev is a decision layer — you give it a situation and it gives you the odds [01:37](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=97s).
- Example: hand it an email plus a few questions with fixed answers, and it returns a percentage for each — no writing, no text output [01:43](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=103s).
- Output forms: yes/no, pick one of several choices, or a rating (e.g. how upset someone is on a 1–10 scale → 5.5, 6.6), plus percentage answers [01:53](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=113s).
- Summary metaphor: a sorter for every answer with a percentage [02:18](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=138s).

### [02:18](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=138s) Why Jev Is So Fast and Cheap

- Because it only sorts and decides, it is fast and cheap [02:22](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=142s).
- Claims Jev is up to 200x faster than many large language models — framed as TypeSafe's own claim ("they claim") [02:25](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=145s).
- His explanation: Jev only has inputs, since there is no output/generation [02:32](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=152s).
- Pricing contrast: traditional models charge per million input tokens *and* per million output tokens; here there is only input, so it is cheap and fast [02:38](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=158s).
- Metaphor: think of it as a traffic cop — cheap, instant, decisive [02:57](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=177s).

### [03:02](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=182s) Jev Traffic Control Demo

- Demo app "Rush Hour Under Control," built with GPT-6 Astra — he stresses again that Jev cannot build anything [03:04](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=184s).
- Setup: a simulated city with buildings, a central park, a sports arena on the left, and a hospital, with traffic arriving from all directions [03:13](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=193s).
- Clicking "Let Jev drive" starts the simulation; Jev's job is to instantly decide which directions to let traffic through so nothing gets stuck [03:31](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=211s).
- Runs in real time; Jev responds in under 100 milliseconds, sometimes 130–150ms [04:00](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=240s).
- Clicking an intersection shows what is happening there; Jev is presented with multiple-choice decisions (let this car in, that car out) and picks in near real time [04:14](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=254s).

### [04:32](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=272s) Jev vs LLMs: The Decision Layer

- The same decision given to an LLM would be evaluated, thought about, generated as output, and only then acted on — a much slower process [04:32](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=272s).
- Those extra milliseconds matter for latency-critical domains — trading, air or ground traffic control — where they are the difference between a jam and smooth flow [04:48](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=288s).
- The "shake things up" feature closes a road, introducing new variables and forcing Jev to instantly re-decide [05:11](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=311s).
- Key distinction: Jev is handed a bounded set of choices to pick from, not asked to evaluate everything and produce an open-ended solution [05:39](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=339s).
- Restates the debunk: things you see "built with Jev" online are wrong, because Jev can't build [05:54](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=354s).
- Correct pattern: use Claude Code or GPT-6 Astra to build the app, and have Jev sit in the middle as the decision layer for choice-type decisions [06:08](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=368s).

### [06:24](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=384s) How to Get Jev Access

- To use Jev *with* (not inside) GPT-6 Astra or Claude Code, head to TypeSafe.ai [06:24](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=384s).
- There used to be a waitlist; now anyone can join and create an account [06:38](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=398s).
- After creating an account, go to the playground and accept the terms [06:44](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=404s).

### [06:51](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=411s) Connect Jev API Keys

- Go to the API keys section and create a new API key [06:51](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=411s).
- Back in GPT-6 Astra or Claude Code, the safest way — especially if non-technical — is to put the API key in an environment variable [06:56](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=416s).
- If environment variables are unfamiliar, he says you can just paste the key into your app and have it connect — not the safest, but fine for local use on your own machine; same for Claude Code [07:10](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=430s).
- Alternative access if still waitlisted: create a Vercel (vercel.com) account and make an API key there, or use OpenRouter [07:36](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=456s). See [[Connecting Claude to External Tools]].

### [08:03](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=483s) Jev + Jarvis AI Assistant Use Case

- Shows his AI second brain, "Jarvis," his personal assistant, now with Jev incorporated [08:01](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=481s).
- Previously, asking Jarvis to pull up a note or a client file used a model like Opus 5 to think through the retrieval and return matches [08:10](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=490s).
- With Jev, that "which file / when to use what" decision is made much faster, so responses are quicker — Jev handles the fast routing step [08:31](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=511s).
- Teases a follow-up video incorporating more Jarvis features with Jev [08:49](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=529s).

### [09:03](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=543s) Final Thoughts

- Wraps up: free resources in the description, asks for comments and questions, like and subscribe, more videos coming [09:04](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=544s).

## Caveats & disagreements

- **"You can't build with Jev" is the framing, stated absolutely.** The corrective is reasonable — Jev isn't generative, so it can't author code or apps — but it is pitched against unnamed strawman hype (a "rebuilt Tesla self-driving with Jev" claim) [00:11](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=11s). The accurate version is narrower: Jev decides among choices, it doesn't generate.
- **"Input-only / no output" is a rhetorical simplification, not literal accounting.** He explains Jev's speed and cost by saying it "only has inputs, no output" [02:32](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=152s). A decision model still computes structured outputs (probabilities); the canonical framing is that output tokens are free/free-form text isn't generated, not that no compute produces an answer.
- **~200x faster is an unverified vendor claim.** He explicitly attributes it to TypeSafe ("they claim") and shows no benchmark [02:25](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=145s). Treat as marketing.
- **~100ms latency is from his own demo only.** The "under 100ms, sometimes 130–150ms" figures come from his simplified simulation, not an independent benchmark [04:00](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=240s).
- **Pasting API keys into an app is a security risk.** He flags it himself as "not the safest way" and limits it to local use [07:10](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=430s). Standard practice is environment variables or secret management, never hardcoding keys — do not paste keys into shared or hosted environments.
- **Speculative product landscape.** GPT-6 Astra and "Opus 5" are treated as available tools in the video's 2026 framing; do not assume they are current shipping products. Claims about Jev's capabilities and pricing come from a promoter with free/paid Skool communities and a lead-magnet PDF — weigh the enthusiasm accordingly.
- **The Jarvis integration is described, not demonstrated end to end** — the concrete build is deferred to a promised follow-up [08:49](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=529s).

## Build from this

- [[Add a Jev Decision Layer to Claude Code]] — the recommended architecture from this video: an LLM (Claude Code / GPT-6 Astra) builds and reasons, while Jev handles the fast "which file / when to use what" routing decision, as in the Jarvis file-routing use case [06:08](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=368s) [08:31](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=511s).

## Resources mentioned

- **TypeSafe.ai** — signup, playground, and API keys for Jev [06:24](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=384s).
- **Vercel (vercel.com)** and **OpenRouter** — alternative routes to Jev access if waitlisted [07:36](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=456s).
- **Free PDF guide** on what Jev is, with example prompts for GPT-6 Astra / Claude Code, linked in the description [00:39](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=39s).
- His **AI Workshop** Skool communities are promoted in the description (a free tier plus a paid "Build AI Employees & Assistants / JARVIS" tier); MCP is referenced only via a description sponsor link, not in the video body.

## Beyond the source

- On Jev's category and the "System 1" naming, see the TypeSafe framing summarized in [[Jev]] and [[System 1 and System 2 AI Models]]; this video uses "System One Model" branding without going into its origins.

## Transcript notes

- The auto-captions render the product name **"Jev" as "Jeff"** throughout (e.g. at 03:09, 03:31, 04:00, 05:52); corrected to **Jev** everywhere in the prose above.
- **"Code X app"** [07:18](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=438s) is most likely **Codex** (OpenAI's coding agent), but it is unclear in the captions.
- **"Opus 5 or something like that"** [08:23](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=503s) — the speaker is vague; treated as an Anthropic Claude Opus model reference.

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Connecting Claude to External Tools]]
