import re
from app.config import DATA_DIR
import os

def keyword_search(question: str):
    hits = []
    pattern = re.compile(r"\b" + re.escape(question.lower()) + r"\b")

    for file in os.listdir(DATA_DIR):
        if not file.endswith(".pdf"):
            continue

        with open(os.path.join(DATA_DIR, file), "rb"):
            if pattern.search(question.lower()):
                hits.append({"source": file, "text": question})

    return hits
