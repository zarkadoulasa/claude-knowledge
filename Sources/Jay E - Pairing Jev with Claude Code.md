---
type: source
title: Jev will 10x your Claude Code (Here's How)
creator: "[[Jay E]]"
channel: Jay E | RoboNuggets
url: https://www.youtube.com/watch?v=tTnUcSj-QPA
video_id: tTnUcSj-QPA
published: 2026-09-21
duration: 11:46
ingested: 2026-09-24
topics: [jev, system-1-models, model-routing, skill-selection, classification]
tags: [source/youtube, topic/claude-code, topic/models, topic/skills]
---

# Jev will 10x your Claude Code (Here's How)

> **Creator:** [[Jay E]] · **Published:** 2026-09-21 · **Length:** 11:46 · [Watch on YouTube](https://www.youtube.com/watch?v=tTnUcSj-QPA)

## TL;DR

A launch-day explainer for [[Jev]], a "System 1" model from TypeSafe that only returns structured decisions (true/false, a menu pick, or a score) and so is pitched as far faster and cheaper than chat LLMs. Jay E's thesis: don't replace Claude with Jev — pair them, using a fast System 1 decision layer (Jev) alongside a System 2 reasoning model (Claude). See [[System 1 and System 2 AI Models]]. He walks three "levels": Level 1 wires Jev into Claude Code for model routing and faster skill selection; Level 2 uses it for high-volume business classification; Level 3 builds new apps that cheap decision inference makes viable (semantic media search, a page-declutter extension).

## Key takeaways

- **Pair System 1 with System 2.** The single takeaway is to combine a fast decision model (Jev) with a text/reasoning model (Claude), not to choose one over the other ([02:45](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=165s)).
- **Jev only answers in three shapes** — binary true/false, a pick from a menu, or a score on a scale — which is what makes it fast and cheap ([01:21](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=81s)).
- **Model routing inside Claude Code:** let Jev pick the cheapest adequate Claude model per task instead of defaulting to Opus or Fable ([05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s)).
- **Faster skill selection:** feed the task as input and your skills as options, and Jev returns the skill for Claude to load ([07:35](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=455s)).
- **High-volume classification is where it shines** — anything received in bulk with a business question attached (leads, fraud, spam, refunds, churn) ([09:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=545s)).
- **Ship a toggle skill** (`/jev on`) so you can turn Jev routing on and off per session ([06:26](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=386s)).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=0s) Intro

- A new model, Jev, is out from someone the video calls a co-inventor of ChatGPT, pitched as very cheap and very fast ([00:00](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=0s)).
- As a speed demo he sends a live prompt and gets a result in under a second at a fraction of the usual cost ([00:11](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=11s)).
- The video's goal: explain Jev simply and show the best ways to integrate it with agentic harnesses like Claude Code to make setups faster, cheaper, and capable of new automations ([00:16](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=16s)).

### [00:32](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=32s) What is Jev

- Jev is notable because it was released by a claimed co-inventor of ChatGPT ([00:36](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=36s)).
- A promoter's post (~38 million views) claims Jev is a new frontier model type, 20–200x faster and 40–400x cheaper than existing models ([00:42](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=42s)).
- Reading the rate card, Jay says it looks roughly 24x cheaper than Haiku and 230x cheaper than Fable 5.1 ([00:59](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=59s)).
- Pricing mechanic: output tokens are always free; you pay only for input tokens, at about four cents per million ([01:06](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=66s)).
- Jev can only answer in three shapes: binary true/false, a selection from a menu of options, or a rating on a scale such as 0–10 ([01:21](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=81s)).
- Jev is not a large language model. TypeSafe, the company behind it, frames it as the first "System 1" model, versus "System 2" models like Fable and Astra ([01:46](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=106s)).
- He ties this to *Thinking, Fast and Slow*: System 1 makes fast snap decisions; Jev optimizes for that and outputs classifications very fast and cheaply ([02:04](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=124s)).
- System 2 models (LLMs) generate text word by word — more flexible output, but slower ([02:28](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=148s)).
- The core takeaway: combine a System 1 model like Jev with a System 2 model like the Claude models ([02:45](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=165s)).

### [03:00](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=180s) How to set it up

- Jev is available through several platforms. One route is connecting directly to TypeSafe ([03:03](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=183s)).
- Per TypeSafe's launch post at recording time, Jev just became available to everyone; a waitlist had existed until hours earlier. Sign up at their URL to get an API key to connect to Claude ([03:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=192s)).
- The route Jay actually used was OpenRouter, which stays updated with the newest models ([03:26](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=206s)).
- Setup with Claude or any agentic harness is "one prompt away"; he shows a starter prompt you can screenshot ([03:39](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=219s)).
- He also offers a free PDF guide with all the prompts and setup to hand to your agent ([03:47](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=227s)).
- After setup, confirm with Claude that it has access to Jev, then start using it ([03:59](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=239s)).
- He'll cover three levels of use, after a plug for the RoboNuggets community, its "Claude Living Master Class," and an "agents as a service" course ([04:06](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=246s)).

### [04:43](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=283s) Level 1 — integrate Jev into your agentic OS

- Level 1 is wiring Jev into your agentic operating system (how you work with your agents) for faster results and less token burn ([04:43](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=283s)).
- **Use case 1 — model routing:** let Jev automate which model handles each task given to Claude ([05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s)).
- Rationale: Fable is the most expensive and defaulting to Opus every time drains usage; Sonnet and Haiku are often enough, and no cheap, quick way to automate that choice existed until Jev ([05:13](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=313s)).
- In his demo, he had Claude run about 12 prompts with Jev routing versus a run using Fable 5.1 every time; Jev routing gave ~70% savings because 9 of the 12 tasks never needed the top model ([05:48](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=348s)).
- His own caveat: test it on your work to check output quality is still good enough for the tokens saved ([06:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=372s)).
- Practical tip: build a skill command to toggle Jev off and on. He typed `/jev on`, so for that whole session Claude used Jev to pick the model per task ([06:26](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=386s)).
- Example: asked to find the file path of the Jev router script, Jev assigned a cheap Haiku helper; without Jev the session would have used its Opus 5 default ([06:44](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=404s)).
- **Use case 2 — faster skill selection:** make Claude quicker at finding the right skill ([07:03](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=423s)).
- Across 14 tests asking Claude to find a specific skill, Jev found the right one in about 5 seconds total versus roughly 30 seconds for Opus 5 ([07:29](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=449s)).
- How it works: input is the task, options are your skills; Jev picks the skill Claude then loads. He has about 145 skills in his workspace, and Jev returns the right one almost instantly ([07:35](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=455s)).

### [08:01](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=481s) Level 2 — business classification automations

- Level 2 is using Jev for business use cases — automations at near "lightning speed" for far less cost than other models ([08:01](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=481s)).
- Demo: 100 emails, with the automation needing to answer a business question — which are leads worth contacting (support-ticket triage is another example) ([08:16](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=496s)).
- Jev does the classification in one column while Haiku and Fable run alongside to compare speed and cost ([08:33](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=513s)).
- On run, Jev classified all the emails (warm / not a lead / cold) in under a second, much faster and cheaper than the other models ([08:52](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=532s)).
- Where Jev shines: a high volume of items with a business question attached ([09:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=545s)).
- Example domains: invoice-fraud detection, spam detection, community moderation, high-volume refund requests, and churn classification for a subscription business ([09:16](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=556s)).
- The pattern to look for in your business: things received in volume that need classifying — introduce Jev to upgrade those automations with a few prompts ([09:36](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=576s)).

### [09:51](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=591s) Level 3 — new apps enabled by System 1 models

- Level 3 is building apps that only become viable or cost-effective because of cheap System 1 inference ([09:51](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=591s)).
- His own example: he generates many images and videos and stores them in his OS, Rubric ([10:02](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=602s)).
- Problem: default search matches only file names — typing "claude" returns only files whose names contain "claude," like a plain Ctrl-F ([10:16](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=616s)).
- With Jev in the image search, you can search by meaning (semantic search) across images and videos, shown side by side against filename search ([10:26](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=626s)).
- Good fit: any app where users search a lot — try Jev to improve the experience ([10:42](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=642s)).
- Second example: Unclutter, a Chrome extension (by a maker whose name is garbled in the captions) that toggles on to auto-clean pages of elements classified as "slop." Jev does the classifying under the hood, deciding whether elements are ads or cookie banners and removing them ([10:51](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=651s)).

### [11:18](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=678s) Wrap up

- Recap of Jev plus the use cases as a new paradigm for how AI models are made and used; he asks viewers what they'd use Jev for and signs off ([11:18](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=678s)).

## Caveats & disagreements

- **The big multipliers are vendor/promoter claims, not benchmarks.** "20–200x faster, 40–400x cheaper," ~24x cheaper than Haiku, and ~230x cheaper than Fable 5.1 come from a viral promoter post and TypeSafe's own rate card, not independent testing ([00:42](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=42s), [00:59](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=59s)). Treat as unverified.
- **Pricing is launch-day vendor pricing.** "Output tokens always free, ~4c per million input" is a launch claim that may change ([01:06](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=66s)).
- **His own results are small, non-rigorous tests.** The "~70% savings" (12-prompt routing comparison) and "5s vs 30s" (14-prompt skill-selection comparison) are his own quick tests on his workspace, not controlled evaluations; he explicitly warns you must validate quality on your own tasks ([05:48](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=348s), [06:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=372s), [07:10](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=430s)).
- **"Not an LLM / first System 1 model"** is TypeSafe's marketing framing, not a neutral technical classification ([01:46](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=106s)).
- **"Co-inventor of ChatGPT"** is presented as the video's attribution, not established fact ([00:36](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=36s)).
- **Model names (Fable 5.1, Opus 5, Astra)** are spoken as near-future/hypothetical version names; capitalization and versioning are unverified.
- The video is a launch-day explainer with sponsor and affiliate links and a lead-gen PDF, so availability, access, and pricing are time-sensitive ([03:12](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=192s), [03:47](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=227s)).

## Build from this

- [[Add a Jev Decision Layer to Claude Code]] — wire Jev into Claude Code for model routing and skill selection, with a `/jev on` toggle skill.
- [[Build a Jev Classification Pipeline]] — run Jev over high-volume items (leads, fraud, spam, refunds, churn) as a fast classifier.

## Resources mentioned

- **Jev** — the structured System 1 model from TypeSafe; three output shapes, free output tokens ([00:04](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=4s), [01:06](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=66s)).
- **TypeSafe** — the company behind Jev; direct API-key access ([01:53](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=113s)).
- **OpenRouter** — the route Jay used to connect to Jev ([03:26](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=206s)).
- **Claude / Claude Code** — the System 2 harness Jev augments; models named Haiku, Sonnet, Opus / Opus 5, Fable 5.1 ([02:54](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=174s), [06:44](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=404s)).
- **Rubric** — Jay's own OS where he stores media and demos semantic search ([10:02](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=602s)).
- **Unclutter** — a Chrome extension that uses Jev to classify and strip page "slop" ([10:51](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=651s)).
- Free PDF setup guide, and the RoboNuggets community ([03:47](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=227s), [04:09](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=249s)).

## Transcript notes

- Captions render the product name as "Javis" at the wrap up ([11:18](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=678s)) and as "Jeb"/"Jeff" elsewhere — the product is **Jev** throughout.
- "Typesafe" → **TypeSafe** (TypeSafe AI), the company behind Jev.
- "/jv on" → the intended slash command is **`/jev on`**.
- "cloud code" / "cloud" → **Claude Code / Claude**.
- "ChachiBT" → **ChatGPT**; "system one / system 2" → **System 1 / System 2**.
- The promoter's name ("Dooo") and the Unclutter maker's name ("Kits") are garbled in the captions; actual names *(unclear in captions)*.

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Choosing a Claude Model]]
