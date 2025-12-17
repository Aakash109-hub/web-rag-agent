from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

os.environ["USER_AGENT"] = "Mozilla/5.0 (Web RAG Agent)"


def build_vector_store_from_url(url: str) -> FAISS:
    """Load a webpage and build a FAISS vector store."""
    loader = WebBaseLoader(web_paths=(url,))
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    splits = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vector_store = FAISS.from_documents(splits, embeddings)
    return vector_store
