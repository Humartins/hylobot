import streamlit as st

def exibir_conversa():
    html_conversa = '<div id="chat-container" style="max-height: 400px; overflow-y: auto; padding-right: 10px;">'

    for remetente, mensagem in st.session_state.mensagens:
        if remetente == 'human':
            html_conversa += f'<div class="user"><p><strong>Você:</strong> {mensagem}</p></div>'
        else:
            html_conversa += f'<div class="bot"><p><strong>Hylo:</strong> {mensagem}</p></div>'

    html_conversa += "</div>"

    html_conversa += """
    <script>
        const chatContainer = document.getElementById("chat-container");
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>
    """

    st.markdown(html_conversa, unsafe_allow_html=True)
