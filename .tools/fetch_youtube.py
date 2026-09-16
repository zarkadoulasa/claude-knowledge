#!/usr/bin/env python3
"""Fetch metadata + timestamped transcript for a YouTube video.

Usage: .tools/.venv/bin/python .tools/fetch_youtube.py <url> <out_dir>

Writes <out_dir>/<video_id>.meta.json and <out_dir>/<video_id>.transcript.md
(transcript lines prefixed with [mm:ss]). Raw transcripts are working files —
keep them out of the visible vault; vault notes should document the knowledge.
"""
import json
import re
import sys
from pathlib import Path

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi


def video_id(url: str) -> str:
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([A-Za-z0-9_-]{11})", url)
    if not m:
        sys.exit(f"Could not parse video id from {url}")
    return m.group(1)


def ts(seconds: float) -> str:
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def main() -> None:
    url, out_dir = sys.argv[1], Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    vid = video_id(url)

    with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
    meta = {
        "id": vid,
        "url": f"https://www.youtube.com/watch?v={vid}",
        "title": info.get("title"),
        "channel": info.get("channel") or info.get("uploader"),
        "channel_url": info.get("channel_url"),
        "upload_date": info.get("upload_date"),
        "duration": info.get("duration"),
        "duration_string": info.get("duration_string"),
        "view_count": info.get("view_count"),
        "description": info.get("description"),
        "chapters": [
            {"start": ts(c["start_time"]), "start_seconds": int(c["start_time"]), "title": c["title"]}
            for c in (info.get("chapters") or [])
        ],
        "tags": info.get("tags"),
    }
    (out_dir / f"{vid}.meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    transcript = YouTubeTranscriptApi().fetch(vid, languages=["en", "en-US", "en-GB"])
    lines = [f"[{ts(snip.start)}] {snip.text.strip()}" for snip in transcript if snip.text.strip()]
    (out_dir / f"{vid}.transcript.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({k: meta[k] for k in ("id", "title", "channel", "upload_date", "duration_string")}))
    print(f"chapters: {len(meta['chapters'])}, transcript lines: {len(lines)}")


if __name__ == "__main__":
    main()
