---
type: technique
goal: "Before work starts, write every required outcome into a GATES.md ledger with a runnable check, the output it must produce and an evidence line, so that a checker other than the worker decides when the task is done."
difficulty: intermediate
time_to_build: "About 30 minutes for the template, CLAUDE.md rule and checker, plus about an hour for the Stop hook and the orchestrated variant (vault estimate, not from the video)"
sources: ["[[AI LABS - The Unlazy Skill for Lazy Agents]]", "[[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]"]
tools: ["[[Claude Code]]", "[[OpenAI Codex]]", "[[Unlazy]]"]
tags: [topic/verification, topic/loops, topic/subagents, topic/planning, topic/claude-code, topic/agents]
---

# Evidence-Gated Completion Ledger

## Goal

A check should prove "done"; the agent's word shouldn't be enough. Before any real work, write a ledger (`GATES.md`) that lists every outcome the task needs. Each outcome gets three lines:

- **CHECK:** a command that proves it
- **EXPECT:** the words that command must print
- **EVIDENCE:** starts as `pending`

Something other than the worker runs the commands and fills in the evidence. That can be a script, the parent agent or a verifier subagent. The worker never ticks a box.

The idea comes from [[Unlazy]], as [[AI LABS - The Unlazy Skill for Lazy Agents]] describes it: prove completion against a ledger instead of reporting it ([01:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=73s), [01:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=77s)), with no point where the agent decides it's done ([08:59](https://www.youtube.com/watch?v=c47uqR7XB_c&t=539s), [09:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=541s)).

This note makes the idea work without the skill. It supplies an original template, a CLAUDE.md rule, a tested ~100-line checker, a Stop hook, and a depth-tree variant for big builds.

- The general habit is [[Verification Before Done]].
- Lighter checks (screenshots, rubrics, reviewers) are in [[Build Verification into Every Task]].

## Use when

- **The task has several required parts, and a false "done" would cost you.** [[AI LABS - The Unlazy Skill for Lazy Agents]] names two failure modes:
  - **Claiming done when it isn't.** Claude Code opens a few of many files and reports it covered them all ([02:30](https://www.youtube.com/watch?v=c47uqR7XB_c&t=150s), [02:35](https://www.youtube.com/watch?v=c47uqR7XB_c&t=155s)).
  - **Quietly skipping the hard part.** It builds four of five parts, and the summary never mentions the gap ([03:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=182s), [03:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=193s)).

  The false claim is the expensive one. You only find out by checking, and meanwhile more work gets built on top ([02:44](https://www.youtube.com/watch?v=c47uqR7XB_c&t=164s), [02:57](https://www.youtube.com/watch?v=c47uqR7XB_c&t=177s)). See [[Agent Laziness]].
- **The session will be long.**
  - Laziness barely shows in a fresh context. It grows as the history resent each turn piles up ([01:52](https://www.youtube.com/watch?v=c47uqR7XB_c&t=112s), [02:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=137s), [02:22](https://www.youtube.com/watch?v=c47uqR7XB_c&t=142s)).
  - An instruction like "be thorough" is the first thing a long session loses ([07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s)).
- **Your current loop lets the agent, or its transcript, judge completion.** The video objects to three common setups:
  - **Ralph loop:** the finish line is text the agent writes ([03:46](https://www.youtube.com/watch?v=c47uqR7XB_c&t=226s)).
  - **`/goal`:** the judge reads the conversation, not the work ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)).
  - **Self-graded task lists:** the agent still decides ([04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s)).

  All three falter deep into real work ([04:16](https://www.youtube.com/watch?v=c47uqR7XB_c&t=256s)). See [[Loop Engineering]].
- **You want to fan a large build out to subagents.** Use the depth-tree variant (steps 10–15).

**Skip it** for one-line fixes, factual answers, and anything where writing the checks costs more than looking. That's a vault judgement, and Unlazy's own skill file says the same (see Beyond the source).

## Prerequisites

- **An agent that runs shell commands.** The video says Unlazy works with [[Claude Code]], [[OpenAI Codex]] and others ([01:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=87s)). The ledger itself is plain markdown.
- **Node.js 16 or newer** for the vault checker and hook below (tested on Node 20). Alternatively, install [[Unlazy]] and use its checker.
- **Commands that can prove your outcomes:** a test runner, type checker or build, or small `scripts/verify-*.mjs` files that exit non-zero on failure and print a success-only line.
- **Git**, so a failed or abandoned run is easy to roll back (vault).
- **For the orchestrated variant:** a harness that runs subagents in parallel. The video says Claude Code and Codex both can ([10:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=645s), [10:50](https://www.youtube.com/watch?v=c47uqR7XB_c&t=650s)).

## Steps

### Solo ledger (one session)

1. **Pick the mode.**
   - **Solo:** at tree depth 3 or less, Unlazy keeps everything in one session with one agent ([06:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=405s), [06:50](https://www.youtube.com/watch?v=c47uqR7XB_c&t=410s)).
   - **Orchestrated:** for a build at depth 4 or more, where every leaf is at least ten minutes of real work ([06:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=387s), [06:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=414s)).
   - **Rough depth:** 2–3 for a feature, 5 for an app from scratch ([11:23](https://www.youtube.com/watch?v=c47uqR7XB_c&t=683s), [11:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=689s)).
2. **List the outcomes before touching code.** Re-read the request and list every required outcome, especially the hard one that would be easiest to drop ([03:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=185s)). Prompt D has Claude draft the list; you edit it.
3. **Write `GATES.md` from template A.**
   - **Gate structure.** One gate per outcome: a checkbox and the outcome, then the proving command, the exact words it must return, and `EVIDENCE: pending` ([07:32](https://www.youtube.com/watch?v=c47uqR7XB_c&t=452s)–[07:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=467s)).
   - **Timing.** The file exists before work begins, because a file survives a long session where an instruction doesn't ([07:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=441s)).
   - **Manual gates.** If no command can decide an outcome, make it a manual gate that names the evidence it needs.
4. **Prove every check can fail (vault practice).** Before any implementation, run `node scripts/check-gates.mjs --run GATES.md`. Every runnable gate should come back UNMET. A gate that already passes measures nothing.
5. **Add the no-self-grading rule (starter B).**
   - **The rule.** The worker never ticks a box or edits EVIDENCE.
   - **Why.** A ticked box with pending evidence counts as unmet, and the video rates it worse than an empty box ([08:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=489s), [08:17](https://www.youtube.com/watch?v=c47uqR7XB_c&t=497s), [08:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=501s)).
   - **Optional lock.** In Claude Code you can also block edits to the ledger (starter G).
6. **Do the work.**
7. **Verify with something other than the worker.** You, a verifier subagent or the parent agent runs the checker (starter C).
   - **From the video:** it executes each CHECK, ticks the box when the output contains the expected words, and writes the deciding line into EVIDENCE ([07:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=471s)–[08:01](https://www.youtube.com/watch?v=c47uqR7XB_c&t=481s)).
   - **Vault additions:** the starter also requires exit code 0, and it re-runs gates that are already ticked.
8. **Abandon openly, never silently.** In the video, an impossible task gets a written line that gives up its gate by name with a reason, and that line goes into the final report ([08:47](https://www.youtube.com/watch?v=c47uqR7XB_c&t=527s), [08:53](https://www.youtube.com/watch?v=c47uqR7XB_c&t=533s), [08:55](https://www.youtube.com/watch?v=c47uqR7XB_c&t=535s)).
   - In this note's format (vault), keep the gate, add `ABANDON: <id> <reason>` at column 1, and lead the report with it.
   - The starter then exits 3 with `HANDOFF REQUIRED`, so nobody mistakes it for success.
   - Never delete, soften or reword a gate to get a pass.
9. **Report from the ledger.** Paste the checker's summary line from a run in this session, not from memory.

### Depth-tree variant (a fresh subagent per leaf)

10. **Plan, then gates, then build.**
    - Write `PLAN.md` (starter E), then the gates files, all before building. The video describes orchestrated mode as a plan file plus a separate checklist per task ([07:00](https://www.youtube.com/watch?v=c47uqR7XB_c&t=420s), [07:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=422s)), with the plan written first and the gates next ([11:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=700s), [11:43](https://www.youtube.com/watch?v=c47uqR7XB_c&t=703s)).
    - Adding an integration `GATES.md` for end-to-end checks on top of the per-leaf files is vault practice.
    - Give each leaf one clear goal, so its agent isn't carrying the rest of the job ([06:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=372s), [06:18](https://www.youtube.com/watch?v=c47uqR7XB_c&t=378s)).
11. **Brief each leaf narrowly.** A fresh subagent gets only the plan and its own gates file ([08:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=509s), [08:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=511s)). The leaf brief is in starter F.
12. **Re-verify every return in the parent.** When a leaf says it's finished, the parent runs that leaf's checks itself. Only then does it log a line in the plan and move on ([08:37](https://www.youtube.com/watch?v=c47uqR7XB_c&t=517s), [08:42](https://www.youtube.com/watch?v=c47uqR7XB_c&t=522s)).
13. **Dispatch in parallel, with file ownership.**
    - **What went wrong.** The shipped skill handed out one task and waited before the next. AI LABS got 3–4 hours of work and only a login page ([10:36](https://www.youtube.com/watch?v=c47uqR7XB_c&t=636s), [10:40](https://www.youtube.com/watch?v=c47uqR7XB_c&t=640s), [10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s), [10:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=656s)).
    - **Their fix.** The plan records which files each task owns, so concurrent agents don't overwrite each other. The foundation goes first, then the work fans out ([11:45](https://www.youtube.com/watch?v=c47uqR7XB_c&t=705s), [11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s), [11:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=716s)).
    - **Result.** Ten agents at once, a run of nearly two hours, and a working first version of the app ([12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s), [12:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=724s), [12:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=726s)).
    - **Rule (vault, matching Unlazy's current dispatch reference; see Beyond the source):** launch every ready leaf before waiting on any of them.
14. **Route leaves by difficulty.** Send mechanical leaves to a cheaper model and hard ones to a strong model, so a big fan-out doesn't hit your limits early ([12:15](https://www.youtube.com/watch?v=c47uqR7XB_c&t=735s), [12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s)). See [[Route Tasks to the Right Claude Model]].
15. **Integrate and close.** Once every leaf is VERIFIED or abandoned, run the integration `GATES.md` with `--run` and report the counts.

### Optional backstop

16. **Add the Stop hook (starter H)** so Claude can't end its turn while `GATES.md` has unmet gates. Its limits are under Pitfalls and Beyond the source.

## Starter files & prompts

*Vault starter content written for this note; nothing here is copied from the video or the Unlazy repo. The gate layout (checkbox, CHECK, EXPECT, EVIDENCE, ABANDON) follows the video's description. Starters C and H were run against test ledgers on Node 20 on 2026-09-15 (status, run, handoff, malformed, CRLF and timeout cases).*

### A. `GATES.md` template (save a copy as `docs/gates-template.md`)

```markdown
# Gates: <task name>

Scope: <one sentence describing the complete deliverable>

- [ ] G1: <observable outcome, e.g. "an expired reset token is refused">
  CHECK: <command that observes it, e.g. node scripts/verify-expired-token.mjs>
  EXPECT: <text only success prints, or a /regex/>
  EVIDENCE: pending

- [ ] G2: <next outcome>
  CHECK: <command>
  EXPECT: <success-only text>
  EVIDENCE: pending

- [ ] G3: <outcome no command can decide>
  EVIDENCE: pending
  <!-- manual gate: replace pending with a file path, count or quoted output, then tick it -->

<!--
Rules
- One outcome per gate, worded so a stranger could judge it.
- Ids are unique; CHECK, EXPECT and EVIDENCE are indented under their gate.
- A runnable gate has both CHECK and EXPECT. A manual gate has neither.
- EXPECT must be text that only success prints. "passed" alone also matches "0 passed".
- Only the checker ticks runnable gates. A tick above EVIDENCE: pending is unmet.
- For an impossible gate, keep it and add this line at column 1:
  ABANDON: G<n> <reason, and who owns it now>
-->
```

### B. CLAUDE.md rule

Keep it this short and let the files do the enforcing ([[Keep CLAUDE.md Lean]]):

```markdown
## Completion ledger
For any task with more than one required outcome or more than ~10 minutes of work:
1. Before changing anything, write GATES.md from docs/gates-template.md: one gate per required outcome, each with CHECK, EXPECT and `EVIDENCE: pending`. Show it to me and wait.
2. Run `node scripts/check-gates.mjs --run GATES.md` once before starting. Every runnable gate must fail; fix any that pass.
3. Never tick a gate or edit an EVIDENCE line yourself. Only the checker writes them.
4. Don't say "done" until the checker prints ALL MET in this session. Paste its summary line.
5. If a gate is impossible, tell me why. Once I agree, it gets `ABANDON: <id> <reason>` and leads your report. Never delete, weaken or reword a gate to get a pass.
```

### C. Checker: `scripts/check-gates.mjs`

| Command | What it does |
|---|---|
| `node scripts/check-gates.mjs GATES.md` | Status only: runs nothing and changes nothing. Lists unmet gates with their CHECK and EXPECT |
| `node scripts/check-gates.mjs --run GATES.md gates/leaf-1.1.md` | Runs every CHECK, including gates already ticked. Ticks or unticks each box and writes the evidence. Prints `ALL MET` only if everything passed |
| `--timeout=SECONDS` | Timeout per check; the default is 120 |

Exit codes: `0` all met · `1` unmet · `2` malformed ledger or bad usage · `3` handoff (only abandoned gates remain). CHECK lines are shell commands that run with your permissions, so read every one before `--run`, above all in ledgers you didn't write.

```js
#!/usr/bin/env node
// check-gates.mjs: vault starter checker for GATES.md ledgers (not Unlazy's gate-check.mjs).
// Status, runs nothing:  node scripts/check-gates.mjs GATES.md
// Verify, runs CHECKs:   node scripts/check-gates.mjs --run GATES.md gates/leaf-1.1.md
// Exit codes: 0 all met | 1 unmet gates | 2 malformed ledger or usage | 3 handoff (only abandoned gates left)
import { readFileSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
const run = args.includes('--run');
const tArg = args.find((a) => a.startsWith('--timeout='));
const timeoutMs = Number(tArg ? tArg.split('=')[1] : 120) * 1000;
const files = args.filter((a) => !a.startsWith('--'));
const die = (msg) => { console.error(msg); process.exit(2); };
if (!files.length || !(timeoutMs > 0)) die('usage: check-gates.mjs [--run] [--timeout=SECONDS] LEDGER.md ...');

const GATE = /^- \[([ xX])\] ([A-Za-z0-9._-]+): (\S.*)$/;
const ATTR = /^\s+(CHECK|EXPECT|EVIDENCE):[ \t]*(.*)$/;
const ABANDON = /^ABANDON: ([A-Za-z0-9._-]+) (\S.*)$/;
const FENCE = /^ {0,3}(`{3,}|~{3,})/;
const matches = (expect, text) => {
  const re = expect.match(/^\/(.+)\/([a-z]*)$/);
  return re ? new RegExp(re[1], re[2]).test(text) : text.includes(expect);
};
const setBox = (line, on) => line.replace(/^- \[[ xX]\]/, on ? '- [x]' : '- [ ]');
const setEvidence = (line, text) => line.replace(/EVIDENCE:.*$/, () => `EVIDENCE: ${text}`);

let met = 0, unmet = 0, abandoned = 0;
for (const file of files) {
  const raw = readFileSync(file, 'utf8');
  const eol = raw.includes('\r\n') ? '\r\n' : '\n';
  const lines = raw.split(/\r?\n/);
  const gates = [], abandons = new Map();
  let fenced = false, cur = null;
  lines.forEach((line, i) => {
    if (FENCE.test(line)) { fenced = !fenced; cur = null; return; }
    if (fenced) return;
    let m;
    if ((m = line.match(GATE))) gates.push((cur = { id: m[2], ticked: m[1] !== ' ', line: i }));
    else if (cur && (m = line.match(ATTR))) { cur[m[1]] = m[2].trim(); cur[`${m[1]}Line`] = i; }
    else if ((m = line.match(ABANDON))) abandons.set(m[1], m[2]);
  });

  if (!gates.length) die(`${file}: no gates found`);
  const ids = new Set();
  for (const g of gates) {
    if (ids.has(g.id)) die(`${file}: duplicate gate id ${g.id}`);
    ids.add(g.id);
    if (!('EVIDENCELine' in g)) die(`${file}: ${g.id} has no EVIDENCE line`);
    const hasCheck = 'CHECKLine' in g, hasExpect = 'EXPECTLine' in g;
    if (hasCheck !== hasExpect || (hasCheck && (!g.CHECK || !g.EXPECT))) {
      die(`${file}: ${g.id} needs a non-empty CHECK and EXPECT, or neither`);
    }
    try { if (hasCheck) matches(g.EXPECT, ''); } catch { die(`${file}: ${g.id} has an invalid EXPECT pattern`); }
    g.runnable = hasCheck;
  }
  for (const id of abandons.keys()) if (!ids.has(id)) die(`${file}: ABANDON names unknown gate ${id}`);

  for (const g of gates) {
    const tag = `${file}:${g.id}`;
    if (abandons.has(g.id)) { abandoned++; console.log(`ABANDONED ${tag}: ${abandons.get(g.id)}`); continue; }
    const pending = !g.EVIDENCE || /^pending$/i.test(g.EVIDENCE);
    if (!g.runnable) {
      const ok = g.ticked && !pending;
      ok ? met++ : unmet++;
      console.log(`${ok ? 'MET (manual)' : 'UNMET'} ${tag}${g.ticked && pending ? ' (ticked with no evidence: worse than an empty box)' : ''}`);
      continue;
    }
    if (!run) {
      const ok = g.ticked && g.EVIDENCE.startsWith('exit=0;');
      ok ? met++ : unmet++;
      console.log(ok ? `RECORDED ${tag}` : `UNMET ${tag}\n    CHECK:  ${g.CHECK}\n    EXPECT: ${g.EXPECT}`);
      continue;
    }
    const r = spawnSync(g.CHECK, { shell: true, encoding: 'utf8', timeout: timeoutMs, maxBuffer: 16 * 1024 * 1024 });
    const out = `${r.stdout ?? ''}\n${r.stderr ?? ''}`;
    if (r.status === 0 && matches(g.EXPECT, out)) {
      const hit = out.split(/\r?\n/).find((l) => matches(g.EXPECT, l)) ?? '(multi-line match)';
      lines[g.line] = setBox(lines[g.line], true);
      lines[g.EVIDENCELine] = setEvidence(lines[g.EVIDENCELine], `exit=0; matched "${hit.trim().slice(0, 160)}"; ${new Date().toISOString()}`);
      met++;
      console.log(`MET ${tag}`);
    } else {
      lines[g.line] = setBox(lines[g.line], false);
      lines[g.EVIDENCELine] = setEvidence(lines[g.EVIDENCELine], 'pending');
      unmet++;
      console.log(`UNMET ${tag} (exit ${r.status ?? r.signal ?? r.error?.code})`);
      console.log(out.trim().split(/\r?\n/).slice(-15).map((l) => `    ${l}`).join('\n'));
    }
  }
  if (run) writeFileSync(file, lines.join(eol));
}

const total = met + unmet + abandoned;
console.log(`\n${met}/${total} ${run ? 'met' : 'met or recorded'}, ${unmet} unmet, ${abandoned} abandoned`);
if (unmet) process.exit(1);
if (abandoned) { console.log('HANDOFF REQUIRED: list every abandoned gate and its reason in the report'); process.exit(3); }
console.log(run ? 'ALL MET' : 'ALL RECORDED (nothing was re-run; use --run to verify)');
process.exit(0);
```

### D. Prompt: draft the ledger

```text
Before writing any code, re-read my request and list every separate outcome it requires. Constraints count too, e.g. "don't change the public API". Then write GATES.md from docs/gates-template.md, one gate per outcome:
- Each CHECK must observe the outcome directly: run the test, call the endpoint, read the file. Where no command exists, write scripts/verify-<name>.mjs that exits non-zero on any failure and prints one success-only line.
- EXPECT is text that only success prints.
- Anything a command can't decide becomes a manual gate that says what evidence it needs.
Then run `node scripts/check-gates.mjs --run GATES.md`, confirm every runnable gate fails, and show me the ledger. Don't start the work until I approve it.
```

### E. `PLAN.md` for the depth-tree variant

```markdown
# Plan: <task>
Depth: tree <N>    Mode: orchestrated

## Contract (fixed before any leaf starts)
- Interfaces: <types, endpoints and schemas that leaves share>
- Conventions: <naming, error handling, file layout>
- Checks: <test and build commands, shell, Node version>

## Tree
- 1 <task> → GATES.md (integration: end-to-end and regression gates)
  - 1.0 foundation → gates/leaf-1.0.md
  - 1.1 <area>
    - 1.1.1 <leaf> → gates/leaf-1.1.1.md
    - 1.1.2 <leaf> → gates/leaf-1.1.2.md

## Dispatch table
| Leaf | Owns (only this leaf writes here) | Needs | Wave | Model | State |
|---|---|---|---|---|---|
| 1.0 foundation | package.json, src/types/** | – | 0 | strong | READY |
| 1.1.1 <leaf> | src/<a>/**, tests/<a>/** | 1.0 | 1 | cheap | WAITING |
| 1.1.2 <leaf> | src/<b>/**, tests/<b>/** | 1.0 | 1 | strong | WAITING |

States: WAITING → READY → IN-FLIGHT → VERIFIED (parent re-ran the checks) or ABANDONED.

## Status log (append only)
- <time> 1.0 VERIFIED: check-gates --run gates/leaf-1.0.md printed ALL MET
```

### F. Orchestrator prompt and leaf brief

```text
Build <feature or app> as a depth-tree run, tree <N>.
1. Write PLAN.md from docs/plan-template.md: contract, tree and dispatch table. Every leaf is at least ~10 minutes of real work and owns paths no other leaf owns. Shared setup is a wave-0 foundation leaf.
2. Write gates/leaf-<id>.md for every leaf and GATES.md for integration. Run the checker on each and confirm every runnable gate fails. Stop and show me the plan.
3. After I approve, do wave 0 yourself and verify it with --run.
4. For each wave, start every READY leaf as its own background subagent in one go, before waiting on any of them. Give each one only the leaf brief.
5. When a leaf returns, run `node scripts/check-gates.mjs --run gates/leaf-<id>.md` yourself. ALL MET means mark it VERIFIED and log it. Anything else means sending it back with the failing gate ids, or bringing me the abandonment.
6. Never run two leaves whose Owns overlap. If a leaf needs a file it doesn't own, stop and change the plan.
7. When every leaf is VERIFIED or abandoned, run GATES.md with --run and report met, unmet and abandoned counts.
```

```text
You are leaf <id>. This brief is everything you get: the contract from PLAN.md and your ledger, gates/leaf-<id>.md.
- Write only inside your Owns paths: <paths>.
- Work until `node scripts/check-gates.mjs --run gates/leaf-<id>.md` prints ALL MET. Don't tick boxes or edit EVIDENCE yourself.
- If a gate is impossible, stop and return the gate id and the reason.
- Reply in three lines: what you built, the checker's summary line, and anything the parent should check by hand.

<contract>
<gates file>
```

### G. Lock the ledger against Claude's edit tools (Claude Code, optional)

Add this to `.claude/settings.local.json` once the ledger is approved, then start the build session:

```json
{
  "permissions": {
    "deny": ["Edit(/GATES.md)", "Edit(/gates/**)"]
  }
}
```

Claude's edit tools can no longer touch the ledger, but the checker, a Node process, still can (see Beyond the source). Abandonments now have to come through you, which makes giving up a human decision. This stops casual hand-ticking. It isn't a security boundary.

### H. Stop hook backstop (Claude Code, optional)

`.claude/hooks/gates-stop.mjs`:

```js
// .claude/hooks/gates-stop.mjs: keeps Claude working while GATES.md has unmet gates.
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

process.chdir(process.env.CLAUDE_PROJECT_DIR ?? process.cwd());
if (!existsSync('GATES.md')) process.exit(0); // no ledger in play, nothing to enforce

const r = spawnSync(process.execPath, ['scripts/check-gates.mjs', 'GATES.md'], { encoding: 'utf8' });
if (r.status === 0 || r.status === 3) process.exit(0); // every gate recorded, or an honest handoff

process.stderr.write(
  `GATES.md is not finished:\n${`${r.stdout}${r.stderr}`.slice(-1500)}\n` +
  'Work the next unmet gate, then have the checker verify it with --run. ' +
  'If a gate is impossible, add an ABANDON line with the reason and report it.\n'
);
process.exit(2); // exit 2 blocks the stop; stderr goes back to Claude
```

`.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/gates-stop.mjs\"" }
        ]
      }
    ]
  }
}
```

The hook uses status mode, so it's fast and never executes CHECK lines. The trade-off is that it trusts whatever evidence the checker last recorded. Real verification is still the `--run` in step 7. If you also use starter G, the hook's ABANDON hint won't work, so the agent has to ask you instead.

## Done when

- [ ] `GATES.md` existed before the first code change, and every required outcome in the re-read request has a gate or an ABANDON line.
- [ ] Every runnable gate was seen failing before the work started.
- [ ] Each EXPECT is text only success prints, and each CHECK observes the outcome its title names.
- [ ] The CLAUDE.md rule is in place, and no `[x]` sits above `EVIDENCE: pending`.
- [ ] The final `--run` was executed by you, the parent or a verifier (not the worker) in this session. It printed `ALL MET`, or `HANDOFF REQUIRED` with every abandonment leading the report.
- [ ] **Orchestrated runs:**
  - [ ] The parent re-ran every leaf before marking it VERIFIED.
  - [ ] `PLAN.md` logs each verification.
  - [ ] No two in-flight leaves shared an Owns path.
- [ ] The met, unmet and abandoned counts in the report come from that last checker run.

## Pitfalls

- **Gates that can't be falsified.** The title says one thing and the CHECK measures another, e.g. `G1: invoices reconcile` with `CHECK: echo ok`. The checker only proves the command you wrote, so make the CHECK read the real artifact (vault; Unlazy's gate reference makes the same point).
- **Checks that pass trivially.**
  - EXPECT text that failures also print: "passed" appears inside "0 passed", and "ok" inside "not ok".
  - Absence checks (for example, a grep that finds no TODOs) that also pass when the path is wrong. Try them on a file that should fail.
  - Numbers copied from the brief into EXPECT instead of measured.
  - Exit codes ignored. The starter requires exit 0 *and* the match.

  Step 4, watching every gate fail first, catches most of these.
- **Trusting recorded evidence.** EVIDENCE is text in a file, and anyone, including the agent, can type something that looks right. Verifying means re-running with `--run`, not reading the ledger. Status mode and the Stop hook are only backstops.
- **Enforcing with instructions alone.** The video says a line telling the agent to be thorough is the first thing lost in a long session ([07:12](https://www.youtube.com/watch?v=c47uqR7XB_c&t=432s), [07:14](https://www.youtube.com/watch?v=c47uqR7XB_c&t=434s)). The file and the checker do the enforcing; the CLAUDE.md rule only points at them.
- **The worker grading itself.** Real checks graded by the agent that did the work still leave that agent deciding ([04:09](https://www.youtube.com/watch?v=c47uqR7XB_c&t=249s), [04:11](https://www.youtube.com/watch?v=c47uqR7XB_c&t=251s)). The `--run` that counts happens outside the worker.
- **Rewriting gates mid-task.** Deleting or softening the hard gate is the silent scope shrink again ([03:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=185s), [03:13](https://www.youtube.com/watch?v=c47uqR7XB_c&t=193s)). After approval, ledger changes go through you.
- **Running CHECK lines you didn't write.** They run with your credentials and network access. Read inherited ledgers before `--run`. See [[Permissions and Approval Gates]].
- **Leaves too small or trees too deep.** The video's rule is that a leaf must be at least ten minutes of real work, a proper piece an agent can finish alone; smaller leaves mean the depth is too high ([06:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=387s), [06:31](https://www.youtube.com/watch?v=c47uqR7XB_c&t=391s)). Start at depth 2–3 for a feature ([11:29](https://www.youtube.com/watch?v=c47uqR7XB_c&t=689s)).
- **Serial dispatch.** Handing out one leaf and waiting before sending the next is where AI LABS' hours went ([10:54](https://www.youtube.com/watch?v=c47uqR7XB_c&t=654s), [11:03](https://www.youtube.com/watch?v=c47uqR7XB_c&t=663s)).
- **Parallel leaves sharing files.** Without an ownership map, concurrent agents overwrite each other's work ([11:49](https://www.youtube.com/watch?v=c47uqR7XB_c&t=709s), [11:51](https://www.youtube.com/watch?v=c47uqR7XB_c&t=711s)). Move shared files into the foundation leaf, or give leaves separate worktrees ([[Parallel Sessions with Git Worktrees]]).
- **Whole-project checks in leaf ledgers.** Put end-to-end and regression gates in the integration `GATES.md`. Otherwise every leaf re-check runs the whole suite (vault; matches Unlazy's leaf-versus-branch rule).
- **Wide fan-outs cost a lot.** Ten agents running for two hours ([12:02](https://www.youtube.com/watch?v=c47uqR7XB_c&t=722s), [12:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=724s)) uses a lot of your plan's quota, so route mechanical leaves to cheaper models ([12:21](https://www.youtube.com/watch?v=c47uqR7XB_c&t=741s)).
- **Stop-hook nagging.** A ledger that can never pass makes the hook block repeatedly until Claude Code's block cap overrides it (see Beyond the source). Use an ABANDON line instead of letting it spin.

## Variations

- **Use Unlazy itself.** Its checker adds approval before commands run, evidence bound to the gate definition, a gate linter, ownership leases and parallel dispatch waves. See [[Unlazy]].
- **Solo only.** Skip steps 10–15. One `GATES.md` covers most feature work.
- **Tests as gates.** Write each gate's test before the code, then let the checker run it. See [[Tests-First Goal Loop]].
- **A `/goal` that reads the checker.** The evaluator then judges printed checker output rather than Claude's claims (why this works is under Beyond the source):

  ```text
  /goal `node scripts/check-gates.mjs --run GATES.md` prints ALL MET, or HANDOFF REQUIRED with every abandoned gate reported to me; `git diff GATES.md` shows only checkbox and EVIDENCE changes; or stop after 25 turns
  ```
- **Verifier subagent.** A subagent with no edit tools runs `--run` and reports back. See [[Build Verification into Every Task]] (starter F there) and [[Multi-Agent Review and Scoring Loops]].
- **Held-out checks.** In [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]], Ouroboros keeps how checks run and what they expect out of the builder's instructions ([07:58](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=478s)). Failures go back as fixes to that part, and the checks rerun so earlier work stays intact ([08:02](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=482s)–[08:11](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=491s)). Vault adaptation: keep the CHECK and EXPECT lines in a ledger the worker can't read, and have the checker report only failing gate IDs. This reverses the default here, where the worker writes its own gates. See [[Verification Before Done]] (row 6b).
- **Non-code deliverables.** Use manual gates with concrete evidence (a path, a count, a screenshot), or a rubric graded in a separate context ([[Build Verification into Every Task]]).
- **Codex.** The files are the same; put the rule in AGENTS.md instead of CLAUDE.md ([[Tool-Agnostic Context Files]], [[Port a Claude Code Brain to Other Agents]]).

## Sources

- [[AI LABS - The Unlazy Skill for Lazy Agents]] chapters:
  - why agents get lazy and why earlier loops fail ([01:48](https://www.youtube.com/watch?v=c47uqR7XB_c&t=108s)–[04:20](https://www.youtube.com/watch?v=c47uqR7XB_c&t=260s))
  - the depth tree and modes ([05:26](https://www.youtube.com/watch?v=c47uqR7XB_c&t=326s)–[07:04](https://www.youtube.com/watch?v=c47uqR7XB_c&t=424s))
  - the gates ledger, checker, parent verification and abandonment ([07:06](https://www.youtube.com/watch?v=c47uqR7XB_c&t=426s)–[09:05](https://www.youtube.com/watch?v=c47uqR7XB_c&t=545s))
  - serial versus parallel dispatch with file ownership ([10:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=627s)–[12:27](https://www.youtube.com/watch?v=c47uqR7XB_c&t=747s))
- [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]]: Ouroboros's held-out checks, the "Held-out checks" variation ([07:55](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=475s)–[08:11](https://www.youtube.com/watch?v=Ua0APTMVcb8&t=491s))

## Beyond the source

*Not from the video. Checked on 2026-09-15 at the linked pages.*

- **Unlazy's current gate contract** (source targets 2.1.0, unreleased):
  - A runnable gate passes only on exit 0 plus an EXPECT match.
  - `--status` never executes anything. A command with no approval record is only previewed until `--approve` runs it.
  - `--reverify` re-runs gates that are already ticked.
  - `ABANDON` exits 1 with `HANDOFF REQUIRED`.
  - Optional `CWD:` and `OWNS:` lines.
  - Evidence is bound to a SHA-256 digest of the gate definition. The README notes that anyone who can edit a ledger could still forge it, so parents must re-run the checks.

  <https://github.com/Leonxlnx/unlazy#the-gate-contract>
- **Unlazy's rules for gates that can fail:**
  - observe the artifact directly
  - print a success-only marker after all assertions
  - test absence checks against a known positive
  - measure numbers instead of copying them
  - review consequential manual gates in proportion to their risk
  - keep cross-cutting checks in branch ledgers rather than leaves
  - optionally lint the ledger with `scripts/gate-lint.mjs` as its own G0 gate

  <https://github.com/Leonxlnx/unlazy/blob/main/references/gates.md>
- **Scope.** Unlazy's SKILL.md says not to create gates for trivial edits or factual replies. <https://github.com/Leonxlnx/unlazy/blob/main/SKILL.md>
- **Command safety.** The README calls approval consent rather than a sandbox. Checks run with your ambient filesystem, credential and network access. <https://github.com/Leonxlnx/unlazy#security-boundary>
- **Parallel dispatch.** Unlazy's dispatch reference, added after the video, requires launching and recording every ready leaf before the first wait.
  - *Claude Code:* launch leaves as background Agent tasks.
  - *Codex:* call `spawn_agent` per leaf, and `wait_agent` only after the wave is sealed.

  <https://github.com/Leonxlnx/unlazy/blob/main/references/dispatch.md>
- **Claude Code subagents.**
  - Each subagent starts with a fresh, isolated context window.
  - Frontmatter sets a per-agent `model`, and `isolation: worktree` gives it its own checkout.
  - Independent investigations can run at the same time.

  <https://code.claude.com/docs/en/sub-agents>
- **Stop hooks.**
  - A Stop hook fires when the main agent finishes responding, and Stop has no matcher support.
  - Exit code 2 blocks the stop and passes stderr to Claude as the reason (JSON `decision: "block"` with a `reason` also works).
  - `CLAUDE_PROJECT_DIR` is the project root where the session started.

  <https://code.claude.com/docs/en/hooks>
- **Stop hook block cap.** Claude Code overrides a Stop hook once it has blocked eight times in a row without progress. The guide suggests exiting early when the input's `stop_hook_active` is true. Starter H deliberately doesn't, so a stuck ledger ends at this cap. <https://code.claude.com/docs/en/hooks-guide#stop-hook-hits-the-block-cap>
- **Edit deny rules.**
  - `Edit(path)` rules use gitignore-style patterns. In project settings (`.claude/settings.json` or `.claude/settings.local.json`), a leading `/` anchors to the primary working directory.
  - They cover Claude's built-in edit tools, the Bash file commands Claude Code recognises (such as `sed`) and redirection targets.
  - They don't cover scripts that open files themselves. That's why the checker can still write evidence, and why starter G isn't a hard lock. For OS-level enforcement the docs point to the sandbox.

  <https://code.claude.com/docs/en/permissions>
- **How `/goal` judges.** After each turn a small fast model (Haiku by default) judges the condition from the conversation, without running tools. The docs advise a measurable end state, a stated check such as a command's result, and a turn cap. A condition that names the checker's printed output therefore gives the judge real evidence, which narrows the gap the video describes ([03:56](https://www.youtube.com/watch?v=c47uqR7XB_c&t=236s)). <https://code.claude.com/docs/en/goal>

## Related

- **Concepts:** [[Verification Before Done]] · [[Agent Laziness]] · [[Loop Engineering]] · [[Subagents and Agent Teams]] · [[Context Window Management]] · [[Plan Before Executing]] · [[Permissions and Approval Gates]]
- **Techniques:** [[Build Verification into Every Task]] · [[Tests-First Goal Loop]] · [[Plan-First Workflow]] · [[Multi-Agent Review and Scoring Loops]] · [[Parallel Sessions with Git Worktrees]] · [[Route Tasks to the Right Claude Model]] · [[Keep CLAUDE.md Lean]] · [[Configure Safe Autonomy Permissions]]
- **Tools:** [[Unlazy]] · [[Claude Code]] · [[OpenAI Codex]]
- **People:** [[Leon Lin]]
- **Source:** [[AI LABS - The Unlazy Skill for Lazy Agents]]
- [[Home]]
