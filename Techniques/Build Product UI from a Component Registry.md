---
type: technique
goal: Build dashboards, app screens and mobile UI that behave like real products by assembling registry components under the maker's rules, with marketing pages routed to a separate design track
difficulty: intermediate
time_to_build: 1–2 hours to set up and build a first dashboard screen (vault estimate)
sources: ["[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]"]
tools: ["[[shadcn]]", "[[Claude Code]]"]
tags: [topic/design, topic/skills, topic/mcp, topic/claude-code]
---

# Build Product UI from a Component Registry

## Goal

Ship functional UI (dashboards, forms, settings, app screens) that is consistent and conventional rather than "distinctive". The agent assembles it from professionally built registry components and fits them to your project.

Sources, abbreviated below:
- **June** = [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: shadcn skill plus MCP, a dashboard skill, the two-track design system, mobile skills.
- **September** = [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: SwiftUI skills for Liquid Glass and iPhone Duo.

The distinctive-look track lives in [[Build a Distinctive Site with Design Skills]]. When to escape defaults: [[Escaping the Default AI Design Look]] and [[Design Systems for Claude]].

## Use when

- **People operate it rather than admire it.** June says Anthropic's frontend-design skill does poorly on functional UI, where many components must all behave [02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s). Their own product layer is deliberately plain [03:06](https://www.youtube.com/watch?v=Ot582-E61ac&t=186s).
- **The agent keeps hand-rolling components you then fix.** June: common dashboard parts already exist at professional quality [03:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=201s), so start from ship-ready parts, not a rough draft [03:52](https://www.youtube.com/watch?v=Ot582-E61ac&t=232s).
- **A dashboard feels cluttered** although each component is fine [05:03](https://www.youtube.com/watch?v=Ot582-E61ac&t=303s).
- **Phone output looks like a shrunken website** (June [11:25](https://www.youtube.com/watch?v=Ot582-E61ac&t=685s)).
- **iOS output fakes Liquid Glass with blurs** (September [08:31](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=511s)).

## Prerequisites

- **Web track:** a React and Tailwind project, Node with npx or pnpm, and [[Claude Code]] (stack under Beyond the source).
- **Mobile track:** Compose or Flutter for Material 3; a Mac with Xcode 26+ for SwiftUI skills; an Expo app for cross-platform (Beyond the source).
- **Time to read community skills before installing.** June mixes official skills with community ones (dashboard, mobile-app-ui-design, material-3, SwiftUI). See [[Build vs Install Third-Party Skills]].

## Steps

1. **Split UI work into two tracks and route by page type.**
   - June keeps two skills: a functional one for UI people have to use, such as dashboards, and a marketing-UI one [02:12](https://www.youtube.com/watch?v=Ot582-E61ac&t=132s).
   - The marketing skill holds a modified frontend-design prompt called "break the default" [02:26](https://www.youtube.com/watch?v=Ot582-E61ac&t=146s) and hands landing-page animation to the GSAP skill [09:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=561s).
   - Their files are paywalled. Put the vault's routing block (below) in CLAUDE.md so a dashboard never gets the art-direction skill.
2. **Initialise shadcn** so `components.json` exists; the skill reads it (Beyond the source).
3. **Install the shadcn skill, the rulebook.** June: it holds shadcn's correct way of building [04:04](https://www.youtube.com/watch?v=Ot582-E61ac&t=244s) and checks how your project is set up so output fits [04:10](https://www.youtube.com/watch?v=Ot582-E61ac&t=250s). The payoff is clean output first time [04:20](https://www.youtube.com/watch?v=Ot582-E61ac&t=260s).
4. **Connect the shadcn MCP, the catalogue.** June: a live registry connection to browse and pull real components [04:28](https://www.youtube.com/watch?v=Ot582-E61ac&t=268s). Keep both: June calls them two parts that work together [04:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=241s), with the skill's rules, patterns and project context giving the agent judgement to use components correctly [04:49](https://www.youtube.com/watch?v=Ot582-E61ac&t=289s). June's token argument is dated (Where sources differ).
5. **Ask for the screen in registry parts.** The model needn't generate components or configure animations from scratch (June [03:29](https://www.youtube.com/watch?v=Ot582-E61ac&t=209s)). Use the build prompt below.
6. **For dashboards, settle the arrangement before components.** June: the core problem is grouping data and how much fits on one screen before clutter [05:07](https://www.youtube.com/watch?v=Ot582-E61ac&t=307s). They add a separate dashboard skill from another developer [05:18](https://www.youtube.com/watch?v=Ot582-E61ac&t=318s) that reasons through arrangement first [05:26](https://www.youtube.com/watch?v=Ot582-E61ac&t=326s). With or without it, fill in the layout brief below.
7. **For mobile, add one principles skill and exactly one platform skill.** June: models ignore how phones are held, thumb reach, navigation and platform design languages [11:34](https://www.youtube.com/watch?v=Ot582-E61ac&t=694s). Those languages help pick the platform skill: Material 3 is bold and colourful, with big rounded shapes and springy motion [12:26](https://www.youtube.com/watch?v=Ot582-E61ac&t=746s), while Apple is restrained and leans on translucent Liquid Glass [12:51](https://www.youtube.com/watch?v=Ot582-E61ac&t=771s).
   - **Principles:** mobile-app-ui-design covers the thumb zone, consistent spacing and few font sizes [11:57](https://www.youtube.com/watch?v=Ot582-E61ac&t=717s), the same rules June says sit behind Airbnb, Duolingo and Spotify [12:07](https://www.youtube.com/watch?v=Ot582-E61ac&t=727s).
   - **Android:** Material 3, which June calls the mobile counterpart of shadcn [12:16](https://www.youtube.com/watch?v=Ot582-E61ac&t=736s). One colour yields a full theme, and it checks guideline adherence [12:38](https://www.youtube.com/watch?v=Ot582-E61ac&t=758s).
   - **Native iPhone:** SwiftUI skills that turn Apple's documentation from Xcode into rules [13:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=781s).
   - **Both platforms:** the official Expo skill for navigation, styling and platform features [13:20](https://www.youtube.com/watch?v=Ot582-E61ac&t=800s).
8. **For iOS 26 specifics, add a targeted skill.** September: fwc-swiftui-skills has a Liquid Glass skill for Apple's built-in buttons and menus, with common mistakes [09:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=544s), and an iPhone Duo skill for the wider screen [09:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=553s). Install the one you need and tell the agent to follow it [09:22](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=562s).
9. **Check against the registry and platform, not by eye.** *Vault step:* list components added, flag hand-built duplicates of registry parts, and run a platform audit where one exists (Material 3 has one). See [[Build Verification into Every Task]].

## Starter files & prompts

*Vault starter content, not from either video.*

**CLAUDE.md routing block**

```markdown
## UI routing
Pick the track before touching UI code.
- Product track: dashboards, forms, tables, settings, auth, admin, logged-in screens.
  Use product-ui. Registry components first; no bespoke styling or motion.
- Marketing track: landing, pricing, portfolio and launch pages.
  Use marketing-ui (animation via the GSAP skill).
- Mixed page (e.g. pricing inside the app): product track.
- Mobile: mobile principles skill + ONE platform skill (material-3 | swiftui | expo).
Unsure which track? Ask me once.
```

**`.claude/skills/product-ui/SKILL.md`**

```markdown
---
name: product-ui
description: Use when building or changing functional app UI such as dashboards, forms, tables, settings, admin or logged-in screens. Not for landing or marketing pages.
---
# Product UI
1. Read components.json; list installed components.
2. For each element, search the registry (shadcn MCP) before writing markup.
   Add missing components as a dry run first and show me the diff.
3. Theme tokens only. No new colours, fonts, shadows or animations.
4. Dashboards: write layout.md first and follow it.
5. Report: components reused, components added, anything hand-built and why.
```

**Dashboard layout brief (`layout.md`)**

```markdown
# Dashboard: <name>
Primary user, and the 3 questions they open it to answer:
Groups (max 4), each tied to a question:
Above the fold (max 4 KPIs + 1 chart):
Secondary (tabs, drill-down, below the fold):
Empty, loading and error state per group:
Filters: global or per group?
```

**Build prompt**

```text
Build <screen> on the product track. Search the shadcn registry for every element
and list what you'll reuse before coding. Follow layout.md. Hand-build nothing the
registry already has.
```

## Done when

- [ ] CLAUDE.md routes product vs marketing pages, and one test request per track picks the right skill.
- [ ] `components.json` exists; the shadcn skill and MCP both appear in the session.
- [ ] Every element on the screen is a registry component or a logged exception.
- [ ] Product-track code has no raw colour values or one-off animations.
- [ ] Each dashboard has a `layout.md`, and the build respects its above-the-fold budget.
- [ ] Mobile has one principles skill and one platform skill.
- [ ] iOS Liquid Glass uses native APIs, checked in the simulator.

## Pitfalls

- **Art direction on the app.** frontend-design doesn't suit functional UI (June [02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s)). If both skills trigger on one request, fix the descriptions: [[Audit Skill Descriptions and Triggers]].
- **MCP without the skill.** The catalogue gives parts, not the rules for using them in your project (June [04:49](https://www.youtube.com/watch?v=Ot582-E61ac&t=289s)).
- **Assuming the dashboard skill plans layout.** The claim couldn't be confirmed from its public page (Beyond the source), so keep the brief.
- **Stacking skills.** June warns against stacking taste presets [10:15](https://www.youtube.com/watch?v=Ot582-E61ac&t=615s). *Vault inference:* the same holds for platform skills, one design language per app.
- **Believing "it's native".** September: the agent claims its blur imitation is the real thing [08:45](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=525s).
- **Stale skills.** June re-tuned an older skill for newer models [02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s). Re-check platform skills after OS or model releases: [[Skill Improvement Loop]].

## Where sources differ

- **Why pair skill and MCP.** June says skills load only when needed while MCP sits in context permanently [04:43](https://www.youtube.com/watch?v=Ot582-E61ac&t=283s). Claude Code now defers MCP tool definitions by default (Beyond the source), so division of labour is the lasting reason. September even picks MCP over the CLI for UI Skills because its tools stay available in the session [05:15](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=315s).
- **Two different "SwiftUI skills".** June's (ameyalambat128) are generated from Apple docs on your Mac [13:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=781s). September's (FloWritesCode) are two targeted skills, Liquid Glass and iPhone Duo, kept up to date with Apple's changes [09:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=541s). *Vault reading:* both cover Liquid Glass. Use June's for broad Apple guidance and September's for iOS 26 and foldable cases.

## Variations

- **Your own registry.** Point the shadcn MCP at a private registry so the agent assembles from your company's system (Beyond the source); pairs with [[Create and Reuse a Claude Design System]].
- **Skills on demand.** September's UI Skills registry loads a fitting design skill over MCP [05:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=337s). *Vault reading:* it suits the marketing track better than this one.
- **Audit an existing app first.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] recommends shadcn's improve skill, which audits a codebase and writes plans for other agents [06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s).

## Beyond the source

*Not in the videos; checked 2026-09-15.*

- **shadcn setup.** Component source is copied into your project by a CLI and registry. `pnpm dlx shadcn@latest init` creates `components.json` (style, Tailwind, aliases, registries). https://ui.shadcn.com/docs/components-json
- **shadcn skill.** `pnpm dlx skills add shadcn/ui`. It reads `components.json`, runs `shadcn info --json`, and enforces rules such as `FieldGroup`/`Field` forms and semantic colour tokens. https://ui.shadcn.com/docs/skills
- **shadcn MCP.** `pnpm dlx shadcn@latest mcp init --client claude` writes `.mcp.json` running `npx shadcn@latest mcp`. It browses, searches and installs from public, private and third-party registries. Restart the client afterwards. https://ui.shadcn.com/docs/mcp
- **Skill's CLI commands:** `info`, `search`, `docs`, `view`, and `add` with `--dry-run` and `--diff`. https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md
- **Tool search** is on by default; a custom `ANTHROPIC_BASE_URL` or `ENABLE_TOOL_SEARCH=false` turns it off. https://code.claude.com/docs/en/mcp
- **Dashboard skill.** The video's GitHub folder link now returns 404, but skills.sh still indexes bergside's "dashboard" skill: `npx skills add https://github.com/bergside/awesome-design-skills --skill dashboard`, or `npx typeui.sh pull dashboard` from the TypeUI registry. Its SKILL.md is mostly a visual system: colour and type tokens, an 8-pt baseline grid, WCAG 2.2 AA and visual hierarchy for complex data. No layout-first procedure is visible, so that claim is unverified. https://www.skills.sh/bergside/awesome-design-skills/dashboard · https://github.com/bergside/typeui
- **mobile-app-ui-design:** `npx skills add ceorkm/mobile-app-ui-design`. Primary actions in the bottom third, 8-pt grid, at most four sizes and two weights. https://github.com/ceorkm/mobile-app-ui-design
- **material-3:** `npx --yes skills add hamen/material-3-skill --skill material-3 -y`. Compose first, Flutter second, limited web; `/material-3 audit` scores 10 categories. https://github.com/hamen/material-3-skill
- **swiftui-skills:** `npx skills add ameyalambat128/swiftui-skills`. macOS and Xcode 26+; docs are extracted locally. https://github.com/ameyalambat128/swiftui-skills
- **fwc-swiftui-skills:** `npx skills add FloWritesCode/fwc-swiftui-skills` (add `--skill swiftui-liquid-glass` or `--skill swiftui-iphone-duo`). Needs the iOS 26 SDK. https://github.com/FloWritesCode/fwc-swiftui-skills
- **Expo:** `claude plugin install expo@claude-plugins-official`. Skills include expo-native-ui, expo-ui, expo-router and expo-design-system. https://github.com/expo/skills

## Sources

- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: functional vs marketing UI, shadcn skill + MCP, dashboard and mobile skills.
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: Liquid Glass and iPhone Duo skills; UI Skills over MCP.
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: shadcn's improve skill.

## Related

- **Concepts:** [[Design Systems for Claude]] · [[Escaping the Default AI Design Look]] · [[Agent Skills]] · [[Connecting Claude to External Tools]] · [[Build vs Install Third-Party Skills]]
- **Techniques:** [[Build a Distinctive Site with Design Skills]] · [[Create and Reuse a Claude Design System]] · [[Audit Skill Descriptions and Triggers]] · [[Build Verification into Every Task]]
- **Tools:** [[shadcn]] · [[Claude Code]]
- **People:** [[AI LABS]] · [[The Coding Sloth]]
