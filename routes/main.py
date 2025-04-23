from ui.chat.chat_logic import processar_mensagem
from core.db.database import initialize_database
from ui.interface import exibir_logo_com_titulo, carregar_estilos_chat
from ui.chat.chat_handler import exibir_conversa
from ui.session_utills import inicializar_sessao

def mostrar_chatbot():
    # Inicializa o banco de dados e configurações da página
    initialize_database()
    carregar_estilos_chat()

    # Exibe o Logo e inicializa a sessão
    exibir_logo_com_titulo('assets/logo_hylo.png')
    inicializar_sessao()

    # Chama a função que processa as mensagens
    processar_mensagem()

    # Exibe a conversa carregada
    exibir_conversa()






