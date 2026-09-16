---
type: technique
goal: "Let Claude run safe, reversible commands without prompts while destructive commands are blocked or gated, messaging tools can only draft, and any always-on agent works from its own least-privilege account, then prove it with a test plan."
difficulty: intermediate
time_to_build: "About 1–2 hours including the test plan (estimate, not from the videos)"
sources: ["[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Simon Pittman - Set Up Claude Cowork]]", "[[Anthropic - What Is Claude Managed Agents]]", "[[Ras Mic - How AI Agents and Claude Skills Work]]"]
tools: ["[[Claude Code]]", "[[Claude Cowork]]", "[[Claude Managed Agents]]", "[[Claude in Chrome]]", "[[OpenClaw]]"]
tags: [topic/permissions, topic/claude-code, topic/cowork, topic/managed-agents, topic/mcp, topic/privacy, topic/agents]
---

# Configure Safe Autonomy Permissions

## Goal

Get most of the speed of skipping permission prompts without handing Claude the ability to wreck a repo, leak a secret or send a message you never saw. By the end you have:

- a Claude Code permissions block, a hook backstop and a sandbox, each tested;
- send and post tools that only draft or wait for approval;
- a separate, least-privilege account for any agent that runs unattended.

The idea behind it is [[Permissions and Approval Gates]].

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: skip `--dangerously-skip-permissions`. Allow the commands you know are safe, deny destructive ones, and remember that deny wins ([14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)).
- [[Simon Pittman - Set Up Claude Cowork]]: never delete, send or publish without checking; drafts only for email; per-tool connector permissions ([10:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=615s), [26:18](https://www.youtube.com/watch?v=pl90LATQlHI&t=1578s), [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)).
- [[Anthropic - What Is Claude Managed Agents]]: a permission policy holds the Slack post until a person approves ([02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the autonomous agent gets its own email, not yours ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=473s)).

## Use when

- You keep approving the same safe commands and are tempted to turn prompts off altogether (Nate [14:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=847s)–[14:14](https://www.youtube.com/watch?v=jqoFP9QapXI&t=854s)).
- Claude has connectors that can send, post or delete: Gmail, Slack, Notion (Simon [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)).
- You're about to leave something running on a schedule or as an always-on agent (Simon [41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s); Ras Mic [07:56](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=476s)).
- Skip it for a throwaway container you'd happily delete. The docs' recommendation for that case is under *Variations*.

## Prerequisites

- [[Claude Code]] in a git repository you can safely test in: a scratch clone or a branch.
- `jq` on your PATH for the hook. The docs' hook examples use it.
- macOS, Linux or WSL2 if you want the Bash sandbox. Native Windows isn't supported ([sandboxing docs](https://code.claude.com/docs/en/sandboxing)).
- For connectors: access to Customize > Connectors in the Claude app or Cowork.
- For an always-on agent: a spare email account and the ability to create scoped credentials for it.

## Steps

1. **List what Claude actually does in this project.** Sort it into three buckets (vault suggestion, following Nate's split between safe and destructive commands, [14:15](https://www.youtube.com/watch?v=jqoFP9QapXI&t=855s)–[14:22](https://www.youtube.com/watch?v=jqoFP9QapXI&t=862s)):
   - **Allow:** routine and reversible, like tests, lint, build and local commits.
   - **Ask:** fine sometimes, but you want to see it, like pushes, installs, `rm`, `curl`.
   - **Deny:** never, like force-push, hard reset, recursive deletes and secrets.
2. **Pick your base mode.** Don't start from bypass mode. Nate's point is that the flag is named "dangerous" for a reason ([14:11](https://www.youtube.com/watch?v=jqoFP9QapXI&t=851s)).
   - Current docs offer Manual (`default`) plus rules, or `auto`, where a classifier reviews actions. `auto` is the built-in starting mode on Pro, Max and Team plans.
   - They reserve `bypassPermissions` for isolated containers and VMs ([permission modes](https://code.claude.com/docs/en/permission-modes)).
   - The rules below work in every mode, because deny rules block even in bypass mode.
3. **Write the project rules.** Paste starter A into `.claude/settings.json` and edit the commands to match your stack. Deny beats allow (Nate [14:32](https://www.youtube.com/watch?v=jqoFP9QapXI&t=872s)), and ask beats allow too ([permissions docs](https://code.claude.com/docs/en/permissions)).
4. **Add personal rules that follow you everywhere.** Paste starter A2 into `~/.claude/settings.json`. It blocks reads of your SSH and cloud credentials in every project and locks you out of bypass mode on your own machine.
5. **Add a hook backstop** (starter B).
   - Prefix rules only match the command text as written. A hook sees the whole command, so it can catch `/bin/rm -rf` or `bash -c '…'`.
   - Make the script executable and register it. A hook exit code of 2 blocks the call, and deny rules still apply whatever a hook returns ([hooks guide](https://code.claude.com/docs/en/hooks-guide), [permissions docs](https://code.claude.com/docs/en/permissions)).
6. **Turn on the Bash sandbox** (starter C, or run `/sandbox`).
   - This is the layer that binds subprocesses: a Python one-liner can't read what your `Read` deny rules protect, because those paths are merged into the sandbox configuration.
   - Explicit deny rules and content-scoped ask rules like `Bash(git push *)` still apply ([sandboxing docs](https://code.claude.com/docs/en/sandboxing)).
7. **Gate every outbound tool.**
   - **Claude Code MCP tools.** Put send, forward and delete tools in `ask` or `deny` with tool-name globs, as in the MCP lines of starter A. Run `/mcp` to see the exact server and tool names ([permissions docs](https://code.claude.com/docs/en/permissions)).
   - **Claude app or Cowork connectors.** In Customize > Connectors, leave read tools allowed and set send, post, delete and publish tools to needs approval or blocked (Simon [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)–[24:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=1481s)).
   - **Instructions.** Paste starter D into CLAUDE.md or Cowork's global instructions. Tell Claude to keep the rule in its memory or instructions when you correct it (Simon [26:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1574s)–[26:38](https://www.youtube.com/watch?v=pl90LATQlHI&t=1598s)). Instructions shape behaviour; the tool settings above are what enforce it.
   - **Managed Agents.** Leave the MCP toolset on its `always_ask` default and pre-approve only named read tools (starter E), mirroring the demo's approval before the Slack post ([03:00](https://www.youtube.com/watch?v=NLWiIj47IdI&t=180s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)).
8. **Give any unattended agent its own account** (starter F).
   - Ras Mic's agent has its own address, and he forwards it only the sponsor emails it should handle ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=473s)).
   - Apply the same idea to databases and OAuth: a read-only database user, and pinned `oauth.scopes` for MCP servers ([MCP docs](https://code.claude.com/docs/en/mcp)).
9. **Lock down browser and computer use.**
   - When Chrome asks, allow the action this time only (Simon [22:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1356s)–[22:42](https://www.youtube.com/watch?v=pl90LATQlHI&t=1362s)). The per-site "always allow" option comes from the [Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide), not the video.
   - Leave off the setting that lets Claude act in Chrome without asking on sites you haven't approved, unless you accept that risk ([44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s)–[44:41](https://www.youtube.com/watch?v=pl90LATQlHI&t=2681s)).
   - Add sensitive apps to the computer-use deny list ([44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s)–[45:00](https://www.youtube.com/watch?v=pl90LATQlHI&t=2700s)).
10. **Run the test plan** (starter G) in the scratch repo and write down each result.
11. **Review once a month** (vault suggestion). `/permissions` lists every rule and the settings file it came from. Rules you approve with "Yes, and don't ask again" pile up in `.claude/settings.local.json` ([permissions docs](https://code.claude.com/docs/en/permissions)); prune them.

## Starter files & prompts

*Everything below is vault starter content, written for this note. Syntax was checked against the Claude Code and Claude Platform docs on 2026-09-15.*

### A. Project rules: `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test *)",
      "Bash(npm run lint *)",
      "Bash(npm run build)",
      "Bash(npm run typecheck)",
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(git switch *)",
      "Bash(git stash *)",
      "Edit(/src/**)",
      "Edit(/tests/**)",
      "WebFetch(domain:code.claude.com)"
    ],
    "ask": [
      "Bash(rm *)",
      "Bash(git push *)",
      "Bash(npm install *)",
      "Bash(curl *)",
      "Bash(wget *)",
      "mcp__gmail__*send*",
      "mcp__gmail__*forward*",
      "mcp__slack__*post*"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Bash(git reset --hard *)",
      "Bash(git clean *)",
      "Read(**/.env)",
      "Read(**/.env.*)",
      "Read(secrets/**)",
      "mcp__gmail__*delete*",
      "mcp__gmail__*trash*"
    ]
  }
}
```

How to read it. Rule behaviour is from the [permissions docs](https://code.claude.com/docs/en/permissions); the choice of rules is the vault's.

| Rule | Why it's there |
|---|---|
| `Bash(npm run test *)` | A trailing ` *` also matches the bare command, so this covers `npm run test` and `npm run test --watch` |
| `Edit(/src/**)` | In project settings, a single leading `/` anchors at the primary working directory (where you started Claude Code), not the filesystem root, so start sessions from the repo root. Use `//` for a true absolute path |
| `Bash(rm *)` in ask **and** `Bash(rm -rf *)` in deny | Deny catches the obvious form. The ask catches spellings like `rm -fr` that slip past the deny pattern. Ask rules are never auto-approved in any mode, even `acceptEdits`, which otherwise auto-approves `rm` |
| `Read(**/.env)`, `Read(**/.env.*)` | Match at any depth. A `Read` deny also blocks Edit and Write on the same path. This blocks `.env.example` too; add a narrower rule if you need it |
| `Read(secrets/**)` | As a deny rule, a single-directory pattern matches a `secrets` folder at any depth |
| `mcp__gmail__*send*` | Deny and ask rules accept globs in the tool-name position, as long as the pattern matches the full tool name. Allow rules need a literal `mcp__<server>__` prefix before any glob. Replace `gmail` and `slack` with the exact server and tool names `/mcp` shows. claude.ai connectors that Claude Code fetches itself appear as `mcp__claude_ai_<server>__<tool>` |
| No `git status` / `git diff` / `ls` | Read-only commands, including read-only git, already run without a prompt |

### A2. Personal rules: `~/.claude/settings.json`

```json
{
  "permissions": {
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(~/.config/gcloud/**)"
    ],
    "disableBypassPermissionsMode": "disable"
  }
}
```

In user settings, `~/` paths are home-relative, so these apply in every project. Remove `disableBypassPermissionsMode` on machines where you deliberately run bypass mode inside a container.

### B. Hook backstop: `.claude/hooks/guard-bash.sh`

```bash
#!/bin/bash
# guard-bash.sh (vault starter). Blocks destructive shell patterns anywhere in the
# command text, including /bin/rm and bash -c '...'. It can't see inside scripts.
INPUT=$(cat)
COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')

BLOCK_PATTERNS=(
  '(^|[^[:alnum:]_-])rm([[:space:]]+-[[:alnum:]-]+)*[[:space:]]+(-[[:alnum:]]*r|--recursive)'
  'git[[:space:]].*push.*(--force|[[:space:]]-f([[:space:]]|$))'
  'git[[:space:]].*reset[[:space:]].*--hard'
  'git[[:space:]].*clean[[:space:]].*-[[:alnum:]]*f'
  '(drop|truncate)[[:space:]]+(table|database|schema)'
)

for pattern in "${BLOCK_PATTERNS[@]}"; do
  if printf '%s' "$COMMAND" | grep -Eiq -- "$pattern"; then
    echo "Blocked by guard-bash.sh (pattern: $pattern). If this is really needed, ask the user to run it." >&2
    exit 2
  fi
done
exit 0
```

Then run `chmod +x .claude/hooks/guard-bash.sh` and add this to the same `.claude/settings.json`, alongside `permissions`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard-bash.sh" }
        ]
      }
    ]
  }
}
```

The script matches case-insensitively and can false-positive, for example on a commit message that mentions `push -f`. That's the right direction to fail in. `.claude/` is a protected path, and settings allow rules can't pre-approve writes to it. In Manual and `acceptEdits` modes an edit to the hook prompts you. In `auto` mode it goes to the classifier instead, and in bypass mode it is allowed. If you run in auto mode, check the hook file with `git diff` now and then ([permission modes](https://code.claude.com/docs/en/permission-modes)).

### C. Sandbox block (add to `.claude/settings.json`)

```json
{
  "sandbox": {
    "enabled": true,
    "allowUnsandboxedCommands": false
  }
}
```

`allowUnsandboxedCommands: false` removes the escape hatch that retries a failed command outside the sandbox. Some tools don't work inside the sandbox: `docker` always needs excluding, and on macOS Go-based CLIs such as `gh`, `gcloud` and `terraform` may fail TLS checks. List those under `sandbox.excludedCommands` and remember they then run unsandboxed ([sandboxing docs](https://code.claude.com/docs/en/sandboxing)).

### D. Outbound-actions block for CLAUDE.md or Cowork global instructions

```markdown
## Outbound actions (non-negotiable)
- Email: create drafts in the original thread. Never send, forward, or delete mail.
  After drafting, list each draft: recipient, subject, one-line summary.
- Chat and social: write the message here for me to post. Don't post it yourself.
- Deleting files, publishing, sharing publicly, paying, or changing account settings:
  stop and ask first, naming exactly what will change.
- If a tool call would do any of the above and I haven't approved it in this
  conversation, don't make the call.
- When I correct one of these behaviours, update these instructions or your memory
  so the correction sticks.
```

### E. Managed Agents: approval before posting

```json
{
  "mcp_servers": [
    { "type": "url", "name": "slack", "url": "https://<your-slack-mcp-server>/mcp" }
  ],
  "tools": [
    { "type": "agent_toolset_20260401" },
    {
      "type": "mcp_toolset",
      "mcp_server_name": "slack",
      "default_config": { "permission_policy": { "type": "always_ask" } },
      "configs": [
        { "name": "<read-channel tool name>", "permission_policy": { "type": "always_allow" } },
        { "name": "<search tool name>", "permission_policy": { "type": "always_allow" } }
      ]
    }
  ]
}
```

- **Why the default stays `always_ask`.** It's already the MCP toolset default. The docs say it exists so tools a server adds later can't run without approval. Setting it explicitly and pre-approving only named read tools keeps posting, and any future write tool, behind a person. Don't flip the default to `always_allow` and try to list the risky tools one by one.
- **Tool names.** Per-tool `configs` use the tool name the MCP server reports.
- **When the session pauses.** It emits `session.status_idle` whose `stop_reason.type` is `requires_action`; the waiting event IDs are in `stop_reason.event_ids`. For each one, your app sends a `user.tool_confirmation` event with that ID as `tool_use_id`, `"result": "allow"` or `"deny"`, and an optional `deny_message`.
- **The agent toolset is `always_allow` by default.** That includes bash in the session container. Add a `configs` entry for `bash` with `always_ask` if the container can reach anything you care about.
- **Don't use `auto` here.** It isn't a human checkpoint.
- **Custom tools are ungoverned.** Tools your backend runs aren't covered by these policies, so gate them in your own code.

Verified: [Managed Agents permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies).

### F. Dedicated-account checklist for an always-on agent

- [ ] The agent has its own mailbox. It never signs in to yours (Ras Mic [07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=466s)).
- [ ] You forward only what it should process (Ras Mic [07:49](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=469s)).
- [ ] Database access uses a read-only user ([MCP docs](https://code.claude.com/docs/en/mcp)).
- [ ] OAuth-based MCP servers have `oauth.scopes` pinned to the minimum ([MCP docs](https://code.claude.com/docs/en/mcp)).
- [ ] API keys belong to the agent alone, so you can revoke them without breaking anything else (vault suggestion).
- [ ] No payment or banking connectors (vault suggestion, prompted by Simon's PayPal aside, [23:49](https://www.youtube.com/watch?v=pl90LATQlHI&t=1429s)).
- [ ] Synced folders contain only what the agent needs. See [[Sync a Workspace to an Always-On Cloud Agent]].

### G. Test plan (run in the scratch repo)

Create a fake `.env` containing `DUMMY_SECRET=not-a-real-secret` and a disposable `build/` folder first.

| # | Ask Claude to… | Expected result | What it proves |
|---|---|---|---|
| 1 | Run the test suite | Runs, no prompt | Allow rule |
| 2 | Commit the current change | Runs, no prompt | Allow rule |
| 3 | Push the branch | Prompt | Ask rule |
| 4 | Run `rm -rf build` | Denied | Deny rule beats everything |
| 5 | Run `/bin/rm -rf build` | Blocked by the hook | Hook catches what the prefix rule misses |
| 6 | Show the contents of `.env` | Denied | `Read` deny also covers `cat` |
| 7 | Print `.env` with a Python one-liner | Blocked with the sandbox on; may succeed with it off | Why the sandbox layer matters |
| 8 | Force-push | Denied | Deny rule plus hook |
| 9 | Reply "yes" to a test email via the connector | Draft created. Any send attempt prompts or is blocked | Instructions plus tool setting |
| 10 | Start `claude --dangerously-skip-permissions` | Bypass mode isn't available (with starter A2) | Bypass lock-out |
| 11 | Run `/permissions` | Every rule listed with its source file, no invalid-rule warnings | Config loaded as intended |

## Done when

- [ ] `.claude/settings.json` holds allow, ask and deny lists that match your three buckets, and `/permissions` shows them.
- [ ] `~/.claude/settings.json` denies credential folders everywhere.
- [ ] The guard hook is executable, registered, and blocked test 5.
- [ ] The sandbox is on, or you've written down why it isn't. Test 7 behaved as expected.
- [ ] Every send, post, delete and publish tool you've connected is set to ask, needs approval, or blocked, in every surface you use.
- [ ] The outbound-actions block is in CLAUDE.md or Cowork's global instructions.
- [ ] Any unattended agent runs from its own account with the starter F boxes ticked.
- [ ] All 11 tests are recorded with pass or fail.

## Pitfalls

- **Deny rules aren't a security boundary.** They match the command as written, so `/bin/rm`, `sh -c` and `git -C . push` get past a prefix rule. Read and Edit denies don't bind scripts that open files themselves. Use the hook and the sandbox too ([permissions docs](https://code.claude.com/docs/en/permissions)). This is the gap in Nate's "same speed without the danger" ([14:24](https://www.youtube.com/watch?v=jqoFP9QapXI&t=864s)).
- **Ask beats allow, and a broad deny can't carry exceptions.** An ask rule for `Bash(npx *)` silently overrides an allow for `Bash(npx tsc *)`, and denying `Bash(aws *)` also blocks an allowed `Bash(aws s3 ls)` ([permissions docs](https://code.claude.com/docs/en/permissions)).
- **A `*` before the subcommand in an allow rule is too broad.** `Bash(git * main)` matches every git subcommand. Environment runners such as `npx`, `docker exec` and `devbox run` execute whatever follows them, so allow exact inner commands instead ([permissions docs](https://code.claude.com/docs/en/permissions)).
- **`acceptEdits` auto-approves `rm`, `mv` and `sed` inside the working directory.** Only an explicit ask or deny rule stops that ([permission modes](https://code.claude.com/docs/en/permission-modes)).
- **Headless runs in untrusted folders skip project allow rules.** `claude -p` in a folder you never trusted doesn't apply the project's `permissions.allow`, but deny and ask rules still apply. Scheduled or scripted runs can behave differently from your interactive session ([permissions docs](https://code.claude.com/docs/en/permissions)).
- **Bypass mode is for isolated environments only.** In bypass mode allow rules do nothing, protected paths aren't checked and nothing guards against prompt injection ([permission modes](https://code.claude.com/docs/en/permission-modes)).
- **Instructions aren't enforcement.** Simon's never-send rule ([10:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=615s)) shapes what Claude attempts. The connector's per-tool setting ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s)) is what stops the call. Current docs say permission rules, not CLAUDE.md, decide what's allowed ([permissions docs](https://code.claude.com/docs/en/permissions)).
- **Settings that quietly widen access.** Granting a folder "just for a demo" (Simon [05:21](https://www.youtube.com/watch?v=pl90LATQlHI&t=321s)) or letting the browser act unasked on unapproved sites ([44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s)) undoes the rest of this setup.
- **Unattended schedules.** Scheduled tasks run with your connectors while nobody watches ([41:35](https://www.youtube.com/watch?v=pl90LATQlHI&t=2495s)). The Cowork Help Center advises keeping irreversible actions out of them ([Use Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)).

## Variations

- **Auto mode instead of a long allow list.** A classifier reviews actions and your deny and ask rules still apply. It's the built-in starting mode on Pro, Max and Team, and needs a supported model ([permission modes](https://code.claude.com/docs/en/permission-modes)).
- **CI with an exact allowlist.** Run `claude -p "run the test suite" --permission-mode dontAsk --allowedTools "Bash(npm test)" "Read"`. Anything not pre-approved is denied rather than prompted ([permission modes](https://code.claude.com/docs/en/permission-modes)).
- **Fully unattended in a container.** Here `--dangerously-skip-permissions` is acceptable, run as a non-root user, for example with the dev container config. Keep deny rules in place, since they still block in bypass mode ([permission modes](https://code.claude.com/docs/en/permission-modes)).
- **Cowork only, no Claude Code.**
  - Use per-tool connector settings and a computer-use app deny list (Simon [24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s), [44:43](https://www.youtube.com/watch?v=pl90LATQlHI&t=2683s)). Add Manually approve mode for high-stakes sessions ([Use Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)).
  - Cowork asks before permanently deleting files in every mode ([Use Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)).
  - Full walkthrough: [[Set Up Claude Cowork]].
- **Organisation-wide.** Put `disableBypassPermissionsMode` and your deny list in managed settings so no user or project can override them. Set risky claude.ai connector tools to `ask` or `blocked` at the org level; `ask` prompts even in `auto` and bypass modes ([permissions docs](https://code.claude.com/docs/en/permissions), [MCP docs](https://code.claude.com/docs/en/mcp)).
- **Event-triggered agents.** Combine starter E with the build in [[Build an Event-Triggered Managed Agent]].

## Sources

- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: allow safe commands, deny destructive ones instead of skipping permissions, deny beats allow ([14:02](https://www.youtube.com/watch?v=jqoFP9QapXI&t=842s)–[14:35](https://www.youtube.com/watch?v=jqoFP9QapXI&t=875s)).
- [[Simon Pittman - Set Up Claude Cowork]]:
  - one-folder workspace ([04:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=255s));
  - questioning delete prompts ([07:16](https://www.youtube.com/watch?v=pl90LATQlHI&t=436s));
  - written safety rules ([10:15](https://www.youtube.com/watch?v=pl90LATQlHI&t=615s));
  - per-tool connector permissions ([24:24](https://www.youtube.com/watch?v=pl90LATQlHI&t=1464s));
  - drafts-only email ([26:14](https://www.youtube.com/watch?v=pl90LATQlHI&t=1574s)–[26:57](https://www.youtube.com/watch?v=pl90LATQlHI&t=1617s));
  - browser and computer-use settings ([22:36](https://www.youtube.com/watch?v=pl90LATQlHI&t=1356s), [44:33](https://www.youtube.com/watch?v=pl90LATQlHI&t=2673s)–[45:00](https://www.youtube.com/watch?v=pl90LATQlHI&t=2700s)).
- [[Anthropic - What Is Claude Managed Agents]]: approval before the Slack post ([02:58](https://www.youtube.com/watch?v=NLWiIj47IdI&t=178s)–[03:08](https://www.youtube.com/watch?v=NLWiIj47IdI&t=188s)); isolated containers and network controls ([00:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=15s), [00:24](https://www.youtube.com/watch?v=NLWiIj47IdI&t=24s)).
- [[Ras Mic - How AI Agents and Claude Skills Work]]: the agent's own email, forwarded messages only ([07:36](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=456s)–[07:53](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=473s)).

## Beyond the source

*None of the videos show rule syntax, hooks, sandbox settings or API policy fields. Everything of that kind in this note comes from these pages, checked on 2026-09-15:*

- [Configure permissions](https://code.claude.com/docs/en/permissions): rule syntax, deny → ask → allow order, what Bash and Read/Edit rules don't match, MCP rule names, workspace trust.
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes): the six modes, auto as the Pro/Max/Team starting mode, bypass only in isolated environments, protected and critical paths, `disableBypassPermissionsMode`.
- [Sandboxing](https://code.claude.com/docs/en/sandboxing): `sandbox.enabled`, `allowUnsandboxedCommands`, `excludedCommands`, and how permission rules are merged into the sandbox.
- [Hooks guide](https://code.claude.com/docs/en/hooks-guide): PreToolUse registration, `tool_input.command` on stdin, exit code 2 blocks.
- [MCP](https://code.claude.com/docs/en/mcp): read-only DB users, `oauth.scopes`, org-level connector tool controls.
- [Managed Agents permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies): `always_allow`, `always_ask`, `auto`, per-tool `configs`, `user.tool_confirmation`.
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) and [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors): Cowork approval modes (Manually approve for sensitive or hard-to-undo work) and deletion prompts; Gmail sending asks for approval by default.
- [Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide): the same three approval modes, and site prompts that allow one action or always allow actions on that site.

## Related

- Concept: [[Permissions and Approval Gates]] · [[Connecting Claude to External Tools]] · [[Routines and Scheduled Tasks]]
- Techniques: [[Set Up Claude Cowork]] · [[Build an Event-Triggered Managed Agent]] · [[Schedule Recurring Claude Tasks]] · [[Sync a Workspace to an Always-On Cloud Agent]] · [[Build Verification into Every Task]] · [[Parallel Sessions with Git Worktrees]]
- Tools: [[Claude Code]] · [[Claude Cowork]] · [[Claude Managed Agents]] · [[Claude in Chrome]] · [[OpenClaw]]
- People: [[Nate Herk]] · [[Simon Pittman]] · [[Ras Mic]]
- [[Home]]
