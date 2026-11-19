# Build report: the GitHub Pages site

Built with scroll-craft 0.3.1 on 2026-11-19. Published output in `docs/` (index.html, scrollcraft.js, scrollcraft.css, .nojekyll). All asset paths are relative, fonts come from Google Fonts, there are no images.

The brief (`site/BRIEF.md`) is self-authored under explicit creative delegation; nobody was interviewed. A copy with a build addendum (names changed, the curve as built) sits in `scrollcraft/builds/text-humanizer/BRIEF.md`.

## Where the page comes from

- `scrollcraft/builds/text-humanizer/index.src.html` is the hand-written page. `build.py` (same folder) fills it from `site/content/examples.json` and writes `index.html`, which is copied to `docs/`. The build folder is gitignored, so **`docs/index.html` is the final source of record**.
- Every demo string is taken verbatim from `examples.json`. `build.py` asserts that each quoted specimen is a substring of its original, that the edit sequence starts exactly at `before` and ends exactly at `after`, and that the endpoint scores match the JSON (32 and 100).
- Every number in the peak is scan.py's real output on the exact text on screen at that step. `build.py` imports `scan.py`, runs it on the 11 intermediate texts and embeds the results: 32, 42, 58, 67, 67, 69, 83, 93, 97, 97, 100. No number on the page is interpolated or invented. The two benchmark counters tick from 0 to their real values (65 and 49) when they come into view.

## Grammar, and why

**Live surface.** The product is a tool whose honest pitch is "watch what it does", and the brief's signature idea (the page's own copy is the demo) is exactly that grammar. The page is the skill's own procedure: input loaded and measured, tics marked, rewrite, report, limits, then an actual input. Section headings are report-sized, the chrome is an editor status bar, the close is two real command fields.

Why the other seven lost:

- **Filmic one-shot:** no footage, and the brief asks for distinct scenes, not a carried film.
- **Chaptered editorial:** the closest runner-up (paper, folios, restraint fit the vibe), but it would describe the edit rather than perform it.
- **Continuous world:** there is no geography to travel through.
- **Typographic poster:** the type here is evidence to read, not imagery at 40vw.
- **Gallery / catalog:** fits one act (the specimen drawer) but not a page whose question is "does it work", not "what are the options".
- **Split stage:** before/after is two-sided, but the peak needs the text to change in one place, and the brief's reduced-motion two-column view is the fallback, not the experience.
- **Rhythmic cutlist:** wrong energy for "calm, exact, a little dry".

## Signature move

**The scroll performs the edit.** On the pinned desk, the four tic families are underlined in red one at a time, then the visitor's scroll draws a red pen stroke through each AI paragraph, line by line. When the stroke completes, the paragraph is replaced by the skill's real rewrite (the paragraphs below glide into place with a FLIP transform, nothing animates height), an edit log names what changed in English, and the score, the word count and five other measures step to scan.py's reading of the new text. Coded in the page; the engine is untouched.

Tell-someone sentence: "It's the site where you watch an AI post turn into something a person would actually write."

## Fingerprint gate

The registry (`scrollcraft/FINGERPRINTS.md`) was empty, so the gate had nothing to clear: 6 of 6 against zero rows. The build's row is appended; it now constrains the next build.

## Journey and score

| Beat | Feeling | Device | Why this one |
|---|---|---|---|
| 1 Recognition | a wince | `flow` (static hero) | The input already loaded and measured: a truncated AI feed card, rocket first, with scan.py's 32/100 slip clipped over it |
| 2 Complicity | amused | `pan`, span 2.6 | Lateral travel reads as breadth: the same tics quoted from all four drafts, on specimen slips that settle in sequence |
| silence | anticipation | `flow`, 70svh | Empty paper and one status line before the peak (authored, not dead scroll) |
| 3 Relief (peak) | relief | `pin`, span 6 (largest on the page) | The frame holds while state advances: marks, ten strike-and-replace edits, score 32 to 100, resolve line |
| 4 Trust | calm, factual | `count` + tabs | Four real before/after pairs with scan.py tables, then 65/65 vs 49/65 ticking in |
| 5 Respect | respect | `reveal` | A false Python claim struck, the skill's correction wiped in; .NET 8 kept and flagged; the honest limits |
| 6 Ease | ease | `flow`, held | Two read-only command fields with Copy buttons, colophon below |

Five device families, none twice in a row, no scrub, kinetic, spotlight or drift (all banned by the grammar). Length: 15.1 viewport-heights on desktop, 17.8 on a 390x844 phone, 9.2 with reduced motion. That is past the 8 to 14 pacing reference; the extra is the reading of the report (long real texts), not pinned scroll. Not in the 13.6 to 13.8 band.

## Feel check

Done from the final contact sheets and full-size frames, after the build. It was not truly cold: I wrote the page, so treat this as a careful second read, not fresh eyes.

| Act | Intended | Felt | Change made |
|---|---|---|---|
| 1 | recognition, a wince | recognition: the rocket and the red 32 read as a verdict | none |
| 2 | amused complicity | amused at first, then browsing: seven similar slips at span 3 felt long | span cut from 3 to 2.6 |
| silence | anticipation | a pause, with a blinking cursor | none |
| 3 | relief | relief, and the largest visual change on the sheet | edit-mode notes raised from 0.5 to 0.7 opacity so they stay readable |
| 4 | trust | trust, a little dense | none (it is the proof; dense is honest) |
| 5 | respect | respect | none |
| 6 | ease | ease; the last screen holds with content | none |

The peak is the biggest change and holds the most scroll; the act before it is the quietest on the page; the close stands still with two usable inputs.

## What was verified

Server: `serve.mjs --root docs --port 4517`. Harness: `shoot.mjs` with installed Chrome.

| Run | Result | Contact sheet |
|---|---|---|
| Desktop 1440x900 | no dead scroll, all cues clear 4.5:1, 0 console errors, 0 failed requests | `lab/shots/sheet.png` |
| Phone 390x844 | same | `lab/mobile/sheet.png` |
| Reduced motion | no dead scroll, 0 errors; the peak becomes two static texts side by side (before with marks, after) with no pinned space; the drawer wraps into a grid | `lab/reduced/sheet.png` |

Fixes found by reading the sheets and full-size frames, then reshot: the hero was not sampled (made it a flow act); the phone peak's note slot covered the last line of the post (smaller galley type, filename hidden on phones); the install commands were cut off on phones (text fields became wrapping read-only textareas); the drawer held a still screen for 3vh under reduced motion (it now becomes a wrapped grid with no pin); the resolve line vanished during the desk's exit slide (window extended).

Also checked by script: tabs switch on click and arrow keys with roving tabindex; Copy writes the exact command to the clipboard and confirms; tab order follows the page (status bar first, then hero link, tabs, links, command fields); rail overflow 1984px at 1440 wide; no horizontal page overflow; the only em dashes on the page are inside the quoted AI originals.

Design-hook notes left standing: a static "tiny text" warning (the phone galley floors at 11.5px only on screens under about 760px tall; 12.8px on a 390x844 phone) and "positioned child clipped by overflow" (the phone note slot lives inside the pinned stage on purpose).

## What was not verified

- **A real phone.** Headless Chrome cannot reproduce iOS touch scrolling, sticky behaviour under the collapsing URL bar, or Safari's font rendering. There are no clips, so the iOS video issues do not apply.
- A compact 360x640 phone was not shot.
- Safari and Firefox were not tested.
- The page was not opened at the real GitHub Pages URL; Pages is not enabled. Relative paths were checked against a local server rooted at `docs/`.
- Screen reader output was not tested.
- The one dated fact on the page outside the verbatim demo text (.NET 8 end of support on 10 November 2026, linked to Microsoft's policy page) was not re-checked against the live page during this build.
