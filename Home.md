---
type: index
updated: 2026-09-15
---

# Claude Knowledge Bank

A curated bank of the best guidance on using and improving Claude, built from tutorials. **26 sources · 30 concepts · 42 techniques · 19 tools · 18 people.**

**How to use it**
- *Add a tutorial:* paste a YouTube link (or several) into Claude Code in this folder. The `ingest-youtube` skill does the rest.
- *Ask a question:* for example, "How do I stop Claude getting lazy on long tasks?" Claude starts here, then reads the matching Concepts and Techniques.
- *Build something:* for example, "Set up [[Evidence-Gated Completion Ledger]] in ~/projects/app."

## Start here

| If you want to… | Read | Then build |
|---|---|---|
| Get better results from Claude Code day to day | [[Context Window Management]] · [[Plan Before Executing]] · [[Verification Before Done]] | [[Context Hygiene Routine]] · [[Plan-First Workflow]] · [[Build Verification into Every Task]] |
| Stop agents cutting corners on long tasks | [[Agent Laziness]] · [[Verification Before Done]] | [[Evidence-Gated Completion Ledger]] · [[Tests-First Goal Loop]] |
| Package your workflows | [[Agent Skills]] · [[Build vs Install Third-Party Skills]] | [[Workflow Audit into Skills]] · [[Build a Skill from a Successful Run]] · [[Audit Skill Descriptions and Triggers]] |
| Run Claude while you're away | [[Routines and Scheduled Tasks]] · [[Loop Engineering]] · [[Permissions and Approval Gates]] | [[Schedule Recurring Claude Tasks]] · [[Configure Safe Autonomy Permissions]] |
| Design sites that don't look AI-made | [[Escaping the Default AI Design Look]] · [[Design Systems for Claude]] | [[Create and Reuse a Claude Design System]] · [[Build a Distinctive Site with Design Skills]] · [[Benchmark-Driven Design Critique]] |
| Make images, video and marketing assets | [[Generating Images and Video with Claude]] | [[Build a Brand-Aware Marketing Project]] · [[Generate On-Brand Images from Claude Code]] · [[Storyboard-First AI Video and Motion Graphics]] |
| Build a second brain or wiki | [[LLM Wiki]] · [[Second Brain Levels]] | [[Bootstrap an LLM Wiki from the Karpathy Gist]] · [[Add a Journal and Personal CRM to a Second Brain]] · [[Second Brain Pain-Point Audit]] |
| Build an agentic OS | [[Agentic OS]] | [[Build a Level 1 Second Brain]] · [[Build an Agentic OS Dashboard]] |
| Set up Claude Cowork | [[Claude Cowork]] | [[Set Up Claude Cowork]] |
| Do trustworthy research with Claude | [[Grounding Research in Real Sources]] · [[Multi-Perspective Research]] | [[Set Up Claude Research Connectors]] · [[Build a STORM Multi-Perspective Research Skill]] |

## Sources

| Source | Creator | Published | Topics |
|---|---|---|---|
| [[AI LABS - Eight GitHub Repos to Upgrade Claude Code]] | [[AI LABS]] | 2026-09-14 | verification, token trimming, skill evals, design registry |
| [[Chase AI - GPT-6 Astra Motion Design in After Effects]] | [[Chase AI]] | 2026-09-14 | motion graphics, storyboards (mostly non-Claude stack) |
| [[Nate Herk - Build Skills Instead of Agents]] | [[Nate Herk]] | 2026-09-13 | skills, descriptions, verification |
| [[AI LABS - Claude Design Skills for Beautiful Sites]] | [[AI LABS]] | 2026-08-24 | design skills, Claude Design |
| [[Nate Herk - The Scrollcraft Website Design Skill]] | [[Nate Herk]] | 2026-08-22 | scroll-driven sites, design skill |
| [[Jay E - The ARMS Framework for a Claude Agentic OS]] | [[Jay E]] | 2026-08-21 | agentic OS, skills, routines, memory |
| [[Nate Herk - Claude as a One-Person Marketing Team]] | [[Nate Herk]] | 2026-08-21 | marketing, media generation, non-coders |
| [[AI LABS - The Unlazy Skill for Lazy Agents]] | [[AI LABS]] | 2026-08-20 | agent laziness, evidence gates, subagents |
| [[The Coding Sloth - 1000 Hours of Claude Code Lessons]] | [[The Coding Sloth]] | 2026-08-18 | Claude Code features tier list |
| [[Jack Roberts - Design Systems, Critic Loops and a Design OS]] | [[Jack Roberts]] | 2026-08-12 | design systems, critic loops |
| [[Sergei Chyrkov - Claude Design Full Tutorial]] | [[Sergei Chyrkov]] | 2026-07-30 | Claude Design, design systems |
| [[David Stuckler - Claude Connectors and Skills for Academic Research]] | [[David Stuckler]] | 2026-07-22 | research connectors, Consensus, hallucination, SOP skills |
| [[AI LABS - Types of Claude Loops Explained]] | [[AI LABS]] | 2026-07-09 | loops, verification, multi-agent review |
| [[Nate Herk - Stanford STORM Method as a Claude Research Skill]] | [[Nate Herk]] | 2026-06-29 | STORM, multi-perspective research, subagents, verification |
| [[Chase AI - The Agentic OS Setup for Claude Code]] | [[Chase AI]] | 2026-06-25 | agentic OS, skills audit, vault structure |
| [[AI LABS - Design Skills from Landing Pages to Mobile Apps]] | [[AI LABS]] | 2026-06-23 | design skills, product and mobile UI |
| [[Nate Herk - Every Level of a Claude Second Brain]] | [[Nate Herk]] | 2026-06-17 | second brain, memory, retrieval |
| [[Knowing More - Every Claude Model Explained]] | Knowing More | 2026-05-07 | models (versions now dated) |
| [[Matt Wolfe - Second Brain Wiki with Journal and CRM]] | [[Matt Wolfe]] | 2026-05-06 | LLM Wiki, journal, CRM (built in Codex) |
| [[Chase AI - The Three-Step Claude Code Agentic OS]] | [[Chase AI]] | 2026-05-05 | agentic OS (earlier version of his framework) |
| [[Nate Herk - 32 Tricks to Level Up Claude Code]] | [[Nate Herk]] | 2026-04-27 | Claude Code tips |
| [[Jay E - Claude and GPT-Image-2 for On-Brand Design]] | [[Jay E]] | 2026-04-22 | image generation, brand assets |
| [[Simon Pittman - Set Up Claude Cowork]] | [[Simon Pittman]] | 2026-04-10 | Cowork setup, connectors, scheduled tasks |
| [[Anthropic - What Is Claude Managed Agents]] | Anthropic | 2026-04-09 | Managed Agents |
| [[Ras Mic - How AI Agents and Claude Skills Work]] | [[Ras Mic]] | 2026-04-08 | skills, context files, agents |
| [[Nate Herk - Set Up the Karpathy LLM Wiki with Obsidian]] | [[Nate Herk]] | 2026-04-05 | LLM Wiki setup, Obsidian |

## Concepts

**Working with Claude Code**
- [[Context Window Management]]: the context window is a finite budget, and quality drops as it fills
- [[Agent Laziness]]: why agents claim they're done early or quietly shrink the task
- [[Plan Before Executing]]: plan mode, clarifying questions, and planning with a stronger model than the one that implements
- [[Verification Before Done]]: give Claude a way to check its own work, and decide who judges when it's done
- [[Choosing a Claude Model]]: model tiers, when to escalate, and routing tasks by difficulty
- [[Grounding Research in Real Sources]]: pull from real databases and verify every citation, so Claude stops inventing references

**Skills**
- [[Agent Skills]]: what skills are, progressive disclosure, and skills instead of a new agent per job
- [[Build vs Install Third-Party Skills]]: write your own skills or install other people's (sources disagree)

**Agents, loops and automation**
- [[Subagents and Agent Teams]]: isolated workers vs communicating peers, orchestrators, parallel dispatch
- [[Multi-Perspective Research]]: run a topic through several expert lenses (Stanford's STORM) so disagreement surfaces the blind spots
- [[Loop Engineering]]: loop types, and when to loop vs keep a human judging
- [[Routines and Scheduled Tasks]]: every way to keep Claude working without you
- [[Permissions and Approval Gates]]: allow/deny rules, drafts-only rules, human approval for irreversible actions
- [[Connecting Claude to External Tools]]: CLI vs API vs MCP, aggregators, and what each costs in context
- [[Agentic OS]]: ARMS, Chase's frameworks, and how they map to other frameworks

**Design and media**
- [[Escaping the Default AI Design Look]]: why AI-built designs look alike and the levers that fix it
- [[Design Systems for Claude]]: giving Claude a real design system instead of a vague brief
- [[Generating Images and Video with Claude]]: Claude as the prompt writer and orchestrator for image and video models

**Second brains and memory**
- [[Second Brain Levels]]: five levels from a CLAUDE.md router to an always-on brain OS
- [[CLAUDE.md as a Router]]: the auto-loaded file that says where things live (and whether you need one at all)
- [[Agent Memory Patterns]]: auto memory, instruction-maintained memory, hot caches, learning journals, memory stores
- [[Claude Code Auto Memory]]: memory Claude writes for itself, and how to keep it portable
- [[LLM Wiki]]: an index-driven wiki of linked markdown pages that Claude maintains
- [[Semantic Search]]: retrieval by meaning, and where it fails
- [[Knowledge Graphs]]: entities and typed relationships for multi-hop questions
- [[Always-On Brain OS]]: continuously syncing, autonomous memory
- [[Design for Retrieval]]: shape how you store data around the questions you'll ask
- [[Context vs Connections]]: store lasting context; keep live data reachable
- [[Keyword vs Semantic vs Graph Retrieval]]: side-by-side comparison
- [[Tool-Agnostic Context Files]]: one set of instructions, memory and skills across agents

## Techniques

| Technique | Builds | Area |
|---|---|---|
| [[Context Hygiene Routine]] | Session habits that keep context lean | Claude Code |
| [[Keep CLAUDE.md Lean]] | An audited, self-maintaining CLAUDE.md | Claude Code |
| [[Plan-First Workflow]] | Plan → questions → approve → execute, optionally with two models | Claude Code |
| [[Build Verification into Every Task]] | Definition of done, runtime and screenshot checks, lint gates | Claude Code |
| [[Evidence-Gated Completion Ledger]] | A GATES.md whose runnable checks decide when work is done | Claude Code |
| [[Parallel Sessions with Git Worktrees]] | Isolated parallel agent sessions | Claude Code |
| [[Route Tasks to the Right Claude Model]] | A model-routing rule and its configuration | Models |
| [[Workflow Audit into Skills]] | A skills backlog mined from your recurring work | Skills |
| [[Build a Skill from a Successful Run]] | A SKILL.md distilled from a real run | Skills |
| [[Audit Skill Descriptions and Triggers]] | One-job skill descriptions that trigger when they should | Skills |
| [[Skill Improvement Loop]] | Skills that improve after every failure and prove they earn their tokens | Skills |
| [[Build a Reference-Rich Skill]] | A SKILL.md router to reference files and proven scripts | Skills |
| [[Grill Me Interview Skill]] | An interview that pulls knowledge out of your head | Skills |
| [[Build a STORM Multi-Perspective Research Skill]] | A five-lens research skill with contradiction mapping and citation verification | Research |
| [[Set Up Claude Research Connectors]] | Research connectors that ground citations in real, clickable sources | Research |
| [[Tests-First Goal Loop]] | An unattended /goal run gated on tests | Loops |
| [[Multi-Agent Review and Scoring Loops]] | Critic panels, persona reviews, score-maximising loops | Loops |
| [[Schedule Recurring Claude Tasks]] | A skill that runs on a schedule | Automation |
| [[Sync a Workspace to an Always-On Cloud Agent]] | 24/7 routines on a cloud agent sharing your skills and memory | Automation |
| [[Configure Safe Autonomy Permissions]] | Allow/deny rules and drafts-only guardrails | Automation |
| [[Build an Event-Triggered Managed Agent]] | An app event starts a graded, memory-backed agent session | Automation |
| [[Build an Agentic OS Dashboard]] | Dashboard buttons that run skills headlessly, plus observability panels | Agentic OS |
| [[Set Up Claude Cowork]] | A complete Cowork setup in seven steps | Cowork |
| [[Build a Context Map for a Connected Tool]] | A map of a connected tool (e.g. Notion) so Claude can navigate it | Cowork |
| [[Write Anti-AI Writing Rules]] | A writing-rules file that removes AI-writing tells | Cowork |
| [[Create and Reuse a Claude Design System]] | A design system from an inspiration image, reused across site and brand assets | Design |
| [[Build a Distinctive Site with Design Skills]] | A generate → refine → review chain for sites | Design |
| [[Build a Scroll-Driven Landing Page]] | An interview-led, scroll-driven landing page with keyframe checks | Design |
| [[Benchmark-Driven Design Critique]] | A measured gap report and critic loop against a benchmark design | Design |
| [[Build Product UI from a Component Registry]] | Consistent app, dashboard and mobile UI from registry components | Design |
| [[Generate On-Brand Images from Claude Code]] | An image-model skill with brand references and contact-sheet selection | Media |
| [[Storyboard-First AI Video and Motion Graphics]] | Storyboard → agent-written build prompt → targeted revisions | Media |
| [[Build a Brand-Aware Marketing Project]] | A brand-context project that produces sites, ads, reels and a creative tracker | Marketing |
| [[Second Brain Pain-Point Audit]] | A per-folder diagnosis of which brain level each part needs | Second brain |
| [[Build a Level 1 Second Brain]] | A CLAUDE.md router with context, decisions and projects folders | Second brain |
| [[Bootstrap an LLM Wiki from the Karpathy Gist]] | A raw/wiki vault scaffolded from the gist, with capture, lint and backup | Second brain |
| [[Ingest Sources into an LLM Wiki]] | A wiki folder and an ingest workflow | Second brain |
| [[Add a Journal and Personal CRM to a Second Brain]] | Journal and people layers on top of a wiki | Second brain |
| [[Port a Claude Code Brain to Other Agents]] | AGENTS.md bridges, shared skills, cross-machine sync | Second brain |
| [[Tiered Lookup Routing]] | A lookup order from curated context to live systems | Second brain |
| [[Add Semantic Search to One Folder]] | Vector search over one high-volume folder | Second brain |
| [[Build a Knowledge Graph Layer]] | An entity/relationship layer | Second brain |

## Tools

- **Anthropic:** [[Claude Code]] · [[Claude Cowork]] · [[Claude Design]] · [[Claude Managed Agents]] · [[Claude in Chrome]] · [[Claude Deep Research]]
- **Other agent harnesses:** [[OpenAI Codex]] · [[Hermes Agent]] · [[OpenClaw]]
- **Skills:** [[Unlazy]] · [[Scrollcraft]]
- **Design and media:** [[shadcn]] · [[Higgsfield]]
- **Research and retrieval:** [[Consensus]] · [[Obsidian]] · [[Qdrant]] · [[LightRAG]] · [[GBrain]] · [[Syncthing]]

## People

- **Creators:** [[AI LABS]] · [[Chase AI]] · [[David Stuckler]] · [[Jack Roberts]] · [[Jay E]] · [[Matt Wolfe]] · [[Nate Herk]] · [[Ras Mic]] · [[Sergei Chyrkov]] · [[Simon Pittman]] · [[The Coding Sloth]]
- **Referenced:** [[Andrej Karpathy]] · [[Barry Zhang]] · [[Garry Tan]] · [[Greg Isenberg]] · [[Leon Lin]] · [[Mahesh Murag]] · [[Matt Pocock]]

---
Vault rules live in `CLAUDE.md`. Every ingest is recorded in [[Ingest Log]].
