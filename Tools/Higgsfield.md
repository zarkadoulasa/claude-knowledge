---
type: tool
category: Paid AI image and video platform (many models under one subscription, with an MCP server, CLI and app plugins)
website: https://higgsfield.ai
sources: ["[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Chase AI - GPT-6 Astra Motion Design in After Effects]]", "[[AI LABS - Design Skills from Landing Pages to Mobile Apps]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]", "[[Jason Lee - Vibe Coding an Animated App with Fable 5.1]]", "[[Nick Saraev - Animated Sites with Claude Code and Kling]]"]
tags: [topic/media, topic/mcp, topic/marketing, topic/design]
---

# Higgsfield

## What it is

A paid platform that puts many third-party image and video models under one subscription. [[Nate Herk - Claude as a One-Person Marketing Team]] names Seedance 2.5, Kling, Sora, GPT Image 2 and Nano Banana among them ([02:13](https://www.youtube.com/watch?v=yCACmFTiCto&t=133s)). It also has a Marketing Studio that turns your assets into ads or sizzle reels ([02:46](https://www.youtube.com/watch?v=yCACmFTiCto&t=166s)). In these workflows Claude writes the prompts and Higgsfield generates the media. See [[Generating Images and Video with Claude]].

## How sources use it

- [[Nate Herk - Claude as a One-Person Marketing Team]] connects it to Claude as a claude.ai custom connector. Copy the Claude URL from Higgsfield's "MCP and CLI" page, add it under Customize > Connectors, then sign in ([16:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=992s), [16:53](https://www.youtube.com/watch?v=yCACmFTiCto&t=1013s)).
  - 18 ad creatives cost $3.43 and a sizzle reel about $17.55 ([27:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=1656s), [29:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1746s)).
  - He admits it isn't the cheapest way to reach these models ([27:48](https://www.youtube.com/watch?v=yCACmFTiCto&t=1668s)).
- [[Chase AI - GPT-6 Astra Motion Design in After Effects]] uses its Motion Designer plugin from Codex. The plugin connects the model to After Effects, comes with bundled skills, and works through scripts and computer use ([01:27](https://www.youtube.com/watch?v=C8dWdic-oK4&t=87s)).
  - For storyboard images in Claude Code, he says you'd add the Higgsfield MCP ([03:01](https://www.youtube.com/watch?v=C8dWdic-oK4&t=181s)).
  - He calls the plugin free, credit-free and open source ([00:23](https://www.youtube.com/watch?v=C8dWdic-oK4&t=23s)). Higgsfield's pages don't back that (see below).
- [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] uses it to put real visuals on sites instead of stock photos, and picks Seedance for video ([10:47](https://www.youtube.com/watch?v=Ot582-E61ac&t=647s), [11:05](https://www.youtube.com/watch?v=Ot582-E61ac&t=665s)).
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] offers it as one of the providers you can switch between in his design OS ([13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s)).
- [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] mentions it only as a comparison ([09:38](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=578s)).
- [[Jason Lee - Vibe Coding an Animated App with Fable 5.1]] adds it to Claude Code as an MCP connector and lets Claude drive it — GPT Image 2.5 for stills and Seedance 2.5 to animate a character and moving backdrop — and it also generated his app icon ([02:50](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=170s), [23:21](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=1401s)). Higgsfield is his video's sponsor, so the new pay-as-you-go pricing, the "30–50% cheaper than Fal AI" claim and the "$15 free credits" promo are promotional ([03:20](https://www.youtube.com/watch?v=29Vto7o2I2Q&t=200s)).
- [[Nick Saraev - Animated Sites with Claude Code and Kling]] uses it to reach Kling 3.0 for video, seeded by Nano Banana Pro stills; on the ~$29–30 Pro plan (600 credits) a 5-second clip works out to about $0.36 ([03:44](https://www.youtube.com/watch?v=ZfYvv-0l9NA&t=224s)). The link in his description is an affiliate link, so read his "pretty affordable" framing with that in mind.

## Notes

- Nate's and Chase's video descriptions carry Higgsfield referral links. Jack's uses a shortened link. Jason Lee's video is Higgsfield-sponsored, and Nick Saraev's carries an affiliate link — treat all their pricing and discount claims as promotional.
- Jack's panel shows the price before you generate ([16:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=1011s)). Nate only asks for the cost afterwards ([22:35](https://www.youtube.com/watch?v=yCACmFTiCto&t=1355s)). No source sets a spending cap. See [[Permissions and Approval Gates]].

## Beyond the source

*Checked 2026-09-15.*

- **Connecting.** The MCP URL is `https://mcp.higgsfield.ai/mcp`. It works with Claude, ChatGPT, Cursor and other MCP clients, and needs an active subscription but no API key. Claude Code can use the CLI instead (`npm i -g @higgsfield/cli`). [Help center](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent)
- **Credits.** Every generation run through an agent deducts credits, whatever your plan. Unlimited and free generations apply only on higgsfield.ai. [External integrations](https://higgsfield.ai/creator-hub/help-center/integrations/external-integrations-higgsfield)
- **Motion Designer.** In ChatGPT you invoke it with `@Higgsfield /use-after-effects`; Claude can reach it through the MCP. It needs active Higgsfield, GPT and After Effects subscriptions, and Higgsfield generations use credits. Neither page calls it open source. [AI Motion Designer](https://higgsfield.ai/ai-motion-designer), [blog](https://higgsfield.ai/blog/ai-motion-designer-after-effects-gpt)

## Related

- [[Generating Images and Video with Claude]] · [[Connecting Claude to External Tools]] · [[Build a Brand-Aware Marketing Project]] · [[Storyboard-First AI Video and Motion Graphics]] · [[Vibe-Code an Animated Mobile App with Claude]] · [[Build an Animated Marketing Site with Claude Code and Kling]] · [[Nate Herk]] · [[Chase AI]] · [[AI LABS]] · [[Jack Roberts]] · [[Jason Lee]] · [[Nick Saraev]] · [[Home]]
