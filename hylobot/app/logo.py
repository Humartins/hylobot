# logo.py
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def carregar_logo(caminho_logo: str, tamanho: int = 50, margin_top: int = 10, margin_left: int = 10):
    """
    Função para carregar o logo, aplicando margens e tamanhos.

    Args:
    caminho_logo (str): Caminho para o logo (pode ser relativo, como 'assets/logo.png').
    tamanho (int): Tamanho da imagem em pixels.
    margin_top (int): Margem superior para a imagem.
    margin_left (int): Margem à esquerda para a imagem.
    """
    # Carregar logo
    logo = Image.open(caminho_logo)
    
    # Converter logo para base64 para exibir no Streamlit
    buffered = BytesIO()
    logo.save(buffered, format="PNG")
    logo_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    # Gerar HTML com logo e estilo
    html_img = f'<img src="data:image/png;base64,{logo_b64}" width="{tamanho}" style="margin-top: {margin_top}px; margin-left: {margin_left}px;" />'
    
    return html_img
