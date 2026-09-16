---
type: technique
goal: Turn a spec and one inspiration image (or a real product's design-system spec) into a reusable design system, apply it to a site, build the site in Claude Code, and reuse the system for other brand assets
difficulty: beginner
time_to_build: 2–3 hours for a landing page plus two extra assets (vault estimate)
sources: ["[[Sergei Chyrkov - Claude Design Full Tutorial]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]"]
tools: ["[[Claude Design]]", "[[Claude Code]]"]
tags: [topic/design, topic/claude-code, topic/models, topic/marketing]
---

# Create and Reuse a Claude Design System

## Goal

Ship a site and matching collateral that share one deliberate look.

- **Route A** is [[Sergei Chyrkov]]'s [[Claude Design]] workflow ([[Sergei Chyrkov - Claude Design Full Tutorial]]).
- **Route B** takes the system from a real product's spec, as [[Jack Roberts]] does ([[Jack Roberts - Design Systems, Critic Loops and a Design OS]]).
- **Background:** [[Design Systems for Claude]].

## Use when

- **Your first draft looks generic.** Sergei's baseline was fine for most people but generic to a designer, with SVG-style illustrations [02:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=160s).
- **You need more than a site.** Sergei's plan builds the site in Claude Code, then reuses the system for a menu and social posts [00:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=32s).
- **You can't say why a site you admire works.** Jack says a system spells out what you can only sense [05:36](https://www.youtube.com/watch?v=NAumQObJEwM&t=336s).

## Prerequisites

- **Claude Design access** on a paid plan (Beyond the source). Sergei opens it from the bottom of the Claude desktop app's sidebar [01:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=92s).
- **[[Claude Code]]** for the build.
- **One to three inspiration images**, from Pinterest [04:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=242s) or Mobbin [04:08](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=248s). Pick each for one quality you want; Sergei's was typography [04:22](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=262s).
- **Real photos**, if the site needs them. Sergei made his in ChatGPT [09:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=544s). See [[Generate On-Brand Images from Claude Code]].

## Steps

1. **Write the spec in ordinary Claude chat.** Describe the project in a few words and ask for a detailed prompt as a Markdown file [01:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=71s). It should cover how the project looks and works [01:18](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=78s). Download it (Starter 1).
2. **Build an unstyled baseline.** In Claude Design, type "implement", attach the file and pick Opus [01:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=106s). Use no template and no design system [02:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=127s). He ran it on Opus 5 [02:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=139s).
   - Test every feature. In his test the crust option did nothing [02:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=178s) and dragging the cheese didn't work [03:07](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=187s). Note the bugs.
   - *Vault note:* if tokens are tight, create the system first (steps 3–4) and attach it to this first run instead.
3. **Choose the inspiration.** Download one site image; he stresses it's inspiration, not copying [04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s).
4. **Create the design system.**
   - **Route A, Claude Design.** Open the design-system dropdown and click create [05:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=305s).
     - Inputs on offer: a GitHub project [05:20](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=320s), a local codebase, a Figma file or visual assets [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s).
     - Drag in the image [05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s), name the system [05:48](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=348s) and generate.
     - Check what came back: fonts [06:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=373s); colours, shapes and a wordmark [06:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=392s); animation, elevations and radii [06:39](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=399s); a landing-page style [06:51](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=411s). Then run Starter 2.
   - **Route B, borrowed spec, in Claude or Claude Code.** Jack picks a system from a gallery of 2,000+ real products [01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s). Entries include a Tailwind config, CSS variables and design tokens [02:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=161s).
     - He pastes the spec into Claude with a brief [03:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=222s), letting it generate images if needed [03:56](https://www.youtube.com/watch?v=NAumQObJEwM&t=236s), and expects to iterate [04:09](https://www.youtube.com/watch?v=NAumQObJEwM&t=249s). In Claude Code, the vault saves the spec as an adapted `DESIGN.md` (Starter 5).
     - For an existing site, have Claude compare it against a gallery system [05:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=351s) to get exact gaps such as loose letter spacing [06:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=401s). See [[Benchmark-Driven Design Critique]].
5. **Apply the system.** Click +, choose the design system, select yours and click Done [07:11](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=431s)–[07:28](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=448s).
   - Prompt: restyle with the system, make the hero full viewport, add scroll parallax [07:34](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=454s)–[07:46](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=466s) (Starter 3).
   - Adjust parallax speed and colours in Tweaks [08:23](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=503s).
6. **Swap generic illustrations for images.** He added three people photos and replaced the pizza illustration with a real photo [09:14](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=554s)–[09:20](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=560s).
7. **Stop iterating in Claude Design once the layout is right.** It uses a lot of tokens [09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s), so hand off when you're happy with the layout [10:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=604s).
8. **Hand off to Claude Code.** Go to Share, more formats and apps, then Claude Code [10:16](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=616s)–[10:24](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=624s).
   - Targets: a local agent or a web session [10:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=630s), a local save, or a zip for another editor [10:38](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=638s).
   - He pasted the prompt into a new local folder [10:53](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=653s) and chose Sonnet 5, since the design already existed [10:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=659s) and that's much cheaper [11:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=673s). Add Starter 4.
   - He still polished the hero in Claude Code afterwards [13:19](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=799s).
9. **Reuse the system for other assets.**
   - **Menu.** Attach the system [11:25](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=685s), pick the document template [11:33](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=693s) and answer its intake questions [11:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=700s). The menu matched the site [12:03](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=723s).
   - **Instagram posts.** Attach a photo and ask for post layouts [12:30](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=750s), using the same system [12:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=760s) (Starter 6).
   - A consistent look across site, menu and posts is the point [13:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=782s).
10. **Add the review neither source runs.** *Vault step:* check the build against the spec and the system. See [[Benchmark-Driven Design Critique]] and [[Verification Before Done]].

## Starter files & prompts

*Vault starter content, not the creators' wording.*

**Starter 1: spec request (Claude chat)**

```text
Project: <name>: <what it is, who it's for, the one action a visitor should take>.
Write a build spec as a downloadable Markdown file for a design tool.
Include: sections in order; each interactive feature with its states and rules;
placeholder copy; data such as prices; one acceptance check per feature.
Leave colours, fonts and imagery open. A design system will supply them.
```

**Starter 2: design-system review (Claude Design, before applying)**

```text
Review the <name> design system. Change nothing yet.
1. Tabulate every token: colours (hex), fonts and weights, type scale, spacing steps,
   radii, elevation levels, motion durations and easing.
2. Flag gaps: error and focus states, disabled buttons, text on the accent colour.
3. Flag anything lifted so closely from the reference that it could read as a copy
   (logo shapes, signature illustrations), and propose an original replacement.
4. Check body text and buttons against WCAG AA contrast.
```

**Starter 3: apply**

```text
Restyle this project with the <name> design system. Use no values outside it.
Layout changes: <e.g. full-viewport hero; parallax on product images as you scroll>.
Keep every feature in the spec working and list anything you had to change.
Use the attached photos in place of illustrations where they fit.
```

**Starter 4: add to the Claude Code handoff prompt**

```text
Before building: put every design token in one file (styles/tokens.css) and reference it
everywhere, with no hard-coded colours or sizes. Build from the design; don't redesign.
When done: run the site locally, test each acceptance check in the spec, screenshot at
390px and 1440px, and list every place the build differs from the design.
```

**Starter 5: `DESIGN.md` skeleton (Route B, Claude Code)**

```markdown
# DESIGN.md: <brand>
Based on: <gallery entry or own brand>. Logo, wordmark, imagery and copy are ours.

## Colour
| Token | Hex | Use |
|---|---|---|
| --color-bg | #______ | page background |
| --color-text | #______ | body text |
| --color-accent | #______ | one primary action per view |

## Type
- Display: <family>, <weights>, letter-spacing <value>
- Body: <family>, <size>/<line-height>

## Space, radius, elevation
- Spacing: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 px
- Radius: sm <__> · md <__> · lg <__>
- Elevation: 0 flat · 1 card · 2 menu · 3 dialog (shadow values)

## Motion
- Durations <__> ms, easing <__>; honour reduced-motion settings

## Avoid
- <e.g. more than one accent per view, stock SVG illustrations, gradient text>
```

Prompt: *"Build <brief> using only the tokens in DESIGN.md. Ask before inventing a missing value."*

**Starter 6: reuse for another asset**

```text
Using the <name> design system, make <one-page menu | 3 Instagram posts at 1080×1350>.
Content: <items, or the attached photo>. Match the website's type, colours and shapes.
Ask me about format and content before drafting.
```

## Done when

- [ ] The system has been reviewed: hex values, type, spacing, radii, elevation and motion are all present
- [ ] No logo, signature illustration or copy was carried over from the reference
- [ ] The restyled site passes every acceptance check in the spec, including baseline bugs
- [ ] Generic SVG illustrations are replaced, or kept on purpose
- [ ] The Claude Code build runs locally, reads one token file and matches the design at two widths
- [ ] At least one more asset uses the same system and visibly matches
- [ ] The tokens also live in the repo (`DESIGN.md` or a tokens file), not only in Claude Design

## Pitfalls

- **Token burn.** Claude Design hit his limit mid-run [07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s). Iterate there only until the layout is right [09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s), then polish on a cheaper model in Claude Code.
- **Generic SVG illustrations carry into the build.** After the handoff he still wanted photos in their place [14:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=842s). Supply images before handing off.
- **A restyle isn't a bug fix.** He never says whether the baseline's crust and cheese-dragging bugs were fixed [02:58](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=178s).
- **Untested fidelity, and the copying line.** Neither source measures how closely a system matches its reference. Jack's route borrows a whole brand's look [03:06](https://www.youtube.com/watch?v=NAumQObJEwM&t=186s), so adapt rather than copy [11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s).
- **The UI may not match the docs.** If the project dropdown [05:05](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=305s) is missing, look in organisation onboarding (Beyond the source).
- **The system stays inside Claude Design.** *Vault reading:* unlike a skill folder, it doesn't travel to other agents. Export the tokens (Starter 5); see [[Build a Reference-Rich Skill]].

## Variations

- **Other ways to source the system:** a generated rulebook, a brand book or a guidelines PDF. See [[Design Systems for Claude]] and [[Build a Brand-Aware Marketing Project]].
- **A skill chain instead of Claude Design:** [[Build a Distinctive Site with Design Skills]].

## Beyond the source

*Not from the videos. Checked on 2026-09-15.*

- **Access and cost.** Claude Design is in beta on Pro, Max, Team and Enterprise (off by default on Enterprise). It shares usage limits with chat, Cowork and Claude Code. https://support.claude.com/en/articles/14604416-get-started-with-claude-design
- **Documented setup.** Setup runs during organisation onboarding and accepts codebases, screenshots, design files, PPTX or PDF documents and logos. Published makes a system the default, Remix edits it, and Anthropic suggests a test landing-page or dashboard prompt. https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- **Handoff and export.** Export covers PDF, PPTX, HTML and apps such as Canva or Vercel. Run in Claude Code, `/design-sync` pulls a codebase's design system into Claude Design. https://claude.com/product/design
- **Local handoff failure.** In issue #69246 (opened 2026-06-18, now closed), the "Send to local coding agent" prompt needed a Claude Design connector that local Claude Code lacked. Workaround: choose "Download zip instead", unzip it into the project and point Claude Code at it. https://github.com/anthropics/claude-code/issues/69246
- **Ready-made specs for Route B.** Refero Styles offers 2,000+ systems, each with a DESIGN.md meant for Claude Code, Cursor or Codex. https://styles.refero.design/
- **Sergei's finished repo.** Vanilla HTML, CSS and JS, with styles split into tokens, components and layout. The spec prompt file is included. https://github.com/chyrkov/pizza-project

## Sources

- [[Sergei Chyrkov - Claude Design Full Tutorial]]: Route A, handoff and reuse.
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: Route B and benchmark comparison.

## Related

- **Concepts:** [[Design Systems for Claude]] · [[Escaping the Default AI Design Look]] · [[Choosing a Claude Model]] · [[Verification Before Done]]
- **Techniques:** [[Benchmark-Driven Design Critique]] · [[Build a Distinctive Site with Design Skills]] · [[Build a Reference-Rich Skill]] · [[Generate On-Brand Images from Claude Code]] · [[Build a Brand-Aware Marketing Project]] · [[Route Tasks to the Right Claude Model]]
- **Tools:** [[Claude Design]] · [[Claude Code]]
- **People:** [[Sergei Chyrkov]] · [[Jack Roberts]]
- [[Home]]
