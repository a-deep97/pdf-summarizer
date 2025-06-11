import streamlit as st
from utils.summarizer import generate_summary
from utils.topic_generator import generate_topic

from components.text_input import show_text_input
from components.summarize_text_button import show_summarize_button
from components.text_summary_output import show_summary
from components.text_summary_downloader import show_pdf_download_button

def show_text_summarizer():
    # Add this line once here (or in app.py if global)
    st.markdown("""
        <style>
            .block-container {
                max-width: 80%;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header("📝 Summarize Text")

    input_text = show_text_input()

    if show_summarize_button():
        with st.spinner("Generating summary..."):
            summary = generate_summary(input_text)
            raw_topic = generate_topic(input_text)

            topic = (
                raw_topic.strip()
                .split("\n")[0][:60]
                .strip()
                .replace(" ", "_")
                .replace("/", "_")
            )

            show_summary(topic, summary)
            show_pdf_download_button(topic, summary)

