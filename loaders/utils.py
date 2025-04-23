from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
import os

def split_documentos(documento, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    return splitter.split_documents(documento)

def carrega_site(url_site):
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    return split_documentos(lista_documentos)

def carrega_youtube(url_youtube):
    loader = YoutubeLoader.from_youtube_url(url_youtube,language=['pt', 'en'])
    lista_documentos = loader.load()
    return split_documentos(lista_documentos)

def carrega_pdf(arquivo_pdf):
    conteudo = arquivo_pdf.read()

    if not conteudo:
        raise ValueError("O arquivo PDF está vazio.")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(conteudo)
        temp_path = temp_file.name

    loader = PyPDFLoader(temp_path)
    lista_documentos = loader.load()
    os.remove(temp_path)
    return split_documentos(lista_documentos)
