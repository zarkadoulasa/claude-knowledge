---
type: source
title: "Turn Claude into a Design Genius... Just Watch"
creator: "[[Jack Roberts]]"
channel: "Jack Roberts"
url: https://www.youtube.com/watch?v=NAumQObJEwM
video_id: NAumQObJEwM
published: 2026-08-12
duration: "17:55"
ingested: 2026-09-15
topics: [design systems, ai slop tells, benchmark design critique, design loop, gauntlet loop, critic subagents, html email, zapier mcp, design os, image generation, style recipes]
tags: [source/youtube, topic/design, topic/loops, topic/subagents, topic/verification, topic/mcp, topic/permissions, topic/agentic-os, topic/media]
---

# Jack Roberts - Design Systems, Critic Loops and a Design OS

> **Creator:** [[Jack Roberts]] · **Published:** 2026-08-12 · **Length:** 17:55 · [Watch on YouTube](https://www.youtube.com/watch?v=NAumQObJEwM)

## TL;DR

[[Jack Roberts]] says Claude designs badly because it has never seen great design, and that AI slop gives itself away in five places. He offers three levels:

1. **Design-system specs.** Paste a real product's spec into Claude from a gallery of 2,000+ systems (unnamed, very likely Refero Styles). Then have Claude compare your site against a benchmark, "ruthlessly", in an HTML gap report.
2. **The design loop.** His skill, adapted from the Gauntlet Loop, has three critic subagents judge the output against a benchmark screenshot until it matches. He recreates Apple and Anthropic launch emails this way, then sends one through Zapier.
3. **A design OS.** A local app inside his Claude Code "operating system". It generates images across several providers, searches his images by content and saves style recipes. Demo only.

The ideas are sound, but he shows no skill file, critic prompt, stop rule or loop cost.

## Key takeaways

- **Slop has five tells:** typography, imagery, hierarchy, colour and spacing [01:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=99s). See [[Escaping the Default AI Design Look]].
- **Show Claude a real product's design system,** with its hierarchy, palette and typography spelled out [02:28](https://www.youtube.com/watch?v=NAumQObJEwM&t=148s). See [[Design Systems for Claude]].
- **Name the gap before you ask for a fix.** If you can't say why a design is better, you can't direct Claude [05:34](https://www.youtube.com/watch?v=NAumQObJEwM&t=334s). See [[Benchmark-Driven Design Critique]].
- **Have separate critics judge the work against a benchmark** [10:16](https://www.youtube.com/watch?v=NAumQObJEwM&t=616s). See [[Multi-Agent Review and Scoring Loops]].
- **One connector hub can serve every harness** [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s). *Vault caveat:* that also gives each harness broad access. See [[Connecting Claude to External Tools]].
- **Design work benefits from an environment** that brings generation, asset search and reusable styles together [13:08](https://www.youtube.com/watch?v=NAumQObJEwM&t=788s). See [[Agentic OS]].

## The three levels at a glance

| Level | Input | Output | Reproducible from the video? | When |
|---|---|---|---|---|
| 1a · Apply a design system | Gallery spec plus a brief | A site in that style | Yes; the prompt is read out | [03:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=224s) |
| 1b · Ruthless comparison | Your site, plus the benchmark's page and screenshots | HTML gap report | Mostly; the skill isn't shown | [05:54](https://www.youtube.com/watch?v=NAumQObJEwM&t=354s) |
| 2 · Design loop | Benchmark screenshot plus a brief | HTML refined by three critics, sent through Zapier | Partly; no skill, rubric or stop rule | [09:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=584s) |
| 3 · Design OS | Prompt, provider, style recipe | Images with cost shown; a searchable library | No; only the finished app is shown | [13:33](https://www.youtube.com/watch?v=NAumQObJEwM&t=813s) |

## Notes by chapter

The metadata chapters are grouped here, and each heading lists the chapter titles it covers.

### [00:00](https://www.youtube.com/watch?v=NAumQObJEwM&t=0s) Killing AI Slop Forever · Three Techniques Overview · Why AI Designs Look Sloppy · The Five Telltale Signs

- **Three questions:**
  1. What is outstanding design, and how can Claude use it?
  2. How do you apply it to real work?
  3. How do you give Claude a "systematic advantage"?

  [00:33](https://www.youtube.com/watch?v=NAumQObJEwM&t=33s)
- **Diagnosis.** Models design poorly because they have never seen great design, so show them excellent human work. That holds in the Claude app and in [[Claude Design]] [01:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=64s). He credits the idea to "Mike" *(unidentified)*.
- **Five tells** recur in slop: typography, imagery, hierarchy, colour and spacing [01:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=99s). Give Claude the same prompt as everyone else and you get the same result [01:46](https://www.youtube.com/watch?v=NAumQObJEwM&t=106s).

### [01:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=119s) Level 1 · Apple Aesthetics Applied Anywhere · Protein Shake Site Built Live · Stunning Results In One Shot

- **The gallery** holds 2,000+ design systems from real products such as Wispr Flow, Phantom and Linear [01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s). He doesn't name it; Refero Styles matches (see Beyond the source). He says it isn't a sponsor [03:17](https://www.youtube.com/watch?v=NAumQObJEwM&t=197s).
- **Each entry** explains the design hierarchy, colour palette and typography [02:28](https://www.youtube.com/watch?v=NAumQObJEwM&t=148s). It also gives a Tailwind config, CSS variables and design tokens to copy [02:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=161s).
- **Demo.** He pastes Apple's spec into Claude. His prompt, in short: build a gorgeous site selling titanium protein shakes, and generate images if needed [03:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=224s).
- **Result.** It isn't perfect; he says the best designs come from iteration [04:09](https://www.youtube.com/watch?v=NAumQObJEwM&t=249s). Still, the Apple influence shows, with bottle visuals and a bento section, and he supplied no images [04:24](https://www.youtube.com/watch?v=NAumQObJEwM&t=264s).

### [04:50](https://www.youtube.com/watch?v=NAumQObJEwM&t=290s) Upgrade Your Existing Website · A Billion-Dollar Design Benchmark · Ruthless Design Comparison · Side-By-Side Design Gaps Revealed · Interactive Slider Shows The Difference

- **Use case:** improve a site you already have (his startup Glaido) using Linear's dark-mode design as the benchmark [05:12](https://www.youtube.com/watch?v=NAumQObJEwM&t=312s).
- **Why:** knowing a design looks good isn't the same as saying why, and only the explanation helps Claude [05:34](https://www.youtube.com/watch?v=NAumQObJEwM&t=334s).
- **His prompt, paraphrased** [05:54](https://www.youtube.com/watch?v=NAumQObJEwM&t=354s):
  - Compare the benchmark's gallery page with my site.
  - Be ruthless about the differences and about how to improve mine.
  - You may visit Linear's site and use screenshots.
  - Return a concise HTML breakdown [06:14](https://www.youtube.com/watch?v=NAumQObJEwM&t=374s).

  He calls this a skill [06:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=386s).
- **The report.**
  - **Three big gaps:** letter spacing too loose, no elevation ladder, and hero art that competes with the product [06:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=398s).
  - **Asked for more detail,** it added a slider showing Glaido's letter spacing against Linear's [06:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=411s).
  - **Further sections** set values side by side for shadows, accent frequency, border radius, vocabulary and display weight [07:25](https://www.youtube.com/watch?v=NAumQObJEwM&t=445s).
  - **Hex values** copy on click [07:47](https://www.youtube.com/watch?v=NAumQObJEwM&t=467s).
- **Action step:** run the comparison against a couple of sites you admire [08:02](https://www.youtube.com/watch?v=NAumQObJEwM&t=482s).

### [08:25](https://www.youtube.com/watch?v=NAumQObJEwM&t=505s) Beyond Websites · The Design Loop Method · Multi-Agent Critics Refine Output · Pixel-Perfect Email In One Shot · Anthropic Style Cloned Instantly

- **The design loop** is the most powerful design technique he has seen [08:34](https://www.youtube.com/watch?v=NAumQObJEwM&t=514s). It's his version of what its discoverer named the gauntlet loop [08:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=522s).
- **References** come from George Hartley's collection of great brand emails, including Apple and Figma [08:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=538s). The problem to solve is turning a picture of a good design into something you can use [09:15](https://www.youtube.com/watch?v=NAumQObJEwM&t=555s).
- **Steps:** screenshot a design (Apple's launch email), paste it into Claude, and run the design loop with a slash command [09:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=584s).
- **Mechanism.**
  1. You supply the benchmark [09:54](https://www.youtube.com/watch?v=NAumQObJEwM&t=594s).
  2. Claude spawns critics. His examples are benchmark fidelity ("proof", *unclear in captions*), design quality and visual impact [10:08](https://www.youtube.com/watch?v=NAumQObJEwM&t=608s).
  3. The three subagents loop until the output hits the mark [10:16](https://www.youtube.com/watch?v=NAumQObJEwM&t=616s).
- **The brief:** recreate this launch as HTML that looks right in an email, for Glaido's Windows launch, paying attention to the luminosity divide and energy [10:25](https://www.youtube.com/watch?v=NAumQObJEwM&t=625s). He calls the result one shot [10:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=638s).
- **Second example.** Anthropic's "Claude welcomes Claude Platform" email became a "Kastle Platform" email with an orange, Anthropic-style API-key button [11:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=673s).
- **His caveat:** don't just take the result. Ask what works, change specifics, or adapt from several references [11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s).

### [11:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=699s) Sending The Email For Real · Zapier Delivers Your Design · Gorgeous Email Lands In Inbox

- **Send:** in [[Claude Code]], tell Claude to use the Zapier connection to draft or send the HTML to himself, with a random subject line [11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s).
- **Why Zapier: his "authentication layer."** Tools connected in Claude have to be connected again in [[OpenAI Codex]], Antigravity and [[Hermes Agent]]. Connect Zapier once and every harness gets the same tools, Skool included [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s).
- **Result:** the email renders well and its button works [12:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=764s).

### [12:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=779s) Level 3 · Your Personal Design OS · Images Generated On Demand · Custom AI Images In Seconds

- **Premise:** give Claude an environment to work in, "one engine, one box" [13:08](https://www.youtube.com/watch?v=NAumQObJEwM&t=788s). He calls this level the most powerful of the three [11:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=711s).
- **Design OS:** a module inside his Claude Code operating system [13:33](https://www.youtube.com/watch?v=NAumQObJEwM&t=813s).
  - Pick a provider: [[Higgsfield]], Kie AI, OpenRouter or OpenAI [13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s).
  - Then set the model (Nano Banana 2), aspect ratio, resolution and image count. The UI shows what each generation costs [14:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=858s).
- **The wider OS** tracks usage and spend. It also reviews his chats locally every day and suggests new skills [14:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=889s). See [[Workflow Audit into Skills]].

### [15:05](https://www.youtube.com/watch?v=NAumQObJEwM&t=905s) Your Entire Image Library Searchable · Find Any Asset Instantly · Save Your Brand Style Recipe · Consistent Brand Thumbnails On Demand

- **Library.** Every image on his computer, searchable by what it shows ("burger") rather than just its metadata, because he indexed them with a model [15:22](https://www.youtube.com/watch?v=NAumQObJEwM&t=922s). You can copy an image to chat, download it, filter the library, and re-index with "magic scan" [15:46](https://www.youtube.com/watch?v=NAumQObJEwM&t=946s).
- **Style recipes.** A named style made of a text description plus reference images [16:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=986s). He picks his "Jack design" recipe and asks it to swap the object in the image for a giant protein shake. That's two 16:9 images at 2K, for 12 cents [16:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=1011s).
- **Use:** for consistent thumbnails, pick a recipe and change one element [17:17](https://www.youtube.com/watch?v=NAumQObJEwM&t=1037s).

### [17:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=1064s) What's Next

- **Next:** a follow-up video on the design loop [17:50](https://www.youtube.com/watch?v=NAumQObJEwM&t=1070s).

## Caveats & disagreements

**About the video**

- **Nothing to inspect.** He doesn't show the comparison skill [06:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=386s), the loop skill or the critic definitions. The loop has no pass bar, round cap or stop rule [10:16](https://www.youtube.com/watch?v=NAumQObJEwM&t=616s).
- **No loop cost.** "One shot" [10:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=638s) means one prompt that triggers hidden critic rounds, and no token figure is given. For an outside estimate, see Beyond the source.
- **How the images were made is never explained** [04:24](https://www.youtube.com/watch?v=NAumQObJEwM&t=264s). *Vault guess:* SVG or CSS drawings, or a connected tool. See [[Generating Images and Video with Claude]].
- **IP caution.** The Apple and Anthropic emails are recreated almost verbatim [11:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=673s), and his caveat is brief [11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s). *Vault view:* close copies of another brand's layout, look or copy can raise trademark, trade-dress or copyright issues. Take the principles, and replace the identity, copy and imagery.
- **No approval step.** Claude Code may draft *or send* through Zapier [11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s), and approval settings never come up. See [[Permissions and Approval Gates]].
- **Broad connector.** He points several harnesses at one Zapier connection [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s). *Vault view:* that concentrates access to many apps, so enable only the actions you need.
- **Level 3 can't be rebuilt from the video.** There's no architecture or setup, and the name of the indexing model is *unclear in captions* [15:22](https://www.youtube.com/watch?v=NAumQObJEwM&t=922s).
- **Omitted:** promotion of Glaido, including a promo code in the description; a paid masterclass and community pitch (13:12–13:31), through which the design OS is also offered; a meetup plug; and probable affiliate links.

**Conflicts with existing vault notes**

- **[[Escaping the Default AI Design Look]].**
  - *Vault:* keep references at pixel level (Lever 3), and treat clones as templates.
  - *Jack:* a token-level spec works well [02:28](https://www.youtube.com/watch?v=NAumQObJEwM&t=148s), yet his emails stay close to the originals [11:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=673s).
  - *Reading:* a curated spec sits between prose descriptions and pixel extraction.
  - *Diagnosis also differs:* AI LABS blame each model's house pattern, while Jack blames lack of exposure to great design [01:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=64s).
- **[[Multi-Agent Review and Scoring Loops]] and [[Build a Distinctive Site with Design Skills]].**
  - *Vault:* critics must cite evidence, and loops need thresholds, round caps and stop rules.
  - *Jack:* three visual critics loop until the work hits the mark, in "one shot" [10:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=638s).
  - *Fix:* add the vault's cap and pass bar.
- **[[Loop Engineering]].** A refinement rather than a conflict: the design loop, his version of the Gauntlet Loop [08:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=522s), adds a judge anchored to a concrete example. That note files it under "a benchmark as the yardstick".
- **[[Connecting Claude to External Tools]].** *Vault:* install only the MCP servers you need, and generate a CLI where no connector exists (as with Jay E's Skool CLI). *Jack:* one Zapier hub for every harness [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s).
- **[[Permissions and Approval Gates]].** *Vault:* drafts only, and a human approves every send. *Jack:* draft or send, with no gate [11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s).
- **[[Agentic OS]].** *Vault:* Jay E rates the interface at 20–30% of the value, and Chase calls the UI levels the "cherry on top". *Jack:* the environment level is the most powerful [11:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=711s).
- **[[Workflow Audit into Skills]].** A refinement rather than a conflict: a daily local review of chats suggests skills [14:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=889s). See [[Routines and Scheduled Tasks]].

**Other sources in this batch**

- [[Sergei Chyrkov - Claude Design Full Tutorial]] builds a design system from one inspiration image ([05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s)) and stresses that he isn't copying anyone's work ([04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s)). Jack's email recreations stay much closer to their originals.
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] finds that an image reference gets Claude only 50–60% of the way to your intent ([13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s)). That supports adding a critique pass or a loop.
- [[Nate Herk - Claude as a One-Person Marketing Team]] drives Higgsfield from inside Claude, so generation carries the business context ([02:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=177s)). Jack generates from a separate panel and uses style recipes instead.

## Build from this

*Starter guidance from the vault. Steps taken from the video carry timestamps.*

1. **Adopt and adapt a design system.**
   - Copy a benchmark spec [02:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=161s).
   - Adapt it to your brand and save it as `DESIGN.md` at the repo root.
   - Reference that file from CLAUDE.md.

   See [[Create and Reuse a Claude Design System]].
2. **Benchmark gap report.**
   - Screenshot your site and one benchmark at two widths.
   - Measure letter spacing, line height, radius, elevation, accent frequency and font weight.
   - Write `design/compare/<benchmark>.html`, leading with the three biggest gaps [06:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=398s).

   See [[Benchmark-Driven Design Critique]].
3. **Capped critic loop.**
   - Run a builder, then three fresh-context critics (fidelity, craft, impact) that compare the rendered output with the reference [10:08](https://www.youtube.com/watch?v=NAumQObJEwM&t=608s).
   - Pass only when every critic gives 8/10 or more with no blockers. Stop at a three-round cap, or earlier on a plateau or regression.
   - Log each round's scores, blockers, fixes and decision, plus the stop reason, in `design/loop/log.md`. Check token use after the run.

   See [[Multi-Agent Review and Scoring Loops]], [[Plan Before Executing]] and [[Context Window Management]].
4. **Gated HTML email.**
   - Write email-safe HTML: tables and inline CSS.
   - Screenshot it in a few email clients.
   - Draft through a connector [11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s), with send tools set to `ask`.

   See [[Permissions and Approval Gates]].
5. **Design panel and style recipes.**
   - Build a dashboard page with provider, size and a cost estimate [14:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=858s).
   - Store each recipe as `recipes/<name>/recipe.md` plus a `refs/` folder [16:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=986s).

   See [[Build an Agentic OS Dashboard]] and [[Generating Images and Video with Claude]].

## Resources mentioned

- **Design-system gallery** (likely Refero Styles): https://styles.refero.design [01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s)
- **Linear:** https://linear.app [05:12](https://www.youtube.com/watch?v=NAumQObJEwM&t=312s)
- **George Hartley's email collection:** https://nitrosend.com/best-email-designs [08:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=538s)
- **Gauntlet Loop video:** shown on screen, not linked [08:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=522s)
- **Zapier and agent harnesses:** Zapier, OpenAI Codex, Google Antigravity (https://antigravity.google), Hermes Agent (https://nousresearch.com) [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s)
- **Image providers and model:** Higgsfield, Kie AI, OpenRouter (https://openrouter.ai), OpenAI; Nano Banana 2 [13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s)

## Beyond the source

*Not in the video. Checked on 2026-09-15.*

- **Refero Styles** lists 2,000+ AI-readable design systems taken from product sites. Each has colours, typography, spacing, components and a DESIGN.md for tools such as Claude Code. Apple and Linear are included. https://styles.refero.design/
- **"47 Best Email Designs of 2026"** by George Hartley of Nitrosend (he previously founded SmartrMail, acquired in 2022) is a free Figma file with screenshots, notes and a DESIGN.md. It features Apple, Stripe and Figma; Anthropic isn't listed. https://nitrosend.com/best-email-designs
- **The Gauntlet Loop** was named by Matt Shumer in late July 2026. Each part of a goal gets a builder and a blind critic, and the critic passes work only if it beats a real-world equivalent. https://x.com/mattshumer_/status/2081830214384886228
  - A write-up of test runs says references the agent can inspect are load-bearing. Without them, the loop amplifies generic output at full cost. https://wotai.co/blog/gauntlet-loop-playbook
- **Jack's earlier video** (2026-08-10) describes three critics, about 2–3M tokens per run and a free skill, according to a third-party summary. https://www.dutchstartup.ai/en/tv/this-new-prompting-technique-just-10x-d-claude-design
- **Zapier MCP for Claude Code:** run `claude mcp add --transport http "Zapier-MCP" https://mcp.zapier.com/api/v1/connect`, then sign in to Zapier. Tools are enabled afterwards by following Zapier's onboarding skill. https://docs.zapier.com/mcp/get-started/connect/claude-code
- **Gating MCP tools:** permission rules accept `mcp__<server>` or `mcp__<server>__<tool>`. Put send tools under `ask`. https://code.claude.com/docs/en/permissions

## Transcript notes

| Caption | Reading |
|---|---|
| "Glido", "Glider" | Glaido |
| "Whisper flow" (02:06) | Wispr Flow |
| "George Harley" (08:58) | George Hartley (likely) |
| "Does it hit the proof?" (10:08) | probably benchmark fidelity *(unclear in captions)* |
| "Kastle" (11:13) | placeholder brand *(unclear in captions)* |
| "authentication lamp" (12:15) | authentication layer |
| "school" (12:31) | Skool (likely) |
| "KAI" (13:49), "Nana Banana too" (14:13) | Kie AI, Nano Banana 2 (likely) |
| "Karuchi model" (15:24) | unidentified image-indexing model |
| "60 by 9" (16:51), "Hicks field" (17:32), "design lip" (17:50) | 16:9, Higgsfield, design loop |
| "explained by Mike" (01:04) | unattributed |

## Related

- **Home:** [[Home]]
- **Concepts:** [[Design Systems for Claude]] · [[Escaping the Default AI Design Look]] · [[Loop Engineering]] · [[Generating Images and Video with Claude]] · [[Agentic OS]]
- **Techniques:** [[Create and Reuse a Claude Design System]] · [[Benchmark-Driven Design Critique]] · [[Multi-Agent Review and Scoring Loops]] · [[Build an Agentic OS Dashboard]]
- **Tools:** [[Claude Design]] · [[Claude Code]] · [[Higgsfield]]
- **Sources:** [[Sergei Chyrkov - Claude Design Full Tutorial]] · [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] · [[Nate Herk - The Scrollcraft Website Design Skill]] · [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[AI LABS - Types of Claude Loops Explained]]
- **People:** [[Jack Roberts]] · [[Sergei Chyrkov]]
