import streamlit as st
from utils.pdf_exporter import save_summary_to_pdf

def show_pdf_download_button(topic: str, summary: str):
    filename = f"{topic}_summary.pdf"
    
    # Save PDF to disk temporarily
    pdf_path = save_summary_to_pdf(topic.replace('_', ' '), summary, filename=filename)

    # Trigger download with browser's native "Save As" dialog
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Summary PDF",
            data=f,
            file_name=filename,
            mime="application/pdf"
        )
