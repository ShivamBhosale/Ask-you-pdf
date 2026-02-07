import streamlit as st
from pdf_loader import load_pdf_text

st.set_page_config(page_title="Ask Your PDF")
st.title("Ask Your PDF — Step 1")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        text = load_pdf_text(uploaded_file)

    st.subheader("Extracted Text Preview")
    st.text_area(
        label="PDF Content",
        value=text[:3000],  # show first part only
        height=400
    )

    st.success("PDF text extracted successfully!")
