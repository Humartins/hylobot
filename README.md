# HyloBot 🤖

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)

Assistente inteligente para interagir com conteúdo de **PDFs**, **sites** e **vídeos do YouTube**. O HyloBot usa inteligência artificial para te ajudar a entender documentos e responder perguntas com base nas informações fornecidas. Um projeto prático e moderno para explorar o poder dos LLMs!

---

## 📚 Sobre o Projeto

O **HyloBot** é um chatbot com múltiplas entradas de dados, desenvolvido em Python, utilizando **LangChain**, **Llama 3 via Groq** e loaders inteligentes. Ele permite:

- Analisar o conteúdo de um site (via BeautifulSoup)
- Carregar e conversar com PDFs
- Extrair transcrições de vídeos do YouTube e responder sobre eles

O foco é criar uma ferramenta simples, mas poderosa, para automação de leitura e compreensão.

---

## ⚙️ Tecnologias Utilizadas

- 🐍 Python 3.11
- 🧠 [LangChain](https://www.langchain.com/)
- 🔗 [Groq API](https://console.groq.com/)
- 📄 [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- 🌐 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- 📺 [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- 📦 virtualenv

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   
git clone https://github.com/Humartins/hylobot.git
cd hylobot

3. Ative o ambiente virtual
   
   venv\Scripts\activate

5. Instale as dependencias:
   
   pip install -r requirements.txt

4. Crie uma variável de ambiente com sua chave da API Groq:
   
   $env:GROQ_API_KEY = "sua-chave-aqui"

6. Rode o bot:
   
   cd app
   python main.py
   
---

## 📌Observações

O projeto ainda está em desenvolvimento, novas funcionalidades serão adicionadas em breve.

Você pode encerrar a conversa com o comando x.
