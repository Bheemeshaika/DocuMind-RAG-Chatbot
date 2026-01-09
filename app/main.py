from fastapi import FastAPI, UploadFile, File
from typing import List
from pydantic import BaseModel

from app.pdf_loader import load_uploaded_pdfs
from app.vector_store import create_vector_db
from app.rag import answer_query


app = FastAPI(
    title="Documind RAG API",
    description="Upload PDFs and ask questions using RAG",
    version="1.0.0"
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload", summary="Upload and index PDF files")
async def upload_pdfs(files: List[UploadFile] = File(...)):
   
    try:
        docs = load_uploaded_pdfs(files)
        create_vector_db(docs)
        return {"message": "PDFs uploaded and indexed successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/ask", summary="Ask a question from uploaded PDFs")
async def ask_question(payload: QuestionRequest):

    answer = answer_query(payload.question)
    return {"answer": answer}
