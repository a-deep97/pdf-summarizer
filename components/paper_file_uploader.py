import streamlit as st

def paper_file_uploader():
    
    pdf = st.file_uploader("📎 Upload a PDF paper", type=["pdf"])

    if pdf:
        with open("uploaded_paper.pdf", "wb") as f:
            f.write(pdf.read())
        st.success("✅ File uploaded!")
        return "uploaded_paper.pdf"
    
    return None
