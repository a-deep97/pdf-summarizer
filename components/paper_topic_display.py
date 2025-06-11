import streamlit as st

def paper_display_topic(topic: str):
    topic_clean = topic.strip().split("\n")[0][:60].strip().replace(" ", "_").replace("/", "_")
    st.subheader(f"🧠 Topic: {topic_clean.replace('_', ' ')}")
    return topic_clean
