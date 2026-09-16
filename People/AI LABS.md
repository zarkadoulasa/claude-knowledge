---
type: person
role: "YouTube channel — AI LABS, a self-described software company publishing Claude Code, skills and agent-loop tutorials"
links: ["https://www.youtube.com/channel/UCelfWQr9sXVMTvBzviPGlFw", "https://ailabspro.io/"]
sources: ["[[AI LABS - Types of Claude Loops Explained]]", "[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[AI LABS - Claude Design Skills for Beautiful Sites]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tags: [topic/loops, topic/verification, topic/subagents, topic/skills, topic/design, topic/claude-code, topic/mcp, topic/media]
---

# AI LABS

## Who

- **A channel with no named presenter.**
- **Self-description:** a software company that tests these setups in its own coding work ([00:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=16s)).

## In this vault

- [[AI LABS - Types of Claude Loops Explained]] — creator.
- [[AI LABS - The Unlazy Skill for Lazy Agents]] — creator; reviews [[Leon Lin]]'s [[Unlazy]].
- [[AI LABS - Claude Design Skills for Beautiful Sites]] — creator.
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] — creator (June 2026). Sorts design skills by job: art direction, component registries, generated design systems, motion, style presets, media and mobile. Mostly description, with one demo.
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] — creator (September 2026). Eight free community repos, each covering a gap in Claude Code or Codex. Several narrated claims differ from the repos' own docs; see the source note.

## Recurring themes

- **Pick the right loop type.** Loops waste tokens only when the type doesn't fit the job ([00:12](https://www.youtube.com/watch?v=8wsM0euQOvc&t=12s)). → [[Loop Engineering]]
- **Use hard checks.** Write tests first, then set /goal to passing them ([03:16](https://www.youtube.com/watch?v=8wsM0euQOvc&t=196s)). → [[Tests-First Goal Loop]]
- **Split review across agents.** → [[Multi-Agent Review and Scoring Loops]]
  - Four critic agents ([08:03](https://www.youtube.com/watch?v=8wsM0euQOvc&t=483s)), or an implementer paired with a reviewer that scores its work against a set metric ([09:27](https://www.youtube.com/watch?v=8wsM0euQOvc&t=567s)).
  - The fan-out review is costly ([10:53](https://www.youtube.com/watch?v=8wsM0euQOvc&t=653s)).
- **Agents get lazy.** → [[Agent Laziness]], [[Evidence-Gated Completion Ledger]]
  - They claim false completion ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s)) or quietly drop the hard part ([03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s)).
  - Instructions get lost in long sessions, so requirements go into a gates file ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)).
- **Run subagents in parallel.** → [[Subagents and Agent Teams]]
  - Serial dispatch gave only a login page after 3–4 hours ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s)).
  - Ten agents in parallel built the app in about two hours ([12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s)).
- **Escape the default look.** → [[Escaping the Default AI Design Look]], [[Build a Distinctive Site with Design Skills]]
  - Every model has a recognisable design pattern ([00:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=18s)).
  - Skills made by experienced designers steer the model away from it ([00:32](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=32s)). Some also score an existing design so you can keep refining it ([05:01](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=301s)).
- **Match the skill to the surface.** → [[Design Systems for Claude]], [[Build Product UI from a Component Registry]], [[shadcn]]
  - Anthropic's frontend-design skill makes the model commit to a design direction before writing code ([01:18](https://www.youtube.com/watch?v=Ot582-E61ac&t=78s)). It doesn't work well for functional UI ([02:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=167s)).
  - Their own marketing skill uses a modified copy, updated because the original got outdated for newer models ([02:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=152s)).
  - UI UX Pro Max runs a search engine first, so the model starts from a design system chosen for its industry ([05:32](https://www.youtube.com/watch?v=Ot582-E61ac&t=332s)).
  - Pick one style preset rather than stacking them ([10:15](https://www.youtube.com/watch?v=Ot582-E61ac&t=615s)). Phones need their own skills, because mobile isn't a smaller web ([11:25](https://www.youtube.com/watch?v=Ot582-E61ac&t=685s)).
- **Check the finished app, not the builder's word.** → [[Verification Before Done]], [[Evidence-Gated Completion Ledger]]
  - Reticle runs the app once the agent says it's finished ([01:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=115s)) and gives three verdicts: worked, failed, or not enough information to tell ([02:22](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=142s)).
  - Ouroboros never tells the builder how its checks run or what results they expect ([07:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=475s)).
- **Test whether a skill still helps.** /skill-doctor shows a skill's token cost and whether it's used, but not whether it improves the work ([09:53](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=593s)). Caliper compares runs with and without the skill ([10:15](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=615s)). → [[Skill Improvement Loop]], [[Audit Skill Descriptions and Triggers]]

## The channel revises itself

- **Loops video:** presents /goal as the clearest stateless loop ([01:50](https://www.youtube.com/watch?v=8wsM0euQOvc&t=110s)).
- **Unlazy video, about six weeks later:**
  - /goal judges the conversation, not the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)).
  - Its own earlier loops let the agent grade itself ([04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s)).
- **Skills vs MCP.**
  - June: pair the shadcn skill with its MCP, because the skill loads only when needed while MCP sits in context all the time ([04:43](https://www.youtube.com/watch?v=Ot582-E61ac&t=283s)).
  - September: they pick UI Skills' MCP over its CLI because MCP tools stay available in the session ([05:17](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=317s)), while a CLI must be named in the prompt or project instructions ([05:21](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=321s)).
  - Only June's context-cost argument is dated (see *Beyond the source*). *Vault reading:* September's reason is discoverability, which deferred tool loading doesn't undo.

## Paywalled assets pattern

- **What's paywalled:** its paid community holds the loop resources (per the video description), the refined Unlazy skill ([12:28](https://www.youtube.com/watch?v=c47uqR7XB_c&t=748s)) and its own design skills ([12:18](https://www.youtube.com/watch?v=Ysr7oNDajJI&t=738s)).
- **Effect on the vault:** Technique notes rebuild these setups from the narration.
- **Sponsors:** segments unrelated to Claude are left out.

## Beyond the source

- **AI Labs Pro** (checked 2026-09-15): a paid monthly membership, listed at £15 a month, with weekly implementation guides, resource kits and starter templates. — [ailabspro.io](https://ailabspro.io/)
- **Unlazy now:** its README describes rolling dispatch of tasks as soon as they're ready. — [GitHub](https://github.com/Leonxlnx/unlazy)
- **MCP tools are deferred by default** (checked 2026-09-15). Claude Code finds MCP tools through tool search instead of keeping every definition in context; setting `ENABLE_TOOL_SEARCH=false` turns this off. So the June context-cost argument for skills is weak. A better reason for the pairing is division of labour: the skill carries rules, the MCP gives live registry access. — [Claude Code docs: MCP](https://code.claude.com/docs/en/mcp)

## Related

- [[Home]]
- [[Claude Design]]
- [[shadcn]]
- [[Higgsfield]]
- [[Leon Lin]]
