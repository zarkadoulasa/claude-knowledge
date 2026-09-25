---
type: source
title: Nate Herk - Testing Jev on 12 Real Use Cases
creator: "[[Nate Herk]]"
channel: Nate Herk | AI Automation
url: https://www.youtube.com/watch?v=ymgH8jS6Wb8
video_id: ymgH8jS6Wb8
published: 2026-09-19
duration: 16:08
ingested: 2026-09-24
topics: [jev, classification, model-routing, ai-economics, evals]
tags: [source/youtube, topic/models, topic/automation, topic/verification]
---

# Nate Herk - Testing Jev on 12 Real Use Cases

> **Creator:** [[Nate Herk]] · **Published:** 2026-09-19 · **Length:** 16:08 · [Watch on YouTube](https://www.youtube.com/watch?v=ymgH8jS6Wb8)

## TL;DR

An honest review of [[Jev]], TypeSafe's fast, cheap decision model, stress-tested on 12 mostly-classification use cases (emails, YouTube comments, Skool posts, X feed, meetings, video clips, contracts, jobs/leads, brain-dump routing, customer support, trading). Jev outputs only structured decisions (yes/no, pick-one, score) plus a confidence level, never free-form text, so Nate frames it as a [[System 1 and System 2 AI Models|System 1]] classifier you pair with a smart reasoning model. His verdict: a genuine game-changer for high-volume, real-time decision workflows where cost and speed compound, but not a frontier model, capped at a 64k context window, and unable to write, summarize, or reason. His strongest advice is to run [[Verification Before Done|evals against a golden dataset]] before trusting it in production. The numbers and the caveats below carry the review.

## Key takeaways

- Jev makes decisions and outputs no tokens; you set the classification rules and it returns a yes/no + confidence, a category, and a score [00:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=48s).
- On a 1,000-email, 7-rule benchmark Jev ran ~70s / 9¢ (unparallelized), then 6s / 9¢ after back-end optimization, versus a chat model at ~5 min / 62¢ [05:52](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=352s).
- 64k input context (vs ~1M for Claude/GPT) is the headline limit; Jev cannot write, summarize, find themes, or reason [03:37](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=217s).
- The core pattern is a two-model handoff: Jev cheaply buckets a big corpus, then a smart model writes, analyzes, or acts [03:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=228s).
- Don't trust it blind: build a golden dataset (~100 labeled cases) and eval Jev against smarter models for the best balance of accuracy, cost, and speed [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s).

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=0s) 12 Jev Use Cases

- Nate opens saying Jev is "everywhere" and will change how AI automations are built; he tested it on 12 use cases and compared speed and cost against other models [00:00](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=0s).
- Two live builds teased: a Chrome extension that labels X posts as breaking / golden nugget / AI slop in real time (he admits it wasn't doing well in the first hour), and a "Jev trader" that predicts every second whether Bitcoin goes up, down, or stays and places trades, because the model is so good at quick decisions [00:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=7s).

### [00:41](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=41s) What Jev Is

- Core framing: Jev is an AI that makes decisions but writes nothing, outputs no tokens, and can't be conversed with [00:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=48s).
- It was announced by Diogo, described as a co-inventor of ChatGPT, who spent about two years building a new training method, RLCD (reinforcement learning for calibrated decisions), published on TypeSafe's blog [00:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=58s). (Present "co-inventor of ChatGPT" as the video's claim, not established fact.)
- Access: join the TypeSafe AI waitlist (approval in a few hours), or use it now through Vercel's AI Gateway or OpenRouter [01:14](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=74s).
- How it differs from a chat model: instead of reading, reasoning, and emitting text, Jev returns decisions. His support-ticket example: urgent? 99% confidence yes; which team? technical; how frustrated? 1 out of 2 on the frustration scale. You define the decision rules and criteria [01:32](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=92s).
- Three decision types: yes/no (the captions render it "null" — the canonical TypeSafe name is Noul), pick-one is a "choice", and the third is a numeric "score" [02:13](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=133s).

### [02:40](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=160s) Speed, Cost & Limits

- The traction driver: Diogo's claim that Jev is 20–200× faster and 40–400× cheaper, with output tokens free [02:41](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=161s). (Vendor figures, not independently benchmarked.)
- Nate's speed test against placeholder models "Terra," "Luna," and "Sol" shows Jev far faster, but he stresses it was one very quick test and doesn't prove "Terra is always faster than Luna" [02:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=170s).
- On cost, at thousands of decisions/day Jev is provably cheaper, but you must confirm quality is the same to justify the savings [03:10](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=190s).
- What Jev cannot do: write, summarize, find themes, or do deep analysis; it only outputs decisions [03:29](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=209s).
- The small-context limit: 64,000 input tokens, versus roughly a million for models like Claude or GPT [03:37](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=217s).
- Recommended pattern: cheaply sort, say, 5,000 YouTube comments into buckets (needs reply / stuck / wants to buy) with Jev, then hand the narrowed set to a smarter model (ChatGPT) to analyze themes or draft replies, so you don't pay a slow, expensive model for bulk categorization [03:48](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=228s).
- Jev is not a frontier model, "not even in the same bucket" as the placeholder frontier models Astra or Fable; it's a different category [04:21](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=261s).
- When to use it: thousands of items, a corpus of data, classification/decision workflows at scale, or fast real-time decisions. Stay with ChatGPT for a handful of items, understanding why, brainstorming, or chatting [04:27](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=267s). → [[Choosing a Claude Model]]

### [05:28](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=328s) Email Classification Benchmark

- Playground demo on emails with seven rules: invoice/receipt, brand deal, scammer/phishing (all yes/no), email type (category), urgency and sponsor fit (scores) [05:28](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=328s).
- Benchmark over 1,000 emails across all seven rules: Jev unparallelized ran ~70 seconds for 9¢; the chat model "GPT 5.6 Luna" took ~5 minutes for 62¢; Jev after back-end optimization (parallel, bigger payloads) ran in 6 seconds for 9¢ [05:52](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=352s).
- Nate concedes Luna can also parallelize, but says it won't match 6s for 1,000 emails across seven categories [06:38](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=398s).
- Single-rule yes/no example (invoice/receipt): you write the question, define what counts as "yes," and call it yes when Jev is at least 50% confident; it returned in 4 seconds for 5¢, landing no on 763 and yes on 237 of the 1,000 [06:56](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=416s).
- Choice example: email type (notification / newsletter / billing / opportunity), where you must define each option, a standard classification [07:32](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=452s).
- Score example: sponsor fit rated lowest-to-highest, with 942 coming back low and no strong fits; a second urgency score averaged 2.8 out of 5 [07:45](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=465s).
- Benchmark summary: in the first run Luna cost 12× the cost and 46× the time of Jev, and that's only Luna; "Terra" and "Sol" would be far more expensive [08:22](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=502s).

### [08:33](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=513s) Comments, Communities & Automations

- YouTube comments: classify thousands by comment type, worth-a-reply, gives-a-video-idea, sentiment, and question difficulty; Jev did 1,000 in 5 seconds for 5¢ [08:33](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=513s).
- Jev console stat: 85¢ of total spend across almost 20,000 requests, illustrating how cheap high request volume is versus other models [08:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=538s).
- Skool posts: custom categories for question type, needs help, needs team answer, churn risk, member experience level, and testimonial strength [09:12](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=552s).
- The bigger idea: move from a playground view into real automations that update a database on every new post, comment, CRM entry, or form lead. Speed may matter less in production, but cost compounds at thousands of requests, which is where "AI economics and model routing" pays off [09:26](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=566s).

### [10:00](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=600s) X Feed Chrome Extension

- X-feed classifier: pulls posts from his feed and labels on-topic, category, breaking news, and video-idea potential [10:00](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=600s).
- Live build "Jev Judged": on a hard refresh of X, each post gets a badge (slop / breaking / golden nugget). Jev powers the back end, reading and classifying posts in near-real-time as they hit the screen to keep him focused; the reaction is "basically instant," a case where speed genuinely matters [10:15](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=615s).

### [10:57](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=657s) Meetings & Video Clips

- Meetings: analyze transcripts as they land in Fireflies or Granola, categorizing call type, whether decisions were made, and whether action steps exist. If many calls lack next steps with ownership and timelines, use that data to change how you run calls [10:57](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=657s).
- Key nuance: Jev on its own doesn't analyze for you, but with strategically designed questions (categories + scores) you can make the aggregated data "tell a story." It can't read thousands of transcripts and surface common themes; you compose the narrative from the per-question outputs (tension level, waiting-on-Nate, revenue relevance) [11:19](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=679s).
- Video clips: have a smart model ("Astra") split videos into clips, then Jev scores each, postable on its own? hook strength? clip type? needs screen? quotable line? to surface repost-worthy clips [11:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=718s).
- Recurring thesis: take a big corpus and, instead of paying more or waiting longer, use the right questions to have Jev do the work, then build it into back-end automations as throughput rises [12:26](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=746s).

### [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s) Evals & More Use Cases

- Strong caveat: don't just plug in Jev and trust it. Run evals, a golden dataset of ~100 cases with 100 correct answers, and run Jev, Opus, and "Sol" through it to see which model gives the best balance of accuracy, cost, and (if relevant) speed [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s). → [[Verification Before Done]]
- More use cases: contract vetting (risk type, clause type, custom questions); jobs/leads (red flags, lead quality, next steps); a brain-dump router (talk into your phone; Jev classifies ideas vs tasks vs journals, deadlines, priority, life area) [13:13](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=793s).
- Highlighted best example: customer support, routing emails by sentiment, urgency, and category, called a huge game-changer because support is many fast decisions and Jev is fast and cheap at decisions [13:52](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=832s).

### [14:13](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=853s) Real-Time Trading & Handoffs

- Live build "Jev trader," a paper-trading POC, explicitly "not very vetted" with "a lot wrong with it." Every second Jev predicts Bitcoin up / unclear / down, with confidence scores jumping each second, and decides when to buy or sell [14:13](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=853s).
- Limit: trading fees are far more expensive than Jev's decision cost, raising the question of how much profit is needed to make it worthwhile [14:44](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=884s).
- Cost comparison: running these per-second decisions 24/7 costs Jev about $2/day, whereas "Sol," "Opus," and "Fable" would cost significantly more [14:55](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=895s).
- Model-handoff pattern: he's seen people have Jev play video games and do browser use, but you must plan the handoff. In browser use Jev couldn't actually type; it makes decisions, then routes to a different model better at controlling the browser [15:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=907s).
- Adoption path: build dashboards/automations with Jev on the back end for things you care about, get a return, then later extend workflows with other models [15:28](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=928s).

### [15:45](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=945s) Final Thoughts

- Closing: all 12 examples lived in "the realm of classification"; he hopes viewers learn to ask the right questions and work Jev into their own workflows to make sense of their data [15:45](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=945s).

## Caveats & disagreements

This is an honest review, and the caveats are load-bearing.

- **Vendor speed/cost claims are secondhand.** "20–200× faster, 40–400× cheaper, output tokens free" comes from Diogo/TypeSafe, not an independent benchmark. Nate calls his own speed test "just one very quick test" that doesn't prove any placeholder model is always faster than another [02:41](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=161s), [02:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=170s).
- **The benchmark isn't apples-to-apples on parallelism.** Jev's fast 6s run used an optimized parallel back end while the initial Luna comparison did not; Nate concedes Luna can parallelize too. The 12×-cost / 46×-time figure comes from the non-optimized run [06:38](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=398s), [08:22](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=502s).
- **Quality is assumed, never measured.** Nate repeatedly stresses cost savings only matter if accuracy matches, and that you must eval, but Jev's actual accuracy versus chat models is never quantified in the video [03:10](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=190s), [12:50](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=770s).
- **Jev can't reason or analyze.** Any "insight" is composed by the human through clever question design; Jev cannot surface themes or explain "why" [03:29](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=209s), [11:19](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=679s).
- **The trading POC is explicitly unreliable.** "Not very vetted," "a lot wrong with it," and trading fees dwarf the model cost, so profitability is unproven. A demo, not a strategy, and not financial advice [14:13](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=853s), [14:44](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=884s).
- **Browser use needs a second model.** Jev couldn't type or act; it decides, then hands off to a model that controls the browser, so "Jev does X autonomously" claims elsewhere should be read with that caveat [15:07](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=907s).
- **Anonymized competitor names** ("Terra," "Luna," "Sol," "Astra," "Fable," "Opus," "GPT 5.6 Luna") make the comparisons hard to reproduce or independently check. See Transcript notes.
- **Commercial framing.** The video sits alongside a free lead magnet and community plug; the enthusiasm is genuine but promotional, though the review does foreground real limits.

## Build from this

- [[Build a Jev Classification Pipeline]] — the email-benchmark and automation-wiring patterns generalize into a production classification pipeline: define yes/no, choice, and score rules over a corpus, run in parallel, write results to a database on every new event, and eval against a golden dataset before trusting it.

## Resources mentioned

- **Jev** / **TypeSafe (TypeSafe AI)** — the reviewed model and the company behind it; blog hosts the RLCD writeup; waitlist for access [00:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=58s).
- **Vercel AI Gateway** and **OpenRouter** — alternative ways to access Jev without the waitlist [01:14](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=74s).
- **Jev console** — dashboard showing spend and requests (85¢ / ~20k requests) [08:58](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=538s).
- **Fireflies, Granola** — meeting-transcription tools feeding the meetings use case [10:57](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=657s).
- **Skool** — his AI Automation Society community, source of the "Skool posts" use case and the free first-client SOP [09:12](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=552s).
- **Comparison LLMs (anonymized placeholders):** "Terra," "Luna," "Sol," "Astra," "Fable," "Opus," "GPT 5.6 Luna," used as speed/cost/accuracy baselines and as the generative half of handoffs.

## Beyond the source

- Nate's yes/no type (captioned "null") is TypeSafe's **Noul** primitive: a yes/no question returning the probability of "yes" as 0–1, with no separate confidence value. — [TypeSafe docs / SDK naming, per this batch's canonical facts]

## Transcript notes

Non-obvious caption corrections made silently in the prose above:

- **"a null"** [02:14] — the yes/no decision type. This is the auto-caption of TypeSafe's **Noul** primitive; "null" is a mishearing. (Nate never actually says "bool".)
- **"TypeSafety's blog"** [01:13] — should be **TypeSafe** (the company; also "TypeSafe AI").
- **"school posts"** [09:12] — should be **Skool posts** (the Skool community platform).
- **"Soul"** [12:51], [15:04] vs **"Sol"** [02:52], [08:29] — the same placeholder model; normalized to **Sol**.
- **Placeholder model names** (**Terra, Luna, Sol, Astra, Fable, Opus, "GPT 5.6 Luna"**) are deliberate codenames/obfuscations, not caption errors; they are not "corrected" to real names. Only **Opus** likely denotes Claude Opus, and even that is inferred, not stated.

## Related

- [[Jev]]
- [[System 1 and System 2 AI Models]]
- [[Verification Before Done]]
- [[Choosing a Claude Model]]
- [[Build a Jev Classification Pipeline]]
- [[Nate Herk]]
