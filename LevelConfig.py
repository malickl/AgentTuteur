LEVEL_CONFIG = {
    "facile": {
        "label": "Niveau facile",
        "objectif": (
            "Produire une explication très accessible pour un public débutant, "
            "sans aucune connaissance scientifique."
        ),
        "contraintes": (
            "- Utiliser un langage simple et des phrases courtes.\n"
            "- Éviter tout jargon scientifique, équations ou détails techniques.\n"
            "- Expliquer uniquement les idées essentielles.\n"
            "- Utiliser des analogies concrètes si utile.\n"
            "- Ne jamais inventer de contenu manquant dans l'article."
        ),
    },

    "moyen": {
        "label": "Niveau moyen",
        "objectif": (
            "Produire une explication destinée à un public ayant des bases "
            "scientifiques (niveau licence – début master)."
        ),
        "contraintes": (
            "- Utiliser un vocabulaire scientifique léger : 'modèle', 'algorithme', 'complexité'.\n"
            "- Expliquer chaque terme technique brièvement.\n"
            "- Donner quelques détails méthodologiques sans entrer dans les preuves.\n"
            "- Ne jamais inventer de contenu manquant dans l'article."
        ),
    },

    "avancé": {
        "label": "Niveau avancé",
        "objectif": (
            "Produire une explication détaillée pour un public expert "
            "(master/doctorat, habitué aux articles scientifiques)."
        ),
        "contraintes": (
            "- Utiliser le vocabulaire technique de l'article.\n"
            "- Mentionner les équations importantes, hypothèses, protocoles expérimentaux.\n"
            "- Discuter les limites lorsqu’elles sont explicitement présentes.\n"
            "- Ne jamais spéculer ni inventer de résultats absents de l’article."
        ),
    },
}