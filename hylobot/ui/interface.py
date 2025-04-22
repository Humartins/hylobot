import streamlit as st

def configurar_pagina():
    st.set_page_config(
        page_title="Hylo",
        page_icon='assets/logo_hylo.ico',
        layout="centered"
    )

def aplicar_estilos():
    st.markdown("""
        <style>
            .chat-container {
                max-height: 500px;
                overflow-y: auto;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
            }
            .message {
                margin-bottom: 10px;
            }
            .user { color: #1f77b4; }
            .bot { color: #2ca02c; }
        </style>
    """, unsafe_allow_html=True)

def exibir_logo_com_titulo(caminho_logo: str):
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(caminho_logo, width=70)

    with col2:
        st.markdown("<h1 style='padding-top: 5px;'>Hylo</h1>", unsafe_allow_html=True)

def exibir_conversa(mensagens):
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in mensagens:
        autor = msg["autor"]
        conteudo = msg["mensagem"]
        classe = "user" if autor == "usuário" else "bot"
        st.markdown(f'<div class="message {classe}"><strong>{autor}:</strong> {conteudo}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def campo_input():
    return st.text_input("Digite sua pergunta", key="user_input")
