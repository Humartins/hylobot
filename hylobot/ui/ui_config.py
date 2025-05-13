# logo.py
import streamlit as st
from PIL import Image

def exibir_logo_com_titulo(caminho_logo: str):
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(caminho_logo, width=70)

    with col2:
        st.markdown("<h1 style='padding-top: 5px;'>Hylo</h1>", unsafe_allow_html=True)

def configurar_pagina():
    st.set_page_config(
        page_title="Hylo",
        page_icon='assets/logo_hylo.ico',
        layout="centered"
    )