---
type: technique
goal: "Turn a vague sense that another design looks better into a measured gap report, then push a design toward a benchmark with a builder and three critic subagents that stop on explicit rules"
difficulty: intermediate
time_to_build: "About 30 minutes for the comparison skill; 1–2 hours to set up and tune the design loop (vault estimate)"
sources: ["[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]"]
tools: ["[[Claude Code]]"]
tags: [topic/design, topic/loops, topic/subagents, topic/verification, topic/skills]
---

# Benchmark-Driven Design Critique

> **Provenance.** Both methods come from [[Jack Roberts - Design Systems, Critic Loops and a Design OS]], with timestamps. He says both are packaged as skills ([06:26](https://www.youtube.com/watch?v=NAumQObJEwM&t=386s), [09:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=589s)), and that "design loop" is his name for the Gauntlet Loop ([08:40](https://www.youtube.com/watch?v=NAumQObJEwM&t=520s)). He never shows the skill files, critic prompts, pass criteria or a round cap. **Every file, rubric and stop rule below is original vault starter content**, written to current Claude Code formats (Beyond the source).

## Goal

| Part | Command | Output |
|---|---|---|
| A. Ruthless benchmark comparison | `/design-compare <your-url> <benchmark>` | `design/compare/<benchmark>.html`, which lists the top gaps with measured values side by side |
| B. Design loop | `/design-loop <reference.png> <brief>` | An HTML asset plus a log of critic scores and why the loop stopped |

## Use when

- **You can tell a design looks better but can't say why.** Jack's point: sensing quality isn't the same as putting it into words, and only the words help Claude ([05:34](https://www.youtube.com/watch?v=NAumQObJEwM&t=334s)–[05:43](https://www.youtube.com/watch?v=NAumQObJEwM&t=343s)).
- **You want to level up an existing site** against one you admire. He compares his startup Glaido with Linear ([04:54](https://www.youtube.com/watch?v=NAumQObJEwM&t=294s)).
- **You have a picture of a great design and need something usable,** such as an HTML email built from a screenshot ([09:15](https://www.youtube.com/watch?v=NAumQObJEwM&t=555s)).
- **Not when:**
  - there's no real benchmark, because the critic then invents its own standard (Beyond the source);
  - each pass is slow and costly. See "How good is good enough?" in [[Escaping the Default AI Design Look]].

## Prerequisites

- **[[Claude Code]]** in a git repo, so you can revert a bad round.
- **A browser tool** that can resize the viewport and take screenshots: Playwright MCP (Beyond the source) or [[Claude in Chrome]]. Jack lets Claude visit the benchmark and take screenshots itself ([06:16](https://www.youtube.com/watch?v=NAumQObJEwM&t=376s)).
- **A benchmark:** a live site, a reference screenshot, or a design-system spec. Jack takes specs from a gallery of 2,000+ product systems ([01:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=118s)), and the one he opens includes Tailwind, CSS variables and design tokens ([02:41](https://www.youtube.com/watch?v=NAumQObJEwM&t=161s)). See [[Design Systems for Claude]].
- **A token budget for Part B.** This video gives no cost. His earlier video puts a run at 2–3M tokens (Beyond the source).

## Steps

### Part A: ruthless benchmark comparison

1. **Pick one benchmark you admire.** Jack picks Linear for its balanced dark mode and palette ([05:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=321s)). He adds that it isn't the peak of design ([07:58](https://www.youtube.com/watch?v=NAumQObJEwM&t=478s)).
2. **Install `design-compare`** (starter below).
3. **Run it.** Jack's prompt gave Claude both sites, asked for a ruthless account of the differences and how to improve his, allowed site visits and screenshots, and asked for a concise HTML breakdown ([05:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=351s)–[06:22](https://www.youtube.com/watch?v=NAumQObJEwM&t=382s)).
4. **Read the top three gaps.** His: loose letter spacing, no elevation ladder, and hero art competing with the product ([06:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=398s)).
5. **Ask for detail.** A follow-up added a slider placing his letter spacing against Linear's ([06:47](https://www.youtube.com/watch?v=NAumQObJEwM&t=407s)). The report covered shadows, accent frequency, border radius, vocabulary and display weight, with values side by side ([07:25](https://www.youtube.com/watch?v=NAumQObJEwM&t=445s)).
6. **Change tokens, not pages.** Jack sent the report to his team, and its hex values can be copied ([07:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=462s)). Update your design system, then rerun.
7. **Repeat against a couple more benchmarks** ([08:05](https://www.youtube.com/watch?v=NAumQObJEwM&t=485s)). Vault view: this avoids drifting toward one brand.

### Part B: the design loop

8. **Get a reference image.** Jack screenshots an Apple launch email and pastes it into Claude ([09:32](https://www.youtube.com/watch?v=NAumQObJEwM&t=572s)).
9. **Install `design-loop` and the three critics** (starters below).
10. **Name what to match in the brief.** He asked for the launch recreated as HTML that looks right in an email, for his own product, attending to named qualities of the reference ([10:25](https://www.youtube.com/watch?v=NAumQObJEwM&t=625s)).
11. **Run `/design-loop`.** You give a benchmark ([09:53](https://www.youtube.com/watch?v=NAumQObJEwM&t=593s)). Claude spins up three critic subagents that loop until the work reaches the mark ([10:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=618s)). The three ask: does it hit the benchmark, is the design great, and what's its visual impact? The first is garbled as "the proof" *(unclear in captions)*.
12. **Read the stop reason in the log.** Jack calls his result "one shot" ([10:38](https://www.youtube.com/watch?v=NAumQObJEwM&t=638s)). The vault reads that as one user prompt, with the critic rounds inside the skill.
13. **Adapt, don't copy.** His second run recreated Anthropic's platform email, down to an Anthropic-style orange button ([11:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=664s)). His caveat: work out what works, change specific things, or blend several references ([11:21](https://www.youtube.com/watch?v=NAumQObJEwM&t=681s)). The starter critic treats copied identity as a blocker.

## Starter files & prompts

*Vault starter content, not Jack's files.*

### `.claude/skills/design-compare/SKILL.md`

```markdown
---
name: design-compare
description: Measured comparison of our site against a benchmark site or DESIGN.md, written as a concise HTML gap report. Use when the user runs /design-compare.
argument-hint: "<our-url> <benchmark-url-or-DESIGN.md>"
disable-model-invocation: true
---

Arguments: $ARGUMENTS. The first is ours, the second the benchmark. Be ruthless: every claim needs a value or a screenshot region.

1. Load both at 1440px and 375px. Screenshot the hero, one content section and the footer.
2. Read computed styles (or DESIGN.md tokens) for: type scale and display weight, letter spacing, line height,
   spacing and white space, border radius, shadow/elevation levels, accent colour frequency, hierarchy, copy vocabulary.
3. Per dimension record ours, benchmark, gap, and the fix as a token change. Mark screenshot-only values "estimated".
4. Write design/compare/<benchmark>.html: top three gaps first, then a section per dimension with side-by-side values,
   sliders for numeric gaps and click-to-copy hex swatches. Self-contained. Save the findings as JSON alongside.
5. Learn traits, not identity: never recommend copying the benchmark's logo, imagery, copy or signature colour-and-shape combinations.
```

### `.claude/skills/design-loop/SKILL.md`

```markdown
---
name: design-loop
description: Builds an HTML asset to the quality bar of a reference image, judged by three critic subagents under a round cap. Use when the user runs /design-loop.
argument-hint: "<reference-image-path> <brief> [max-rounds]"
disable-model-invocation: true
---

Arguments: $ARGUMENTS. First: reference image. A trailing number: max rounds (default 3, never above 5). The rest: the brief.

You are the builder. Critics see only images and the brief, never your reasoning.

Round 0: write design/loop/brief.md with the brief, the reference's five strongest traits, and what must differ
(brand, copy, imagery, accent colour). Warn that a run can use millions of tokens; wait for OK.

Each round N:
1. Build or revise design/loop/output.html; commit "design-loop round N".
2. Screenshot at the reference's width (and 375px for web pages) into design/loop/round-N/.
3. Call benchmark-fidelity-critic, design-quality-critic and visual-impact-critic in parallel with only the
   reference, the screenshots and brief.md. Save replies to design/loop/round-N/.
4. Append to design/loop/log.md: round, three scores, blockers, top fixes, decision.
5. Stop at the first of:
   PASS: every score 8+ and no blockers.  CAP: N = max rounds.
   PLATEAU: average rose < 0.5 since last round.
   REGRESSION: average fell by 1+; git revert --no-edit HEAD, then stop.
6. Otherwise fix blockers, then fixes raised by at least two critics.

Report the stop reason, the score table and open issues, and remind the user to check originality.
```

### `.claude/agents/benchmark-fidelity-critic.md`

```markdown
---
name: benchmark-fidelity-critic
description: Read-only critic for /design-loop. Judges whether an output reaches the quality bar of a reference image. Never edits.
tools: Read, Glob
model: opus
color: blue
---

You judge; you never fix. Inputs: reference image, output screenshots, brief.

Focus: does the output reach the reference's level on layout rhythm, type hierarchy, colour restraint, imagery and finish?
Judge the level, not sameness. Anything copied from the reference's identity (logo, text, imagery, signature colour and shape) is a blocker.

Reply only with JSON:
{"score": 1-10, "blockers": [], "gaps": [{"issue": "", "where": "", "fix": ""}], "copied_elements": []}
At most five gaps, most important first.
```

### The other two critics

Copy the file above. Change `name`, `description`, `color` and the Focus line.

- **design-quality-critic:** craft on its own terms. Check Jack's five tells ([01:39](https://www.youtube.com/watch?v=NAumQObJEwM&t=99s)): typography, imagery, hierarchy, colour and spacing. Also check alignment, contrast, and consistent radius and shadow.
- **visual-impact-critic:** does it stop a viewer in the first second? Look for one focal point and energy that fits the brief. Anything generic enough to fit any brand counts as a gap.

## Done when

- [ ] The comparison report opens offline and shows measured or "estimated" values, not adjectives
- [ ] At least one gap became a token change, and a rerun shows it narrowed
- [ ] `/design-loop` stopped for a named reason (PASS, CAP, PLATEAU or REGRESSION)
- [ ] `design/loop/log.md` shows every critic's score for each round
- [ ] The output shares no logo, copy, imagery or signature colour-and-shape combination with the reference

## Pitfalls

- **The source has no stop rules.** Jack's critics loop until the work hits the mark ([10:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=618s)), with no pass bar, cap or cost. Keep the cap and plateau exit. See [[Loop Engineering]].
- **Critics always find something.** The two-critic agreement rule and the PLATEAU exit stop endless polishing. See [[Multi-Agent Review and Scoring Loops]].
- **Fidelity sliding into copying.** Jack's recreations stay very close to Apple's and Anthropic's emails ([11:04](https://www.youtube.com/watch?v=NAumQObJEwM&t=664s)). Learn a benchmark's rhythm and restraint; don't ship its identity. Near-copies of a real brand can raise trademark and copyright issues. Vault caution, not legal advice.
- **Screenshots carry no exact values, and reports can invent them.** Prefer live pages or a token spec, and require the "estimated" label.
- **Sending from the loop.** Jack has Claude Code draft or send the email through Zapier ([11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s)). Keep sends behind approval ([[Permissions and Approval Gates]]).
- **Slow media.** When a pass takes many minutes, a couple of human-judged passes beat a critic loop ([[Chase AI - GPT-6 Astra Motion Design in After Effects]] [07:30](https://www.youtube.com/watch?v=C8dWdic-oK4&t=450s)).

## Variations

- **Cheaper loop:** one critic covering all three focuses, with a cap of 2.
- **System first:** paste a benchmark's design-system spec and ask for a build in that style ([03:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=224s)), then run Part A against the live site. See [[Create and Reuse a Claude Design System]].

## Beyond the source

*Not from the video. Checked on 2026-09-15.*

- **Subagent format.** Subagents are Markdown files with YAML frontmatter in `.claude/agents/`. `name` and `description` are required. `tools`, `model` (`sonnet`, `opus`, `haiku`, `fable`, a full ID or `inherit`) and `color` are optional. Non-fork subagents start without the conversation history, which keeps critics blind to the builder's reasoning. https://code.claude.com/docs/en/sub-agents
- **Skill format.** Skills live in `.claude/skills/<name>/SKILL.md`. The docs cover `argument-hint`, `disable-model-invocation` and `$ARGUMENTS`. https://code.claude.com/docs/en/skills
- **Origin.** The Gauntlet Loop repo, packaged by [[Jay E]]'s RoboNuggets, credits Matt Shumer. A fresh-context critic compares the output blind with a concrete bar, and the loop exits when the output wins, never after a fixed number of rounds. The vault's cap departs from that on purpose. https://github.com/robonuggets/gauntlet-loop
- **Known limit.** With no existing benchmark, the critic invents its own standard. https://daily.dev/posts/the-new-gauntlet-loop-has-a-flaw-this-claude-skill-just-fixed-it-2u5yvngy5
- **Cost.** A summary of Jack's earlier design-loop video gives about 2–3M tokens per run. https://www.dutchstartup.ai/en/tv/this-new-prompting-technique-just-10x-d-claude-design
- **The gallery.** It's unnamed in the video. Refero Styles advertises 2,000+ AI-readable design systems, each with a DESIGN.md. It's likely the gallery he shows, but that isn't confirmed. https://styles.refero.design
- **Screenshots.** Install with `claude mcp add playwright npx @playwright/mcp@latest`. It exposes `browser_resize` and `browser_take_screenshot`. https://github.com/microsoft/playwright-mcp

## Sources

- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: the comparison report ([05:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=351s)) and the design loop ([09:53](https://www.youtube.com/watch?v=NAumQObJEwM&t=593s))

## Related

- **Concepts:** [[Escaping the Default AI Design Look]] · [[Design Systems for Claude]] · [[Loop Engineering]] · [[Subagents and Agent Teams]] · [[Verification Before Done]]
- **Techniques:** [[Multi-Agent Review and Scoring Loops]] · [[Build a Distinctive Site with Design Skills]] · [[Create and Reuse a Claude Design System]]
- **People:** [[Jack Roberts]]
- [[Home]]
