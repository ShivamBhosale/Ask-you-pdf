import streamlit as st
from pdf_loader import load_pdf_text
from chunker import chunk_text

st.set_page_config(page_title="Ask Your PDF")
st.title("Ask Your PDF — Step 2")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        text = load_pdf_text(uploaded_file)

    chunks = chunk_text(text)

    st.success(f"PDF split into {len(chunks)} chunks")

    st.subheader("Sample Chunks")

    # Show first 3 chunks for inspection
    for i, chunk in enumerate(chunks[:3]):
        st.markdown(f"### Chunk {i + 1}")
        st.text(chunk)
