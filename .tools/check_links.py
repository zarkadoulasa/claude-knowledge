#!/usr/bin/env python3
"""Report [[wikilinks]] in the vault that don't resolve to a note.

Usage: .tools/.venv/bin/python .tools/check_links.py   (run from the vault root)
Exits 1 if any link is broken.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".obsidian", ".tools", ".claude", "Templates", ".trash"}
LINK = re.compile(r"\[\[([^\]]+?)\]\]")


def notes():
    for p in ROOT.rglob("*.md"):
        if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts):
            yield p


def main() -> None:
    names = {p.stem for p in notes()} | {str(p.relative_to(ROOT).with_suffix("")) for p in notes()}
    broken = []
    for p in notes():
        text = re.sub(r"```.*?```", "", p.read_text(), flags=re.S)  # ignore code blocks
        text = re.sub(r"`[^`\n]*`", "", text)  # and inline code (placeholder examples)
        for raw in LINK.findall(text):
            target = raw.split("|")[0].split("#")[0].strip()
            if target and target not in names:
                broken.append((p.relative_to(ROOT), target))
    for src, target in broken:
        print(f"{src}: [[{target}]]")
    print(f"{len(broken)} broken link(s) across {sum(1 for _ in notes())} notes")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
