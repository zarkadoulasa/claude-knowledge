---
type: technique
goal: "Make each skill in a library load for the requests it should handle and stay out of the rest: one job per skill, descriptions in the words you actually type, no two skills competing, trigger tests with obvious, reworded and negative requests, and a re-check after every model update"
difficulty: beginner
time_to_build: "About 45 minutes for a library of 10–20 skills, then about 10 minutes per skill after each model update (vault estimate)"
sources: ["[[Nate Herk - Build Skills Instead of Agents]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[Nate Herk - The Scrollcraft Website Design Skill]]"]
tools: ["[[Claude Code]]"]
tags: [topic/skills, topic/claude-code, topic/context, topic/verification, topic/models]
---

# Audit Skill Descriptions and Triggers

> **Provenance.** Timestamped points come from [[Nate Herk - Build Skills Instead of Agents]] (his second practice), two [[AI LABS]] videos and one Scrollcraft point. Nate speaks his audit prompt and tests aloud and shows no files. The prompts, test table, description pattern and `trigger_check.sh` are **vault starter content**. The script follows the documented output format but hasn't been run against real sessions. Claude Code mechanics are under **Beyond the source**. Background: [[Agent Skills]].

## Goal

A skill library where Claude picks the right skill without being asked:

- each skill does one job;
- each description says what the skill does and when to use it, in your own words;
- no two skills compete for the same request;
- every skill Claude may invoke passes trigger tests in fresh sessions;
- skills are re-checked after each model update.

## Use when

- **Claude loads the wrong skill, or none.** A skill Claude can't find is, in effect, one you don't have ([04:46](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=286s)).
- **Your library has grown, or mixes your own skills with plugins.** Vague, overlapping descriptions leave Claude guessing ([03:54](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=234s)).
- **A new model has shipped.** [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] warns it may already do what a skill says, so the skill only adds token cost ([09:40](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=580s)). In [[AI LABS - Design Skills from Landing Pages to Mobile Apps]], they rework Anthropic's frontend-design prompt after the Opus 4.8 and Fable 5 prompting guides came out ([02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s)).

**Skip** skills set to `disable-model-invocation: true`. Their descriptions aren't in context (Beyond the source).

## What Nate's practice asks for

| Rule | What he says | Timestamp |
|---|---|---|
| Descriptions select | Claude starts with names and descriptions, and reads the full SKILL.md only on a match | [03:29](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=209s) |
| What and when | Name the output, the inputs and the requests that should load it | [04:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=245s) |
| One job, your words | No two skills competing for one request | [04:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=257s) |
| Let Claude audit | Report what each skill does, when it triggers and where it overlaps; rewrite only ambiguous ones | [04:25](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=265s) |
| Test three ways | Obvious, reworded, and unrelated (must not trigger) | [04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s) |

People read descriptions too. Typing "scroll" shows Nate's Scrollcraft skill with its summary ([[Nate Herk - The Scrollcraft Website Design Skill]] [03:03](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=183s)).

## Where sources and docs pull apart

- **Negatives.** Nate tests an unrelated request ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)). skill-creator says obvious negatives test nothing and wants near-misses instead (Beyond the source). *Vault:* test both.
- **Precise or pushy.** Nate wants sharp, non-overlapping descriptions. skill-creator says Claude undertriggers, so descriptions should be a little pushy. *Vault:* be pushy only about the skill's own phrases, and add a "Not for" line.
- **Cost or value.** `/skill-doctor` can't show whether a skill helps ([10:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=601s)), so AI LABS point to Caliper, which compares runs with and without it ([10:15](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=615s)). *Vault:* the numbers flag candidates; with/without runs decide.

## Prerequisites

- [[Claude Code]] with personal, project or plugin skills. `/skill-doctor` needs v2.1.252 or later.
- The project in git, so description edits are reviewable diffs.
- For the script: `jq`, a normal terminal, and usage budget for two short headless runs per test row.

## Steps

1. **Take an inventory.** Run `/skills` for the list and `/skill-doctor` for cost, usage and skills never invoked. Note which skills come from plugins.
2. **Audit without editing.** Prompt 1 is Nate's audit ([04:25](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=265s)) plus a list of collision pairs.
3. **Resolve collisions before rewording.**
   - Merge two skills that do one job.
   - Split a skill that does two ([04:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=257s)).
   - Or draw a boundary between them.

   If a plugin duplicates one of your skills, turn off your copy with `skillOverrides`, or the plugin with `/plugin`.
4. **Rewrite only the flagged descriptions** with Prompt 2. Put the key use case first, because the listing truncates long descriptions (Beyond the source).
5. **Fill in the test table.** Write Nate's obvious, reworded and unrelated rows ([04:36](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=276s)), then add a near-miss. Phrase them the way you really ask.
6. **Run each row twice, each time in a fresh session.** Use `/clear` or a new terminal, or run `trigger_check.sh`.
7. **Fix and retest.**
   - It doesn't trigger: add your real phrases, earlier in the description.
   - It fires on the near-miss: narrow the "when", add "Not for", or use `paths`.
   - Two skills fire: edit both descriptions, then rerun both skills' rows.
   - A skill with side effects fires on its own: set `disable-model-invocation: true`.
8. **Check the skill did its job.** For skills with scripts, run the same task twice and confirm the saved file gets called ([02:42](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=162s)).
9. **After each model update, repeat steps 5–7, then compare suspect skills with and without.**
   - Use Phase 4 of [[Skill Improvement Loop]], or Caliper, which the AI LABS repos video says reports whether a skill's gain is worth its tokens ([11:25](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=685s)).
   - Shrink or retire skills that don't beat the baseline.
10. **Commit** the descriptions and `skill-triggers.md`, noting the model and date.

## Starter files & prompts

*Vault starter content, not from the videos.*

### Prompt 1: audit (read-only)

```text
Read the frontmatter of every skill in this session (personal, project, plugin).
Don't edit anything. Return a table: skill · source · what it does · when it should
trigger (phrases a user would type) · overlaps with · verdict (clear / ambiguous /
two jobs / never used). Then list every pair of skills that could claim the same
request, with one example prompt each. Flag descriptions in first or second person,
ones that never say when to use the skill, and ones that bury the key use case.
```

### Prompt 2: rewrite flagged descriptions

```text
Rewrite only descriptions marked ambiguous or two jobs. Third person. Sentence one:
what it produces, from what input. Sentence two: "Use when" plus 3–5 phrases I
actually use. Where there was an overlap, add "Not for …" naming the other skill.
Show old and new side by side and wait for my approval.
```

### Description pattern

```yaml
description: Turns a sales-call transcript into a client follow-up email listing decisions, owners and dates. Use when the user asks for a recap email, a follow-up, or to send the client the notes. Not for internal meeting minutes (use meeting-notes).
```

### `skill-triggers.md`

| Skill | Row | Prompt (fresh session) | Expect | Run 1 | Run 2 |
|---|---|---|---|---|---|
| client-followup | Obvious | Write the follow-up email to Dana from today's call; transcript is calls/0914.md | loads | | |
| client-followup | Reworded | can u send acme the notes + next steps from this morning | loads | | |
| client-followup | Near-miss | Turn calls/0914.md into internal minutes for the wiki | meeting-notes instead | | |
| client-followup | Unrelated | Rename the files in exports/ by date | nothing | | |

### `trigger_check.sh` (optional)

```bash
#!/usr/bin/env bash
# One trigger test in a fresh headless session: did Claude call the Skill tool for <skill>?
# Run from a normal terminal in the project folder, not from inside Claude Code.
# Usage: trigger_check.sh <skill-name> "<prompt>" <yes|no>
set -uo pipefail
skill=$1; prompt=$2; expect=$3

calls=$(claude -p "$prompt" \
    --output-format stream-json --verbose \
    --permission-mode dontAsk --allowedTools "Skill,Read,Glob,Grep" \
    --max-turns 3 --no-session-persistence < /dev/null |
  jq -c 'select(.type == "assistant") | .message.content[]?
         | select(.type == "tool_use" and .name == "Skill") | .input')

if grep -q -- "$skill" <<< "$calls"; then got=yes; else got=no; fi
[ "$got" = "$expect" ] && result=PASS || result=FAIL
printf '%s | %s | expected %s, got %s | %s\n' "$result" "$skill" "$expect" "$got" "$prompt"
[ "$result" = PASS ]
```

Try it first on a row you know should trigger, and check the result by hand.

## Done when

- [ ] Every skill has a verdict, and every collision pair has a decision: merge, split, boundary or switch off.
- [ ] Every description Claude sees is in the third person, says what and when, and leads with the key use case.
- [ ] Each skill Claude may invoke passes its obvious, reworded, near-miss and unrelated rows twice, each run in a fresh session.
- [ ] No test prompt loads two skills.
- [ ] Skills flagged as never used were tested, then fixed, set to manual or retired.
- [ ] After the latest model update, suspect skills had a with/without comparison, and the result is recorded.
- [ ] `skill-triggers.md` is committed with the model name and date.

## Pitfalls

- **Warm sessions.** A skill loaded earlier in the session skews later results, so use a fresh session for each row.
- **Prompts that are too easy.** Claude may skip a skill for a one-step task it can handle alone (Beyond the source). Use realistic requests.
- **Tests copied from the description.** They always pass. Keep a few real phrasings back until after rewriting.
- **Pushy everywhere.** It recreates the overlap Nate warns about ([03:54](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=234s)).
- **Pruning on numbers alone.** Cost and usage don't show value, as the AI LABS repos video notes ([10:01](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=601s)).
- **Editing an installed plugin's skill in place.** *Vault caution:* disable it in `/plugin` and write your own skill instead.
- **Hidden skills.** `disable-model-invocation`, `user-invocable-only` or `off` overrides, and unmatched `paths` make automatic-trigger rows fail by design; `name-only` weakens them.
- **Script gotchas.**
  - A nested-session guard has been reported to block `claude -p` launched from Claude Code's Bash tool (see [[Skill Improvement Loop]]).
  - `grep` matches substrings, so `notes` also matches `meeting-notes`.

## Variations

- **skill-creator tuning** for your most important skills (Beyond the source).
- **Delegation.** In the AI LABS design-skills video, their marketing-UI skill names the GSAP skill for animation ([09:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=561s)).
- **A registry.** In the AI LABS repos video, UI Skills pulls in only what a job needs ([05:46](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=346s)). See [[Build vs Install Third-Party Skills]].
- **A second harness.** Run important skills in another agent to expose hidden assumptions ([06:34](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=394s)).

## Sources

- [[Nate Herk - Build Skills Instead of Agents]]: scripts ([01:26](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=86s)–[02:54](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=174s)); descriptions and tests ([03:17](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=197s)–[04:48](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=288s)).
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: stale skills and Caliper ([09:34](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=574s)–[11:35](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=695s)).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: updating an official skill ([02:12](https://www.youtube.com/watch?v=Ot582-E61ac&t=132s)–[02:46](https://www.youtube.com/watch?v=Ot582-E61ac&t=166s)).
- [[Nate Herk - The Scrollcraft Website Design Skill]]: the slash menu ([03:03](https://www.youtube.com/watch?v=QUI6Ug4cHnE&t=183s)).

## Beyond the source

*Checked 2026-09-15.*

- **Claude Code's skill listing.**
  - **What loads.** Listed descriptions are in context every turn. `description` plus `when_to_use` is cut at 1,536 characters, and SKILL.md edits apply mid-session.
  - **Diagnostics.** `/skill-doctor` (v2.1.252+) shows each skill's cost and usage, and flags skills never invoked.
  - **What Claude sees.** `skillOverrides` accepts `on`, `name-only`, `user-invocable-only` or `off`, and doesn't apply to plugin skills (use `/plugin`). `disable-model-invocation` keeps a description out of context, and `paths` limits automatic loading.
  - **Name clashes.** Same-name plugin and local skills both load, and the plugin's is namespaced.

  Source: [Claude Code docs: Skills](https://code.claude.com/docs/en/skills).
- **Descriptions.** Write in the third person, and say what the skill does and when to use it: Claude may be choosing among 100+ skills. Test with each model you'll use. Source: [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- **skill-creator tuning.**
  - **Queries.** About 20, half of them near-miss negatives, each run three times.
  - **Selection.** A 60/40 train/test split, keeping the description that scores best on the test set.
  - **Advice.** Be slightly pushy. Simple one-step queries may not trigger a skill at all.

  Source: [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md).
- **Script flags.** `stream-json` is paired with `--verbose`, and `dontAsk` denies anything that would prompt. Source: [headless docs](https://code.claude.com/docs/en/headless).
- **Caliper.** An eval harness for Claude Code, Codex, Pi and Hermes. `--ablate <skill-name>` reruns tasks without that skill, and results report pass@k, tokens and time. Source: [edonadei/caliper](https://github.com/edonadei/caliper).

## Related

- Concepts: [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Context Window Management]] · [[Choosing a Claude Model]] · [[Verification Before Done]]
- Techniques: [[Skill Improvement Loop]] · [[Build a Skill from a Successful Run]] · [[Workflow Audit into Skills]] · [[Build a Reference-Rich Skill]]
- Tools and people: [[Claude Code]] · [[Scrollcraft]] · [[Nate Herk]] · [[AI LABS]]
- [[Home]]
