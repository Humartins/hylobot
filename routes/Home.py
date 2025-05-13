import streamlit as st

def mostrar_home():
    st.title("Bem-vindo ao Hylo!")
    st.markdown("""
        ##### O Hylo é um assistente virtual inteligente, criado para facilitar o acesso a informações extraídas de diversas fontes, como PDFs, sites e vídeos do YouTube. Usando tecnologias modernas de IA e Processamento de Linguagem Natural, o Hylo interpreta suas perguntas e responde com base no conteúdo fornecido.

        ##### 🔍 *O que o Hylo faz?*
                
        - 📄 PDFs: Carregue documentos e faça perguntas sobre o conteúdo.
                
        - 🌐 Sites: Insira uma URL e explore os textos de forma interativa.
                
        - 📺 YouTube: Forneça o link de um vídeo e extraia insights diretamente do que foi falado.
                
        ##### 🧠 Como funciona?
                
        O Hylo utiliza:
                
        - LangChain para orquestrar a cadeia de interações com a IA.
                
        - Groq + LLaMA 3 como motor de raciocínio.
                
        - Streamlit para uma interface simples, leve e acessível via navegador.
                
        - Banco de dados SQLite para registrar todas as interações.
                
        ##### 🚀 Por que usar o Hylo?
                
        Porque ele transforma qualquer conteúdo estático em algo dinâmico e interativo. Ideal para:
        Estudos e resumos.
                
        Pesquisa rápida de documentos.
                
        Apoio no entendimento de vídeos longos.
        
        ##### 🛠️ Projeto em Desenvolvimento
        O Hylo ainda está em constante evolução! Este projeto também faz parte do meu portfólio como estudante de Engenharia da Computação. Novas funcionalidades estão sendo desenvolvidas para torná-lo ainda mais poderoso e intuitivo.

        Acesse a aba *Hylo* na esquerda para começar!
                
        Linkedin: https://www.linkedin.com/in/humberto-martins-79822a2a6/     
        E-mail: hummartinsg@gmail.com                
""")


