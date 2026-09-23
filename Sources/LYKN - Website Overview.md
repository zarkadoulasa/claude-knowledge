---
type: source
title: "LYKN: AI Anywhere You Need (website)"
creator: "Omnia Technologies LLC"
channel: "lykn.io (product website)"
url: https://lykn.io/
published: 2026-08-26
ingested: 2026-09-23
topics: [desktop AI assistant, cross-tool memory, MCP, screen context, usage-based pricing, workflow templates]
tags: [source/website, topic/memory, topic/portability, topic/mcp, topic/agentic-os, topic/privacy]
---

# LYKN - Website Overview

> **Maker:** Omnia Technologies LLC (Utah) · **Terms effective:** 2026-08-26 · **Format:** product website, read 2026-09-23 · [lykn.io](https://lykn.io/)

**A light ingest, on purpose.** This is a commercial product site, not a tutorial, so it's captured as inspiration for tools we build, not as guidance on how to use Claude. Links go to the page each point comes from. The site renders with JavaScript, so it was read in a real browser, and every page was read on 2026-09-23. The published date above is the terms' effective date, the only date on the site.

## TL;DR

[[LYKN]] is a Mac app ("Glass", opened with ⌘L) that puts an AI chat bar on your desktop and keeps your files and screen one shortcut away. It resells several model providers under one usage-based subscription.

The part that matters for this vault: it offers a personal **memory and vault** that any AI tool can connect to over MCP, OAuth or REST. It pitches itself as a single context layer shared by ChatGPT, Claude and Cursor ([terms](https://lykn.io/terms)). That's a commercial take on [[Tool-Agnostic Context Files]].

The user reports that LYKN plans to open-source the product. The site doesn't say so; see Caveats.

## Key takeaways

- **One memory layer, many AI tools.** You connect external AI tools to your LYKN account and pass them your saved notes, links and files. Access can be revoked per tool, immediately ([terms](https://lykn.io/terms)).
- **Your desktop is the context.** Glass syncs your Desktop folder and Finder files, and can use what's on screen through snips, page text and an optional "live watch", so questions start with context already loaded ([home](https://lykn.io/); [terms](https://lykn.io/terms)).
- **Local access is opt-in and approval-gated.** "Local Mode" (files, apps, terminal) is off by default, limited to the folders you sync, and asks before any write or command that could change your Mac ([terms](https://lykn.io/terms)). This matches [[Permissions and Approval Gates]].
- **Capture only when a feature needs it.** Screen and microphone input is processed when a feature asks for it, not continuously. The exception is live watch, and it runs only while you leave it on ([terms](https://lykn.io/terms)).
- **Workflows ship as scheduled templates.** Roughly 80 ready-made workflows across seven role groups, many with a default schedule such as "weekdays 9am" or "every Monday". Examples: a standup digest from yesterday's commits, a PR summary from a diff, a daily source digest ([templates](https://lykn.io/templates)). See [[Routines and Scheduled Tasks]].
- **The subscription is paid out as usage.** Each plan converts into a monthly usage allowance across all models and tools, and heavy compute (images, video, agent runs) draws on a prepaid balance ([pricing](https://lykn.io/pricing); [terms](https://lykn.io/terms)).

## Notes by page

### Home ([lykn.io](https://lykn.io/))

The Mac app's modules:

- **Home:** wallpaper, widgets and a central chat bar.
- **Sync with Mac:** your Desktop folder, Finder files and wallpaper.
- **Chat**, with context preloaded.
- **Build:** a sentence into working software.
- **Imagine:** on-brand images and ads.
- **Voice:** real-time and hands-free.
- **Research:** a structured report.
- **Browser:** an agent that acts on the web.
- **Glass:** the ⌘L overlay.

### Pricing ([lykn.io/pricing](https://lykn.io/pricing))

- **Plans:** Student $15, Pro $20, Pro+ $60 and Max $200 per month, billed monthly.
- **Pro includes:** $20 of monthly usage, LYKN Memory, custom agents and personalisation, all models, tools and connections, plus desktop, browser and Glass.

### Developers ([lykn.io/developers](https://lykn.io/developers))

A single-key API covering text, code, voice, images, video, 3D, audio and "world models". It's listed as coming soon, opening in stages, with a waitlist.

### Terms ([lykn.io/terms](https://lykn.io/terms))

- **Operator:** Omnia Technologies LLC, under Utah law.
- **Providers:** content goes to OpenAI, Anthropic, Google, xAI and ElevenLabs, depending on the feature and model. No training on user content, and no cross-user datasets.
- **Connected tools:** once data leaves LYKN for a connected tool (ChatGPT, Claude, Cursor…), that tool's terms apply. The same goes the other way for accounts you connect in, such as Google, Slack or Notion.
- **Account rules:** one person per account, with any number of connected tools. You can export your data at any time.
- **New accounts:** a one-time $10 usage grant with no card needed.
- **Liability:** capped at 12 months of fees or $100, whichever is greater.

### Templates ([lykn.io/templates](https://lykn.io/templates))

- **Groups:** Students, Creatives, Sales, Marketing, Business, Research and Development, with 12 each.
- **How they work:** each template names the input (snip, paste, point Glass at a page), which module does the work (Chat, Build, Voice, Research), and often a default schedule.

## Caveats & disagreements

- **Open-sourcing is unconfirmed.** The user says LYKN will soon be open-sourced. On 2026-09-23 the site had no mention of open source, no public repo and no licence beyond the proprietary desktop licence in the terms. Recheck before relying on it.
- **Pricing pages disagree.** The terms list Student $15, Pro $20 and **Max $100** with no Pro+. The pricing page lists Pro+ $60 and **Max $200**. The terms were probably written before the plans changed.
- **Marketing claims only.** There's no changelog, version history, user count or independent review. The `/apps/claude` path in the sitemap returns a 404.
- **Privacy surface.** Screen stills, file contents, command output and voice are sent to several third-party model providers.

## Build from this

These are ideas to borrow for our own tools. They're the vault's suggestions, not from the site:

- **One memory, exposed over MCP.** Put a personal vault (like this knowledge bank) behind a small MCP server so Claude, Codex and Cursor all read the same notes. Extends [[Port a Claude Code Brain to Other Agents]].
- **Per-tool, revocable access.** Give each connected agent its own token and scope, instead of one shared key.
- **Scheduled templates as a product surface.** Ship workflows as named templates with a default cadence, which is how [[Schedule Recurring Claude Tasks]] would look as a menu.
- **Capture on demand, not always on.** Take screen or microphone context only when a feature asks for it, and make any continuous mode obviously on and easy to turn off.

## Resources mentioned

- Site: <https://lykn.io/> · pricing, developers (API waitlist), templates, terms, privacy, DPA
- Contact: hello@lykn.io

## Beyond the source

- **The MCP standard.** The Model Context Protocol is the open standard LYKN uses for connections; Claude supports it as connectors. <https://modelcontextprotocol.io/>

## Transcript notes

- "Glass" is both the Mac app's name ("LYKN Glass") and its ⌘L overlay.
- The site's JavaScript-free shell shows only the title, so plain HTTP fetchers see nothing. Read it in a real browser.

## Related

- **Concepts:** [[Tool-Agnostic Context Files]] · [[Agent Memory Patterns]] · [[Context vs Connections]] · [[Permissions and Approval Gates]] · [[Routines and Scheduled Tasks]] · [[Connecting Claude to External Tools]]
- **Techniques:** [[Port a Claude Code Brain to Other Agents]] · [[Schedule Recurring Claude Tasks]]
- **Tools:** [[LYKN]] · [[Claude Cowork]] · [[Claude in Chrome]]
