---
type: tool
category: "Agentic work mode in the Claude apps (Anthropic)"
website: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
sources: ["[[Simon Pittman - Set Up Claude Cowork]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Jay E - Claude and GPT-Image-2 for On-Brand Design]]"]
tags: [topic/cowork, topic/agents, topic/context, topic/memory, topic/mcp, topic/skills, topic/permissions, topic/scheduling, topic/privacy, topic/automation]
---

# Claude Cowork

## What it is

Claude Cowork is the part of the Claude apps where you give Claude a piece of work rather than a question. In Simon's demo it sets itself a task list and works through it ([06:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=403s)), using files and connected tools.

In [[Simon Pittman - Set Up Claude Cowork]], Cowork is a tab in the desktop app next to Chat and Code ([03:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=206s)). It's meant for work done inside folders on your computer ([03:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=217s)). He calls it a wrapper built on the Claude Code base ([03:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=222s)). Anthropic's own description, a shared agentic architecture rather than a model, is under *Beyond the source*.

To build a setup step by step, see [[Set Up Claude Cowork]].

## How sources use it

### [[Simon Pittman - Set Up Claude Cowork]]

The whole video sets up Cowork on a Mac, and almost all of it is demoed live on his own account.

| Feature | What he shows | Where |
|---|---|---|
| Workspace folder | Give Cowork one dedicated folder. Claude can only work there, so keep anything private outside ([04:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=255s), [04:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=259s)). He then grants Desktop access for a demo, breaking his own rule ([05:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=319s)) | [03:48](https://www.youtube.com/watch?v=pl90LATQlHI&t=228s) |
| Model and thinking | Turn extended thinking on. Start with Sonnet and move to Opus for ambitious work, which costs more tokens ([04:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=282s), [04:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=297s)) | [04:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=275s) |
| Progress panel | Shows Claude's own task list, the instruction files it read and the tools it used ([07:02](https://www.youtube.com/watch?v=pl90LATQlHI&t=422s)) | [06:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=399s) |
| Deletion prompts | Cowork asks before deleting. You can ask what it means instead of approving ([07:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=444s)) | [05:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=353s) |
| Global instructions | The general settings apply across Chat, Cowork and Code ([08:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=514s)). He keeps a Cowork-only set under Settings › Cowork › Global instructions › Edit ([08:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=525s)). Claude reads them at the start of every conversation, so they work like a CLAUDE.md ([08:51](https://www.youtube.com/watch?v=pl90LATQlHI&t=531s), [09:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=541s)) | [08:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=492s) |
| Folder rules | Extra CLAUDE.md files in any folder, or trigger-phrase rules ([12:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=728s), [12:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=731s)) | [12:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=726s) |
| Context files | An About Me folder holding about-me, writing-rules and memory files, which the instructions tell Claude to read ([12:58](https://www.youtube.com/watch?v=pl90LATQlHI&t=778s), [13:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=830s)) | [12:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=755s) |
| Connectors | Customize › Connectors. Browse the directory and add the tools you use ([23:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1417s)). Gmail allows one account ([24:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1455s)). Notion shows per-tool options to allow, require approval or block ([24:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=1470s), [24:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1477s)). Notion connects through an MCP server ([28:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1717s)) | [20:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1238s) |
| Context map | A file describing his Notion workspace, after which Claude found the right database on the first try ([29:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=1775s), [30:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1833s)) | [29:23](https://www.youtube.com/watch?v=pl90LATQlHI&t=1763s) |
| [[Claude in Chrome]] | Turn it on in Connectors and install the extension. It browses, reads pages, fills forms and clicks through multi-step flows. It's a beta with risks, and optional ([21:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1271s), [22:07](https://www.youtube.com/watch?v=pl90LATQlHI&t=1327s), [23:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1395s)) | [21:03](https://www.youtube.com/watch?v=pl90LATQlHI&t=1263s) |
| Skills | Built-in skills make documents, spreadsheets, slides and PDFs. Under Customize › Skills › + you can create, write or upload a skill ([32:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1961s)). He recommends turning on skill-creator ([32:59](https://www.youtube.com/watch?v=pl90LATQlHI&t=1979s)) | [32:11](https://www.youtube.com/watch?v=pl90LATQlHI&t=1931s) |
| Plugins | Customize › Personal plugins › Add plugin › Browse. Install Anthropic's plugins, then use Customize to fit them to your business ([38:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2302s), [39:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=2384s)). His framing: skills are tools, plugins are specialists ([40:45](https://www.youtube.com/watch?v=pl90LATQlHI&t=2445s)) | [38:08](https://www.youtube.com/watch?v=pl90LATQlHI&t=2288s) |
| Scheduled tasks | Tasks run on a timer using your instructions, connectors and context ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)). His examples are a weekly briefing and a weekday inbox triage ([42:01](https://www.youtube.com/watch?v=pl90LATQlHI&t=2521s), [42:34](https://www.youtube.com/watch?v=pl90LATQlHI&t=2554s)). The form has a keep-awake option ([43:22](https://www.youtube.com/watch?v=pl90LATQlHI&t=2602s)) | [41:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2487s) |
| Dispatch | Control the desktop app from your phone ([44:12](https://www.youtube.com/watch?v=pl90LATQlHI&t=2652s)). In the demo he asks for today's calendar, the desktop does the work and replies ([45:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=2714s)) | [43:55](https://www.youtube.com/watch?v=pl90LATQlHI&t=2635s) |
| Computer use | Give permission to operate the computer, with a list of apps Claude may not use ([44:50](https://www.youtube.com/watch?v=pl90LATQlHI&t=2690s), [44:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=2693s)) | [44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s) |
| Privacy | If you're cautious, turn off the "Help improve Claude" setting under Settings › Privacy ([27:10](https://www.youtube.com/watch?v=pl90LATQlHI&t=1630s)) | [27:06](https://www.youtube.com/watch?v=pl90LATQlHI&t=1626s) |

**His answer to "should AI touch my stuff?"**
- Cowork writes email drafts rather than sending, and his global instructions forbid sending without checking ([26:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1609s), [26:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1613s)).
- When he corrects Claude, he asks it to update its memory or instructions so the change sticks ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s)).

**Settings he flags as your call.** One option lets Claude act in Chrome without asking, even on sites you haven't approved. Only turn it on if you accept that ([44:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2675s), [44:39](https://www.youtube.com/watch?v=pl90LATQlHI&t=2679s)).

**Always-on desktop.**
- He says scheduled tasks need the computer on and online ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)).
- He's moving to an always-on studio Mac for Dispatch ([44:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=2658s)).
- With Dispatch he likens Cowork to an [[OpenClaw]]-style assistant you can reach while out ([45:27](https://www.youtube.com/watch?v=pl90LATQlHI&t=2727s)).

### [[Ras Mic - How AI Agents and Claude Skills Work]]

- **One mention.** Cowork comes up once, as evidence for a bigger point. Products like Cowork and [[OpenClaw]] work under the hood by writing code that calls APIs ([19:23](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1163s), [19:26](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1166s)). He uses this to argue that in software projects the code itself is the context ([19:59](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1199s)).
- **Advice that bears on Simon's setup.**
  - Most people don't need an always-loaded instruction file. The exception is information specific to you that every turn needs ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s), [03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
  - Procedures should live in skills, which load only when relevant ([03:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=208s)).
  - [[Set Up Claude Cowork]] weighs this against Simon's always-read context files.

### [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]

- **One mention.** Touring the desktop app's tabs, he says Chat explains, while Cowork can also do things for you, such as organising files or using the browser as a person would ([05:01](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=301s)). He builds in Code instead ([05:11](https://www.youtube.com/watch?v=uuP3lDlKfCI&t=311s)).

## Notes

- **Dated or imprecise claims** (checked 2026-09-15):
  - **Computer must be on for scheduled tasks** ([41:47](https://www.youtube.com/watch?v=pl90LATQlHI&t=2507s)). Per current docs this applies only to tasks that need local files or apps (*Beyond the source*).
  - **Plan advice.** He says signing up for an account is free but recommends Pro ([02:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=163s)); he doesn't say whether Cowork itself works on Free. It doesn't: Cowork needs a paid plan (*Beyond the source*).
  - **Wrapper on the Claude Code base model** ([03:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=222s)). Anthropic says it shares Claude Code's architecture (*Beyond the source*).
  - **Drafts-only email** ([26:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1609s)) comes from his instructions, not from a product lock.
- **Per-tool connector permissions.**
  - Simon shows allow, needs-approval and blocked choices on his own account ([24:30](https://www.youtube.com/watch?v=pl90LATQlHI&t=1470s)).
  - The Help Center documents these as controls set by Team and Enterprise owners.
  - Check what your plan's panel offers.
- **Other unconfirmed or narrower claims.**
  - **One Gmail account** ([24:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=1455s)) isn't confirmed in Anthropic's docs.
  - **The privacy toggle** covers training use and retention. It doesn't stop your data from being processed (*Beyond the source*).
- **Native features he doesn't use.** Cowork now has its own projects, project memory and, in cloud sessions, memory shared with chat (*Beyond the source*). These overlap his hand-made `memory.md` and `projects/` folders.
- **Unversioned models.** He only says "Sonnet" and "Opus". See [[Choosing a Claude Model]].
- **Two meanings of "always-on".** Simon's always-on Mac means a machine kept awake for tasks and Dispatch. That is different from the self-syncing brain in [[Always-On Brain OS]].
- **Caption fixes:**
  - "claw.md" and "Claude MD" → CLAUDE.md
  - "CoWork", "co-worker", "Claude Work" and "Cospace" → Claude Cowork
  - "Claude computer" → computer use
  - "open Claude style assistant" → OpenClaw-style assistant

## Beyond the source

*Not from either video. Each item was checked on 2026-09-15 at the linked page.*

- **What Anthropic says it is.**
  - Cowork uses the same agentic architecture as Claude Code, without the terminal.
  - Cloud sessions (beta) run in isolated environments on Anthropic's servers and keep going when you close your laptop.
  - Local files, the browser and computer use need the desktop app open.
  - Cowork uses more of your usage allowance than chat.
  - Permanently deleting files always needs you to click Allow.
  - Approval modes are Manually approve, Automatically approve and Skip all approvals.
  - Global instructions live at Settings › Cowork › Edit. Folder instructions are added when you pick a local folder, and Claude can update them.
  - Cloud sessions share memory with chat.

  [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- **Plans and surfaces.**
  - Paid plans only: Pro, Max, Team, Enterprise.
  - Desktop app on macOS and Windows for all paid plans.
  - Web and mobile on Pro, Max and Team, and on Enterprise where an admin enables it.
  - The Chrome side panel on Max and Team, rolling out to Pro.

  Same page as above.
- **Projects.**
  - Each project has its own instructions, context, scheduled tasks and memory.
  - Project memory stays inside that project.
  - Projects made from a local folder stay on that computer.

  [Organize your tasks with projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- **Scheduled tasks.**
  - Cadences are hourly, daily, weekly, weekdays or manual.
  - Tasks run remotely, even with the computer asleep or the app closed. They use connectors and files saved to your Claude account.
  - A task can't be tied to a local folder. A task that needs local files or apps runs only locally, so the desktop app has to be open to reach them.

  [Schedule recurring tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- **Dispatch.**
  - A limited beta on Pro and Max: one ongoing conversation shared between phone and desktop.
  - The desktop must stay awake with the app open.
  - Anthropic warns that messages from your phone can trigger real actions on the computer.

  [Assign tasks from anywhere](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- **Computer use.**
  - A beta on Pro and Max only; Team and Enterprise don't have it yet. Works in the desktop app on macOS and Windows, and on macOS 15 or later Claude can work in background windows. Turn it on at Settings › General › Enable computer use.
  - Claude asks before using each app. You can block apps, and investment and crypto apps are blocked by default.
  - Claude tries connectors first, then the browser, and only then the screen.

  [Let Claude use your computer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
- **Claude in Chrome.**
  - Modes are Manually approve, Automatically approve (the Cowork default) and Skip all approvals, which was formerly "Act without asking" and has no automatic safety review.
  - On Max and Team, and on Pro as it rolls out, the side panel runs as a Cowork session.

  [Permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide), [Get started](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- **Connectors, plugins and skills.**
  - A connector acts with your permissions in the connected service. Team and Enterprise owners can set each tool to Always allow, Needs approval or Blocked. [Connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
  - Plugins bundle skills, connectors and sub-agents. Customize on an installed plugin opens a Cowork task that tailors it. [Plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
  - Skills need code execution and file creation turned on. Anthropic advises installing skills only from trusted sources. [Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- **Privacy setting.** On consumer plans (Free, Pro, Max), turning off the model-improvement toggle under Settings › Privacy stops new chats and coding sessions from being used for training. The Privacy Center labels it "Help Improve our AI models"; conversations flagged by safety classifiers may still be used for safety work. [Anthropic Privacy Center](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)
  - Retention is 30 days with training off and up to five years with it on. [Consumer terms update](https://www.anthropic.com/news/updates-to-our-consumer-terms)

## Related

- **Techniques:** [[Set Up Claude Cowork]] · [[Build a Context Map for a Connected Tool]] · [[Write Anti-AI Writing Rules]] · [[Schedule Recurring Claude Tasks]] · [[Configure Safe Autonomy Permissions]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Build a Skill from a Successful Run]]
- **Concepts:** [[Connecting Claude to External Tools]] · [[Permissions and Approval Gates]] · [[Routines and Scheduled Tasks]] · [[Agent Skills]] · [[Build vs Install Third-Party Skills]] · [[Agent Memory Patterns]] · [[CLAUDE.md as a Router]] · [[Choosing a Claude Model]] · [[Always-On Brain OS]]
- **Tools:** [[Claude Code]] · [[Claude in Chrome]] · [[OpenClaw]]
- **People:** [[Simon Pittman]] · [[Ras Mic]] · [[Jay E]]
- **Sources:** [[Simon Pittman - Set Up Claude Cowork]] · [[Ras Mic - How AI Agents and Claude Skills Work]] · [[Jay E - Claude and GPT-Image-2 for On-Brand Design]]
- [[Home]]
