---
type: source
title: "Turn Claude Into a One Person Marketing Team in 38 Mins"
creator: "[[Nate Herk]]"
channel: "Nate Herk | AI Automation"
url: https://www.youtube.com/watch?v=yCACmFTiCto
video_id: yCACmFTiCto
published: 2026-08-21
duration: "38:28"
ingested: 2026-09-15
topics: [marketing, brand context, three Ps, Claude Code desktop, custom MCP connectors, Higgsfield, AI image and video, scroll-driven websites, UGC ads, skills, creative tracking]
tags: [source/youtube, topic/marketing, topic/media, topic/claude-code, topic/mcp, topic/design, topic/context, topic/skills, topic/verification]
---

# Nate Herk - Claude as a One-Person Marketing Team

> **Creator:** [[Nate Herk]] · **Published:** 2026-08-21 · **Length:** 38:28 · [Watch on YouTube](https://www.youtube.com/watch?v=yCACmFTiCto)

## TL;DR

A walkthrough for beginners who don't code. [[Nate Herk]] builds a marketing project in the [[Claude Code]] desktop app for Perkform, a canned coffee-protein drink brand he made up. He writes a "three Ps" brief (pain, person, promise) and has Claude turn it into a short CLAUDE.md plus context files. He drops logos, product shots and a brand-guidelines PDF into an assets folder. Then he adds [[Higgsfield]], a paid bundle of image and video models, as a custom MCP connector.

With one plain-language prompt each, he gets:

- a scroll-animated site built with the third-party Scroll World skill;
- 18 BOGO ad creatives, a sizzle reel and five Instagram carousels;
- UGC-style video ads that Claude storyboards and checks itself;
- an Excel creative tracker in the brand's colours.

Claude reports costs only after the runs, and gives no figure for the UGC run. His case for working through Claude rather than Higgsfield's own interface: the project carries business context, brand guidelines and, eventually, skills. He builds no skills, does no planning and deploys nothing, and he admits the first passes need human work.

## Key takeaways

- **Give assets intent.** Without the three Ps, he says, assets look like generic AI slop [02:00](https://www.youtube.com/watch?v=yCACmFTiCto&t=120s). See [[Build a Brand-Aware Marketing Project]].
- **The project is the advantage, not the model.** Context, skills and guidelines are what Claude adds over Higgsfield's own UI [02:56](https://www.youtube.com/watch?v=yCACmFTiCto&t=176s). The guidelines even reached an Excel sheet without being asked [36:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=2184s). See [[Design Systems for Claude]] and [[Escaping the Default AI Design Look]].
- **One connector, many models.** Claude does the prompting and navigates Higgsfield for you [05:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=318s). See [[Connecting Claude to External Tools]] and [[Generating Images and Video with Claude]].
- **Brief Claude like a colleague.** State the motivation, the end goal and where to save, and ask for the cost [24:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1442s). Add any ad expertise you have [27:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=1642s).
- **Plan video with images first.** Claude made characters, then storyboards, then clips, then ran QA [31:50](https://www.youtube.com/watch?v=yCACmFTiCto&t=1910s). See [[Storyboard-First AI Video and Motion Graphics]].
- **Turn taste into skills.** Outputs you liked become skills, and outputs you disliked become rules against repeating them [30:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1807s). See [[Build a Skill from a Successful Run]].
- **Volume first, then data.** Generate many creatives, then review performance weekly [30:48](https://www.youtube.com/watch?v=yCACmFTiCto&t=1848s). See [[Routines and Scheduled Tasks]].

## Deliverables at a glance

| Deliverable | Asked for | Came back | Cost (his account) | Prompt | Build note |
|---|---|---|---|---|---|
| Context base | Owner, business, three Ps, marketing angles; create CLAUDE.md and context files | CLAUDE.md router, 7 context files, open-questions file, empty assets/ and output/ | — | [08:28](https://www.youtube.com/watch?v=yCACmFTiCto&t=508s) | [[Build a Brand-Aware Marketing Project]] |
| Website | Assets plus Scroll World; premium but fun; copy built on the three Ps | Scroll-scrubbed site with Seedance 2.5 clips; localhost only; placeholder nutrition facts | — | [17:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1073s) | [[Build a Scroll-Driven Landing Page]] |
| BOGO ads | Many test creatives; report cost; save to a summer BOGO folder | 18 on-brand images, some copy-free, plus ad copy and run notes | $3.43 | [22:09](https://www.youtube.com/watch?v=yCACmFTiCto&t=1329s) | [[Generate On-Brand Images from Claude Code]] |
| Sizzle reel | Marketing Studio, for music and fast edits | Vertical and landscape reels; logo slightly wrong | ~$17.55 | [22:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=1377s) | [[Generating Images and Video with Claude]] |
| Carousels | Instagram launch posts on why, who, the pain and the flavours; which to pin | 5 carousels of 7–8 slides | $9.56 | [23:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1401s) | [[Generate On-Brand Images from Claude Code]] |
| UGC ads | Vertical, organic-feeling reviews by the target person | Characters, storyboards, QA folder, fast-cut clips | "Most expensive" (not given) | [24:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1450s) | [[Storyboard-First AI Video and Motion Graphics]] |
| Tracker | Excel sheet: date, type, outputs, core angle | Six-tab workbook in brand colours, built in ~8 minutes | — | [35:25](https://www.youtube.com/watch?v=yCACmFTiCto&t=2125s) | [[Build a Brand-Aware Marketing Project]] |

## Notes by chapter

### [00:00](https://www.youtube.com/watch?v=yCACmFTiCto&t=0s) What We're Building

- The pitch: you need no technical, video or photo skills, only to know what to ask for [00:00](https://www.youtube.com/watch?v=yCACmFTiCto&t=0s). There are three steps: set up the project, connect Higgsfield, then generate assets [00:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=18s).
- Claude and Higgsfield made Perkform's logos and its product shots for three flavours before recording [00:47](https://www.youtube.com/watch?v=yCACmFTiCto&t=47s), using GPT Image 2 [01:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=76s).

### [01:38](https://www.youtube.com/watch?v=yCACmFTiCto&t=98s) The Three Ps

- **The framework.** Pain is what the business solves, person is who specifically feels it, and promise is how the brand solves it for them [01:39](https://www.youtube.com/watch?v=yCACmFTiCto&t=99s). You need these before you can set up the project [01:54](https://www.youtube.com/watch?v=yCACmFTiCto&t=114s).
- **Higgsfield.** Many video and image models come under one subscription [02:13](https://www.youtube.com/watch?v=yCACmFTiCto&t=133s). Its Marketing Studio templates turn your assets into ad creatives or sizzle reels [02:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=165s).
- **Why go through Claude.** Skills work like recipes, so a carousel or UGC ad comes out the same way every time [03:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=187s). Brand guidelines (colours, logo system, typography) apply to every deliverable [03:19](https://www.youtube.com/watch?v=yCACmFTiCto&t=199s).
- **Perkform's version.** The person is a busy, fitness-minded professional who rushes breakfast [03:48](https://www.youtube.com/watch?v=yCACmFTiCto&t=228s). The pain is needing too many separate morning products [03:54](https://www.youtube.com/watch?v=yCACmFTiCto&t=234s). The promise is coffee and protein in one grab-and-go can [04:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=242s).
- **No logo yet?** Make one first in Higgsfield's image tool; he'd pick GPT Image 2 [04:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=281s).

### [05:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=327s) Set Up Claude Code

- **The app.** Install the Claude Code desktop app. It looks like a chat app, but you pick a folder to work in [05:30](https://www.youtube.com/watch?v=yCACmFTiCto&t=330s).
- **"Code" doesn't mean coding.** It works out of folders, so the project learns more about your business over time [05:56](https://www.youtube.com/watch?v=yCACmFTiCto&t=356s).
- **The brand kit came from here too.** He gave Claude the Perkform idea and asked for shots, logos and guidelines. It created the folders on his desktop [06:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=378s).

### [07:12](https://www.youtube.com/watch?v=yCACmFTiCto&t=432s) Build Your Marketing Project

- **Open the project.** Create an empty folder, sign in with your subscription and start a new chat [07:42](https://www.youtube.com/watch?v=yCACmFTiCto&t=462s). Open the folder and click Trust workspace, which lets Claude read, add, edit and move files there [08:04](https://www.youtube.com/watch?v=yCACmFTiCto&t=484s).
- **First prompt.** Say who you are and what the business does, and that Claude is your marketing team for ads, a website and UGC. Ask it to create CLAUDE.md plus whatever context files it thinks are useful [08:28](https://www.youtube.com/watch?v=yCACmFTiCto&t=508s). Then paste in the three Ps, business details and marketing angles [09:29](https://www.youtube.com/watch?v=yCACmFTiCto&t=569s).
- **Watch progress.** Three dots > Files shows files as they appear [09:52](https://www.youtube.com/watch?v=yCACmFTiCto&t=592s).
- **Grill Me.** His version is one big markdown prompt that interviews you relentlessly [10:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=622s). Install it by dragging the file into the chat and asking Claude to install it in the project [10:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=653s). Run it on your product and marketing: it asks one question at a time and saves the interview [11:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=665s). See [[Grill Me Interview Skill]].
- **What Claude built.** Empty output/ and assets/ folders, plus a context folder [11:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=696s). The context files are brand positioning (holding the three Ps), customer avatar, product facts, voice and copy, message bank, playbooks and landscape [11:55](https://www.youtube.com/watch?v=yCACmFTiCto&t=715s). The positioning file also says what the brand is not, e.g. not a gym-bro brand [13:11](https://www.youtube.com/watch?v=yCACmFTiCto&t=791s).
- **CLAUDE.md.** The summary he reads out calls it the "operating doc" [11:47](https://www.youtube.com/watch?v=yCACmFTiCto&t=707s). It is tiny: it names the project and owner, then says to read the context files before writing anything [12:33](https://www.youtube.com/watch?v=yCACmFTiCto&t=753s). He expects to add to it daily or weekly [12:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=765s).

### [13:25](https://www.youtube.com/watch?v=yCACmFTiCto&t=805s) Add Your Brand Assets

- **Add the files.** Drag logos, the product-shots folder and the guidelines PDF into assets/ using your file explorer [14:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=841s). Copies work too [14:14](https://www.youtube.com/watch?v=yCACmFTiCto&t=854s).
- **If something looks off, ask Claude what it sees.** The Files panel showed the product shots oddly. He asked, and Claude read and listed all 11 images [15:04](https://www.youtube.com/watch?v=yCACmFTiCto&t=904s).

### [15:51](https://www.youtube.com/watch?v=yCACmFTiCto&t=951s) Build A Website

- **Scroll World** is a public GitHub repo for 3D, scroll-driven sites, which Claude pairs with Higgsfield video [16:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=961s).
- **Connect Higgsfield.** You need an account on a plan first [16:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=987s).
  1. In Higgsfield, open "MCP and CLI", choose Claude and copy the URL [16:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=992s).
  2. In Claude, go to Customize > Connectors > Add custom connector. Paste the URL, name it Higgsfield and click Add [16:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1001s).
  3. Click Connect, sign in and allow access [16:54](https://www.youtube.com/watch?v=yCACmFTiCto&t=1014s).
- **Website prompt.** Paste the repo URL [17:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1047s). Ask Claude to think carefully about design and combine the assets with Scroll World into something premium yet fun [17:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1073s). Have it shape the copy and structure around the target person's pain and the promise [18:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1090s).
- **Why it works, he says.** Context and assets keep a site from looking generic and bland [18:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1115s).

### [19:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=1141s) Website Demo

- **How Claude approached it.** It said it took the design system from the guidelines PDF rather than inventing one [19:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1150s), and opened on the pain, not the product [19:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=1156s).
- **The page.** As you scroll, a coffee and a protein shake merge into one can [19:40](https://www.youtube.com/watch?v=yCACmFTiCto&t=1180s). The flavour sections play Seedance 2.5 clips forward in step with the scroll [20:39](https://www.youtube.com/watch?v=yCACmFTiCto&t=1239s).
- **Limits.** He calls it more distinctive than a typical first-pass AI site, but says not to expect perfection from one prompt [20:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1207s). The nutrition facts are placeholders [20:19](https://www.youtube.com/watch?v=yCACmFTiCto&t=1219s). It runs only on localhost [21:04](https://www.youtube.com/watch?v=yCACmFTiCto&t=1264s). Publishing (GitHub, then Vercel) is left for another video [21:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1295s).

### [21:43](https://www.youtube.com/watch?v=yCACmFTiCto&t=1303s) Generate Marketing Assets

- **Four prompts at once.** He sends them into the same chat and they run together [22:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1322s); the table above summarises each.
- **Liked it? Make it a skill,** so future outputs match [25:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1507s).

### [25:14](https://www.youtube.com/watch?v=yCACmFTiCto&t=1514s) Ads, Reels & Carousels

- **Folders.** Each campaign gets its own folder of images, a V1 backup, ad copy and run notes [25:47](https://www.youtube.com/watch?v=yCACmFTiCto&t=1547s).
- **Ads.** They use the brand fonts and colours, with consistent product renders [26:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=1561s). Some are blank for your own copy [26:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1618s). Next promotion, change only the call to action or copy instead of regenerating [27:09](https://www.youtube.com/watch?v=yCACmFTiCto&t=1629s). Or work the other way: take one copy line you like, put it on all 18 graphics and run them as a new round of ads [27:12](https://www.youtube.com/watch?v=yCACmFTiCto&t=1632s).
- **Cost.** He admits Higgsfield isn't the cheapest route, but it gathers the models in one place and adds Marketing Studio [27:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1673s).
- **Sizzle reels.** The logo wasn't quite right [28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s). Video costs more than images but far less than hiring an editor [29:18](https://www.youtube.com/watch?v=yCACmFTiCto&t=1758s).
- **Carousels.** Branding stayed consistent across them [29:31](https://www.youtube.com/watch?v=yCACmFTiCto&t=1771s).

### [31:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1867s) UGC Ads & QA

- **The pipeline.** The run created four folders: boards, creators, QA and video [31:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=1882s).
  1. Four character images, reusable as a brand avatar [31:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=1905s).
  2. Storyboards for each shot, giving tighter control over the story [31:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1918s).
  3. Clips, then a QA pass that screenshotted the videos [32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s) and rejected at least one before reporting done [32:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1978s).
- **Verdict.** The ads were realistic but read as AI, and too salesy to feel organic [33:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=2007s). His fix is to have Claude study real UGC or draft scripts for your approval before generating [33:34](https://www.youtube.com/watch?v=yCACmFTiCto&t=2014s).
- **Editing and effort.** His brief invited both styles, some more edited and some a raw take [24:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1481s), yet every clip shown came cut into one- to two-second pieces, which he says Claude chose over a raw 15-second take [34:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=2056s). *Vault reading:* name the edit style for each variant rather than asking loosely for a mix. He also stresses these are use cases, which still need your own research and touch [34:42](https://www.youtube.com/watch?v=yCACmFTiCto&t=2082s).

### [35:14](https://www.youtube.com/watch?v=yCACmFTiCto&t=2114s) Build A Creative Tracker

- **Why track.** Output folders get messy, so keep a sheet that Claude can later update with views or conversions [35:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=2121s).
- **The build.** Claude scanned sessions and outputs for about eight minutes [36:09](https://www.youtube.com/watch?v=yCACmFTiCto&t=2169s).
- **Tabs.** An overview, then a generation log with ID, date, type, campaign, channel, angles, deliverables, generations billed, tool and model, credits, dollars and status [36:46](https://www.youtube.com/watch?v=yCACmFTiCto&t=2206s). Also creative assets, angle performance, a copy bank and a cost summary [37:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=2255s).
- **Models chosen by Claude.** The UGC brief names Seedance 2.5 but lets Claude try other models [24:50](https://www.youtube.com/watch?v=yCACmFTiCto&t=1490s), and the tool/model column records each run's pick: Nano Banana Pro, Marketing Studio, GPT Image 2, then Soul, GPT Image and Seedance 2.5 [36:59](https://www.youtube.com/watch?v=yCACmFTiCto&t=2219s). Matching rows to runs by order (an inference), that's ads, reel, carousels and UGC, so the BOGO ads apparently used Nano Banana Pro, not GPT Image 2.
- **Suggested, not built.** An automated sweep to keep the sheet current [37:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=2241s), using the sheet as an intake queue where you drop ideas and Claude processes anything new [37:23](https://www.youtube.com/watch?v=yCACmFTiCto&t=2243s), and weekly research that scrapes other creatives into an ideas list [37:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=2247s).

### [37:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=2277s) Final Thoughts

- **Recap.** Connecting Higgsfield to Claude is about bringing context, skills and guidelines into generation [38:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=2287s).

## Caveats & disagreements

**About the video**

- **Promotion.** Higgsfield is the backbone of the video. The first description link is a Higgsfield referral link, and the transcript discloses no affiliation. His claim that Seedance 2.5 early access is only on Higgsfield [02:20](https://www.youtube.com/watch?v=yCACmFTiCto&t=140s) is marketing that will date. Paid-programme, community, course and discount links are omitted here.
- **Paid credits with no gate.** Cost is only reported after the run [22:37](https://www.youtube.com/watch?v=yCACmFTiCto&t=1357s), while several paid jobs run at once. There is no estimate, cap or approval step. See [[Permissions and Approval Gates]].
- **Skips planning.** There is no plan mode and no clarifying questions before large paid runs [22:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1322s). His own [[Nate Herk - 32 Tricks to Level Up Claude Code]] says to always start in plan mode [02:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=168s). See [[Plan Before Executing]].
- **The agent grades itself.** The only QA is Claude checking its own UGC [32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s). A wrong logo still shipped in the reel [28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s). Compare the screenshot-and-fix passes in 32 Tricks [09:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=564s). See [[Verification Before Done]].
- **Unmeasured results.** The brand is fake and its kit was generated before recording. Quality is judged by eye. The costs are what Claude reported when asked [22:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1355s), or for the reel a figure "based on my credits" [29:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1746s), and none is checked independently. Skills are discussed but never built [25:07](https://www.youtube.com/watch?v=yCACmFTiCto&t=1507s).
- **Flags, not endorsements.** The logo demo uses a real SaaS brand name, Calendly [04:49](https://www.youtube.com/watch?v=yCACmFTiCto&t=289s). The UGC ads are AI people "reviewing" a product [24:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1467s); see the FTC note below.

**Versus existing vault notes**

- **[[Keep CLAUDE.md Lean]].** He'd grow CLAUDE.md daily or weekly with no cap [12:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=765s). That note, like his own 150–200-line cap [07:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=426s), says to trim and route out. His generated file does start small and route out [12:33](https://www.youtube.com/watch?v=yCACmFTiCto&t=753s).
- **[[Build vs Install Third-Party Skills]].** He installs a downloaded skill by drag-and-drop [10:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=653s) and a repo by pasting its URL [17:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1047s), without reading either. That note's cautious side says to review others' skills or build your own.
- **[[Grill Me Interview Skill]].** A refinement: he uses it to capture marketing thinking [11:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=665s) and installs it as a single file [10:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=622s). The documented format is a folder containing SKILL.md.
- **[[Connecting Claude to External Tools]].** He adds a claude.ai custom connector [16:41](https://www.youtube.com/watch?v=yCACmFTiCto&t=1001s) rather than using `claude mcp add`. Both work, but connectors reach Claude Code only on a claude.ai login.
- **[[Escaping the Default AI Design Look]].** That note stresses design skills, references and review loops. He relies on brand context and a single one-prompt pass [18:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1115s), which adds brand guidelines as a lever.
- **[[Context vs Connections]].** He'd copy views and conversions into the tracker [35:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=2121s). That note leaves volatile data in its source system and fetches it when needed.

## Build from this

1. **Brand workspace.** A CLAUDE.md router, three-Ps positioning with a "what we're not" list, assets/, and output/ organised by campaign. See [[Build a Brand-Aware Marketing Project]].
2. **Spend-gated generation.** Put generation tools behind `ask` rules, estimate credits before each batch, and log the cost to the tracker. See [[Generate On-Brand Images from Claude Code]].
3. **Format skills from approved runs.** Build one each for ad sets, carousels, reels and UGC, each reading the positioning and guidelines first. See [[Build a Skill from a Successful Run]] and [[Audit Skill Descriptions and Triggers]].
4. **UGC with approved scripts.** Scripts → characters → storyboards → clips → a separate brand-QA check → a disclosure check. See [[Storyboard-First AI Video and Motion Graphics]].
5. **Verified scroll site.** Vet the skill, fill every fact from product-facts, run screenshot checks, then deploy. See [[Build a Scroll-Driven Landing Page]].
6. **Weekly creative review.** A scheduled job that joins platform metrics to tracker IDs and drafts next week's brief. See [[Schedule Recurring Claude Tasks]].

## Resources mentioned

- **Claude:** the Claude Code desktop app, CLAUDE.md, and Customize > Connectors > Add custom connector.
- **Higgsfield:** the "MCP and CLI" page, Marketing Studio, and models including Seedance 2.5, Kling, Sora and GPT Image 2 [02:25](https://www.youtube.com/watch?v=yCACmFTiCto&t=145s), with Nano Banana Pro and Soul appearing in the tracker [36:59](https://www.youtube.com/watch?v=yCACmFTiCto&t=2219s).
- **Skills:** Grill Me (his version); Scroll World, at github.com/oso95/scroll-world [16:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=961s).
- **Other:** GitHub, Vercel, and Excel or Google Sheets.

## Beyond the source

*Not from the video. Checked 2026-09-15 at the linked pages.*

- **Higgsfield MCP.** The URL is `https://mcp.higgsfield.ai/mcp`. Higgsfield requires an active paid subscription, and every generation through an agent deducts credits whatever your plan. In Claude Code, `@higgsfield/cli` is an alternative. An "Unlimited MCP" trial (posted 2026-07-28) gave new users 24 hours with no credit charges on a listed set of models, but it was only offered until 2026-07-31. <https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent>, <https://higgsfield.ai/blog/unlimited-mcp>
- **Custom connectors.** Available on Free (one connector), Pro, Max, Team and Enterprise; on Team and Enterprise only Owners can add them. Claude connects from Anthropic's cloud. Anthropic advises using only trusted servers and reviewing tool calls before choosing "Allow always". <https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp>
- **Connectors in Claude Code.** They load only under a claude.ai subscription login, not an API key. List them with `/mcp`, or disable them with `disableClaudeAiConnectors`. The terminal equivalent is `claude mcp add --transport http <name> <url>`. <https://code.claude.com/docs/en/mcp>
- **Gating paid tools.** Permission rules can target `mcp__<server>` or `mcp__<server>__<tool>`. Tools from connectors that Claude Code fetches itself appear as `mcp__claude_ai_<server>__<tool>`. An `ask` rule makes Claude confirm each call. <https://code.claude.com/docs/en/permissions>
- **Scroll World.** An MIT-licensed skill, installed with `/plugin marketplace add oso95/scroll-world` and then `/plugin install scroll-world@scroll-world`. It needs ffmpeg, Python 3 with Pillow, and paid backends: Monid pay-per-clip video by default, with Higgsfield credits for stills and as the video fallback. Its README warns that generation costs money and states the estimated total before spending. <https://github.com/oso95/scroll-world>
- **AI "reviews" in US ads.** The FTC's final rule on reviews and testimonials, announced August 2024, bans testimonials that misrepresent that they come from someone who doesn't exist (including AI-generated ones) or who lacks real experience of the product. <https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials>

## Transcript notes

Caption fixes applied throughout: Higgsfield, Seedance 2.5, GPT Image 2, CLAUDE.md, Skool, Claude Code. Non-obvious ones:

| Caption | Corrected |
|---|---|
| "UDC ad" (03:15) | UGC ad |
| "Perk Form" | Perkform (fictional; capitalisation *uncertain*) |
| "vanilla, latte, salted caramel, and bold mocha" (01:07) | three flavours: vanilla latte, salted caramel, bold mocha (he says three at 20:24) |
| "custom avatar" (11:57) | customer avatar |
| "this guy named Oso" (16:03) | GitHub user oso95 |
| "what Hicksfield can actually host" (18:52) | *unclear in captions*; probably "provide" |
| "our ad creators" (25:05) | ad creatives |
| "make a scale around that one" (30:02) | make a skill |
| "17.55 cents" (29:06) | about $17.55 (he contrasts it with three and 20 dollars) |
| "Jen's build" (36:56) | generations billed |
| 32:38–34:12 | voiceover from the generated ads, not Nate |

## Related

- **Concepts:** [[Design Systems for Claude]], [[Generating Images and Video with Claude]], [[Agent Skills]], [[Verification Before Done]], [[CLAUDE.md as a Router]], [[Routines and Scheduled Tasks]], [[Agentic OS]]
- **Techniques:** [[Create and Reuse a Claude Design System]], [[Benchmark-Driven Design Critique]], [[Build a Distinctive Site with Design Skills]], [[Skill Improvement Loop]], [[Build a Reference-Rich Skill]], [[Workflow Audit into Skills]], [[Build Verification into Every Task]], [[Build an Agentic OS Dashboard]], [[Build a Level 1 Second Brain]]
- **Tools and people:** [[Claude Code]], [[Higgsfield]], [[Scrollcraft]], [[Claude Design]], [[Nate Herk]], [[Jay E]], [[Chase AI]], [[AI LABS]]
- **Same creator:** [[Nate Herk - The Scrollcraft Website Design Skill]] (his own scroll-site skill, with screenshot self-checks), [[Nate Herk - Build Skills Instead of Agents]], [[Nate Herk - Every Level of a Claude Second Brain]]
- **Related sources:** [[Jay E - Claude and GPT-Image-2 for On-Brand Design]], [[Chase AI - GPT-6 Astra Motion Design in After Effects]], [[Jack Roberts - Design Systems, Critic Loops and a Design OS]], [[AI LABS - Design Skills from Landing Pages to Mobile Apps]], [[Simon Pittman - Set Up Claude Cowork]]
- [[Home]]
