# Claude Knowledge Bank

A second brain of the best guidance on using Claude (Claude Code, the apps, the API, skills, agents, memory, prompting), built from YouTube tutorials. Plain markdown in the LLM Wiki pattern. Claude Code reads it through `CLAUDE.md`, and Obsidian is an optional viewer.

- `Home.md` is the master index. Start there.
- `Sources/`, `Concepts/`, `Techniques/`, `Tools/`, `People/` hold the notes.
- `.claude/skills/ingest-youtube/` is the skill that turns a YouTube link into notes.
- `.tools/` holds the fetch, link-check, sync and contribute scripts.

## How sharing works

- **Pull before use:** hooks in `.claude/settings.json` run `.tools/sync.py` when a Claude Code session starts and before prompts (at most every 10 minutes). The script only updates `main` when there are no uncommitted edits.
- **Contribute after ingest:** the `ingest-youtube` skill ends by running `.tools/contribute.py`. It commits the new notes locally, replays them on a branch from the shared `main`, pushes (to your fork if you can't write to this repo), and opens a pull request. It needs the GitHub CLI (`gh auth login`).
- **Review:** a GitHub Action checks every PR for broken wikilinks. Once a PR is merged, every copy picks it up on its next sync.

## Set it up with Claude Code

Open Claude Code in the folder where you want the vault to live and paste the prompt in [SETUP_PROMPT.md](SETUP_PROMPT.md).

## Set it up by hand

```bash
git clone https://github.com/zarkadoulasa/claude-knowledge.git ~/claude-knowledge
cd ~/claude-knowledge
python3 -m venv .tools/.venv
.tools/.venv/bin/pip install -r .tools/requirements.txt
.tools/.venv/bin/python .tools/check_links.py
gh auth login
```

Then run `claude` inside `~/claude-knowledge` and trust the folder when asked, so the sync hooks can run. Ask it "how should I…" questions, or paste a YouTube link to ingest a tutorial.
