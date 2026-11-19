# Changelog

## 1.2.0 (2026-11-19)

- Skills renamed by language: `text-humanizer-en` and `text-humanizer-fr` (`/text-humanizer:text-humanizer-en`, `/text-humanizer:text-humanizer-fr`).
- Each skill now handles only texts in its own language: it keeps only its own marker catalogue, always runs `scan.py` with its language, and hands a text in the other language to the other skill.

## 1.1.0 (2026-11-19)

- Two skills with the same behaviour, one per language of the request:
  - `text-humanizer` (English): `SKILL.md` and `references/formats.md` translated into English. Use `/text-humanizer:text-humanizer`.
  - `humaniser-texte` (French): the original French skill, renamed. Use `/text-humanizer:humaniser-texte`.
- Each description says which requests it covers, so the two do not compete. The text to fix can be English or French in both.
- Each skill is self-contained: both marker catalogues and an identical copy of `scan.py`. The eval cases stay in `text-humanizer/evals/`.

## 1.0.0 (2026-11-17)

First public release.

- Skill `text-humanizer`: measure, fact-check, rewrite, measure, report. French and English.
- `scan.py`: report and `--compare` modes, format checks for LinkedIn, email, YouTube script, blog and description, indicative score out of 100.
- References: AI markers catalogue in French and English, sourced best practices per format.
- Four eval cases with 65 graders in total, runnable with `claude plugin eval`.
- Findings from testing that shaped the rules:
  - A fact that describes the author's own work (a target version) is kept and flagged; a general claim that is wrong is corrected and flagged.
  - No invented framing about the conversation with the recipient ("as I didn't get to mention").
  - Each run uses its own temp folder: two parallel runs overwrote a shared `/tmp` file.
  - `--lang` is always passed: auto-detection failed on a short mixed text.
