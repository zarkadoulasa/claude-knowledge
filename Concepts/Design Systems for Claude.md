---
type: concept
aliases: ["Design System", "Brand Book"]
sources: ["[[Sergei Chyrkov - Claude Design Full Tutorial]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tags: [topic/design, topic/context, topic/marketing, topic/skills]
---

# Design Systems for Claude

## In one sentence

A design system is a written set of visual decisions that Claude builds from: tokens for colour, type, spacing, radii, elevation and motion, plus components, identity marks and things to avoid, so Claude stops using its defaults and every asset matches.

## How it works

### Why a system beats a better prompt

- **Claude lacks references, not ability.** [[Jack Roberts]] argues models design badly because they have never seen great design [01:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=64s). Give Claude the same prompt as everyone else and you get the same result [01:46](https://www.youtube.com/watch?v=NAumQObJEwM&t=106s). The giveaways sit in typography, imagery, hierarchy, colour and spacing [01:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=99s).
- **Taste has to become values.** Sensing that a design looks good is not the same as saying why, and only the second helps Claude [05:36](https://www.youtube.com/watch?v=NAumQObJEwM&t=336s).
- **Process over prompt.** [[Sergei Chyrkov]] credits design process, not wording, for the gap between his first and final site [00:06](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=6s). He calls design-system creation the standout feature of [[Claude Design]] [04:59](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=299s).
- **A decision, not general taste.** [[AI LABS]] say most skills treat good design as one general idea, so everything drifts toward the same look [05:52](https://www.youtube.com/watch?v=Ot582-E61ac&t=352s). A generated system gives the model a decision fitted to the product before it starts [06:46](https://www.youtube.com/watch?v=Ot582-E61ac&t=406s).

### What goes in one

The grouping is the vault's; the examples come from the sources.

| Layer | What it pins down | Where sources show it |
|---|---|---|
| Colour | Brand, accent and background values, ideally as hex | Jack's gallery [02:30](https://www.youtube.com/watch?v=NAumQObJEwM&t=150s); Sergei [06:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=392s); Jay's brand book [07:56](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=476s); Nate [03:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=204s) |
| Typography | Families, pairings, weights, letter spacing | Jack [02:32](https://www.youtube.com/watch?v=NAumQObJEwM&t=152s); Sergei [06:13](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=373s); UI UX Pro Max [06:16](https://www.youtube.com/watch?v=Ot582-E61ac&t=376s); Nate [03:31](https://www.youtube.com/watch?v=yCACmFTiCto&t=211s) |
| Spacing, radii, elevation | White space, corner radius, a shadow ladder | Sergei [06:39](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=399s); Jack's audit found loose letter spacing and no elevation ladder [06:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=401s) |
| Motion | Animation style and who implements it | Sergei [06:39](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=399s); AI LABS's marketing skill hands animation to GSAP's skill [09:19](https://www.youtube.com/watch?v=Ot582-E61ac&t=559s) |
| Identity | Wordmark, logo system | Sergei [06:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=392s); Nate [03:29](https://www.youtube.com/watch?v=yCACmFTiCto&t=209s) |
| Layout and components | Page pattern, reusable UI parts | Sergei's landing-page style [06:51](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=411s); Material 3 as Google's own system for Android [12:16](https://www.youtube.com/watch?v=Ot582-E61ac&t=736s) |
| Anti-patterns | What would look wrong for this product | UI UX Pro Max filters those choices out [06:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=381s) |
| Machine-readable form | Values code can use directly | Jack's gallery: Tailwind config, CSS variables and design tokens [02:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=161s) |

### Five ways sources get one

| Route | Source | Input | What Claude gets | Where |
|---|---|---|---|---|
| Borrow a real product's spec | [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] | A gallery of 2,000+ systems from real products | Apple's spec, pasted in with a brief for an unrelated product | [01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s), [03:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=222s) |
| Generate from an image | [[Sergei Chyrkov - Claude Design Full Tutorial]] | One Pinterest screenshot; a GitHub project, codebase or Figma file also work | Fonts, colours, shapes, a wordmark, motion, elevation, radii | [05:32](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=332s), [05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s) |
| Generate an industry-fitted rulebook | [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] | Your product idea; UI UX Pro Max searches 161 industry categories | Palette, font pairing and layout, with mismatches removed | [06:13](https://www.youtube.com/watch?v=Ot582-E61ac&t=373s), [06:27](https://www.youtube.com/watch?v=Ot582-E61ac&t=387s) |
| One-page brand book | [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] | Type options and palettes, converted to JPEG because the image model rejects PDFs | A reference mapped to each image generation | [07:56](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=476s), [08:20](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=500s), [09:17](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=557s) |
| Brand guidelines in the project | [[Nate Herk - Claude as a One-Person Marketing Team]] | A guidelines PDF in `assets/` | Claude reports taking its design system from the PDF instead of inventing one | [14:23](https://www.youtube.com/watch?v=yCACmFTiCto&t=863s), [19:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1150s) |

- **Starting from nothing.** Jay's earlier skill builds a brand book from your website, or just give Claude the URL [08:04](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=484s). Nate had Claude Code create guidelines, logos and product shots from a bare brand idea [06:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=392s).
- **A system as a benchmark.** Jack also has Claude compare his own site against Linear's system and report the gaps [05:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=351s). See [[Benchmark-Driven Design Critique]].

### Build once, reuse everywhere

- **Sergei** uses one system for the site, a menu made from the document template, and Instagram posts [11:25](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=685s), [12:40](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=760s). Consistency is the payoff [13:02](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=782s).
- **Jack's team** uses Glaido's system for presentations, the website and the app [07:35](https://www.youtube.com/watch?v=NAumQObJEwM&t=455s).
- **Nate** wants guidelines that every deliverable follows [03:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=216s). Unprompted, Claude even coloured an Excel tracker in the brand's lime green [36:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=2184s).
- **Jay's** brand book kept social posts on type and colour [01:52](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=112s).

## When to use it — and when not to

- **Use one** whenever several assets must read as one brand.
- **Fit the system to the surface.** AI LABS say Anthropic's frontend-design skill works poorly for functional UI [02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s), and their own product layer is deliberately plain [03:12](https://www.youtube.com/watch?v=Ot582-E61ac&t=192s). For product UI, a component library's system is the design system; see [[Build Product UI from a Component Registry]] and [[shadcn]]. Save distinctive art direction for marketing pages.
- **Budget for Claude Design.** Sergei hit his usage limit mid-run [07:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=472s) and warns it uses a lot of tokens [09:52](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=592s).
- **Hold the copying line.** Sergei treats his image as inspiration [04:15](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=255s), and Jack says to adapt what works rather than lift it [11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s). Borrowing Apple's whole system for another product [03:06](https://www.youtube.com/watch?v=NAumQObJEwM&t=186s) edges toward imitation, so the vault advises swapping identity marks and copy.

## Perspectives from sources

Two points the tables above miss:

- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: outputs from his design loop could seed a system of your own [10:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=658s).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: their own design system gives marketing UI and functional UI separate skills [02:12](https://www.youtube.com/watch?v=Ot582-E61ac&t=132s).

## Where sources disagree

- **A written spec or exact pixels?**
  - *Existing view:* [[Escaping the Default AI Design Look]] records the AI LABS warning that models turn a reference image into a lossy text summary ([[AI LABS - Claude Design Skills for Beautiful Sites]] [10:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=627s)–[10:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=645s)).
  - *Jack* pastes structured tokens instead, and the Apple influence shows without a single image [04:24](https://www.youtube.com/watch?v=NAumQObJEwM&t=264s).
  - *Sergei* lets Claude Design read one image into a system [05:41](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=341s) and never checks fidelity.
  - *Jay* says an image reference gets you only 50–60% of the way, and doesn't translate cleanly into HTML components [13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s), which supports the worry.
  - *Vault reading:* exact values (hex codes, font names, pixel sizes) are the middle path. Spot-check a few against the reference.
- **Borrowed, generated or your own?** Jack borrows a system, Sergei and AI LABS generate one (from an image or a database), and Jay and Nate start from their own brand. Each carries a risk: borrowing edges toward imitation, a generated system is unvetted, and your own brand has to exist first.
- **Is one pass enough?** Jack says the best designs come from iteration [04:09](https://www.youtube.com/watch?v=NAumQObJEwM&t=249s). Sergei stops once the layout looks right, to save tokens [10:04](https://www.youtube.com/watch?v=T96O8dTzi2Q&t=604s), and runs no review.

## Beyond the source

*Not from the videos. Checked on 2026-09-15.*

- **Anthropic's setup.**
  - During organisation onboarding, for people an admin permits, Claude Design builds a system from codebases, screenshots, design files, PPTX or PDF documents, logos and type specimens.
  - It returns a palette, typography, components and layout patterns.
  - Published makes the system the organisation's default, and Remix edits it.
  - https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- **From a codebase.** Run in Claude Code, `/design-sync` pulls a codebase's design system into Claude Design. https://support.claude.com/en/articles/14604416-get-started-with-claude-design · https://claude.com/product/design
- **The gallery Jack likely used.** Refero Styles lists 2,000+ AI-readable systems taken from product sites. Each has colours, type, spacing, components and a DESIGN.md for Claude Code, Cursor or Codex, and the site offers an MCP connection. https://styles.refero.design/
- **UI UX Pro Max today.** Its system covers pattern, style, colours, type, effects, anti-patterns and a pre-delivery checklist. `--persist` saves it as `design-system/<project>/MASTER.md`. The repo now cites 192 industry reasoning rules, not the video's 161 categories. https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## Related

- **Build it:** [[Create and Reuse a Claude Design System]] · [[Build a Reference-Rich Skill]] · [[Benchmark-Driven Design Critique]] · [[Build a Brand-Aware Marketing Project]] · [[Generate On-Brand Images from Claude Code]] · [[Build Product UI from a Component Registry]]
- **Concepts:** [[Escaping the Default AI Design Look]] · [[Agent Skills]] · [[Generating Images and Video with Claude]]
- **Tools:** [[Claude Design]] · [[Claude Code]] · [[shadcn]]
- **People:** [[Sergei Chyrkov]] · [[Jack Roberts]] · [[AI LABS]] · [[Jay E]] · [[Nate Herk]]
- [[Home]]
