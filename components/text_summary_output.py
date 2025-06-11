import streamlit as st

def show_summary(topic: str, summary: str):
    st.subheader(f"🧠 Topic: {topic.replace('_', ' ')}")
    st.subheader("Summary")
    st.write(summary)
