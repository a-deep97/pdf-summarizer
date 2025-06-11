import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.summarizer import generate_summary
from utils.topic_generator import generate_topic

def summarize_chapters_and_display(pdf_path, chapters):
    full_summary = ""
    topic_keywords = []

    with st.spinner("Summarizing chapters..."):
        for title, start, end in chapters:
            chapter_text = extract_text_from_pdf(pdf_path, start_page=start, end_page=end)
            summary = generate_summary(chapter_text)
            topic = generate_topic(chapter_text)

            clean_topic = topic.replace('_', ' ').strip().split("\n")[0]
            topic_keywords.append(clean_topic.replace(" ", "_"))

            st.subheader(f"📘 {title} — {clean_topic}")
            st.write(summary)

            full_summary += f"{title} — {clean_topic}\n{'-'*50}\n{summary}\n\n"

    return full_summary, topic_keywords
