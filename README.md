# TextHumanizer

**A Claude skill that rewrites LLM-generated text so it reads like a person wrote it. French and English, with one skill per language of your request.**

[![MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757.svg)](https://code.claude.com/docs/en/plugins)
[![Site](https://img.shields.io/badge/site-GitHub%20Pages-222.svg)](https://atypical-consulting.github.io/TextHumanizer/)

Paste a LinkedIn post, an email, a YouTube script, a blog post or a description that ChatGPT, Claude or Gemini wrote. You get back a version that keeps every fact and sounds like you, plus the numbers that show what changed.

It is not a detector-evasion tool. AI tics are symptoms of soft writing: generic openers, predictable structure, borrowed enthusiasm, a flat rhythm. Fix the writing and the tics go with it.

## What it does

1. **Measures the original.** `scan.py` counts em dashes, emoji bullets, Markdown residue, typical AI phrases (around 50 per language), sentence-length variation and paragraph uniformity, checks the target format's constraints and gives an indicative score out of 100.
2. **Checks dated facts.** Software versions, support status, release dates, prices, statistics. It searches primary sources, keeps the author's own choices in the text and flags them with a source and a ready-to-use alternative, and corrects general claims that are simply wrong.
3. **Rewrites** with the best practices of the format: hook length and hashtags on LinkedIn, 30 to 90 words for a follow-up email, a hook in the first 15 seconds of a video script, 70-word paragraphs and informative headings for a blog post.
4. **Measures again** and fixes what is left.
5. **Reports**: the rewritten text, a before/after table, what changed, facts to check, and the concrete detail you could add. It never invents an anecdote, a figure or a quote to "sound human".

## Results

Four test texts (LinkedIn FR, follow-up email EN, YouTube script FR, blog post EN), 65 checks in total, run with and without the skill on the same model.

| | With skill | Without skill |
|---|---|---|
| Checks passed (final iteration) | **65 / 65** | 49 / 65 |
| Invented details in the rewrite | 0 of 4 texts | 3 of 4 texts |
| Before/after measures in the answer | 4 of 4 | 0 of 4 |
| Indicative score (before → after) | 30-54 → 94-100 | not measured |

Details and method: [BENCHMARK.md](BENCHMARK.md). The test cases live in [`plugins/text-humanizer/skills/text-humanizer/evals/`](plugins/text-humanizer/skills/text-humanizer/evals/) and run with `claude plugin eval`.

## Install

### Claude Code

```bash
/plugin marketplace add Atypical-Consulting/TextHumanizer
```
```bash
/plugin install text-humanizer@text-humanizer
```

Then just paste a text and say it sounds like AI, or invoke it directly. The plugin ships the same skill twice, one per language of your request (the text itself can be English or French in both):

```
/text-humanizer:text-humanizer      requests written in English
/text-humanizer:humaniser-texte     requests written in French
```

### Claude.ai and other agents

Download either folder, [`skills/text-humanizer`](plugins/text-humanizer/skills/text-humanizer/) (English) or [`skills/humaniser-texte`](plugins/text-humanizer/skills/humaniser-texte/) (French), keep `references/` and `scripts/`, zip it and upload it as a skill in Claude.ai, or place it in your agent's skill directory. Both are self-contained.

### Using the scanner on its own

```bash
python3 plugins/text-humanizer/skills/text-humanizer/scripts/scan.py text.txt --lang en --format linkedin
python3 plugins/text-humanizer/skills/text-humanizer/scripts/scan.py --compare before.txt after.txt --lang fr --format email
```

Formats: `linkedin`, `email`, `youtube`, `blog`, `description`. Python 3.9+, no dependencies. Each skill folder carries an identical copy of `scan.py`; its output labels are in French.

## What is in here

```
plugins/text-humanizer/skills/
├── text-humanizer/           English skill (requests written in English)
│   ├── SKILL.md              the procedure: measure, fact-check, rewrite, measure, report
│   ├── references/
│   │   ├── marqueurs-fr.md   AI markers in French, by family, with fixes
│   │   ├── markers-en.md     the same for English
│   │   └── formats.md        sourced best practices and numeric targets per format
│   ├── scripts/scan.py       the measuring tool (report or before/after table)
│   └── evals/                four test cases, 16-17 graders each
└── humaniser-texte/          French skill (requests written in French), same content in French
    ├── SKILL.md
    ├── references/           marqueurs-fr.md, markers-en.md, formats.md
    └── scripts/scan.py       identical copy
site/                         brief and real examples for the site
docs/                         the GitHub Pages site (built output)
```

## Honest limitations

- The score is indicative. It counts patterns; it does not judge whether a text is good, and it is not an AI detector.
- Fact-checking needs a web search tool. Without one, dated facts are flagged as unverified rather than checked.
- Best-practice numbers come from vendor studies (Hunter, Saleshandy, vidIQ, Nielsen Norman Group...). They are reference points; an author's proven habit wins.
- Voice matching is only as good as the samples you give it. Paste two or three of your own texts for the best result.

## En français

Ce skill réécrit un texte généré par une IA pour qu'il sonne écrit par un humain, en français ou en anglais. Il mesure le texte, vérifie les faits datés, applique les bonnes pratiques du format (post LinkedIn, email, script YouTube, article, description), puis rend le texte réécrit avec un tableau avant/après. Pour une demande rédigée en français, c'est le skill `humaniser-texte` (`/text-humanizer:humaniser-texte`). Installation : voir plus haut.

## Licence

MIT. See [LICENSE](LICENSE).
