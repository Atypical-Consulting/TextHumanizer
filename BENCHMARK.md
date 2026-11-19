# Benchmark

How the skill was tested, and what the numbers mean.

## Method

- **Four test texts**, each a realistic AI-written draft with the usual tics:
  - `linkedin-post-fr`: a LinkedIn post announcing a .NET Framework 4.6 to .NET 8 migration (contains a fact that went stale on 10 November 2026: .NET 8 left support).
  - `email-relance-en`: a sales follow-up to a CTO met at a conference.
  - `script-youtube-fr`: the intro of a YouTube video about building an iOS app with Claude Code.
  - `article-blog-en`: a blog post about upgrading Python, with two false claims (3.13 is "the latest", 3.10 is "supported until 2027").
- **Two configurations** on the same model (Claude Opus 5.5): with the skill, and without any skill.
- **Each run sees only the user's message.** An early run that could read the grading criteria was discarded and rerun.
- **65 graders** (16 or 17 per case). Most are checked by script (`scan.py` measures, word counts, subject length, presence of a before/after table); the rest are judged by reading the output (facts kept, nothing invented, dated facts flagged with a source).

## Results by iteration

| Iteration | With skill | Without skill | Main change |
|---|---|---|---|
| 1 (3 cases, 6 checks each) | 18/18 | 14/18 | First draft |
| 2 (4 cases, 65 checks) | 64/65 (98.5 %) | 49/65 (75.8 %) | Fact-checking step, sourced format targets, before/after measures |
| 3 (4 cases, 65 checks) | **65/65** | 49/65 (baseline unchanged) | Rule against invented conversational framing, unique temp folders, author-choice vs general-claim distinction |

## Where the skill makes the difference

- **Fidelity.** Without the skill, the model adds details to sound lived-in: "I've been coding for years", "users didn't notice a thing", a 25 % speed-up quoted from memory. With the skill, suggestions for concrete details go to a separate "worth adding if you have it" section.
- **Format targets.** Without the skill, the blog rewrite doubled in length and broke the paragraph target. With it, every format constraint passed.
- **Measures.** Every answer with the skill includes a before/after table. Indicative scores went from 30-54 to 94-100.

## Where it does not

- **Fact-checking** of .NET and Python versions was also done by the model without the skill when web search was available. The skill guarantees the format (a "Facts to check" section with links and replacement wording), not the instinct.
- **Removing the obvious tics** (em dashes, "In today's fast-paced world") also happens without the skill, especially when the user has a saved preference against em dashes.

## Cost

About 15 % more tokens and 30 to 45 seconds more per text with the skill, mostly from web searches and the two scanner passes.

## Reproduce

From the skill folder, with Claude Code 2.1.269 or later:

```bash
cd plugins/humaniser-texte/skills/humaniser-texte
claude plugin eval . --allow-tools Write,Edit,Bash,WebSearch,WebFetch
```

These are real, billed model runs.
