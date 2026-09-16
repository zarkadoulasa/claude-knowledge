---
type: technique
goal: "Build a landing page whose scroll drives the story (scrubbed video, counters, reveals) from a written intake, owned or generated assets and smooth GSAP-grade motion, then check it with keyframe screenshots, a human content review and one section-by-section feedback pass"
difficulty: intermediate
time_to_build: "Half a day for a first page including review (vault estimate; Nate's first build ran about 30 minutes)"
sources: ["[[Nate Herk - The Scrollcraft Website Design Skill]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tools: ["[[Scrollcraft]]", "[[Claude Code]]", "[[Higgsfield]]"]
tags: [topic/design, topic/skills, topic/claude-code, topic/verification, topic/media, topic/marketing]
---

# Build a Scroll-Driven Landing Page

## Goal

Ship a landing page where the visitor's scroll controls what happens, reviewed for both how it looks and whether its facts are right.

- **The idea.** [[Nate Herk - The Scrollcraft Website Design Skill]] ties the scroll to something happening on the page [00:54](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=54s). Visitors can scroll backwards or forwards while images move, numbers fade in or images fade out [07:53](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=473s).
- **Why.** Nate likens a landing page to short-form content: no early hook, no interest [01:26](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=86s). [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] say GSAP motion is at its best on landing pages and scroll storytelling [09:08](https://www.youtube.com/watch?v=Ot582-E61ac&t=548s).

## Use when

- **Redesigning a plain site without losing its identity.** Nate's rebuild kept the copy, branding and feel [00:31](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=31s).
- **You're selling one offer as a story.** In [[Nate Herk - Claude as a One-Person Marketing Team]], the site opens on the customer's pain rather than the product [19:16](https://www.youtube.com/watch?v=yCACmFTiCto&t=1156s).
- **Not for app screens.** AI LABS say the direction-first design skill doesn't suit functional UI [02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s). Use [[Build Product UI from a Component Registry]] instead.

## Prerequisites

- **[[Claude Code]] in a project folder.** Both Nate videos use the desktop app [02:43](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=163s). *Vault:* use git to diff feedback rounds.
- **One scroll-building route:**
  - **[[Scrollcraft]]:** install it as a plugin, or copy its folders in [02:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=177s).
  - **Scroll World:** a public repo for 3D, interactive scroll sites [16:21](https://www.youtube.com/watch?v=yCACmFTiCto&t=981s).
  - **GSAP's official skills** (AI LABS [08:29](https://www.youtube.com/watch?v=Ot582-E61ac&t=509s)). *Vault:* the route when you direct the build yourself.
- **Brand context and assets:** logos, guidelines, product shots and positioning. See [[Build a Brand-Aware Marketing Project]].
- **Optional paid media service:** a Kie.ai key in the project's environment variables for Scrollcraft [05:11](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=311s), or [[Higgsfield]] connected in Claude [16:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=992s).
- **Time to read the skill first.** Per their READMEs, both scroll skills run scripts and can make paid calls (Beyond the source; [[Build vs Install Third-Party Skills]]).

## Steps

1. **Start with a short brief and let the intake ask the rest.**
   - **Nate's opening prompt** is a few adjectives, such as premium and trusted [03:49](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=229s), plus one anti-goal: no flight through a world of AI-generated assets [03:56](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=236s). The skill then interviews him [04:05](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=245s).
   - **The five questions shown on screen** (more follow off screen [08:10](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=490s); the current SKILL.md has eight topics, see [[Nate Herk - The Scrollcraft Website Design Skill]]):
     - Which section opens the page, and what sequence follows? [05:31](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=331s)
     - What one sentence must they believe by the end? [05:44](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=344s)
     - Which real assets do you own? [05:53](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=353s)
     - What will this site do that no other site does? That becomes the signature move [07:08](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=428s). It drives a page-wide mechanic, so pick it deliberately: Nate's "every claim has a receipt" [07:10](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=430s) shows up as a sources counter that unlocks as you scroll [09:59](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=599s) and a closing recap of all nine sources [11:31](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=691s).
     - Where should it feel calm, and where intense? [08:08](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=488s)
   - **Be as specific as your vision allows** [07:15](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=435s). Without a vision, the skill's built-in taste fills the gaps [07:23](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=443s).
   - **Describe the feeling** you want and have the model imagine being the visitor [08:18](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=498s). That models now respond to this is Nate's impression, not a test.

2. **Give it context, not a blank page.**
   - **Scrollcraft demo.** Claude had Nate's current site, brand assets and earlier builds [04:33](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=273s).
   - **Marketing video.** He asks for copy and structure aimed at the target person's pain and the brand promise [18:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1090s). Without it, he says, sites come out generic and bland [18:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1115s). Claude took its design system from the brand-guidelines PDF [19:10](https://www.youtube.com/watch?v=yCACmFTiCto&t=1150s).

3. **Use the assets you own first, and generate only what's missing.**
   - **Scrollcraft demo.** Nate keeps his existing photos [06:07](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=367s). The rest comes from one style line: minimal low-poly figures [06:44](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=404s) in the brand's colours [06:57](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=417s). Scrollcraft makes images, turns them into video and stitches the clips together [05:20](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=320s).
   - **Marketing video.** Higgsfield's Seedance 2.5 clips [20:39](https://www.youtube.com/watch?v=yCACmFTiCto&t=1239s) play forward as you scroll [20:49](https://www.youtube.com/watch?v=yCACmFTiCto&t=1249s).
   - **AI LABS.** Models left alone grab ill-fitting stock images, so generate hero images and clips from the agent [10:40](https://www.youtube.com/watch?v=Ot582-E61ac&t=640s).

4. **Build designed motion, not the stock reveal.**
   - **The default.** AI LABS say that when asked for animation, models almost always add the same slide-in on scroll [08:13](https://www.youtube.com/watch?v=Ot582-E61ac&t=493s).
   - **GSAP's skills** come from the GSAP team and cover basic movement through scroll-driven sequences [08:35](https://www.youtube.com/watch?v=Ot582-E61ac&t=515s).
   - **Why motion turns janky.** Animating size or position makes the browser rebuild the page every frame; the skill steers towards movement the browser handles easily [08:50](https://www.youtube.com/watch?v=Ot582-E61ac&t=530s).
   - **Make it a rule.** AI LABS's marketing skill sends all landing-page animation to the GSAP skill [09:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=561s); copy that into CLAUDE.md (starter below).
   - **Not every section needs heavy motion.** Of Nate's two perfume versions, one animates mainly its opening [01:53](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=113s).

5. **Self-check with keyframe screenshots.**
   - **What Scrollcraft does.** After building, it screenshots the site and zooms into the keyframes its automated harness can't judge [08:48](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=528s). The run took about 30 minutes and ended with one screenshot of the whole scroll [09:13](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=553s).
   - **No built-in check?** Use the keyframe prompt below and [[Build Verification into Every Task]].

6. **Review the content yourself.**
   - **What the self-check missed:**
     - screenshots of unknown origin [10:42](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=642s)
     - a wrong photo caption [11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s)
     - copy and a button link that needed fixing [11:26](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=686s)
     - in the marketing build, unfilled nutrition facts [20:22](https://www.youtube.com/watch?v=yCACmFTiCto&t=1222s)
   - **Check by hand** every number, caption, link and asset source.

7. **Scroll at normal speed.** Nate's draft looked boring at first glance [09:32](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=572s), and one animation ran too fast for a typical scroll [10:16](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=616s).

8. **Send one section-by-section feedback message.**
   - **Open with what worked,** so it stays [12:19](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=739s).
   - **Go top to bottom, one fix per section:**
     - The hero is bland and needs depth, because it's the hook [12:38](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=758s).
     - Keep the globe, but slow it down a lot [12:50](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=770s).
     - Give the founder section a scroll animation, and make the certification animation last longer [13:21](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=801s).
   - **Take facts from the source of truth,** e.g. the live site's real waitlist link [13:36](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=816s).
   - **Cut what doesn't work** [13:52](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=832s), and say the rest is fine [14:03](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=843s).

9. **Check v2 against your list, then ask for small follow-ups.**
   - **What v2 changed.** It removed the register section [14:14](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=854s), rebuilt the hero as a magazine cover [14:21](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=861s), added hover colours behind the sideways exhibit cards [15:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=912s) and fixed the link [15:34](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=934s).
   - **What vague feedback missed.** Exhibit A, which he had called bland without naming a fix [13:04](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=784s), was still static in v2 [15:01](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=901s), although he says all requested changes were done [15:38](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=938s).
   - **Follow-up.** Once he named a typewriter-style reveal, a regeneration added it [16:02](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=962s) and brought the faces and screens in one at a time [16:09](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=969s), leaving a small reload bug [16:17](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=977s).
   - *Vault reading:* name a concrete effect rather than saying a section "feels bland", and check each flagged section in v2 yourself rather than trusting an "all done" summary.

10. **Publish.** The marketing site ran only on localhost [21:04](https://www.youtube.com/watch?v=yCACmFTiCto&t=1264s). Nate's route is to push to GitHub, then deploy on Vercel [21:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1295s).

## Starter files & prompts

*Vault starter content: original wording, not taken from any source or skill file.*

**`design/scroll-brief.md`**

```markdown
# Scroll brief
- Feel, in three words:
- Not this (one anti-goal):
- The one action at the end:
- Belief by the last section (a single claim, not features):
- Journey in order: 1 hook · 2 … · 3 proof · 4 action
- Energy curve: calm at … · peak at … · settle at …
- Signature move (one thing no competitor page does):
- Owned assets (path → section):
- Generate only: subject · shared style line · brand hex values
- Motion budget: sections that move · sections that stay still
- Facts file: design/facts.md (every number, link and caption, with its source)
```

**Motion rule for `CLAUDE.md`**

```markdown
## Landing-page motion
- Use the GSAP skills for animation; no default fade-up-on-scroll.
- Animate transform and opacity only; never width, height, top or left.
- Scroll-linked sections must also work when scrolling back up.
- Respect prefers-reduced-motion: show final states without movement.
```

**Keyframe check prompt**

```text
Serve the page locally. Screenshot scroll depths 0/25/50/75/100% at 1440px
and 390px, plus one reduced-motion pass, into design/checks/round-N-sheet.png.
Per section, report anything clipped, overlapping, unreadable or frozen
mid-animation. Then match every number, caption and link to design/facts.md
and flag mismatches or missing sources. Don't fix anything yet.
```

**Feedback message template**

```text
Round N feedback. Keep everything I don't mention.
Worked, keep as is: …
Section by section:
- [section]: keep / change / cut · problem: … · fix: … · fact source: …
Remove entirely: …
Then mark each item done or not done.
```

## Done when

- [ ] `scroll-brief.md` answers every field, including the belief and the signature move
- [ ] Owned assets are used first, and every generated asset shares one style line
- [ ] Scroll-linked sections work in both directions at a normal scroll speed
- [ ] No animation changes width, height, top or left
- [ ] A keyframe sheet exists for desktop, phone and reduced motion
- [ ] A person has checked every number, caption and link against `facts.md`
- [ ] Every feedback item is ticked off against the v2 change report
- [ ] The page is deployed, or the reason it isn't is written down

## Pitfalls

- **Trusting a visual check to catch factual errors.** Screenshots show layout, not facts: Scrollcraft's self-check passed a mislabelled photo and a link that needed fixing (step 6).
- **Janky size and position animation.** It forces a page rebuild every frame (step 4); animate transform and opacity instead (Beyond the source).
- **Motion too fast to follow.** Nate had to ask for the globe to be slowed a lot (step 8). *Vault reading:* tie animation to scroll distance, not a timer.
- **Spending without noticing.** Generated video costs money, and neither Nate video sets a budget. Start from owned assets, and gate paid tools ([[Permissions and Approval Gates]]).
- **Extras of disputed cost.** img2threejs rebuilds an object from your image as a code-only 3D model, checked stage by stage against the image [01:13](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=73s). [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] say it burns many tokens, runs long and may lack detail at first [01:23](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=83s); its README instead calls it token-efficient, because Python scripts do the mechanical checks, and warns that unseen sides are guessed (Beyond the source).

## Variations

- **Scroll World route** ([[Nate Herk - Claude as a One-Person Marketing Team]]): paste the repo URL [17:27](https://www.youtube.com/watch?v=yCACmFTiCto&t=1047s), ask for careful design thinking [17:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1073s) and a premium-but-fun result [18:05](https://www.youtube.com/watch?v=yCACmFTiCto&t=1085s), and treat the output as a first pass [20:12](https://www.youtube.com/watch?v=yCACmFTiCto&t=1212s).
- **3D hero from a product photo** ([[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]): img2threejs output is plain code, so the model can sit on the landing page, animate and respond to visitors [00:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=40s), and the agent can recolour or relight it on request [00:52](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=52s). Give the agent the image and name the skill [01:05](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=65s), then keep asking it to improve specific parts [01:28](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=88s). Hidden sides are inferred (Beyond the source).
- **Build it yourself with GSAP** ([[AI LABS - Design Skills from Landing Pages to Mobile Apps]]): frontend-design or one taste preset for the look, GSAP skills plus the CLAUDE.md rule for motion ([[Build a Distinctive Site with Design Skills]]).

## Beyond the source

*Not from the videos. Checked 2026-09-15.*

- **Scrollcraft:** install steps and requirements are in [[Scrollcraft]]. https://github.com/nateherkai/scroll-craft
- **Scroll World:** `/plugin marketplace add oso95/scroll-world`, then `/plugin install scroll-world@scroll-world`. Needs ffmpeg, Python 3 with Pillow, Monid (default, pay per clip) and the Higgsfield CLI (stills, fallback); a six-scene 1080p chain costs about $27 per the README. https://github.com/oso95/scroll-world
- **GSAP skills:** `npx skills add https://github.com/greensock/gsap-skills`. GSAP, ScrollTrigger included, has been free since April 2025. https://github.com/greensock/gsap-skills · https://webflow.com/updates/gsap-becomes-free
- **ScrollTrigger:** `scrub` ties progress to the scrollbar, `pin` holds an element in place, `markers: true` shows trigger points. https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- **Reduced motion:** `gsap.matchMedia()` takes a `(prefers-reduced-motion: reduce)` condition and reverts its animations when it stops matching. https://gsap.com/docs/v3/GSAP/gsap.matchMedia()
- **img2threejs:** eight gated passes (blockout through optimisation), each reviewed visually, with Python scripts doing the validation; output is a TypeScript Three.js model factory. The README calls this token-efficient and says one image can't show hidden sides, so unseen faces are mirrored from visible ones. https://github.com/img2threejs/img2threejs
- **Why transform and opacity:** they skip layout work; in web.dev's test a `top`/`left` animation dropped 50% of frames, `transform` 1%. https://web.dev/articles/animations-guide

## Sources

- [[Nate Herk - The Scrollcraft Website Design Skill]]: intake, assets, keyframe self-check, content review, feedback pass.
- [[Nate Herk - Claude as a One-Person Marketing Team]]: Scroll World route, brand context, scroll-scrubbed clips, publishing.
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: GSAP skills, the stock-reveal tell, smooth motion, generated visuals.
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: img2threejs 3D hero and its cost.

## Related

- **Concepts:** [[Escaping the Default AI Design Look]] · [[Verification Before Done]] · [[Generating Images and Video with Claude]]
- **Techniques:** [[Build a Distinctive Site with Design Skills]] · [[Generate On-Brand Images from Claude Code]] · [[Create and Reuse a Claude Design System]] · [[Benchmark-Driven Design Critique]]
- **Tools:** [[Scrollcraft]] · [[Higgsfield]] · [[Claude Code]]
- **People:** [[Nate Herk]] · [[AI LABS]]
- [[Home]]
