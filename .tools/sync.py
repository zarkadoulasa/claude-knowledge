#!/usr/bin/env python3
"""Pull new knowledge from the shared repo before the vault is used.

Usage: python3 .tools/sync.py [--force]

Runs from Claude Code hooks (see .claude/settings.json): on session start with
--force, and before each prompt otherwise (throttled to one fetch per
THROTTLE_MIN minutes). Only fast-forwards/rebases `main` when the working tree
is clean, so it never interferes with an ingest in progress. Whatever it prints
is added to Claude's context. Uses only the standard library and always exits 0.
"""
import subprocess
import sys
import time
from pathlib import Path

UPSTREAM_SLUG = "zarkadoulasa/claude-knowledge"
UPSTREAM_URL = f"https://github.com/{UPSTREAM_SLUG}.git"
BRANCH = "main"
THROTTLE_MIN = 10
ROOT = Path(__file__).resolve().parent.parent


def git(*args, timeout=30):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=timeout)


def upstream_remote() -> str:
    """Name of the remote pointing at the shared repo; adds one if missing."""
    for line in git("remote", "-v").stdout.splitlines():
        name, url = line.split()[:2]
        if UPSTREAM_SLUG in url.removesuffix(".git"):
            return name
    git("remote", "add", "upstream", UPSTREAM_URL)
    return "upstream"


def replay_unmerged(ref: str, before: str):
    """Rebuild main as <ref> plus only the local commits the shared repo doesn't have yet.

    A contribution whose conflicts were resolved on its PR branch lands upstream
    with a different patch than the local commit, so a plain rebase conflicts.
    Such commits are recognised by subject (squash merges append " (#N)").
    """
    merged = set(git("log", "--format=%s", "-n", "1000", ref).stdout.splitlines())
    local = [line.split(" ", 1) for line in git("rev-list", "--reverse", "--format=%H %s", "--no-commit-header", f"{ref}..{before}").stdout.splitlines()]
    keep = [sha for sha, subject in local
            if subject not in merged and not any(m.startswith(subject + " (#") for m in merged)]
    git("reset", "--hard", "-q", ref)
    result = git("cherry-pick", *keep) if keep else git("status")
    if result.returncode != 0:
        git("cherry-pick", "--abort")
        git("reset", "--hard", "-q", before)
    return result


def main() -> None:
    force = "--force" in sys.argv
    stamp = ROOT / ".git" / "knowledge-sync-stamp"  # last attempt, successful or not
    if not force and stamp.exists() and time.time() - stamp.stat().st_mtime < THROTTLE_MIN * 60:
        return
    stamp.touch()

    remote = upstream_remote()
    try:
        fetched = git("fetch", "--quiet", remote, BRANCH, timeout=20)
    except subprocess.TimeoutExpired:
        fetched = None
    if not fetched or fetched.returncode != 0:
        if force:
            print("[knowledge sync] Could not reach GitHub; answering from the local copy of the vault.")
        return

    ref = f"{remote}/{BRANCH}"
    behind = int(git("rev-list", "--count", f"HEAD..{ref}").stdout.strip() or 0)
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if behind == 0:
        if force:
            where = "" if branch == BRANCH else f" (currently on branch '{branch}', not `{BRANCH}`)"
            print(f"[knowledge sync] Vault is up to date with the shared repo{where}.")
        return

    dirty = git("status", "--porcelain").stdout.strip()
    busy = (ROOT / ".git" / "rebase-merge").exists() or (ROOT / ".git" / "rebase-apply").exists()
    if branch != BRANCH or dirty or busy:
        reason = "a rebase is in progress" if busy else f"on branch '{branch}'" if branch != BRANCH else "there are uncommitted changes"
        print(f"[knowledge sync] {behind} new commit(s) in the shared repo, not pulled because {reason}. "
              f"Finish or contribute the current work, then run `python3 .tools/sync.py --force`.")
        return

    before = git("rev-parse", "HEAD").stdout.strip()
    pulled = git("rebase", ref)
    if pulled.returncode != 0:
        git("rebase", "--abort")
        pulled = replay_unmerged(ref, before)
    if pulled.returncode != 0:
        print(f"[knowledge sync] {behind} new commit(s) in the shared repo conflict with local commits; nothing was pulled. "
              f"Tell the user and offer to resolve: `git rebase {ref}`, fix conflicts keeping both sides' entries, continue.")
        return

    changed = git("diff", "--name-status", before, "HEAD", "--", "*.md").stdout.strip().splitlines()
    labels = {"A": "new", "M": "updated", "D": "deleted"}
    lines = [f"  {labels.get(s[0], s[0])}: {p}" for s, p in (c.split("\t", 1) for c in changed)]
    print(f"[knowledge sync] Pulled {behind} new commit(s) from the shared repo. Notes changed:")
    print("\n".join(lines[:60]) or "  (no notes)")
    if len(lines) > 60:
        print(f"  …and {len(lines) - 60} more")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # a sync problem must never block the session
        print(f"[knowledge sync] Skipped: {e}")
