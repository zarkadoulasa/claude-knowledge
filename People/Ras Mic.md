---
type: person
role: "Guest — Michael Shimeles, full-stack engineer and YouTuber, interviewed on Greg Isenberg's podcast about context and skills"
links: ["https://www.rasmic.xyz/", "https://www.youtube.com/@rasmic", "https://x.com/Rasmic", "https://github.com/michaelshimeles", "https://github.com/michaelshimeles/skills"]
sources: ["[[Ras Mic - How AI Agents and Claude Skills Work]]", "[[The Coding Sloth - 1000 Hours of Claude Code Lessons]]", "[[Jay E - The ARMS Framework for a Claude Agentic OS]]", "[[Chase AI - The Agentic OS Setup for Claude Code]]"]
tags: [topic/skills, topic/context, topic/agents, topic/subagents, topic/claude-code]
---

# Ras Mic

## Who

- **In the video:** a returning guest on [[Greg Isenberg]]'s podcast ([00:00](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=0s)). His full name, Michael Shimeles, comes from his own site and GitHub (see *Beyond the source*).
- **Stance:** says he disagrees with most current agent advice ([00:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=4s)).
- **Examples:** agents he runs for his YouTube business, such as sponsor-email vetting ([07:10](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=430s)).
- **Harness:** his personal agent system is built on [[OpenClaw]]. He found it confusing at first and says it took about two weeks to become useful ([24:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1444s)).

## In this vault

- [[Ras Mic - How AI Agents and Claude Skills Work]] — guest and main presenter.

## Ideas associated with him

- **Minimal context files.** → [[Keep CLAUDE.md Lean]], [[CLAUDE.md as a Router]]
  - 95% of people don't need AGENTS.md or CLAUDE.md ([02:04](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=124s)).
  - The exception is company-specific or proprietary information, or a method of your own, that every conversation needs ([03:08](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=188s)).
- **Skills are cheap until used.** Counted with OpenAI's tokenizer, his code-structure skill is 944 tokens in full ([30:42](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1842s)), but 53 for its name and description ([30:54](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1854s)). → [[Agent Skills]]
- **Build skills from a successful run.** → [[Build a Skill from a Successful Run]]
  - Walk the agent through the workflow step by step ([09:17](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=557s)).
  - Write the skill only after repeated successful runs ([11:12](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=672s)).
- **Don't install others' skills.** → [[Build vs Install Third-Party Skills]]
  - Read them and learn from them instead ([12:39](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=759s)).
  - Downloaded skills are an easy attack route ([13:02](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=782s)).
- **Recursive improvement.** → [[Skill Improvement Loop]]
  - Pass each failure back to the agent, then have it update the skill ([21:46](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1306s)).
  - Five rounds made his eight-source report generator reliable ([22:13](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1333s)).
- **Scale for productivity** ([14:44](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=884s)): start with one agent and its skills, then add subagents ([15:28](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=928s)). He now has five, naming marketing, business and personal ([26:24](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1584s)). → [[Subagents and Agent Teams]]
- **Context budget:** keep usage below about 70% ([31:19](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=1879s)). → [[Context Window Management]]

## Where sources disagree

- **Installing skills.** [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] installs community skills from skills.sh ([05:55](https://www.youtube.com/watch?v=YAsxyoTWFDA&t=355s)).
- **When to write a skill.**
  - [[Jay E - The ARMS Framework for a Claude Agentic OS]] made one from a pasted X post ([06:00](https://www.youtube.com/watch?v=8NSyI-npJCU&t=360s)).
  - [[Chase AI - The Agentic OS Setup for Claude Code]] agrees with Ras Mic: confirm the task works by hand first ([07:18](https://www.youtube.com/watch?v=HRw-vP0j8OM&t=438s)).

## Beyond the source

- **Profile:** Michael Shimeles, a full-stack engineer who runs Fabrika, a software studio and AI consultancy — [rasmic.xyz](https://www.rasmic.xyz/). GitHub lists Toronto; his `skills` repo includes code-structure. — [GitHub](https://github.com/michaelshimeles/skills)
- **How CLAUDE.md loads.** He says CLAUDE.md is added every turn ([04:14](https://www.youtube.com/watch?v=S_oN3vlzpMw&t=254s)). The docs say it loads at session start. They recommend under 200 lines, with procedures moved into skills. — [Claude Code docs: memory](https://code.claude.com/docs/en/memory)

## Related

- [[Home]]
- [[Greg Isenberg]]
- [[OpenClaw]]
