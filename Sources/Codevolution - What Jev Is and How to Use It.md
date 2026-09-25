---
type: source
title: Codevolution - What Jev Is and How to Use It
creator: "[[Codevolution]]"
channel: Codevolution
url: https://www.youtube.com/watch?v=ZgXej_9isxY
video_id: ZgXej_9isxY
published: 2026-09-20
duration: 22:12
ingested: 2026-09-24
topics: [jev, typesafe, system-1, typescript-sdk, classification]
tags: [source/youtube, topic/models]
---

# Codevolution - What Jev Is and How to Use It

> **Creator:** [[Codevolution]] · **Published:** 2026-09-20 · **Length:** 22:12 · [Watch on YouTube](https://www.youtube.com/watch?v=ZgXej_9isxY)

## TL;DR

The most developer-focused tour of [[Jev]] in this batch: a TypeScript-SDK deep dive from Codevolution. Jev (from the company TypeSafe) is framed as a "smart if statement" — a fast, structured decision model for judgments you can't express in plain code, like "does this customer sound frustrated?". Unlike GPT/Claude/Grok, it generates no free-form text; it returns judgments as data (probabilities), which lets it compute answers in parallel rather than token-by-token. You send a **state** (text, JSON, or array) plus one or more named **questions**, each of type **Noul** (yes/no), **Choice** (pick from your options), or **Score** (rate on a scale you define). The video demos a support message first in the TypeSafe Playground, then via `@typesafe.ai/sdk` with `client.system1(...)` and the `noul`/`choice`/`score` helpers — including batching all three questions in one request and acting on the result with a review threshold.

## Key takeaways

- Jev is a decision model, not a chat model — best mental model is a "smart if statement" for judgments code can't express directly [00:29](https://www.youtube.com/watch?v=ZgXej_9isxY&t=29s).
- It is a "System 1 model": fast, structured judgments software can consume directly; it returns no sentences [01:30](https://www.youtube.com/watch?v=ZgXej_9isxY&t=90s).
- Structured output isn't unique to Jev — GPT and Claude can do it too. Jev's edge is *focus*: only the judgment, so probabilities compute in parallel [03:59](https://www.youtube.com/watch?v=ZgXej_9isxY&t=239s).
- The request model is **state + named questions → per-question answers**; three question types: Noul, Choice, Score [06:41](https://www.youtube.com/watch?v=ZgXej_9isxY&t=401s).
- A low Noul probability means confidently "no", not "unsure"; ~0.5 is genuine uncertainty [07:31](https://www.youtube.com/watch?v=ZgXej_9isxY&t=451s).
- Choice and Score return a confidence value; Noul does not. Confidence reflects the probability spread, not guaranteed accuracy [10:27](https://www.youtube.com/watch?v=ZgXej_9isxY&t=627s).
- Multiple questions over one state go in a single `client.system1(...)` call and are evaluated independently, in parallel [09:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=565s).
- Don't reach for Jev when you need to write/summarize/generate text, or when you can compute the answer exactly in code [20:28](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1228s).

## Notes by chapter

### [00:29](https://www.youtube.com/watch?v=ZgXej_9isxY&t=29s) What Is Jev

Jev is an AI model from the company TypeSafe used to make decisions; the simplest mental model is a smart if statement [00:29](https://www.youtube.com/watch?v=ZgXej_9isxY&t=29s). The contrast: "free delivery if 3+ items" is trivial to write in code, but "flag customers who sound frustrated" can't be done with keyword matching — a message like "I've contacted you three times and I'm still waiting" never says "frustrated" yet clearly is [00:42](https://www.youtube.com/watch?v=ZgXej_9isxY&t=42s). You hand Jev the message, ask whether the customer sounds frustrated, and it makes a judgment in a fraction of a second [01:15](https://www.youtube.com/watch?v=ZgXej_9isxY&t=75s).

### [01:30](https://www.youtube.com/watch?v=ZgXej_9isxY&t=90s) System 1 Models and the Name Jev

TypeSafe describes Jev as a System 1 model built to make fast, structured decisions software can use directly, and Codevolution unpacks that in three parts [01:30](https://www.youtube.com/watch?v=ZgXej_9isxY&t=90s). "System 1" comes from Daniel Kahneman's *Thinking, Fast and Slow* — fast intuitive judgments versus slower deliberate reasoning; Jev borrows the first for quick judgments inside software [01:44](https://www.youtube.com/watch?v=ZgXej_9isxY&t=104s). The name "Jev" comes from William Stanley Jevons and the Jevons paradox: more efficient steam engines made coal cheaper to burn, so total coal use went *up* — efficiency can increase consumption. TypeSafe's bet is the same for AI: much cheaper decisions get used in far more places [02:13](https://www.youtube.com/watch?v=ZgXej_9isxY&t=133s). "Fast" = a reported end-to-end response time of 70–500 ms [02:53](https://www.youtube.com/watch?v=ZgXej_9isxY&t=173s); "structured" = answers as data, not sentences [03:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=184s); "software can use directly" = Jev makes the judgment, your app decides what happens next (e.g. flag for support) [03:16](https://www.youtube.com/watch?v=ZgXej_9isxY&t=196s).

### [03:34](https://www.youtube.com/watch?v=ZgXej_9isxY&t=214s) Jev vs GPT Claude Grok

Anticipating "can't I already do this with OpenAI or Claude?" — yes: general models can make judgments and return structured output, so that isn't unique to Jev [03:38](https://www.youtube.com/watch?v=ZgXej_9isxY&t=218s). The difference is design. GPT and Claude can also write replies, explain concepts, and generate code; Jev focuses only on the judgment and never generates a reply or explains its answer [03:59](https://www.youtube.com/watch?v=ZgXej_9isxY&t=239s). Because it doesn't emit a reply one token at a time, it can produce the answer probabilities in parallel — the core reason it's faster and cheaper for pure decision tasks [04:18](https://www.youtube.com/watch?v=ZgXej_9isxY&t=258s). Vendor example: a task that took a GPT model (name garbled in captions) about 8.6 seconds took Jev only 114 ms [04:33](https://www.youtube.com/watch?v=ZgXej_9isxY&t=273s), and the same task cost the GPT request ~1.4¢ versus under 1/100th of a cent for Jev — roughly 1/170th the cost [04:48](https://www.youtube.com/watch?v=ZgXej_9isxY&t=288s).

### [05:03](https://www.youtube.com/watch?v=ZgXej_9isxY&t=303s) Cost

Current price: 4.2¢ per million input tokens (= $42 per billion input tokens) [05:08](https://www.youtube.com/watch?v=ZgXej_9isxY&t=308s), with output tokens completely free — you pay only for what you send in [05:21](https://www.youtube.com/watch?v=ZgXej_9isxY&t=321s). Perspective: at ~500 input tokens per message-plus-question, you could check ~47,000 messages for about $1, so screening every incoming message for frustration is cheap [05:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=325s).

### [05:59](https://www.youtube.com/watch?v=ZgXej_9isxY&t=359s) How Jev Works

Understand Jev through its input and output [06:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=364s). The input is the information to look at plus the questions to answer; TypeSafe calls the information the **state**, which can be plain text, a JSON object, or an array [06:22](https://www.youtube.com/watch?v=ZgXej_9isxY&t=382s). The customer message is the state. You then give one or more **questions** about that state, and for each you choose a question type based on the kind of answer you need — Noul, Choice, or Score [06:41](https://www.youtube.com/watch?v=ZgXej_9isxY&t=401s).

### [06:51](https://www.youtube.com/watch?v=ZgXej_9isxY&t=411s) Noul Choice and Score

**Noul** — for a yes/no question. Instead of true/false, Jev returns the probability that the answer is "yes" as a number between 0 and 1 (e.g. 0.95 = 95% probability of yes). A value near 0 means confidently "no"; ~0.5 means it isn't leaning either way. The key nuance: a low number means confidently no, not unsure [07:09](https://www.youtube.com/watch?v=ZgXej_9isxY&t=429s).

**Choice** — pick from a set of options you provide (e.g. update / refund / replacement / something else). Jev picks one option and returns probabilities for all options; you define the options and it must choose from the list, so a "something else" catch-all covers messages that don't fit [07:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=472s).

**Score** — judge where something falls on a scale you define. Example levels for frustration: level 0 = a request with no frustration, level 1 = dissatisfaction, level 2 = strong anger. You *describe* each level (better than "rate 1–10"). Levels start at 0, and the score is a weighted average of the level probabilities, so it can fall between levels — equal probability on levels 1 and 2 gives a score of 1.5 [08:31](https://www.youtube.com/watch?v=ZgXej_9isxY&t=511s). Questions over the same state don't need separate requests: put them in one request and Jev evaluates them independently, in parallel — "independently" meaning no question can read another's answer, so each must make sense from the state alone [09:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=565s).

### [09:59](https://www.youtube.com/watch?v=ZgXej_9isxY&t=599s) Understanding the Response

You get one answer per question, matched to the name you gave that question [10:01](https://www.youtube.com/watch?v=ZgXej_9isxY&t=601s). Noul → the probability of "yes". Choice → the selected option plus probabilities for all options. Score → the score, the level probabilities, and a **legend** mapping levels back to their descriptions [10:18](https://www.youtube.com/watch?v=ZgXej_9isxY&t=618s). Getting an answer doesn't make it correct — Jev can misinterpret. Choice and Score also return a **confidence** value based on how the probabilities are distributed; use it to decide whether the app acts or routes to human review. Confidence is not a guarantee of accuracy, so you must try your own examples to pick a threshold [10:27](https://www.youtube.com/watch?v=ZgXej_9isxY&t=627s). Noul does not return a separate confidence value — you read how strongly its probability favors yes or no [10:54](https://www.youtube.com/watch?v=ZgXej_9isxY&t=654s). The response also reports which model version handled the request and how many tokens it used [11:04](https://www.youtube.com/watch?v=ZgXej_9isxY&t=664s).

### [11:20](https://www.youtube.com/watch?v=ZgXej_9isxY&t=680s) Playground

Jev is in early access, so you join the waitlist if you don't have access; you can also reach it through Vercel's AI Gateway, and it's noted as free to use until Sept 23rd [11:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=684s). (Both are launch-window details — see Caveats.) In the TypeSafe Console you can try Jev in the Playground or get an API key. The Playground layout puts the **state** in the top section and the **questions** in the bottom [11:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=712s). The demo enters the state as JSON with a `message` property (plain text is allowed, but a `message` field matches the code), asks a Noul question "Does the customer message express frustration?", and gets back 92% true with the response time shown in milliseconds — closer to 1 means more strongly frustrated [12:19](https://www.youtube.com/watch?v=ZgXej_9isxY&t=739s).

### [12:54](https://www.youtube.com/watch?v=ZgXej_9isxY&t=774s) TypeScript SDK

TypeSafe provides a Python SDK and a JavaScript SDK with TypeScript support; the demo uses TypeScript, with a linked GitHub repo [12:56](https://www.youtube.com/watch?v=ZgXej_9isxY&t=776s). In `package.json`, the SDK is installed as **`@typesafe.ai/sdk`**, alongside TypeScript, Node.js types, and TSX (to run `.ts` files directly); the project uses ES modules, enabling top-level `await` [13:19](https://www.youtube.com/watch?v=ZgXej_9isxY&t=799s). A `.env` file holds the API key created in the console [13:43](https://www.youtube.com/watch?v=ZgXej_9isxY&t=823s). Two demo files: `demo.ts` (one Noul question) and `all_questions.ts` (Noul, Choice, Score together) [13:59](https://www.youtube.com/watch?v=ZgXej_9isxY&t=839s). `demo.ts` imports the TypeSafe client and the `noul` helper, checks an API key is available, and creates a client [14:15](https://www.youtube.com/watch?v=ZgXej_9isxY&t=855s). It defines the state as an object with a `message` property, then calls `client.system1(...)` passing the state and a question named `is frustrated` (the name used to find its answer); the text inside `noul(...)` is the actual question, pointed at the `message` field [14:38](https://www.youtube.com/watch?v=ZgXej_9isxY&t=878s). A `demo` npm script uses TSX to load the env file and run `demo.ts` via `npm run demo` [15:03](https://www.youtube.com/watch?v=ZgXej_9isxY&t=903s). The response comes back almost instantly: model **Jev 1.13.0**; under `answers`, `is frustrated` holds a `noul` value of 0.94 (probability of yes); usage shows input tokens 292, output tokens 23 [15:20](https://www.youtube.com/watch?v=ZgXej_9isxY&t=920s). Changing the message to "Thanks for the update. Everything is working now." with the same question returns a Noul of 0.03 — no frustration — again in under a second [15:48](https://www.youtube.com/watch?v=ZgXej_9isxY&t=948s).

### [16:17](https://www.youtube.com/watch?v=ZgXej_9isxY&t=977s) Multiple Questions in One Request

`all_questions.ts` reuses the original message but adds three question types in one call, importing `noul`, `choice`, and `score` [16:17](https://www.youtube.com/watch?v=ZgXej_9isxY&t=977s). The questions: (Noul) `is frustrated` = "Does message express frustration?"; (Choice) `request type` = "What is the main request in message?" with options update / refund / replacement / something else; (Score) "How much frustration does message express?" with the three described levels [16:43](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1003s). It's still only one call because all three share the same state; run with `npm run all` [17:22](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1042s). The response: `is frustrated` (Noul); `request type` (Choice) = update with confidence 0.99 and per-option probabilities (update ~99%, others near 0) [17:38](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1058s); the Score question returns score 1.02, confidence 0.97 — between levels 1 and 2 (dissatisfaction edging into anger) with probabilities 0.98 and 0.02 — and even with three questions the elapsed time stays under a second [18:12](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1092s). The app code then sets a review threshold of 0.8 (a demo value), checks whether the `is frustrated` Noul value is ≥ the threshold, and if so flags the message for support review; choose your own threshold by testing representative messages [18:45](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1125s).

### [19:32](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1172s) When to Use Jev and When Not

Good fits: route customer requests, categorize large document collections, check whether a passage supports a claim, decide which model should handle a task (model routing), or make a quick decision in a game or interface [19:40](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1180s). TypeSafe's docs list many more — search and retrieval, scientific discovery, model routing, LLM guardrails, semantic code linting, recruiting, lead generation, customer support, insurance claims, financial crime, advertising, gaming — worth looking up [20:00](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1200s). When **not** to use Jev: if you need to write a reply, summarize an article, or generate code, use a text-generating model — Jev judges the information going into a task but won't write the result [20:28](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1228s). Also skip it when you can compute the answer exactly in code — the 3-items free-delivery check, arithmetic, counting, comparing dates [20:45](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1245s). Rule of thumb: if you have a judgment to make, can describe the possible answers, and speed or repeated use matters, Jev is worth trying [20:57](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1257s).

### [21:09](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1269s) Recap

Jev is TypeSafe's model for making decisions about information: give it a state plus questions, get structured answers for your app. The three types recap as Noul (yes/no judgment), Choice (pick from your options), and Score (judge on a scale you define). Its focus on decisions makes it fast and inexpensive; it was demoed both in the Playground and from TypeScript. Suggested start: pick one small decision in your app and see how Jev handles your examples [21:09](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1269s).

## Caveats & disagreements

- **All latency and cost figures are vendor / single-task numbers.** The 70–500 ms latency, the "8.6 s → 114 ms" speedup, and the "~1/170th the cost" comparison come from TypeSafe/Codevolution's own examples on one task, not independent benchmarks; the compared GPT model name is garbled in the captions, so the head-to-head isn't verifiable [04:33](https://www.youtube.com/watch?v=ZgXej_9isxY&t=273s).
- **Pricing is time-sensitive.** "4.2¢ per million input tokens", "output free", and "47,000 messages for $1" are current-as-of-video and rest on a 500-token/message assumption [05:08](https://www.youtube.com/watch?v=ZgXej_9isxY&t=308s).
- **Early-access details are stale.** The waitlist, Vercel AI Gateway path, and "free until Sept 23rd" are launch-window specifics from a video dated 2026-09-20 and are likely already out of date [11:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=684s).
- **Confidence ≠ accuracy.** Confidence reflects the probability distribution, not guaranteed correctness, and thresholds must be tuned on real examples; Noul returns no confidence value at all [10:27](https://www.youtube.com/watch?v=ZgXej_9isxY&t=627s).
- **"Smart if statement" is a simplification.** A useful mental model, but it understates that outputs are probabilistic judgments needing threshold/review logic, not deterministic branches.
- **Demo-run artifacts.** The model version (Jev 1.13.0) and token counts (292/23) are specifics of one demo run, not stable facts [15:20](https://www.youtube.com/watch?v=ZgXej_9isxY&t=920s).

## Build from this

- [[Build a Jev Classification Pipeline]] — the Playground-first, then `@typesafe.ai/sdk` batched multi-question workflow with a review threshold, drawn straight from this demo.

## Resources mentioned

- Jev / TypeSafe docs: https://docs.typesafe.ai/introduction
- Demo repo (TypeScript project used in the video): https://github.com/gopinav/jev-demo
- npm package: `@typesafe.ai/sdk` (JavaScript/TypeScript SDK; a Python SDK also exists)
- TypeSafe Console / Playground (state + questions, API keys); access via early-access waitlist or Vercel's AI Gateway
- Comparison models named as general-purpose LLMs: GPT / OpenAI, Claude, Grok, Gemini

## Beyond the source

- Jev's canonical product facts (three question types, request shape, SDK method) are consistent with TypeSafe's docs at https://docs.typesafe.ai/introduction. The demo repo lives under the `gopinav` GitHub account: https://github.com/gopinav/jev-demo.

## Transcript notes

- **"null" → Noul** (systematic). The captions consistently render the first question type and the SDK helper as "null"; the official name per the video's title/chapter metadata is **Noul** (the `noul(...)` helper / `noul` value). Corrected throughout.
- **"Jef" / "Jeff" → Jev** — the model name is spelled Jev throughout; captions frequently render it "Jef" or "Jeff".
- **"typesafe.ai/sdk" → `@typesafe.ai/sdk`** — the captions drop the `@` scope prefix from the npm package name.
- **"GPT 5.6 tera" [04:33] → garbled GPT model name** *(unclear in captions)* — almost certainly a GPT model name mangled by the captions; the exact string is not reliable.
- **"Type Safe" / "Typesafe" → TypeSafe** — the company is one word, camelCase.

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Choosing a Claude Model]]
