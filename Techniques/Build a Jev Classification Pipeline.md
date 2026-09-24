---
type: technique
goal: "Classify high-volume data with Jev — Playground first, then the TypeScript SDK, with review thresholds and evals"
difficulty: intermediate
time_to_build: "an afternoon"
sources: ["[[Codevolution - What Jev Is and How to Use It]]", "[[Nate Herk - Testing Jev on 12 Real Use Cases]]", "[[Jay E - Pairing Jev with Claude Code]]"]
tools: ["[[Jev]]"]
tags: [topic/models, topic/automation, topic/verification]
---

# Build a Jev Classification Pipeline

## Goal

Use [[Jev]] to make the same judgment across thousands of items — emails, comments, leads, transcripts — cheaply and in near real time. You prototype the decision in the TypeSafe Playground, move it to the `@typesafe.ai/sdk` TypeScript SDK, act on the results with a calibrated review threshold, wire it into automations that fire on every new event, and **run evals against a golden dataset** before trusting it. Jev is the [[System 1 and System 2 AI Models|System 1]] classifier; hand anything generative (a written reply, a summary, theme analysis) off to Claude or GPT.

## Use when

- You have thousands of items that all need the *same* judgment — lead scoring/triage, spam or invoice-fraud detection, refund/churn classification, community moderation, support routing. [Jay E, [09:16](https://www.youtube.com/watch?v=tTnUcSj-QPA&t=556s)]
- You need real-time classification (per new email/comment/lead/transcript, or a live feed). [Nate, [09:26](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=566s)]
- The judgment can't be written as exact code (e.g. "does this customer sound frustrated?") but you *can* describe the possible answers. [Codevolution, [00:42](https://www.youtube.com/watch?v=ZgXej_9isxY&t=42s)]

Do **not** use Jev when you need to write, summarize, or reason (use Claude/GPT), or when you can compute the answer exactly in code. [Codevolution, [20:28](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1228s)]

## Prerequisites

- Jev access: a TypeSafe account (Playground + API key), or the Vercel AI Gateway [Codevolution, [11:24](https://www.youtube.com/watch?v=ZgXej_9isxY&t=684s)]; OpenRouter is another route [Nate, [01:24](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=84s)].
- For the SDK step: Node.js with TypeScript. The demo project uses `@typesafe.ai/sdk`, `typescript`, `@types/node`, and TSX (to run TS files directly), as ES modules with top-level await. [Codevolution, [13:19](https://www.youtube.com/watch?v=ZgXej_9isxY&t=799s)]
- A small labelled dataset (~100 cases) for evals before production. [Nate, [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s)]
- Reference demo repo: `https://github.com/gopinav/jev-demo`.

## Steps

### 1. Define the decision: one state + named questions

Every Jev request is a **state** (plain text, a JSON object, or an array) plus one or more **named questions** about it. Pick a question type per question. [Codevolution, [06:22](https://www.youtube.com/watch?v=ZgXej_9isxY&t=382s)]

The three official question types — get these exact:

- **Noul** — a yes/no question. Returns the **probability that the answer is "yes"** as a number 0–1 (0.95 = 95% yes). A **low value means confidently "no,"** not "unsure"; ~0.5 is genuinely on the fence. **Noul returns no separate confidence value** — you read the probability itself. [Codevolution, [07:09](https://www.youtube.com/watch?v=ZgXej_9isxY&t=429s), [10:54](https://www.youtube.com/watch?v=ZgXej_9isxY&t=654s)]
- **Choice** — pick one of the options *you* supply. Returns the **selected option, per-option probabilities, and a confidence value**. Include a "something else" catch-all. [Codevolution, [07:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=472s)]
- **Score** — rate on a scale you define, with **0-indexed, described levels** (level 0 = …, level 1 = …). Returns a **weighted-average score** (can fall *between* levels, e.g. 1.5), the **level probabilities, a confidence value, and a legend**. Describing each level beats "rate 1–10." [Codevolution, [08:31](https://www.youtube.com/watch?v=ZgXej_9isxY&t=511s)]

Nate Herk's captions render the yes/no type as "null"; the canonical name is **Noul**. [Nate, [02:12](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=132s)]

### 2. Prototype in the TypeSafe Playground

No project setup needed. In the Console → Playground: **state goes in the top section, questions in the bottom.** [Codevolution, [11:52](https://www.youtube.com/watch?v=ZgXej_9isxY&t=712s)]

- Enter the state (Codevolution uses JSON `{ "message": "I've contacted you three times and I'm still waiting" }`; plain text is allowed, but a `message` field matches the code later).
- Add a Noul question "Does the customer message express frustration?", run it, and read the probability (~92% in the demo) and the response time in ms. [Codevolution, [12:19](https://www.youtube.com/watch?v=ZgXej_9isxY&t=739s)]
- Add more questions and view all answers together before you write any code.

### 3. Move to the TypeScript SDK (`@typesafe.ai/sdk`)

Concrete shape from the Codevolution demo:

- Put the API key (created in the console) in a **`.env`** file — update your own key there. [Codevolution, [13:43](https://www.youtube.com/watch?v=ZgXej_9isxY&t=823s)]
- **Single question** (`demo.ts`): import the TypeSafe client and the **`noul`** helper → check the API key is present → create a new client → define the state `{ message: "..." }` → call **`client.system1(state, question)`** where the question is *named* (e.g. `is frustrated`) and its text is wrapped in `noul(...)` pointed at the `message` field → log the response. [Codevolution, [14:15](https://www.youtube.com/watch?v=ZgXej_9isxY&t=855s)]
- Run it with a `demo` npm script that uses TSX to load `.env` and execute the file: **`npm run demo`**. Response comes back sub-second: model `Jev 1.13.0`; under **`answers`**, the key `is frustrated` matches the question name; inside it the **noul value = probability of "yes"** (0.94 in the demo). Usage reports input/output token counts. [Codevolution, [15:20](https://www.youtube.com/watch?v=ZgXej_9isxY&t=920s)]
- **Batch multiple questions in ONE call** (`all_questions.ts`): import `noul`, `choice`, `score`; send one `client.system1` over the same state with three named questions (a Noul, a Choice with options update/refund/replacement/something else, a Score with three described levels). They're evaluated **independently, in parallel** — one question can't see another's answer, so each must make sense from the state alone. Even three questions return in under a second. Read each answer by name: `answers[name]`. [Codevolution, [16:17](https://www.youtube.com/watch?v=ZgXej_9isxY&t=977s), [09:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=565s)]

In the demo the Choice came back `update` with confidence 0.99, and the Score came back 1.02 with confidence 0.97 (between "dissatisfaction" and "anger"). [Codevolution, [17:38](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1058s), [18:12](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1092s)]

### 4. Act on results with a calibrated review threshold

Getting an answer doesn't make it correct — **confidence reflects the probability distribution, not accuracy.** Set a threshold and route uncertain cases to a human. [Codevolution, [10:27](https://www.youtube.com/watch?v=ZgXej_9isxY&t=627s)]

- Codevolution's app sets a review threshold of **0.8** (a demo value): if `answers.is_frustrated.noul >= threshold`, flag the message for support review. [Codevolution, [18:45](https://www.youtube.com/watch?v=ZgXej_9isxY&t=1125s)]
- Nate's variant: for a Noul, define what counts as "yes" and call it yes when the probability is above your cutoff (he used ≥50% for an invoice check). [Nate, [06:56](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=416s)]
- **Calibrate the threshold on representative examples** — don't inherit the demo's 0.8.

### 5. Wire it into production automations

Move from Playground/dashboard runs to real automations: trigger a Jev classification on **each new event** — a new email, comment, lead, form submission, or meeting transcript — and write the structured result to a database. Speed may matter less in a nightly batch, but **cost compounds** at thousands of requests, which is the whole point of routing bulk classification to Jev. [Nate, [09:26](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=566s)]

Nate's throughput data points (vendor/demo figures): 1,000 emails across 7 rules ran ~6 seconds / 9¢ after back-end optimization (vs a chat model ~5 min / 62¢); a console showed ~85¢ of spend across ~20,000 requests. Parallelize the back end to get the fast numbers. [Nate, [05:52](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=352s), [08:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=538s)]

### 6. Run evals, then hand off to a System 2 model

- **Before trusting Jev in production, run evals** against a golden dataset of ~100 labelled cases: run Jev (and a couple of chat models) through it and compare accuracy, cost, and speed. Confidence is not accuracy. [Nate, [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s)]
- **Hand off anything generative.** Jev can't write, summarize, find themes, or reason — use it to cheaply bucket a large corpus, then route the narrowed set to Claude/GPT to draft replies or analyze themes. In browser/computer use, Jev can only *decide*; a second model must act. [Nate, [03:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=228s), [15:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=907s)]

See [[Verification Before Done]] for the general eval-before-trust discipline.

## Starter files & prompts

Modelled on the Codevolution demo (`https://github.com/gopinav/jev-demo`):

- `.env` — `TYPESAFE_API_KEY=...` (name is illustrative; the video shows only that the key lives in `.env`).
- `demo.ts` — client + `noul` helper; state `{ message }`; `client.system1(state, { "is frustrated": noul("Does the message express frustration?") })`; log `answers["is frustrated"].noul`.
- `all_questions.ts` — one `client.system1` call with a Noul, a Choice (options + a catch-all), and a Score (0-indexed described levels).
- `package.json` scripts — `demo` and `all` running the files via TSX with `.env` loaded (`npm run demo`, `npm run all`).

## Economics (vendor figures — time-sensitive)

- **~4.2¢ per million input tokens; output tokens are free.** At ~500 input tokens/message that's ~47,000 messages for $1. [Codevolution, [05:08](https://www.youtube.com/watch?v=ZgXej_9isxY&t=308s)]
- End-to-end latency ~**70–500 ms** (TypeSafe's own figure). [Codevolution, [03:01](https://www.youtube.com/watch?v=ZgXej_9isxY&t=181s)]

Frame all of these as vendor/demo numbers, not independent benchmarks.

## Done when

- [ ] The decision is expressed as a state + named questions with the right types (Noul / Choice / Score).
- [ ] It works in the Playground and returns sensible probabilities on your examples.
- [ ] The SDK version runs (`npm run demo` / `npm run all`) and you read answers by name from `answers[...]`.
- [ ] Multiple questions go in one `client.system1` call, not one call each.
- [ ] A review threshold is set and *calibrated on your data*, routing low-confidence cases to review.
- [ ] Evals against a ~100-case golden dataset have run before any production trust.
- [ ] Generative follow-up (replies/summaries) is handed to Claude/GPT, not attempted with Jev.

## Pitfalls

- **Confidence ≠ accuracy.** A confident answer can be wrong; calibrate thresholds and eval before trusting. [Codevolution, [10:27](https://www.youtube.com/watch?v=ZgXej_9isxY&t=627s); Nate, [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s)]
- **64k-token context window** — far smaller than the ~1M of Claude/GPT; you can't feed huge documents in one request. Chunk, or narrow before sending. [Nate, [03:37](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=217s)]
- **Noul has no confidence field** — don't look for one; read the probability's distance from 0.5. A low Noul is a confident "no." [Codevolution, [10:54](https://www.youtube.com/watch?v=ZgXej_9isxY&t=654s)]
- **Questions are independent** — one can't reference another's answer; each must stand alone against the state. [Codevolution, [09:25](https://www.youtube.com/watch?v=ZgXej_9isxY&t=565s)]
- **Parallelize the back end** to get the advertised throughput; a naive serial loop is far slower. [Nate, [06:23](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=383s)]
- **Validate quality vs a chat model** — cost savings only count if accuracy holds; the videos never quantify Jev's accuracy. [Nate, [03:10](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=190s)]
- **Costs compound at scale** — cheap per call, but volume adds up; the flip side is that's exactly where Jev beats a chat model.
- **Pricing/access are launch-window figures** (free trials, waitlist state, rates) and may already be stale.

## Variations

- **Model routing / skill selection** — the same Choice mechanic applied to picking a model or skill; see [[Add a Jev Decision Layer to Claude Code]].
- **Semantic search & content moderation** — Jev as the meaning-based classifier behind search results or a "slop" filter (Jay E's Level 3 apps).
- **Real-time feeds** — classify a live stream (Nate's X-feed badge extension; per-second decisioning) where latency, not just cost, is the win.

## Sources

- [[Codevolution - What Jev Is and How to Use It]] — the three question types, Playground, and the `@typesafe.ai/sdk` demo with review threshold. `https://www.youtube.com/watch?v=ZgXej_9isxY`
- [[Nate Herk - Testing Jev on 12 Real Use Cases]] — production automations, throughput/cost benchmarks, evals, handoff and the 64k limit. `https://www.youtube.com/watch?v=ymgH8jS6Wb8`
- [[Jay E - Pairing Jev with Claude Code]] — high-volume business classification use cases (lead/fraud/spam/churn/moderation). `https://www.youtube.com/watch?v=tTnUcSj-QPA`

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Verification Before Done]]
- [[Add a Jev Decision Layer to Claude Code]]
