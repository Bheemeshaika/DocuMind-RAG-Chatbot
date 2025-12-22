import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

response = co.chat(
    model="command-a-03-2025",
    message="Say hello"
)

print(response.text)
