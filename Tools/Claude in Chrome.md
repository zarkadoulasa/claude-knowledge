---
type: tool
category: Anthropic browser extension (Claude browses and acts in Chrome)
website: https://claude.com/claude-in-chrome
sources: ["[[Simon Pittman - Set Up Claude Cowork]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]"]
tags: [topic/cowork, topic/claude-code, topic/verification, topic/permissions, topic/automation]
---

# Claude in Chrome

## What it is

Claude in Chrome is Anthropic's browser extension that lets Claude work inside web pages for you. [[Simon Pittman]] installs it so [[Claude Cowork]] can browse the web. [[Nate Herk]]'s browser-check tips describe the same kind of job for [[Claude Code]], though he names a different tool (see below). Current official details are under *Beyond the source*.

## How sources use it

### [[Simon Pittman - Set Up Claude Cowork]]

It comes in his connectors step, where Notion, Slack and other tools are already connected ([20:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1242s)). He covers Claude in Chrome first, before setting up Gmail ([21:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=1261s)).

- **What it does, per Simon.** It's an extension that lets Claude visit sites, read pages, pull information, fill in forms and click through multi-step workflows ([21:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1271s), [21:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1275s)). Instead of pasting URLs into chat, you just tell it to go read the page ([21:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=1279s)). He thinks it's worth installing right away if you're comfortable with it ([21:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=1268s)).
- **Setup as shown.**
  1. In Cowork's Connectors, find Claude in Chrome and enable it ([21:28](https://www.youtube.com/watch?v=pl90LATQlHI&t=1288s)).
  2. Install the Chrome extension. You can ask Claude for the link ([21:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=1290s), [21:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1295s)). His request says he's demoing the setup and asks Claude to walk through it or give him the link ([21:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=1299s)).
  3. Open the link and click install ([21:56](https://www.youtube.com/watch?v=pl90LATQlHI&t=1316s), [22:00](https://www.youtube.com/watch?v=pl90LATQlHI&t=1320s)).
  4. Heed the warning. At the time it was a beta with risks, so using it is your call ([22:07](https://www.youtube.com/watch?v=pl90LATQlHI&t=1327s), [22:09](https://www.youtube.com/watch?v=pl90LATQlHI&t=1329s)).
- **Demo.** He asks it to find a popular Reddit thread about Claude in Chrome ([22:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=1337s)). A permission prompt lets him allow the action for this time only ([22:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=1359s)), and then it navigates ([22:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1362s)). Groups of tabs from its earlier work are still there, and deleting a group closes them if you don't need them ([22:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=1371s), [22:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=1375s)). In one of them it had been researching sites whose design he liked, for a website plan ([23:00](https://www.youtube.com/watch?v=pl90LATQlHI&t=1380s)).
- **It's optional.** If you don't want to give Claude browser access, skip it. Everything else in his setup works without it ([23:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1391s), [23:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1395s)).
- **The riskier setting.** A post-filming update shows a setting that lets Claude act in Chrome without asking, even on sites you haven't approved ([44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s), [44:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=2677s)). He says to turn it on only if you're okay with that ([44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s)). See [[Permissions and Approval Gates]].

### [[Nate Herk - 32 Tricks to Level Up Claude Code]]

Nate says "Chrome DevTools", not Claude in Chrome, and shows no setup (see Notes). Claude Code's own Chrome integration supports the same kinds of checks (see *Beyond the source*).

- **Hack 10: add verification to-dos.** After a build to-do such as "build the website", add one to screenshot the result and check it looks right ([03:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=238s), [04:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=251s)). Then add another to open the browser and confirm nothing is functionally broken ([04:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=255s)). That way Claude checks its own work before handing it back for feedback ([04:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=264s)). He also tells Claude not to move to the next to-do until it's 95% confident the current one is right ([04:31](https://www.youtube.com/watch?v=jqoFP9QapXI&t=271s)). See [[Build Verification into Every Task]].
- **Screenshot passes.** On websites he has Claude design, take a screenshot and revise, about three times before he sees V1 ([09:21](https://www.youtube.com/watch?v=jqoFP9QapXI&t=561s), [09:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=564s)).
- **Hack 21: functional checks.** Claude opens a browser, uses the app and checks that it works ([09:33](https://www.youtube.com/watch?v=jqoFP9QapXI&t=573s), [09:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=577s)). It's like the screenshot loop, but for buttons and features. He calls it huge for front-end work ([09:46](https://www.youtube.com/watch?v=jqoFP9QapXI&t=586s)).
- **Jobs with no API.** The same browser control can fill in forms and work on sites that have no API ([09:48](https://www.youtube.com/watch?v=jqoFP9QapXI&t=588s), [09:53](https://www.youtube.com/watch?v=jqoFP9QapXI&t=593s)). It works best when you're already signed in and it only has to navigate, click and fill ([09:59](https://www.youtube.com/watch?v=jqoFP9QapXI&t=599s)).

## Notes

- **Which tool Nate means is unclear.** He shows no install, so "Chrome DevTools" most likely means Google's Chrome DevTools MCP server, a separate product from Claude in Chrome. It could also be loose wording for Claude in Chrome *(unclear in captions)*.
- **CAPTCHAs.** Nate speculates that browser control might get past CAPTCHAs ([09:58](https://www.youtube.com/watch?v=jqoFP9QapXI&t=598s)). Don't plan around that: Anthropic's guidance prohibits it (see below).
- **Simon's "beta" label is dated.** The video was published on 2026-04-10, and the extension has since reached general availability (see below).
- **Caption fix.** "Claude Chrome" → Claude in Chrome.

## Beyond the source

*Not from the videos. Checked 2026-09-15 at the linked pages.*

- **Availability.**
  - The extension lets Claude read, click and navigate websites, and works with the Claude desktop app, Claude Cowork and Claude Code.
  - It's included in every paid plan (Pro, Max, Team, Enterprise). The Help Center says it runs only in Google Chrome, not other Chromium browsers or mobile.
  - On Team and Enterprise plans, admins can restrict which sites it can use.

  <https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome>
- **General availability.**
  - Anthropic announced general availability on every paid plan on 2026-08-26.
  - Claude can now act on its own instead of asking approval for every action.
  - A safety classifier checks each action before it runs, using the same mechanism as auto mode in Claude Code.

  <https://claude.com/blog/claude-in-chrome-generally-available>
- **Permission modes and safety.**
  - **Modes.** "Automatically approve" is the default: Claude screens its own actions and pauses when something needs your approval. "Manually approve" asks you to review every action.
  - **Named risks.** Prompt injection hidden in web content is the main one. Claude's screenshots also capture anything visible in the tab.
  - **Blocked and prohibited.** Some site categories are blocked, and financial sites require permission. Bypassing CAPTCHAs and entering sensitive data are prohibited uses.
  - **Advice.** Start with trusted sites and use a separate browser profile that isn't signed in to sensitive accounts.

  <https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely>
- **Cowork no longer needs the extension to browse.**
  - Since 2026-08-26, Cowork has its own built-in browser. There's nothing to install, and Claude doesn't see your own tabs, bookmarks or passwords; you can bring logins in site by site if you choose.
  - It's rolling out to Pro, Max and Team in the desktop app (macOS; Windows and Linux in beta).
  - If you already use Claude in Chrome, it stays your default.
  - Simon's install step is therefore optional for Cowork today. Install the extension when you want Claude working inside your own signed-in Chrome.

  <https://claude.com/blog/cowork-built-in-browser>
- **Side panel is now Cowork.** Since 2026-08-12, the extension's side panel runs as Cowork, and sessions are saved so you can continue them in the desktop, web or mobile apps. It launched on Max and Team, with Pro rolling out. <https://claude.com/blog/cowork-chrome-side-panel>
- **Using it for Nate-style checks in Claude Code.**
  - **Turn it on.** Launch with `claude --chrome`, or run `/chrome` and choose "Enabled by default".
  - **Requirements.** Extension version 1.0.36 or later, a direct Anthropic plan and a `/login` sign-in. API-key authentication keeps the integration off.
  - **What it can do.** Read console errors and DOM state, check a built UI against a design, test form validation and user flows, and record GIFs.
  - **How it behaves.** It shares your browser's login state and pauses at login pages or CAPTCHAs so you can handle them.
  - **Context cost.** Enabling it by default loads the browser tools into every session and raises context use.
  - **Browser support.** These docs list Chrome and Edge and say other Chromium browsers (Brave, Arc and others) are detected, which is broader than the Help Center's Chrome-only statement. Check against your own setup.

  <https://code.claude.com/docs/en/chrome>
- **The tool Nate probably meant.** Chrome DevTools MCP is Google's MCP server that lets a coding agent control and inspect a live Chrome browser. It's added as an MCP server that runs `npx -y chrome-devtools-mcp@latest`. <https://github.com/ChromeDevTools/chrome-devtools-mcp>

## Related

- **Concepts:** [[Verification Before Done]], [[Permissions and Approval Gates]], [[Connecting Claude to External Tools]]
- **Techniques:** [[Set Up Claude Cowork]], [[Build Verification into Every Task]], [[Configure Safe Autonomy Permissions]]
- **Tools:** [[Claude Cowork]], [[Claude Code]]
- **People:** [[Simon Pittman]], [[Nate Herk]]
- **Sources:** [[Simon Pittman - Set Up Claude Cowork]], [[Nate Herk - 32 Tricks to Level Up Claude Code]]
- [[Home]]
