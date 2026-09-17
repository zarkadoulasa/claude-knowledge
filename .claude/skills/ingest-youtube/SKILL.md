---
name: ingest-youtube
description: Ingest a YouTube tutorial into the Claude Knowledge Bank vault — fetch metadata and transcript, write or update Source, Concept, Technique, Tool and People notes, then update Home.md and the Ingest Log. Use whenever the user shares a YouTube URL (youtube.com/watch, youtu.be, shorts) in this vault.
---

# Ingest a YouTube tutorial

Follow the conventions in `CLAUDE.md` throughout.

## 0. Sync

Run `python3 .tools/sync.py --force` so the plan builds on the latest shared notes. If it reports that nothing was pulled (uncommitted changes, another branch, conflicts), sort that out with the user before writing.

## 1. Fetch

```bash
.tools/.venv/bin/python .tools/fetch_youtube.py "<url>" "<scratch-or-temp-dir>/yt"
```

Writes `<id>.meta.json` (title, channel, date, duration, description, chapters) and `<id>.transcript.md` (`[mm:ss]`-prefixed lines) into the scratch directory — never into the vault.

- venv missing → `python3 -m venv .tools/.venv && .tools/.venv/bin/pip install youtube-transcript-api yt-dlp`
- No transcript available → stop and tell the user.
- `IpBlocked` / `RequestBlocked` / HTTP 429 means YouTube is rate-limiting this IP, usually after many fetches in a row; the transcript itself isn't missing. The metadata usually still downloads. Don't retry in a tight loop. Run `.tools/.venv/bin/python .tools/retry_transcripts.py "<scratch>/yt" <ids…>` in the background: it waits, fetches one video at a time and backs off when blocked. On 2026-09-15 the block cleared within about 20 minutes.
- Check that each video is actually about Claude before ingesting it (title and description); tell the user about anything off-topic rather than ingesting it.

## 2. Check for an existing ingest

`grep -rl "video_id: <id>" Sources/` — if found, update that note instead of creating a new one.

## 3. Read everything

Read the **whole** transcript and the description. Read `Home.md` to learn which Concepts, Techniques, Tools and People already exist.

## 4. Plan the notes (before writing anything)

- **Source** — always exactly one.
- **Concepts** — new ideas, plus existing concept notes this video adds to or disagrees with.
- **Techniques** — every buildable thing the video teaches or demonstrates.
- **Tools / People** — only substantive mentions; skip passing mentions and sponsor plugs.

Fix the full list of note titles up front so every `[[link]]` resolves. Note likely caption errors (product names, jargon) so they are corrected consistently.

## 5. Write

Use the templates in `Templates/`. The Source note needs: TL;DR, key takeaways, chapter-by-chapter notes with timestamp links, caveats & disagreements, "Build from this" (concrete system ideas linking to Techniques), resources mentioned, beyond-the-source context, transcript notes.

For long or dense videos, fan out: one agent per group of notes → an adversarial fact-check of each note against the transcript → a completeness pass comparing the transcript to all notes.

### Batches of several videos

1. **Analyse first.** Run one agent per video that reads the whole transcript and returns a structured digest (key points with timestamps, concepts, techniques, tools, people, caption corrections, conflicts with existing notes). Save the digests to the scratch directory.
2. **Plan across all videos.** Merge overlapping topics into one note each, and decide which existing notes get updated. Give every file exactly one writing agent.
3. **Write, then fact-check each group.** Agents writing shared notes use the digests as a map, confirm each point in the transcripts, and credit every point to its source note.
4. **Review each video.** One review agent per video reads its transcript plus only the vault lines citing that video (`grep -rn "v=<id>"`). Group the findings so fix batches never share a file.
5. **Recovering from an interrupted run** (e.g. a usage limit): don't resume a run that would redo the writing step, because it can overwrite checked notes. Start a new run that does only the unfinished checking.

## 6. Verify

- Every video claim has a timestamp link landing within ~15 s of where it is said.
- Nothing from outside the video sits outside a `## Beyond the source` section; external facts carry a verification link.
- `.tools/.venv/bin/python .tools/check_links.py` reports no broken links.
- No long verbatim transcript passages.

## 7. Index and log

- Add new notes to `Home.md` in the right sections (keep each section sorted) and update the source count.
- Append a row to `Ingest Log.md`: date, source, notes created, notes updated.

## 8. Contribute

Every ingest goes back to the shared repo as a pull request, so everyone else gets the knowledge.

1. Write a PR description to the scratch directory, not the vault: the video link, a 2–3 line summary, the notes created, the notes updated, and the verification done (fact-check fixes, `check_links.py` result).
2. From the vault root on `main`, run:
   `python3 .tools/contribute.py --title "Ingest: <Creator> - <Video title>" --body-file <scratch>/pr-body.md`
   For a batch, use one PR titled `Ingest: batch of N (<short theme>)`.
3. Handle the exit code:
   - **0**: it prints the PR link.
   - **2**: the GitHub CLI is missing or not signed in. Tell the user to install `gh` and run `gh auth login`, then rerun. The notes are already committed locally and stay available.
   - **3**: newer shared notes conflict (usually `Home.md`). Resolve each file by keeping both sides' entries and recounting totals. Then `git add` the files, run `git -c core.editor=true cherry-pick --continue`, and rerun the same command with `--resume`.
   - **1**: read the message and fix the cause. Broken links must be fixed before contributing.
4. Never push directly to `main` on the shared repo.

## 9. Report to the user

The 3–5 most useful takeaways, which notes were created/updated, 2–3 systems that could be built from the tutorial, and the PR link.
