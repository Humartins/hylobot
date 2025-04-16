from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens, documento):
    system_message = (
        "Você é um assistente amigável chamado Hylo.\n"
        "Você utiliza as seguintes informações para formular suas respostas: {informacoes}"
    )
    mensagens_modelo = ['system', system_message]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content
