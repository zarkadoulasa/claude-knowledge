---
type: tool
category: "Decision model (System 1) — TypeSafe"
website: "https://typesafe.ai"
sources: ["[[Jay E - Pairing Jev with Claude Code]]", "[[Zubair Trabzada - What Jev Actually Is]]", "[[Codevolution - What Jev Is and How to Use It]]", "[[Nate Herk - Testing Jev on 12 Real Use Cases]]"]
tags: [topic/models, topic/claude-code, topic/automation]
---

# Jev

## What it is

Jev is an AI model from the company TypeSafe, pitched not as an LLM but as the first **"System 1 model"**: it makes fast, structured decisions and returns **no free-form text** — only machine-usable data ([01:37](https://www.youtube.com/watch?v=ZgXej_9isxY&t=97s), Codevolution; [01:19](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=79s), Zubair, "the type of AI that decides but does not write"). Nate Herk frames the same idea: Jev makes decisions but doesn't write, emits no conversational tokens, and can't be chatted with ([00:51](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=51s)).

Every answer takes one of **three question types** (official TypeSafe names): **Noul**, **Choice**, and **Score** ([07:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=424s), Codevolution). Auto-captions often render Noul as "null" — including in [[Nate Herk - Testing Jev on 12 Real Use Cases|Nate Herk's]] video ([02:15](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=135s)) — but the canonical name is Noul.

**Request shape:** you send a **state** (plain text, a JSON object, or an array) plus one or more **named questions** about it; the state is the information Jev looks at ([06:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=384s), Codevolution). Multiple questions over the same state go in one call and are evaluated **independently, in parallel** — one question can't see another's answer ([09:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=565s)).

**Speed and cost (vendor figures — time-sensitive):** TypeSafe reports end-to-end response times of **70–500 ms** ([03:01](https://www.youtube.com/watch?v=ZgXej_9isxY&t=181s), Codevolution); Zubair observed responses under ~100 ms in his demo ([04:04](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=244s)). Pricing is **~4.2¢ per million input tokens** with **output tokens free** ([05:11](https://www.youtube.com/watch?v=ZgXej_9isxY&t=311s), Codevolution; Jay E gives the same "four cents per million" input, output always free at [01:11](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=71s)). No token-by-token generation is why the probabilities can be computed in parallel and cheaply ([04:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=264s), Codevolution).

**SDK and access:** the TypeScript/JS package is **`@typesafe.ai/sdk`**, called via **`client.system1(...)`** with `noul` / `choice` / `score` helpers and an API key in a `.env` file; a Python SDK also exists, and there's a web **Playground/Console** for trying it without code ([12:56](https://www.youtube.com/watch?v=ZgXej_9isxY&t=776s), [13:19](https://www.youtube.com/watch?v=ZgXej_9isxY&t=799s), [11:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=712s), Codevolution). Access is via the **TypeSafe waitlist/early access**, **Vercel AI Gateway**, or **OpenRouter** ([11:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=684s), Codevolution; [07:36](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=456s), Zubair; [01:14](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=74s), Nate). The context window is **64k input tokens**, far smaller than the ~1M of Claude or GPT ([03:40](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=220s), Nate). The demo model version shown was **Jev 1.13.0** ([15:20](https://www.youtube.com/watch?v=ZgXej_9isxY&t=920s), Codevolution).

## How sources use it

- [[Codevolution - What Jev Is and How to Use It]] — the most thorough technical walkthrough: Jev as a "smart if statement" for judgments you can't hardcode, demoed on a frustrated customer-support message in the Playground and via the TypeScript SDK ([00:35](https://www.youtube.com/watch?v=ZgXej_9isxY&t=35s)).
- [[Jay E - Pairing Jev with Claude Code]] — wires Jev into a Claude Code "agentic OS" for **model routing** and faster **skill selection**, then high-volume classification and new apps ([05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s)).
- [[Zubair Trabzada - What Jev Actually Is]] — a myth-buster: you **can't build with Jev**; it's a decision layer that sits in the middle of an app built by Claude Code or another model, e.g. the fast routing step in his "Jarvis" assistant ([06:06](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=366s)).
- [[Nate Herk - Testing Jev on 12 Real Use Cases]] — stress-tests Jev on ~12 classification workflows, benchmarks it on 1,000 emails, and foregrounds its limits and the need for evals ([04:27](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=267s)).

## Notes

**The three question types** ([07:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=424s)–[10:18](https://www.youtube.com/watch?v=ZgXej_9isxY&t=618s), Codevolution):
- **Noul** — a yes/no question. Instead of true/false it returns the **probability of "yes" as a number 0–1** (0.95 = 95% yes). A **low value means confidently "no"**, not "unsure"; ~0.5 is genuinely uncertain ([07:22](https://www.youtube.com/watch?v=ZgXej_9isxY&t=442s)).
- **Choice** — pick one from **options you supply**; returns the selected option plus **per-option probabilities** ([07:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=472s)). A "something else" catch-all covers off-list cases.
- **Score** — rate on a **scale you define** with **0-indexed, described levels**; the result is a **weighted average of the level probabilities**, so it can fall between levels (equal weight on levels 1 and 2 → 1.5) ([08:34](https://www.youtube.com/watch?v=ZgXej_9isxY&t=514s), [09:09](https://www.youtube.com/watch?v=ZgXej_9isxY&t=549s)); the response also carries a legend mapping levels back to their descriptions ([10:18](https://www.youtube.com/watch?v=ZgXej_9isxY&t=618s)).

**Confidence vs accuracy:** Choice and Score also return a **confidence value** from how the probabilities are distributed; **Noul returns no separate confidence** (you read how strongly its probability leans) ([10:35](https://www.youtube.com/watch?v=ZgXej_9isxY&t=635s), [10:54](https://www.youtube.com/watch?v=ZgXej_9isxY&t=654s), Codevolution). Confidence is **not a guarantee of accuracy** — tune your own threshold against real examples.

**The core pattern — pair Jev with Claude:** all four videos converge on combining a fast **System 1** decision model (Jev) with a slower **System 2** reasoning LLM (Claude), handing off anything that must be written, summarized, or reasoned about (see [[System 1 and System 2 AI Models]]). Jay E states it directly — "combine a system one with a system two" model ([02:49](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=169s)); Zubair positions Jev in the middle of an app built by Claude Code ([06:06](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=366s)).

**Named uses:**
- **Model routing + skill selection inside Claude Code** — Jev picks the cheapest adequate model per task and the right skill from a large library (~145 skills, ~5s vs ~30s with Opus 5 over Jay E's tests) — see [[Add a Jev Decision Layer to Claude Code]] ([05:05](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=305s), [07:29](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=449s), [07:46](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=466s), Jay E).
- **High-volume classification** — lead/email triage, fraud, spam, refunds, churn, moderation, support routing — see [[Build a Jev Classification Pipeline]] (Nate's 1,000-email run: Jev ~6s optimized / 9¢ vs a chat model ~5 min / 62¢, [06:20](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=380s)–[06:38](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=398s)).

**Limits** (mostly Nate Herk): Jev **cannot write, summarize, find themes, or reason** ([03:29](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=209s)); its context window is **64k tokens** ([03:40](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=220s)); for browser/computer use it can only **decide**, and a second model must act ([15:18](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=918s)); run **evals against a golden dataset** (~100 labeled cases) before trusting it in production ([12:54](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=774s)). Zubair's blunt version: **you can't build anything with Jev** ([00:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=16s)).

**Vendor-claim flags:** the headline **20–200× faster, 40–400× cheaper** than chat LLMs (and Jay E's ~24× cheaper than Haiku, ~230× cheaper than Fable 5.1) are **vendor/promoter claims, not independent benchmarks** ([02:42](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=162s), Nate; [01:01](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=61s), Jay E). All speed/cost multipliers, the latency and pricing figures above, and the "co-inventor of ChatGPT" attribution are the **videos' claims**. The videos credit TypeSafe's founder **Diogo, described as a co-inventor of ChatGPT**, and say Jev was trained with **RLCD (reinforcement learning for calibrated decisions)** ([01:00](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=60s)–[01:05](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=65s), Nate); treat "co-inventor of ChatGPT" as a claim, not established fact.

## Beyond the source

- **Naming origins.** "System 1" borrows Daniel Kahneman's *Thinking, Fast and Slow* (fast intuitive judgments vs slow deliberate reasoning); "Jev" is from 19th-century economist William Stanley Jevons and the **Jevons paradox** (efficiency lowers unit cost and raises total consumption — TypeSafe's bet that cheaper AI decisions get used far more widely). Codevolution explains both on-camera ([01:44](https://www.youtube.com/watch?v=ZgXej_9isxY&t=104s), [02:13](https://www.youtube.com/watch?v=ZgXej_9isxY&t=133s)); background at [en.wikipedia.org/wiki/Jevons_paradox](https://en.wikipedia.org/wiki/Jevons_paradox).
- **Docs:** official documentation at [docs.typesafe.ai/introduction](https://docs.typesafe.ai/introduction); demo repo at [github.com/gopinav/jev-demo](https://github.com/gopinav/jev-demo).

## Related

- [[System 1 and System 2 AI Models]]
- [[Add a Jev Decision Layer to Claude Code]]
- [[Build a Jev Classification Pipeline]]
- [[Choosing a Claude Model]]
- [[Claude Code]]
