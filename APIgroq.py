from groq import Groq
from dotenv import load_dotenv
import os
from LevelConfig import LEVEL_CONFIG

load_dotenv(dotenv_path=".env")

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




class Agent():
    def __init__(self):
        self.groqclient = Groq(api_key=os.getenv("GROQ_API_KEY"))


    def InfoNiveau(self,LEVEL_CONFIG):
        return (
            f"NIVEAU D’EXPLICATION : {LEVEL_CONFIG['label']}\n\n"
            f"Objectif :\n{LEVEL_CONFIG['objectif']}\n\n"
            f"Contraintes :\n{LEVEL_CONFIG['contraintes']}\n"
        )
    
    def AjoutPrompt(self,niveau,prompt):
        TexteNiveau = self.InfoNiveau(LEVEL_CONFIG[niveau])
        prompt = prompt.replace("{info_niveau}", TexteNiveau)
        return prompt


    def ask(self,message,FinalPrompt):
        chat_completion = self.groqclient.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": FinalPrompt
            },
            {
                "role": "user",
                "content": message,
            }
        ],

            model="llama-3.3-70b-versatile"
        )

        return chat_completion.choices[0].message.content


    def resumé(self,artcile):
        pass
