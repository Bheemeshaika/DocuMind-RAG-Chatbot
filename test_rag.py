from app.rag import answer_query

question = "what is java Hash map?"
answer = answer_query(question)

print("QUESTION:", question)
print("ANSWER:\n", answer)