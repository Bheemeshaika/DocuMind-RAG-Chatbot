import streamlit as st
import requests
import json

API = "http://127.0.0.1:8000"

st.title("Documind RAG")
st.caption("A RAG Based Chatbot")

files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Upload PDFs"):
    res = requests.post(
        f"{API}/upload",
        files=[("files", (f.name, f.getvalue(), "application/pdf")) for f in files]
    )
    st.write(res.json())

question = st.text_input("Ask a question")

if st.button("Ask"):
    res = requests.post(f"{API}/ask", json={"question": question})
    try:
        st.success(res.json()["answer"])
    except:
        st.error("Invalid backend response")
        st.text(res.text)
