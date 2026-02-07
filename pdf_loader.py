import pdfplumber

def load_pdf_text(file) -> str:
    """
    Extract all text from an uploaded PDF file.
    """
    text = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)

    return "\n".join(text)
