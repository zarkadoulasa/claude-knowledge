---
type: technique
goal: "Make every Claude task end with an objective check (tests, type checks, a screenshot and browser pass, or a rubric graded separately) so 'done' arrives with evidence instead of a claim."
difficulty: beginner
time_to_build: "About an hour for the CLAUDE.md block, verifier subagent and optional Stop hook (estimate, not from the videos)"
sources: ["[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[AI LABS - Types of Claude Loops Explained]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[Nate Herk - Build Skills Instead of Agents]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]"]
tools: ["[[Claude Code]]", "[[Claude in Chrome]]", "[[Claude Design]]", "[[Claude Managed Agents]]", "[[Unlazy]]", "[[Scrollcraft]]"]
tags: [topic/verification, topic/claude-code, topic/planning, topic/prompting, topic/subagents, topic/design, topic/skills]
---

# Build Verification into Every Task

## Goal

Stop being the one who checks everything. Every task Claude does should end with something it ran and read: a test suite, a type check, a screenshot and click-through, or a rubric grade. It should also show you the output. The idea behind this is [[Verification Before Done]]; this note is the setup.

- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] rates verification S tier or higher. Claude should check its own work before calling something done, because by itself it can't tell whether the code is correct ([08:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=517s), [08:49](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=529s), [08:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=535s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]] puts those checks into Claude's to-do list. Claude builds, checks, and only then comes back for your feedback ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s), [04:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=260s), [04:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=264s)).

## Use when

- Work reported as done keeps turning out not to be. You only find out by checking yourself, and anything built on top inherits the problem ([[AI LABS - The Unlazy Skill for Lazy Agents]] [02:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=164s), [02:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=173s)).
- You're doing front-end or UI work. Claude can't see what it built without screenshots or a browser (Sloth [09:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=582s)), and Nate calls browser checks huge for front-end work ([09:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=586s)).
- You want to leave Claude running unattended. Tests are what make that safe ([[AI LABS - Types of Claude Loops Explained]] [03:07](https://www.youtube.com/watch?v=8wsM0euQOvc&t=187s)).
- A test suite can't capture what "good" means (a report, a page, a design), so a rubric or a review skill has to stand in. [[Anthropic - What Is Claude Managed Agents]] grades work against a written rubric ([00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s)), and [[AI LABS - Claude Design Skills for Beautiful Sites]] runs a skill that scores an existing design ([05:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=303s)).
- A skill makes the same kind of output again and again. Build the checks into it so its first output is an internal draft ([[Nate Herk - Build Skills Instead of Agents]] [08:37](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=517s)).

## Prerequisites

- **[[Claude Code]] in a git repository.** Git gives you before/after comparisons ([09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s)). AI LABS wants a way to roll back to the last working version but names no mechanism ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)); git provides it (vault choice, see [[Tests-First Goal Loop]]).
- **Your language's test runner, type checker and linter**, where they exist (Sloth [09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)).
- **For UI work:** the app running locally, plus a browser tool Claude can drive.
  - Nate names Chrome DevTools ([09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)). The Sloth says screenshot and browser testing are now built in ([09:54](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=594s)).
  - Setup for [[Claude in Chrome]] and the Chrome DevTools MCP is under *Beyond the source*.
- **For the optional Stop hook:** `jq` and a POSIX shell (vault starter requirement).
- **Optional checkers:** Reticle needs a web or desktop app you own plus its dev-only SDK; anti-slop needs a JS or TS project that runs Oxlint (*Beyond the source*).

## Steps

1. **Write a definition of done into CLAUDE.md.** Paste starter A and swap in your commands. It encodes:
   - **The Sloth's rules:** tests before the implementation ([09:06](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=546s)), tests only for what matters ([09:19](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=559s)), type checker and linter before done ([09:30](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=570s)), and screenshot and browser testing for UI ([09:37](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=577s)).
   - **The loops video's rollback rule:** save every working version ([03:32](https://www.youtube.com/watch?v=8wsM0euQOvc&t=212s)).
   - **Keep it short**, and move longer procedures into skills ([[Keep CLAUDE.md Lean]]).
2. **Put a verification to-do after every build to-do.** Nate's example: build the website, then screenshot it and check it looks right, then use Chrome DevTools to confirm nothing is functionally broken ([04:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=247s)–[04:19](https://www.youtube.com/watch?v=jqoFP9QapXI&t=259s)). Prompt B asks for this in every plan.
   - **Nate's gate:** don't move to the next to-do until Claude is 95% confident in the current one ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)).
   - **Prompt B changes the gate.** It asks for pasted evidence instead of a confidence figure, following Unlazy's point that completion Claude grades for itself is exactly what fails ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s), [08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s)).
3. **Make tests or type checks the gate for code.**
   - **Tests first, then the implementation (prompt C).**
     - **Written afterwards,** the tests pass Claude's own code by design (Sloth [09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)–[09:17](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=557s)).
     - **Written first,** they throw errors whenever Claude builds a feature the wrong way (Loops [02:58](https://www.youtube.com/watch?v=8wsM0euQOvc&t=178s)–[03:06](https://www.youtube.com/watch?v=8wsM0euQOvc&t=186s)).
   - **For longer runs, make passing them a /goal condition.** The Sloth's example goal is every test passing with no type errors ([19:14](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1154s)). The loops video sets the goal as passing all the tests ([03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)).
   - **Full loop:** [[Tests-First Goal Loop]].
   - **Lint for patterns agents tend to write.** anti-slop reports specific coding mistakes to the agent, so you don't have to read the code ([[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] [11:43](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=703s)). Some rules catch wasted work that slows the app; others are the author's style preferences ([11:51](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=711s)). It covers JS/TS (*Beyond the source*): keep the rules you agree with and add `oxlint` to starters A and G.
4. **Run a screenshot and browser loop for anything visual.** Prompt D runs all three passes; tool setup is under *Beyond the source*.
   - **Visual pass.** Ask Claude to screenshot the page and say whether the layout looks right. It analyses the image and reports what's off ([09:06](https://www.youtube.com/watch?v=jqoFP9QapXI&t=546s)–[09:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=555s)). Nate has it design, screenshot and fix for about three rounds before he sees V1 ([09:18](https://www.youtube.com/watch?v=jqoFP9QapXI&t=558s)–[09:27](https://www.youtube.com/watch?v=jqoFP9QapXI&t=567s)).
   - **Functional pass.** Claude opens the app, clicks around and checks that features work (Nate [09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s)–[09:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=583s); Sloth [09:46](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=586s)).
   - **Optional reference.** Give Claude screenshots of sites you like and ask it to match the look (Nate [10:05](https://www.youtube.com/watch?v=jqoFP9QapXI&t=605s)).
   - **Runtime pass.** Pages can load and look right while other things fail ([01:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=100s)). Reticle follows what happens inside the running app and marks each check worked, failed or not enough information ([02:26](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=146s)). Prompt H counts the third verdict as unmet.
   - **Animated pages.** [[Scrollcraft]] screenshots keyframes along the scroll ([[Nate Herk - The Scrollcraft Website Design Skill]] [08:48](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=528s)), yet a wrong photo caption still got through ([11:12](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=672s)). Prompt I adds a content table that a person signs off.
5. **Use a rubric for outputs without tests.** Starter E is a rubric template; starter F is a verifier subagent that grades against it.
   - **Write checkable criteria**, like the Managed Agents demo's measurable ones ([00:56](https://www.youtube.com/watch?v=NLWiIj47IdI&t=56s)–[01:02](https://www.youtube.com/watch?v=NLWiIj47IdI&t=62s)).
   - **Grade in a separate context.** A grader running in its own context window checks the output, and Claude reads the feedback, fixes what it missed and resubmits ([01:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=75s)–[01:26](https://www.youtube.com/watch?v=NLWiIj47IdI&t=86s)).
   - **For design work,** the design video uses skills that score a page, or review it and list findings to iterate on ([05:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=303s)–[05:12](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=312s), [09:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=558s)–[09:22](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=562s)). See [[Build a Distinctive Site with Design Skills]].
   - **Inside a skill, put the block in SKILL.md.** [[Nate Herk - Build Skills Instead of Agents]] suggests adding one to almost any skill: define acceptance criteria, draft, inspect, fix, re-check, then report what was checked and what couldn't be verified ([08:11](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=491s)). The evidence must come from outside the draft ([07:59](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=479s)). Starter J is a vault version.
6. **Keep the judge separate from the worker.**
   - **No editing tools for the reviewer.** AI LABS' score-only reviewer has none ([10:25](https://www.youtube.com/watch?v=8wsM0euQOvc&t=625s)–[10:31](https://www.youtube.com/watch?v=8wsM0euQOvc&t=631s)); starter F follows the same idea.
   - **Built-in reviews after a feature lands.** The Sloth runs Claude Code's code review and security review skills ([05:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=327s)–[05:35](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=335s)).
   - **Whole-app review with several critics or a scorer:** see [[Multi-Agent Review and Scoring Loops]]. The loops video keeps the expensive fan-out version for large apps ([11:05](https://www.youtube.com/watch?v=8wsM0euQOvc&t=665s)).
7. **Require evidence and honest gaps in the final report.** Claude's summary lists each check it ran with its result, and names anything left unfinished.
   - **A tick without proof counts as unmet** under Unlazy's rules ([08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s)–[08:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=501s)).
   - **Name dropped items.** Giving up an item by name with a reason beats dropping it silently ([08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s)–[08:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=537s)).
   - **For a file-based ledger checked by a script,** use [[Evidence-Gated Completion Ledger]].
8. **Optional: make the gate deterministic.** CLAUDE.md lines are instructions, and Unlazy notes that instructions are the first thing lost in a long session ([07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s)). Starter G is a Stop hook that runs your checks and keeps Claude working while they fail. The mechanics are under *Beyond the source*.
9. **Feed failures back.** When a better second attempt fixes a recurring mistake, have Claude update the relevant skill or CLAUDE.md so it doesn't happen again (Nate [08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).

## Starter files & prompts

*Vault starter content, written for this note; none of it is copied from the videos. Replace anything in angle brackets with your project's details.*

### A. CLAUDE.md block: definition of done

```markdown
## Definition of done
A task is finished only when the checks below have run in this session and their output is shown. Don't say "done" without that evidence.

- Code: write or update tests for the new behaviour first and show them failing, then implement. Cover the paths that matter, not every line.
- Before finishing: run `<test command>`, `<type-check command>` and `<lint command>`. All must pass.
- UI: start the app, screenshot each changed screen, compare it with the request or reference, and click through the changed flows. Fix and repeat, up to 3 passes.
- Non-code deliverables: grade against `<path/to/rubric.md>` and report pass/fail per criterion.
- Commit each working state before a risky change so you can roll back.
- If a check can't pass, stop and report which one, why, and what you tried. Never weaken, skip or delete a test to get a pass.
```

### B. Planning prompt: verification to-dos

```text
Before starting, write a to-do list for this task. After every build item, add a check item that says how you'll prove it works: the command, the screenshot, or the browser steps. Don't start the next build item until its check has passed and you've pasted the result.

Task: <describe the task>
```

### C. Tests-first prompt and a goal condition

```text
Step 1: Write tests for <feature> covering <the 2–4 cases that matter>. Run them and show that they fail. No implementation code yet.
Step 2, after I approve the tests: implement until they pass. Don't modify the test files.
```

```text
/goal `<test command>` exits 0 including the new tests, `<type-check command>` reports no errors, and no test file has changed since approval, or stop after 20 turns
```

### D. UI screenshot and browser loop

```text
Start the dev server and open <URL> in the browser.
1. Screenshot <page>. Compare it with <the request or reference screenshot> and list every layout, spacing and content difference.
2. Fix those differences and screenshot again. Up to 3 passes.
3. Walk through <flows, e.g. sign up, submit the contact form, open the mobile menu> and check the browser console for errors.
Finish with the final screenshot, a pass/fail line for each flow, and any console errors.
```

### E. Rubric template for non-code outputs

```markdown
# Rubric: <deliverable>
Pass rule: every Must criterion passes. Should failures are reported but don't block.

## Must
- [ ] <Checkable fact, e.g. "Every figure names its source file or URL">
- [ ] <Checkable fact, e.g. "Summary is under 300 words">
- [ ] <Checkable fact, e.g. "Covers all 5 items in the brief">

## Should
- [ ] <Quality bar, e.g. "Recommendations are ordered by impact">

## Grader instructions
Grade each criterion on its own. Give pass/fail plus one line of evidence: a count, a location, or a short excerpt. Ignore anything outside the criteria.
```

### F. Verifier subagent

Save as `.claude/agents/verifier.md`:

```markdown
---
name: verifier
description: Independent checker for finished work. Use after implementation to confirm a task meets the definition of done in CLAUDE.md or a named rubric. Runs checks and reads files; never edits.
tools: Read, Grep, Glob, Bash
model: sonnet
---
You didn't do this work. Your job is to find out whether it really meets the bar.

1. Read the task, then the definition of done in CLAUDE.md or the rubric you were given.
2. Run every listed check yourself. Don't rely on output already in the conversation.
3. For UI work, list the screenshots or browser steps still needed rather than assuming they passed.
4. Reply with a table: criterion | pass/fail | evidence (command output, file and line, or screenshot).
5. Flag only gaps that affect correctness or the stated requirements. Don't modify any file.
```

Invoke it with: `Use the verifier subagent to check <task> against the definition of done.`

### G. Optional Stop hook that blocks on failing checks

Save as `.claude/hooks/verify-on-stop.sh` and run `chmod +x` on it:

```bash
#!/bin/bash
# Vault starter content. Keeps Claude working while the project's checks fail.
INPUT=$(cat)

# If this hook already forced one continuation, let Claude stop (see Beyond the source).
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

# No changes in the working tree means nothing to verify.
if [ -z "$(git status --porcelain 2>/dev/null)" ]; then
  exit 0
fi

# Replace with your project's fast, deterministic checks.
if ! OUTPUT=$( { <type-check command> && <test command>; } 2>&1 ); then
  echo "Checks are failing. Fix them before finishing:" >&2
  echo "$OUTPUT" | tail -n 40 >&2
  exit 2
fi
exit 0
```

Register it in `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/verify-on-stop.sh" }
        ]
      }
    ]
  }
}
```

### H. Runtime verification prompt (Reticle)

```text
Use Reticle to verify <feature> in the running app. For each criterion, drive the flow, read the runtime evidence and give one verdict: pass, fail or couldn't tell.
- <e.g. Signup creates a user and the response body has no errors>
"Couldn't tell" is not done: name the missing evidence. Fix failures from the reported file and line, then re-run every check.
```

### I. Keyframe and content check for animated pages

```text
1. Screenshot <page> at <6> scroll positions, desktop and 390 px wide, as one contact sheet. Fix anything clipped, overlapping or blank mid-animation; up to 3 passes.
2. Table every caption, stat, testimonial, image and link: item | source | matches <source of truth>? Leave blank if unsure. I sign it off before we ship.
```

### J. SKILL.md verification block

```markdown
## Before returning
1. Write 3–6 checkable acceptance criteria. The first version is a draft.
2. Check it with outside evidence: render slides or pages and inspect them; open the primary source for each claim; for persuasive copy, ask persona subagents and act on issues two or more raise; for code, run <test and lint commands>.
3. Fix and re-check, up to <3> passes.
4. End with "Checked" (criterion → evidence) and "Not verified" (what's left, and why).
```

## Done when

- [ ] CLAUDE.md has a definition-of-done block with your real test, type-check and lint commands.
- [ ] Asking for a small feature produces a to-do list with a check item after each build item.
- [ ] Claude writes failing tests before implementation code and leaves them unchanged afterwards.
- [ ] On a UI change, Claude returns a final screenshot and a pass/fail line for each flow it clicked through.
- [ ] At least one non-code deliverable has a rubric and has been graded by the verifier subagent.
- [ ] Claude's closing summary shows evidence for every check and names anything unfinished.
- [ ] (Optional) With the Stop hook installed, breaking a test and asking Claude to wrap up makes it keep working instead of stopping.
- [ ] (Optional checkers) Reticle gives a verdict per criterion with no "couldn't tell" reported as done, and `oxlint` runs in the definition of done or hook.
- [ ] Repeat-use skills end with Checked and Not verified lists. Animated pages come back with a contact sheet and a signed-off content table.

## Pitfalls

- **Self-grading.** A to-do like "check it looks right" still has Claude marking its own work. Unlazy's objection to AI LABS' earlier loops was that the checks were real but the agent graded them ([04:07](https://www.youtube.com/watch?v=c47uqR7XB_c&t=247s)–[04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)). Ask for pasted output, and use a separate verifier for anything important. For research on models favouring their own output, see [[Verification Before Done]].
- **Confidence isn't evidence.** Nate's 95% gate ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)) is a useful nudge, but a percentage is still a claim. Unlazy treats a ticked box with no proof behind it as unmet ([08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s)).
- **Tests written after the code.** They end up passing whatever Claude wrote (Sloth [09:10](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=550s)).
- **Over-testing.** Strong models tend to test everything and bloat the codebase (Sloth [09:23](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=563s)).
- **A judge that only reads the chat.** /goal's judge works from the conversation, not the work (Unlazy [03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)–[04:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=245s)). Make sure the check's real output lands in the transcript; starter C names the command for that reason.
- **Checks that fade in long sessions.** Completion checks start slipping deep into a session (Unlazy [04:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=254s)), so for long runs move the gate into a hook (starter G) or a gates file.
- **Heavy review for small jobs.** A fan-out review across many dimensions takes a long time and burns tokens (Loops [10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s)); a normal reviewer agent is much cheaper ([11:11](https://www.youtube.com/watch?v=8wsM0euQOvc&t=671s)). The Sloth also rates /goal a tier lower on low-usage plans ([19:22](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1162s)).
- **Chasing a perfect score.** The design video suggests rerunning a scoring skill until the design scores perfectly ([05:09](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=309s)). Reviewers asked to find problems tend to keep finding some (see [[Verification Before Done]]), so stop at your pass rule.
- **A reviewer that can fix things itself.** AI LABS gives its scorer no editing tools ([10:29](https://www.youtube.com/watch?v=8wsM0euQOvc&t=629s)). Starter F still includes Bash; see *Beyond the source* for what that means.
- **Flaky or slow checks.** See *Beyond the source*.
- **Screenshots aren't fact checks.** Nate couldn't tell where Claude had found the leaderboard screenshots on his page ([10:42](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=642s)). Check facts, images and links separately (starter I).
- **Acting on every reviewer.** Taking all persona feedback would probably make the output worse ([07:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=466s)).
- **Trusting narrated automation, or installing unread.** The video says anti-slop runs on every task unasked ([12:04](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=724s)); the repo documents only an install skill, so its rules run when Oxlint does. Both checkers add code to your project, so read them first ([[Build vs Install Third-Party Skills]]).

## Variations

- **Tests as a /goal condition** for unattended runs (Loops [03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)). Build: [[Tests-First Goal Loop]].
- **An evidence ledger checked by a script**, using [[Unlazy]] ([07:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=446s)). Build: [[Evidence-Gated Completion Ledger]].
- **Several critics, or an implementer paired with a scorer**, for whole-app reviews (Loops [08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s), [09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s)). Build: [[Multi-Agent Review and Scoring Loops]].
- **Hosted rubric grading** with [[Claude Managed Agents]] outcomes ([01:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=75s)). Build: [[Build an Event-Triggered Managed Agent]].
- **Design review skills** that score pages, flag regressions against git history and fix layout to the pixel ([09:24](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=564s), [09:59](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=599s)). Build: [[Build a Distinctive Site with Design Skills]].
- **Verifying a skill rather than a task.** Run the same job with and without the skill to measure its real impact (Loops [06:30](https://www.youtube.com/watch?v=8wsM0euQOvc&t=390s)). Build: [[Skill Improvement Loop]].
- **Planning the checks up front.** Build: [[Plan-First Workflow]].
- **Held-out acceptance checks** that the builder never sees (Ouroboros; see [[Verification Before Done]], row 6b).

## Sources

- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]:
  - The case for verification; tests first; type checkers, linters, screenshots and browser tests ([08:31](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=511s)–[09:57](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=597s)).
  - Built-in review skills ([05:27](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=327s)) and a test-based goal ([19:08](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=1148s)).
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]:
  - Verification to-dos and a confidence gate ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s)–[04:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=285s)).
  - A screenshot loop and Chrome DevTools checks ([08:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=539s)–[09:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=587s)).
  - Updating the skill or CLAUDE.md after a correction ([08:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=495s)).
- [[AI LABS - Types of Claude Loops Explained]]:
  - Tests as the /goal standard, plus the rollback line ([02:42](https://www.youtube.com/watch?v=8wsM0euQOvc&t=162s)–[03:46](https://www.youtube.com/watch?v=8wsM0euQOvc&t=226s)).
  - A read-only scorer and when it's worth the cost ([10:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=617s)–[11:17](https://www.youtube.com/watch?v=8wsM0euQOvc&t=677s)).
- [[AI LABS - The Unlazy Skill for Lazy Agents]]:
  - Failure modes and the limits of existing checks ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s)–[04:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=261s)).
  - Rules for evidence and for abandoning a task ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[09:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=545s)).
- [[Anthropic - What Is Claude Managed Agents]]:
  - Measurable criteria and a grader in its own context ([00:54](https://www.youtube.com/watch?v=NLWiIj47IdI&t=54s)–[01:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=89s)).
- [[AI LABS - Claude Design Skills for Beautiful Sites]]:
  - Scoring and review skills, regression checks and layout flags ([05:03](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=303s)–[05:14](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=314s), [09:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=556s)–[10:10](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=610s), [11:45](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=705s)–[12:16](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=736s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]:
  - Runtime verdicts with Reticle ([01:36](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=96s)–[02:45](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=165s)) and anti-slop lint rules ([11:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=695s)–[12:14](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=734s)).
- [[Nate Herk - Build Skills Instead of Agents]]:
  - Verification built into skills, with an acceptance-criteria block ([06:43](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=403s)–[09:00](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=540s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]]:
  - Keyframe verification ([08:37](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=517s)–[09:20](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=560s)) and the content errors it missed ([10:38](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=638s)–[11:31](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=691s)).

## Beyond the source

*Not from the videos. Checked against the linked pages on 2026-09-15. The wider verification ladder, Managed Agents outcome limits and self-grading research are in [[Verification Before Done]].*

- **Claude in Chrome.**
  - **Setup:** install the extension, then start Claude Code with `claude --chrome` or manage the connection with `/chrome`.
  - **Requirements:** a Pro, Max, Team or Enterprise plan signed in with `/login`. API-key auth keeps it off.
  - **What the docs list:** reading console errors and DOM state, testing form validation, checking visual regressions, saving screenshots.
  - **Login pages and CAPTCHAs:** Claude pauses and hands them to you.
  - **Cost:** leaving it on by default loads the browser tools in every session.
  - Source: [Claude Code docs: Chrome](https://code.claude.com/docs/en/chrome)
- **Chrome DevTools MCP, the likeliest match for the "Chrome DevTools" Nate names.** He never says MCP or shows any setup, so he could also mean [[Claude in Chrome]].
  - **Install:** Chrome's guide adds it as a plugin: `/plugin marketplace add ChromeDevTools/chrome-devtools-mcp`, then `/plugin install chrome-devtools-mcp@chrome-devtools-plugins`. It needs Node.js LTS and current Chrome.
  - **Tools:** screenshots, console messages, network requests, performance traces and input automation.
  - Sources: [Chrome for Developers: Get started](https://developer.chrome.com/docs/devtools/agents/get-started), [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- **Built-in reviewers.** Anthropic's best-practices page points to:
  - the bundled `/code-review` skill, which reviews the current diff in a fresh subagent;
  - `/verify`, for checking a change against the running app.
  - Source: [Claude Code docs: Best practices](https://code.claude.com/docs/en/best-practices)
- **Writing the /goal condition in starter C.**
  - **Why:** the evaluator (Haiku by default) doesn't run commands or read files; it judges only what's in the conversation.
  - **What to include:** a measurable end state, a stated check, constraints such as untouched test files, and a turn limit.
  - Source: [Claude Code docs: /goal](https://code.claude.com/docs/en/goal)
- **Stop hook mechanics behind starter G.**
  - **Blocking:** exit code 2 blocks the stop, and stderr becomes the reason.
  - **The `stop_hook_active` guard:** the docs advise checking it and exiting early to avoid endless continuation. That's why starter G gives Claude one extra attempt per stop; drop the guard for stricter gating.
  - **Block cap:** Claude Code overrides a Stop hook after eight blocks in a row without progress. `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` raises the cap.
  - **Script paths:** the guide's examples reference scripts through `"$CLAUDE_PROJECT_DIR"`, and it suggests that or an absolute path if you hit "command not found".
  - **Alternative:** prompt-based Stop hooks (`"type": "prompt"`) return `ok` and `reason` instead of running a script.
  - Source: [Claude Code docs: Hooks guide](https://code.claude.com/docs/en/hooks-guide)
- **Flaky or slow checks.**
  - **The problem:** a failing check reopens the turn, so a randomly failing test can burn turns without progress.
  - **Built-in brakes:** the eight-block Stop hook cap; /goal handing back control when Claude stops making tool calls for several turns; a turn limit in the condition.
  - **This note's suggestion:** keep gating commands fast and deterministic, and run slow or flaky suites outside the gate.
  - Sources: [Hooks guide](https://code.claude.com/docs/en/hooks-guide), [/goal](https://code.claude.com/docs/en/goal)
- **Restricting the verifier's tools.**
  - **Frontmatter:** `tools` is an allowlist, `disallowedTools` a denylist and `model` picks the model. Project subagents live in `.claude/agents/`.
  - **This note's caveat:** Bash can still change files. For a strictly read-only judge, drop Bash and feed it the check output, or add permission deny rules.
  - Source: [Claude Code docs: Subagents](https://code.claude.com/docs/en/sub-agents)
- **Rubric writing.**
  - **Criteria:** write explicit, gradeable criteria; vague ones make grading noisy.
  - **No rubric yet?** Have Claude analyse a known-good example and turn that analysis into criteria.
  - Source: [Claude Platform docs: Define outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)
- **Reticle (starter H).**
  - **What it is:** a dev-only SDK plus MCP server for apps you own. It reads network calls, state, console and DOM. For sites you don't ship, the README points to Playwright.
  - **Setup:** `npx @reticlehq/server init`. New checks start when you ask or type `/reticle`.
  - **Not only on request:** remembered flows re-run after each change, every run is kept, and an in-app HUD exists (a closed bug report covers it intercepting clicks). That broadly backs the pop-up and check history in [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] ([02:37](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=157s)).
  - **Verdicts:** pass, fail or "couldn't tell", with file and line on failures.
  - **Licences:** SDK Apache-2.0; server, CLI and MCP FSL-1.1-ALv2.
  - Sources: [reticlehq/reticle](https://github.com/reticlehq/reticle), [reticle.sh](https://www.reticle.sh/), [issue #783](https://github.com/reticlehq/reticle/issues/783)
- **anti-slop (step 3).**
  - **What it is:** an Oxlint JS plugin, meant to be vendored, with generic JS/TS rules plus optional Effect rules. Oxlint's JS plugins are in alpha.
  - **Install:** `npx skills add dmmulroy/anti-slop --skill install-anti-slop`, or copy its `src/` into your project and register it under `jsPlugins` in `oxlint.config.ts`. Then run `oxlint`.
  - **No per-task run:** the only bundled skill installs it.
  - Sources: [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop), [Oxlint JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins.html)

## Related

- **Concepts:** [[Verification Before Done]], [[Agent Laziness]], [[Loop Engineering]], [[Plan Before Executing]], [[Subagents and Agent Teams]], [[Context Window Management]], [[Escaping the Default AI Design Look]]
- **Techniques:** [[Evidence-Gated Completion Ledger]], [[Tests-First Goal Loop]], [[Multi-Agent Review and Scoring Loops]], [[Plan-First Workflow]], [[Keep CLAUDE.md Lean]], [[Build a Distinctive Site with Design Skills]], [[Configure Safe Autonomy Permissions]], [[Build a Scroll-Driven Landing Page]]
- **Tools:** [[Claude Code]], [[Claude in Chrome]], [[Unlazy]], [[Claude Managed Agents]], [[Claude Design]], [[Scrollcraft]]
- [[Home]]
