import streamlit as st
from utils.key_terms import extract_key_terms

def paper_display_key_terms(text: str):
    with st.spinner("Extracting key terms..."):
        terms = extract_key_terms(text)
        st.subheader("Key Terms")
        st.write(", ".join(terms) if terms else "No key terms found.")
