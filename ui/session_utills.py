import streamlit as st
import uuid
from loaders.utils import carrega_pdf, carrega_site, carrega_youtube

def inicializar_sessao():
    # Inicializa variáveis na sessão, se não existirem
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    if "documento" not in st.session_state:
        st.session_state.documento = []

    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    #Adicionar botão para limpar a sessão

    if st.button("Limpar conversa"):
        st.session_state.mensagens.clear()
        st.session_state.documento.clear()
        st.session_state.session_id = str(uuid.uuid4())
        st.success("Sessão limpa com sucesso!")

    # Seleção da fonte de informações
    fonte = st.selectbox("Escolha a fonte de informações:", ["Nenhuma", "Site", "PDF", "YouTube"])
    
    if fonte == "Site":
        url_site = st.text_input("Digite a URL do site:", key="input_site_url")
        if st.button("Carregar site"):
            if url_site:
                st.session_state.documento = carrega_site(url_site)
            else:
                st.warning("Por favor, insira uma URL válida.")

    elif fonte == "PDF":
        arquivo_pdf = st.file_uploader("Envie seu arquivo PDF", type=["pdf"], key="input_pdf_file")

        if st.button("Carregar PDF"):
            if arquivo_pdf is not None:
                try:
                    st.session_state.documento = carrega_pdf(arquivo_pdf)
                    st.success("PDF carregado com sucesso!")
                except ValueError as e:
                    st.error(str(e))
                except Exception as e:
                    st.error(f"Erro sao processar o PDF: {e}")
            else:
                st.warning("Por favor, envie um arquivo PDF válido.")

    elif fonte == "YouTube":
        url_youtube = st.text_input("Digite a URL do vídeo:", key="input_youtube_url")
        if st.button("Carregar YouTube"):
            if url_youtube:
                st.session_state.documento = carrega_youtube(url_youtube)
            else:
                st.warning("Por favor, insira uma URL válida.")
    return fonte
