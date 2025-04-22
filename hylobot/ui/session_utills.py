import streamlit as st
from loaders.utils import carrega_pdf, carrega_site, carrega_youtube

def inicializar_sessao():
    # Inicializa variáveis na sessão, se não existirem
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    if "documento" not in st.session_state:
        st.session_state.documento = []

    # Seleção da fonte de informações
    fonte = st.selectbox("Escolha a fonte de informações:", ["Nenhuma", "Site", "PDF", "YouTube"])

    # Lógica para carregar o conteúdo conforme a fonte selecionada
    if fonte == "Site":
        if st.button("Carregar site"):
            st.session_state.documento = carrega_site()

    elif fonte == "PDF":
        if st.button("Carregar PDF"):
            st.session_state.documento = carrega_pdf()

    elif fonte == "YouTube":
        if st.button("Carregar YouTube"):
            st.session_state.documento = carrega_youtube()

    return fonte
