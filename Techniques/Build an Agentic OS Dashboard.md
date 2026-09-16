---
type: technique
goal: A local dashboard whose panels show what you care about and whose buttons run allowlisted Claude Code skills headlessly with claude -p, saving a report for every run
difficulty: intermediate
time_to_build: 2–4 hours for the minimal starter below, once the skills exist (estimate)
sources: ["[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]", "[[Chase AI - The Three-Step Claude Code Agentic OS]]", "[[Jack Roberts - Design Systems, Critic Loops and a Design OS]]"]
tools: ["[[Claude Code]]", "[[Obsidian]]", "[[Higgsfield]]"]
tags: [topic/agentic-os, topic/claude-code, topic/skills, topic/automation, topic/permissions, topic/teams]
---

# Build an Agentic OS Dashboard

## Goal

Put a visual front end on an [[Agentic OS]] you already have. Panels show your metrics, recent runs and outputs. Buttons run specific skills through headless Claude Code, each with a model, an effort level and permissions you picked in advance. Every run leaves a report you can open later.

## Use when

- **Your skills and memory already work in the terminal.** Both sources treat the UI as the last layer. Jay E learns bottom-up and puts apps last ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s)). Chase calls the UI levels the "cherry on top" and says to spend almost all your time on skills and memory first ([30:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1824s), [30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)).
- **You trigger some skills often, outside any chat.** Jay E put his cleanup skill on the dashboard because he runs it whenever his machine slows down, so he no longer opens a terminal and types the slash command ([09:12](https://www.youtube.com/watch?v=8NSyI-npJCU&t=552s)).
- **You want one place to see things that are hard to see from a terminal** ([26:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1565s)).
- **Non-technical teammates or clients should be able to press a button** instead of learning Claude Code ([24:35](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1475s)).

**Skip it** if you have no tested skills yet. Jay E puts the dashboard at only about 20–30% of the value ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s)).

## What the sources built

None of the videos shows code, config or permission settings. What follows is what was demonstrated; the steps after it are vault starter content.

**Jay E's command center** ([[Jay E - The ARMS Framework for a Claude Agentic OS]]):
- **Widgets:**
  - Calendar events and time zones he cares about ([00:53](https://www.youtube.com/watch?v=8NSyI-npJCU&t=53s)).
  - An email summary that includes messages Claude flags for his attention ([00:56](https://www.youtube.com/watch?v=8NSyI-npJCU&t=56s)).
  - Quick links to micro-apps he built ([01:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=62s)).
  - A YouTube widget ([01:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=68s)).
  - A routines board showing which scheduled tasks fire when ([01:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=71s)).
- **A skills deck:** pick the model and effort for a run, then launch it from the page ([01:16](https://www.youtube.com/watch?v=8NSyI-npJCU&t=76s)).
- **Layout:** widgets can be resized and moved, and Claude Code builds new ones on request ([01:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=89s)).
- **An "artifacts ring":** a searchable index of past artifacts. He searches by client and opens an HTML file from a given date ([01:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=100s), [01:50](https://www.youtube.com/watch?v=8NSyI-npJCU&t=110s)).
- **An entry point to his visual second brain** ([02:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=122s)).
- **Mechanism:** each skills-deck run is a `claude -p` one-shot with the chosen model and effort ([09:49](https://www.youtube.com/watch?v=8NSyI-npJCU&t=589s)). The prompt is just the slash command ([09:58](https://www.youtube.com/watch?v=8NSyI-npJCU&t=598s)), and the run produces a summary report ([09:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=570s)).

**Chase's web app and Obsidian plugin** ([[Chase AI - The Agentic OS Setup for Claude Code]]):
- **Setup:** Claude Code runs underneath and connects to his Obsidian vault ([23:41](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1421s)).
- **Metric panels:**
  - Subscriber counts, his latest video and his Claude 5-hour usage window ([23:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1431s)).
  - Directives pulled from Google Calendar ([23:59](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1439s)).
  - Documents Claude has created ([24:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1443s)).
- **Skill buttons:**
  - Skills and automations appear as single buttons ([24:04](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1444s)).
  - Clicking "inbox brief" queues a run that goes through his inbox, creates drafts and reports what looks important ([24:11](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1451s)–[24:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1459s)).
  - The panels are whatever metrics you choose to show ([24:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1464s)).
  - Finished briefs open as full write-ups that can also be opened in Obsidian ([25:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1530s)).
- **Voice:** an optional voice model he says runs locally ([25:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1517s)).
- **How he suggests building it:** give Claude Code a screenshot of a site you like, your list of skills, the vault connection and the metrics you want ([26:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1594s), [26:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1599s)). He doesn't show his own build.
- **Obsidian variant:** a command center inside Obsidian showing token burn, run buttons and tabs ([25:39](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1539s), [25:49](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1549s)). He suggests asking Claude Code to turn the web app into a plugin ([27:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1623s)).
- **Mechanism:** a button calls headless Claude Code through `claude -p` ([27:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1634s)–[27:48](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1668s)).

**Chase's earlier dashboard** ([[Chase AI - The Three-Step Claude Code Agentic OS]]), where observability is one of three steps:
- **Buttons that take an input.** The deep research button fills in its prompt and asks for one input, the same as typing that prompt into Claude Code ([13:23](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=803s)). Run starts a hidden headless instance with `-p` ([13:42](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=822s)), and the write-up links its sources and the report's place in Obsidian ([15:35](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=935s)).
- **Observability panels:** 5-hour and weekly usage windows and routines used today ([14:54](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=894s)), plus recent vault changes and forecasts ([15:01](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=901s)). They can show anything, but ideally tie back to your skills ([15:10](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=910s)); choose them by asking what you wish the terminal showed you ([15:14](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=914s)).
- **Placeholder-first scaffolding.** His dashboard prompt starts with placeholders, then a conversation about which skills to wire in and what you want to observe ([15:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=947s)–[15:57](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=957s)).
- **Who the buttons are for:** teammates and clients. Fluent terminal users gain little ([14:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=840s), [14:18](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=858s)).

**Jack Roberts's design OS** ([[Jack Roberts - Design Systems, Critic Loops and a Design OS]]), a module inside his own Claude Code OS ([13:35](https://www.youtube.com/watch?v=NAumQObJEwM&t=815s)):
- **Multi-provider generation panel.** Pick a platform (Higgsfield, Kie AI, OpenRouter, OpenAI) ([13:49](https://www.youtube.com/watch?v=NAumQObJEwM&t=829s)), then aspect ratio, resolution, image count and model ([14:07](https://www.youtube.com/watch?v=NAumQObJEwM&t=847s)).
- **Cost on screen.** The panel shows the credits or money each generation costs ([14:18](https://www.youtube.com/watch?v=NAumQObJEwM&t=858s)). Two 2K images in a saved style were quoted at 12 cents ([16:51](https://www.youtube.com/watch?v=NAumQObJEwM&t=1011s)).
- **Also in the module:** saved style recipes, and a searchable library of every image and video on the machine ([16:09](https://www.youtube.com/watch?v=NAumQObJEwM&t=969s), [15:05](https://www.youtube.com/watch?v=NAumQObJEwM&t=905s)).
- **The wider OS** has a dashboard showing usage and spend ([14:44](https://www.youtube.com/watch?v=NAumQObJEwM&t=884s)). He shows no code. See [[Generating Images and Video with Claude]].

## Prerequisites

- **Skills that already produce good output in a normal session.** Chase wants a task done by hand and confirmed before it becomes a skill ([07:20](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=440s)). See [[Workflow Audit into Skills]] and [[Build a Skill from a Successful Run]].
- **A workspace the agent can navigate,** such as a CLAUDE.md router ([12:23](https://www.youtube.com/watch?v=8NSyI-npJCU&t=743s)) or a vault CLAUDE.md with a navigation pattern ([21:50](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1310s)). See [[CLAUDE.md as a Router]] and [[Agent Memory Patterns]].
- **Claude Code installed and logged in** on the machine that will run the buttons.
- **Node.js 20 or newer,** for the vault starter server; it has no npm dependencies.
- **A decision about each skill's side effects.** Is it read-only? Does it write files? Does it touch email, messages or money? See [[Permissions and Approval Gates]].

## Steps

*Vault starter method. The architecture, flags and security choices are this vault's, checked against the docs under Beyond the source.*

1. **Pick three to five buttons.**
   - Choose skills you trigger by hand often and that finish in a few minutes.
   - Label each one: read-only, writes files, or has external effects.
   - Anything that would send messages or delete things stays off the dashboard, or becomes draft-only (Chase's inbox brief writes drafts ([24:19](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1459s))).
2. **Prove each skill headless before building any UI.**
   - From the workspace folder, run the skill with the exact flags the button will use (see *Starter files*).
   - Watch for `permission_denied` events.
   - Add only the tools the skill genuinely needs, then re-run until it finishes cleanly.
3. **Write `skills.json`.** One entry per button: `id`, `label`, the slash-command `prompt`, `permissionMode`, `allowedTools`, `maxTurns` and `timeoutMinutes`.
   - The page only ever sends an `id`. It never sends prompt text.
4. **Add `server.mjs` and `index.html`** from *Starter files* to a `dashboard/` folder (or its own repo).
   - Start it with `OS_WORKSPACE=/path/to/workspace node server.mjs` and open the URL it prints. The token is in the part of the URL after `#`.
5. **Click each button once.**
   - Confirm that `runs/<skill>/<timestamp>.json` appears in the workspace, with exit code `0` and the result text.
   - These logs are also what a later improvement loop reads ([22:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1350s)); see [[Loop Engineering]].
6. **Add panels that read files, not live APIs.**
   - Recent runs are already there.
   - Add a "latest outputs" list over your reports or artifacts folder, a simple version of Jay E's artifacts ring.
   - For live data such as calendar or inbox counts, have a skill fetch it through a connector and write a small JSON snapshot that the panel reads. The page then never holds API keys. See [[Connecting Claude to External Tools]] and [[Context vs Connections]].
   - **Chase's observability set, from local files** *(vault starter method)*:
     - *Usage windows:* a status line script saves the 5-hour and weekly usage to a JSON file (starter below). Add a token-checked `GET /api/usage` route that returns that file.
     - *Routines used today:* count today's files under `runs/` and in your routine output folder.
     - *Recent vault changes:* the ten most recently modified `.md` files in the vault, or `git log --since=midnight --name-only` if the vault is versioned.
7. **Add a routines panel, if you schedule work.**
   - Have scheduled runs save their outputs where the dashboard can list them. Jay E's daily YouTube-to-newsletter routine drops its drafts into his OS for review ([15:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=927s)).
   - Desktop local tasks keep their prompt in a per-task folder, but not their schedule (see *Beyond the source*). A panel can list the task names; keep the schedule list next to them by hand.
   - See [[Schedule Recurring Claude Tasks]].
8. **Style it last.** Hand Claude Code the starter files plus a screenshot of a layout you like, as Chase suggests ([26:34](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1594s)), using the starter prompt below. Keep the security checks unchanged.
   - Or start placeholder-first with the prompt below, as Chase's earlier video does ([15:47](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=947s)).
9. **Run the Done-when checks,** then use the dashboard for a week before adding more buttons.

### Security checklist

- **Loopback only.** The server binds `127.0.0.1`, never `0.0.0.0`. If you need runs while you're away, use a cloud routine instead of opening a port (see *Variations*).
- **Host header allowlist.** Reject any request whose `Host` isn't `127.0.0.1:<port>` or `localhost:<port>`. This blocks DNS-rebinding attacks from web pages you visit.
- **A token on every API call,** sent in a custom header, with no CORS headers. Other sites' pages then can't trigger runs.
- **No shell and no free text.** Spawn `claude` with an argument array. The prompt comes from `skills.json`, never from the request.
- **Narrow permissions for each skill.** Use `dontAsk` plus a short `--allowedTools` list. Never use `bypassPermissions` on a button. See [[Configure Safe Autonomy Permissions]].
- **A trusted folder only.** A `-p` run loads that folder's hooks and MCP servers without asking.
- **Caps.** One run at a time, `--max-turns`, and a process timeout.
- **No secrets or client data in the dashboard repo.** Keep `runs/` out of anything you share if reports contain client material.
- **If a button takes input** (Chase's pattern), that skill is the one exception to "no free text". Cap the length, strip control characters, and give the skill only read tools plus its report folder, because typed text can still try to steer Claude.

## Starter files & prompts

*Vault starter content: original, not from either video. Check flags against the current CLI reference before relying on them.*

**Headless smoke test for one skill** (step 2):

```bash
cd /path/to/workspace
claude -p "/morning-brief" --output-format stream-json --verbose \
  --permission-mode dontAsk --allowedTools "Edit(reports/**)" --max-turns 30 \
  | grep -E 'permission_denied|"type":"result"'
```

**`skills.json`.** The tool names are placeholders. `Edit(...)` rules cover every file-writing tool, and reads inside the working folder need no rule in `dontAsk` mode.

```json
[
  {
    "id": "morning-brief",
    "label": "Morning brief",
    "prompt": "/morning-brief",
    "permissionMode": "dontAsk",
    "allowedTools": ["Edit(reports/**)", "mcp__calendar__list_events"],
    "maxTurns": 30,
    "timeoutMinutes": 10
  },
  {
    "id": "content-audit",
    "label": "Content audit",
    "prompt": "/content-audit",
    "permissionMode": "dontAsk",
    "allowedTools": ["Edit(reports/**)"],
    "maxTurns": 40,
    "timeoutMinutes": 20
  }
]
```

**`server.mjs`** (Node 20+, no dependencies):

```js
// Local-only backend: serves index.html and runs allowlisted skills via headless Claude Code.
import http from "node:http";
import { spawn } from "node:child_process";
import { readFile, writeFile, mkdir, readdir } from "node:fs/promises";
import { randomBytes } from "node:crypto";
import path from "node:path";

const HOST = "127.0.0.1";                          // loopback only
const PORT = Number(process.env.OS_PORT || 4777);
const WORKSPACE = path.resolve(process.env.OS_WORKSPACE || ".");
const TOKEN = randomBytes(24).toString("hex");     // new token on every start
const here = (f) => new URL(f, import.meta.url);
const skills = JSON.parse(await readFile(here("./skills.json"), "utf8"));
const MODELS = ["haiku", "sonnet", "opus"];        // add "fable" or full model names if you use them
const EFFORTS = ["low", "medium", "high"];         // CLI also accepts xhigh, max, ultracode
let running = null;                                // one run at a time

const send = (res, status, body, type = "application/json") => {
  res.writeHead(status, { "Content-Type": type, "Cache-Control": "no-store" });
  res.end(typeof body === "string" || Buffer.isBuffer(body) ? body : JSON.stringify(body));
};

function runSkill(skill, model, effort) {
  const args = ["-p", skill.prompt, "--output-format", "json",
    "--model", model, "--effort", effort,
    "--permission-mode", skill.permissionMode || "dontAsk",
    "--max-turns", String(skill.maxTurns || 25)];
  if (skill.allowedTools?.length) args.push("--allowedTools", skill.allowedTools.join(","));
  return new Promise((resolve) => {
    const child = spawn("claude", args, {           // argument array, no shell
      cwd: WORKSPACE, stdio: ["ignore", "pipe", "pipe"],
      timeout: (skill.timeoutMinutes || 15) * 60_000,
    });
    let out = "", err = "";
    child.stdout.on("data", (d) => (out += d));
    child.stderr.on("data", (d) => (err += d));
    child.on("error", (e) => resolve({ code: -1, out, err: String(e) }));
    child.on("close", (code) => resolve({ code, out, err }));
  });
}

async function recentRuns(limit = 20) {
  const rows = [];
  for (const s of skills) {
    const files = await readdir(path.join(WORKSPACE, "runs", s.id)).catch(() => []);
    for (const f of files) if (f.endsWith(".json")) rows.push({ skill: s.id, file: f });
  }
  return rows.sort((a, b) => b.file.localeCompare(a.file)).slice(0, limit);
}

http.createServer(async (req, res) => {
  try {
    if (![`${HOST}:${PORT}`, `localhost:${PORT}`].includes(req.headers.host)) return send(res, 403, { error: "host" });
    const url = new URL(req.url, `http://${req.headers.host}`);
    if (req.method === "GET" && url.pathname === "/") return send(res, 200, await readFile(here("./index.html")), "text/html");
    if (req.headers["x-os-token"] !== TOKEN) return send(res, 401, { error: "token" });

    if (req.method === "GET" && url.pathname === "/api/state") {
      return send(res, 200, { running, models: MODELS, efforts: EFFORTS,
        skills: skills.map(({ id, label }) => ({ id, label })), runs: await recentRuns() });
    }
    if (req.method === "GET" && url.pathname === "/api/report") {
      const skill = skills.find((s) => s.id === url.searchParams.get("skill"));
      const file = path.basename(url.searchParams.get("file") || "");   // blocks path traversal
      if (!skill || !file.endsWith(".json")) return send(res, 404, { error: "not found" });
      return send(res, 200, await readFile(path.join(WORKSPACE, "runs", skill.id, file), "utf8"));
    }
    if (req.method === "POST" && url.pathname === "/api/run") {
      if (running) return send(res, 409, { error: `busy with ${running}` });
      let raw = "";
      for await (const chunk of req) raw += chunk;
      const { skill: id, model, effort } = JSON.parse(raw || "{}");
      const skill = skills.find((s) => s.id === id);
      if (!skill || !MODELS.includes(model) || !EFFORTS.includes(effort)) return send(res, 400, { error: "bad request" });
      running = skill.id;
      send(res, 202, { started: skill.id });
      const stamp = new Date().toISOString().replace(/[:.]/g, "-");
      try {
        const r = await runSkill(skill, model, effort);
        let parsed = null;
        try { parsed = JSON.parse(r.out); } catch {}
        const dir = path.join(WORKSPACE, "runs", skill.id);
        await mkdir(dir, { recursive: true });
        await writeFile(path.join(dir, `${stamp}.json`), JSON.stringify(
          { skill: skill.id, model, effort, exitCode: r.code, result: parsed ?? r.out, stderr: r.err.slice(-4000) }, null, 2));
      } finally { running = null; }
      return;
    }
    send(res, 404, { error: "not found" });
  } catch (e) {
    if (!res.headersSent) send(res, 500, { error: String(e) });
  }
}).listen(PORT, HOST, () => console.log(`Open http://${HOST}:${PORT}/#${TOKEN}`));
```

**`index.html`.** A plain page for Claude Code to restyle later. It writes report text with `textContent`, so report content can't inject markup.

```html
<meta charset="utf-8"><title>Command center</title>
<style>body{font:14px system-ui;margin:2rem;max-width:60rem} button{margin:.25rem} pre{white-space:pre-wrap;background:#f4f4f4;padding:1rem}</style>
<h1>Command center</h1>
<label>Model <select id="model"></select></label>
<label>Effort <select id="effort"></select></label>
<div id="skills"></div><p id="status"></p>
<h2>Recent runs</h2><ul id="runs"></ul><pre id="report"></pre>
<script>
const $ = (s) => document.querySelector(s), token = location.hash.slice(1);
const api = (p, o = {}) => fetch(p, { ...o, headers: { "x-os-token": token, "Content-Type": "application/json" } }).then((r) => r.json());
const fill = (el, vals) => el.replaceChildren(...vals.map((v) => new Option(v, v)));
async function refresh() {
  const s = await api("/api/state");
  if (!$("#model").options.length) { fill($("#model"), s.models); fill($("#effort"), s.efforts); }
  $("#status").textContent = s.running ? `Running: ${s.running}` : "Idle";
  $("#skills").replaceChildren(...s.skills.map((k) => {
    const b = document.createElement("button");
    b.textContent = k.label; b.disabled = !!s.running;
    b.onclick = () => api("/api/run", { method: "POST",
      body: JSON.stringify({ skill: k.id, model: $("#model").value, effort: $("#effort").value }) }).then(refresh);
    return b;
  }));
  $("#runs").replaceChildren(...s.runs.map((r) => {
    const li = document.createElement("li"), a = document.createElement("a");
    a.href = "#" + token; a.textContent = `${r.file.slice(0, 19)}  ${r.skill}`;
    a.onclick = async (e) => {
      e.preventDefault();
      const rep = await api(`/api/report?skill=${encodeURIComponent(r.skill)}&file=${encodeURIComponent(r.file)}`);
      $("#report").textContent = rep.result?.result ?? JSON.stringify(rep, null, 2);
    };
    li.append(a); return li;
  }));
}
refresh(); setInterval(refresh, 5000);
</script>
```

**Starter prompt: choose dashboard-safe skills** (vault starter wording):

> List every skill in this workspace. For each one, read its SKILL.md and any files it references, then tell me which tools and connectors it uses and whether it writes files, sends anything outside this machine, deletes anything or spends money. Propose a skills.json entry for each skill that is safe to run unattended, with the narrowest allowedTools list that would still let it finish. Mark every other skill as not dashboard-safe and say why. Don't change any files.

**Starter prompt: style the page** (vault starter wording):

> Restyle dashboard/index.html to match the attached screenshot. Keep server.mjs's host check, token check, loopback binding and skills allowlist exactly as they are, add no npm dependencies and add no CORS headers. Add two panels that read only from files on disk: the newest ten files in reports/, and a list of the task folders in my scheduled-tasks directory. When you're done, show me curl commands that prove requests with a wrong Host header or no token are refused.

**Starter prompt: placeholder-first scaffold** (vault starter wording):

> Build a first version of dashboard/index.html with placeholder panels and no live data. Then interview me one question at a time: which skills here should get a button, which of those need a text input, and what I want to see that the terminal doesn't show me. After each answer, replace one placeholder with a real button or a panel that reads a file on disk. Keep server.mjs's security checks unchanged.

**Status line snapshot for the usage panel** (vault starter; needs `jq`). Save as `~/.claude/statusline-usage.sh`, make it executable, and add `"statusLine": {"type": "command", "command": "~/.claude/statusline-usage.sh"}` to `~/.claude/settings.json`:

```bash
#!/bin/bash
# Shows 5h/7d usage and saves the rate-limit windows for the dashboard.
input=$(cat)
out="$HOME/.claude/os-usage.json"
if echo "$input" | jq -e '.rate_limits' >/dev/null 2>&1; then
  echo "$input" | jq '{saved_at: (now | floor), rate_limits}' > "$out.tmp" && mv "$out.tmp" "$out"
fi
echo "$input" | jq -r '"5h \(.rate_limits.five_hour.used_percentage // "-")% | 7d \(.rate_limits.seven_day.used_percentage // "-")%"'
```

**Buttons that take one input** (vault starter patch to `server.mjs`). Give the skill entry `"input": {"label": "Topic", "maxLength": 200}`, have `runSkill` take the final prompt as a fourth argument (`["-p", prompt, ...]`), and return `input: s.input?.label` in `/api/state` so the page can draw a text box. Then, in `POST /api/run`:

```js
const { skill: id, model, effort, input = "" } = JSON.parse(raw || "{}");
// ...existing skill/model/effort check...
let prompt = skill.prompt;
if (skill.input) {
  const text = String(input).replace(/[\x00-\x1f\x7f]/g, " ").trim();
  if (!text || text.length > (skill.input.maxLength || 200)) return send(res, 400, { error: "bad input" });
  prompt = `${skill.prompt} ${text}`;          // still one argument, no shell
}
// ...then: const r = await runSkill(skill, model, effort, prompt);
```

## Done when

- [ ] Every button's skill has produced a good result in a normal interactive session.
- [ ] The step-2 smoke test for each skill ends with a `result` event and no denials for tools the skill needs.
- [ ] `lsof -nP -iTCP:4777 -sTCP:LISTEN` shows only `127.0.0.1:4777`.
- [ ] `curl -s -o /dev/null -w "%{http_code}\n" -H "Host: attacker.example" http://127.0.0.1:4777/` prints `403`.
- [ ] `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:4777/api/state` prints `401`.
- [ ] Each button writes `runs/<skill>/<timestamp>.json` with exit code `0`, and the report opens from the page.
- [ ] Clicking a second button mid-run returns "busy" instead of starting a parallel run.
- [ ] A skill that tries a tool outside its list is denied and still finishes. It doesn't stall.
- [ ] No API keys, tokens or client data are committed with the dashboard.
- [ ] With the server stopped, every skill still works from the terminal. The dashboard is a layer, not a dependency ([13:00](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=780s)).

## Pitfalls

*Items with timestamps come from the videos. The rest are vault guidance, and the doc facts behind them are under Beyond the source.*

- **Building the UI before the skills.** Both creators warn against this ([04:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=267s), [30:30](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1830s)). A button over an unreliable skill just makes failures faster.
- **Mistaking visuals for value.** Chase describes viewers either dazzled by dashboards or dismissing them as smoke and mirrors, and says both miss the fundamentals underneath ([01:05](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=65s), [01:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=82s)).
- **Using `--bare` to "speed it up".** It skips skills and CLAUDE.md and needs an API key instead of your subscription login.
- **Loosening permissions until runs stop failing.** A `-p` run starts in Manual mode, so unapproved tools get denied. Add specific tools, not `bypassPermissions`.
- **Exposing the server** by binding `0.0.0.0` or adding `Access-Control-Allow-Origin: *` so a phone can reach it.
- **Unreviewed side effects.** Keep email and messaging buttons draft-only. Don't wire up a skill built from a random post that runs system commands you haven't read. Jay E's cleanup skill came from a post on X ([06:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=374s)); review anything like that line by line first.
- **Forgetting the usage cost.** Every click is a full Claude Code session drawing on your plan. Chase notes the billing for `claude -p` has already been in flux ([27:51](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1671s)).
- **Timeouts that are too tight.** When the process timeout fires, Node sends SIGTERM. Claude Code then exits with code 143 and records no result for that turn, so the run log holds only stderr. Set `timeoutMinutes` well above a normal run.
- **Using a button where a schedule belongs.** If something should happen every morning, make it a routine and let the dashboard show the result. See [[Routines and Scheduled Tasks]].

## Variations

*Items with timestamps come from the videos. The rest are vault additions, checked under Beyond the source.*

- **Jay E's micro-apps.** Besides the dashboard, he links small apps Claude built for him. One shows image and video generations in a masonry grid, and another is a landing pad for reusing illustration artifacts ([20:30](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1230s)–[20:51](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1251s)).
- **Jay E's widget grid.** Ask Claude Code for resizable, rearrangeable widgets ([01:29](https://www.youtube.com/watch?v=8NSyI-npJCU&t=89s)):
  - an artifacts ring that searches past outputs by client and date ([01:40](https://www.youtube.com/watch?v=8NSyI-npJCU&t=100s))
  - a routines board ([01:11](https://www.youtube.com/watch?v=8NSyI-npJCU&t=71s))
  - a link into your visual second brain ([02:02](https://www.youtube.com/watch?v=8NSyI-npJCU&t=122s))
- **Chase's Obsidian command center.** Ask Claude Code to port the web app into an Obsidian plugin ([27:03](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1623s)).
  - Because the plugin spawns `claude`, it needs Node APIs and so works on desktop only.
  - Build it in a separate test vault first (see *Beyond the source*).
- **Voice.** Chase adds a local voice model so you can speak commands and hear results ([25:17](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1517s)). The model is never named.
- **A generation panel with cost display,** like Jack Roberts's (see *What the sources built*). *Vault starter approach:* wrap each provider in a skill that reports the provider's stated cost in its result, cap images per run inside the skill (`--max-budget-usd` limits only Claude's own spend), and log provider, model and cost in `runs/` for a spend panel. See [[Generate On-Brand Images from Claude Code]] and [[Higgsfield]].
- **Cloud buttons.** Point a button at a cloud routine's API trigger instead of local `claude -p`.
  - It runs with your laptop closed, from a fresh repo clone with no local files.
  - Keep that routine's bearer token server-side.
- **Hand it to a team or clients.**
  - Chase shares web builds as a GitHub repo or zip ([29:01](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1741s)) and sets up Obsidian builds per person ([29:21](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1761s)). Jay E builds dashboard mockups for clients ([02:27](https://www.youtube.com/watch?v=8NSyI-npJCU&t=147s)).
  - *Vault addition:* ship the repo with `skills.json` and a README, but not `runs/`. Each person logs in to Claude Code with their own account.
- **Other harnesses.** Both creators say the approach carries over to Codex ([10:14](https://www.youtube.com/watch?v=8NSyI-npJCU&t=614s), [01:38](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=98s)). The flags in this note are Claude Code's only. See [[OpenAI Codex]].

## Beyond the source

*None of this is said in any of the videos. Checked at the linked pages on 2026-09-15.*

- **`claude -p` behaviour this starter relies on.**
  - **Skills:** `/skill-name` in the prompt runs that skill.
  - **Output:** `--output-format json` returns the `result`, session ID and an estimated `total_cost_usd`. `stream-json` emits `permission_denied` messages.
  - **Permissions:**
    - Runs start in Manual mode.
    - `--allowedTools` uses permission-rule syntax.
    - In `dontAsk` mode, anything that would prompt is denied. Reads inside working directories and allowlisted tools still run.
  - **Trust:** without `--bare`, the folder's `.claude/settings.json` hooks and `.mcp.json` servers load with no trust dialog.
  - **`--bare`** skips skills, CLAUDE.md and MCP discovery, and needs `ANTHROPIC_API_KEY`.
  - **Other flags:** `--model` aliases include `haiku`, `sonnet`, `opus` and `fable`. `--effort` accepts `low`, `medium`, `high`, `xhigh`, `max` and `ultracode`, though which levels are available depends on the model. `--allowedTools` takes one comma-separated string, as the server does, or several space-separated arguments.
  - **Stopping a run:** a `claude -p` run stopped with SIGTERM exits with code 143 and records no result for the unfinished turn. `--max-turns`, `--max-budget-usd` and `--no-session-persistence` are print-mode options.
  - Sources: [Headless docs](https://code.claude.com/docs/en/headless), [CLI reference](https://code.claude.com/docs/en/cli-reference)
- **Usage windows in the status line.**
  - A status line command receives session JSON on stdin. `rate_limits.five_hour` and `rate_limits.seven_day` each carry `used_percentage` (0–100) and `resets_at` (Unix seconds).
  - The object appears only for Claude.ai Pro and Max subscribers (or behind a gateway that sets a spend limit), and only after the session's first API response. Either window can be missing.
  - The script runs at session start, after each assistant message, on a few other events, and on a timer if you set `refreshInterval`. The snapshot is therefore only as fresh as your last interactive session *(vault inference: the docs don't say headless runs update it)*.
  - Source: [Status line](https://code.claude.com/docs/en/statusline)
- **Permission rule syntax.**
  - Path rules are checked only as `Edit(path)` and `Read(path)`. A `Write(...)` path rule is never consulted, and `Edit` covers all file-editing tools.
  - `Edit(reports/**)` is relative to the current directory.
  - MCP tools are named `mcp__<server>__<tool>`, and `mcp__<server>__*` covers a whole server.
  - Source: [Permissions](https://code.claude.com/docs/en/permissions)
- **Billing.** Anthropic paused its planned move of `claude -p` and Agent SDK usage to a separate credit. As of the help article's June 2026 update, this usage still draws on subscription limits. Source: [Claude Help Center](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- **Scheduled tasks and routines.**
  - **Local Desktop tasks:**
    - They fire only while the app is open and the computer awake.
    - Each keeps its prompt at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`. Schedule, folder, model and enabled state are not stored in that file.
  - **Cloud routines:**
    - They run with the computer off, from a fresh clone.
    - They can be started by POSTing to a per-routine `/fire` endpoint with a bearer token. That endpoint is in research preview behind a beta header.
  - Sources: [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Routines](https://code.claude.com/docs/en/routines)
- **Localhost is reachable from the browser.**
  - DNS rebinding and loose CORS let web pages reach local servers.
  - GitHub Security Lab recommends validating the Host header, avoiding wildcard CORS and requiring auth tokens.
  - Sources: [GitHub Blog, 2025-04-03](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/), [NCC Group Singularity wiki](https://github.com/nccgroup/singularity/wiki/Preventing-DNS-Rebinding-Attacks)
- **Spawning safely.** Node warns never to pass unsanitised input to a shell. `spawn` without `shell` passes arguments as an array with no shell interpretation, and supports a `timeout` option. Source: [Node.js child_process](https://nodejs.org/api/child_process.html)
- **Obsidian plugins.**
  - A plugin lives in `.obsidian/plugins/<id>/` with `manifest.json` and a compiled `main.js`, and is enabled under Settings → Community plugins.
  - Set `isDesktopOnly: true` when it uses Node.js or Electron APIs.
  - Obsidian advises developing in a separate vault.
  - Sources: [Build a plugin](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin), [Manifest reference](https://docs.obsidian.md/Reference/Manifest)

## Sources

- [[Jay E - The ARMS Framework for a Claude Agentic OS]]:
  - command-center widgets ([00:43](https://www.youtube.com/watch?v=8NSyI-npJCU&t=43s)–[02:08](https://www.youtube.com/watch?v=8NSyI-npJCU&t=128s))
  - the 20–30% value estimate ([03:35](https://www.youtube.com/watch?v=8NSyI-npJCU&t=215s))
  - headless skill runs ([09:04](https://www.youtube.com/watch?v=8NSyI-npJCU&t=544s)–[10:24](https://www.youtube.com/watch?v=8NSyI-npJCU&t=624s))
  - the dashboard as a self-built app ([20:26](https://www.youtube.com/watch?v=8NSyI-npJCU&t=1226s))
- [[Chase AI - The Agentic OS Setup for Claude Code]]:
  - Level 3 web app and Obsidian plugin ([23:24](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1404s)–[27:12](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1632s))
  - `claude -p` under the hood ([27:14](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1634s)–[28:13](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1693s))
  - distribution ([28:37](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1717s)–[30:22](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=1822s))
- [[Chase AI - The Three-Step Claude Code Agentic OS]]:
  - buttons with an input and headless runs ([13:23](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=803s)–[13:42](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=822s))
  - observability panels and the placeholder-first build ([14:00](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=840s)–[16:09](https://www.youtube.com/watch?v=Bgxsx8slDEA&t=969s))
- [[Jack Roberts - Design Systems, Critic Loops and a Design OS]]: design OS generation panel, cost display and asset library ([13:35](https://www.youtube.com/watch?v=NAumQObJEwM&t=815s)–[17:30](https://www.youtube.com/watch?v=NAumQObJEwM&t=1050s))

## Related

- [[Agentic OS]], [[Agent Skills]], [[Agent Memory Patterns]], [[Routines and Scheduled Tasks]]
- [[Configure Safe Autonomy Permissions]], [[Permissions and Approval Gates]], [[Schedule Recurring Claude Tasks]], [[Connecting Claude to External Tools]]
- [[Workflow Audit into Skills]], [[Build a Skill from a Successful Run]], [[Loop Engineering]]
- [[Claude Code]], [[Obsidian]], [[OpenAI Codex]], [[Jay E]], [[Chase AI]], [[Jack Roberts]], [[Higgsfield]]
