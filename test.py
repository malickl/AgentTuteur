from APIgroq import Agent
from APIgemini import Gemini
from LevelConfig import LEVEL_CONFIG

'''
GroqAgent = Agent()

reponse = GroqAgent.ask("Bonjour, ca va ?")

print(reponse)



GeminiAgent = Gemini()

GeminiAgent.audio(reponse)
'''

def InfoNiveau(LEVEL_CONFIG):
    return (
        f"NIVEAU D’EXPLICATION : {LEVEL_CONFIG['label']}\n\n"
        f"Objectif :\n{LEVEL_CONFIG['objectif']}\n\n"
        f"Contraintes :\n{LEVEL_CONFIG['contraintes']}\n"
    )

content = """
Tu es un assistant spécialisé dans la vulgarisation d’articles scientifiques arXiv.

Ton rôle est de produire un résumé structuré en 4 sections :

1. Problème abordé  
2. Méthode  
3. Résultats  
4. Intérêt / limites  

Règles fondamentales :

- Tu ne dois utiliser *que* les informations réellement présentes dans l’article.
- Si une section ne peut pas être remplie, écris exactement :
« Informations non disponibles dans l’article. »
- Aucune spéculation, aucune hallucination, aucun ajout externe.
- Le résumé doit être cohérent, factuel et fidèle au contenu.
- Ton style d’écriture doit strictement respecter les instructions du niveau choisit.

{info_niveau}

Répond toujours en français.
            """

TexteNiveau = InfoNiveau(LEVEL_CONFIG["facile"])

#print(TexteNiveau)

content = content.replace("{info_niveau}", TexteNiveau)

print(content)


