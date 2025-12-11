from groq import Groq
from dotenv import load_dotenv
import os
from config import CONTEXT, PROMPT, LEVEL_CONFIG
import requests
import fitz


class TutorAgent:
    def __init__(self):
        load_dotenv()
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.history = []


    def update_history(self, role, content):
        self.history.append(
            {
                "role": role,
                "content": content
            }
        )


    def build_context(self, level):
        level_info = (
            f"NIVEAU D’EXPLICATION : {LEVEL_CONFIG[level]['label']}\n\n"
            f"Objectif :\n{LEVEL_CONFIG[level]['objectif']}\n\n"
            f"Contraintes :\n{LEVEL_CONFIG[level]['contraintes']}\n"
        )
        context = CONTEXT.replace("{info_niveau}", level_info)
        
        self.update_history(role="system", content=context)


    @staticmethod
    def get_pdf_content(arxiv_url):
        response = requests.get(arxiv_url)
        pdf_path = "cache/article.pdf"
        open(pdf_path, "wb").write(response.content)     

        doc = fitz.open(pdf_path)

        pdf_content = []

        for page_num in range(doc.page_count):
            page = doc[page_num]
            pdf_content.append(page.get_text())
            
        doc.close()

        return "".join(pdf_content)
    


    def build_prompt(self, arxiv_url):
        prompt = PROMPT.replace("{article_content}", TutorAgent.get_pdf_content(arxiv_url))
        self.update_history(role="user", content=prompt)




    def explain(self, level, arxiv_url):
        self.build_context(level)
        self.build_prompt(arxiv_url)

        explanations = self.groq_client.chat.completions.create(
            messages=self.history,
            model="llama-3.3-70b-versatile"
        ).choices[0].message.content

        self.update_history(role="assistant", content=explanations)
        
        return explanations
    

    def ask_tutor(self, question):

        self.update_history(role="user", content=question)
        
        response = self.groq_client.chat.completions.create(
            messages=self.history,
            model="llama-3.3-70b-versatile"
        ).choices[0].message.content

        self.update_history(role="assistant", content=response)