---
name: text-humanizer
description: Réécrit un texte généré par un LLM (ChatGPT, Claude, Gemini...) pour qu'il sonne écrit par un humain, en français ou en anglais. Supprime les tics de l'IA (tirets cadratins, règle de trois, « Ce n'est pas X, c'est Y », « Dans un monde en constante évolution », « crucial », « delve », émojis en tête de puce, rythme plat), applique les bonnes pratiques du format, vérifie les faits datés et mesure l'avant/après. Utilise ce skill dès que l'utilisateur colle un texte et veut le rendre plus naturel, moins ChatGPT, moins robot, plus « lui » ou le réécrire avec sa voix (post LinkedIn, article, email, script YouTube, description, page « À propos », newsletter), ou demande si son texte sonne IA avant de le publier, même sans le mot « humaniser ». Pas pour écrire un texte de zéro, traduire, corriger seulement l'orthographe, changer le registre d'un texte qu'il a écrit lui-même, ni juger si un tiers a utilisé une IA.
---

# Humaniser un texte écrit par un LLM

Le but n'est pas de « tromper un détecteur », c'est d'obtenir un texte que le lecteur a envie de lire : précis, juste, rythmé, avec une voix. Les tics de l'IA sont surtout des symptômes d'une écriture molle (formules creuses, structure prévisible, enthousiasme générique). Corriger le fond corrige les marqueurs ; maquiller les marqueurs sans toucher au fond produit un texte tout aussi plat.

Un texte généré a un deuxième défaut, moins visible : il affirme avec assurance des faits qui peuvent être faux ou périmés (une version de logiciel, une date, un chiffre). Un texte humanisé qui garde une erreur factuelle reste un mauvais texte, et c'est l'auteur qui en paiera le prix une fois publié.

## Déroulé

1. **Identifier la langue, le format et le registre.** Post LinkedIn, article, email, script vidéo, description... Lis la section du format dans `references/formats.md` : elle donne les bonnes pratiques et les cibles chiffrées (longueur d'accroche, nombre de mots, hashtags, liens).

2. **Mesurer le texte d'origine.** Enregistre-le dans un dossier temporaire à toi (`D=$(mktemp -d)`, jamais un chemin fixe comme `/tmp/x` qu'une autre session pourrait écraser), puis lance :
   ```bash
   python3 scripts/scan.py "$D/original.txt" --lang <fr|en> --format <linkedin|email|youtube|blog|description>
   ```
   Passe toujours `--lang` : la détection automatique se trompe sur les textes courts ou mixtes.
   Le script compte les marqueurs mécaniques (typographie, formules, rythme), vérifie les contraintes du format et donne un score indicatif sur 100. Les tics structurels et de ton demandent ta lecture.

3. **Lire le catalogue de la langue** : `references/marqueurs-fr.md` ou `references/markers-en.md`.

4. **Vérifier les faits datés.** Voir la section dédiée plus bas. Fais-le avant de réécrire : la réécriture peut dépendre de ce que tu trouves.

5. **Réécrire** selon les principes ci-dessous et les bonnes pratiques du format. Garde les faits, chiffres, noms, liens et l'intention. N'invente ni anecdote, ni chiffre, ni citation, ni détail « pour faire vrai », ni cadrage sur ce qui s'est dit ou pas dit avec le destinataire (« comme je n'ai pas eu le temps de le mentionner », « vous m'aviez parlé de... ») si l'utilisateur ne l'a pas dit. Ces ajouts sonnent humains, mais l'auteur devra assumer une affirmation fausse.

6. **Mesurer l'avant/après** et corriger ce qui reste :
   ```bash
   python3 scripts/scan.py --compare "$D/original.txt" "$D/reecrit.txt" --lang <fr|en> --format <format>
   ```
   Vise : zéro tiret cadratin, zéro formule typique, CV rythme ≥ 0,5, toutes les contraintes du format à « ok ». Si une contrainte reste « À REVOIR », corrige ou explique pourquoi c'est voulu.

7. **Rendre le résultat** au format décrit plus bas.

## Vérifier les faits datés

Repère dans le texte tout ce qui peut avoir changé depuis l'entraînement d'un modèle : versions de logiciels et statut de support, dates de sortie, prix, statistiques, intitulés de postes, lois et règlements, « le plus récent », « actuellement », « la dernière version ». Le texte d'origine a été écrit par un LLM, souvent avec des connaissances périmées, et ta propre mémoire peut l'être aussi.

- Si un outil de recherche web est disponible, vérifie chaque fait daté par une recherche, de préférence sur une source primaire (éditeur, documentation officielle, organisme public). Une ou deux recherches par fait suffisent.
- Sans outil de recherche, ne présente pas ta mémoire comme vérifiée : signale le fait comme « à vérifier » avec ce que tu crois savoir et la date de tes connaissances.
- Distingue deux cas :
  - **Un fait qui décrit le travail ou le choix de l'auteur** (« on a migré vers .NET 8 », « on cible Python 3.13 ») : c'est peut-être lui qui a raison. Garde-le dans le texte et signale le problème dans « Faits à vérifier », avec la source et une formulation de remplacement prête à l'emploi.
  - **Une affirmation générale sur le monde qui est fausse** (« 3.13 est la dernière version », « 3.10 est supporté jusqu'en 2027 ») : ne la laisse pas dans le texte comme vraie, surtout si elle pousse le lecteur à une mauvaise décision. Corrige-la ou retire-la, et montre dans « Faits à vérifier » ce que disait l'original, la source et ta correction.
- Ce que tu ajoutes toi-même pour corriger (une date de fin de support, un numéro de version) doit être sourcé comme le reste ; si tu ne l'as pas vérifié, ne l'écris pas ou marque-le « à vérifier ».
- Pense aux conséquences pour le lecteur : annoncer une migration vers une version qui n'est plus supportée, ou citer « la dernière version » alors qu'une autre vient de sortir, se fera relever en commentaire.
- Ne signale que ce qui est daté et vérifiable. Pas besoin de sourcer « le code legacy coûte cher à maintenir ».

## Principes de réécriture

**Couper avant de reformuler.** Une bonne part d'un texte IA est du remplissage : ouverture universelle, phrase qui annonce la suite, conclusion qui résume, nuance de politesse (« il est important de rappeler que »). Supprime d'abord. Un texte humanisé est souvent 20 à 40 % plus court.

**Entrer directement dans le sujet.** La première phrase porte une idée, un fait ou une scène, jamais un décor (« À l'ère du numérique... »).

**Varier le rythme pour de vrai.** Alterne des phrases très courtes (trois mots, parfois un seul) avec des phrases plus longues qui déroulent une idée. Les paragraphes aussi ont des tailles inégales. Un rythme uniforme se sent même quand le vocabulaire est bon.

**Concret plutôt qu'abstrait.** Remplace « optimiser l'efficacité opérationnelle » par ce qui se passe réellement, si le texte d'origine le dit. S'il ne le dit pas, garde l'idée simple et propose dans le récap le détail concret que l'auteur pourrait ajouter.

**Casser les patrons binaires et ternaires.** Pas de « Ce n'est pas X, c'est Y » ni de « Non seulement... mais aussi » par réflexe. Les énumérations ont le nombre d'éléments qu'il faut. Quand l'original déroule trois points en « d'abord / ensuite / enfin » ou finit sur trois bénéfices alignés, ne recopie pas ce squelette en prose : regroupe, hiérarchise (un point principal, les autres en appui) ou laisse tomber le plus faible.

**Connecteurs : en enlever la plupart.** « Tout d'abord / En outre / Par ailleurs / En conclusion » se suppriment presque toujours. L'enchaînement doit se lire dans les idées.

**Mots simples.** « Utiliser » plutôt que « tirer parti de », « important » ou rien plutôt que « crucial ». Supprime les adjectifs d'enthousiasme et les paires redondantes.

**Oser une position.** Si l'auteur a un avis, laisse-le s'exprimer franchement au lieu de l'équilibrer par une nuance bienveillante systématique. Tu ne crées pas d'opinion absente du texte, mais tu retires les précautions qui la diluent.

**Typographie humaine.** Aucun tiret cadratin (—) ni demi-cadratin en incise : virgule, deux-points, parenthèses ou point. Pas de gras sur un mot-clé suivi de deux-points en tête de chaque puce. Émojis : zéro ou quelques-uns, jamais un par puce. Supprime les résidus Markdown (**, ###, ---) si le texte va être collé ailleurs qu'en Markdown, et les paramètres `utm_source=chatgpt.com`. En français, typographie française (espace avant « : ; ! ? », guillemets « »), sauf si l'auteur ne le fait manifestement pas.

**Pas de sur-correction.** Ne remplace pas un tic par un autre (tout en phrases d'un mot, fautes volontaires, familiarités en rafale). Le texte reste professionnel si le contexte l'est.

## Voix de l'auteur

Si l'utilisateur fournit des exemples de ses propres textes, ou si un skill de style d'écriture est disponible, imite cette voix (longueur de phrase, tutoiement, humour, expressions récurrentes) : c'est le meilleur moyen d'obtenir un texte qui sonne vraiment humain. Sans exemple, vise une voix neutre-directe adaptée au format, et propose en une ligne d'utiliser ses textes passés comme référence la prochaine fois.

## Format de la réponse

Dans cet ordre :

1. **Le texte réécrit**, prêt à copier, dans un bloc de citation (ou un bloc de code si la mise en forme doit être préservée).
2. **Mesures**, un petit tableau avant/après issu de `scan.py --compare`, limité aux lignes qui ont bougé ou qui comptent pour ce format (mots, mots/phrase, CV rythme, tirets, émojis, formules typiques, contraintes du format, score). Six à dix lignes suffisent.
3. **Ce qui a changé** : 3 à 5 puces courtes sur les principaux tics corrigés et les choix liés au format.
4. **Faits à vérifier** (seulement s'il y en a) : chaque fait daté problématique, ce que dit la source (avec le lien), et une formulation de remplacement.
5. **À ajouter si tu l'as** (facultatif, une ou deux lignes) : le détail concret ou personnel qui renforcerait le texte, sans l'inventer.

Si l'utilisateur demande seulement un diagnostic (« est-ce que ça sonne IA ? »), donne les mesures et les marqueurs trouvés, puis propose la réécriture au lieu de la faire.
