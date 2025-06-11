import streamlit as st
from components.book_file_uploader import book_file_uploader
from components.book_chapter_input import get_chapter_ranges
from components.book_chapter_summarizer import summarize_chapters_and_display
from components.book_pdf_downloader import download_full_summary_pdf

def show_book_summarizer():
    st.markdown("""
        <style>
            .block-container {
                max-width: 80%;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    """, unsafe_allow_html=True)
    st.header("📚 Book Chapter Summarizer")

    file_path = book_file_uploader()
    if not file_path:
        return

    chapters = get_chapter_ranges()

    if st.button("📑 Summarize Chapters"):
        full_summary, topic_keywords = summarize_chapters_and_display(file_path, chapters)
        download_full_summary_pdf(full_summary, topic_keywords)
