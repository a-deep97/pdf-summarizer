import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.topic_generator import generate_topic

from components.paper_file_uploader import paper_file_uploader
from components.paper_topic_display import paper_display_topic
from components.paper_summary_output import paper_generate_and_display_summary
from components.paper_QA import paper_question_answer_box
from components.paper_pdf_downloader import paper_download_pdf

def show_paper_summarizer():
    st.markdown("""
        <style>
            .block-container {
                max-width: 80%;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header("📄 Summarize a Paper")

    # --- Upload file ---
    file_path = paper_file_uploader()

    if file_path:
        # Extract text
        text = extract_text_from_pdf(file_path)
        st.info(f"Extracted {len(text)} characters.")
        st.session_state["summary_in_progress"] = True

        # --- Topic ---
        topic = generate_topic(text)
        topic_clean = paper_display_topic(topic)

        # --- Summary ---
        summary = paper_generate_and_display_summary(text)
        st.session_state["summary_ready"] = True
        st.session_state["summary_in_progress"] = False

        # --- QA Box ---
        paper_question_answer_box(text)

        # --- Download PDF ---
        paper_download_pdf(topic_clean, summary)
