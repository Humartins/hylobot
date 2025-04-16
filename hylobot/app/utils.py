from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documentos(documento, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    return splitter.split_documents(documento)

def carrega_site():
    url_site = input('Digite a url do site:')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    return split_documentos(lista_documentos)

def carrega_pdf():
    loader = PyPDFLoader('CAMINHO/DO/SEU/ARQUIVO.pdf')
    lista_documentos = loader.load()
    return split_documentos(lista_documentos)

def carrega_youtube():
    url = input('Digite a url do vídeo: ')
    loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
    lista_documentos = loader.load()
    return split_documentos(lista_documentos)

