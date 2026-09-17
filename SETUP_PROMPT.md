# Setup prompt

Paste this into Claude Code (terminal, desktop app, or IDE) on the machine that should get the vault.

---

Set up the "Claude Knowledge Bank" second brain on this machine. It's a shared markdown vault in the LLM Wiki pattern. Claude Code uses it through its CLAUDE.md, it has an `ingest-youtube` skill for adding YouTube tutorials, and Obsidian is an optional viewer. Every copy pulls new knowledge from the shared GitHub repo before it's used, and sends back anything it ingests as a pull request.

1. **Check prerequisites.** Confirm `git`, `python3` (3.10 or newer) and the GitHub CLI `gh` are installed, and that git has `user.name` and `user.email` set. If anything is missing, tell me how to install or set it for my OS and wait. Don't install anything without asking.
2. **Clone.** Clone `https://github.com/zarkadoulasa/claude-knowledge.git` into `~/claude-knowledge`. If that folder already exists, stop and ask me before touching it.
3. **GitHub sign-in.** Run `gh auth status`. If I'm not signed in, ask me to run `gh auth login` myself (choose HTTPS and let it set up git credentials), then continue. Contributions go through a fork of the shared repo under my account, which is created automatically the first time.
4. **Python tools.** Inside the vault, run:
   `python3 -m venv .tools/.venv && .tools/.venv/bin/pip install -r .tools/requirements.txt`
5. **Verify.**
   - Run `.tools/.venv/bin/python .tools/check_links.py` from the vault root. It must report no broken links.
   - Run `python3 .tools/sync.py --force`. It should say the vault is up to date.
   - Confirm `CLAUDE.md`, `Home.md`, `.claude/settings.json` and `.claude/skills/ingest-youtube/SKILL.md` exist.
   - Count the notes in `Sources/`, `Concepts/` and `Techniques/`, and report the numbers.
6. **Obsidian (optional).** Ask if I want Obsidian. If I say yes, tell me to install it from https://obsidian.md and use "Open folder as vault" on `~/claude-knowledge`.
7. **Explain how to use it.** In a few lines, tell me:
   - Always start Claude Code from inside `~/claude-knowledge`. The first time, accept the prompt to trust the folder so its hooks can run. They pull new shared knowledge at session start and before prompts.
   - Ask "how should I…" questions. Claude answers from the notes, with timestamped source links.
   - Paste a YouTube tutorial link to ingest it. Claude writes the notes, keeps them locally, and opens a pull request so everyone else gets them once it's merged.
   - Say "build X from <technique or video>" to set up a system from a Technique note.
8. **Smoke test.** Read `Home.md` and give me a 5-line overview of what the vault covers so far.

Don't change any vault notes during setup.
