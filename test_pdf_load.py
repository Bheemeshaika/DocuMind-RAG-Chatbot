from app.pdf_loader import load_pdfs

docs = load_pdfs("data/pdfs")

print("DOC COUNT:", len(docs))
print("FIRST FILE:", docs[0]["source"])
print("FIRST 500 CHARS:\n", docs[0]["text"][:500])
