import streamlit as st
from utils.pdf_exporter import save_summary_to_pdf

def paper_download_pdf(topic_clean: str, summary: str):
    filename = f"{topic_clean}_summary.pdf"
    pdf_path = save_summary_to_pdf(topic_clean.replace('_', ' '), summary, filename=filename)
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Summary PDF", f, file_name=filename, mime="application/pdf")
