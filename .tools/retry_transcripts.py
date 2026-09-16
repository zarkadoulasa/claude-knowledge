#!/usr/bin/env python3
"""Fetch transcripts politely when YouTube is rate-limiting this IP.

Usage: .tools/.venv/bin/python .tools/retry_transcripts.py <out_dir> <video_id> [<video_id> ...]
       [--initial-wait MIN] [--max-hours H]

Transcript-only (metadata is fetched separately by fetch_youtube.py). Waits before the
first attempt, fetches one video at a time with a pause between successes, and backs off
(10 → 20 → 40 min) whenever YouTube blocks the request. Writes <out_dir>/<id>.transcript.md
in the same format as fetch_youtube.py. Exits when every video is done or unavailable, or at
the deadline.
"""
import argparse
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
    TranscriptsDisabled,
    VideoUnavailable,
)


def ts(seconds: float) -> str:
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir")
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--initial-wait", type=float, default=10, help="minutes before the first attempt")
    ap.add_argument("--max-hours", type=float, default=4)
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pending = [i for i in args.ids if not (out / f"{i}.transcript.md").exists()]
    unavailable = []
    deadline = time.time() + args.max_hours * 3600
    backoff = 10

    log(f"{len(pending)} pending; waiting {args.initial_wait:g} min before first attempt")
    time.sleep(args.initial_wait * 60)

    api = YouTubeTranscriptApi()
    while pending and time.time() < deadline:
        vid = pending[0]
        try:
            snippets = api.fetch(vid, languages=["en", "en-US", "en-GB"])
        except (IpBlocked, RequestBlocked):
            log(f"blocked on {vid}; backing off {backoff} min ({len(pending)} pending)")
            time.sleep(backoff * 60)
            backoff = min(backoff * 2, 40)
            continue
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            log(f"{vid}: no transcript ({type(e).__name__})")
            unavailable.append(vid)
            pending.pop(0)
            continue
        lines = [f"[{ts(s.start)}] {s.text.strip()}" for s in snippets if s.text.strip()]
        (out / f"{vid}.transcript.md").write_text("\n".join(lines) + "\n")
        log(f"{vid}: saved {len(lines)} lines")
        pending.pop(0)
        backoff = 10
        if pending:
            time.sleep(25)

    log(f"DONE fetched={len(args.ids) - len(pending) - len(unavailable)} "
        f"unavailable={unavailable} still_pending={pending}")


if __name__ == "__main__":
    main()
