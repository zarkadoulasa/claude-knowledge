#!/usr/bin/env python3
"""Share new vault knowledge as a pull request to the shared repo.

Usage: python3 .tools/contribute.py --title "Ingest: <video title>" --body-file <file> [--slug <short-slug>]

Run from `main` after an ingest (or any note change) has been written and
verified. It:
  1. commits the uncommitted vault changes on `main` (so this machine keeps the
     new knowledge right away),
  2. replays that one commit on a fresh branch from the shared repo's `main`,
  3. pushes the branch (to the shared repo if you have write access, otherwise
     to your fork, which it creates) and opens a PR with the GitHub CLI.

If step 2 hits conflicts it stops with the branch mid-cherry-pick. Resolve
the files (keep both sides' entries), `git add` them,
`git -c core.editor=true cherry-pick --continue`, then rerun with `--resume`.
Needs `gh` installed and signed in (`gh auth login`).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True  # keep __pycache__ out of the vault
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sync import BRANCH, ROOT, UPSTREAM_SLUG, git, upstream_remote  # noqa: E402


def run(*cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def fail(msg: str, code: int = 1):
    print(f"[contribute] {msg}")
    sys.exit(code)


def ensure_gh() -> str:
    if not shutil.which("gh"):
        fail("The GitHub CLI is not installed. Install it (macOS: `brew install gh`; others: "
             "https://cli.github.com), run `gh auth login`, then rerun this script. "
             "The notes are safe on this machine in the meantime.", 2)
    who = run("gh", "api", "user", "--jq", ".login")
    if who.returncode != 0:
        fail("The GitHub CLI is not signed in. Ask the user to run `gh auth login`, then rerun this script.", 2)
    return who.stdout.strip()


def push_target(login: str) -> tuple[str, str]:
    """(remote to push to, owner for the PR head)."""
    perms = run("gh", "api", f"repos/{UPSTREAM_SLUG}", "--jq", ".permissions.push")
    if perms.stdout.strip() == "true":
        return upstream_remote(), UPSTREAM_SLUG.split("/")[0]
    fork_slug = f"{login}/{UPSTREAM_SLUG.split('/')[1]}"
    for line in git("remote", "-v").stdout.splitlines():
        name, url = line.split()[:2]
        if fork_slug in url.removesuffix(".git"):
            return name, login
    made = run("gh", "repo", "fork", UPSTREAM_SLUG, "--clone=false")
    if made.returncode != 0 and "already exists" not in made.stderr:
        fail(f"Could not fork {UPSTREAM_SLUG}: {made.stderr.strip()}")
    git("remote", "add", "fork", f"https://github.com/{fork_slug}.git")
    return "fork", login


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--body-file", required=True)
    ap.add_argument("--slug", help="branch name suffix; defaults to a slug of the title")
    ap.add_argument("--resume", action="store_true", help="continue after resolving cherry-pick conflicts")
    a = ap.parse_args()

    login = ensure_gh()
    slug = a.slug or re.sub(r"[^a-z0-9]+", "-", a.title.lower()).strip("-")[:50]
    pr_branch = f"contrib/{slug}"
    remote = upstream_remote()

    if not a.resume:
        if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != BRANCH:
            fail(f"Run this from the `{BRANCH}` branch.")
        check = run(sys.executable, ".tools/check_links.py")
        if check.returncode != 0:
            fail("Broken wikilinks; fix them before contributing:\n" + check.stdout)
        if not git("status", "--porcelain").stdout.strip():
            fail("No uncommitted vault changes to contribute.")
        git("add", "-A")
        committed = git("commit", "-q", "-m", f"{a.title}\n\nContributed by @{login}")
        if committed.returncode != 0:
            fail("Commit failed: " + committed.stderr.strip())
        commit = git("rev-parse", "HEAD").stdout.strip()

        if git("fetch", "--quiet", remote, BRANCH).returncode != 0:
            fail("Could not fetch the shared repo. The notes are committed on main; rerun when online "
                 "with `--resume` after `git checkout -b " + pr_branch + f" {remote}/{BRANCH} && git cherry-pick {commit}`.")
        git("branch", "-D", pr_branch)
        git("checkout", "-q", "-b", pr_branch, f"{remote}/{BRANCH}")
        picked = git("cherry-pick", commit)
        if picked.returncode != 0:
            conflicts = git("diff", "--name-only", "--diff-filter=U").stdout.strip()
            fail("Conflicts with newer shared notes in:\n" + conflicts +
                 "\nResolve them (keep both sides' entries; recount totals in Home.md), `git add` the files, "
                 "`git -c core.editor=true cherry-pick --continue`, then rerun with the same arguments plus --resume.", 3)
    elif git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != pr_branch:
        fail(f"--resume expects to be on `{pr_branch}`.")
    elif (ROOT / ".git" / "CHERRY_PICK_HEAD").exists() or git("diff", "--name-only", "--diff-filter=U").stdout.strip():
        fail("The cherry-pick is still unfinished. Resolve the conflicts, `git add` the files, "
             "`git -c core.editor=true cherry-pick --continue`, then rerun with --resume.", 3)
    if git("rev-list", "--count", f"{remote}/{BRANCH}..HEAD").stdout.strip() == "0":
        fail(f"`{pr_branch}` has nothing beyond the shared main; no pull request to open.")

    push_remote, head_owner = push_target(login)
    for attempt in range(4):  # a brand-new fork can take a few seconds to accept pushes
        pushed = git("push", "--force-with-lease", "-u", push_remote, f"{pr_branch}:{pr_branch}", timeout=120)
        if pushed.returncode == 0:
            break
        time.sleep(5 * (attempt + 1))
    if git("rev-list", "--count", f"{remote}/{BRANCH}..{BRANCH}").stdout.strip() == "1":
        # main holds only this contribution: point it at the PR version (with any
        # conflict resolution) so later syncs fast-forward cleanly.
        git("branch", "-f", BRANCH, pr_branch)
    back = git("checkout", "-q", BRANCH)
    if back.returncode != 0:
        print(f"[contribute] Warning: could not switch back to `{BRANCH}`: {back.stderr.strip()}")
    if pushed.returncode != 0:
        fail("Push failed: " + pushed.stderr.strip())

    existing = run("gh", "pr", "list", "--repo", UPSTREAM_SLUG, "--head", pr_branch, "--json", "url")
    urls = [p["url"] for p in json.loads(existing.stdout or "[]")] if existing.returncode == 0 else []
    if urls:
        print(f"[contribute] Updated the existing pull request: {urls[0]}")
        return
    pr = run("gh", "pr", "create", "--repo", UPSTREAM_SLUG, "--base", BRANCH,
             "--head", f"{head_owner}:{pr_branch}", "--title", a.title, "--body-file", a.body_file)
    if pr.returncode != 0:
        fail("Could not open the pull request: " + pr.stderr.strip())
    print(f"[contribute] Opened pull request: {pr.stdout.strip()}")


if __name__ == "__main__":
    main()
