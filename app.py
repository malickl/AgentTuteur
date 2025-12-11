import streamlit as st
from APIgroq import Agent
from APIgemini import Gemini
from Prompt import content

GroqAgent = Agent()
GeminiAgent = Gemini()

#niveau par defaut
niveau="facile"

# choix des niveau avec un bouton
if st.button("facile"):
    niveau = "facile"

if st.button( "moyen"):
    niveau =  "moyen"

if st.button("avancé"):
    niveau = "avancé"

# Contient le prompt final en fonction du niveeau choisi
FinalPrompt = GroqAgent.AjoutPrompt(niveau,content)


# espace vide qui va contenir les audios
FichierAudio = st.empty()


st.title("Agent Tuteur")

#message = ""
message = st.text_input("Entrez votre message")

reponse = GroqAgent.ask(message,FinalPrompt)
st.write(reponse)

# ici je prend le lien et je stocke dans lien
lien = st.text_input("Entrez votre lien")
 
# a est juste un boloen pour faire mon while
a = True
while a:
    if lien == "":
        break
    else:
        # ici je met le lien dans recup pdf pour qu'il telecharge le pdf du lien
        GroqAgent.RecupPdf(lien)

        # ici je prend le contenu du pdf que j'ai telecharger
        ContenuPdf = GroqAgent.PdfToText("article.pdf")

        # ici je recupere le resumer du contenu du lien que le llm donne 
        ReponseResume = GroqAgent.ask(ContenuPdf,FinalPrompt)

        st.write(ReponseResume)
        a = False









# GeminiAgent.audio(reponse)


# with open("résumé.wav", "rb") as f:
#     audio_bytes = f.read()

# FichierAudio.audio(audio_bytes, format="audio/wav")



