import streamlit as st
from chatbot import resposta_bot
from utils import carrega_pdf, carrega_site, carrega_youtube

st.set_page_config(page_title="Hylo", layout="centered")
st.title("🤖 Hylo")
st.write("Converse com PDFs, Sites ou Vídeos do YouTube!")

# Escolha da fonte de dados
opcao = st.radio("Escolha a fonte de dados:", ("PDF", "Site", "YouTube"))

if "documento" not in st.session_state:
    st.session_state.documento = None

if st.button("Carregar dados"):
    if opcao == "PDF":
        st.session_state.documento = carrega_pdf()
    elif opcao == "Site":
        st.session_state.documento = carrega_site()
    elif opcao == "YouTube":
        st.session_state.documento = carrega_youtube()
    st.success("Dados carregados com sucesso!")

# Caixa de entrada para o usuário perguntar
pergunta = st.text_input("Digite sua pergunta:")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if st.button("Enviar"):
    if st.session_state.documento is None:
        st.warning("Carregue os dados primeiro!")
    else:
        st.session_state.mensagens.append(("user", pergunta))
        resposta = resposta_bot(st.session_state.mensagens, st.session_state.documento)
        st.session_state.mensagens.append(("assistant", resposta))
        st.markdown(f"**HyloBot:** {resposta}")

# Histórico de conversa
if st.session_state.mensagens:
    st.subheader("🗂 Histórico de Conversa")
    for role, msg in st.session_state.mensagens:
        prefix = "👤 Você" if role == "user" else "🤖 HyloBot"
        st.markdown(f"**{prefix}:** {msg}")
