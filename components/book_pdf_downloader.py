import streamlit as st
from utils.pdf_exporter import save_summary_to_pdf

def download_full_summary_pdf(summary_text, topic_keywords):
    filename = f"book_summary_{'_'.join(topic_keywords[:3])}.pdf"
    pdf_path = save_summary_to_pdf("Book Summary", summary_text, filename=filename)

    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Full Book Summary PDF", f, file_name=filename)
