import streamlit as st
from components.sidebar import render_sidebar
from summarizers.text_summarizer import show_text_summarizer
from summarizers.paper_summarizer import show_paper_summarizer
from summarizers.book_summarizer import show_book_summarizer

# --- Sidebar ---
selected = render_sidebar()

# --- Load Selected Summarizer ---
if selected == "Text Summarizer":
    show_text_summarizer()
elif selected == "Paper Summarizer":
    show_paper_summarizer()
elif selected == "Book Summarizer":
    show_book_summarizer()
