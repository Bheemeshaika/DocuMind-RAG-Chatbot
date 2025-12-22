from app.pdf_loader import load_pdfs
from app.vector_store import create_vector_db

docs = load_pdfs("data/pdfs")
create_vector_db(docs)

print("FAISS index created successfully")
