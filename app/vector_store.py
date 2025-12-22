from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import FAISS_DIR
import shutil
import os

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def create_vector_db(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=300
    )

    texts, metadatas = [], []

    for doc in documents:
        chunks = splitter.split_text(doc["text"])
        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({
                "source": doc["source"],
                "page": doc["page"]
            })

    if os.path.exists(FAISS_DIR):
        shutil.rmtree(FAISS_DIR)

    FAISS.from_texts(
        texts=texts,
        embedding=embedding,
        metadatas=metadatas
    ).save_local(FAISS_DIR)
