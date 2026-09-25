---
type: concept
aliases: ["AI Media Generation", "Image Generation"]
sources: ["[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]", "[[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]", "[[Nick Saraev - Animated Sites with Claude Code and Kling]]"]
tags: [topic/media, topic/marketing, topic/design, topic/skills, topic/mcp, topic/verification]
---

# Generating Images and Video with Claude

## In one sentence

Claude doesn't produce the images or video here. It plans assets, writes prompts and calls an outside model, then files, checks and costs the results.

## How it works

### Why go through Claude

- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] connects GPT Image 2 to Claude so Claude writes the prompts instead of you ([04:30](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=270s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]] could use Higgsfield's own interface. Going through a Claude project adds business context, repeatable skills and brand guidelines ([02:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=177s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]] points out the gap: GPT-6 Astra generates images natively, while Claude Code needs something like the Higgsfield MCP added ([02:54](https://www.youtube.com/watch?v=C8dWdic-oK4&t=174s)).
- [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]] states the thesis plainly: because Claude has no native image or video model, he adds the Higgsfield MCP connector to Claude Code, and Claude writes every image and video prompt from his spoken description — he never types one himself ([02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s), [08:30](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=510s)). The stills come from GPT Image 2.5, the animation from Seedance 2.5.
- [[Nick Saraev - Animated Sites with Claude Code and Kling]] keeps Claude Code as the orchestrator: it writes the site code and wires the finished clips in, while Nick writes the image/video generation prompts himself and the visuals come from Nano Banana Pro stills fed into Kling 3.0 ([04:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=286s)). (Contrast Jason Lee, where Claude writes the asset prompts too, through the Higgsfield MCP.)

### Four routes to a model, plus one with no model

| Route | Source | Wiring | Watch for |
|---|---|---|---|
| **A skill that calls an aggregator API** | Jay E (fal.ai), Scrollcraft (Kie.ai) | Jay's skill lets Claude set references, quality, resolution, image count and format ([07:19](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=439s)). Scrollcraft reads a Kie.ai key from the project env, and the skill tells Claude how to make images, turn them into clips and stitch those together ([05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s)) | You hold the key and pay the bill. Jay adds a new model by pasting its fal docs into the session ([11:49](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=709s)) |
| **A vendor MCP connector** | Nate (marketing), AI LABS | Higgsfield is added as a custom connector, and Claude then does the prompting ([16:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1004s)). AI LABS request hero images and clips from inside the agent ([10:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=647s)) | One subscription covers many models, but Nate says it isn't the cheapest ([27:48](https://www.youtube.com/watch?v=yCACmFTiCto&t=1668s)) |
| **A vendor plugin for a desktop app** | Chase | Higgsfield's Motion Designer connects the model to After Effects with bundled skills, working through scripts and computer use ([01:27](https://www.youtube.com/watch?v=C8dWdic-oK4&t=87s)) | Shown in Codex rather than Claude. A 15–20 second graphic can take 10–20 minutes ([02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s)) |
| **A provider panel in a local OS** | Jack Roberts | Pick Higgsfield, Kie AI, OpenRouter or OpenAI for each generation, with the cost shown ([13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s), [14:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=858s)) | Demo only |
| **No media model: Claude writes code that renders it** | u/AzorAhai1TK (Reddit) | Claude Code draws the frames with numpy (including a 3D raycast) and cairo, synthesises audio with numpy and scipy, voices a script with Piper TTS, and assembles it all with [[FFmpeg]] ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbexf59/)). A commenter cuts real footage with FFmpeg the same way ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbh9qmt/)) | No generation credits, and everything runs locally. The look is stylised: one viewer found it a bit mechanical ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf7nvy/)) |

### Patterns the sources share

1. **Send brand references with every request.**
   - Jay passes the brand book and logo as file paths. He has Claude convert the PDF to JPEG first, because the model won't accept PDFs ([08:16](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=496s)).
   - Jack saves "style recipes", each a description plus reference images, to keep thumbnails consistent ([16:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=986s)).
   - Scrollcraft asks which real assets you already own, which decides how much it generates ([05:55](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=355s)).
2. **Generate in volume, then pick.**
   - Jay says image models need volume and variation so you can steer toward what works ([10:03](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=603s)).
   - His numbered 5x5 grid is billed as one image ([10:11](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=611s)). Ask for one cell at top quality and Claude finds the prompt it used for that cell ([11:13](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=673s)).
   - Nate: the more you make, the less you rely on luck ([30:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=1824s)).
3. **Plan video with images first.**
   - Chase storyboards first because After Effects passes are slow ([01:51](https://www.youtube.com/watch?v=C8dWdic-oK4&t=111s)). The storyboard then supplies the beats for the build prompt ([04:50](https://www.youtube.com/watch?v=C8dWdic-oK4&t=290s)), and reference videos can set the motion style ([03:26](https://www.youtube.com/watch?v=C8dWdic-oK4&t=206s)).
   - Nate's UGC run made character images, then storyboards, then video ([31:29](https://www.youtube.com/watch?v=yCACmFTiCto&t=1889s), [31:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1913s)).
   - Jay animates an approved still with Kling, keeping its text and aspect ratio fixed ([12:43](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=763s)).
4. **The agent checks its own media.**
   - Nate's UGC run screenshotted its clips and rejected at least one ([32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s)).
   - Scrollcraft screenshots and inspects the page it built ([08:52](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=532s)).
   - Chase's plugin checks the build against the storyboard, renders it, then reviews the render ([06:05](https://www.youtube.com/watch?v=C8dWdic-oK4&t=365s)).
   - The catch is that the worker grades itself: Nate's sizzle reel still had a slightly wrong logo ([28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s)), and Scrollcraft's keyframe pass let a wrong photo caption through ([11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s)). See [[Verification Before Done]].
5. **Track cost.**
   - Nate ends prompts by asking what the run cost ([22:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1355s)): $3.43 for 18 ads ([27:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=1656s)), $9.56 for five carousels ([30:57](https://www.youtube.com/watch?v=yCACmFTiCto&t=1857s)), about $17.55 for a sizzle reel ([29:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1746s)).
   - He leaves model choice to Claude: the UGC brief names Seedance 2.5 but invites other models ([24:50](https://www.youtube.com/watch?v=yCACmFTiCto&t=1490s)). The tracker then logs each run's tool and model beside its cost ([36:59](https://www.youtube.com/watch?v=yCACmFTiCto&t=2219s)). *Inferred from row order:* Nano Banana Pro for the ads, Marketing Studio for the reel, GPT Image 2 for the carousels, and Soul, GPT Image and Seedance 2.5 for UGC ([37:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=2225s)).
   - Scrollcraft's cost goes unmentioned, but Nate's Kie.ai logs list the images and videos it generated for his sites ([04:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=297s)).
   - Jack's panel shows 12 cents for two images before generating ([16:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=1011s)).
   - Settings matter: one of Jay's posts came out pixelated, not made at top resolution ([02:07](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=127s)).
6. **Make assets you can reuse.**
   - Nate's BOGO brief asked for varied copy and images ([22:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=1344s)). Claude also returned some copy-free versions on its own, so the next promotion can swap copy or CTA instead of regenerating ([26:58](https://www.youtube.com/watch?v=yCACmFTiCto&t=1618s)). His generated characters can serve as a recurring brand avatar ([31:45](https://www.youtube.com/watch?v=yCACmFTiCto&t=1905s)).
   - He turns outputs he likes into skills ([25:09](https://www.youtube.com/watch?v=yCACmFTiCto&t=1509s)) and has Claude build a spreadsheet tracker of every generation ([35:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=2102s)).

## When to use it — and when not to

| Situation | Leaning | Source |
|---|---|---|
| Many on-brand stills from an existing brand book | A skill that calls an aggregator API, with brand files passed as paths. See [[Generate On-Brand Images from Claude Code]] | Jay [08:16](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=496s) |
| A non-coder wants ads, carousels and reels | A vendor connector inside a project that holds brand context. See [[Build a Brand-Aware Marketing Project]] | Nate [16:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1004s) |
| A site is using stock photos or grey placeholders | Generate hero images and background clips | AI LABS [10:40](https://www.youtube.com/watch?v=Ot582-E61ac&t=640s) |
| Short video or motion graphics that are slow to render | Storyboard first. See [[Storyboard-First AI Video and Motion Graphics]] | Chase [02:34](https://www.youtube.com/watch?v=C8dWdic-oK4&t=154s) |
| Stylised short video (motion graphics, horror, explainers) with no media budget | Have Claude Code write and render it in Python. See [[Render a Video Entirely in Code with Claude Code]] | u/AzorAhai1TK [post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/) |
| Editing a backlog of your own narrated footage | Learn the style from past project files, transcribe, cut with FFmpeg. See [[Auto-Edit Footage from Your Editing History]] | Reddit commenter [comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbf8sni/) |
| Building UI from a generated mockup | Treat the image as a loose reference: it gets you about 50–60% of the way | Jay [13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s) |

**When not to lean on it**

- **Unattended creative loops.** Chase says don't loop these videos unless you really know what you're doing, and keep a human in the loop ([07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s)).
- **Content that must feel authentic.** Nate's UGC still looked like AI avatars and came across as salesy ([33:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=2001s)). His fix is to have Claude study real UGC, or to approve the scripts first ([33:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=2012s)).
- **Exact logos, text and figures.** *This note's reading:* treat generated marks and numbers as drafts to check, as Nate's logo shows ([28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s)).

## Where sources disagree

- **Subscription connector or pay-per-call API?**
  - Nate concedes Higgsfield isn't the cheapest option, but values having the models in one place and Marketing Studio ([27:48](https://www.youtube.com/watch?v=yCACmFTiCto&t=1668s)).
  - Jay's skill calls fal.ai, a model aggregator ([07:00](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=420s)). He never mentions a key, though the skill's README requires one (Beyond the source; [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]).
  - Scrollcraft reads your own Kie.ai key from the project env ([05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s)).
  - Jack keeps providers swappable ([13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s)).
  - *This note's reading:* the API route keeps model choice and pricing in your skill. The connector route spares you managing keys and adds the vendor's templates.
- **Who judges the output?**
  - Nate's UGC run leaves QA to the agent ([32:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=1941s)).
  - Scrollcraft self-checks visuals ([08:52](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=532s)), but Nate still reviews the content by eye. He catches screenshots of unknown origin ([10:42](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=642s)), a wrong caption ([11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s)) and a link to fix ([11:26](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=686s)), then sends one feedback round ([12:19](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=739s)). That puts this video nearer Chase's view.
  - Chase wants a human in the loop, not an autonomous loop steered only by the storyboard ([07:40](https://www.youtube.com/watch?v=C8dWdic-oK4&t=460s)).
  - Jay picks by eye from many options ([14:39](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=879s)).

## Perspectives from sources

- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]: a fal.ai skill, brand files as references, numbered grids ([05:52](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=352s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]]: Higgsfield inside a brand-context project, with a cost report after each run ([22:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1355s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]]: storyboard first, the agent writes the build prompt, no loops ([01:51](https://www.youtube.com/watch?v=C8dWdic-oK4&t=111s)).
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: swappable providers and style recipes ([16:09](https://www.youtube.com/watch?v=NAumQObJEwM&t=969s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]]: Kie.ai, which he likens to OpenRouter for media models, fills gaps in a site's assets ([04:52](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=292s)).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: Higgsfield for site visuals, and Seedance for video ([11:05](https://www.youtube.com/watch?v=Ot582-E61ac&t=665s)).
- [[AzorAhai1TK - Opus 5.5 One-Shot Programmatic Video]]: one prompt to Opus 5.5 in Claude Code produced a one-minute surreal horror video. It used no image or video model, rendered entirely in code, and took about 45 minutes and 4% of a $20 plan's weekly limit ([post](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/)). Asked whether it used Higgsfield, the OP said it programs the video directly in Python ([comment](https://www.reddit.com/r/ClaudeAI/comments/1wnh4fn/comment/pbfwutc/)).
- [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]: an app-build variant of the connector route. Claude Code (running the Claude model Fable 5.1) drives Higgsfield over MCP to make character art and a moving backdrop — GPT Image 2.5 for stills, Seedance 2.5 to animate them — and even generated the app icon; you describe the shot by voice and Claude writes the prompt ([14:45](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=885s), [23:21](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1401s)). The first animation pass was glitchy and needed correction rounds, and Higgsfield is the video's sponsor. Build it: [[Vibe-Code an Animated Mobile App with Claude]].
- [[Nick Saraev - Animated Sites with Claude Code and Kling]]: seed motion by generating a still in Nano Banana Pro, then feed it to Kling 3.0 with a motion constraint (rotate in place, centre of mass doesn't move), and have Claude Code wire the clip into a scroll-scrubbed animation and optimise it — extracting the video's frames to JPEGs tied to scroll position ([09:46](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=586s)) and compressing a 5.3 MB hero asset to 252 KB ([11:37](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=697s)). Clips run through Higgsfield's Pro plan at roughly $0.36 each ([03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s); the description's Higgsfield link is an affiliate link). Build it: [[Build an Animated Marketing Site with Claude Code and Kling]].

## Beyond the source

*Not from the videos. Checked 2026-09-15.*

- **Claude doesn't output images.** Anthropic's vision docs say Claude analyses images but can't generate or edit them, which is why every model route above calls another model. The code-rendered route works around this: Claude writes programs that draw the pixels, rather than outputting an image itself. [Vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)
- **Jay's skill needs a fal key.** Its README says to set `FAL_KEY` when installing, a step the video never shows. [gpt-image-2-skill README](https://github.com/robonuggets/gpt-image-2-skill)
- **fal.ai** hosts more than 1,000 generative media models (image, video, audio and 3D), priced per output or by GPU hour. [fal.ai](https://fal.ai)
- **Kie.ai** serves image, video, audio and some chat models through one API. Access is by Bearer API key, jobs run as async tasks, and a generation costs roughly 10–50 credits for an image or 100–500 for a video. Its docs say never to expose the key in client code or public repos. [Kie.ai quickstart](https://docs.kie.ai/market/quickstart)
- **Higgsfield via an agent** deducts credits on every generation, on any plan. [Higgsfield help center](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent)
- **The Motion Designer isn't simply free.** Chase calls it free and credit-free ([00:23](https://www.youtube.com/watch?v=C8dWdic-oK4&t=23s)). Higgsfield's blog lists active Higgsfield, GPT and After Effects subscriptions as requirements, with Higgsfield generations billed in credits. [Higgsfield blog](https://higgsfield.ai/blog/ai-motion-designer-after-effects-gpt)

## Related

- Concepts: [[Connecting Claude to External Tools]] · [[Design Systems for Claude]] · [[Escaping the Default AI Design Look]] · [[Verification Before Done]] · [[Permissions and Approval Gates]]
- Techniques: [[Render a Video Entirely in Code with Claude Code]] · [[Auto-Edit Footage from Your Editing History]] · [[Generate On-Brand Images from Claude Code]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Build a Brand-Aware Marketing Project]] · [[Build a Scroll-Driven Landing Page]] · [[Vibe-Code an Animated Mobile App with Claude]] · [[Build an Animated Marketing Site with Claude Code and Kling]]
- Tools: [[FFmpeg]] · [[Higgsfield]] · [[Scrollcraft]] · [[Claude Code]]
- People: [[Jay E]] · [[Nate Herk]] · [[Chase AI]] · [[Jack Roberts]] · [[AI LABS]]
- [[Home]]
