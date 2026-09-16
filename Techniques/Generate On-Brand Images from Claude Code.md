---
type: technique
goal: "Give Claude Code a small image skill that keeps outputs on brand, drafts cheap numbered variants, re-renders only the pick at high quality, can grow to video models, and never starts a paid batch without an estimate and your approval"
difficulty: intermediate
time_to_build: "About an hour for the skill, key and first batch; minutes per batch after that (vault estimate)"
sources: ["[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]"]
tools: ["[[Claude Code]]", "[[Higgsfield]]"]
tags: [topic/media, topic/design, topic/marketing, topic/skills, topic/claude-code, topic/permissions]
---

# Generate On-Brand Images from Claude Code

> **Provenance.** The method comes from [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]. Jay drives GPT Image 2 on fal.ai through his own skill, but never shows how he set up the key or what it cost. [[Nate Herk - Claude as a One-Person Marketing Team]] adds a [[Higgsfield]] route and reports his costs. **The skill outline, script, permission rule and prompts are original vault starter content**, checked against fal's and Anthropic's docs.

## Goal

Claude writes the image prompts, not you, which is Jay's reason for pairing an image model with an agent ([04:30](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=270s)). You end up with a project skill that attaches your brand references, drafts cheap variants, and re-renders only the one you pick. It logs every prompt and its cost, and can later animate a still or seed a UI build.

## Use when

- **You need on-brand assets.** Ads, carousels, pricing cards, merch or mockups, and you have a brand book or a website.
- **You want volume to steer from.** Jay says image models need variation before you can direct them ([10:01](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=601s)); Nate says volume beats luck ([30:24](https://www.youtube.com/watch?v=yCACmFTiCto&t=1824s)).
- **Not for figures you must trust.** Jay's chart cited sources from Claude's research, and the video never checks them ([03:29](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=209s)).

## Prerequisites

- **[[Claude Code]].** Jay says the skill installs the same way in the desktop app and in IDE extensions ([05:39](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=339s)).
- **A way to call an image model**, either of:
  - a fal.ai key saved as `FAL_KEY` in a git-ignored `.env`, plus `pip install fal-client`;
  - a paid Higgsfield plan added as a connector (Nate, [16:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=987s)).
- **A brand book and logo.** Save a one-page brand book as a JPEG, because the model won't take a PDF ([08:20](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=500s)), and have a logo PNG. With no brand book, give Claude your website ([08:04](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=484s)) or see [[Create and Reuse a Claude Design System]].
- **A spending cap** for each batch.

## Steps

1. **Create the skill** using the layout below. Jay installs his ready-made skill with an install prompt, and Claude lists what it can do ([06:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=406s)). Writing your own means you've read every line that spends money ([[Build vs Install Third-Party Skills]]).
2. **Store the references inside the skill.** Jay pastes the brand book path ([08:16](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=496s)) and the logo path ([08:39](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=519s)) into every prompt. A `references/` folder does that once ([[Build a Reference-Rich Skill]]).
3. **Gate spending** with the `ask` rule below, and put your cap in SKILL.md.
4. **Get a plan and an estimate first.** Jay optionally asks Claude to outline its steps ([07:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=466s)). Its plan: prepare and convert the references, match them to each image, write the prompts, then start nine generations in parallel ([09:12](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=552s)). Prompt 1 adds a cost line and waits for your go-ahead.
5. **List every asset in one prompt.**
   - **Jay** asks for a magazine spread, pricing cards, charts, a brand kit, ads and merch at once ([08:46](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=526s)). Claude sends one prompt per asset, each with its references ([08:57](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=537s)).
   - **Nate** briefs Claude like a colleague: why, what, where to save, and what it cost ([24:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1442s)). He added no ad expertise himself, and says yours would make results better ([27:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=1642s)).
6. **Review at full size.** By default Claude returns only file paths ([09:29](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=569s)). One of Jay's posts came out pixelated because it wasn't rendered at top resolution ([02:05](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=125s)).
7. **Draft variants as a numbered grid.** A 5×5 grid is billed as one image ([10:11](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=611s)). Numbering the cells 1–25 lets you name one later ([10:22](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=622s)). His prompt puts each number in a small circle at top left and includes the reference paths ([10:40](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=640s)).
8. **Re-render the pick at high quality.** Name the cell and ask for it on its own at top settings ([11:00](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=660s)). Claude finds that cell's prompt and sets quality and resolution ([11:11](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=671s)). *Vault note:* this is a fresh render, not an upscale, so it can differ from the cell.
9. **Add a model from its docs, then test it.**
   - fal's model pages link docs written for LLMs ([11:47](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=707s)).
   - Jay pastes Kling 3.0's docs into the session where he installed the skill and asks Claude to add the model ([11:51](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=711s)). Claude updates the skill ([12:19](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=739s)).
   - **Vault guard:** save the docs as a reference file, make one cheap test call, then edit SKILL.md (Prompt 4).
10. **Animate a still.** Ask for a Kling animation that keeps the text fixed and the aspect ratio unchanged ([12:41](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=761s)). Claude works out the API call itself ([12:49](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=769s)). For clips with several shots, use [[Storyboard-First AI Video and Motion Graphics]].
11. **Optional: mockup to HTML.** Ask Claude Code to build a generated UI image as HTML in a named style and open it on localhost ([13:33](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=813s)). Expect about 50–60% alignment ([13:58](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=838s)) and some refinement ([14:21](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=861s)). See [[Build a Distinctive Site with Design Skills]].
12. **Pick by taste, then codify.**
    - **Jay** lets a human choose from several iterations ([14:29](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=869s)).
    - **Nate** makes a skill from a format he liked and bans one he didn't ([30:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1802s)). He reuses saved creatives with new copy ([27:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=1625s)), or the reverse: one copy line he likes put onto all 18 graphics for a fresh round of ads ([27:12](https://www.youtube.com/watch?v=yCACmFTiCto&t=1632s)).

## Starter files & prompts

*Original vault starter content.*

```text
.claude/skills/brand-images/
├── SKILL.md
├── references/
│   ├── brand-book.jpg      # palette, type, logo rules
│   ├── logo.png
│   └── models/             # one file per model, from provider llms.txt
└── scripts/generate.py
output/images/<campaign>/   # renders + prompts.jsonl
```

### SKILL.md outline

```markdown
---
name: brand-images
description: Generates on-brand images (ads, carousels, mockups, merch) with GPT Image 2 on fal. Use for image requests, variant grids or re-rendering a grid cell.
---
# Brand images
## Before generating
1. Attach references/brand-book.jpg and references/logo.png.
2. Show a plan (one line per image: purpose, size, quality, count) and a dollar estimate.
3. Wait for "go". Never exceed $5 per batch without asking again.
## Rules
- Drafts: quality low, or one numbered N×N grid. Finals: quality high, picked images only.
- Always run: python .claude/skills/brand-images/scripts/generate.py ... --out output/images/<campaign>
- Grid cell N: rebuild its prompt from prompts.jsonl, render it alone at high.
- New model: save its llms.txt to references/models/, run the cheapest test, then update this file.
- Finish by reporting files, total cost, and any wrong logo or text.
```

### scripts/generate.py

```python
# Vault starter. Needs: pip install fal-client, FAL_KEY in the environment.
import argparse, json, pathlib, time, urllib.request
import fal_client

p = argparse.ArgumentParser()
p.add_argument("--prompt", required=True)
p.add_argument("--refs", nargs="*", default=[])
p.add_argument("--quality", default="low", choices=["low", "medium", "high"])
p.add_argument("--w", type=int, default=1024)
p.add_argument("--h", type=int, default=1024)
p.add_argument("--n", type=int, default=1)
p.add_argument("--out", required=True)
a = p.parse_args()

args = {"prompt": a.prompt, "quality": a.quality, "num_images": a.n,
        "image_size": {"width": a.w, "height": a.h}, "output_format": "png"}
endpoint = "openai/gpt-image-2"
if a.refs:  # references must be URLs, so upload local files first
    endpoint += "/edit"
    args["image_urls"] = [fal_client.upload_file(r) for r in a.refs]

result = fal_client.run(endpoint, arguments=args)
out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
files = []
for i, img in enumerate(result.get("images", [])):  # confirm schema in the model's llms.txt
    f = out / f"{int(time.time())}-{i}.png"
    urllib.request.urlretrieve(img["url"], f); files.append(str(f))
with open(out / "prompts.jsonl", "a") as log:
    log.write(json.dumps({"endpoint": endpoint, "args": args, "files": files}) + "\n")
print("\n".join(files))
```

### Permission gate (`.claude/settings.json`)

```json
{ "permissions": { "ask": [
  "Bash(python .claude/skills/brand-images/scripts/generate.py *)"
] } }
```

### Prompts

```text
PROMPT 1 (plan): Use brand-images. Campaign: <name>. Assets: <list with sizes>.
Show the plan and total estimate first, draft at low quality, and wait for my go.

PROMPT 2 (grid): Draft <asset> as one 5x5 grid image at <size>, medium quality.
Number each cell 1-25 in a small top-left circle. Use the brand references.

PROMPT 3 (pick): Cell <N> is the one. Rebuild its prompt from prompts.jsonl as a
standalone image, give the cost, and after my OK render it at high quality.

PROMPT 4 (new model): Below are fal's llms.txt docs for <model>. Save them to
references/models/<model>.md, propose the cheapest test call with its cost, and
update SKILL.md only after it succeeds. <paste docs>
```

## Done when

- [ ] `FAL_KEY` is only in a git-ignored `.env`, and never appears in chat, logs or SKILL.md.
- [ ] A batch request shows a dollar estimate and waits, and the `ask` rule prompts on each call.
- [ ] At 100% zoom, the final images show the right logo and palette, and the text is spelled correctly.
- [ ] One grid cell has been re-rendered at high quality from its logged prompt.
- [ ] Every render and every model test has a line in `prompts.jsonl`.

## Pitfalls

- **fal defaults to high quality.** A 1024×1024 image costs about $0.21 at high but $0.006 at low, so set quality on every call.
- **Local paths aren't references.** The edit endpoint accepts URLs only. Jay's on-camera local paths ([08:16](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=496s)) skip that step.
- **Cropped cells and unchecked numbers.** Re-render a cell rather than cropping it, and check any figures against the data ([[Verification Before Done]]).
- **Logo drift.** The logo in Nate's sizzle reel was slightly wrong ([28:44](https://www.youtube.com/watch?v=yCACmFTiCto&t=1724s)).
- **Cost after the fact.** Nate asks for the cost only when runs finish ([22:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1355s)). Estimate first.
- **Bash rules match command text,** so the skill always uses one exact command.

## Variations

- **Higgsfield instead of fal.** Nate asks Claude to use Higgsfield with the brand context ([22:30](https://www.youtube.com/watch?v=yCACmFTiCto&t=1350s)), and 18 ad images cost him $3.43 ([27:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=1656s)). He admits it isn't the cheapest option, but the models are all in one place ([27:50](https://www.youtube.com/watch?v=yCACmFTiCto&t=1670s)). Gate it with an `ask` rule on `mcp__<server>`, using the name `/mcp` shows.

## Where sources disagree

- **Docs first, or a working run first?** Jay adds Kling from pasted docs before any Kling call ([11:51](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=711s)), and the call works ([12:49](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=769s)). [[Ras Mic]] says skills written without a successful run botch API calls ([11:18](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=678s)). *Vault:* reference file, then a test call, then update the skill ([[Build a Skill from a Successful Run]]).
- **Install or build?** Jay shares a ready-made skill that calls a paid API ([05:52](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=352s)); Ras Mic calls skill marketplaces an easy attack route ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)).
- **Taste or scores?** Jay has a human pick ([14:29](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=869s)); [[Benchmark-Driven Design Critique]] scores designs. Marketing stills have no objective bar, so this note uses a human pick after a cheap grid.

## Sources

- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]: skill ([05:47](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=347s)), batch ([07:39](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=459s)), grid ([09:51](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=591s)), Kling ([11:22](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=682s)), mockup ([13:10](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=790s)). Caption fix: "File AI" is fal.ai.
- [[Nate Herk - Claude as a One-Person Marketing Team]]: briefs and costs ([22:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1326s)), results ([25:47](https://www.youtube.com/watch?v=yCACmFTiCto&t=1547s)).

## Beyond the source

*Checked 2026-09-15.*

- **GPT Image 2 on fal.**
  - **Endpoints:** `openai/gpt-image-2`, and `openai/gpt-image-2/edit`, which takes up to 16 `image_urls`.
  - **Settings:** quality defaults to `high`. Each call makes 1–4 images, at sizes in multiples of 16 up to a 3,840 px edge.
  - **Cost** for 1024×1024: about $0.006 low, $0.053 medium, $0.211 high.
  - Sources: [model page](https://fal.ai/models/openai/gpt-image-2), [edit docs](https://fal.ai/models/openai/gpt-image-2/edit/llms.txt).
- **Uploads.** `fal_client.upload_file` returns a CDN URL ([fal-client](https://pypi.org/project/fal-client/)). Jay's README also requires public URLs for references ([GitHub](https://github.com/robonuggets/gpt-image-2-skill)).
- **Kling 3.0 standard image-to-video.** Needs `start_image_url`; 3–15 s clips, audio on by default, no documented aspect-ratio parameter; $0.084/s silent ([llms.txt](https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video/llms.txt)).
- **Claude Code.**
  - **Skills:** project skills live in `.claude/skills/<name>/SKILL.md`; keep the file under 500 lines ([skills](https://code.claude.com/docs/en/skills)).
  - **Permissions:** rules are checked deny, then ask, then allow. `mcp__<server>` covers all of that server's tools. Bash rules match the command text ([permissions](https://code.claude.com/docs/en/permissions)).

## Related

- [[Generating Images and Video with Claude]] · [[Design Systems for Claude]] · [[Build a Brand-Aware Marketing Project]] · [[Permissions and Approval Gates]] · [[Connecting Claude to External Tools]] · [[Skill Improvement Loop]]
- [[Jay E]] · [[Nate Herk]] · [[Home]]
