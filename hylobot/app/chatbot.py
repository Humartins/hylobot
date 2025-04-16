from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
os.environ['USER_AGENT'] = "HyloBot/1.0"

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens, documentos, limite_chunks=4):
    # Limita os chunks (caso esteja recebendo uma lista de documentos)
    if isinstance(documentos, list):
        documentos_limitados = documentos[:limite_chunks]
        informacoes = " ".join(doc.page_content for doc in documentos_limitados)
    else:
        # Caso já venha como string (backup)
        informacoes = documentos

    # Define a mensagem de sistema com as informações do contexto
    system_message = (
        "Você é um assistente amigável chamado Hylo.\n"
        "Você utiliza as seguintes informações para formular suas respostas: {informacoes}"
    )

    mensagens_modelo = ['system', system_message]
    mensagens_modelo += mensagens

    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat

    return chain.invoke({'informacoes': informacoes}).content
