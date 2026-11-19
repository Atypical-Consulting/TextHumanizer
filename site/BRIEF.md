# BRIEF: humaniser-texte site

**Self-authored under explicit creative delegation.** Philippe Matray (Atypical Consulting) asked for a GitHub Pages site built with scroll-craft and left the creative questions without preference. The answers below are authored decisions, not user quotes. Evidence (real numbers, real texts) is marked as such; everything else is an assumption to revisit.

## What this is and who it is for

A landing page for `humaniser-texte`, an open-source Claude skill and Claude Code plugin that rewrites AI-generated text so it reads human, in French and English. Audience: developers, consultants and creators who use Claude Code or Claude.ai and publish on LinkedIn, by email, on YouTube or on a blog. They are tired of posts that open with "In today's fast-paced world".

- **What the visitor must believe by the end:** this skill fixes the writing, not just the symptoms, and it proves it with numbers.
- **The one action:** install the plugin. One label everywhere: **Install the plugin**. It reveals the two commands with a copy button.
- **Language:** English (decided: widest audience). French appears only inside the real FR examples.

## The eight topics

1. **Vibe in three to five words:** an editor's red pen, calm, exact, a little dry. References: a proofreader's marked-up galley proof; the typography of a good newspaper corrections column; the moment in a film edit when a scene is recut and suddenly works.
2. **The scroll journey:** (1) a wall of AI text you recognise instantly; (2) the tics light up, one family at a time; (3) the text repairs itself under the scroll, line by line, while a score climbs; (4) proof: four real before/after pairs and the benchmark; (5) the honest part: what it does not do; (6) install.
3. **Energy curve:** quiet and slightly uncomfortable at the start, building through the diagnosis, a sharp release at the repair, then calm and factual for the proof, quiet confidence at the close.
4. **Feeling, stage by stage, and the one moment:** recognition and a wince, then amused complicity, then relief, then trust, then respect for the honesty, then ease. The moment to remember: watching a ChatGPT LinkedIn post rewrite itself as you scroll, with the score going from 32 to 100.
5. **One thing no other site does:** the page's own copy is the demo. The hero text is genuinely AI-written and gets humanised by the scroll, using the real output of the skill, not a mock.
6. **Distance from premium-minimal:** editorial. Paper and ink, one red correction accent, a serif for the text being edited, a mono for measures. No gradients, no glow.
7. **One unbroken world or distinct scenes:** distinct scenes. Chapters of an edit, not a camera flight.
8. **Assets already available:** no photos or footage, no image-generation key in the build environment so far. Real material in `site/content/examples.json`: four AI-written originals, the skill's rewrites, the measures before/after, the phrases removed. Brand: Atypical Consulting, site https://atypical.consulting. The page is typographic by nature; that is the route, not a fallback.

## Feeling curve (draft, one line per act)

| Act | Feeling | What causes it |
|---|---|---|
| 1 | Recognition, a wince | A full-screen AI LinkedIn post, rocket emoji and all, set like a real feed card |
| 2 | Amused complicity | Each tic family is marked in the margin in red, with its name (em dash, rule of three, "it's not X, it's Y") |
| 3 | **Relief (the peak)** | The scroll drives the edit: struck words fall away, replacements set in, the score meter climbs 32 → 100 |
| 4 | Trust | Four real before/after pairs, FR and EN, with their measures; the benchmark 65/65 vs 49/65 |
| 5 | Respect | "What it will not do": invent an anecdote, a figure, a quote. The fact-check example (.NET 8 support ended 10 Nov 2026) with its source |
| 6 | Ease | Install: two commands, copy button, link to the repo |

**The peak:** "You scroll and a ChatGPT post literally fixes itself, the score goes from 32 to 100." Lives in act 3, which gets the largest scroll span and the quietest act before it.

**Tell-someone sentence:** "It's the site where you watch an AI post turn into something a person would actually write."

**Authored silence:** a short beat of empty paper between act 2 and act 3, before the edit starts.

## Hard constraints from the product

- Only real numbers: 65/65 and 49/65 checks, scores 32/42/54/30 → 100/100/100/94, word counts from `examples.json`. No invented testimonials, no user counts, no stars.
- No em dash anywhere visible (also a skill rule and an author preference).
- The demo text must be the real skill output from `examples.json`, not rewritten for the site.
- Accessible with reduced motion: the before/after must still be readable as two static texts.
- Works on a phone: the edit sequence needs a separate portrait composition.

## Left for the build to decide

Grammar (the fingerprint registry starts empty), signature move implementation, navigation, close pattern, fonts, the exact device per act. Suggested lean: a "live surface" or "chaptered editorial" grammar, with the self-editing post as the signature move.
