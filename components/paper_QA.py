import streamlit as st
from transformers import pipeline
from utils.qa import load_embed_model, get_top_passages

@st.cache_resource
def load_qa_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def paper_question_answer_box(text: str):
    with st.expander("💬 Ask a question"):
        query = st.text_input("Your question:")
        if query:
            embed_model = load_embed_model()
            context = get_top_passages(text, query, embed_model)
            qa_prompt = f"Answer the question using context:\n\n{context}\n\nQ: {query}\nA:"
            summarizer = load_qa_summarizer()
            answer = summarizer(qa_prompt, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            st.subheader("Answer")
            st.write(answer)
