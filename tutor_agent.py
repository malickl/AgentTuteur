from groq import Groq
from dotenv import load_dotenv
import os
from config import CONTEXT, PROMPT, LEVEL_CONFIG
import requests
import fitz
from fpdf import FPDF
import xml.etree.ElementTree as ET

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

    def get_last_assistant_message(self):
        """
        Retourne le dernier message envoyé par l'assistant (souvent le résumé).
        Retourne None s'il n'y en a pas.
        """
        for message in reversed(self.history):
            if message["role"] == "assistant":
                return message["content"]
        return None

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

    def export_last_summary_to_pdf(self, filepath: str = "resume_article.pdf"):
      """
      Crée un PDF simple avec le dernier résumé.
      Retourne le chemin du fichier.
      """
      summary = self.get_last_assistant_message()
      if not summary:
         return None

      pdf = FPDF()
      pdf.add_page()
      pdf.set_auto_page_break(auto=True, margin=15)

      # Titre
      pdf.set_font("Arial", "B", 16)
      pdf.multi_cell(0, 10, "Résumé de l'article arXiv")
      pdf.ln(5)

      # Corps
      pdf.set_font("Arial", "", 12)
      pdf.multi_cell(0, 7, summary)

      pdf.output(filepath)

      return filepath

    def search_similar_articles(self, keywords, max_results=5):
        pass