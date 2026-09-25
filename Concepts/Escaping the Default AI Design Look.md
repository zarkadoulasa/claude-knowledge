---
type: concept
aliases: ["Generic AI Design Look", "AI Slop Design", "Design by Reference"]
sources: ["[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[Sergei Chyrkov - Claude Design Full Tutorial]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Nick Saraev - Animated Sites with Claude Code and Kling]]", "[[Codex Community - Testing Opus 5.5 on Design and 3D]]"]
tags: [topic/design, topic/skills, topic/verification, topic/prompting, topic/media]
---

# Escaping the Default AI Design Look

## In one sentence

Left to itself, any model designs in a house style you can spot. A site stands out only when something outside the model steers it: a practising designer's packaged judgement, real references kept at full detail, precise words for what you want, and a review loop that checks the result ([[AI LABS - Claude Design Skills for Beautiful Sites]] [00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s)–[00:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=30s); [[Nate Herk - 32 Tricks to Level Up Claude Code]] [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)–[10:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=615s)).

## How it works

### Why the default look exists

- **Capability doesn't remove the pattern.** [[AI LABS]] grant that models now design well [00:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=18s)–[00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s). But each model follows its own pattern, and that pattern is easy to recognise [00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s)–[00:26](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=26s), so something has to push it elsewhere for a site to stand out [00:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=28s)–[00:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=30s).
- **A stronger model can be its own lever — one reviewer's claim.** [[Codex Community - Testing Opus 5.5 on Design and 3D]] runs his standard design prompts on Claude Opus 5.5 in the Claude app and judges the visual hierarchy, typography, colour and micro-animation "essentially what I would expect from a professional graphics designer" ([04:44](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=284s)). Treat it as a single-reviewer, subjective take on a handful of prompts, not a benchmark — and note the cost: most prompts ran roughly an hour each ([08:27](https://www.youtube.com/watch?v=Da7ZuhyWACg&t=507s)).
- **An elaborate workflow isn't the fix.** Some design skills run an impressive-looking process and still end with a site like every other [00:05](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=5s)–[00:11](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=11s). In their testing only a few delivered [00:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=13s). The vault's takeaway: judge a skill by its output, not its process.
- **Context decides between quality and slop.** [[Ras Mic]] makes the general case in [[Ras Mic - How AI Agents and Claude Skills Work]]. Models are good now, but the context you supply steers them toward quality or toward slop ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s)–[01:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=77s)).
- **Two more diagnoses.** [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] say that at each design call a model reaches for the most common choice in its training data [01:03](https://www.youtube.com/watch?v=Ot582-E61ac&t=63s). [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] says models have never seen great design [01:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=64s), so slop shows in typography, imagery, hierarchy, colour and spacing [01:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=99s).

### Lever 1: borrow a practising designer's judgement

- **Skills as packaged expertise.** The skills AI LABS cover were written by people with long design experience, who turned workflows they had tested into a reusable form [00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s)–[00:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=41s). See [[Agent Skills]].
- **They add what the model won't.** Meng To's build-awwwards-quality-sites lists the principles and details found on Awwwards-level sites, because Claude doesn't reach that level unaided [08:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=493s)–[08:19](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=499s). Beyond principles, it carries the specific techniques and effects that make a site look expensive, which a model won't produce by itself [08:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=507s)–[08:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=514s).
- **Taste, not only rules.** tastemaker exists to stop models falling back on generic defaults [10:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=615s)–[10:19](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=619s). AI LABS describe it as giving the model taste to design with [10:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=659s)–[11:04](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=664s).
- **A portable "taste" skill as the whole lever.** [[Nick Saraev - Animated Sites with Claude Code and Kling]] one-shots luxury marketing sites in Claude Code by pointing it at [[Leon Lin]]'s open-source "taste" skill — a public GitHub repo of high-end web-design principles and schematics that, he says, is how you get high-quality one-shot sites from a simple prompt ([01:14](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=74s)). It stands in for the designer-written skills above; the caveat is that it's a solo teenager's fast-moving repo that could change or break.
- **Commit to one direction first.** AI LABS say frontend-design forces the model to pick a design direction before writing anything [01:20](https://www.youtube.com/watch?v=Ot582-E61ac&t=80s).
- **Or let an interview set it.** [[Nate Herk - The Scrollcraft Website Design Skill]] has no template. Its interview about feel and the visitor's journey makes every site come out different [01:10](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=70s), and he finds models now take emotional direction [08:17](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=497s). See [[Scrollcraft]].

### Lever 2: never design from thin air

- **Reference-grounded skills.**
  - web-design-engineer first works through your requirements until they're clear [04:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=252s)–[04:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=258s), then looks for real designs to work from [04:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=258s).
  - Its principle is that good design always builds on something that came before [04:20](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=260s)–[04:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=267s).
  - It bundles references on judging a design, on how designs typically fail, and style recipes modelled on famous sites such as Apple's and Linear's, which it checks while it builds [04:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=271s)–[04:46](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=286s).
- **Nate's design-by-reference hack, no skill needed.**
  - In [[Claude Code]], [[Nate Herk]] screenshots sites he likes and asks Claude to make his look like them [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)–[10:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=612s). Claude picks up their design patterns without the generic AI look [10:12](https://www.youtube.com/watch?v=jqoFP9QapXI&t=612s)–[10:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=615s).
  - He also gives Claude the reference site's HTML and styling [10:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=615s)–[10:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=622s).
  - Claude could more or less clone the site, so he treats the result as a template and adds his own touch [10:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=622s)–[10:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=628s).
- **Visual references inside your own skills.** [[Jay E]], in [[Jay E - The ARMS Framework for a Claude Agentic OS]], keeps a brand HTML file with fonts and palettes inside his skill folder ([07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s)–[08:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=482s)). He says visual references like this work especially well for design skills ([08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s)–[08:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=487s)). See [[Build a Reference-Rich Skill]].
- **A design system beats a better prompt.**
  - [[Sergei Chyrkov - Claude Design Full Tutorial]] credits the design process, more than a better prompt, for the jump from his generic first try [00:06](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=6s). His main lever is a [[Claude Design]] design system built from one inspiration image [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s).
  - Sergei also names SVG-style illustrations as a generic tell in that first try [02:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=160s). He swaps the illustrated pizza for a photo and adds photos of people [09:14](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=554s), and would still replace the SVGs left after the Claude Code build [14:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=842s).
  - Jack pastes in a real product's system from a gallery of 2,000+ [01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s).
  - See [[Design Systems for Claude]].
- **Brand context for marketing.** [[Nate Herk - Claude as a One-Person Marketing Team]] says a brand's pain, person and promise keep its assets from reading as generic slop [02:00](https://www.youtube.com/watch?v=yCACmFTiCto&t=120s). [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] gives the image model a one-page brand book as its reference [07:56](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=476s). See [[Generating Images and Video with Claude]].
- **Reference videos for motion.** [[Chase AI - GPT-6 Astra Motion Design in After Effects]] feeds the agent videos that have the effects he wants [03:26](https://www.youtube.com/watch?v=C8dWdic-oK4&t=206s).

### Lever 3: keep references at pixel level

- **Why agents drift from a reference.** Handed an image, a model usually writes a text summary of it to use later [10:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=627s)–[10:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=632s), and detail is lost in that translation [10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s)–[10:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=645s).
- **The fix is extraction, not description.**
  - tastemaker works from the reference's actual pixels, so nothing is lost turning a look into words [10:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=621s)–[10:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=627s).
  - Its scripts pull exact design details into a structured format that agents can reuse [10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)–[10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s).
  - Scripts handle whatever doesn't need the agent [10:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=647s)–[10:50](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=650s), and its decisions carry across the whole project, not just one screen [10:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=655s)–[10:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=659s).
- **A generated mockup as the spec.** Jay generates images of the components he wants and hands them to Claude Code [13:15](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=795s). That aligns Claude with his intent about 50–60% of the way, far quicker than describing it, but the HTML still needs refining [13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s).

### Lever 4: say exactly what you want

- **Name the page type.**
  - A landing page isn't a homepage [05:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=345s)–[05:49](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=349s). A homepage tries to serve many kinds of visitor, while a landing page has one job: getting people to act [05:49](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=349s)–[05:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=355s).
  - Models produce homepages that work but aren't specialised for landing pages [05:57](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=357s)–[06:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=363s).
  - So landing-page-design builds the page around the single action you want [06:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=363s)–[06:11](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=371s), holds one visual style [06:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=372s)–[06:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=375s), and covers being found in search [06:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=375s)–[06:22](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=382s).
- **Name the motion.** animation-vocabulary converts a vague description of an animation into precise terms a model understands [01:35](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=95s)–[01:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=101s).
- **Know the default motion tells.** Asked to animate, models almost always add the same slide-in reveal on scroll, so AI LABS use GSAP's official skills instead [08:11](https://www.youtube.com/watch?v=Ot582-E61ac&t=491s)–[08:29](https://www.youtube.com/watch?v=Ot582-E61ac&t=509s). In After Effects, Chase finds each beat lingers for 2.5–3 seconds unless you set the pacing [07:02](https://www.youtube.com/watch?v=C8dWdic-oK4&t=422s).
- **Let the skill interview you.**
  - emil-design-eng asks about the app before building, as Claude Design does natively [02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s)–[02:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=147s). landing-page-design also asks first [06:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=387s).
  - In Claude Code, Nate tells Claude to use its AskUserQuestion tool and keep asking until it's 95% confident it knows what you need [03:42](https://www.youtube.com/watch?v=jqoFP9QapXI&t=222s)–[03:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=229s).
  - See [[Plan Before Executing]] and [[Grill Me Interview Skill]].

### Lever 5: split generate, refine and review

The role labels are the vault's; AI LABS describe each job.

| Role | Job | Skills in the video | Where |
|---|---|---|---|
| Generate | Build the first design from a brief | emil-design-eng (the one to start with), web-design-engineer, landing-page-design, build-awwwards-quality-sites, tastemaker | [01:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=111s), [04:46](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=286s), [06:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=384s), [08:36](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=516s), [11:06](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=666s) |
| Refine | Improve something already built | animate (motion on an existing site), better-layout (spacing, positioning, alignment), perception laws (how the eye reads a design, applied after the critique) | [02:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=160s), [09:48](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=588s), [12:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=732s) |
| Review | Score or list issues so you can fix and rerun | web-design-engineer run on an existing design, Jakub Krehel's review skill (interface-review), screen critique | [05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s), [09:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=554s), [12:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=723s) |

- **Refiners change less than you'd think.**
  - animate's gain on a landing page was modest, because landing pages lean on scroll-based animation [02:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=179s)–[03:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=194s).
  - It did better on small functional details, like feedback when a form is submitted and graphics that appear on hover [03:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=196s)–[03:36](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=216s).
  - better-layout won't make a site look very different. It makes it correct against the principles designers work to [10:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=607s)–[10:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=613s).

### Lever 6: review against evidence, then iterate

- **Score and rerun.** Run web-design-engineer on an existing design and it scores it in several areas. AI LABS say to keep refining and rerunning it until the score is perfect and the result is the design you were after [05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s)–[05:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=314s).
- **Regression-aware review.**
  - Jakub Krehel's review skill works better connected to GitHub, because it compares the design before and after your changes [09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s)–[09:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=570s).
  - It flags anything that worked before and no longer does, and names the change that broke it [09:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=572s)–[09:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=579s).
  - It also checks animations, accessibility and different screen sizes, then lists every finding [09:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=581s)–[09:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=587s).
- **Research-grounded design laws.**
  - designer-skills grounds its skills in research and in the named laws designers work from, with a separate skill for each [11:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=681s)–[11:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=691s).
  - Screen critique reviews a screen from many angles against guidelines for judging design quality [11:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=705s)–[11:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=715s). Perception laws describe how the eye actually takes in a design [11:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=715s)–[12:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=723s).
  - The review reports problems with what stands out first, type and spacing [12:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=723s)–[12:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=732s). Applying the laws made the site feel more refined [12:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=732s)–[12:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=736s).
- **Let Claude look at its own work.**
  - Nate has Claude design, screenshot, apply changes and repeat, about three passes before he sees V1 [09:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=555s)–[09:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=567s). That V1 is much better than the ones he used to get [09:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=567s)–[09:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=571s).
  - A browser check does for function what the screenshot loop does for looks [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)–[09:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=586s).
  - See [[Build Verification into Every Task]] and [[Verification Before Done]].
- **Raise the bar, then keep the lesson.** When output is merely okay, Nate tells Claude to scrap it and do a more elegant version, or a different approach [08:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=482s)–[08:09](https://www.youtube.com/watch?v=jqoFP9QapXI&t=489s). Once the better version lands, he has Claude update the skill or CLAUDE.md [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)–[08:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=502s). See [[Skill Improvement Loop]].
- **Measure the gap to a benchmark.** Jack says Claude needs the why behind "it looks better" [05:34](https://www.youtube.com/watch?v=NAumQObJEwM&t=334s), so he asks for an HTML report of measured gaps against a benchmark site [05:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=351s), then loops three critic subagents toward a benchmark screenshot (disagreements below). Build it: [[Benchmark-Driven Design Critique]].
- **Volume, then human selection.** Jay has Claude produce several iterations so his own taste picks one [14:37](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=877s).

## When to use it — and when not to

Match the lever to the job:

| Situation | What the sources point to | Where |
|---|---|---|
| Landing page | Build around one action first; motion polish adds little unless it's scroll-based | AI LABS [06:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=363s), [02:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=179s) |
| App or form-heavy site | Motion refiners pay off on small functional interactions | AI LABS [03:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=196s) |
| Premium or story-led marketing site | Awwwards-style principles and scroll storytelling | AI LABS [08:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=493s), [08:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=527s) |
| You already have a design | Review and score it instead of regenerating | AI LABS [05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s) |
| You have sites you admire but no design skills | Screenshots plus HTML as references, then a screenshot self-check loop | Nate Herk [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s), [09:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=555s) |
| Front-end behaviour matters | Visual skills aren't enough: web-design-engineer targets stunning visuals, not function, so add a browser check | AI LABS [04:09](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=249s); Nate Herk [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s) |
| Functional UI: dashboards, app screens | Consistency and proven components, not art direction. AI LABS say Anthropic's design skill doesn't work well here | AI LABS (earlier video) [02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s); see [[Build Product UI from a Component Registry]] |
| Mobile app | Mobile isn't a smaller web: thumb reach, navigation and each platform's design language | AI LABS (earlier video) [11:25](https://www.youtube.com/watch?v=Ot582-E61ac&t=685s) |

**Where the sources hold back:**

- **Don't clone literally.** Nate treats a cloned site as a template to make his own [10:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=624s)–[10:28](https://www.youtube.com/watch?v=jqoFP9QapXI&t=628s).
- **Don't install whole collections by default.** From designer-skills, AI LABS installed only the two skills that fit their work [11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)–[11:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=705s).

## Perspectives from sources

- [[AI LABS - Claude Design Skills for Beautiful Sites]] is the main source. Designer-written skills steer a model off its house style [00:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=28s). They tested seven collections, mostly in [[Claude Design]] [00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s), and chained generators with refiners and reviewers.
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] gives the skill-free route in Claude Code: reference screenshots and HTML [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s), [10:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=615s), a screenshot self-check loop [09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s), and a rule not to move on until Claude is 95% confident [04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s).
- [[Jay E - The ARMS Framework for a Claude Agentic OS]] puts visual reference files inside a design skill ([08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: context decides between quality and slop ([01:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=70s)).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]], speaking about coding skills, warns that some skills are subjective, so stick to one coherent group ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)–[08:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=504s)). See below.
- **Added September 2026:** seven sources on design systems, benchmark critique, brand context, image and motion work. Each is named where its point appears in the levers, table and disagreements.

## Where sources disagree

- **Install lots of other people's skills, a few, or none?**
  - *AI LABS:* add as many of Emil's skills as you like [03:42](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=222s)–[03:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=227s), but only the designer-skills that fit how you work [11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s)–[11:43](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=703s).
  - *[[The Coding Sloth]]:* don't install a hundred skills. Some are subjective, so stick with one group that matches your style. His context is coding skills ([08:12](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=492s)–[08:24](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=504s)).
  - *Ras Mic:* he reads other people's skills and learns from them but doesn't install them, because an agent needs the context of your own successful run ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)–[12:55](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=775s)). Skill marketplaces are also an easy way to attack someone ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=787s)).
  - *AI LABS, earlier video:* pick one taste preset rather than stacking them [10:15](https://www.youtube.com/watch?v=Ot582-E61ac&t=615s).
  - See [[Build vs Install Third-Party Skills]].
- **Do you need design skills at all?** AI LABS present skills as the thing that steers a model off its pattern [00:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=28s). Nate escapes the generic look in Claude Code with screenshots, HTML and a self-check loop, and names no design skill [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)–[10:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=615s), [09:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=555s)–[09:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=567s). In the vault's reading the two stack, since web-design-engineer and tastemaker are themselves reference-driven. Newer sources lean on systems or context instead: Sergei on a Claude Design design system [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s), and Nate's marketing build on brand context [18:33](https://www.youtube.com/watch?v=yCACmFTiCto&t=1113s) plus one third-party scroll skill [17:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1078s).
- **How good is good enough?** AI LABS talk of rerunning until the design reaches a perfect score [05:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=307s)–[05:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=314s). Nate accepts that AI rarely nails a task in one go and aims for 90% of the way rather than 60–65% [04:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=277s)–[04:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=285s). The real rubric is under Beyond the source.
  - *Jack* loops critics until the work hits the mark, with no cap [10:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=618s).
  - *Chase* usually needed two or three human-judged iterations [06:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=410s). He avoids loops because each After Effects build is slow [07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s).
  - *Vault reading:* iterate toward a score when a pass is cheap, and use a few human-judged passes when it's slow.
- **How close to a reference is too close?**
  - Jack recreates Apple's and Anthropic's launch emails almost directly [11:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=664s). His only caveat is to adapt [11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s).
  - Sergei stresses his image is for inspiration, not copying [04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s).
  - [[Benchmark-Driven Design Critique]] adds a copied-identity check.

## Beyond the source

*Not from any video. Checked on 2026-09-15 at the links given.*

- **Anthropic's own skill for this problem.**
  - Anthropic's frontend-design skill aims at distinctive, intentional UI instead of templated defaults.
  - It asks for typefaces chosen for the brief, palettes specific to the subject rather than stock combinations, and composition that opens with the most characteristic element.
  - Motion should be sparse, with one orchestrated moment rather than scattered effects.
  - https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- **The frontend-design skill has been rewritten.** AI LABS say the original had aged for newer models [02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s). The anthropics/claude-code copy now:
  - asks for a plan, reviewed against the brief, before building;
  - names five default AI looks to avoid, for example cream with terracotta;
  - discourages fade-and-slide-up motion.

  https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- **Anthropic's worked example.** A Claude Academy use case builds a design skill with a main instruction file plus reference documents: a design interrogation checklist, a technique catalogue, an exemplar library, a refinement protocol and a design philosophy. The aim is output that reads as hand-crafted rather than template-based. https://academy.claude.com/use-cases/elevate-claudes-design-using-skills
- **A first-party anchor.** Claude Design can extract a design system from your codebase, screenshots or brand files: colours, type, components and spacing. It then builds with it, a brand-specific alternative to generic defaults. https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- **Vocabulary examples.** animation-vocabulary maps described effects to named ones: a cascade becomes a stagger, the iOS drag-past-the-edge feel is rubber-banding, a thumbnail expanding into a card is a shared element transition, and there are also origin-aware animation and parallax. https://github.com/emilkowalski/skills/blob/main/skills/animation-vocabulary/SKILL.md
- **What emil-design-eng teaches.** Don't animate actions people repeat constantly. Prefer ease-out and custom curves, keep UI animations short (under about 300 ms), animate only transform and opacity, and respect reduced-motion settings. https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md
- **"Perfect score" in practice.** web-design-engineer's critique guide scores five dimensions on a 10-point scale: philosophy alignment, visual hierarchy, craft quality, functionality and originality. It returns Keep, Fix (sorted by severity) and three Quick Wins. Treat the target as a threshold, not perfection. https://github.com/ConardLi/garden-skills/blob/main/skills/web-design-engineer/references/critique-guide.md
- **interface-review gives a verdict, not a score.**
  - It runs only when invoked, on a PR, branch, range or uncommitted changes.
  - It reads removed lines to find regressions and tags each finding Introduced, Regression or Pre-existing.
  - It ends with Block or Approve.
  - https://github.com/jakubkrehel/skills/blob/main/skills/interface-review/SKILL.md
- **What better-layout checks.** Grouping through spacing, alignment, reading order and progressive disclosure. Findings are rated by severity and the report closes with Block or Approve. https://github.com/jakubkrehel/skills/blob/main/skills/better-layout/SKILL.md
- **tastemaker's machinery.** Python scripts extract palettes from reference pixels (Pillow, with a vision fallback), check contrast, and scan for common AI-design antipatterns. Decisions persist in `.tastemaker/style-lock.md` and `.tastemaker/decisions.log`, and personal preferences in `~/.tastemaker/profile.md`. https://github.com/codeswithroh/tastemaker
- **The "perception laws" and "screen critique" names.** No designer-skills skill is called perception laws. The closest match is the ui-design plugin's Gestalt skills: law-of-proximity, law-of-similarity, law-of-closure, law-of-common-region, law-of-continuity, law-of-figure-ground and von-restorff-effect. Screen critique is the `/visual-critique:critique-screen` command, which runs seven visual critiques and returns a prioritised fix list. https://github.com/Owl-Listener/designer-skills/tree/main/ui-design/skills · https://github.com/Owl-Listener/designer-skills
- **Where referencing becomes copying.** Meng To's Awwwards skill extracts traits from references to build a new identity. It forbids reusing, tracing or closely reproducing a reference's assets, screenshots, source code, identity or copy, and requires original or licensed media. That's a practical line for Nate's clone hack. https://github.com/MengTo/Skills/blob/main/agent-skills/web-design/build-awwwards-quality-sites/SKILL.md

## Related

- **Build it:** [[Build a Distinctive Site with Design Skills]] · [[Benchmark-Driven Design Critique]] · [[Create and Reuse a Claude Design System]] · [[Build a Scroll-Driven Landing Page]] · [[Build Product UI from a Component Registry]] · [[Generate On-Brand Images from Claude Code]] · [[Storyboard-First AI Video and Motion Graphics]]
- **Concepts:** [[Design Systems for Claude]] · [[Generating Images and Video with Claude]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Verification Before Done]] · [[Plan Before Executing]]
- **Techniques:** [[Build Verification into Every Task]] · [[Build a Reference-Rich Skill]] · [[Skill Improvement Loop]] · [[Multi-Agent Review and Scoring Loops]] · [[Grill Me Interview Skill]]
- **Tools:** [[Claude Design]] · [[Claude Code]] · [[Scrollcraft]] · [[shadcn]] · [[Higgsfield]]
- **People:** [[AI LABS]] · [[Nate Herk]] · [[Ras Mic]] · [[Jay E]] · [[The Coding Sloth]] · [[Jack Roberts]] · [[Sergei Chyrkov]] · [[Chase AI]] · [[Nick Saraev]] · [[Leon Lin]] · [[Codex Community]]
- [[Home]]
