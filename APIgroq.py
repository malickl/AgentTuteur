from groq import Groq
from dotenv import load_dotenv
import os
from LevelConfig import LEVEL_CONFIG
import requests

load_dotenv(dotenv_path=".env")



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
    
    def RecupPdf(self,url):
        URL = url
        response = requests.get(URL)
        open("article.pdf", "wb").write(response.content)


    def PdfToText(self,pdf):
        import fitz

        # Open a PDF file
        pdf_document = pdf
        doc = fitz.open(pdf_document)

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Iterate through each page and extract text
        for page_num in range(doc.page_count):
            page = doc[page_num]
            extracted_text += page.get_text()
            
        # Close the PDF document
        doc.close()

        return extracted_text
    



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
