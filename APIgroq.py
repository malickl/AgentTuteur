from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

class Agent():
    def __init__(self):
        self.groqclient = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def ask(self,message):
        chat_completion = self.groqclient.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                            Tu es un assistant spécialisé dans la vulgarisation d’articles scientifiques arXiv.

                            Ton objectif est de produire un résumé structuré en 4 sections :

                            1. Problème abordé  
                            2. Méthode  
                            3. Résultats  
                            4. Intérêt / limites  

                            Règles strictes :

                            - Tu ne dois utiliser *que* les informations réellement présentes dans l’article.  
                            - Si une section ne peut pas être remplie (information absente), écris :
                            « Informations non disponibles dans l’article. »
                            - Aucune spéculation, aucune hallucination, aucun ajout externe.
                            - Le résumé doit être cohérent, fidèle et factuel.
                            - Le niveau d’explication dépendra des instructions supplémentaires fournies dans la section "NIVEAU D’EXPLICATION".

                            NIVEAU D’EXPLICATION :
                            {info_niveau}
                            """
            },
            {
                "role": "user",
                "content": message,
            }
        ],

            model="llama-3.3-70b-versatile"
        )

        return chat_completion.choices[0].message.content

