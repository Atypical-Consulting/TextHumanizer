#!/usr/bin/env python3
"""Mesure les marqueurs mécaniques d'écriture IA dans un texte (FR/EN).

Usage :
    python3 scan.py texte.txt [--lang fr|en] [--format linkedin|email|youtube|blog|description]
    python3 scan.py --compare avant.txt apres.txt [--lang ...] [--format ...]
    echo "texte" | python3 scan.py - [...]

Sortie : rapport lisible, ou tableau avant/après avec --compare.
Ne couvre que ce qui se détecte par motif ou se compte : typographie, lexique,
rythme, contraintes de format. Structure et ton restent à juger à la lecture.
"""
import argparse
import re
import statistics
import sys

FR_PHRASES = [
    r"dans un monde en (constante|perp[ée]tuelle) [ée]volution", r"[àa] l'[èe]re (du|de l'|de la|des)",
    r"dans le paysage", r"aujourd'hui plus que jamais", r"vous [êe]tes-vous d[ée]j[àa] demand[ée]",
    r"ce n'est pas .{1,60}, c'est", r"il ne s'agit pas (seulement|uniquement|simplement)",
    r"non seulement", r"\btout d'abord\b", r"\ben outre\b", r"\bpar ailleurs\b", r"\bde plus\b",
    r"\ben conclusion\b", r"\ben somme\b", r"\ben fin de compte\b", r"il convient de (noter|souligner)",
    r"il est (important|essentiel|crucial) de", r"jou(e|er|ent) un r[ôo]le (essentiel|cl[ée]|crucial|majeur|central)",
    r"marqu(e|er|ent) un tournant", r"plong(er|eons|ez) (au c[œo]eur|dans|ensemble)", r"naviguer dans",
    r"ouvr(ir|e|ent) la voie", r"repousser les limites", r"pierre angulaire", r"lib[ée]rer (le|tout le) potentiel",
    r"fa[çc]onner l'avenir", r"un monde de possibilit[ée]s", r"tirer parti", r"dans cet article",
    r"dans (la|cette) vid[ée]o d'aujourd'hui", r"sans plus attendre",
    r"et vous, qu'en pensez-vous", r"\bcrucial(e|es|aux)?\b", r"\bfascinant(e|es|s)?\b", r"\bpassionnant(e|es|s)?\b",
    r"\br[ée]volutionn(aire|aires|ent|e)\b", r"\btransformat(eur|rice|eurs|rices)\b", r"\bincontournable(s)?\b",
    r"\bvertigineu(x|se|ses)\b", r"\bv[ée]ritable(s|ment)?\b", r"\bsynergie(s)?\b", r"\bholistique(s)?\b",
    r"\blevier(s)?\b", r"\b[ée]cosyst[èe]me(s)?\b", r"\brobuste(s)?\b", r"\bj'ai le plaisir\b", r"ravi(e)? d'annoncer",
    r"essentiel(le)? et crucial(e)?", r"complexe et nuanc[ée]", r"clair et concis",
    r"cependant, il est important", r"le r[ée]sultat \?",
]
EN_PHRASES = [
    r"in today's (fast-paced|digital|ever)", r"ever-evolving", r"in the (digital age|realm of)",
    r"have you ever wondered", r"let's dive", r"\bdelv(e|es|ing)\b", r"\btapestry\b", r"\btestament\b",
    r"\brealm\b", r"\blandscape\b", r"\bnavigat(e|ing)\b", r"\bembark\b", r"\bunlock(ing)?\b", r"\bunleash\b",
    r"\bharness\b", r"\bleverag(e|ing)\b", r"\belevate\b", r"\bfoster\b", r"\bempower\b", r"\bseamless(ly)?\b",
    r"\brobust\b", r"\bpivotal\b", r"\bcrucial\b", r"\bparamount\b", r"\btransformative\b", r"game[- ]changer",
    r"cutting-edge", r"groundbreaking", r"\bintricate\b", r"\bmultifaceted\b", r"\bmeticulous(ly)?\b",
    r"\bvibrant\b", r"\bholistic\b", r"\bsynergy\b", r"it's not .{1,60}, it's", r"not only .{1,60} but also",
    r"not just .{1,40}; it's", r"\bfurthermore\b", r"\bmoreover\b", r"\badditionally\b", r"in conclusion",
    r"it's worth noting", r"it's important to (note|remember|consider)", r"at the end of the day",
    r"plays? a (pivotal|crucial|key|vital) role", r"paving the way", r"at the forefront", r"here's the thing",
    r"in this article", r"hope this (email|message) finds you", r"what do you think\?", r"strategic imperative",
    r"excited to (share|announce)", r"the result\?",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿✅⭐]")
URL_RE = re.compile(r"https?://\S+")


def sentences(text):
    flat = re.sub(r"\s+", " ", URL_RE.sub("URL", text))
    parts = re.split(r"(?<=[.!?…])\s+", flat)
    return [p for p in parts if p.split()]


def detect_lang(text):
    fr = len(re.findall(r"\b(le|la|les|des|est|une|que|pour|dans|avec)\b", text, re.I))
    en = len(re.findall(r"\b(the|and|is|are|that|with|for|this|you)\b", text, re.I))
    return "fr" if fr >= en else "en"


def measure(text, lang, fmt):
    m = {}
    words = text.split()
    m["mots"] = len(words)
    m["tirets cadratins"] = text.count("—")
    m["demi-cadratins en incise"] = len(re.findall(r"\s–\s", text))
    m["émojis en début de ligne"] = len(re.findall(r"(?m)^\s*(?:[-*•]\s*)?" + EMOJI_RE.pattern, text))
    m["émojis"] = len(EMOJI_RE.findall(text))
    m["gras Markdown"] = len(re.findall(r"\*\*[^*]+\*\*", text))
    m["puces « **Mot** : »"] = len(re.findall(
        r"(?m)^\s*(?:[-*•]|\d+[.)]|" + EMOJI_RE.pattern + r")?\s*\*\*[^*]+\*\*\s*:", text))
    m["titres Markdown"] = len(re.findall(r"(?m)^#{1,6}\s", text))
    m["séparateurs ---"] = len(re.findall(r"(?m)^\s*-{3,}\s*$", text))
    m["liens utm chatgpt"] = len(re.findall(r"utm_source=chatgpt", text))
    m["listes numérotées (lignes)"] = len(re.findall(r"(?m)^\s*\d+[.)]\s", text))
    if lang == "fr":
        m['guillemets droits'] = len(re.findall(r'"[^"\n]+"', text))
    hits = {}
    for p in (FR_PHRASES if lang == "fr" else EN_PHRASES):
        for h in re.finditer(p, text, re.I):
            k = h.group(0).lower()
            hits[k] = hits.get(k, 0) + 1
    m["_hits"] = hits
    m["formules typiques"] = sum(hits.values())

    lens = [len(s.split()) for s in sentences(text)]
    m["phrases"] = len(lens)
    if lens:
        mean = statistics.mean(lens)
        m["mots/phrase (moy.)"] = round(mean, 1)
        m["mots/phrase (min-max)"] = f"{min(lens)}-{max(lens)}"
        m["phrases ≤ 5 mots"] = sum(1 for l in lens if l <= 5)
        m["CV rythme"] = round(statistics.pstdev(lens) / mean, 2) if len(lens) >= 3 and mean else None
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    m["paragraphes"] = len(paras)
    if len(paras) >= 3:
        pl = [len(p.split()) for p in paras]
        m["CV paragraphes"] = round(statistics.pstdev(pl) / statistics.mean(pl), 2)
        m["mots/paragraphe (max)"] = max(pl)

    # Contraintes de format
    fc = []
    first_line = next((l.strip() for l in text.splitlines() if l.strip()), "")
    if fmt == "linkedin":
        tags = re.findall(r"(?<!\w)#\w+", text)
        links = URL_RE.findall(text)
        fc += [("accroche ≤ 210 caractères (avant « voir plus »)", len(first_line) <= 210, f"{len(first_line)} car."),
               ("pas d'émoji dans l'accroche", not EMOJI_RE.search(first_line), ""),
               ("hashtags ≤ 3", len(tags) <= 3, f"{len(tags)}"),
               ("pas de lien externe dans le corps", not links, f"{len(links)} lien(s)"),
               ("longueur ≤ 3000 caractères", len(text) <= 3000, f"{len(text)} car.")]
    elif fmt == "email":
        subj = re.search(r"(?im)^(?:subject|objet)\s*:\s*(.+)$", text)
        body = re.sub(r"(?im)^(?:subject|objet)\s*:.*$", "", text)
        bw = len(body.split())
        if subj:
            sw = len(subj.group(1).split())
            fc.append(("objet de 2 à 7 mots", 2 <= sw <= 7, f"{sw} mots"))
            fc.append(("objet sans deux-points ni guillemets", not re.search(r'[:"«»]', subj.group(1)), ""))
        fc.append(("corps ≤ 125 mots (relance : viser 30-90)", bw <= 125, f"{bw} mots"))
        fc.append(("une seule question / demande", len(re.findall(r"\?", body)) <= 1, f"{body.count('?')} « ? »"))
    elif fmt == "youtube":
        wpm = 150
        fc += [("mots/phrase moyen ≤ 14 (écrit pour l'oral)", (m.get("mots/phrase (moy.)") or 0) <= 14,
                f"{m.get('mots/phrase (moy.)')}"),
               ("aucune liste numérotée", m["listes numérotées (lignes)"] == 0, ""),
               ("pas d'ouverture « bienvenue sur la chaîne / today I'm going to »",
                not re.search(r"bienvenue sur (la|ma) cha[îi]ne|aujourd'hui (on va|nous allons)|today i'?m going to|welcome back to",
                              " ".join(text.split()[:30]), re.I), ""),
               ("durée orale estimée", True, f"~{round(m['mots'] / wpm * 60)} s à {wpm} mots/min")]
    elif fmt == "blog":
        fc += [("paragraphes ≤ 70 mots", (m.get("mots/paragraphe (max)") or 0) <= 70, f"max {m.get('mots/paragraphe (max)')}"),
               ("mots/phrase moyen ≤ 20", (m.get("mots/phrase (moy.)") or 0) <= 20, f"{m.get('mots/phrase (moy.)')}"),
               ("pas d'annonce du plan", not re.search(r"dans cet article|in this article|nous allons voir|we'll explore", text, re.I), "")]
    elif fmt == "description":
        fc += [("l'essentiel dans les 150 premiers caractères", True, f"« {text.strip()[:150]} »"),
               ("pas de paramètre utm chatgpt", m["liens utm chatgpt"] == 0, "")]
    m["_format"] = fc

    # Score : 100 moins des pénalités plafonnées, pour comparer avant/après
    pen = 0
    pen += min(25, 5 * (m["tirets cadratins"] + m["demi-cadratins en incise"]))
    pen += min(10, 3 * m["émojis en début de ligne"])
    pen += min(10, 3 * m["puces « **Mot** : »"])
    pen += min(10, 2 * (m["titres Markdown"] + m["séparateurs ---"] + m["liens utm chatgpt"]))
    pen += min(30, 4 * m["formules typiques"])
    cv = m.get("CV rythme")
    if cv is not None and cv < 0.45:
        pen += 15 if cv < 0.35 else 8
    if m.get("CV paragraphes") is not None and m["CV paragraphes"] < 0.35:
        pen += 5
    pen += 3 * sum(1 for _, ok, _ in fc if not ok)
    m["score humain /100"] = max(0, 100 - pen)
    return m


ROWS = ["mots", "phrases", "mots/phrase (moy.)", "mots/phrase (min-max)", "phrases ≤ 5 mots", "CV rythme",
        "paragraphes", "CV paragraphes", "tirets cadratins", "demi-cadratins en incise", "émojis",
        "émojis en début de ligne", "puces « **Mot** : »", "gras Markdown", "titres Markdown", "séparateurs ---",
        "listes numérotées (lignes)", "liens utm chatgpt", "guillemets droits", "formules typiques", "score humain /100"]


def report(m, lang):
    out = [f"Langue : {lang}", "", "## Mesures"]
    out += [f"- {k} : {m[k]}" for k in ROWS if k in m and m[k] not in (0, None) or k in ("mots", "score humain /100", "CV rythme")]
    out.append("\n## Formules typiques")
    out += [f"- « {k} » ×{v}" for k, v in sorted(m["_hits"].items(), key=lambda x: -x[1])] or ["- aucune"]
    if m["_format"]:
        out.append("\n## Contraintes du format")
        out += [f"- [{'ok' if ok else 'À REVOIR'}] {name} {('(' + d + ')') if d else ''}" for name, ok, d in m["_format"]]
    out.append("\nRepères : CV rythme < 0,45 = plat ; > 0,6 = varié. Score indicatif, pas un détecteur.")
    return "\n".join(out)


def compare(a, b, lang):
    out = [f"Langue : {lang}", "", "| Mesure | Avant | Après |", "|---|---|---|"]
    for k in ROWS:
        if k in a or k in b:
            va, vb = a.get(k, "-"), b.get(k, "-")
            if va in (0, None, "-") and vb in (0, None, "-") and k not in ("score humain /100",):
                continue
            out.append(f"| {k} | {va if va is not None else '-'} | {vb if vb is not None else '-'} |")
    left = {k: v for k, v in b["_hits"].items()}
    out.append("\nFormules restantes : " + (", ".join(f"« {k} »" for k in left) if left else "aucune"))
    if b["_format"]:
        out.append("\nContraintes du format (après) :")
        out += [f"- [{'ok' if ok else 'À REVOIR'}] {n} {('(' + d + ')') if d else ''}" for n, ok, d in b["_format"]]
    return "\n".join(out)


def read(path):
    return sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--compare", action="store_true", help="comparer deux fichiers : avant puis après")
    ap.add_argument("--lang", choices=["fr", "en"])
    ap.add_argument("--format", choices=["linkedin", "email", "youtube", "blog", "description"])
    a = ap.parse_args()
    if a.compare:
        if len(a.paths) != 2:
            ap.error("--compare attend deux fichiers")
        t1, t2 = read(a.paths[0]), read(a.paths[1])
        lang = a.lang or detect_lang(t1)
        print(compare(measure(t1, lang, a.format), measure(t2, lang, a.format), lang))
    else:
        t = read(a.paths[0])
        lang = a.lang or detect_lang(t)
        print(report(measure(t, lang, a.format), lang))


if __name__ == "__main__":
    main()
