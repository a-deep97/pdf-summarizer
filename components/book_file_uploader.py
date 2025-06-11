import streamlit as st

def book_file_uploader() -> str:
    pdf = st.file_uploader("📎 Upload book PDF", type=["pdf"])
    if not pdf:
        return None

    path = "uploaded_book.pdf"
    with open(path, "wb") as f:
        f.write(pdf.read())
    st.success("✅ File uploaded!")
    return path
