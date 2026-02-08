import streamlit as st
from pdf_loader import load_pdf_text
from chunker import chunk_text
from retriever import build_retriever, retrieve_chunks
from llm_answerer import answer_question

st.set_page_config(page_title="Ask Your PDF")
st.title("Ask Your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading PDF..."):
        text = load_pdf_text(uploaded_file)

    chunks = chunk_text(text)
    st.success(f"Document split into {len(chunks)} chunks")

    with st.spinner("Preparing search index..."):
        vectorizer, matrix = build_retriever(chunks)

    question = st.text_input("Ask a question about the PDF")

    if st.button("Ask"):
        with st.spinner("Searching document..."):
            relevant_chunks = retrieve_chunks(
                question, chunks, vectorizer, matrix
            )

        with st.spinner("Generating answer..."):
            answer = answer_question(question, relevant_chunks)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")
        for i, chunk in enumerate(relevant_chunks):
            st.markdown(f"**Chunk {i+1}**")
            st.text(chunk)
