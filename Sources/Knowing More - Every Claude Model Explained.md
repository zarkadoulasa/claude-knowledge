---
type: source
title: "Every Claude Model Explained in 7 Minutes"
creator: "Knowing More"
channel: "Knowing More"
url: https://www.youtube.com/watch?v=BJauPEH_9OU
video_id: BJauPEH_9OU
published: 2026-05-07
duration: "7:25"
ingested: 2026-09-15
topics: [Claude models, model selection, Haiku, Sonnet, Opus, Mythos, Project Glasswing, context window, usage limits, benchmarks]
tags: [source/youtube, topic/models, topic/context, topic/claude-code, topic/subagents]
---

# Knowing More - Every Claude Model Explained

> **Creator:** Knowing More (faceless explainer channel) · **Published:** 2026-05-07 · **Length:** 7:25 · [Watch on YouTube](https://www.youtube.com/watch?v=BJauPEH_9OU)

> [!warning] Dated lineup
> This video was recorded in May 2026, and every model version it names had been superseded by 2026-09-15. This note records what the video said, with timestamps. The verified current lineup, prices and switching mechanics are under **Beyond the source**.

## TL;DR

A narrated explainer with no demos, screen recordings or prompts. It sorts the Claude family into four tiers as they stood in May 2026:

- **Haiku:** the fast, cheap tier for quick and repetitive work.
- **Sonnet 4.6:** the everyday default.
- **Opus 4.7:** the expensive flagship for hard problems.
- **Mythos:** a withheld model reachable only through Project Glasswing.

Its routing rule is Haiku for quick and batch tasks, Sonnet for everything else, and Opus for hard engineering, financial modelling and decisions that are hard to reverse. If Sonnet struggles, move up to Opus. It then lists Claude's downsides: slowness, tight usage limits, heavy token use, no image or video generation, and overcaution. For blunt answers the narrator uses Grok instead.

It works as a quick picture of the tiers, and the "default, then escalate" habit is sound. Beyond that it's thin. The tone is hype-heavy, and it never explains how to switch models or how to tell when Sonnet is "struggling". It also files a 2025 Opus 4 example under Opus 4.7, and every version it names is now out of date.

## Key takeaways

- **Claude is a family of models, not one AI.** The tiers differ in size and speed. The video claims most people either use the wrong one or don't know the others exist ([00:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=4s), [00:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=9s)). See [[Choosing a Claude Model]].
- **Haiku is for speed and volume.** Use it for quick summaries, pulling key facts from documents, simple questions, and batch or repetitive jobs ([01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s), [01:41](https://www.youtube.com/watch?v=BJauPEH_9OU&t=101s)). It acts without deliberating ([01:51](https://www.youtube.com/watch?v=BJauPEH_9OU&t=111s)) but lacks depth on hard engineering or nuanced analysis ([01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s), [01:59](https://www.youtube.com/watch?v=BJauPEH_9OU&t=119s)).
- **Sonnet is the default.** The video presents it as the daily workhorse for coding, serious writing, whole-document analysis and business operations ([02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s)). New users should start there ([03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s)).
- **The "90%" heuristic.** Use Sonnet for about 90% of work and Opus only when a decision is hard to reverse. The video credits this to a "community" view it calls unanimous but never sources ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s), [02:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=175s)).
- **Escalate when Sonnet struggles.** Move the task to Opus ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)). The video never says how to recognise struggling or how to switch; [[Route Tasks to the Right Claude Model]] covers that from the docs.
- **Opus costs you in money and in usage limits.** The video calls it very expensive and token-hungry, and jokes that you can hit your rate limit within three prompts ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s), [04:18](https://www.youtube.com/watch?v=BJauPEH_9OU&t=258s), [04:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=260s)). See [[Context Window Management]] and [[Context Hygiene Routine]].
- **It sells the 1M context window as roughly 2,000–3,000 pages in a single conversation** ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s), [02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)), yet later complains that Claude burns through tokens very fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)). Having room isn't a reason to fill it; see Caveats and [[CLAUDE.md as a Router]].
- **Mythos was held back for security reasons.** Only Project Glasswing partners had access, because it finds and exploits software vulnerabilities better than human experts ([05:10](https://www.youtube.com/watch?v=BJauPEH_9OU&t=310s), [05:18](https://www.youtube.com/watch?v=BJauPEH_9OU&t=318s), [05:42](https://www.youtube.com/watch?v=BJauPEH_9OU&t=342s)). This is dated; see Caveats.
- **Named downsides:**
  - Slow ([06:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=361s)).
  - A free-tier usage wall after two or three prompts ([06:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=364s)).
  - No image or video generation ([06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s)).
  - Overcautious on edgy but legitimate requests ([06:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=382s)).
- **The final routing rule:**
  - Haiku for quick, batch and repetitive work ([06:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=410s)).
  - Sonnet for everything else ([06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s)).
  - Opus for hard engineering, financial modelling and decisions you can't easily reverse ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)).
  - Mythos isn't an option ([07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s)).

## The models at a glance (as the video presents them)

| Tier | How the video frames it | Version and specs it quotes | Use it for | Limits it names |
|---|---|---|---|---|
| **Haiku** | "The speedster": smallest, lightest, fastest, and the tier users forget ([01:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=81s), [01:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=89s)) | No version or specs given | Quick summaries, pulling key information, simple questions, batch and repetitive work ([01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s), [06:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=410s)) | Struggles with depth: hard engineering, nuanced analysis. An intern, not the one leading the meeting ([01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s), [02:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=124s)) |
| **Sonnet** | "The reliable workhorse", the narrator's daily model, which thinks about the approach before acting ([02:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=135s), [03:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=184s)) | Sonnet 4.6, Feb 2026, 1M-token context, framed as ~2,000–3,000 pages ([02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s), [02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s)) | Senior-level coding, serious writing, whole-document analysis, an "operations brain". Default for ~90% of work and the starting model for newcomers ([02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s), [02:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=175s), [03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s)) | None named. The implied limit is that Opus takes over when Sonnet struggles ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)) |
| **Opus** | "The big dog", a flagship most users haven't tried because it's paid ([03:17](https://www.youtube.com/watch?v=BJauPEH_9OU&t=197s), [03:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=204s)) | Opus 4.7, Apr 2026. 1M context, $5 per million input tokens. 87.6% on SWE-bench, 94.2% on GPQA Diamond ([03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s), [03:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=215s), [03:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=229s), [03:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=238s)) | Hard engineering, financial modelling, decisions that are hard to reverse, anything Sonnet struggles with. Its long-run example is a seven-hour Rakuten job ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s), [07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)) | Very expensive and token-hungry, quick to hit rate limits, wordy about its caution ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s), [04:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=267s)) |
| **Mythos** | Nicknamed "Tai Lung", the "destroyer of worlds". Unreleased and considered too dangerous for the public ([04:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=292s), [05:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=306s)) | 64.7% on Humanity's Last Exam. Found thousands of high-severity bugs in major operating systems and browsers ([05:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=322s), [05:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=336s)) | Nothing: only a handful of partners get it, through Project Glasswing ([05:10](https://www.youtube.com/watch?v=BJauPEH_9OU&t=310s), [07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s)) | Kept locked away until safeguards are strong enough ([05:54](https://www.youtube.com/watch?v=BJauPEH_9OU&t=354s)) |

*Every row reflects May 2026. The matching September 2026 table is under Beyond the source.*

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=BJauPEH_9OU&t=0s) How Claude Works

- **The opening claim.** Most people think of Claude as one AI, but it's a family of models of different sizes and speeds ([00:00](https://www.youtube.com/watch?v=BJauPEH_9OU&t=0s), [00:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=4s)). Most people who have heard of Claude, it says, are on the wrong model for their needs or unaware the others exist ([00:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=9s)).
- **The lineup covered:** Haiku, Sonnet and Opus, plus Mythos, which Anthropic won't release publicly ([00:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=16s), [00:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=20s)).
- **Who makes it.** Anthropic was started by researchers who left OpenAI because they thought AI was moving too fast and too recklessly ([00:26](https://www.youtube.com/watch?v=BJauPEH_9OU&t=26s), [00:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=29s)). In the video's telling, its central aim is AI that's safe, not merely powerful ([00:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=36s)).
- **The name.** Claude is named after Claude Shannon, the American mathematician called the father of information theory ([00:42](https://www.youtube.com/watch?v=BJauPEH_9OU&t=42s), [00:44](https://www.youtube.com/watch?v=BJauPEH_9OU&t=44s)). The video credits him with the groundwork for how computers process language ([00:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=50s)).
- **How it works.** Like every AI model, Claude predicts the next token, one at a time ([00:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=55s)). All its impressive output, from code to explanations, comes down to being very good at that one prediction ([01:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=62s)).
- **What sets it apart is training** ([01:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=68s)). Anthropic uses constitutional AI ([01:12](https://www.youtube.com/watch?v=BJauPEH_9OU&t=72s)). Rather than repeating prohibitions endlessly, it gives the model a set of principles, a moral framework to reason against ([01:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=75s)). That brief contrast is all the video says about it.

### [01:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=82s) Claude Haiku

- The video nicknames Haiku "the speedster" and calls it the model most Claude users forget about ([01:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=81s), [01:25](https://www.youtube.com/watch?v=BJauPEH_9OU&t=85s)).
- It's the smallest, lightest and fastest model in the family ([01:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=89s)), built for speed, for volume, and for tasks that need an answer immediately ([01:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=92s)).
- **Use cases:**
  - Quick summaries, pulling key information out of documents, and answering simple questions ([01:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=96s)).
  - Batch tasks, and any repetitive job you'd hate to do by hand ([01:41](https://www.youtube.com/watch?v=BJauPEH_9OU&t=101s)).
- **How it behaves.** Ask it to do something and it does it, with no overthinking ([01:46](https://www.youtube.com/watch?v=BJauPEH_9OU&t=106s), [01:51](https://www.youtube.com/watch?v=BJauPEH_9OU&t=111s)).
  - *This note's connection, not the video's:* a model that doesn't deliberate is a risky pick for tasks where [[Agent Laziness]] (shallow work, declaring done too early) is already a concern. The video never discusses agents.
- **Its limit is depth** ([01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s)). Hand it something genuinely complex, like a hard engineering problem or nuanced analysis, and it struggles ([01:59](https://www.youtube.com/watch?v=BJauPEH_9OU&t=119s), [02:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=124s)).
- **Analogy.** Haiku is like an intern who handles emails, scheduling and copy-paste work while the senior team does what matters ([02:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=124s), [02:07](https://www.youtube.com/watch?v=BJauPEH_9OU&t=127s)). It's good at its job, but don't ask it to lead the meeting ([02:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=133s)).

### [02:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=136s) Claude Sonnet

- The video calls Sonnet "the reliable workhorse". The narrator uses it every day and says it still amazes them ([02:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=135s), [02:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=141s)).
- **Version quoted:** Sonnet 4.6, described as current and released in February 2026 ([02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s)).
- **Context window:** 1 million tokens, which the video equates to about 2,000–3,000 pages of text in one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s), [02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)). It says nothing about the cost of filling that window or how quality holds up.
- **Who uses it, and for what** ([02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s)–[02:45](https://www.youtube.com/watch?v=BJauPEH_9OU&t=165s)):
  - Developers, for senior-level coding.
  - Writers, for serious content.
  - Researchers, to analyse whole documents.
  - Businesses, as an "operations brain".
- **The community heuristic.** The video says the community's view is unanimous, but names no source ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s)):
  - Sonnet is the default, and Opus is only for decisions you can't easily undo ([02:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=169s), [02:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=173s)).
  - Sonnet handles roughly 90% of work, and Opus is for when it really matters ([02:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=175s)).
- **How it behaves.** Unlike Haiku, Sonnet first works out the best way to approach the task ([03:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=181s), [03:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=184s)). *(This note's link:* you can enforce that instinct on any model with [[Plan Before Executing]].)
- **Pushback rather than flattery.** The video says Claude won't praise a half-baked idea and will call you out ([03:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=188s), [03:10](https://www.youtube.com/watch?v=BJauPEH_9OU&t=190s)). It gives no example.
- **Where to start.** If you've never used Claude, start with Sonnet ([03:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=195s)).

### [03:18](https://www.youtube.com/watch?v=BJauPEH_9OU&t=198s) Claude Opus

- The video calls Opus "the big dog". Most users have never touched it, not for lack of interest but because it costs money ([03:17](https://www.youtube.com/watch?v=BJauPEH_9OU&t=197s), [03:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=200s), [03:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=204s)).
- **Version quoted:** Opus 4.7, released April 2026 and described as Anthropic's flagship ([03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)).
- **Specs quoted:** 1M tokens of context, with input priced at $5 per million ([03:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=212s), [03:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=215s)). The output price isn't mentioned.
- **Benchmarks quoted:**
  - **SWE-bench**, explained as checking whether a model can repair genuine bugs taken from actual GitHub repositories, as an engineer would: 87.6% ([03:38](https://www.youtube.com/watch?v=BJauPEH_9OU&t=218s), [03:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=229s)).
  - **GPQA Diamond**, described as questions hard enough to trouble PhD scientists: 94.2% ([03:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=232s), [03:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=238s)).
- **Long-running example.** Engineers at Rakuten ran Opus 4 for seven straight hours to refactor an entire open-source codebase, and it never lost focus ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s), [04:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=246s)). The narration really does say "Opus 4", in the middle of the Opus 4.7 section. The details differ from the published case study; see Caveats.
- **Escalation rule.** When Sonnet starts struggling, escalate to Opus, which the video says will simply solve it ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s), [04:11](https://www.youtube.com/watch?v=BJauPEH_9OU&t=251s)).
- **Cost warning.**
  - Opus is incredibly expensive and "consumes tokens like a camel" ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s), [04:18](https://www.youtube.com/watch?v=BJauPEH_9OU&t=258s)).
  - The narrator claims three prompts can exhaust your rate limit, depending on "the weather outside" ([04:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=260s)). The weather line marks it as a joke, not a measurement.
  - It takes the most money out of your wallet ([04:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=264s)).
- **Verbosity joke.** Developers joke that Opus writes three paragraphs about why it's being careful before it answers ([04:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=267s), [04:30](https://www.youtube.com/watch?v=BJauPEH_9OU&t=270s)).
- **Verdict.** For genuinely hard problems, nothing else comes close ([04:37](https://www.youtube.com/watch?v=BJauPEH_9OU&t=277s)).
- An engagement ask follows: comment which models you've tried, and like the video ([04:39](https://www.youtube.com/watch?v=BJauPEH_9OU&t=279s)).

### [04:51](https://www.youtube.com/watch?v=BJauPEH_9OU&t=291s) Claude Mythos / Fable

- The narrator introduces Mythos by the nickname "Tai Lung", "the destroyer of worlds". The name belongs to a Kung Fu Panda villain, which the video doesn't explain (this note's gloss) ([04:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=292s), [04:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=295s)).
- **Availability.** Mythos isn't available to viewers, to the narrator or to the public ([04:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=298s)).
- **What it is.** Anthropic's unreleased "super AI", so capable at reasoning and software engineering that it's considered dangerous to release publicly ([05:03](https://www.youtube.com/watch?v=BJauPEH_9OU&t=303s), [05:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=306s)).
- **Access.** Only a handful of partners can use it, through a restricted programme called Project Glasswing ([05:10](https://www.youtube.com/watch?v=BJauPEH_9OU&t=310s), [05:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=315s)).
- **Why it's restricted.**
  - It spots security flaws in software more quickly than any human specialist ([05:18](https://www.youtube.com/watch?v=BJauPEH_9OU&t=318s)).
  - Sweeping the major operating systems and browsers, it turned up thousands of serious flaws, some hidden for decades ([05:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=322s), [05:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=327s)).
- **Benchmark.** Mythos scored 64.7% on Humanity's Last Exam, which the video calls the hardest knowledge benchmark ever designed ([05:31](https://www.youtube.com/watch?v=BJauPEH_9OU&t=331s), [05:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=336s)). It adds that the best public models aren't close ([05:40](https://www.youtube.com/watch?v=BJauPEH_9OU&t=340s)).
- **Internal testing.** In early tests it read code, found bugs and exploited systems better than the most skilled human hackers ([05:42](https://www.youtube.com/watch?v=BJauPEH_9OU&t=342s), [05:45](https://www.youtube.com/watch?v=BJauPEH_9OU&t=345s)).
- **Status.** You can't use it for now. It stays locked away until Anthropic has safeguards robust enough to keep it in check ([05:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=349s), [05:54](https://www.youtube.com/watch?v=BJauPEH_9OU&t=354s)).
- **Fable is never mentioned in the narration.** Only the chapter title in the description names it. Most likely the description was edited after Fable launched, but that's an inference.

### [05:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=358s) Harsh Truth about Claude

- **Slow**, sometimes painfully so ([05:58](https://www.youtube.com/watch?v=BJauPEH_9OU&t=358s), [06:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=361s)).
- **Usage limits.** On the free tier you can run into a usage wall within two or three prompts ([06:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=364s), [06:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=366s)). Most casual ChatGPT or Gemini users, the video says, never see a limit at all ([06:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=369s)).
- **Token burn.** Claude goes through tokens very fast ([06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)).
- **No image or video generation.** The video calls Claude text and code, "full stop" ([06:16](https://www.youtube.com/watch?v=BJauPEH_9OU&t=376s), [06:19](https://www.youtube.com/watch?v=BJauPEH_9OU&t=379s)).
- **Overcaution.** Claude is more hesitant than ChatGPT or Gemini about anything slightly edgy, even when the request is entirely legitimate ([06:22](https://www.youtube.com/watch?v=BJauPEH_9OU&t=382s), [06:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=387s), [06:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=392s)).
- **The narrator's workaround.** For a blunt answer with no ceremony, they use Grok, whose personality they prefer for that ([06:34](https://www.youtube.com/watch?v=BJauPEH_9OU&t=394s), [06:37](https://www.youtube.com/watch?v=BJauPEH_9OU&t=397s)). Claude's carefulness is sometimes the last thing you need ([06:43](https://www.youtube.com/watch?v=BJauPEH_9OU&t=403s)).
- None of these limitations comes with numbers, sources or tips for working around them.

### [06:46](https://www.youtube.com/watch?v=BJauPEH_9OU&t=406s) Which Claude Model Should You Use?

- **Haiku:** quick tasks, fast answers, batch work and repetitive jobs, because it's fast and cheap ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s), [06:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=410s), [06:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=412s)).
- **Sonnet:** "literally everything else", the sweet spot between intelligence and speed ([06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s), [07:00](https://www.youtube.com/watch?v=BJauPEH_9OU&t=420s)).
- **Opus:** worth paying for when the work is hard engineering, financial modelling, or a decision you can't easily reverse ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s), [07:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=424s)).
- **Mythos:** nobody gets that choice, the narrator included ([07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s)).
- The video ends with a one-line recap and a request to subscribe ([07:12](https://www.youtube.com/watch?v=BJauPEH_9OU&t=432s), [07:17](https://www.youtube.com/watch?v=BJauPEH_9OU&t=437s)).

## Caveats & disagreements

### Out of date as of 2026-09-15

Verified details and links are under Beyond the source.

- **Sonnet 4.6** ([02:24](https://www.youtube.com/watch?v=BJauPEH_9OU&t=144s)) is no longer the default. Claude Sonnet 5 (2026-06-30) replaced it as the default on the Free and Pro plans.
- **Opus 4.7** ([03:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=209s)) was followed by Opus 4.8 (2026-05-28) and Claude Opus 5 (2026-07-24).
- **"You can't use Mythos"** ([05:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=349s), [07:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=429s)) is no longer the whole story.
  - The Mythos-class model became public with safeguards, first as Claude Fable 5 (2026-06-09) and then Claude Fable 5.1 (2026-09-01).
  - Mythos 5.1 is the same model with different safeguards, and access to it is still restricted.
- **Haiku** gets no version number in the video ([01:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=81s)). The current one is Haiku 4.5.
- **"The best public models aren't close" on Humanity's Last Exam** ([05:40](https://www.youtube.com/watch?v=BJauPEH_9OU&t=340s)) no longer holds. A third-party leaderboard updated 2026-09-14 puts Fable 5.1 (65%) and Opus 5 (64.7%) level with or above Mythos Preview's 64.7%. It doesn't say whether its runs used tools, so treat the comparison as rough.

### Current official guidance departs from the video's default

- **Sources disagree on the default model.**
  - This video says to default to Sonnet for about 90% of work and use Opus only for irreversible or very hard work ([02:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=175s), [06:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=415s)).
  - Anthropic's API docs (checked 2026-09-15) instead suggest starting with Opus 5 for most workloads. They add that tuning the effort setting is often a better lever than switching models.
  - Claude Code is split. Its alias descriptions still call Sonnet the daily-coding model and Opus the complex-reasoning model. The account default, though, is now Opus 5 on most plans, with Sonnet 5 only on Pro and Team Standard seats.
  - Both positions are recorded here, and neither is settled. Test on your own tasks; see [[Choosing a Claude Model]].
- **No practical switching guidance.** The video covers none of these:
  - How to change models in an app or in Claude Code.
  - API model IDs.
  - Effort or thinking settings.
  - Per-subagent models.
  - How to tell when Sonnet is "struggling" ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)).

  [[Route Tasks to the Right Claude Model]] fills that gap from the docs.

### Hype and unsupported claims

- **Presented as fact, but unsourced:**
  - A "unanimous" community view ([02:47](https://www.youtube.com/watch?v=BJauPEH_9OU&t=167s)).
  - "Doesn't flatter you", with no example ([03:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=188s)).
  - Mythos beating the best human hackers, stated without citing the source ([05:42](https://www.youtube.com/watch?v=BJauPEH_9OU&t=342s)).
- **Hype rather than information:** "destroyer of worlds" ([04:55](https://www.youtube.com/watch?v=BJauPEH_9OU&t=295s)) and "blows my mind" ([02:21](https://www.youtube.com/watch?v=BJauPEH_9OU&t=141s)).
- **Jokes that sound like measurements:**
  - A three-prompt rate limit "depending on the weather" ([04:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=260s)).
  - A free-tier wall after two or three prompts ([06:04](https://www.youtube.com/watch?v=BJauPEH_9OU&t=364s)).

  In reality, usage depends on conversation length, features, model and effort, and usage in claude.ai, Claude Code and the desktop app all counts toward one shared limit.
- **Subjective comparisons.** The usage-limit and caution comparisons with ChatGPT and Gemini, and the Grok preference ([06:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=369s), [06:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=387s), [06:37](https://www.youtube.com/watch?v=BJauPEH_9OU&t=397s)) are personal impressions, not measurements.

### Figures that need qualifying

- **SWE-bench.** The 87.6% figure ([03:49](https://www.youtube.com/watch?v=BJauPEH_9OU&t=229s)) is from SWE-bench Verified. Opus 4.7's score on the harder SWE-bench Pro was 64.3%.
- **Humanity's Last Exam.** Mythos Preview's 64.7% ([05:36](https://www.youtube.com/watch?v=BJauPEH_9OU&t=336s)) is the with-tools score. Without tools it scored 56.8%.
- **Opus pricing.** The video gives only the input price ([03:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=215s)). Output cost $25 per million tokens, and Opus 4.7's new tokenizer can turn the same text into up to about 1.35× as many tokens.
- **The Rakuten example is misplaced** ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s)).
  - The video names Opus 4 but places it in the Opus 4.7 section.
  - Anthropic's May 2025 Claude 4 launch post credits Opus 4 with a seven-hour open-source refactor at Rakuten.
  - Claude's own Rakuten case study says it was Claude Code *implementing* an activation-vector extraction method in vLLM, not refactoring "an entire" codebase.
- **"Text and code, full stop"** ([06:19](https://www.youtube.com/watch?v=BJauPEH_9OU&t=379s)) oversimplifies. Current Claude models accept images as input. What they don't do is generate images or video.
- **The Glasswing bug count checks out, and has grown.** "Thousands of high-severity bugs" ([05:27](https://www.youtube.com/watch?v=BJauPEH_9OU&t=327s)) matches Anthropic's launch page directly: it uses the same high-severity wording for flaws that include some in every major operating system and web browser. Separately, the page reports thousands of zero-day vulnerabilities, many of them critical. A May 2026 update reported more than ten thousand high- or critical-severity vulnerabilities found with about 50 partners in the first month.
- **The context window depends on where you use it.** The video gives 1M for Opus 4.7 ([03:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=212s)), but the Help Center lists 500K for Opus 4.7 and Sonnet 4.6 in chat on paid plans. The 1M figure applies in Claude Code, where Opus 1M on Pro and Sonnet 4.6 1M on any paid plan need usage credits enabled, and to Opus 4.7 in Cowork. At launch, Sonnet 4.6's 1M window was a beta.
- **Chapter title.** "Claude Mythos / Fable" appears in the description, but the narration never mentions Fable ([04:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=292s)).
- **Promotional content.** Engagement asks (comment, like, subscribe) at [04:39](https://www.youtube.com/watch?v=BJauPEH_9OU&t=279s) and [07:17](https://www.youtube.com/watch?v=BJauPEH_9OU&t=437s). No sponsor or affiliate content.

### Tensions with other vault notes

- **[[CLAUDE.md as a Router]] vs "load thousands of pages".**
  - This video pitches the 1M window as fitting 2,000–3,000 pages in one conversation ([02:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=149s), [02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)).
  - [[Nate Herk - Every Level of a Claude Second Brain]] argues that Claude shouldn't read your whole project, because the time and token cost make routing the better design ([05:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)).
  - This video's own complaints about token burn and rate limits ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s), [06:14](https://www.youtube.com/watch?v=BJauPEH_9OU&t=374s)) back Herk's reasoning.
  - Both are recorded here. A large window gives you capacity, but that's no reason to fill it. See [[Context Window Management]].
- **[[Design for Retrieval]] gains a cost dimension.**
  - Herk designs storage by working backwards from the question ([02:29](https://www.youtube.com/watch?v=DTCyvo6cC54&t=149s)).
  - This video adds another decision: which model runs each step. Quick and batch work goes to Haiku ([06:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=410s)) and hard work goes to Opus ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)).
  - That's a refinement, not a contradiction. Pairing the two ideas is this note's, not either creator's.
- **[[Context vs Connections]] still applies to big windows.**
  - Herk's one-year test for what to ingest ([27:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1667s)) is about noise, not capacity.
  - Nothing in this video's pitch for the context window ([02:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=152s)) weakens that test. *(This note's synthesis.)*
- **Model cost matters for [[Always-On Brain OS]].**
  - Herk's Level 5 brain is constantly syncing and refreshing ([25:45](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1545s)).
  - Combined with this video's warning that Opus exhausts limits ([04:13](https://www.youtube.com/watch?v=BJauPEH_9OU&t=253s)), jobs that run constantly in the background are the natural home for the cheap, fast tier ([06:50](https://www.youtube.com/watch?v=BJauPEH_9OU&t=410s)). *(This note's synthesis, not either creator's.)*
- **Disagreements with this batch's other sources** (Simon Pittman, Nate Herk's 32 tricks, the Coding Sloth, Ras Mic) on the default tier, Opus and limits, big windows and how much the model matters are recorded, with timestamps, under Where sources disagree in [[Choosing a Claude Model]] and [[Context Window Management]].

## Build from this

*These build ideas are this note's own. The video contributes only its tiering rule. Current model IDs, commands and prices are under Beyond the source.*

1. **A personal model-routing card.** A one-page table: task type → model → when to escalate. Start from the video's rule ([06:48](https://www.youtube.com/watch?v=BJauPEH_9OU&t=408s)–[07:06](https://www.youtube.com/watch?v=BJauPEH_9OU&t=426s)), update it to the current lineup, and replace "when Sonnet struggles" with triggers you can observe: two failed attempts, tests still failing, or an irreversible action. See [[Route Tasks to the Right Claude Model]] and [[Choosing a Claude Model]].
2. **Tiered subagents for this vault's ingest pipeline.** The cheapest tier takes batch chores like caption clean-up and timestamp arithmetic, the video's "batch, repetitive" slot ([01:41](https://www.youtube.com/watch?v=BJauPEH_9OU&t=101s)). The mid tier writes notes ([02:35](https://www.youtube.com/watch?v=BJauPEH_9OU&t=155s)). The top tier does cross-source synthesis and conflict checks ([07:02](https://www.youtube.com/watch?v=BJauPEH_9OU&t=422s)). Pin each subagent's model in its frontmatter. See [[Subagents and Agent Teams]] and [[Ingest Sources into an LLM Wiki]].
3. **Escalate on evidence, not feel.** Make "when Sonnet starts struggling" ([04:08](https://www.youtube.com/watch?v=BJauPEH_9OU&t=248s)) testable: verify after each attempt, escalate after two failures, and log the reason. See [[Build Verification into Every Task]].
4. **Model-tiered lookup.** Extend [[Tiered Lookup Routing]] so the fast tier handles file and wiki lookups, and a stronger model steps in only for synthesis across tiers. This follows the video's split between speed and depth ([01:32](https://www.youtube.com/watch?v=BJauPEH_9OU&t=92s), [01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s)).
5. **Usage and context hygiene check.** A weekly review of which model consumed usage and where large contexts were loaded needlessly. It tests the "Opus eats your limits" claim ([04:20](https://www.youtube.com/watch?v=BJauPEH_9OU&t=260s)) against your own data. See [[Context Hygiene Routine]] and [[Context Window Management]].
6. **Model-freshness sweep.** A scheduled task that finds superseded model claims in the vault (e.g. "Sonnet 4.6 is current", "Mythos can't be used") and adds a dated "superseded" line with a verification link. See [[Schedule Recurring Claude Tasks]].
7. **Cheap batch summarisation with an escape hatch.** Run bulk documents through the cheapest tier in batch ([01:41](https://www.youtube.com/watch?v=BJauPEH_9OU&t=101s)), and send only the items it flags as complex to a stronger model ([01:53](https://www.youtube.com/watch?v=BJauPEH_9OU&t=113s)). See [[Route Tasks to the Right Claude Model]].

## Resources mentioned

- **The description has no links**, only chapter timestamps and hashtags.
- **Named in the video, with no link:**
  - Anthropic ([00:26](https://www.youtube.com/watch?v=BJauPEH_9OU&t=26s)) and Claude Shannon ([00:44](https://www.youtube.com/watch?v=BJauPEH_9OU&t=44s)).
  - Constitutional AI ([01:12](https://www.youtube.com/watch?v=BJauPEH_9OU&t=72s)).
  - Benchmarks: SWE-bench ([03:38](https://www.youtube.com/watch?v=BJauPEH_9OU&t=218s)), GPQA Diamond ([03:52](https://www.youtube.com/watch?v=BJauPEH_9OU&t=232s)), Humanity's Last Exam ([05:31](https://www.youtube.com/watch?v=BJauPEH_9OU&t=331s)).
  - Rakuten ([04:01](https://www.youtube.com/watch?v=BJauPEH_9OU&t=241s)) and Project Glasswing ([05:15](https://www.youtube.com/watch?v=BJauPEH_9OU&t=315s)).
  - Other assistants: ChatGPT and Gemini ([06:09](https://www.youtube.com/watch?v=BJauPEH_9OU&t=369s)), Grok ([06:37](https://www.youtube.com/watch?v=BJauPEH_9OU&t=397s)).

## Beyond the source

*None of this is in the video. It was added at ingest on 2026-09-15 and verified at the links given.*

### The current lineup (September 2026)

| | Claude Fable 5.1 | Claude Opus 5 | Claude Sonnet 5 | Claude Haiku 4.5 |
|---|---|---|---|---|
| Docs positioning | Demanding reasoning and long-horizon agentic work | Complex agentic coding and enterprise work | Best mix of speed and intelligence | Fastest, near-frontier intelligence |
| Released | 2026-09-01 | 2026-07-24 | 2026-06-30 | 2025-10-15 |
| Claude API ID | `claude-fable-5-1` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5` (snapshot `claude-haiku-4-5-20251001`) |
| Price per million tokens (input / output) | $10 / $50 | $5 / $25 | $2 / $10 | $1 / $5 |
| Context window (API) | 1M | 1M | 1M | 200K |
| Max output (synchronous API) | 128K | 128K | 128K | 64K |
| Relative latency | Slower | Moderate | Fast | Fastest |
| Thinking | Adaptive, always on | Adaptive | Adaptive | Extended |
| Earliest retirement | Not before 2027-09-01 | Not before 2027-07-24 | Not before 2027-06-30 | Not before 2026-10-15 |

- **Where the table comes from:**
  - Specs, IDs, prices and retirement commitments: https://platform.claude.com/docs/en/about-claude/models/overview
  - Release dates: https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/ (Fable 5.1), https://www.anthropic.com/news/claude-opus-5 (Opus 5), https://www.anthropic.com/news/claude-sonnet-5 (Sonnet 5) and https://www.anthropic.com/news/claude-haiku-4-5 (Haiku 4.5).
- **Pricing notes from the same overview:**
  - Batch API requests cost 50% less.
  - Prompt-cache reads cost 10% of the base input price, or 2.5% on Fable 5.1 and Mythos 5.1.
- **Legacy models you can still call:** Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Sonnet 4.6 and Sonnet 4.5.
- **Haiku 4.5's retirement date is close.** The overview only commits not to retire it before 2026-10-15, so any routing plan built on it should watch the deprecations page. Source: https://platform.claude.com/docs/en/about-claude/model-deprecations

### What changed after the video

- **Claude Opus 4.8** launched 2026-05-28. Source: https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/
- **Claude Fable 5 and Claude Mythos 5** launched 2026-06-09. Source: https://www.anthropic.com/news/claude-fable-5-mythos-5
  - They are the same model, and the safeguards are the only difference.
  - Fable 5 went straight to the API and consumption-based Enterprise. Pro, Max, Team and seat-based Enterprise plans got it at no extra cost until 2026-06-22, then needed usage credits.
  - At launch only existing Mythos Preview users, such as Project Glasswing's cyber partners, could upgrade to Mythos 5. Biomedical researchers were to follow in the coming weeks through a trusted-access programme for biology.
  - Price: $10/$50 per million tokens.
- **Claude Sonnet 5** launched 2026-06-30. Source: https://www.anthropic.com/news/claude-sonnet-5
  - It's the default model on the Free and Pro plans.
  - The launch price of $2/$10 was made permanent in an August 2026 update, replacing a planned $3/$15.
- **Claude Opus 5** launched 2026-07-24. Source: https://www.anthropic.com/news/claude-opus-5
  - It's the new default on Max and the strongest model on Pro.
  - Price: $5/$25.
  - It has adjustable effort and a fast mode that runs about 2.5× faster at twice the price.
  - Anthropic says it trails Mythos 5 on cybersecurity and biology work.
- **Claude Fable 5.1 and Claude Mythos 5.1** launched 2026-09-01.
  - Anthropic describes them as the same model with different levels of safeguards. Fable 5.1 is generally available.
  - The sources describe Mythos 5.1 access in two ways, so both are recorded here. The announcement limits it to vetted US organisations in trusted-access programmes. One is a new Life Sciences Verification Program. The other, a Cyber Verification Program, says Mythos-class access is coming soon. The model-choice docs say Project Glasswing participants only.
  - Sources: https://www.anthropic.com/claude-fable-and-mythos-5-1 and https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- **What the video said about Sonnet 4.6 was mostly right for May.** It launched 2026-02-17 as the Free and Pro default at $3/$15. The 1M context window was a beta at launch. Source: https://www.anthropic.com/news/claude-sonnet-4-6

### Fable on Claude plans

- **Free:** Fable isn't available.
- **Included** (up to 50% of the weekly limit): Max, and Premium seats on Team and Enterprise.
- **Usage credits required:** Pro, and Standard seats on Team and Enterprise.
- **Surfaces:** web, mobile, desktop, Cowork, Claude Code and Claude Design, among others. This article says Fable 5.1 in Claude Code needs version 2.1.255 or later. The Claude Code model-config docs say 2.1.257 or later, so go by the higher number.
- Source: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan

### Anthropic's current model-choice guidance

- **Default starting point.** The models overview says to start most workloads on Opus 5, and to use Fable 5.1 for demanding reasoning, long-horizon agentic work, or when Opus 5 at higher effort still falls short. Source: https://platform.claude.com/docs/en/about-claude/models/overview
- **Criteria to weigh:** capabilities, speed, cost and effort. The docs say tuning effort is often a better lever than changing models. Source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- **Two starting strategies:**
  - *Efficiency-first:* start with Haiku 4.5 and upgrade only where you find capability gaps. Suits prototyping, tight latency and high-volume simple tasks.
  - *Capability-first:* start with Opus 5, then lower the effort or move to a cheaper model over time. Go to Fable 5.1 if evals at `xhigh` or `max` effort still fall short.
- **Selection matrix, in brief:**
  - Fable 5.1 for multi-hour agent sessions and deep research.
  - Opus 5 for complex agentic coding and large refactors.
  - Sonnet 5 for everyday coding, analysis and agentic tool use.
  - Haiku 4.5 for real-time, high-volume and sub-agent tasks.
- **Test before switching.** The docs call a use-case-specific eval set the most important step in deciding whether to change models.
- **Combining models.** The docs describe two multi-model patterns. Before building either, sweep effort on your current model and price the stronger model alone at low effort. Source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - **Advisor:** a cheaper executor model calls a frontier "advisor" model for hard judgment calls.
  - **Orchestrator:** a frontier coordinator hands independent pieces of work to cheaper workers. You build it with [[Claude Managed Agents]] multi-agent orchestration, which can also give a session an advisor.
  - *This note's reading:* the advisor pattern is the closest formal version of the video's "escalate to Opus" rule.

### Switching models in Claude Code

- **Model aliases:**
  - `default`, which clears the override and returns to the account default: Opus 5 on most plans, Sonnet 5 on Pro and Team Standard.
  - `best`: Fable where available, otherwise Opus.
  - `fable`, plus `opus` (described as for complex reasoning), `sonnet` (for daily coding) and `haiku` (for simple tasks).
  - `sonnet[1m]` and `opus[1m]`, for the 1M context window.
  - `opusplan`: Opus in plan mode, then Sonnet for execution.
- **Ways to set the model:**
  - `/model <alias>` during a session. Run it with no argument to open the picker.
  - `claude --model <alias>` at launch.
  - The `ANTHROPIC_MODEL` environment variable.
  - The `"model"` key in `~/.claude/settings.json`.
- **Effort:** set it with `/effort`, `--effort` or `CLAUDE_CODE_EFFORT_LEVEL`. The docs list `low`, `medium`, `high`, `xhigh`, `max` and `ultracode`. Fable 5/5.1, Opus 5/4.8/4.7 and Sonnet 5 accept `low` through `max`. Opus 4.6 and Sonnet 4.6 have no `xhigh`, and Haiku 4.5 doesn't support effort.
- **Subagents:**
  - Set `model: haiku` (or any alias) in a subagent's frontmatter.
  - `CLAUDE_CODE_SUBAGENT_MODEL` is the fallback for subagents that don't set a model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` overrides all of them.
- **Pinning aliases:** the `ANTHROPIC_DEFAULT_*_MODEL` variables pin what each alias resolves to. The docs present them for Bedrock, Google Cloud and Foundry deployments.
- Source: https://code.claude.com/docs/en/model-config. See [[Claude Code]].

### Context windows by surface

- **Chat on paid plans:** 1M tokens for Fable 5.1, Opus 5 and Sonnet 5. 500K for Opus 4.8, 4.7, 4.6 and Sonnet 4.6. 200K for other models.
- **Claude Code:** 1M for Fable 5.1, Fable 5, Opus 5, Sonnet 5 and Opus 4.6–4.8. Pro users must turn on usage credits for the Opus 1M window. Sonnet 4.6 can also use 1M on any paid plan, but only with usage credits enabled (usage-based Enterprise excepted).
- **[[Claude Cowork]]:**
  - 1M for Fable, Opus 5, Sonnet 5 and Opus 4.8/4.7.
  - Sonnet 5 automatically compacts the conversation at 500K.
  - Sonnet 4.6, Opus 4.6 and Haiku 4.5 get 200K.
- Source: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
- **Tokens to words.** The API docs put 1M tokens at about 555,000 words on the tokenizer introduced with Opus 4.7, and about 750,000 words on earlier models. They give no page count. Source: https://platform.claude.com/docs/en/about-claude/models/overview

### Claim checks

- **Opus 4.7 launch details.** Released 2026-04-16 at $5/$25. Its updated tokenizer maps the same input to roughly 1.0–1.35× as many tokens. Source: https://www.anthropic.com/news/claude-opus-4-7
- **Opus 4.7 benchmarks:** 87.6% on SWE-bench Verified, 64.3% on SWE-bench Pro, 94.2% on GPQA Diamond. Source: https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained
- **Rakuten.**
  - Anthropic's Claude 4 announcement (2025-05-22) credits Opus 4 with a demanding seven-hour open-source refactor at Rakuten. Source: https://www.anthropic.com/news/claude-4
  - Claude's Rakuten case study says Claude Code implemented an activation-vector extraction method in vLLM, a codebase of about 12.5M lines, in a seven-hour autonomous run with 99.9% numerical accuracy. It doesn't name the model. Source: https://claude.com/customers/rakuten
- **Mythos Preview and Project Glasswing.**
  - Both were announced 2026-04-07.
  - Launch partners included AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA and Palo Alto Networks, plus more than 40 other organisations. Source: https://www.anthropic.com/glasswing
  - The launch page says Mythos Preview found thousands of high-severity vulnerabilities, including some in every major operating system and web browser. In a separate statement it reports thousands of zero-day vulnerabilities, many of them critical.
  - Anthropic's technical write-up says Mythos Preview wrote exploits in hours that expert penetration testers estimated would take them weeks. Source: https://www.anthropic.com/research/mythos-preview
  - A 2026-05-22 update reported more than ten thousand high- or critical-severity vulnerabilities found with about 50 partners in the first month. Source: https://www.anthropic.com/research/glasswing-initial-update
- **Humanity's Last Exam.**
  - Mythos Preview: 56.8% without tools and 64.7% with tools. Opus 4.6: 40.0% and 53.1%. Source: https://www.anthropic.com/glasswing
  - A third-party leaderboard updated 2026-09-14 lists Fable 5.1 at 65%, Opus 5 at 64.7%, Mythos 5 at 64.5%, Sonnet 5 at 57.4% and Opus 4.7 at 54.7%. It doesn't say whether tools were used. Source: https://benchlm.ai/benchmarks/hle
- **Image input.** All current Claude models take text and image input and produce text output. Source: https://platform.claude.com/docs/en/about-claude/models/overview
- **How usage limits work.**
  - Usage depends on conversation length and complexity, the features you use, the model and the effort level.
  - Usage across claude.ai, Claude Code and Claude Desktop counts toward the same limit. Source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
  - Anthropic's tips include batching related questions into one message, uploading core documents to projects (reused project content is cached and doesn't count against limits), and checking Settings > Usage. Source: https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- **Constitution.** Anthropic's published constitution says it generally prefers cultivating good values and judgment over strict rules, and tries to explain any rules it does impose. Source: https://www.anthropic.com/constitution
- **Not verified here, left as the video's claims:**
  - Anthropic's founding story ([00:29](https://www.youtube.com/watch?v=BJauPEH_9OU&t=29s)).
  - The Claude Shannon origin of the name and its framing ([00:44](https://www.youtube.com/watch?v=BJauPEH_9OU&t=44s)).
  - The usage-limit and caution comparisons with ChatGPT and Gemini, and the Grok preference.

## Transcript notes

| Caption | Corrected / interpretation |
|---|---|
| "SWE-bench" (03:38) | The 87.6% figure is SWE-bench Verified |
| "humanity's last exam" (05:31) | Humanity's Last Exam (HLE). 64.7% is Mythos Preview's with-tools score |
| "Mythos" (throughout) | In April–May 2026 the restricted model was Claude Mythos Preview. Mythos 5 and 5.1 came later |
| "Tai Lung" (04:52) | Not a product: the Kung Fu Panda villain, used as a joke nickname for Mythos |
| "Opus 4" (04:01) | Transcribed correctly. The narration says Opus 4 even though it sits in the Opus 4.7 section |
| "It's limitation" (01:53) | "Its limitation" |
| "2 to 3,000 pages" (02:32) | 2,000 to 3,000 pages |
| "[snorts]" (06:14) | A caption sound tag, not speech |
| Chapter title "Claude Mythos / Fable" (04:51) | Fable is never mentioned in the narration. The title was probably edited in later (inference) |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Choosing a Claude Model]] · [[Context Window Management]] · [[Agent Laziness]] · [[CLAUDE.md as a Router]] · [[Context vs Connections]] · [[Always-On Brain OS]] · [[Design for Retrieval]] · [[Subagents and Agent Teams]] · [[Plan Before Executing]]
- **Techniques:** [[Route Tasks to the Right Claude Model]] · [[Context Hygiene Routine]] · [[Tiered Lookup Routing]] · [[Build Verification into Every Task]] · [[Schedule Recurring Claude Tasks]] · [[Ingest Sources into an LLM Wiki]]
- **Tools:** [[Claude Code]] · [[Claude Cowork]] · [[Claude Managed Agents]]
- **Other sources:** [[Nate Herk - Every Level of a Claude Second Brain]] · [[Simon Pittman - Set Up Claude Cowork]] · [[Nate Herk - 32 Tricks to Level Up Claude Code]] · [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[AI LABS - The Unlazy Skill for Lazy Agents]]
