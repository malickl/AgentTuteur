import streamlit as st
from tutor_agent import TutorAgent

if "tutor_agent" not in st.session_state :
	st.session_state.tutor_agent = TutorAgent()

def show_header():
    st.title("Agent Tuteur")
    level = st.selectbox("Niveau d'explications", ["facile", "moyen", "avancé"])
    link = st.text_input("Entrez votre lien")
    return level, link


def show_discussion_history(history_placeholder):
    container = history_placeholder.container()
    with container:
        for message in st.session_state.tutor_agent.history[2:]:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.write(message["content"])


def show_explanations():
    level, arxiv_url = show_header()
    history_placeholder = st.empty()
    if level and arxiv_url and not st.session_state.tutor_agent.history:
        st.session_state.tutor_agent.explain(level, arxiv_url)
        show_discussion_history(history_placeholder)
        user_input = st.chat_input("Pose une question !")
    
    elif st.session_state.tutor_agent.history:
        show_discussion_history(history_placeholder)
        user_input = st.chat_input("Pose une question !")
        if user_input:
            st.session_state.tutor_agent.ask_tutor(user_input)
            user_input = None
            show_discussion_history(history_placeholder)


if __name__ == "__main__":
    show_explanations()