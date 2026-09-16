---
type: tool
category: Open-source continuous file synchronization
website: https://syncthing.net
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]"]
tags: [topic/automation, topic/scheduling, topic/agentic-os, topic/portability, topic/skills, topic/memory]
---

# Syncthing

## What it is

[[Jay E]] uses Syncthing as a bridge. It lets an always-on agent running on another computer use the same skills and memory files as his local [[Claude Code]] workspace. The official description is under *Beyond the source*. For the full build, see [[Sync a Workspace to an Always-On Cloud Agent]].

## How sources use it

### [[Jay E - The ARMS Framework for a Claude Agentic OS]]

It appears in his Routines layer, at level 2 (cloud routines).

- **Why he needs it.**
  - Local routines only run while your computer is on ([16:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=964s)), so a lot of his routines run in the cloud instead ([16:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=968s)).
  - He uses [[Hermes Agent]] for this ([16:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=988s)). It's always on because, like most Hermes users, he gives it its own computer, in his case a cloud machine ([16:46](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1006s), [16:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1010s)).
  - Most of the jobs on his routines board are loaded in Hermes ([16:55](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1015s)).
- **The problem he says most people miss.** An agent on a separate computer can't see the skills and context you've built up in Claude Code ([17:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1020s), [17:03](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1023s)).
- **His fix.**
  - There are many ways to solve it. His own choice, and his tip for beginners, is Syncthing ([17:10](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1030s), [17:15](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1035s)).
  - He describes it as free, open-source software that keeps files in sync between computers ([17:18](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1038s), [17:21](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1041s)).
- **Setup as described.**
  1. Point Syncthing at the workspace Claude Code works in ([17:25](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1045s)).
  2. Install it on the computer Hermes uses too ([17:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1047s)).
  3. Choose the files to share, including the skills and memory files Hermes should get ([17:31](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1051s), [17:34](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1054s)).
  4. He offers a single setup prompt ([17:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1060s)), but it appears only on screen and isn't in the transcript.
- **When you wouldn't need it.**
  - His next level up, which he says some users are already trying, is Claude Code installed on a VPS, so all files and context live on one always-on machine ([17:52](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1072s), [18:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1080s)).
  - Routines then keep running 24/7 through a single agent platform ([18:07](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1087s), [18:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1091s)), and no sync tool like Syncthing is needed ([18:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1096s)).
  - He expects OpenAI and Anthropic to offer hosted versions eventually, slowed by file-storage and security concerns ([18:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1104s), [18:28](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1108s)).

## Notes

- **Not demonstrated.** No Syncthing screens, folder settings, ignore rules, conflict handling or secrets handling are shown. The video also doesn't show how Hermes jobs get pointed at the synced folder.
- **Caption fix.** "Sync Thing" → Syncthing.
- **Starting point for a build.** Combine the facts below with [[Sync a Workspace to an Always-On Cloud Agent]], and see [[Hermes Agent]] for which context file Hermes reads.

## Beyond the source

*Not from the video. Checked 2026-09-15 at the linked pages.*

- **What it is.**
  - A continuous file synchronization program, open source under the Mozilla Public License 2.0.
  - No central server: data stays only on your own devices. Connections use TLS with perfect forward secrecy, and only devices you explicitly authorize, identified by certificates, can connect.
  - Runs on macOS, Windows, Linux, the BSDs and more, with a browser-based interface.

  <https://syncthing.net/>, <https://github.com/syncthing/syncthing>
- **Expect a short lag.**
  - It detects changes with a filesystem watcher plus periodic full rescans (hourly by default).
  - The watcher batches changes for about 10 seconds, and deletions wait longer.
  - *My inference:* a Hermes job that starts right after you edit a skill may still see the old version.

  <https://docs.syncthing.net/users/syncing.html>
- **Conflicts.**
  - When a file changes on two devices at once, the copy with the older modification time is renamed `<name>.sync-conflict-<date>-<time>-<modifiedBy>.<ext>`, and that copy syncs like any other file.
  - *My inference:* if both Claude Code and Hermes write to the same memory files, conflict copies will pile up. Give each folder one writer.

  <https://docs.syncthing.net/users/syncing.html>
- **Folder types.**
  - **Send & Receive** is the default.
  - **Send Only** sends local changes out and ignores changes from other devices.
  - **Receive Only** applies changes from other devices but doesn't send local ones.
  - *My inference:* a skills folder you only edit on your laptop could be Send Only there and Receive Only on the Hermes machine.

  <https://docs.syncthing.net/users/foldertypes.html>
- **Ignore patterns.**
  - Put a `.stignore` file in the root of the synced folder. It isn't synced to other devices.
  - Patterns support `*`, `**`, `!` to re-include, `//` comments and `#include`.
  - *My inference:* exclude secrets and bulky generated files. A vault starter example:

  ```text
  // Vault starter content: adjust to your workspace
  .env
  .env.*
  **/node_modules
  **/*.log
  .git
  ```

  <https://docs.syncthing.net/users/ignoring.html>
- **Claude Code auto memory isn't in your workspace.**
  - Auto memory lives in `~/.claude/projects/<project>/memory/`. It's machine-local and never shared across machines.
  - You can move it with `autoMemoryDirectory` in `settings.json`, which takes an absolute path or one starting with `~/`.
  - *My inference:* syncing the workspace alone won't carry auto memory to Hermes. Point the setting at a synced folder, or keep the memory you want to share in files inside the workspace.

  <https://code.claude.com/docs/en/memory#storage-location>
- **Jay's premise is partly dated.**
  - The Claude Code Desktop Routines page offers remote routines. They run in the cloud even when your computer is off and can also fire on API calls or GitHub events.
  - They run on a fresh clone, though, with no access to local files. Local desktop tasks need the app open and the computer awake.
  - *My inference:* Syncthing still earns its place when an always-on agent needs your local workspace files, but not just to keep schedules running.

  <https://code.claude.com/docs/en/desktop-scheduled-tasks>

## Related

- **Techniques:** [[Sync a Workspace to an Always-On Cloud Agent]], [[Port a Claude Code Brain to Other Agents]], [[Schedule Recurring Claude Tasks]]
- **Concepts:** [[Routines and Scheduled Tasks]], [[Agentic OS]], [[Tool-Agnostic Context Files]], [[Claude Code Auto Memory]], [[Always-On Brain OS]]
- **Tools:** [[Hermes Agent]], [[Claude Code]], [[OpenClaw]]
- **People:** [[Jay E]]
- **Source:** [[Jay E - The ARMS Framework for a Claude Agentic OS]]
- [[Home]]
