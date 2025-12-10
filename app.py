import streamlit as st
from APIgroq import Agent
from APIgemini import Gemini

GroqAgent = Agent()
GeminiAgent = Gemini()


FichierAudio = st.empty()

st.title("Agent Tuteur")

message = st.text_input("Entrez votre message")

reponse = GroqAgent.ask(message)
st.write(reponse)

GeminiAgent.audio(reponse)


with open("résumé.wav", "rb") as f:
    audio_bytes = f.read()

FichierAudio.audio(audio_bytes, format="audio/wav")



