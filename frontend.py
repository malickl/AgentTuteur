import streamlit as st
from tutor_agent import TutorAgent
from audio_agent import GeminiAudioAgent

# Configuration générale de la page
st.set_page_config(
    page_title="Agent Tuteur arXiv",
    page_icon="📚",
    layout="wide"
)

# Initialisation de l'agent en session
if "tutor_agent" not in st.session_state:
    st.session_state.tutor_agent = TutorAgent()

if "gemini_agent" not in st.session_state:
    st.session_state.gemini_agent = GeminiAudioAgent()

if "audio_resume" not in st.session_state:
    st.session_state.audio_resume = None

def show_discussion_history(history_placeholder):
    """Affiche l'historique de discussion (sans les messages système)."""
    container = history_placeholder.container()
    with container:
        # On saute les 2 premiers messages : system + prompt initial
        for message in st.session_state.tutor_agent.history[2:]:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])


def main():
    # --- BARRE LATERALE GAUCHE ---
    with st.sidebar:
        st.markdown("### ⚙️ Paramètres")
        level = st.selectbox("Niveau d'explications", ["facile", "moyen", "avancé"])
        arxiv_url = st.text_input("Lien de l'article arXiv")

        # Bouton pour lancer l'explication (on garde la logique existante)
        lancer = st.button("🚀 Générer / regénérer le résumé")

        st.markdown("---")
        st.markdown("### 📄 Export du résumé")

        # Bouton d'export PDF : seulement si on a déjà une réponse de l'assistant
        if any(m["role"] == "assistant" for m in st.session_state.tutor_agent.history):
            if st.button("📥 Exporter le résumé en PDF"):
                pdf_path = st.session_state.tutor_agent.export_last_summary_to_pdf()
                if pdf_path:
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Télécharger le PDF",
                            data=f,
                            file_name="resume_article.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
        else:
            st.caption("Le bouton d'export sera disponible après le premier résumé.")


        st.markdown("### 🎙️ Obtenir le résumé en audio")

        if st.button("🎧 Générer l'audio du résumé"):
            resume = st.session_state.tutor_agent.get_last_assistant_message()
            if resume:
                # Ton agent Gemini doit retourner des bytes ou un path
                st.session_state.audio_resume = st.session_state.gemini_agent.generate_audio(resume)
            else:
                st.warning("Aucun résumé trouvé. Génère d'abord un résumé avec l'agent tuteur.")

        if st.session_state.audio_resume is not None:
            st.sidebar.audio(st.session_state.audio_resume, format="audio/wav")

    # --- PARTIE DROITE : CONTENU PRINCIPAL ---

    st.markdown("## 🤖 Agent Tuteur arXiv")
    st.markdown(
        "<p style='color: gray;'>Collez un lien arXiv à gauche, choisissez le niveau, puis lancez l'analyse.</p>",
        unsafe_allow_html=True
    )

    history_placeholder = st.empty()

    # 1) Si on clique sur "Générer" et qu'on a tout ce qu'il faut
    if lancer and level and arxiv_url:
        if not st.session_state.tutor_agent.history:
            st.session_state.tutor_agent.explain(level, arxiv_url)
        else:
            # Option : regénérer en repartant de zéro
            st.session_state.tutor_agent.history = []
            st.session_state.tutor_agent.explain(level, arxiv_url)

        show_discussion_history(history_placeholder)

    # 2) Si un historique existe déjà, on affiche la discussion + chat input
    elif st.session_state.tutor_agent.history:
        show_discussion_history(history_placeholder)

    if st.session_state.tutor_agent.history:
        user_input = st.chat_input("Pose une question à l'agent sur l'article...")
        if user_input:
            st.session_state.tutor_agent.ask_tutor(user_input)
            show_discussion_history(history_placeholder)
    else:
        st.info("Aucun résumé pour l'instant. Configure à gauche puis lance l'analyse.")

if __name__ == "__main__":
    main()