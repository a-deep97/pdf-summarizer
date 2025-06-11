# utils/pdf_exporter.py

from fpdf import FPDF
import os

def save_summary_to_pdf(title: str, content: str, filename: str = "summary.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=title, align='C')
    pdf.ln()
    pdf.multi_cell(0, 10, txt=content)
    path = os.path.join("outputs", filename)
    os.makedirs("outputs", exist_ok=True)
    pdf.output(path)
    return path
