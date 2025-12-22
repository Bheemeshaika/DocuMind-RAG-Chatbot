from fastapi import FastAPI, UploadFile, File, Request
from typing import List
from app.pdf_loader import load_uploaded_pdfs
from app.vector_store import create_vector_db
from app.rag import answer_query

app = FastAPI(title="Documind RAG API")


@app.post("/upload")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    try:
        docs = load_uploaded_pdfs(files)
        create_vector_db(docs)
        return {"message": "PDFs uploaded and indexed successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question")

    if not question:
        return {"answer": "No question provided"}

    return {"answer": answer_query(question)}
