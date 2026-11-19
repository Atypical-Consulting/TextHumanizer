# Fingerprints

Every site you build with **scroll-craft** gets one row here, appended after it
ships. The registry exists so your next build can prove it is a different page
rather than a re-skin of one you already made.

This file is **yours**. It starts empty on purpose: the gate is about not
repeating *yourself*, so it has nothing to say until you have built something.

The rules and the gate live in the skill's
`references/uniqueness.md`. Short version:

**A new build must differ from EVERY row below on at least 4 of the 6
dimensions.** Four against each row individually, not four on average across the
table. If a planned build fails, change the plan. Never edit a row to make room
for it.

The six dimensions are: **grammar**, **nav treatment**, **hero device**,
**act-sequence shape**, **close pattern**, **signature move**.

Dimension 6 is free, because a signature move is unique by definition. So the
gate really asks for three more out of the remaining five, and a build that
changes only grammar and world will fail it.

---

## The registry

| Build | Grammar | Nav treatment | Hero device | Act-sequence shape | Close pattern | Signature move | World | Port |
|---|---|---|---|---|---|---|---|---|
| text-humanizer (2026-11-19) | Live surface | Fixed bottom editor status bar: wordmark, section links with scrollspy, live scan.py score of the text on the desk, one CTA "Install the plugin" | Static flow: the input already loaded and measured (truncated AI feed card with a tilted scan.py slip, 32/100, clipped over it) | flow > pan (2.6) > authored silence (flow) > pin peak (6) > flow + count (report tabs) > flow + reveal > flow close; 7 blocks, about 15.1vh desktop, 9.2vh reduced motion | Held install sheet: two real read-only command fields with copy buttons, colophon below, no button island | Scroll-driven red-pen edit: the hand draws the strike through each AI paragraph, the real rewrite sets in with a FLIP glide, and the score steps through scan.py's actual reading of every intermediate text | Typographic paper and ink, one proof red, Source Serif 4 + IBM Plex Mono, no imagery | 4517 |


---

## What is taken

Add a bullet here whenever a build claims something a later build should avoid
reusing: a grammar, a nav treatment, a close pattern, a signature move, an
act-count-and-length band. The shared columns are what the next build inherits
as a constraint, so writing them down is the whole point.

- **Live surface** grammar with a bottom status-bar nav that carries a live measurement.
- **Hero = the input already measured** (document card plus a measurement slip clipped over it).
- **Close = read-only command fields with copy buttons.**
- **Signature: a scroll-drawn strike-and-replace edit with per-step real measurements.**
- Act band: 7 blocks at about 15vh.

---

## Appending a row

After shipping, add one line to the table and one bullet to **What is taken** if
the build claimed something new. Fill every column. Say what the build shares
with existing rows.

Rows are append-only. A build that has been superseded stays in the table,
because the space it occupies is still occupied.

---

## Worked example

The skill's author kept a registry of twelve builds across eight page grammars.
If you want to see what a filled-in table looks like, and which shapes tend to
collide, read `EXAMPLES.md` in the scroll-craft repository. Treat it as
illustration only: those rows are somebody else's builds and they do **not**
constrain yours.
