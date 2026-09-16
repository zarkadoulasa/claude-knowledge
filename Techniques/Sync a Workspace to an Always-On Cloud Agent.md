---
type: technique
goal: Keep the skills, routers and memory files from a local Claude Code workspace available to an always-on agent on its own cloud machine, so scheduled jobs keep running with your laptop off, without the two copies drifting or leaking secrets
difficulty: advanced
time_to_build: 2-4 hours including VM setup (estimate, not from the video)
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Nate Herk - 32 Tricks to Level Up Claude Code]]", "[[Nate Herk - Every Level of a Claude Second Brain]]", "[[Anthropic - What Is Claude Managed Agents]]"]
tools: ["[[Hermes Agent]]", "[[Syncthing]]", "[[Claude Code]]", "[[OpenClaw]]"]
tags: [topic/scheduling, topic/automation, topic/agents, topic/portability, topic/memory, topic/skills, topic/agentic-os, topic/privacy]
---

# Sync a Workspace to an Always-On Cloud Agent

## Goal

Build Jay E's "Routines Level 2". Scheduled tasks run on a dedicated cloud computer that never sleeps. The agent there, [[Hermes Agent]] in his case, uses the same skills and memory you built in [[Claude Code]] on your laptop, and [[Syncthing]] keeps the folders matched. The alternative path puts Claude Code itself on a VPS so there is nothing to sync.

## Use when

- **Your jobs need to run while the laptop is off.** Local routines stopping when the computer sleeps is the reason Jay moved most of his scheduled tasks off his laptop ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)–[16:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=978s)).
- **The jobs depend on your local workspace**, meaning skills, routers and memory files, not just connectors.
- **Your skills and memory already work.** Jay only moves on to routines after that ([14:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=876s)–[14:44](https://www.youtube.com/watch?v=8NSyI-npJCU&t=884s)).
- **You are comfortable running a small Linux server:** SSH, a firewall, updates and service logs.

**Don't use it when** a hosted runner already covers the job. Connector-only knowledge work fits a Cowork scheduled task, and repository work fits a cloud routine. Both run with the computer off (Beyond the source). See [[Schedule Recurring Claude Tasks]] and [[Routines and Scheduled Tasks]].

## What the videos say

### Jay E: Hermes on its own computer, fed by Syncthing

All from [[Jay E - The ARMS Framework for a Claude Agentic OS]]:

- **Why move to the cloud.** Local routines only run while the computer is on ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)). Level 2 puts scheduled tasks in the cloud so they run with his computer off ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)–[16:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=978s)).
- **Options he names:**
  - OpenClaw, which he credits with popularising the idea ([16:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=980s));
  - Grok Bot, new but expensive ([16:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=981s)–[16:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=985s));
  - Hermes, which he uses ([16:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=988s)).
- **Why Hermes is always on.** It runs 24/7 because most users give it its own computer. His is a computer in the cloud ([16:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1000s)–[16:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1012s)). Most of the jobs on his routines board are loaded into Hermes ([16:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1013s)–[17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)).
- **The step people miss.** A Hermes agent on its own machine can't reach the skills and context you built up in Claude Code ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s)–[17:09](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1029s)).
- **His fix.** There are several ways, but he uses Syncthing, free open-source software that syncs files between computers ([17:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1030s)–[17:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1043s)).
  - Point it at the workspace Claude Code uses and install it on the Hermes computer ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)–[17:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1051s)).
  - Then sync the files you choose, including the skills and memory files you want Hermes to share ([17:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1051s)–[17:36](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1056s)).
  - He sets this up with a single prompt shown on screen ([17:39](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1059s)). The prompt text isn't in the transcript.
- **Level 3, the no-sync alternative.** Rent a VPS, install Claude Code on it, and keep every file and all context there ([17:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1074s)–[18:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1084s)). Routines never stop, you work in one platform (Claude Code or Codex), and you need no sync tool ([18:05](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1085s)–[18:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1101s)).
  - He knows users experimenting with it ([17:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1071s)).
  - He expects Anthropic and OpenAI to offer it eventually, not yet, because of file storage and security ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)–[18:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1110s)).

### Nate Herk: the VPS route and the Hermes fit

- **VPS.** [[Nate Herk - 32 Tricks to Level Up Claude Code]] runs Claude Code on a remote server so it keeps running with the laptop shut ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)–[12:43](https://www.youtube.com/watch?v=jqoFP9QapXI&t=763s)). You can SSH in and talk to it through Telegram ([12:45](https://www.youtube.com/watch?v=jqoFP9QapXI&t=765s)–[12:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=767s)). It suits long jobs you don't want to babysit ([12:49](https://www.youtube.com/watch?v=jqoFP9QapXI&t=769s)).
- **Hermes.** [[Nate Herk - Every Level of a Claude Second Brain]] thinks adding GBrain, the always-on memory layer in his Level 5, to a Hermes agent would work well. In Claude Code you'd have to handle the crons yourself ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)–[25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)). That's why he doesn't run GBrain yet, though he is experimenting with it on his Hermes agent ([25:57](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1557s)–[26:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1561s)).

### What the videos don't show

- No Syncthing prompt text, configuration, folder list or ignore rules.
- No secrets handling or conflict handling.
- No explanation of how Hermes jobs find the synced folder.
- No VPS hardening.

Everything below the videos section fills those gaps from the vendors' docs (Beyond the source) or as labelled vault suggestions.

## Prerequisites

- **A Claude Code workspace worth sharing.** A router file, skills in folders, and a memory file you maintain. See [[Build a Level 1 Second Brain]] and [[Agent Skills]].
- **A tool-neutral router.** Hermes reads `AGENTS.md` before `CLAUDE.md` (Beyond the source). Set this up with [[Port a Claude Code Brain to Other Agents]] first.
- **A small always-on Linux VM** you control, reachable with an SSH key. Size and provider are up to you.
- **A model provider account for Hermes**, such as Nous Portal or another provider it supports.
- **A list of which scheduled jobs will move**, and what each one reads and writes. Draft the prompts with [[Schedule Recurring Claude Tasks]].

## Design first: one writer per folder

*Vault suggestion, built on Syncthing's documented folder types (Beyond the source).*

Two agents writing the same files is how conflicts and diverging memory start. Give every shared folder one writer:

| Folder | Laptop side | Cloud side | Why |
|---|---|---|---|
| `skills/` (or `.claude/skills/`) | Send Only | Receive Only | You edit skills locally. A cloud agent's edits stay local on the VM, and can be reverted there |
| `context/`, router files | Send Only | Receive Only | One source of truth for who you are and how to route |
| `memory/shared.md` | Send & Receive, but only one agent appends | Send & Receive | Pick the appending agent. The other agent reads only (see Pitfalls) |
| `outputs/cloud/` | Receive Only | Send Only | Cloud jobs write here; you review on the laptop |
| Secrets, `.env`, caches, `.git` | Not shared | Not shared | Keep out with ignore patterns and folder choice |

```text
Laptop (Claude Code)                          Cloud VM (Hermes gateway + cron)
workspace/                                    ~/workspace/
├── AGENTS.md, CLAUDE.md  ──send only──►      ├── AGENTS.md, CLAUDE.md   (receive only)
├── skills/               ──send only──►      ├── skills/                (receive only)
├── context/              ──send only──►      ├── context/               (receive only)
├── memory/shared.md      ◄──── both ────►    ├── memory/shared.md
└── outputs/cloud/        ◄──send only──      └── outputs/cloud/         (send only)
                    Syncthing, TLS, device-ID pairing
```

## Steps

*Product details come from the docs listed in Beyond the source. Commands and choices marked vault are suggestions, not from the video.*

### A. Prepare the workspace (laptop)

1. **Split the workspace into shareable folders** (vault). Move anything the cloud agent shouldn't have out of those folders: API keys, client documents, personal notes. Don't depend on ignore rules alone.
2. **Decide how memory travels.**
   - Claude Code's auto memory lives outside the workspace by default, so syncing the workspace won't carry it.
   - Either point `autoMemoryDirectory` into a shared folder, or keep a hand-curated `memory/shared.md` that both agents are told to use (Beyond the source).
   - Hermes also keeps its own separate memory files.
3. **Make the router tool-neutral.** Real routing content goes in `AGENTS.md` with plain paths, and `CLAUDE.md` imports it. See [[Port a Claude Code Brain to Other Agents]].
4. **Write `.stignore`** in each shared folder root, on both devices, using the starter below. `.stignore` itself never syncs.

### B. Provision the cloud machine

5. **Create the VM** (vault).
   - Create a non-root user for the agent, allow SSH key login only, turn on automatic security updates, and deny inbound traffic except SSH.
   - Keep the Syncthing GUI on its default `127.0.0.1:8384` and reach it through an SSH tunnel (starter below).
6. **Install Syncthing on both machines.** On the VM, run it as a system service so it starts at boot without a login (`systemctl enable syncthing@<user>.service`). On the laptop, the desktop app or a user service is fine.
7. **Pair the devices.** In each GUI, use Actions, then Show ID to copy the Device ID. Add each machine as a Remote Device on the other.
8. **Share the folders** with the types from the design table. Accept each share on the other device.
9. **Turn on file versioning** where you receive changes. Versioning only keeps copies of files replaced or deleted by a *remote* device. So enable it on the VM for skills and context, and on the laptop for `outputs/cloud/`.

### C. Set up Hermes on the VM

10. **Install Hermes** as the agent user, choose a model (`hermes model`), and leave command approvals on the default `smart` mode. Don't run it with `--yolo`. Consider the Docker terminal backend so tool commands run in a hardened sandbox.
11. **Store secrets** in `~/.hermes/.env` with `chmod 600`. If you connect a messaging app, set its allowed-users variable, for example `TELEGRAM_ALLOWED_USERS`.
12. **Let Hermes see the synced skills.** Add the synced skills folder under `skills.external_dirs` in `~/.hermes/config.yaml`. Hermes skills follow the agentskills.io standard. *Vault caution:* test each skill you rely on, because Claude-Code-specific features may not carry over (unverified).
13. **Install the gateway as a service.** Use `hermes gateway install` plus `sudo loginctl enable-linger $USER`, or `sudo hermes gateway install --system`. Check it with `hermes gateway status`. Cron jobs only fire while the gateway runs.
14. **Create the jobs** with `--workdir` pointing at the synced workspace, so `AGENTS.md` or `CLAUDE.md` load, and `--skill` for the skill each job uses. Write each prompt so it saves results into `outputs/cloud/` and appends a run log (prompt starter below).

### D. Verify, then operate

15. **Sync tests** (vault).
    - Edit a skill on the laptop and confirm it appears on the VM within a minute or two.
    - Create a file in `outputs/cloud/` on the VM and confirm it reaches the laptop.
    - Edit a skill on the VM and confirm it does **not** reach the laptop. The receive-only folder shows a local-changes warning you can revert.
16. **Run one job end to end.** Give it a one-shot schedule such as `in 5m`. Check the output file, the run log, and Hermes's own copy under `~/.hermes/cron/output/`.
17. **Check weekly** (vault):
    - search both machines for `*.sync-conflict-*` files;
    - read `outputs/cloud/` run logs for failures;
    - review recent approval decisions (`hermes approvals suggest` reads them from the session log);
    - make sure the laptop has been online long enough to push skill edits, because Syncthing only moves files while both devices are connected.

### Alternative path: Claude Code on the VPS (Jay's Level 3, Nate's hack 26)

Jay's no-sync option ([17:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1074s)–[18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)). The video gives no setup, so these steps are vault suggestions checked against Anthropic's docs.

1. **Put the workspace on the server.** Clone it from a private repository, so the server copy is the primary one. Don't sync it back to the laptop with a second tool.
2. **Authenticate.**
   - For scheduled headless runs, generate a token with `claude setup-token` and load `CLAUDE_CODE_OAUTH_TOKEN` from a `chmod 600` env file.
   - That token can't start Remote Control or use claude.ai connectors. If you want those, sign in with `/login` in an SSH session instead; the login flow supports pasting a code.
3. **Keep interactive sessions alive** by starting them inside `tmux` or `screen`. Remote Control then lets you steer them from your phone.
4. **Schedule headless runs** with the system's cron or systemd timers calling `claude -p "/<skill>"`. Pass an explicit `--permission-mode` and `--allowedTools`, because `-p` starts in Manual mode. Keep `--dangerously-skip-permissions` for a container or VM that holds nothing else, run as a non-root user.
5. **For Telegram access** (Nate [12:47](https://www.youtube.com/watch?v=jqoFP9QapXI&t=767s)), Claude Code's Channels research preview has a Telegram plugin for a running session. Lock it to your account with pairing and an allowlist.

## Starter files & prompts

*Vault starter content: original wording, not from the videos. Paths are examples.*

### Prompt: have Claude Code draft the share plan (run on the laptop)

```markdown
I want an always-on agent on a cloud VM to run scheduled jobs using this workspace's skills and context.
Inspect this workspace and produce outputs/sync-plan.md with:
1. A table of top-level folders: share or keep local, the reason, and the Syncthing folder type for laptop and VM (Send Only / Receive Only / Send & Receive), following "one writer per folder".
2. Every file or folder that looks like a secret, credential, cache, build output or .git directory, and where it should move or how to ignore it.
3. A draft .stignore for each shared folder.
4. Which memory file both agents should use, and which agent is allowed to append to it.
5. The list of scheduled jobs I've described in routines/ and what each one reads and writes.
Do not change any files other than outputs/sync-plan.md.
```

### `.stignore` (put in each shared folder root on both machines)

```text
// Secrets and credentials never leave the laptop
.env
.env.*
**/*.pem
**/credentials*.json
// Version control and machine-local state
.git
**/node_modules
**/.venv
**/__pycache__
// OS clutter that can block folder deletes
(?d).DS_Store
(?d)Thumbs.db
// Shared extra patterns kept in a synced file
#include .stglobalignore
```

### SSH tunnel to the VM's Syncthing GUI

```bash
# Forward local port 8385 to the VM's GUI on 127.0.0.1:8384, without opening a remote shell
ssh -N -L 8385:127.0.0.1:8384 agent@<vm-address>
# then open http://127.0.0.1:8385 in your laptop browser
```

### Syncthing as a boot-time service on the VM

```bash
sudo systemctl enable syncthing@agent.service
sudo systemctl start syncthing@agent.service
```

### Hermes: let it load the synced skills (`~/.hermes/config.yaml`)

```yaml
skills:
  external_dirs:
    - /home/agent/workspace/skills
```

### Hermes: gateway service and a job

```bash
hermes gateway install
sudo loginctl enable-linger "$USER"
hermes gateway status

# Cron expression for weekdays at 07:03. Check the job's next run time, since the VM may be on UTC.
hermes cron create "3 7 * * 1-5" \
  "$(cat /home/agent/workspace/routines/morning-brief.md)" \
  --skill morning-brief \
  --workdir /home/agent/workspace
```

### Job prompt for the cloud agent (`routines/morning-brief.md`)

```markdown
You are running on the always-on cloud machine. Nobody is watching this run.
Working folder: the synced workspace. Read AGENTS.md first and follow its routing.
Skills, routers and context in this workspace are read-only for you: do not edit anything outside outputs/cloud/ and memory/shared.md.
Run the morning-brief skill for today.
Save the result to outputs/cloud/morning-brief/<YYYY-MM-DD>.md.
Append one entry to outputs/cloud/runs.md: time, job, output path, STATUS (OK/PARTIAL/FAILED), and any error.
If a file you need is missing, it may not have synced yet: record that and stop rather than guessing.
Never send email or messages except the final summary to my allowlisted chat.
```

### Headless Claude Code on the VPS (alternative path)

```bash
#!/usr/bin/env bash
# /home/agent/bin/run-skill.sh <skill-name>
set -euo pipefail
source /home/agent/.config/claude-routine.env   # exports CLAUDE_CODE_OAUTH_TOKEN; chmod 600
cd /home/agent/workspace
mkdir -p "runs/$1"
claude -p "/$1" \
  --permission-mode dontAsk \
  --allowedTools "Read,Write,Edit,Bash(git status *),Bash(git diff *)" \
  --output-format json \
  >> "runs/$1/$(date +%F).jsonl" 2>&1
```

```text
# crontab -e  (as the agent user): weekdays at 07:03
3 7 * * 1-5 /home/agent/bin/run-skill.sh morning-brief
```

## Security notes

- **Least privilege** (vault).
  - The VM user owns only the workspace and the agent's own config.
  - Share only the folders jobs need.
  - Make skills and context receive-only on the VM, so a compromised or confused agent can't rewrite what your laptop trusts.
- **Secrets.**
  - Never sync `.env` files.
  - Hermes keeps its keys in `~/.hermes/.env` (mode 600) and strips secret-looking variables from the environment of its terminal and code-execution tools. A skill can declare variables it needs, and those pass through, so review skills that ask for secrets.
  - On the VPS path, load the Claude token from a mode-600 file, not from the crontab line.
- **Transport and discovery.**
  - Syncthing encrypts traffic with TLS and authenticates devices by certificate fingerprint (the Device ID).
  - Global discovery and public relays can still learn your device IDs and addresses, even though file data stays encrypted.
  - Keep the Syncthing config on an encrypted disk, and remove a lost device promptly.
- **Admin surfaces.**
  - Leave the Syncthing GUI bound to `127.0.0.1`. If you ever bind it to all interfaces, the docs require a username, a strong password and HTTPS.
  - Allowlist who can message the agent.
- **Agent approvals.** Hermes's default `smart` approvals and its blocklist of catastrophic commands are a safety net. `--yolo` removes most of it.
- **Data leaving your machine** (vault). Everything the cloud agent reads is sent to its model provider. Treat the shared folders as data you are willing to send there.

## Done when

- [ ] A sync plan exists listing each shared folder, its writer and its folder type on both devices.
- [ ] No secrets, `.git` directories or caches exist in any shared folder, on either machine.
- [ ] Syncthing runs at boot on the VM, and its GUI is reachable only through the SSH tunnel.
- [ ] A skill edit on the laptop appears on the VM, and a VM-side edit to a skill does not reach the laptop.
- [ ] Hermes lists the synced skills, and the gateway service survives a VM reboot.
- [ ] One scheduled job ran with the laptop closed, wrote `outputs/cloud/…` and a run-log entry, and both reached the laptop afterwards.
- [ ] You know which agent appends to shared memory, and the other agent's prompt says it only reads.
- [ ] A weekly check for `*.sync-conflict-*` files and failed runs is on your calendar or in a routine.

## Pitfalls

- **Sync conflicts.**
  - When both sides change a file before syncing, Syncthing keeps one version and renames the other to `<name>.sync-conflict-<date>-<time>-<device>.<ext>`. That conflict file then syncs everywhere like a normal file.
  - An agent reading a folder may pick up the conflict copy as if it were real context. One writer per folder prevents most of this.
- **Diverging memory.**
  - Three memories can drift apart: Claude Code's auto memory (outside the workspace by default), Hermes's own memory files, and your shared memory file.
  - Jay says to sync "memory files" ([17:33](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1053s)) but doesn't say which. Decide explicitly, and route both agents to the same shared file.
- **Deletes and overrides propagate.**
  - A deletion in a send-and-receive folder deletes on the other side too.
  - "Override Changes" on a send-only folder overwrites the other devices and deletes their extra files.
  - Keep versioning on the receiving side.
- **`.stignore` doesn't sync.** A pattern added on one machine doesn't protect the other. Use `#include` with a synced patterns file, or maintain both copies.
- **The wrong router loads.** Hermes loads one project context file type, and `AGENTS.md` wins over `CLAUDE.md`. A stale `AGENTS.md` quietly overrides a fresh `CLAUDE.md`.
- **Jobs don't see the workspace.** Hermes cron jobs run in fresh sessions. Without `--workdir` they don't load your router, and without `external_dirs` they don't see your skills.
- **The gateway isn't running**, so nothing fires. Job definitions survive restarts, but the scheduler lives in the gateway process.
- **Half-synced files.** A job that starts while the laptop is still pushing an edit may see an old or missing file. Have prompts stop and log when a required file is missing, as in the starter.
- **Timezones.** The VM's clock may be UTC while your schedule is written in local time. Check the next run time after creating each job (vault).
- **Two platforms to maintain.** Jay's Level 3 exists precisely to avoid a separate agent plus a sync tool ([18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s)–[18:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1101s)). If most of your jobs are repository work, a cloud routine may be simpler.

## Variations

- **Claude Code on the VPS, no sync** ([17:54](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1074s); [12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)). Covered in the alternative path above.
- **OpenClaw instead of Hermes.** Jay names it as the tool that popularised always-on agents ([16:20](https://www.youtube.com/watch?v=8NSyI-npJCU&t=980s)). The sync design is the same, but check how it loads context files and skills. See [[OpenClaw]].
- **A private git repository instead of Syncthing** (vault). The laptop pushes skills and context, and the VM pulls on a timer before jobs run. You get history and review for free, at the cost of slower, less automatic updates. It also avoids live file conflicts.
- **Hosted instead of self-run.**
  - Cloud routines run Claude Code from a fresh clone with the computer off.
  - Managed Agents scheduled deployments run on a cron with memory stores that persist between runs (docs, not the video; see Beyond the source). In Anthropic's video, the demo agent reads last week's findings before starting ([02:19](https://www.youtube.com/watch?v=NLWiIj47IdI&t=139s)).
  - See [[Routines and Scheduled Tasks]] and [[Build an Event-Triggered Managed Agent]].

## Beyond the source

*Not from the videos. Checked on 2026-09-15 at the linked pages.*

### Syncthing

- **Getting started.** The GUI runs at `http://localhost:8384/`. Find the Device ID under Actions, then Show ID. Add each machine as a Remote Device on the other and choose which folders to share. [Getting started](https://docs.syncthing.net/intro/getting-started.html)
- **Folder types.**
  - **Send & Receive** is two-way.
  - **Send Only** ignores remote changes. "Override Changes" forces the local state onto others and deletes files they have that it doesn't.
  - **Receive Only** applies remote changes but doesn't send local ones. "Revert Local Changes" undoes them, and if both sides change a file, the cluster version wins.
  - [Folder types](https://docs.syncthing.net/users/foldertypes.html)
- **Conflicts.** The older copy is renamed `<filename>.sync-conflict-<date>-<time>-<modifiedBy>.<ext>`, and conflict files propagate like normal files. [Syncing](https://docs.syncthing.net/users/syncing.html)
- **Ignore patterns.**
  - `.stignore` sits in the folder root and is never synced, but it can `#include` a file that is synced.
  - Syntax includes `//` comments, `**`, `!` negation, `(?i)` for case-insensitive matching and `(?d)` for deletable patterns.
  - [Ignoring files](https://docs.syncthing.net/users/ignoring.html)
- **Versioning.** Versioning applies only to files changed by remote devices. Trash Can, Simple, Staggered and External modes store old versions in `.stversions` by default. [File versioning](https://docs.syncthing.net/users/versioning.html)
- **Security.**
  - Device-to-device traffic uses TLS, and devices are identified by certificate fingerprints.
  - Global and local discovery are on by default and let observers learn device IDs; the global discovery operator can also map devices to IP addresses. Public relays learn the IDs of devices that use them, although relayed data stays encrypted.
  - Protect the keys, for example with an encrypted disk.
  - [Security principles](https://docs.syncthing.net/users/security.html)
- **GUI address.** It defaults to `127.0.0.1:8384`. Binding to `0.0.0.0` exposes it, so set a username, a strong password and HTTPS. [GUI listen address](https://docs.syncthing.net/users/guilisten.html)
- **Running at boot on Linux.** As a system service: `systemctl enable syncthing@myuser.service`. As a user service: `systemctl --user enable syncthing.service` plus `loginctl enable-linger`. [Starting Syncthing automatically](https://docs.syncthing.net/users/autostart.html)
- **SSH tunnel.** `ssh -L [bind_address:]port:host:hostport` forwards a local port to the remote side, and `-N` skips running a remote command. [OpenSSH manual](https://man.openbsd.org/ssh)

### Hermes Agent

- **Install and setup.** Linux install is `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`. Then `hermes model` chooses a provider. [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- **Gateway.**
  - `hermes gateway install` sets up a user service; on Linux, `sudo hermes gateway install --system` sets up a boot-time system service.
  - Manage it with `hermes gateway start`, `stop` and `status`.
  - The gateway runs the cron scheduler every 60 seconds, so scheduled jobs only run while it runs.
  - For headless boot with a user service, enable linger.
  - [Messaging gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
- **Cron.**
  - Jobs can be created in chat, with `/cron add`, or with `hermes cron create "<schedule>" "<prompt>"`. Schedules include `in 30m`, `every 2h`, `weekdays at 9am` and cron expressions.
  - Jobs run in fresh isolated sessions. `--workdir` loads `AGENTS.md`, `CLAUDE.md` and `.cursorrules` from that directory and uses it as the tools' working directory, and `--skill` attaches skills.
  - Jobs are stored in `~/.hermes/cron/jobs.json`, and output goes to `~/.hermes/cron/output/{job_id}/{timestamp}.md`.
  - The documented natural-language examples use whole or half hours (such as `weekdays at 9am`), and the page doesn't say which timezone schedules use, so the starter uses a cron expression and checks the next run time.
  - [Scheduled tasks (cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- **Skills.** `~/.hermes/skills/` is the primary directory. Skills follow the agentskills.io open standard, and `skills.external_dirs` in `~/.hermes/config.yaml` adds more skill folders. [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- **Security.**
  - `approvals.mode` is `smart` (default), `manual` or `off`. `--yolo` skips dangerous-command prompts, but a hardline blocklist still applies.
  - The Docker backend drops capabilities and sets `no-new-privileges`.
  - Keep secrets in `~/.hermes/.env` with mode 600, and use variables like `TELEGRAM_ALLOWED_USERS` as allowlists.
  - Variables whose names look secret (containing KEY, TOKEN, SECRET, PASSWORD and similar) are removed from the environment passed to the `terminal` and `execute_code` tools, unless a skill lists them under `required_environment_variables`.
  - Sessions are logged to `~/.hermes/state.db`, and `hermes approvals suggest` turns past approval decisions into allowlist proposals.
  - [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- **Context files and memory.**
  - Hermes loads one project context file type, first match wins: `.hermes.md`/`HERMES.md`, then `AGENTS.override.md`, then `AGENTS.md`, then `CLAUDE.md`, then `.cursorrules`. [Context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
  - Its `MEMORY.md` and `USER.md` live in `~/.hermes/memories/`, separate from Claude Code's memory. [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
  - Both details were also recorded in [[Port a Claude Code Brain to Other Agents]].

### Claude Code on a server, and hosted alternatives

- **Auto memory location.** By default it is stored at `~/.claude/projects/<project>/memory/`, outside the workspace. `autoMemoryDirectory` relocates it. [Memory](https://code.claude.com/docs/en/memory#auto-memory)
- **Headless auth.**
  - `claude setup-token` prints a one-year OAuth token for `CLAUDE_CODE_OAUTH_TOKEN`, on Pro, Max, Team or Enterprise.
  - It can only make model requests, not Remote Control or claude.ai connectors, and `--bare` doesn't read it.
  - On Linux, `/login` credentials live in `~/.claude/.credentials.json` with mode 600.
  - [Authentication](https://code.claude.com/docs/en/authentication)
- **Headless permissions.** `claude -p` starts in Manual mode, so pass `--permission-mode` or `--allowedTools`. [Headless](https://code.claude.com/docs/en/headless) The docs reserve `--dangerously-skip-permissions` for isolated containers or VMs, run as non-root. [Permission modes](https://code.claude.com/docs/en/permission-modes)
- **Remote Control on a server.** The local process must keep running, so on a remote machine start it inside `tmux` or `screen`. The transcript is stored on Anthropic's servers while connected. [Remote Control](https://code.claude.com/docs/en/remote-control)
- **Channels.** A research preview. Telegram, Discord and iMessage plugins push messages into a running session, and only paired, allowlisted senders get through. [Channels](https://code.claude.com/docs/en/channels)
- **Hosted runners that need no machine of yours.**
  - **Cloud routines** (research preview) run from a fresh repository clone, with a minimum interval of one hour. [Routines](https://code.claude.com/docs/en/routines)
  - **Cowork scheduled tasks** run remotely unless they need local files. [Help Center](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
  - **Managed Agents scheduled deployments** run an agent on a cron with optional memory stores. [Scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)
  - Together these weaken Jay's view that Anthropic hosting is still to come ([18:22](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1102s)). But none gives you a persistent, self-managed workspace like his Hermes machine.

## Sources

- [[Jay E - The ARMS Framework for a Claude Agentic OS]]: Routines Levels 1–3 ([14:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=874s)–[18:32](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1112s)), the core of this note. Video: https://www.youtube.com/watch?v=8NSyI-npJCU
- [[Nate Herk - 32 Tricks to Level Up Claude Code]]: hack 26, Claude Code on a VPS ([12:37](https://www.youtube.com/watch?v=jqoFP9QapXI&t=757s)–[12:52](https://www.youtube.com/watch?v=jqoFP9QapXI&t=772s)).
- [[Nate Herk - Every Level of a Claude Second Brain]]: GBrain's always-on layer on a Hermes agent instead of Claude Code crons ([25:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1549s)–[26:01](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1561s)).
- [[Anthropic - What Is Claude Managed Agents]]: a recurring agent that reads last week's findings from a memory store and stores what changed ([02:15](https://www.youtube.com/watch?v=NLWiIj47IdI&t=135s)–[02:30](https://www.youtube.com/watch?v=NLWiIj47IdI&t=150s)), used in the hosted variation.

## Related

- **Tools:** [[Syncthing]], [[Hermes Agent]], [[Claude Code]], [[OpenClaw]]
- **Techniques:** [[Port a Claude Code Brain to Other Agents]], [[Schedule Recurring Claude Tasks]], [[Configure Safe Autonomy Permissions]], [[Build a Level 1 Second Brain]]
- **Concepts:** [[Routines and Scheduled Tasks]], [[Tool-Agnostic Context Files]], [[Claude Code Auto Memory]], [[Agent Memory Patterns]], [[Agentic OS]], [[Always-On Brain OS]], [[Permissions and Approval Gates]]
- **People:** [[Jay E]], [[Nate Herk]]
- [[Home]]
