# Claude Knowledge Bank

A second brain of the best guidance on using Claude (Claude Code, the apps, the API, skills, agents, memory, prompting), built from YouTube tutorials. Plain markdown in the LLM Wiki pattern. Claude Code reads it through `CLAUDE.md`, and Obsidian is an optional viewer.

- `Home.md` is the master index. Start there.
- `Sources/`, `Concepts/`, `Techniques/`, `Tools/`, `People/` hold the notes.
- `.claude/skills/ingest-youtube/` is the skill that turns a YouTube link into notes.
- `.tools/` holds the fetch and link-check scripts.

## Set it up with Claude Code

Open Claude Code in the folder where you want the vault to live and paste the prompt in [SETUP_PROMPT.md](SETUP_PROMPT.md).

## Set it up by hand

```bash
git clone https://github.com/zarkadoulasa/claude-knowledge.git ~/claude-knowledge
cd ~/claude-knowledge
python3 -m venv .tools/.venv
.tools/.venv/bin/pip install -r .tools/requirements.txt
.tools/.venv/bin/python .tools/check_links.py
```

Then run `claude` inside `~/claude-knowledge`. Ask it "how should I…" questions, or paste a YouTube link to ingest a tutorial.
