import streamlit as st
from transformers import pipeline

@st.cache_resource(show_spinner="Loading summarization model...")
def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, chunk_size=1024):
    summarizer = get_summarizer()
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]["summary_text"] + "\n"
    return summary
