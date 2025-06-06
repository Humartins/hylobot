import streamlit as st

def exibir_logo_com_titulo(caminho_logo: str):
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(caminho_logo, width=70)

    with col2:
        st.markdown("<h1 style='padding-top: 5px;'>Hylo</h1>", unsafe_allow_html=True)

def carregar_estilos_chat():
    with open("ui/chat/chat_style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
