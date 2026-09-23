---
type: tool
category: Commercial multi-model desktop AI assistant (Mac) with a cross-tool memory vault reachable over MCP, OAuth and REST
website: https://lykn.io/
sources: ["[[LYKN - Website Overview]]"]
tags: [topic/memory, topic/portability, topic/mcp, topic/agentic-os]
---

# LYKN

## What it is

LYKN, by Omnia Technologies LLC, is a paid Mac app called "Glass", opened with ⌘L. It combines several things ([home](https://lykn.io/); [terms](https://lykn.io/terms)):

- chat, a builder, image generation, voice, research and a browser agent,
- your Desktop and Finder files synced in,
- screen context from snips, page text and an optional live watch,
- an opt-in, approval-gated Local Mode with file and terminal access.

Models come from OpenAI, Anthropic, Google, xAI and ElevenLabs.

Its **LYKN Memory** vault can be connected to other AI tools over MCP, OAuth or a REST API, so ChatGPT, Claude and Cursor can share one personal context ([terms](https://lykn.io/terms)).

| Fact | Value (checked 2026-09-23) |
|---|---|
| Platform | Mac app (the sitemap also lists a Windows page) |
| Pricing | Student $15 · Pro $20 · Pro+ $60 · Max $200 per month on the pricing page. The terms list different Max pricing; see the Source note |
| Free start | One-time $10 usage grant, no card needed |
| API | One key for all models: "coming soon", with a waitlist |
| Open source | Not yet. The user reports it's planned; the site doesn't say so |

## How sources use it

- [[LYKN - Website Overview]]: a light ingest of the product site, kept as design inspiration for a cross-tool memory layer, scheduled templates and on-demand screen context.

## Ideas worth borrowing

These are the vault's reading, for tools we build:

1. **Memory as a service to other agents.** The vault lives in one place and every agent connects to it, instead of each agent keeping its own. See [[Tool-Agnostic Context Files]].
2. **Scoped, revocable connections.** Each connected tool gets its own access, which you can revoke instantly.
3. **Templates with a default cadence.** Workflows are named by what goes in (snip, paste, point at a page), which module does the work, and when they run.
4. **Permission defaults.** Local access starts off, is limited to synced folders, and asks before writing. Capture happens per feature, not continuously.

## Notes

- **Overlap with Claude's own products:** the desktop app, [[Claude Cowork]], [[Claude in Chrome]], research and scheduled tasks. The distinctive part is the memory shared across different vendors' tools.
- **Watch for the open-source release** before building on it. Revisit this note then; check the repo licence and whether the memory server can be self-hosted.

## Related

- [[Tool-Agnostic Context Files]] · [[Agent Memory Patterns]] · [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[Routines and Scheduled Tasks]]
