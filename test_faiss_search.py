from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import BASE_DIR
import os

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

FAISS_DIR = os.path.join(BASE_DIR, "faiss_db")

db = FAISS.load_local(
    FAISS_DIR,
    embedding,
    allow_dangerous_deserialization=True
)

results = db.similarity_search("email", k=5)

for i, r in enumerate(results):
    print(f"\n--- RESULT {i+1} ---")
    print(r.page_content[:300])
    print("SOURCE:", r.metadata)
