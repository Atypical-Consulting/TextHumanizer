#!/usr/bin/env python3
"""Fills index.src.html with verbatim text from site/content/examples.json and
writes index.html. Every demo string comes from the JSON; every number in the
peak comes from scan.py run on the exact text shown at that step.

Run from the repo root: python3 scrollcraft/builds/text-humanizer/build.py
"""
import html, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "plugins/text-humanizer/skills/text-humanizer/scripts"))
import scan  # noqa: E402

EX = {e["case"]: e for e in json.load(open(os.path.join(ROOT, "site/content/examples.json"), encoding="utf-8"))}
esc = lambda s: html.escape(s, quote=False)
EMOJI = scan.EMOJI_RE

# ---------------------------------------------------------------- the peak --
LI = EX["linkedin-post-fr"]
UNITS = []
for para in LI["before"].split("\n\n"):
    UNITS += para.split("\n")
AFTER = LI["after"].strip().split("\n\n")
MAP = [None, 0, None, None, 1, 2, 3, 4, 5, 6]  # before unit -> after paragraph
assert len(UNITS) == 10 and len(AFTER) == 7

# tic marks per family: 1 typography, 2 stock phrases, 3 structure, 4 ending
MARKS = [
    ("Dans un monde en constante évolution", 2), ("n'est plus une option", 3), ("—", 1),
    ("véritablement", 2), ("transformateur", 2),
    ("Ce n'est pas qu'une simple mise à jour technique, c'est", 3), ("véritable", 2),
    ("Voici les 3 enseignements clés que nous en retirons", 3),
    ("**Anticiper**", 1), ("**Itérer**", 1), ("**Collaborer**", 1), ("cruciale", 2),
    ("joue un rôle essentiel", 2), ("En fin de compte", 2),
    ("Et vous, où en êtes-vous dans la modernisation de vos applications ?", 4),
    ("#DotNet #Modernisation #TransformationDigitale #Legacy #Innovation", 4),
]


def marked(text):
    spans = []
    for s, f in MARKS:
        for m in re.finditer(re.escape(s), text):
            if s == "véritable" and text[m.end():m.end() + 4] == "ment":
                continue
            spans.append((m.start(), m.end(), f))
    for m in EMOJI.finditer(text):
        spans.append((m.start(), m.end(), 0))
    spans.sort()
    out, pos = [], 0
    for a, b, f in spans:
        if a < pos:
            continue
        out.append(esc(text[pos:a]))
        cls = "tic tic--glyph" if f == 0 else "tic"
        out.append(f'<mark class="{cls}" data-f="{1 if f == 0 else f}">{esc(text[a:b])}</mark>')
        pos = b
    out.append(esc(text[pos:]))
    return "".join(out)


def state_text(k):
    out, prev_bullet = "", False
    for i, p in enumerate(UNITS):
        done = i < k
        txt = (AFTER[MAP[i]] if MAP[i] is not None else None) if done else p
        if txt is None:
            continue
        is_bullet = (not done) and p.startswith("✅")
        if out:
            out += "\n" if (prev_bullet and is_bullet) else "\n\n"
        out += txt
        prev_bullet = is_bullet
    return out


STATES = []
for k in range(11):
    t = state_text(k)
    if k == 0:
        assert t == LI["before"]
    if k == 10:
        t += "\n"
        assert t == LI["after"]
    m = scan.measure(t, "fr", "linkedin")
    STATES.append({
        "score": m["score humain /100"], "words": m["mots"], "emoji": m["émojis"],
        "emdash": m["tirets cadratins"], "phrases": m["formules typiques"], "bold": m["gras Markdown"],
        "tags": len(re.findall(r"(?<!\w)#\w+", t)), "cv": m.get("CV rythme"),
    })
assert STATES[0]["score"] == LI["measures"]["score humain /100"][0]
assert STATES[10]["score"] == LI["measures"]["score humain /100"][1]

LOG = [
    "Cut: the emoji opener, the stock phrase, the em dash.",
    "Rewritten: the hook is now the fact. Three months, .NET Framework 4.6 to .NET 8.",
    "Cut: “not just a technical update, a real strategic turning point”.",
    "Cut: “the 3 key lessons we take from it”.",
    "Bullet one becomes the one lesson, in the first person.",
    "Bullet two becomes a plain sentence about small steps.",
    "Bullet three loses “plays an essential role”.",
    "“At the end of the day” and the triple claim are gone. Same three results.",
    "The comment bait becomes a question for people still on .NET Framework.",
    "Five hashtags down to three.",
]

units_html = []
for i, p in enumerate(UNITS):
    kind = " u--bullet" if p.startswith("✅") else ""
    kind += " u--cut" if MAP[i] is None else ""
    after = f'<p class="u__a">{esc(AFTER[MAP[i]])}</p>' if MAP[i] is not None else ""
    units_html.append(
        f'<div class="u{kind}" data-i="{i}"><p class="u__b"><span class="u__ink">{marked(p)}</span></p>{after}</div>')
after_static = "".join(f"<p>{esc(p)}</p>" for p in AFTER)

# ------------------------------------------------------------- the hero card --
hero_paras = LI["before"].split("\n\n")
hero_html = "".join(f"<p>{esc(p)}</p>".replace("\n", "<br>") for p in hero_paras)

# ------------------------------------------------------------ the specimens --
TAG = {"linkedin-post-fr": "linkedin · fr", "email-relance-en": "email · en",
       "script-youtube-fr": "youtube · fr", "article-blog-en": "blog · en"}
L, E, Y, BL = "linkedin-post-fr", "email-relance-en", "script-youtube-fr", "article-blog-en"
SPECIMENS = [
    ("The opener", [("Dans un monde en constante évolution,", L), ("In today's fast-paced logistics landscape,", E),
                    ("In today's ever-evolving tech landscape,", BL), ("Salut à tous et bienvenue sur la chaîne !", Y)]),
    ("Not X, it's Y", [("la modernisation des applications legacy n'est plus une option — c'est une nécessité.", L),
                       ("modernizing legacy systems is not just a technical upgrade; it's a strategic imperative.", E),
                       ("Ce n'est pas simplement un assistant — c'est un véritable partenaire de développement.", Y)]),
    ("The em dash", [("— it was truly a pleasure connecting with you.", E),
                     ("— a testament to the transformative power of a well-executed migration.", E),
                     ("is not just a best practice — it's a strategic imperative.", BL)]),
    ("Bold triplets", [("✅ **Anticiper** : Une cartographie précise des dépendances est cruciale", L),
                       ("- **Pragmatic**: We focus on delivering tangible results.", E),
                       ("- **Assessment**: Inventory your dependencies and identify potential blockers.", BL),
                       ("1. La mise en place de l'environnement de travail.", Y)]),
    ("Connectors", [("Furthermore,", E), ("It's worth noting that", BL), ("Tout d'abord, il convient de noter que", Y),
                    ("En outre,", Y), ("In conclusion,", BL), ("En fin de compte,", L)]),
    ("Borrowed awe", [("un sujet fascinant", Y), ("un projet véritablement transformateur", L),
                      ("the vibrant ecosystem of libraries", BL), ("navigate this complex journey seamlessly", E),
                      ("cette aventure passionnante", Y)]),
    ("The sign-off", [("Et vous, où en êtes-vous dans la modernisation de vos applications ? 👇", L),
                      ("#DotNet #Modernisation #TransformationDigitale #Legacy #Innovation", L),
                      ("Alors, sans plus attendre, plongeons ensemble dans cette aventure passionnante !", Y)]),
]
spec_html = []
for name, quotes in SPECIMENS:
    items = []
    for q, case in quotes:
        assert q in EX[case]["before"], (q, case)
        lang = EX[case]["lang"]
        items.append(f'<li><q lang="{lang}">{esc(q)}</q><span class="tag">{TAG[case]}</span></li>')
    spec_html.append(f'<article class="slip"><h3>{esc(name)}</h3><ul>{"".join(items)}</ul></article>')

tot = {k: sum(scan.measure(e["before"], e["lang"], e["format"])[k] for e in EX.values())
       for k in ("formules typiques", "tirets cadratins", "émojis", "mots")}
tot_after = {k: sum(scan.measure(e["after"], e["lang"], e["format"])[k] for e in EX.values())
             for k in ("formules typiques", "tirets cadratins", "émojis", "mots")}

# ---------------------------------------------------------------- the report --
ORDER = [E, BL, Y, L]
TITLE = {E: "Sales follow-up email", BL: "Blog post", Y: "YouTube intro script", L: "LinkedIn post"}
ROWS = [("words", "mots"), ("rhythm (CV)", "CV rythme"), ("em dashes", "tirets cadratins"),
        ("emoji", "émojis"), ("stock phrases", "formules typiques"), ("score /100", "score humain /100")]
tabs, panels = [], []
for n, c in enumerate(ORDER):
    e = EX[c]
    sel = "true" if n == 0 else "false"
    tabs.append(f'<button role="tab" id="tab-{c}" aria-controls="panel-{c}" aria-selected="{sel}" '
                f'tabindex="{0 if n == 0 else -1}">{TAG[c]}</button>')
    rows = "".join(
        f'<tr><th scope="row">{lab}</th><td>{e["measures"][key][0]}</td><td>{e["measures"][key][1]}</td></tr>'
        for lab, key in ROWS)
    removed = "".join(f"<li><s>{esc(p)}</s></li>" for p in e["phrases_removed"])
    panels.append(f'''<section class="case" role="tabpanel" id="panel-{c}" aria-labelledby="tab-{c}" data-case="{c}">
  <h3 class="case__title">{TITLE[c]} <span class="tag">{TAG[c]}</span></h3>
  <div class="case__cols">
    <div class="case__col case__col--before"><p class="case__label">Before: the AI draft, {e["measures"]["mots"][0]} words</p><div class="case__text" lang="{e["lang"]}">{esc(e["before"])}</div></div>
    <div class="case__col case__col--after"><p class="case__label">After: the skill's rewrite, {e["measures"]["mots"][1]} words</p><div class="case__text" lang="{e["lang"]}">{esc(e["after"].rstrip())}</div></div>
  </div>
  <div class="case__meta">
    <table class="measures"><caption>Measured by scan.py</caption><thead><tr><th scope="col"></th><th scope="col">before</th><th scope="col">after</th></tr></thead><tbody>{rows}</tbody></table>
    <div class="removed"><p class="case__label">Phrases removed</p><ul lang="{e["lang"]}">{removed}</ul></div>
  </div>
</section>''')

src = open(os.path.join(HERE, "index.src.html"), encoding="utf-8").read()
fill = {
    "HERO": hero_html, "UNITS": "\n".join(units_html), "AFTER_STATIC": after_static,
    "STATES": json.dumps(STATES), "LOG": json.dumps(LOG, ensure_ascii=False),
    "SPECIMENS": "\n".join(spec_html), "TABS": "".join(tabs), "PANELS": "\n".join(panels),
    "TOT_PHRASES": str(tot["formules typiques"]), "TOT_DASH": str(tot["tirets cadratins"]),
    "TOT_EMOJI": str(tot["émojis"]), "TOT_WORDS": str(tot["mots"]), "TOT_WORDS_AFTER": str(tot_after["mots"]),
    "S0_SCORE": str(STATES[0]["score"]), "S0_WORDS": str(STATES[0]["words"]), "S0_EMOJI": str(STATES[0]["emoji"]),
    "S0_DASH": str(STATES[0]["emdash"]), "S0_PHRASES": str(STATES[0]["phrases"]), "S0_BOLD": str(STATES[0]["bold"]),
    "S0_TAGS": str(STATES[0]["tags"]), "S0_CV": str(STATES[0]["cv"]),
}
assert all(v == 0 for v in (tot_after["formules typiques"], tot_after["tirets cadratins"], tot_after["émojis"]))
for k, v in fill.items():
    src = src.replace("{{" + k + "}}", v)
assert "{{" not in src, re.findall(r"\{\{\w+\}\}", src)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(src)
print("ok", STATES[0]["score"], "->", STATES[10]["score"], tot, tot_after)
