import os
import cohere
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a document-based assistant.

RULES:
- Use ONLY the context.
- If not found, say exactly:
  "Answer not found in documents."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = co.chat(
        model="command-r-08-2024",
        message=prompt,
        temperature=0.1
    )

    return response.text.strip()
