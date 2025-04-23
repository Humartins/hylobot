import streamlit as st
from core.chatbot import resposta_bot

def obter_limite_chunks():
    limite_chunks = st.slider("Quantidade máxima de blocos de informação:", 1, 20, 20)
    pergunta = st.text_input("Digite sua pergunta:")
    
    if st.button("Enviar"):
        st.session_state.mensagens.append(('human', pergunta))
        resposta = resposta_bot(st.session_state.mensagens, st.session_state.documento, limite_chunks=limite_chunks)
        st.session_state.mensagens.append(('ai', resposta))