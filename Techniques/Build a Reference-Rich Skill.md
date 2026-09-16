---
type: technique
goal: "Refactor a thick skill into a folder where a short SKILL.md routes Claude to reference files, templates and scripts, and use the pattern to build a brand design-system skill that turns a one-line request into an on-brand PDF, HTML page or video visual"
difficulty: intermediate
time_to_build: "About 1 to 2 hours for a brand skill when your brand assets already exist; 20 to 40 minutes to refactor an existing thick skill (vault estimate)"
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]"]
tools: ["[[Claude Code]]", "[[Claude Design]]"]
tags: [topic/skills, topic/design, topic/context, topic/claude-code, topic/agentic-os]
---

# Build a Reference-Rich Skill

> **Provenance.** Points with a timestamp link come from [[Jay E - The ARMS Framework for a Claude Agentic OS]], [[AI LABS - Claude Design Skills for Beautiful Sites]] or [[Ras Mic - How AI Agents and Claude Skills Work]]. Later additions: [[Nate Herk - Build Skills Instead of Agents]] and [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]. Jay E opens his /robo skill folder and its brand HTML file but says little about their contents beyond fonts and colour palettes, and his refactor prompt appears only on screen. AI LABS describes third-party design skills without opening their files. The prompts, folder layout, SKILL.md router, `brand.html` skeleton, palette file and route check below are **vault starter content** written for this note. The two Python scripts were run on sample files before publishing. Skill mechanics and the layouts of the third-party skills named here are verified under **Beyond the source**. For the idea itself, see [[Agent Skills]]. For the same routing idea applied to a whole workspace, see [[CLAUDE.md as a Router]].

## Goal

A skill whose `SKILL.md` is a short router. It holds the trigger, intake questions, workflow and a "when to read what" table, and points to:

- `references/` for detail only some requests need, such as brand rules, per-format specs and style recipes;
- `assets/` for templates Claude copies and fills;
- `scripts/` for deterministic work Claude should run instead of redoing each time, such as pulling exact colours from an image or checking an output against the palette.

The worked example is a brand design-system skill in the spirit of Jay E's /robo. He asks for a PDF guide with a one-line prompt and gets a polished result in one or two prompts ([08:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=510s)–[08:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=530s)).

## Use when

- **A skill has grown thick.** Jay E contrasts two kinds of skill:
  - **Thin.** His cleanup skill is a single `SKILL.md` of instructions, which suits a simple job ([06:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=418s)–[07:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=430s)).
  - **Complex.** For complex work he adds files to the skill instead of forcing everything into one ([08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)–[08:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=498s)).
- **Output must match exact visual values.** Jay E finds visual references work especially well for design skills ([08:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=484s)–[08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)). AI LABS explains why words alone fall short: a model usually reduces a reference image to a text summary, and detail gets lost ([10:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=628s)–[10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)).
- **One brand feeds many formats.** /robo is the design system behind many of Jay E's videos and company assets ([07:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=466s)–[07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s)).
- **Different requests need different material.** A PDF request shouldn't load thumbnail rules. Progressive disclosure is what makes the split pay off:
  - until a skill is needed, only its name and description sit in context ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)–[04:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=247s));
  - Ras Mic measured 53 tokens for those two fields against 944 for the whole file ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)–[30:58](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1858s)). He counted with OpenAI's tokenizer ([30:35](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1835s)), so the figures are only approximate for Claude.

**Skip it** when one file does the job. AI LABS's landing-page skill keeps everything in a single file and still gave them a result that felt like a real brand ([05:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=327s)–[05:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=331s), [06:30](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=390s)–[06:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=394s)). Don't add reference files that only you would ever read.

## Thin, thick and reference-rich

| Shape | What it looks like | Example from the sources | Good for |
|---|---|---|---|
| **Thin** | One `SKILL.md` with a short procedure | Jay E's cleanup skill ([07:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=422s)–[07:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=428s)) | Short, fixed procedures |
| **Thick** | One `SKILL.md` holding every rule, value and example | What Jay E's on-screen refactor prompt goes looking for ([08:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=531s)–[09:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=540s)) | Nothing. It loads everything on every use and buries the step that matters |
| **Reference-rich** | `SKILL.md` routes to files in the same folder | /robo and its brand HTML file ([07:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=457s)–[08:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=482s)). Also web-design-engineer, whose bundled references cover judging a design, common failures, and style recipes for sites like Apple and Linear ([04:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=271s)–[04:44](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=284s)) | Design systems, multi-format output, domain knowledge |
| **Script-backed** | References plus scripts for deterministic steps | tastemaker uses scripts to extract exact design details into a structured form ([10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)–[10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s)), and hands anything that doesn't need the agent to scripts ([10:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=647s)–[10:50](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=650s)). Nate Herk's carousel skill points Claude at renderers and templates that already work, so a run only changes the text ([02:13](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=133s)–[02:22](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=142s)) | Anything where exact values or repeatable checks matter |
| **Split** | Several narrow skills instead of one broad one | Jakub Krehel's set gives typography, colour, accessibility and other areas their own skill ([08:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=536s)–[09:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=552s)) | Areas you apply independently |

## Where the sources differ

- **Many files or one?** Jay E pushes rich references for complex skills ([08:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=489s)–[08:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=498s)). AI LABS rates a single-file landing-page skill highly ([05:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=327s)–[05:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=331s)). *Vault reading:* the number of files isn't the goal. Split when one file mixes material that different requests need.
- **One design-system skill or several?** Jay E uses one /robo skill for his videos and company assets ([07:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=466s)–[07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s)). Jakub Krehel's collection splits design into per-area skills ([08:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=536s)–[09:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=552s)). *Vault default:* one brand skill that routes to per-format references, with review skills kept separate.
- **Where the references come from.**
  - Jay E made his cleanup skill by pasting an X post into skill-creator ([06:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=372s)–[06:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=386s)).
  - Ras Mic argues that skills written without a successful run behind them break on real tasks ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)–[11:45](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=705s)).
  - web-design-engineer grounds its work in real designs that have already worked ([04:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=258s)–[04:31](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=271s)).

  *Vault default:* build brand references from assets you've already approved.
- **References in the skill, or passed per prompt.** [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] passes his one-page brand book (typography, colour palettes) as a file path in the prompt, not as part of a skill ([07:54](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=474s)–[08:17](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=497s)). He has Claude convert the PDF to JPEG first, because GPT Image 2 won't take PDFs ([08:16](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=496s)–[08:25](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=505s)). *Vault default:* keep both formats in `references/`.

## Prerequisites

- [[Claude Code]] in a git repository, or the Claude app if you'll upload the skill there.
- **Your real brand material:**
  - font names, with files or links;
  - colour hex values;
  - a logo;
  - two or three past assets you're happy with.
- Python 3 for the scripts, plus Pillow (`pip install pillow`) for `extract_palette.py`.
- For a refactor: the thick skill, committed so you can compare before and after.

## Steps

### Phase 1: find and triage thick skills

1. **Take an inventory.** Run the line count below, or send Prompt 1. Prompt 1 is the vault's own version of the refactor prompt Jay E shows only on screen ([08:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=531s)–[09:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=542s)).
2. **Sort each block of a thick `SKILL.md` into one of five bins** (Prompt 1 does this):
   - **Keep in `SKILL.md`:** trigger, intake questions, workflow steps, final checks and the routing table.
   - **`references/`:** detail only some requests need.
   - **`assets/`:** skeletons to copy and fill.
   - **`scripts/`:** deterministic steps, such as extracting, converting or validating.
   - **Delete:** what the model already knows. Ras Mic's example is not telling it to write money with a dollar sign. A non-default currency is the kind of detail that does belong ([32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)–[32:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1968s)).

### Phase 2: build the brand design-system skill

3. **Collect the brand from assets that worked, not from memory.** Run `extract_palette.py` on a few approved assets and check each value against your brand files.
   - **No brand files?** Jay E points to his earlier skill that builds a brand book from your website, or says to simply give Claude the site link ([08:04](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=484s)–[08:14](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=494s)).
     - Use Prompt 3, then check its values against the live site's CSS and have the brand owner confirm them.
     - Save an image copy as well, for image models that reject PDFs (see Where the sources differ).
4. **Write `references/palette.json`.** It is the single source of truth for colours, and the checker reads it.
5. **Write `references/brand.html`.** Cover fonts, type scale, palette swatches with hex values and roles, spacing, logo rules, and do/don't examples.
   - This plays the part of Jay E's brand HTML file, which gives guidance on fonts and colour palettes ([07:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=473s)–[08:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=482s)).
   - *Vault reasoning for HTML:* you can open it in a browser and see the brand, and Claude can read the exact CSS values.
6. **Write one reference per output format:** `pdf.md`, `html.md` and `video-visuals.md`. Each covers sizes, layout rules and what to export.
7. **Add templates** under `assets/templates/`, such as a print-ready HTML page for PDFs and a title-card frame for video.
8. **Add scripts for the deterministic parts.** This is tastemaker's scripts-first idea ([10:47](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=647s)–[10:50](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=650s)):
   - `extract_palette.py` reads colours from reference images;
   - `check_brand_colors.py` flags any colour in an output that isn't in the palette.
   - **Promote scripts that already worked.**
     - **Why.** [[Nate Herk - Build Skills Instead of Agents]] retells an Anthropic example. Claude kept rewriting near-identical slide-styling Python, which cost tokens and consistency, until the team had Claude save the script inside the skill ([01:30](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=90s)–[01:55](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=115s)).
     - **How.** Send Prompt 4 to move a script from chat into `scripts/` and have `SKILL.md` run it ([02:23](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=143s)–[02:39](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=159s)).
     - **Check.** Repeat the task and confirm the saved file ran ([02:40](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=160s)–[02:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=172s)). Compare the key parts; the text around the script can still vary ([02:44](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=164s)).
9. **Write the `SKILL.md` router** from the starter.
   - **Intake first.** It asks a few questions before building. Claude asked Jay E a few questions before making the PDF ([08:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=516s)–[08:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=520s)), and the design skills AI LABS tried do the same ([02:23](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=143s)–[02:29](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=149s)).
   - **Checker last.** It ends by running the checker.
10. **Write the description around the words people actually use.** Jay E names the skill in his request, as in making a PDF guide with /robo ([08:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=510s)–[08:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=516s)). The description matters most when Claude has to pick the skill on its own.

### Phase 3: test it

11. **Try a one-line request** in a fresh session, naming the skill as Jay E does.
12. **Watch which files Claude opens.** A PDF request should read `brand.html`, `pdf.md` and the PDF template, and leave `video-visuals.md` closed. If Claude reads everything or misses a file, fix the routing table.
13. **Run the checker on the output** until it prints OK.
14. **Compare with the old thick version** on the same three requests. Keep the refactor only if results hold up. [[Skill Improvement Loop]] has an A/B script for this.

### Phase 4: install and use

15. **Commit the skill folder.** For use across all your projects, place it in `~/.claude/skills/` instead.
16. **Claude app and Claude Design:** zip the folder and upload it under Customize > Skills (Beyond the source). AI LABS says a skill added in your Claude settings is the same one you can use in Claude Design ([00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s)–[01:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=60s)). Anthropic's skills help article doesn't mention Claude Design, so confirm the skill shows up there before relying on it.
17. **Run it outside chat if it's used often.** Jay E's third skills level runs skills headlessly with `claude -p` from a dashboard, choosing the model and effort for each run ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)–[10:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=608s)). See [[Build an Agentic OS Dashboard]].
18. **List it in the relevant department router** so Claude finds it. Jay E's content.md is simply a list of skills and reference files ([12:45](https://www.youtube.com/watch?v=8NSyI-npJCU&t=765s)–[12:57](https://www.youtube.com/watch?v=8NSyI-npJCU&t=777s)).

## Starter files & prompts

*Everything in this section is vault starter content, not from the videos.*

### Find thick skills

```bash
wc -l .claude/skills/*/SKILL.md ~/.claude/skills/*/SKILL.md 2>/dev/null | sort -rn | head -20
```

### Prompt 1: triage thick skills

```text
Look at every SKILL.md in .claude/skills and ~/.claude/skills. List the ones over
150 lines or that mix several kinds of material. For each, make a table of its
sections with a proposed destination:
- keep in SKILL.md (trigger, intake questions, workflow steps, final checks)
- references/<file>.md (detail that only some requests need)
- assets/<file> (templates to copy and fill)
- scripts/<file> (deterministic work: extract, convert, validate)
- delete (things you would do correctly without being told)
Don't change any files. End with the one skill that would gain most from a refactor.
```

### Prompt 2: refactor one skill

```text
Refactor .claude/skills/<name> using the table I approved:
1. Move each block to its destination. Keep SKILL.md under 150 lines.
2. Add a "When to read what" table to SKILL.md: one row per reference, asset and
   script, saying which requests need it. Link every file directly from SKILL.md;
   reference files must not send Claude on to further files.
3. Give any reference longer than 100 lines a short contents list at the top.
4. For each script, say whether to run it or read it, with the exact command.
5. Move rules without rewording them. Show `git diff --stat` and stop.
```

### Prompt 3: one-page brand book from a website

```text
Build a one-page brand book for <brand> from <website URL>. Read the real CSS
on the home page and two inner pages: fonts and weights, type scale, each
colour's hex value and use, spacing, and logo files. Don't invent values; mark
gaps "unknown". Save to .claude/skills/<skill>/references/: brand.html,
palette.json (allowed colours and roles) and brand-book.png (a render of
brand.html for image models, made with a headless browser if one is available).
List every value you inferred rather than read.
```

### Prompt 4: promote a chat script into the skill

```text
The <what it does> script you wrote in this session is the one I want. Save it
to .claude/skills/<skill>/scripts/<name>.py with a docstring (usage, inputs,
dependencies). In SKILL.md, replace any instruction to write this code with a
step that runs the file by exact command. Rerun the same kind of task, confirm
from the tool calls that the saved script ran, and show the diff.
```

### Folder layout

```text
.claude/skills/brand-studio/
├── SKILL.md                    # router: intake, when-to-read table, build, final check
├── references/
│   ├── palette.json            # single source of truth for colours
│   ├── brand.html              # fonts, type scale, swatches, spacing, logo, do/don't
│   ├── pdf.md                  # page size, margins, cover and section rules
│   ├── html.md                 # page structure, responsive rules
│   └── video-visuals.md        # thumbnails, title cards, lower thirds
├── assets/
│   ├── templates/
│   │   ├── pdf-guide.html      # print-ready page skeleton
│   │   └── title-card.html
│   └── logo/
│       └── logo.svg
└── scripts/
    ├── extract_palette.py      # dominant colours of a reference image
    └── check_brand_colors.py   # flags colours that aren't in palette.json
```

### `SKILL.md`

```markdown
---
name: brand-studio
description: Produces on-brand PDFs, HTML pages and video visuals (thumbnails, title cards) using the company design system. Use when the user asks for a branded guide, one-pager, report, landing page, slide, thumbnail or any asset that should match the brand.
argument-hint: "[what to make]"
---

# Brand studio

Request: $ARGUMENTS

## 1. Intake (ask before building)
Ask only what the request leaves open, in one short batch:
- format (PDF, web page, video visual) and size
- audience, and the one thing they should do or remember
- the source content to use and any must-have sections

## 2. When to read what
| If the job involves | Read or run |
|---|---|
| Any output | references/brand.html (fonts, type scale, palette roles, spacing, logo) |
| A PDF | references/pdf.md, then copy assets/templates/pdf-guide.html |
| A web page | references/html.md |
| A thumbnail, title card or lower third | references/video-visuals.md, then copy assets/templates/title-card.html |
| Matching a new reference image | run `python3 ${CLAUDE_SKILL_DIR}/scripts/extract_palette.py <image> 6` and compare with references/palette.json |

Read only the rows that apply. Use only colours listed in references/palette.json.

## 3. Build
1. Copy the template into the working folder. Never edit files inside this skill.
2. Fill it with the content, keeping the type scale and spacing from brand.html.
3. For a PDF, render the HTML to PDF with the project's usual tool and check page breaks.

## 4. Check before delivering
1. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_brand_colors.py <each html, css or svg file you made>`.
2. Fix every flagged colour and rerun until it prints OK.
3. Confirm fonts match brand.html and the logo keeps its clear space.
4. Deliver with one line naming any brand rule you had to bend, and why.
```

### `references/palette.json`

```json
{
  "allowed": ["#0F172A", "#F8FAFC", "#FF5A1F", "#1E3A8A", "#FFFFFF"],
  "roles": {
    "ink": "#0F172A",
    "paper": "#F8FAFC",
    "accent": "#FF5A1F",
    "deep": "#1E3A8A"
  },
  "ignore": ["#add"]
}
```

`ignore` lists strings the checker should skip, such as an in-page anchor like `#add` that is also a valid three-digit hex value.

### `references/brand.html` (skeleton)

```html
<!-- Brand reference. Colour values must match palette.json. Open in a browser to review. -->
<html>
<head>
<style>
  :root {
    --ink: #0F172A; --paper: #F8FAFC; --accent: #FF5A1F; --deep: #1E3A8A;
    --font-display: "Your Display Font", Georgia, serif;
    --font-body: "Your Body Font", Arial, sans-serif;
    --step-0: 1rem; --step-1: 1.25rem; --step-2: 1.563rem; --step-3: 1.953rem; --step-4: 2.441rem;
    --space: 8px; /* every margin and gap is a multiple of this */
  }
  body { font-family: var(--font-body); color: var(--ink); background: var(--paper); }
  h1, h2 { font-family: var(--font-display); }
  h1 { font-size: var(--step-4); }
</style>
</head>
<body>
  <h1>Brand reference</h1>
  <section id="palette"><!-- one swatch per colour: name, hex, role, allowed text pairings --></section>
  <section id="type"><!-- display and body fonts, the scale above, line length --></section>
  <section id="spacing"><!-- 8px grid, margins per format --></section>
  <section id="logo"><!-- clear space, minimum size, backgrounds it may sit on --></section>
  <section id="do-dont"><!-- screenshots of two or three approved assets and one rejected one, with reasons --></section>
</body>
</html>
```

### `scripts/check_brand_colors.py`

```python
#!/usr/bin/env python3
"""Flag hex colours in HTML, CSS or SVG files that are not in the brand palette.

Usage: python3 check_brand_colors.py <file> [<file> ...]
Reads references/palette.json from the skill folder. Exit 0 = clean, 1 = off-brand colours found.
Only #rgb and #rrggbb values are checked; rgb()/hsl() values are not.
"""
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
HEX = re.compile(r"(?<![&\w])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")


def normalise(value):
    value = value.lower()
    if len(value) == 4:  # #abc -> #aabbcc
        value = "#" + "".join(ch * 2 for ch in value[1:])
    return value


def main(paths):
    config = json.loads((SKILL_DIR / "references" / "palette.json").read_text())
    allowed = {normalise(c) for c in config["allowed"]}
    ignore = {c.lower() for c in config.get("ignore", [])}
    problems = 0
    for path in paths:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
        for number, line in enumerate(text.splitlines(), 1):
            for match in HEX.findall(line):
                if match.lower() in ignore or normalise(match) in allowed:
                    continue
                print(f"{path}:{number}: off-brand colour {match}")
                problems += 1
    if problems:
        print(f"{problems} off-brand colour(s). Allowed: {', '.join(sorted(allowed))}")
        return 1
    print("OK: only brand colours found")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
```

### `scripts/extract_palette.py`

```python
#!/usr/bin/env python3
"""Print the dominant colours of a reference image as hex values with their share of pixels.

Usage: python3 extract_palette.py <image> [count]
Needs Pillow (pip install pillow).
"""
import sys

from PIL import Image


def main(path, count=6):
    image = Image.open(path).convert("RGB")
    image.thumbnail((256, 256))
    quantised = image.quantize(colors=count)
    palette = quantised.getpalette()
    counts = sorted(quantised.getcolors(), reverse=True)  # [(pixels, palette index), ...]
    total = sum(pixels for pixels, _ in counts)
    for pixels, index in counts:
        r, g, b = palette[index * 3:index * 3 + 3]
        print(f"#{r:02x}{g:02x}{b:02x}  {pixels / total:6.1%}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 6)
```

### Route check (every path SKILL.md mentions exists)

```bash
cd .claude/skills/brand-studio && grep -oE '(references|assets|scripts)/[A-Za-z0-9._/-]+' SKILL.md | sort -u | while read -r f; do [ -e "$f" ] || echo "missing: $f"; done
```

## Done when

- [ ] `SKILL.md` is under about 150 lines (Anthropic's guidance is under 500), and its when-to-read table covers every file in the folder.
- [ ] The route check prints nothing, and no reference file links on to another file.
- [ ] A one-line request in a fresh session produced the asset in one or two prompts after intake questions, like Jay E's PDF ([08:42](https://www.youtube.com/watch?v=8NSyI-npJCU&t=522s)–[08:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=530s)).
- [ ] The session shows Claude opened only the references for that format.
- [ ] `check_brand_colors.py` prints OK on every output file.
- [ ] Scripts from chat that you reuse live in `scripts/`, and a repeat run shows `SKILL.md` calling them.
- [ ] Someone who knows the brand calls the output on-brand without being told which skill made it.
- [ ] For a refactor: on the same three requests, the new version did at least as well as the thick one.

## Pitfalls

- **A router that says "read everything first."** It loads the whole folder on every run and throws away the benefit.
- **References that point to more references.** Claude may only preview files that are linked from other reference files. Link everything straight from `SKILL.md` (Beyond the source).
- **Describing visuals in words.** AI LABS's point about text summaries losing detail ([10:28](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=628s)–[10:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=645s)) applies to your own references too. Store hex values, sizes and font names, not phrases like "a warm, confident orange".
- **The same values in two places.** If `brand.html` and `palette.json` drift apart, the checker passes off-brand work. Keep `palette.json` canonical and update `brand.html` from it.
- **Unclear script intent.** For each script, say whether Claude should run it or read it, and give the command. List dependencies too, or `extract_palette.py` fails where Pillow isn't installed.
- **Teaching the model what it knows.** References should hold what is specific to you, meaning your workflow and your business ([32:09](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1929s)–[32:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1937s)). General design advice is noise.
- **Mistaking elaborate for effective.** AI LABS found that some design skills run impressive-looking workflows and still produce a site like every other AI site ([00:05](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=5s)–[00:11](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=11s)). Judge a skill by its output.
- **Scripts you haven't read.** Jay E built a system-cleanup skill from a post on X and ran it on his machine ([06:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=372s)–[06:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=397s)). Read every command before a skill runs it. Ras Mic warns that downloaded skills are an easy way to get attacked ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)–[13:07](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=787s)). See [[Build vs Install Third-Party Skills]].
- **Assuming scripts behave the same everywhere.** A script that works in Claude Code may lack packages or network access in other Claude environments (Beyond the source).

## Variations

- **Per-area skills.** Split into narrow skills, as Jakub Krehel does for typography, colour and accessibility, when you apply them separately ([08:56](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=536s)–[09:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=552s)).
- **Style recipes.** Add `references/style-recipes/` with an index and one file per reference site. web-design-engineer does this with recipes for sites such as Apple and Linear ([04:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=280s)–[04:44](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=284s)); its repo layout is under Beyond the source.
- **A locked style for the whole project.** Extract values from reference images into a locked style file that every screen uses, after tastemaker, whose decisions carry across the whole project ([10:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=634s)–[10:40](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=640s), [10:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=655s)–[10:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=659s)).
- **Techniques, not just principles.** Meng To's skill set carries concrete techniques and specific effects alongside the principles in his Awwwards skill ([08:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=507s)–[08:34](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=514s)). Add a `references/effects.md` with working snippets.
- **A vocabulary reference.** Add a glossary that turns vague requests into exact terms, as Emil Kowalski's animation-vocabulary skill does for motion ([01:35](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=95s)–[01:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=101s)).
- **Beyond design.** The same shape suits any skill with detail that only some requests need, such as one reference per dataset, client or product (Beyond the source).
- **A dashboard button.** Trigger the skill with `claude -p` and a chosen model and effort ([09:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=580s)–[09:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=596s)). See [[Build an Agentic OS Dashboard]].
- **Keep improving it.** Log runs, fix failures and A/B-test changes with [[Skill Improvement Loop]].

## Sources

- [[Jay E - The ARMS Framework for a Claude Agentic OS]]:
  - skills as shortcuts to SOPs, and skill-creator ([05:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=325s)–[06:37](https://www.youtube.com/watch?v=8NSyI-npJCU&t=397s));
  - thin vs reference-rich skills, /robo and its brand HTML, the PDF demo and the refactor prompt ([06:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=399s)–[09:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=542s));
  - headless runs ([09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s)–[10:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=633s));
  - department router files ([12:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=736s)–[13:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=809s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]:
  - the default AI look, and why skills help ([00:00](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=0s)–[00:43](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=43s));
  - skills in Claude settings and Claude Design ([00:51](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=51s)–[01:07](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=67s));
  - web-design-engineer's references ([04:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=241s)–[05:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=314s));
  - the single-file landing-page skill ([05:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=324s)–[06:41](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=401s));
  - Meng To ([07:27](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=447s)–[08:53](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=533s));
  - Jakub Krehel ([08:55](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=535s)–[10:13](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=613s));
  - tastemaker ([10:15](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=615s)–[11:21](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=681s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]:
  - progressive disclosure ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)–[05:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=324s));
  - skills built without a successful run, and the risks of installed skills ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)–[13:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=790s));
  - the token count demo ([29:40](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1780s)–[31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s));
  - including only what is unique to you ([32:06](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1926s)–[32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).
- [[Nate Herk - Build Skills Instead of Agents]]: saving a working script into the skill, and his carousel renderers ([01:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=86s)–[02:52](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=172s)).
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]: the one-page brand book, building one from a website, and converting it to JPEG ([07:54](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=474s)–[08:25](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=505s)).
- *Caption fixes used here:*
  - "skill.mmd" is SKILL.md;
  - "Claude P" / "cloud hyphen P" is `claude -p`;
  - "Entropic" is Anthropic;
  - "Awards" is Awwwards;
  - "email design engineering" is emil-design-eng;
  - "Jakob" is Jakub Krehel.

## Beyond the source

*Not from the videos. Each item was checked at the linked page on 2026-09-15.*

- **Skill folders in Claude Code.**
  - **Location.** Skills live in `~/.claude/skills/<name>/` (personal) or `.claude/skills/<name>/` (project). Supporting files sit beside `SKILL.md`, and Claude reads them only when needed. Keep `SKILL.md` under 500 lines.
  - **Variables.** `${CLAUDE_SKILL_DIR}` expands to the skill folder and `$ARGUMENTS` to the text after the command.
  - **Pre-approving a script.** `allowed-tools` can pre-approve one, e.g. `Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)`.
  - **Recurring cost.** Once invoked, a skill's content stays in context for later turns, so every line in `SKILL.md` costs something.

  Source: [skills docs](https://code.claude.com/docs/en/skills).
- **Anthropic's authoring guide.**
  - **Structure.** Treat `SKILL.md` as a table of contents that points to detail. Keep references one level deep, since Claude may only partly read files that are linked from other files. Give reference files over 100 lines a contents list.
  - **Scripts.** Say whether each script should be run or read. Ready-made scripts are more reliable than generated code, and only their output uses context.
  - **Domains.** For a skill covering several areas, split references by domain (its example uses finance, sales and product files) so a request reads only the file it needs.
  - **Descriptions** should be written in the third person.
  - **Environments.** claude.ai can install npm and PyPI packages, but the Claude API's code environment has no network access and no runtime installs.

  Source: [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- **The open Agent Skills layout.**
  - **Folders.** The spec names `scripts/`, `references/` and `assets/` as optional folders.
  - **Loading** happens in stages: metadata (about 100 tokens) at startup, the `SKILL.md` body (under 5,000 tokens recommended) on activation, and other files only when needed.
  - **Limits.** `name` is at most 64 characters and must match the folder name; `description` is at most 1,024 characters.

  Source: [Agent Skills specification](https://agentskills.io/specification).
- **Claude apps.** Add a custom skill under Customize > Skills by uploading a ZIP of the skill folder; code execution and file creation must both be turned on. Skills are available on Free, Pro, Max, Team and Enterprise plans. The help article says skills work in chat and Cowork, in the Claude for Excel, PowerPoint, Word and Outlook add-ins, and (in beta) in Claude Code. It doesn't mention Claude Design, so AI LABS's point that settings skills carry over to Claude Design rests on the video. Source: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
- **Anthropic's own examples.**
  - [brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) keeps its colour hex values and typefaces (Poppins for headings, Lora for body) inline in a single short `SKILL.md`. A small brand can fit in one file.
  - [theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) keeps its themes in a `themes/` folder, with a showcase PDF alongside.
- **web-design-engineer's layout.** Its `references/` folder includes `design-calibration.md`, `failure-patterns.md`, `critique-guide.md`, and a `style-recipes/` folder with an `INDEX.md` and 25 recipes. `SKILL.md` ends with a references routing table that maps situations to files. Source: [garden-skills repo](https://github.com/ConardLi/garden-skills).
- **tastemaker's scripts.** Its Python scripts include `extract_palette.py` (reads pixel values with Pillow), `generate_palette.py`, `check_contrast.py` and `anti_slop_scan.py`. Decisions are saved to `.tastemaker/style-lock.md` per project and `~/.tastemaker/profile.md` per developer. Source: [tastemaker repo](https://github.com/codeswithroh/tastemaker).
- **Headless runs.** `claude -p` expands `/skill-name` in the prompt, and `--model` and `--effort` set the model and effort for a run. `--bare` skips skill discovery, so don't use it for skill runs. Source: [headless docs](https://code.claude.com/docs/en/headless), [CLI reference](https://code.claude.com/docs/en/cli-reference).

## Related

- Concepts: [[Agent Skills]] · [[CLAUDE.md as a Router]] · [[Escaping the Default AI Design Look]] · [[Context Window Management]] · [[Build vs Install Third-Party Skills]] · [[Agentic OS]]
- Techniques: [[Skill Improvement Loop]] · [[Build a Skill from a Successful Run]] · [[Build a Distinctive Site with Design Skills]] · [[Build an Agentic OS Dashboard]] · [[Workflow Audit into Skills]] · [[Keep CLAUDE.md Lean]] · [[Tiered Lookup Routing]]
- Tools and people: [[Claude Code]] · [[Claude Design]] · [[Jay E]] · [[AI LABS]] · [[Ras Mic]]
- [[Home]]
