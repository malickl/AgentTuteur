import streamlit as st
from APIgroq import Agent
from APIgemini import Gemini
from APIgroq import content

GroqAgent = Agent()
GeminiAgent = Gemini()

niveau="facile"

if st.button("facile"):
    niveau = "facile"

if st.button( "moyen"):
    niveau =  "moyen"

if st.button("avancé"):
    niveau = "avancé"

FinalPrompt = GroqAgent.AjoutPrompt(niveau,content)

FichierAudio = st.empty()

st.title("Agent Tuteur")

message = ""
message = st.text_input("Entrez votre message")

reponse = GroqAgent.ask(message,FinalPrompt)
st.write(reponse)







GeminiAgent.audio(reponse)


with open("résumé.wav", "rb") as f:
    audio_bytes = f.read()

FichierAudio.audio(audio_bytes, format="audio/wav")



