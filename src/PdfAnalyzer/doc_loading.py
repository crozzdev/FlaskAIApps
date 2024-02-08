import os
import sys
import shutil

from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import RetrievalQA, ConversationalRetrievalChain

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.extensions import llm_agent
from config import Config

persist_directory = "src/PdfAnalyzer/docs/chroma/"

if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)

if Config.AI_ENGINE == "openai":
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings()


def load_db(file, chain_type, k):
    """
    Load documents from a PDF file, split them into chunks, create a vector database,
    define a retriever, and create a chatbot chain.

    Args:
        file (str): The path to the PDF file.
        chain_type (str): The type of chatbot chain.
        k (int): The number of similar documents to retrieve.

    Returns:
        qa (ConversationalRetrievalChain): The chatbot chain.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the chain_type is not valid.

    """
    # load documents
    loader = PyPDFLoader(file)
    documents = loader.load()
    # split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    # create vector database from data
    vectordb = Chroma.from_documents(
        documents=docs,
        persist_directory=persist_directory,
        embedding=embeddings,
    )
    
    vectordb.persist()
    # db = DocArrayInMemorySearch.from_documents(docs, embeddings)

    # define retriever
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": k})
    # create a chatbot chain. Memory is managed externally.
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm_agent,
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=True,
        return_generated_question=True,
    )
    
    question = "what did they say about matlab?"
    docs = vectordb.similarity_search(question,k)
    return qa, docs

#test
if __name__ == "__main__":
    file = "src/PdfAnalyzer/docs/MachineLearning-Lecture01.pdf"
    qa, docs = load_db(file, "stuff", 5)
    question = "what did they say about matlab?"
    print(len(docs))
    print(docs[0])
    #print(qa.ask(question))
