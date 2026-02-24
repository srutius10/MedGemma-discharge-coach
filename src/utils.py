import os
import tempfile

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

try:
    from docx import Document as DocxDocument
except ImportError:
    os.system("pip install -q python-docx")
    from docx import Document as DocxDocument

from .model import run_model


def read_uploaded_file(file):
    if file is None:
        return ""
    file_path = str(file)

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_path.endswith(".docx"):
        doc = DocxDocument(file_path)
        return "\n".join(
            [p.text for p in doc.paragraphs if p.text.strip()]
        )
    else:
        return "Unsupported file type. Please upload .txt or .docx"


def create_pdf(text: str) -> str:
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    c = canvas.Canvas(pdf_path, pagesize=letter)
    y = 750

    for line in text.split("\n"):
        c.drawString(30, y, line[:90])
        y -= 15
        if y < 40:
            c.showPage()
            y = 750

    c.save()
    return pdf_path


def generate_clinical_note(conversation: str):
    raw_text = run_model(conversation)

    safety = []
    lower_conv = conversation.lower()
    if "chest tightness" in lower_conv or "chest pain" in lower_conv:
        safety.append("⚠️ Possible cardiac risk - chest pain on exertion")

    safety_text = "\n".join(safety) if safety else "✅ No immediate safety flags."
    pdf_path = create_pdf(raw_text)

    return raw_text, safety_text, pdf_path


def ui_generate(conversation_text: str, uploaded_file):
    if uploaded_file is not None:
        conversation_text = read_uploaded_file(uploaded_file)

    if not conversation_text or not conversation_text.strip():
        return (
            "Please enter a doctor-patient conversation.",
            "No safety flags.",
            None,
        )

    return generate_clinical_note(conversation_text)
