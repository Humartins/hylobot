import streamlit as st
from chatbot import resposta_bot
from utils import carrega_pdf, carrega_site, carrega_youtube
from logo import exibir_logo_com_titulo

st.set_page_config(page_title="Hylo", layout="centered")

exibir_logo_com_titulo('../assets/LogoHylo.png')

# Inicializa sessão
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if "documento" not in st.session_state:
    st.session_state.documento = []

# Escolha da fonte
fonte = st.selectbox("Escolha a fonte de informações:", ["Nenhuma", "Site", "PDF", "YouTube"])

if fonte == "Site":
    if st.button("Carregar site"):
        st.session_state.documento = carrega_site()

elif fonte == "PDF":
    if st.button("Carregar PDF"):
        st.session_state.documento = carrega_pdf()

elif fonte == "YouTube":
    if st.button("Carregar YouTube"):
        st.session_state.documento = carrega_youtube()

# Limite de chunks com slider
limite_chunks = st.slider("Quantidade máxima de blocos de informação:", 1, 20, 4)

# Campo de texto para pergunta
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    st.session_state.mensagens.append(('human', pergunta))
    resposta = resposta_bot(st.session_state.mensagens, st.session_state.documento, limite_chunks=limite_chunks)
    st.session_state.mensagens.append(('ai', resposta))

# Histórico
st.markdown("### Conversa:")
for remetente, mensagem in st.session_state.mensagens:
    if remetente == 'human':
        st.markdown(f"🧑‍💻 **Você:** {mensagem}")
    else:
        st.markdown(f"🐺**Hylo:** {mensagem}")


