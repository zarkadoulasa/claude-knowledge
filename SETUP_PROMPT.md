# Setup prompt

Paste this into Claude Code (terminal, desktop app, or IDE) on the machine that should get the vault.

---

Set up the "Claude Knowledge Bank" second brain on this machine. It's a markdown vault in the LLM Wiki pattern. Claude Code uses it through its CLAUDE.md, it has an `ingest-youtube` skill for adding YouTube tutorials, and Obsidian is an optional viewer.

1. **Check prerequisites.** Confirm `git` and `python3` (3.10 or newer) are installed. If one is missing, tell me how to install it for my OS and wait.
2. **Clone.** Clone `https://github.com/zarkadoulasa/claude-knowledge.git` into `~/claude-knowledge`. If that folder already exists, stop and ask me before touching it. If the clone fails on authentication, the repo is private: tell me to ask the owner for access, or to sign in with `gh auth login`, then retry.
3. **Python tools.** Inside the vault, run:
   `python3 -m venv .tools/.venv && .tools/.venv/bin/pip install -r .tools/requirements.txt`
4. **Verify.**
   - Run `.tools/.venv/bin/python .tools/check_links.py` from the vault root. It must report no broken links.
   - Confirm `CLAUDE.md`, `Home.md` and `.claude/skills/ingest-youtube/SKILL.md` exist.
   - Count the notes in `Sources/`, `Concepts/` and `Techniques/`, and report the numbers.
5. **Obsidian (optional).** Ask if I want Obsidian. If I say yes, tell me to install it from https://obsidian.md and use "Open folder as vault" on `~/claude-knowledge`. Don't install anything without asking.
6. **Explain how to use it.** In a few lines, tell me:
   - Always start Claude Code from inside `~/claude-knowledge` so it loads the vault's CLAUDE.md and skill.
   - Ask "how should I…" questions. Claude answers from the notes, with timestamped source links.
   - Paste a YouTube tutorial link to ingest it, which creates Source, Concept and Technique notes.
   - Say "build X from <technique or video>" to set up a system from a Technique note.
   - To get the owner's new notes later, run `git pull` (commit or stash your own changes first).
7. **Smoke test.** Read `Home.md` and give me a 5-line overview of what the vault covers so far.

Don't change any vault notes during setup.
