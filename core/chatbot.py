from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
import os

from core.db.sqlite_chat_history import SQLiteChatMessageHistory  # NOVO

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ['USER_AGENT'] = "HyloBot/1.0"

chat = ChatGroq(model='llama3-70b-8192')

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente chamado Hylo. Use as informações abaixo para responder com clareza e precisão:\n\n{informacoes}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | chat

def resposta_bot(mensagens, documentos, limite_chunks=20, session_id="default_session"):
    if not mensagens:
        raise ValueError("A lista de mensagens está vazia.")
    
    if isinstance(documentos, list) and documentos:
        documentos_limitados = documentos[:limite_chunks]
        informacoes = " ".join(doc.page_content for doc in documentos_limitados)
    else:
        informacoes = documentos or "Nenhuma informação externa fornecida."

    # Usa SQLite como histórico persistente
    memory = ConversationBufferWindowMemory(
        k=5,
        return_messages=True,
        chat_memory=SQLiteChatMessageHistory(session_id=session_id)
    )

    chain_com_memoria = RunnableWithMessageHistory(
        chain,
        get_session_history=lambda _: memory.chat_memory,
        input_messages_key="input",
        history_messages_key="chat_history"
    )

    resposta = chain_com_memoria.invoke({
        "input": mensagens[-1][1],
        "informacoes": informacoes
    }, {"configurable": {"session_id": session_id}})

    return resposta.content
