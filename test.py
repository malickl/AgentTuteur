from APIgroq import Agent
from APIgemini import Gemini
from LevelConfig import LEVEL_CONFIG


GroqAgent = Agent()



# print(reponse)



# GeminiAgent = Gemini()

# GeminiAgent.audio(reponse)


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

def AjoutPrompt(niveau):
    TexteNiveau = InfoNiveau(LEVEL_CONFIG[niveau])
    content = content.replace("{info_niveau}", TexteNiveau)
    return content

'''

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


GroqAgent = Agent()

promptF = GroqAgent.AjoutPrompt("avancé",content)




# GeminiAgent = Gemini()
# GeminiAgent.audio("bonjour")



# import requests

# URL = "https://arxiv.org/pdf/2512.08997"
# response = requests.get(URL)
# open("artcile.pdf", "wb").write(response.content)


# Import PyMuPDF
import fitz

# Open a PDF file
pdf_document = "article.pdf"
doc = fitz.open(pdf_document)

# Initialize an empty string to store extracted text
extracted_text = ""

# Iterate through each page and extract text
for page_num in range(doc.page_count):
    page = doc[page_num]
    extracted_text += page.get_text()
    
# Close the PDF document
doc.close()

# Perform text analysis (e.g., count words)
# word_count = len(extracted_text.split())
# print(f"The Extracted text is as follows:\n{extracted_text}")
# print(f"Total words in the document: {word_count}")


contenu_lien = extracted_text

#print(contenu_lien)

reponse = GroqAgent.ask(contenu_lien,promptF)
print(reponse)

###############################
