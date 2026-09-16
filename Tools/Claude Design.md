---
type: tool
category: AI design and prototyping product (Anthropic Labs, beta)
website: https://claude.com/product/design
sources: ["[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Sergei Chyrkov - Claude Design Full Tutorial]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]"]
tags: [topic/design, topic/skills, topic/portability, topic/claude-code]
---

# Claude Design

## What it is

Claude Design is Anthropic's product for making visual work, such as sites, prototypes and decks, by talking with Claude. In [[AI LABS - Claude Design Skills for Beautiful Sites]], [[AI LABS]] use it as the workbench for testing seven third-party design skill collections. [[Sergei Chyrkov - Claude Design Full Tutorial]] runs a whole project through it, from design system to Claude Code handoff. Anthropic's own description, plans and handoff options are under *Beyond the source*.

The video describes how skills work in Claude Design in three points:

- **Skills come from your Claude settings.** There's no separate install inside Claude Design. Skills added to your Claude setup are the same ones Claude Design can use [00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s)–[00:58](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=58s), so you add each one once, from Claude settings [01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s).
- **You run a skill with a slash.** Type a slash plus the skill's name, then describe the site you want in the same prompt [02:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=134s)–[02:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=136s).
- **Build skills interview you first.** Before generating anything, emil-design-eng quizzes you about the app, much as Claude Design itself does [02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s)–[02:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=147s). landing-page-design also asks questions before it designs [06:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=387s).

AI LABS also say the same skills work in [[Claude Code]], [[OpenAI Codex]] or any other agent and give the same result [01:02](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=62s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s). They use Emil Kowalski's skills in both Claude Code and Claude Design themselves [01:17](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=77s)–[01:22](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=82s). The "same result" claim is asserted, not demonstrated.

## How sources use it

### [[AI LABS - Claude Design Skills for Beautiful Sites]]

**Where plain Claude Design falls short, per the video**

- **A recognisable house style.** However capable a model is, it designs to its own pattern, and that pattern is easy to spot [00:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=21s)–[00:26](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=26s). Skills are what steer it away [00:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=28s). See [[Escaping the Default AI Design Look]].
- **Thinner default output.** The site web-design-engineer built was more interesting and more thorough than what Claude Design produces unaided [04:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=291s)–[05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s).
- **Layout.** Spacing, positioning and alignment are where Claude Design struggles [09:48](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=588s)–[09:57](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=597s), which is why they add better-layout.

**The seven collections they ran**

Roles: *generate* builds a first design from a brief, *refine* improves something already built, and *review* scores a design or lists issues to fix. The role labels are the vault's; the video describes each job.

| Collection (repo) | Author | Role | What the video credits it with | Where |
|---|---|---|---|---|
| Emil Kowalski's skills (emilkowalski/skills) | Emil Kowalski | Generate + refine | emil-design-eng is the skill to start a design with. animate refines motion on a built site and syncs it with scroll. apple-design packages Apple's product principles. animation-vocabulary turns a vague motion description into exact terms | [01:11](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=71s), [01:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=111s), [02:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=160s), [01:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=87s), [01:35](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=95s) |
| garden-skills (ConardLi/garden-skills) | ConardLi (captioned "Connard Lee") | Generate + review | A collection of five skills, some covering video presentations and images [03:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=231s). web-design-engineer clarifies your requirements, then works from real designs and style recipes for sites like Apple and Linear. Run on an existing design, it scores it so you can iterate | [03:49](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=229s), [04:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=252s), [04:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=271s), [05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s) |
| ai-design-skills: landing-page-design (elayadesign) | elayadesign | Generate (landing pages) | A single file that turns an idea into a visual system of colour, type and spacing. It builds the page around one action, keeps one style and covers search findability | [05:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=324s), [05:33](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=333s), [06:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=363s), [06:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=375s) |
| Skills (MengTo/Skills) | Meng To | Generate (storytelling) | build-awwwards-quality-sites adds award-winner principles plus the concrete effects a model won't produce alone, and builds with scroll storytelling. video-to-superprompt turns a screen recording into a prompt | [07:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=447s), [08:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=493s), [08:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=507s), [08:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=527s), [07:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=472s) |
| skills (jakubkrehel/skills) | Jakub Krehel | Review + refine | One skill per design area, such as typography, colour and accessibility [09:05](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=545s). The review skill (interface-review) checks everything and flags what broke since your last change. better-layout gives exact spacing fixes | [08:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=535s), [09:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=554s), [09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s), [09:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=599s) |
| tastemaker (codeswithroh/tastemaker) | Not named in the video (GitHub: codeswithroh) | Generate | Works from a reference's pixels, with scripts that save exact design details in a structured form. Tries variations and applies its decisions across the whole project | [10:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=615s), [10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s), [10:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=652s), [10:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=655s) |
| designer-skills (Owl-Listener/designer-skills) | Not named in the video (GitHub: Owl-Listener) | Review + refine | Research-grounded, with one skill per named design law; install only what fits. Some skills cover why visitors leave partway through and how behaviour shows up as they move around a site [11:33](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=693s). They used screen critique and perception laws | [11:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=681s), [11:39](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=699s), [11:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=705s), [11:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=715s) |

### [[Sergei Chyrkov - Claude Design Full Tutorial]]

[[Sergei Chyrkov]] takes one landing page through the whole product; the steps are in [[Create and Reuse a Claude Design System]].

- **Where it lives.** Bottom of the desktop app's sidebar, opening in its own window [01:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=92s). Templates cover documents, animations, UI mockups, research and résumés [01:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=112s).
- **Design systems from a project.** A dropdown's create option [05:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=305s) takes a GitHub project, a local codebase, a Figma file or visual assets [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s). One inspiration image gave him fonts, colours, shapes, a wordmark, motion, elevations and radii [06:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=373s). Other tools build sites well too, he says, so this feature is what sets Claude Design apart [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s). See [[Design Systems for Claude]].
- **Apply, then tune.** The + menu attaches a system [07:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=431s); Tweaks then change parallax speed and colours with no prompt [08:23](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=503s).
- **Intake questions.** Before drafting a menu, the document template asked about pages, sections, item count and photos [11:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=700s).
- **Token cost.** He hit his usage limit mid-run [07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s) and advises stopping once the layout is right, because Claude Design uses a lot of tokens [09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s).
- **Handoff to [[Claude Code]].** Share, more formats and apps, then Claude Code [10:16](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=616s) offers a local agent or web session [10:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=630s), a local save or a zip [10:38](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=638s). He built on Sonnet 5 because the design already existed [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s), then polished the hero in Claude Code [13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s).
- **One system, several formats.** Site, menu and Instagram posts stayed consistent [13:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=782s).

### [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]

- **Named for the product, but never uses it.** The title and hashtags say Claude Design, yet the product never appears. The skills run in an agent, and the only surface named is the terminal [10:55](https://www.youtube.com/watch?v=Ot582-E61ac&t=655s). Don't treat it as evidence about Claude Design.

## Notes

- **Docs and video put design systems in different places.** Sergei creates one from a project dropdown and lists Figma as an input [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s). Anthropic's help puts setup in organisation onboarding with a Published toggle and doesn't list Figma (Beyond the source). The interface may vary by plan or version.
- **Is layout a weak spot?** AI LABS say spacing and alignment are where Claude Design struggles [09:48](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=588s). Sergei's only layout complaint is an oversized footer [09:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=586s).
- **Results are judged by eye.** Improvements are described in subjective terms [02:54](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=174s), [04:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=291s), [11:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=675s), and no brief is run through two skills side by side.
- **An untested conversion claim.** They say landing-page-design's structure made a purchase much more likely [06:36](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=396s)–[06:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=401s), with no numbers or test behind it.
- **The review skill needs history.** They say it works better connected to GitHub because it compares the design before and after your changes [09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s)–[09:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=570s). That points to a git repository, not a browser canvas. See Beyond the source.
- **Some skills run code on your machine.** video-to-superprompt uses local tools [07:52](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=472s)–[08:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=481s), and tastemaker relies on scripts [10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)–[10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s).
- **Counts drift.** The video says Emil's set has nine skills [01:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=73s); the repo lists more today (Beyond the source).
- **Omitted:** a sponsor segment unrelated to Claude and a paid-community pitch.

## Beyond the source

*Not said in the video. Checked on 2026-09-15 at the links given.*

- **What Anthropic says it is.** Anthropic Labs announced Claude Design on 17 April 2026. It makes designs, prototypes, slides and one-pagers through conversation, and you refine the work by chat, inline comments, direct edits or sliders Claude generates. At launch it was a research preview running on Claude Opus 4.7. https://www.anthropic.com/news/claude-design-anthropic-labs
- **Access.**
  - In beta for Pro, Max, Team and Enterprise; Enterprise admins must turn it on.
  - Open it at claude.ai/design or from the Claude Desktop sidebar. Usage counts toward your plan's normal limits.
  - https://support.claude.com/en/articles/14604416-get-started-with-claude-design
- **References and design systems.**
  - You can attach screenshots, competitor products, decks and code repositories as references.
  - During onboarding it reads a codebase or design files and extracts colours, type, components and spacing. A tested design system can then be published for the whole organisation.
  - Setup is for people an admin permits. Inputs also include PPTX or PDF documents, logos and type specimens. Published makes the system the default for the organisation's projects, and Remix edits it through chat.
  - https://support.claude.com/en/articles/14604416-get-started-with-claude-design · https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- **Handoff to Claude Code.** Export to PDF, PowerPoint or HTML, send work to connected apps such as Canva, or hand it off to Claude Code. Run in Claude Code, `/design-sync` pulls your design system into Claude Design, and `/design` works on designs directly. https://claude.com/product/design
- **Local handoff bug.** Issue #69246 (opened 2026-06-18, now closed): the default "send to local coding agent" prompt relied on a Claude Design connector that local Claude Code lacked. Workaround: download the zip, unzip it into the project and point Claude Code at it. https://github.com/anthropics/claude-code/issues/69246
- **Adding skills in the Claude apps.**
  - Path: Customize > Skills > + > Create skill > Upload a skill, then upload a ZIP of the skill folder.
  - Code execution and file creation must be on.
  - None of the Anthropic pages above says uploaded skills appear in Claude Design; that part rests on the video.
  - https://support.claude.com/en/articles/12512180-use-skills-in-claude
- **The same skill files in Claude Code.**
  - Skills live at `~/.claude/skills/<name>/SKILL.md` (personal) or `.claude/skills/<name>/SKILL.md` (project), and you run one with `/<name>`.
  - A skill whose frontmatter sets `disable-model-invocation: true` runs only when you type the command. interface-review is one, and it reviews a git diff, branch or PR, which makes Claude Code the natural place to run it after a handoff.
  - https://code.claude.com/docs/en/skills · https://github.com/jakubkrehel/skills/blob/main/skills/interface-review/SKILL.md
- **The seven repos** (links from the video description; install commands in [[Build a Distinctive Site with Design Skills]]):
  - https://github.com/emilkowalski/skills (12 skills listed today)
  - https://github.com/ConardLi/garden-skills
  - https://github.com/elayadesign/ai-design-skills
  - https://github.com/MengTo/Skills
  - https://github.com/jakubkrehel/skills
  - https://github.com/codeswithroh/tastemaker
  - https://github.com/Owl-Listener/designer-skills

## Related

- **Techniques:** [[Build a Distinctive Site with Design Skills]] · [[Create and Reuse a Claude Design System]]
- **Concepts:** [[Escaping the Default AI Design Look]] · [[Design Systems for Claude]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Tool-Agnostic Context Files]]
- **Tools:** [[Claude Code]] · [[OpenAI Codex]]
- **Sources:** [[AI LABS - Claude Design Skills for Beautiful Sites]] · [[Sergei Chyrkov - Claude Design Full Tutorial]] · [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] · **People:** [[AI LABS]] · [[Sergei Chyrkov]]
- [[Home]]
