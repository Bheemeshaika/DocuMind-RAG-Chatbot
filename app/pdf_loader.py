import os
from typing import List
from fastapi import UploadFile
from pypdf import PdfReader
from app.config import DATA_DIR


def load_uploaded_pdfs(files: List[UploadFile]):
    documents = []

    for file in files:
        if not file.filename.lower().endswith(".pdf"):
            continue

        path = os.path.join(DATA_DIR, file.filename)

        with open(path, "wb") as f:
            f.write(file.file.read())

        reader = PdfReader(path)

        for page_no, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if not text or len(text.strip()) < 20:
                continue

            cleaned = " ".join(text.split())

            documents.append({
                "text": cleaned,
                "source": file.filename,
                "page": page_no
            })

    if not documents:
        raise ValueError("No readable text found in PDFs")

    return documents
