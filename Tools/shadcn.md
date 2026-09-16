---
type: tool
category: UI component registry and CLI
website: https://ui.shadcn.com
sources: ["[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]"]
tags: [topic/design, topic/skills, topic/mcp, topic/claude-code]
---

# shadcn

## What it is

shadcn/ui is a set of accessible React components delivered by a CLI and registry. The source lands in your project for you to own and edit, instead of arriving as a package (Beyond the source). Around it are an official agent skill, an MCP server for registry access, and other skills from its creator, such as improve.

## How sources use it

- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]]: their answer for functional UI.
  - Common dashboard components already exist at professional quality, so the model pulls them from the registry instead of generating them [03:21](https://www.youtube.com/watch?v=Ot582-E61ac&t=201s).
  - **Skill:** a rulebook for shadcn's way of building that also reads your project setup [04:04](https://www.youtube.com/watch?v=Ot582-E61ac&t=244s).
  - **MCP:** a live registry connection for browsing and pulling components [04:28](https://www.youtube.com/watch?v=Ot582-E61ac&t=268s).
  - **Why both:** the two parts work together [04:01](https://www.youtube.com/watch?v=Ot582-E61ac&t=241s); the skill's rules, patterns and project context give the agent the judgement to use components correctly [04:49](https://www.youtube.com/watch?v=Ot582-E61ac&t=289s). Their other reason, MCP always in context [04:43](https://www.youtube.com/watch?v=Ot582-E61ac&t=283s), is dated (Notes).
  - They call Material 3 the mobile counterpart of shadcn [12:16](https://www.youtube.com/watch?v=Ot582-E61ac&t=736s).
- [[The Coding Sloth - 1000 Hours of Claude Code Lessons]]: shadcn's improve skill, which audits a codebase and writes plans for other agents to carry out [06:42](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=402s).

## Notes

- **Two different skills.** The shadcn/ui skill (component rules, AI LABS) and shadcn/improve (audit and planning, Coding Sloth) do different jobs.
- **Context cost changed.** Claude Code now defers MCP tool definitions by default (Beyond the source), so the reason to pair skill and MCP is division of labour, not tokens.
- **Playbook:** [[Build Product UI from a Component Registry]].

## Beyond the source

*Checked 2026-09-15.*

- **What it is:** React and Tailwind components copied into your project as source, not a packaged library. https://ui.shadcn.com/docs
- **Setup:** `pnpm dlx shadcn@latest init` creates `components.json`; `npx shadcn@latest add <component>` adds parts. https://ui.shadcn.com/docs/components-json
- **Skill:** `pnpm dlx skills add shadcn/ui`. It reads `components.json`, runs `shadcn info --json`, and has the agent search registries before hand-building. https://ui.shadcn.com/docs/skills
- **MCP:** `pnpm dlx shadcn@latest mcp init --client claude` writes `.mcp.json` running `npx shadcn@latest mcp`. It covers public, private and third-party registries. https://ui.shadcn.com/docs/mcp
- **improve:** `npx skills add shadcn/improve`. `/improve execute <plan>` hands a plan to a cheaper model. MIT. https://github.com/shadcn/improve
- **Tool search:** on by default in Claude Code, so MCP tool definitions load on demand; `ENABLE_TOOL_SEARCH=false` turns it off. https://code.claude.com/docs/en/mcp

## Related

- **Techniques:** [[Build Product UI from a Component Registry]] · [[Plan-First Workflow]] · [[Build a Distinctive Site with Design Skills]]
- **Concepts:** [[Design Systems for Claude]] · [[Connecting Claude to External Tools]] · [[Plan Before Executing]]
- **People:** [[AI LABS]] · [[The Coding Sloth]]
