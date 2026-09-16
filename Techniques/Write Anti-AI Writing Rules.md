---
type: technique
goal: "Build a writing-rules.md from Wikipedia's catalogue of AI-writing tells, rewritten as your own rules with a do-this-instead for each. Make Claude read it before writing anything you'll send or publish, and tighten it from your own edits."
difficulty: beginner
time_to_build: "About 30 minutes for a first version, then a minute or two per correction (estimate, not from the video)"
sources: ["[[Simon Pittman - Set Up Claude Cowork]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]"]
tools: ["[[Claude Cowork]]", "[[Claude Code]]", "[[Claude in Chrome]]"]
tags: [topic/prompting, topic/context, topic/cowork, topic/skills]
---

# Write Anti-AI Writing Rules

## Goal

Keep one short file that tells Claude which habits make text read as machine-written, and what to write instead. Drafts in your name then need less rewriting. Claude builds the first version from a public catalogue of those habits, and your own corrections keep it honest.

## What the video shows

In [[Simon Pittman - Set Up Claude Cowork]], writing in his voice is one of the things Cowork now does for him ([00:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=12s)). This file is part of how:

- **Its job.** It's one of three About Me files. It shapes how Claude writes and steers it away from an AI style ([13:10](https://www.youtube.com/watch?v=pl90LATQlHI&t=790s)).
- **How he built it.** Inside his About Me build prompt, he asks Claude to:
  - find Wikipedia's page on AI writing style and research it
  - break it down into a detailed list of what to avoid, so the writing doesn't sound like AI

  ([14:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=873s), [14:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=879s), [14:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=887s)). During the build, Claude works through the page's list of signs ([17:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=1033s)).
- **What came out.** Detailed rules, including banned phrases and a rule against superficial commentary ([18:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1083s)). There were 14 rules in all ([18:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1095s)). The full list isn't shown.
- **How it's used.** The global instructions list it as something to read at the start of every session ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s), [15:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=916s), [18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)).
- **How it improves.**
  - He doesn't refine the writing rules on camera.
  - His general habit is to correct Claude once, then ask it to update its memory or instructions so the change sticks ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s), [26:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1598s)).
  - Applying that habit to the rules file is this note's extension.

## Use when

- Claude drafts emails, posts, documents or replies that go out under your name.
- You keep deleting the same openers, closers, filler or formatting from Claude's drafts.
- A team wants one shared house style for writing done with AI.

**Not the fix when:**

- **You need Claude to sound like a particular person.** Rules only say what to avoid. Add a voice sample and notes to `about-me.md` as well.
- **You want to judge whether someone else used AI.** The source page itself warns that these are signs, not proof (*Beyond the source*).

## Prerequisites

- **Claude can read a web page.** That can be through web search or fetch, or [[Claude in Chrome]], which Simon installs at [21:28](https://www.youtube.com/watch?v=pl90LATQlHI&t=1288s). Otherwise, paste the page text in.
- **A workspace with context files and editable instructions.** For example, the one from [[Set Up Claude Cowork]].
- **5–10 recent drafts you edited by hand.** Your own rules come from these.

## Steps

1. **Collect your evidence.** Pull 5–10 drafts where you changed Claude's wording, and note what you cut or rewrote.
2. **Point Claude at the catalogue.** Ask it to read Wikipedia's "Signs of AI writing" page, as Simon did ([14:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=879s)). The link is under *Beyond the source*.
3. **Have it write rules, not a copy of the page.** Use the build prompt below. It asks Claude to:
   - group rules by category, in plain words
   - give each rule a do-this-instead and a before/after example
   - not paste text from the page

   Simon only asked for a broken-down list of things to avoid ([14:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=887s)); the do-this-instead structure is this note's.
4. **Add your own rules.** Take them from step 1 and mark them `(mine)`. Add a short Voice section for spelling, tone and sentence length. Simon's global brief sets British spelling and a warm but direct tone ([10:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=611s)), and preferences like those belong here.
5. **Cut hard.** Keep the rules that actually change your drafts. Drop rules about wiki markup or citations unless you write those. Simon's file ended at 14 rules ([18:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1095s)); aim for 10–25.
6. **Save it and wire it in.** Save it as `about-me/writing-rules.md` and reference it from your global instructions ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)). The starter block below loads it only when Claude is writing. That differs from Simon, who has it read every session.
7. **Test before and after.** Ask for the same two drafts (an email and a short post) with and without the rules. Run the checker prompt on both versions.
8. **Refine from your corrections.** Each time you edit a draft, paste in your version and ask for one new or tightened rule. This is Simon's correct-then-keep habit ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)) applied to writing.
9. **Prune monthly.** Merge duplicates, drop rules that never come up, and re-check the page for new categories.

## Starter files & prompts

*Vault starter content written for this note. The categories below paraphrase the kinds of signs the Wikipedia page groups together; nothing is copied from the page.*

### Build prompt

```text
Read Wikipedia's "Signs of AI writing" page:
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
Then write about-me/writing-rules.md using the skeleton I'll paste below.

Rules for the rules:
- Use your own words. Don't paste sentences or long word lists from the page.
- Only include signs that matter for <emails, LinkedIn posts, client documents>.
  Skip wiki markup and citation signs.
- Every rule gets: what to avoid, what to do instead, and a one-line before → after example.
- Maximum 20 rules. Put the 5 that will change my drafts most at the top.
- Add a Banned phrases list of up to 15 items, drawn from the page's patterns and from these
  drafts I edited: <paste>.
Ask me about my voice (spelling, tone, sentence length) before you finish.
```

### writing-rules.md skeleton

```markdown
# Writing rules
_Last updated: yyyy-mm-dd · Applies to: anything I'll send, post or publish_
_Why these exist: readers stop trusting text that sounds machine-made. When a rule and clarity
conflict, choose clarity._

## Voice (do this)
Write in <British/American> spelling with a <warm, direct> tone. Keep most sentences short,
one idea each. Open with the point and stop when it's made. Prefer names, numbers, dates and
examples to big claims.

## Top 5 (check these every time)
1. …
2. …

## Content
- **Inflated importance.** Avoid: calling ordinary things historic or groundbreaking.
  Instead: say what happened and why it matters to this reader.
  Before → after: …
- **Vague authority.** Avoid: "experts say", "many believe". Instead: name the source or drop it.
- **Brochure tone.** Avoid: stacks of flattering adjectives. Instead: plain description.
- **Tidy moral at the end.** Avoid: a closing paragraph that sums up the lesson.
  Instead: stop, or give the next step.

## Language
- **Stock vocabulary.** Avoid the words in Banned phrases. Instead: the everyday word.
- **Dodging "is".** Avoid: "serves as", "functions as". Instead: "is".
- **"Not just X, but Y".** Avoid by default. Instead: state Y.
- **Reflex triplets.** Avoid: lists of three for rhythm. Instead: as many items as are real.
- **Signpost openers.** Avoid: starting paragraphs with "Moreover" and friends. Instead: just start.

## Formatting
- **Headings and bullets where prose works.** Emails and short posts are paragraphs.
- **Bold everywhere.** At most one bold phrase per message.
- **Markdown where it won't render.** Plain text for email and chat.

## Talking to the reader
- **Assistant chatter.** No "Great question", "I hope this helps", or offers of more help.
- **Leftovers.** No knowledge-cutoff disclaimers, no unfilled [Name] placeholders.

## Banned phrases
- <phrase> → <use instead>

## My rules (from my edits)
- (mine, yyyy-mm-dd) …
```

### Instruction block

```markdown
## Writing
- Before drafting anything I will send, post or publish, read `about-me/writing-rules.md`.
- After drafting, check the draft against the Top 5 and Banned phrases and fix it before showing me.
- The rules exist because readers switch off when text sounds machine-made. If a rule would make
  the text less clear, choose clarity and tell me.
```

### Refinement prompt

```text
Here's your draft and my edited version:
<your draft>
---
<my version>
Name the pattern I removed or changed. If a rule already covers it, tighten that rule.
Otherwise add one under "My rules" with today's date, a do-this-instead and a before → after line.
Add at most one rule. Show me the change before saving.
```

### Checker prompt

```text
Review this draft against about-me/writing-rules.md. List each rule it breaks, quoting the exact
words, then give a revised draft. Don't change facts, names or numbers.
<draft>
```

## Done when

- [ ] `about-me/writing-rules.md` exists in your own words, with Voice, Top 5, the categories, Banned phrases and My rules
- [ ] Every rule has a do-this-instead
- [ ] There are 25 rules or fewer
- [ ] Your instructions tell Claude to read the file before writing and to check the draft afterwards
- [ ] A before/after test shows fewer broken rules with the file than without it
- [ ] At least one dated rule comes from your own edit
- [ ] A date for the next prune is set

## Pitfalls

- **Signs, not proof.** The source page is advice, and it warns that human writers show these patterns too (*Beyond the source*). Use the rules to improve your own drafts, not to accuse anyone.
- **A list of don'ts steers badly.** Anthropic's prompting guide says to tell Claude what to do rather than what not to do, and to explain why a rule matters (*Beyond the source*). That's why every rule here has a do-this-instead and the file opens with a reason.
- **Replacement tells.** Ban one stock phrase and a new one takes its place. The correction loop and the monthly prune deal with this.
- **Heavy formatting in the rules file.** The same guide notes that a prompt's formatting can pull the response's formatting toward it (*Beyond the source*). A file full of bullets and bold may give you emails full of bullets. That's why the skeleton writes Voice as prose; test whether your own file has this effect.
- **Always-loaded length.**
  - Simon's reading list loads the file every session ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)).
  - [[Ras Mic - How AI Agents and Claude Skills Work]] notes that always-loaded text is carried on every turn ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)), and that quality slips as context fills ([31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)).
  - He'd keep only what the model wouldn't know or do on its own ([32:48](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1968s)).
  - So keep the file short, or load it only when Claude is writing. See [[Keep CLAUDE.md Lean]] and [[Context Window Management]].
- **Copying the page.** Pasting Wikipedia's text or long word lists makes the file long, and it isn't really yours. The build prompt asks for your own words.
- **Rules that don't apply to you.** Much of the page covers wiki markup and citations. Leave those out unless you write that way.
- **No example to copy.** Simon's 14 rules aren't shown ([18:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1095s)), so there's nothing to borrow. Test your own.
- **Voice gap.** Removing tells doesn't add your voice. Pair the file with `about-me.md` and a short sample of your own writing.

## Variations

- **As a skill.** Package the rules as a writing skill whose description triggers on drafting emails or posts, so they load only when Claude writes. This is Ras Mic's argument for loading procedures on demand rather than keeping them always loaded ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s), [05:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=346s)). Build it from a real editing session first, as he recommends ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)). See [[Build a Skill from a Successful Run]] and [[Agent Skills]].
- **Checker pass as a second step.** Draft first, then run the checker prompt in a fresh task. See [[Verification Before Done]].
- **Per-channel files.** Use `writing-rules-email.md` and `writing-rules-linkedin.md`, both sharing one Voice section.
- **Team style guide.** Put the shared file in a shared folder or plugin, and keep personal rules in each person's About Me folder.
- **Claude Code.** Reference the file from CLAUDE.md for docs and release notes, or turn it into a project skill.
- **Design equivalent.** The same idea for visual work is in [[Escaping the Default AI Design Look]].

## Where the sources meet

- **Simon: always-needed context.** In [[Simon Pittman - Set Up Claude Cowork]], writing rules are something Claude always needs ([13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)).
- **Ras Mic: only what's specific to you.** In [[Ras Mic - How AI Agents and Claude Skills Work]], always-loaded context is for things specific to you that every turn needs ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)). The model should get what's unique to you, not general knowledge ([32:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1933s)).
- **This note's reading:**
  - Your voice and your own banned phrases count as specific to you.
  - A long generic catalogue doesn't.
  - So keep the personal part always available, and keep the catalogue short or load it on demand.

## Beyond the source

*Not from either video. Checked 2026-09-15 at the linked pages.*

- **Wikipedia: Signs of AI writing.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
  - **Status.** An advice page from WikiProject AI Cleanup. It says it isn't a Wikipedia policy, because the community hasn't reviewed it.
  - **What it covers.** It groups signs into content, language and grammar, style, communication meant for the user, markup, citations, comment-specific signs, edit summaries, and miscellaneous. Separate sections cover signs of human writing, indicators that don't work, and historical indicators.
  - **Its caveats.** These are signs rather than proof, and people write this way too. Neither detector tools nor human judgement reliably tell AI text from human text.
- **Anthropic's prompting guidance.** [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
  - "Control the format of responses" recommends saying what to do instead of what not to do. It also suggests matching your prompt's style to the output you want; for example, less markdown in the prompt tends to mean less in the reply.
  - "Add context to improve performance" recommends explaining why an instruction matters.

## Sources

- [[Simon Pittman - Set Up Claude Cowork]]: the writing-rules file ([13:10](https://www.youtube.com/watch?v=pl90LATQlHI&t=790s), [14:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=873s)–[14:52](https://www.youtube.com/watch?v=pl90LATQlHI&t=892s), [17:13](https://www.youtube.com/watch?v=pl90LATQlHI&t=1033s)–[18:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1095s)) and the correction habit ([26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s)–[26:40](https://www.youtube.com/watch?v=pl90LATQlHI&t=1600s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: what always-loaded context costs, what belongs in context, and skills ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)–[05:57](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=357s), [31:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1864s)–[32:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1974s)).

## Related

- **Techniques:** [[Set Up Claude Cowork]] · [[Build a Skill from a Successful Run]] · [[Skill Improvement Loop]] · [[Keep CLAUDE.md Lean]] · [[Build a Level 1 Second Brain]]
- **Concepts:** [[Agent Skills]] · [[Context Window Management]] · [[Verification Before Done]] · [[Agent Memory Patterns]] · [[Escaping the Default AI Design Look]]
- **Tools:** [[Claude Cowork]] · [[Claude in Chrome]] · [[Claude Code]]
- **People:** [[Simon Pittman]] · [[Ras Mic]]
- [[Home]]
