---
type: concept
aliases: ["Human in the Loop", "Approval Gates", "Least Privilege for Agents", "Safe Autonomy"]
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[Nate Herk - Claude as a One-Person Marketing Team]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]"]
tags: [topic/permissions, topic/claude-code, topic/cowork, topic/managed-agents, topic/agents, topic/privacy, topic/automation, topic/mcp, topic/marketing]
---

# Permissions and Approval Gates

## In one sentence

Let Claude move quickly on work you can undo. Put a human decision, or a hard block, in front of anything you can't undo, such as sending, publishing, deleting or paying. Where you can, set those limits with the product's own permission controls rather than only with instructions.

## How it works

### The spectrum the sources describe

The ordering below is this note's; each row is sourced.

| Setting | What happens | Source |
|---|---|---|
| Approve every step | Safe but slow, which is why people reach for the skip flag | Nate [14:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=847s)–[14:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=851s) |
| Allow list for safe commands, deny list for destructive ones | Safe work runs freely, destructive work is blocked, and deny beats allow | Nate [14:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=855s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s) |
| Per-tool setting on each connector: allow, needs approval, blocked | Reads flow, writes wait for you | Simon [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s) |
| Approval gate on one side-effecting call | The agent works alone until the moment it would post | Managed Agents [02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s) |
| Separate account for the agent | Even a mistake can only touch what you chose to forward | Ras Mic [07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=473s) |
| Skip all permission prompts | Fastest; named "dangerous" for a reason | Nate [14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=854s) |
| Browser acts without asking, even on unapproved sites | Only if you accept that risk | Simon [44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s)–[44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s) |

### Nate Herk: allow and deny lists instead of skipping prompts

- **The shortcut.** Many creators, himself included, have demoed `--dangerously-skip-permissions` so Claude can run without asking at every step ([14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=851s)). It is much faster, but the name is a warning ([14:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=851s)–[14:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=854s)).
- **His alternative.** Go into your permissions, explicitly allow the commands you know are safe, and explicitly deny destructive ones such as deletes and removes ([14:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=855s)–[14:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=862s)).
- **Deny wins.** Anything on the deny list takes priority over the allow list ([14:32](https://www.youtube.com/watch?v=jqoFP9QapXI&t=872s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)). Current docs agree; see *Beyond the source*.
- **His overclaim.** He says this gets you the same speed and autonomy as skipping permissions, without the danger ([14:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=864s)–[14:30](https://www.youtube.com/watch?v=jqoFP9QapXI&t=870s)). The docs are more careful about what deny rules catch; see *Beyond the source*.
- He shows no rule syntax or settings file. The buildable version is [[Configure Safe Autonomy Permissions]].

### Simon Pittman: layered guardrails for a personal assistant

His Cowork setup stacks several gates. Grouping them into layers is this note's framing.

1. **A workspace boundary.**
   - Give Cowork one folder. Claude can only work there, and anything you don't want it to see stays outside ([04:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=255s)–[04:28](https://www.youtube.com/watch?v=pl90LATQlHI&t=268s)).
   - He breaks his own rule a minute later by granting access to his Desktop for a demo ([05:19](https://www.youtube.com/watch?v=pl90LATQlHI&t=319s)–[05:26](https://www.youtube.com/watch?v=pl90LATQlHI&t=326s)), which shows how easily a boundary erodes.
2. **Prompts before destructive actions.**
   - Cowork stops to confirm before the clean-up task goes ahead ([05:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=353s)–[05:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=357s)).
   - When it asks to delete something, he doesn't just approve. He asks which files it means ([07:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=436s)–[07:29](https://www.youtube.com/watch?v=pl90LATQlHI&t=449s)). You never have to agree to anything you don't want ([07:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=453s)–[07:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=456s)).
3. **Written safety rules.**
   - His global-instructions brief includes a rule that Claude never deletes, sends or publishes anything without checking with him first ([10:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=615s)–[10:21](https://www.youtube.com/watch?v=pl90LATQlHI&t=621s)).
   - The drafted instructions end up with a "non-negotiables" section ([18:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1117s)–[18:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1122s)).
4. **Drafts-only email.**
   - Once Claude writes a reply, he asks for it as a draft in the thread. From then on it should always create drafts and list them, and update its memory or instructions so this sticks ([26:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1574s)–[26:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1598s)).
   - His answer to "should AI read my email?" has two parts: Cowork only drafts unless told to send, and his global instructions forbid sending without checking ([26:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1602s)–[26:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=1617s)). The first part came from his instructions and memory, not a product lock. Gmail sends now need approval by default; see *Beyond the source*.
5. **Per-tool connector permissions.**
   - He says each connector you add will always ask permission to use it ([23:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1421s)–[23:44](https://www.youtube.com/watch?v=pl90LATQlHI&t=1424s)).
   - Tools such as Notion expose many permissions, and you can set each one to allowed, needs approval or blocked ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)).
6. **Browser approvals.**
   - Claude in Chrome lets you allow an action for this time only ([22:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1356s)–[22:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1362s)).
   - A separate setting lets Claude act in Chrome without asking, including on sites you haven't approved. You have to be comfortable with that ([44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s)–[44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s)).
7. **Computer use controls.** Computer-use settings grant permission to operate the machine, and let you deny specific apps ([44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s)–[45:00](https://www.youtube.com/watch?v=pl90LATQlHI&t=2700s)).

### Anthropic: an approval gate inside an autonomous agent

- **The incident demo.** A coordinator agent pulls three specialists' findings into one summary. Before it posts the update to Slack, the permission policy fires. The user sees the draft on screen, approves it, and only then does the message go out ([02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)).
- **The gate sits on one call.** The investigation itself runs unattended; only the side-effecting call waits for a person (this note's reading of the demo).
- **Isolation.** Sessions run inside an isolated container ([00:24](https://www.youtube.com/watch?v=NLWiIj47IdI&t=24s)–[00:29](https://www.youtube.com/watch?v=NLWiIj47IdI&t=29s)), in environments configured with network controls ([00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s)–[00:17](https://www.youtube.com/watch?v=NLWiIj47IdI&t=17s)).
- See [[Build an Event-Triggered Managed Agent]] and [[Verification Before Done]], where a person approving is one way of judging done.

### Ras Mic: give the agent its own account

- **Its own email, not his.** His OpenClaw agent screens sponsor emails from its own address. He hasn't given it access to his inbox because of the attack vectors, and because he has been hacked before ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=466s)).
- **Forwarding is the gate.** He forwards each sponsor email to the agent ([07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s)–[07:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=473s)), which checks its inbox every 15 minutes ([07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)–[08:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=480s)).
- **The general principle** (this note's, not his): the damage an always-on agent can do is limited to what you chose to give it, not your whole account.

### Cautionary examples: spending and sending with no gate

- **Paid credits, billed afterwards.** In [[Nate Herk - Claude as a One-Person Marketing Team]], Claude drives [[Higgsfield]] through a custom connector authorised once ([17:01](https://www.youtube.com/watch?v=yCACmFTiCto&t=1021s)). He fires several generation jobs into one chat ([22:02](https://www.youtube.com/watch?v=yCACmFTiCto&t=1322s)) and asks only that costs be reported once the work is done ([22:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=1352s)). The bills came after the spend: $3.43 for 18 ad creatives ([27:36](https://www.youtube.com/watch?v=yCACmFTiCto&t=1656s)) and about $17.55 in credits for one sizzle reel ([29:06](https://www.youtube.com/watch?v=yCACmFTiCto&t=1746s); captioned "17.55 cents"). *This note's reading:* a cost report is an audit trail, not a gate. Ask for an estimate and a go-ahead per batch, or set the tool to need approval.
- **Draft or send, left to the model.** In [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] he asks Claude Code to use Zapier to draft the HTML email to himself or send it ([11:59](https://www.youtube.com/watch?v=NAumQObJEwM&t=719s)), and it is sent ([12:42](https://www.youtube.com/watch?v=NAumQObJEwM&t=762s)). With himself as recipient the risk was low, but approval never comes up; compare Simon's drafts-only rule.
- **One aggregator connector concentrates access.** Jack treats Zapier as his authentication layer: connect once, and [[OpenAI Codex]], Antigravity and [[Hermes Agent]] all get the same tools, Skool included ([12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s)–[12:31](https://www.youtube.com/watch?v=NAumQObJEwM&t=751s)). *This note's reading:* one sign-in then reaches everything behind it, so a mistaken or injected instruction has more to act on. Scope that connector's tools tightly.

## When to use it — and when not to

A starting policy built from the sources. The gate chosen for each action is this note's suggestion.

| Action | Undoable? | Suggested gate | Grounding |
|---|---|---|---|
| Reading files in the workspace | Yes | Allow | Simon's folder boundary [04:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=255s) |
| Running tests, builds, linters | Yes | Allow | Nate's "commands you know are safe" [14:17](https://www.youtube.com/watch?v=jqoFP9QapXI&t=857s) |
| Deleting files | Often not | Deny, or ask and question the prompt | Nate [14:20](https://www.youtube.com/watch?v=jqoFP9QapXI&t=860s); Simon [07:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=436s) |
| Sending email | No | Draft only, send tool needs approval | Simon [26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s), [24:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1477s) |
| Posting to Slack or publishing | No | Human approves the draft | Managed Agents [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s); Simon [10:17](https://www.youtube.com/watch?v=pl90LATQlHI&t=617s) |
| Acting in a signed-in browser | Varies | Approve per action (per-site allow: *Beyond the source*) | Simon [22:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1356s), [44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s) |
| Operating other apps via computer use | Varies | Deny list for sensitive apps | Simon [44:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=2693s) |
| Money | No | Don't connect it, or block it | Simon's PayPal aside [23:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1429s) |
| Paid generation (image or video credits) | No, the credits are spent | Estimate and approve each batch; a cost report afterwards isn't a gate | Nate's after-the-fact reports [22:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=1352s) |
| Actions through an aggregator connector (Zapier-style) | Varies | Fix the tool list; sends need approval | Jack [12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s) |
| An always-on agent handling email | n/a | A dedicated account you forward to | Ras Mic [07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s) |

**When gates hurt more than they help.** Prompting on every step is slow ([14:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=847s)), and constant prompts tend to get rubber-stamped (this note's inference). For reversible work in an isolated environment, fewer prompts are reasonable. The docs say where fully skipping them is acceptable; see *Beyond the source*.

**Pitfalls**

- **Approving by reflex.** Simon's habit of asking what a prompt will actually do is the fix ([07:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=444s)).
- **Quietly widening the boundary.** One demo grant turned his one-folder rule into Desktop access ([05:21](https://www.youtube.com/watch?v=pl90LATQlHI&t=321s)).
- **Believing deny lists equal safety.** Nate's "same speed without the danger" ([14:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=864s)) overstates what text-matching rules can stop.
- **Leaving the browser acting unasked.** That setting covers sites you never approved ([44:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2675s)).
- **Unattended schedules with write access.** Scheduled tasks run with your connectors while nobody watches ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)). Keep irreversible actions out of them (this note's advice; the Help Center agrees, see below). See [[Routines and Scheduled Tasks]].

## Where sources disagree

- **How much to connect.** Simon says to add every tool you use and govern each with approvals ([23:37](https://www.youtube.com/watch?v=pl90LATQlHI&t=1417s), [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)). Ras Mic won't give his agent his inbox at all ([07:41](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=461s)). *This note's reading:* they describe different trust models. Simon's Cowork is a supervised assistant you watch. Ras Mic's OpenClaw agent runs on its own every 15 minutes, so isolation replaces supervision.
- **Rules in text versus rules in settings.** Simon's strongest email guard is written instructions plus a remembered habit ([26:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=1593s), [26:53](https://www.youtube.com/watch?v=pl90LATQlHI&t=1613s)). Nate and the Managed Agents demo rely on configured permissions that the harness enforces ([14:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=855s), [03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)). The docs side with enforcement; see *Beyond the source*. Simon's per-tool connector settings are the enforceable half of his setup.
- **One connector for everything, or only what you need?** Jack routes every tool through one Zapier connection shared by all his harnesses ([12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s)). Ras Mic gives his agent only what he forwards ([07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s)). *This note's reading:* Jack optimises for less setup, Ras Mic for less exposure.

## Perspectives from sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: skip `--dangerously-skip-permissions`; allow safe commands, deny destructive ones, and deny wins ([14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)).
- [[Simon Pittman - Set Up Claude Cowork]]: a one-folder workspace, questioning delete prompts, written never-send-or-delete rules, drafts-only email, per-tool connector permissions, one-off browser approvals and a computer-use app deny list ([04:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=255s), [07:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=436s), [10:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=615s), [26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s), [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s), [44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s)). See [[Set Up Claude Cowork]].
- [[Anthropic - What Is Claude Managed Agents]]: a permission policy pauses the agent before a Slack post until a person approves the draft ([02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: an autonomous agent gets its own email address and only what you forward ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)).
- [[Nate Herk - Claude as a One-Person Marketing Team]] (cautionary): paid generations with only after-the-fact cost reports ([22:32](https://www.youtube.com/watch?v=yCACmFTiCto&t=1352s)).
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] (cautionary): email sent through Zapier with no approval step, and one connector for every harness ([12:13](https://www.youtube.com/watch?v=NAumQObJEwM&t=733s)).

## Beyond the source

*Not from the videos. Each item was checked on 2026-09-15 against the linked page.*

- **Claude Code permission modes** (verified: [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)). On Pro, Max and Team plans the built-in starting mode is `auto`. Shift+Tab cycles modes in the CLI, and `defaultMode` sets the starting mode in settings.

  | Mode (config value) | Runs without asking | Docs' intended use |
  |---|---|---|
  | `default` (labelled Manual) | Reads only | Sensitive work, reviewing every action |
  | `acceptEdits` | Reads, file edits, common filesystem commands in the working directory | Iterating on code you're reviewing |
  | `plan` | Reads, plus classifier-approved commands where auto mode is available; Claude plans instead of editing | Exploring a codebase before changing it |
  | `auto` | Everything, with a separate classifier model running background safety checks | Long tasks with fewer prompts |
  | `dontAsk` | Reads and pre-approved tools; anything else is denied | Locked-down CI and scripts |
  | `bypassPermissions` | Everything | Isolated containers and VMs only |

- **How rules are evaluated.**
  - Order is deny, then ask, then allow, and a rule's specificity doesn't change that order. A broad deny like `Bash(aws *)` therefore can't carry allow exceptions.
  - A deny at any settings level (user, project, local, managed) beats an allow at any other level.
  - Permission rules are enforced by Claude Code, not by the model. CLAUDE.md instructions shape what Claude tries, but they don't change what is allowed.
  - Verified: [Configure permissions](https://code.claude.com/docs/en/permissions).
- **What deny rules don't catch** (the caveat Nate skips).
  - Bash rules match the command text Claude writes. `Bash(rm *)` stops `rm -rf build/` but not `/bin/rm -rf build/` or `bash -c 'rm -rf build/'`. `Bash(git push *)` doesn't stop `git -C . push`.
  - Read and Edit deny rules cover Claude's file tools and the Bash file commands Claude Code recognises, such as `cat`. They don't cover a Python or Node script that opens files itself.
  - For enforcement that doesn't depend on command text, the docs point to the Bash sandbox (OS-level filesystem and network limits that also bind child processes) and to PreToolUse hooks. A hook that exits with code 2 blocks the call.
  - Verified: [permissions](https://code.claude.com/docs/en/permissions), [sandboxing](https://code.claude.com/docs/en/sandboxing), [hooks guide](https://code.claude.com/docs/en/hooks-guide).
- **Where bypass mode is appropriate.**
  - The docs say to use `bypassPermissions` (the same as `--dangerously-skip-permissions`) only in isolated environments such as containers or VMs where Claude Code can't damage the host.
  - It skips protected-path checks and offers no protection against prompt injection. On Linux and macOS it refuses to run as root or under sudo.
  - Deny rules still block in this mode, explicit ask rules still prompt, and allow rules have no effect. `rm` or `rmdir` aimed at a critical path is never auto-approved in any mode.
  - Setting `permissions.disableBypassPermissionsMode` to `"disable"` switches the mode off, and managed settings make that stick.
  - Verified: [permission modes](https://code.claude.com/docs/en/permission-modes).
- **Managed Agents permission policies.**
  - `always_allow` runs the tool; `always_ask` pauses the session until your app sends a `user.tool_confirmation` event with `allow` or `deny` (optionally with a `deny_message`); `auto` lets the server run, deny or pause each call.
  - The docs warn that `auto` is not a human checkpoint. If a person must review a tool's calls, set that tool to `always_ask`.
  - Defaults: the agent toolset is `always_allow`, MCP toolsets are `always_ask`. Custom tools aren't governed by policies at all.
  - Verified: [Managed Agents permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies).
- **Cowork's current safeguards.**
  - Three approval modes: Manually approve (recommended for high-stakes work), Automatically approve (the default, where Claude reviews each action for safety) and Skip all approvals.
  - Cowork always asks before permanently deleting files.
  - The Help Center warns that computer use has no sandbox between Claude and your screen. File operations go through permission checks and code runs in an isolated environment, but computer use has neither. A link Claude clicks can open another app you never granted. It suggests blocking sensitive apps such as banking and healthcare portals.
  - For scheduled tasks, it advises avoiding sensitive files and irreversible actions and reviewing past runs.
  - Verified: [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely), [Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
- **Claude in Chrome.** It has the same three modes (Manually approve, Automatically approve, Skip all approvals). Site access can be granted for a single action or as "always allow" on that site. Even with always allow, Claude still asks before downloading files, entering sensitive information or granting authorizations. Verified: [Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide).
- **Email sending is gated by default now.** The Gmail connector can send, reply and forward, and by default asks for approval before each; on Team and Enterprise, owners decide whether members can skip that. Pair Simon's drafts-only instruction with the tool setting. Verified: [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors).
- **Zapier MCP can let the agent widen its own toolset.** By default its servers use dynamic discovery, so the agent can search for and enable new app actions mid-conversation. Manual configuration fixes the action list at mcp.zapier.com. Verified: [How Zapier MCP tools work](https://docs.zapier.com/mcp/overview/how-tools-work).
- **Higgsfield bills MCP generations like any other.** Generations through a connected agent use the platform's credits, priced by model and resolution, and its MCP page mentions no spending cap or confirmation step. Verified: [Higgsfield MCP](https://higgsfield.ai/mcp).

## Related

- Technique: [[Configure Safe Autonomy Permissions]]
- Concepts: [[Connecting Claude to External Tools]] · [[Verification Before Done]] · [[Routines and Scheduled Tasks]] · [[Always-On Brain OS]] · [[Build vs Install Third-Party Skills]]
- Techniques: [[Set Up Claude Cowork]] · [[Build an Event-Triggered Managed Agent]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[Claude Managed Agents]] · [[Claude in Chrome]] · [[OpenClaw]] · [[Higgsfield]] · [[Hermes Agent]]
- People: [[Nate Herk]] · [[Simon Pittman]] · [[Ras Mic]] · [[Jack Roberts]]
- Sources: [[Nate Herk - Claude as a One-Person Marketing Team]] · [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]
- [[Home]]
