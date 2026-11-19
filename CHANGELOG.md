# Changelog

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
