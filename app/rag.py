import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import FAISS_DIR
from app.cohere_llm import generate_answer

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def answer_query(question: str) -> str:
    if not os.path.exists(FAISS_DIR):
        return "No documents indexed yet."

    db = FAISS.load_local(
        FAISS_DIR,
        embedding,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(question, k=8)

    if not docs:
        return "Answer not found in documents."

    context = "\n\n".join(
        f"[{d.metadata['source']} - Page {d.metadata['page']}]\n{d.page_content}"
        for d in docs
    )

    return generate_answer(context, question)
