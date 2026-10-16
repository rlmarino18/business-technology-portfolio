import io

import fitz
from docx import Document


def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)

    if file_name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    if file_name.endswith(".txt"):
        return extract_txt_text(uploaded_file)

    raise ValueError(f"Unsupported file type: {uploaded_file.name}")


def extract_pdf_text(uploaded_file):
    file_bytes = uploaded_file.getvalue()
    pdf = fitz.open(stream=file_bytes, filetype="pdf")

    pages = []

    for page_number, page in enumerate(pdf, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append(
                {
                    "page": page_number,
                    "text": text,
                }
            )

    pdf.close()
    return pages


def extract_docx_text(uploaded_file):
    file_bytes = uploaded_file.getvalue()
    document = Document(io.BytesIO(file_bytes))

    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    text = "\n".join(paragraphs)

    return [{"page": None, "text": text}] if text else []


def extract_txt_text(uploaded_file):
    text = uploaded_file.getvalue().decode("utf-8").strip()

    return [{"page": None, "text": text}] if text else []
