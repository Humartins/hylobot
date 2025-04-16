from chatbot import resposta_bot
from utils import carrega_pdf, carrega_site, carrega_youtube

print('Bem-vindo ao HyloBot!')

texto_selecao = '''
Digite 1 para conversar com um site
Digite 2 para conversar com um PDF
Digite 3 para conversar com um vídeo do YouTube
'''

while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    elif selecao == '2':
        documento = carrega_pdf()
        break
    elif selecao == '3':
        documento = carrega_youtube()
        break
    else:
        print('Opção inválida.')

mensagens = []
while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'HyloBot: {resposta}')

print('Muito obrigado por usar o HyloBot!')
print(mensagens)
