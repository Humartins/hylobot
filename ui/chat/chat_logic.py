import streamlit as st
from core.db.interaction_log import salvar_interacao, load_conversation
from core.chatbot import resposta_bot


def processar_mensagem():
    limite_chunks = st.slider("Quantidade máxima de blocos de informação:", 1, 20, 20)

    # Inicializa controle de input
    if "input_submetido" not in st.session_state:
        st.session_state.input_submetido = False
    if "mensagem_temp" not in st.session_state:
        st.session_state.mensagem_temp = ""

    if "user_id" not in st.session_state:
        st.session_state.user_id = "default_user" 

    if "histórico_carregado" not in st.session_state:
        user_id = "usuario_padrao"  # ou outro identificador que você quiser
        st.session_state.historico = load_conversation(user_id)
        st.session_state.historico_carregado = True

    user_input = st.chat_input("Digite sua pergunta:")
    if user_input:
        st.session_state.mensagem_temp = user_input
        st.session_state.input_submetido = True  # Ativa a flag

    # Executa apenas se uma nova mensagem foi submetida
    if st.session_state.input_submetido and st.session_state.mensagem_temp:
        pergunta = st.session_state.mensagem_temp
        st.session_state.input_submetido = False  # Reset flag
        st.session_state.mensagem_temp = ""        # Limpa temp

        st.session_state.mensagens.append(("human", pergunta))

        mensagens_com_historico = st.session_state.mensagens + st.session_state.historico

        resposta = resposta_bot(
            mensagens=mensagens_com_historico,
            documentos=st.session_state.documento,
            limite_chunks=limite_chunks
        )

        st.session_state.mensagens.append(("ai", resposta))
        salvar_interacao(st.session_state.user_id, "human", pergunta)
        salvar_interacao(st.session_state.user_id, "ai", resposta)

        return resposta
