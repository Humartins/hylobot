# app.py

import streamlit as st
from routes.Home import mostrar_home
from routes.main import mostrar_chatbot

st.set_page_config(
    page_title="Hylo",
    page_icon='assets/logo_hylo.ico',
    layout="centered"
)

st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Home", "Hylo"])

if pagina == "Home":
    mostrar_home()
elif pagina == "Hylo":
    mostrar_chatbot()
