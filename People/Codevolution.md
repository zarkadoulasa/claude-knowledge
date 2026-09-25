---
type: person
role: "Creator — runs the Codevolution YouTube channel (web-dev tutorials); presenter goes by gopinav"
links: ["https://github.com/gopinav"]
sources: ["[[Codevolution - What Jev Is and How to Use It]]"]
tags: [topic/models]
---

# Codevolution

## Who

Codevolution is a long-running web-development tutorial YouTube channel. In [[Codevolution - What Jev Is and How to Use It]] the presenter walks through the TypeSafe Jev model from a developer's angle, including a full TypeScript SDK demo. The demo repo used in the video is published under the **gopinav** GitHub account (https://github.com/gopinav/jev-demo), which is how the presenter is identified — the name isn't spoken aloud in the video. The presenter's broader web-dev focus and the gopinav identity are external context, not stated in the video itself.

## In this vault

- [[Codevolution - What Jev Is and How to Use It]] — creator. A 22-minute, developer-focused explainer of Jev: what it is, the System 1 framing, cost, the state/questions/answers model, the three question types, and a Playground-then-TypeScript-SDK walkthrough.

## Ideas associated with them

- **"Smart if statement" framing of Jev** — the clearest one-line mental model in the batch: Jev handles the branching decisions you can't express in plain code (e.g. "does this customer sound frustrated?"), while ordinary conditions (3+ items → free delivery) stay in code.
- **Plain-English breakdown of Noul / Choice / Score** — exactly what each question type returns: Noul → probability of "yes" (low = confidently no, not unsure); Choice → selected option + per-option probabilities + confidence; Score → weighted-average score across described, 0-indexed levels + level probabilities + confidence + a legend.
- **State + named questions → per-question answers**, with multiple questions batched into one `client.system1(...)` call and evaluated independently in parallel.
- **Clear "when NOT to use Jev" guidance** — reach for a text model when you need to write, summarize, or generate code; keep exact computations (arithmetic, counting, date comparison) in code.

## Related

- [[Jev]]
