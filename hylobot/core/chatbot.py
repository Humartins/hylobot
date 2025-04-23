from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
import uuid
import os

# Configuração da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
os.environ['USER_AGENT'] = "HyloBot/1.0"

# Inicializa o modelo
chat = ChatGroq(model='llama3-70b-8192')

# Template do prompt com placeholder para histórico e informações
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente chamado Hylo. Use as informações abaixo para responder com clareza e precisão:\n\n{informacoes}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Pipeline
chain = prompt | chat

# Função principal com memória
def resposta_bot(mensagens, documentos, limite_chunks=20):
    if not mensagens:
        raise ValueError("A lista de mensagens está vazia.")
    
    if isinstance(documentos, list) and documentos:
        documentos_limitados = documentos[:limite_chunks]
        informacoes = " ".join(doc.page_content for doc in documentos_limitados)
    else:
        informacoes = documentos or "Nenhuma informação externa fornecida."

    # Define memória via Streamlit
    memory = ConversationBufferWindowMemory(
        k=5,
        return_messages=True,
        chat_memory=StreamlitChatMessageHistory()
    )

    # Gerando um session_id único para cada interação
    session_id = str(uuid.uuid4())  # Gera um UUID único por sessão

    # Encapsula o chain com memória
    chain_com_memoria = RunnableWithMessageHistory(
        chain,
        get_session_history=lambda _: memory.chat_memory,
        input_messages_key="input",
        history_messages_key="chat_history"
    )

    # Executa, passando o session_id no config
    resposta = chain_com_memoria.invoke({
        "input": mensagens[-1][1],  # última mensagem do usuário
        "informacoes": informacoes
    }, {"configurable": {"session_id": session_id}})

    return resposta.content
