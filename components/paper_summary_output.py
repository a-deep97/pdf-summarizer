import streamlit as st
from utils.summarizer import generate_summary

def paper_generate_and_display_summary(text: str) -> str:
    if "paper_summary" not in st.session_state:
        with st.spinner("Generating summary..."):
            summary = generate_summary(text)
            st.session_state.paper_summary = summary
    else:
        summary = st.session_state.paper_summary

    st.subheader("Summary")
    st.write(summary)
    return summary
