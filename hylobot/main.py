from ui.chat.chat_logic import chat
from core.limite_chunks import obter_limite_chunks
from ui.interface import exibir_logo_com_titulo, configurar_pagina, carregar_estilos_chat
from ui.session_utills import inicializar_sessao

configurar_pagina()
carregar_estilos_chat()
exibir_logo_com_titulo('assets/logo_hylo.png')
inicializar_sessao()
# Limite de chunks com slider
obter_limite_chunks()
chat()



