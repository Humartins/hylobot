from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader

def carrega_site():
  url_site = input('Digite a url do site:')
  loader = WebBaseLoader(url_site)
  lista_documentos = loader.load()
  documento = ''
  for doc in lista_documentos:
    documento += doc.page_content
  return documento

def carrega_pdf():
    loader = PyPDFLoader('CAMINHO/DO/SEU/ARQUIVO.pdf')
    lista_documentos = loader.load()
    return ''.join(doc.page_content for doc in lista_documentos)

def carrega_youtube():
    url = input('Digite a url do vídeo')
    loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento


