import streamlit as st
from core.chatbot import resposta_bot
from ui.interface import exibir_logo_com_titulo, configurar_pagina
from ui.session_utills import inicializar_sessao

configurar_pagina()
exibir_logo_com_titulo('assets/logo_hylo.png')
inicializar_sessao()
# Limite de chunks com slider
limite_chunks = st.slider("Quantidade máxima de blocos de informação:", 1, 20, 20)
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    st.session_state.mensagens.append(('human', pergunta))
    resposta = resposta_bot(st.session_state.mensagens, st.session_state.documento, limite_chunks=limite_chunks)
    st.session_state.mensagens.append(('ai', resposta))

st.markdown("### Conversa:")
for remetente, mensagem in st.session_state.mensagens:
    if remetente == 'human':
        st.markdown(f"🧑‍💻 **Você:** {mensagem}")
    else:
        st.markdown(f"🐺**Hylo:** {mensagem}")


