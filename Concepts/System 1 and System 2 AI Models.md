---
type: concept
aliases: ["System One Models", "Decision models vs LLMs"]
sources: ["[[Jay E - Pairing Jev with Claude Code]]", "[[Zubair Trabzada - What Jev Actually Is]]", "[[Codevolution - What Jev Is and How to Use It]]", "[[Nate Herk - Testing Jev on 12 Real Use Cases]]"]
tags: [topic/models, topic/claude-code]
---

# System 1 and System 2 AI Models

## In one sentence

A fast, structured-decision **"System 1"** model (e.g. [[Jev]]) makes bounded judgments in milliseconds and outputs only data, while a slower text-generating **"System 2"** LLM (e.g. Claude) writes and reasons — and you pair them so each does what it's good at.

## How it works

The framing borrows Daniel Kahneman's *Thinking, Fast and Slow*: **System 1** is fast, intuitive judgment; **System 2** is slower, deliberate reasoning. Codevolution explains that TypeSafe took the System 1 idea for a model that makes quick judgments inside software ([01:44](https://www.youtube.com/watch?v=ZgXej_9isxY&t=104s)), and Jay E draws the same split — LLMs are "system two" models that think more slowly, so the move is to combine a system one with a system two ([02:40](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=160s)).

- **System 1 = bounded, structured outputs.** The model is handed a situation plus a fixed set of possible answers and returns probabilities/decisions as data, never prose ([01:37](https://www.youtube.com/watch?v=ZgXej_9isxY&t=97s), Codevolution). Because it doesn't generate a reply one token at a time, it can compute the answer probabilities **in parallel**, which is why it's much faster and cheaper for decision tasks ([04:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=264s), Codevolution). Zubair's compression: "the type of AI that decides but does not write" ([01:19](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=79s)).
- **System 2 = flexible generation.** General LLMs read input, reason, and emit text word-by-word — more flexible, but slower and pricier per decision. If you gave a System 1-style decision to an LLM it would evaluate, think, then generate an output before deciding — a much slower path ([04:32](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=272s), Zubair). Nate notes System 1 models like Jev are explicitly **not** frontier/System 2 models — a different category, not a competitor to them ([04:21](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=261s)).

## When to use it — and when not to

**Reach for System 1** when you have a **judgment to make**, can **describe the possible answers**, and **speed or repeated use matters** ([20:57](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1257s), Codevolution): high-volume, low-latency classification, request routing, LLM guardrails, and model routing ([19:40](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1180s), Codevolution). Nate's rule: use it for thousands of items or real-time decisions at scale ([04:27](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=267s)).

**Stay with System 2 (Claude/GPT)** when you need to **write a reply, summarize, reason, or generate code** — a System 1 model judges the information going into a task but won't produce the written result ([20:28](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1228s), Codevolution). Nate is blunt about the ceiling: Jev cannot write, summarize, or find themes ([03:29](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=209s)), and for a small handful of items or open-ended understanding you're better off in a chat model ([04:27](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=267s)).

**The handoff / two-model pipeline** is the payoff of the pairing: use the cheap fast model to bucket a large corpus, then hand the narrowed set (or the "act" step) to a capable model to write or analyze ([03:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=228s), [15:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=907s), Nate). For agent work, this is how model routing and skill selection get faster inside Claude Code — see [[Add a Jev Decision Layer to Claude Code]] and [[Build a Jev Classification Pipeline]].

**Before you trust a decision model in production, run evals.** Nate stresses building a golden dataset (~100 inputs with known-correct answers) and running each candidate model through it to compare accuracy, cost, and speed ([12:54](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=774s)) — cost savings only count if the decisions are as accurate.

## Perspectives from sources

- [[Codevolution - What Jev Is and How to Use It]] — the clearest exposition of the analogy: System 1 = Kahneman's fast intuitive judgments, applied as a model for quick decisions in software; structured means answers come back as data, not sentences ([01:44](https://www.youtube.com/watch?v=ZgXej_9isxY&t=104s), [03:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=184s)). Claude appears only as a general-purpose contrast: it *can* return structured output too, so the difference is design/focus, not capability ([03:38](https://www.youtube.com/watch?v=ZgXej_9isxY&t=218s)).
- [[Jay E - Pairing Jev with Claude Code]] — states the pairing thesis directly ("combine a system one with a system two") and applies it to Claude Code model routing and skill selection ([02:49](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=169s)). **Agrees with Codevolution** on the fast/slow split and the combine-both conclusion.
- [[Zubair Trabzada - What Jev Actually Is]] — sharpens the boundary with a skeptical framing: **"you can't build with"** a System 1 model — it's a decision layer that sits in the middle of an app another model builds ([00:16](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=16s), [06:06](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=366s)). His concrete pairing: swap a slow Opus 5 routing call in his "Jarvis" assistant for a fast Jev decision ([08:23](https://www.youtube.com/watch?v=fMV6JKkQVfE&t=503s)).
- [[Nate Herk - Testing Jev on 12 Real Use Cases]] — most explicit on **limits**: not a frontier model, 64k context, can't write/summarize/reason, and any "insight" is composed by the human through question design, not surfaced by the model ([03:29](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=209s), [03:40](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=220s), [11:19](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=679s)). Adds the eval discipline and the handoff pattern ([12:54](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=774s), [15:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=907s)).

## Beyond the source

- **Origins.** "System 1 / System 2" is Daniel Kahneman's dual-process framing from *Thinking, Fast and Slow* ([en.wikipedia.org/wiki/Thinking,_Fast_and_Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)); the product name "Jev" nods to the **Jevons paradox** — efficiency gains raising total consumption ([en.wikipedia.org/wiki/Jevons_paradox](https://en.wikipedia.org/wiki/Jevons_paradox)).
- **"System 1 model" is TypeSafe's marketing framing**, not a neutral technical taxonomy; functionally these are fast classifier/scoring models. Treat the category label as branding, and the vendor speed/cost multipliers as unverified vendor claims (see [[Jev]]).

## Related

- [[Jev]]
- [[Choosing a Claude Model]]
- [[Add a Jev Decision Layer to Claude Code]]
- [[Build a Jev Classification Pipeline]]
- [[Context Window Management]]
