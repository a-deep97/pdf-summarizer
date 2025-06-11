import streamlit as st

def show_text_input():
    st.markdown("""
        <style>
        .custom-textarea > div > textarea {
            width: 100% !important;
            min-height: 200px !important;
            resize: vertical !important;
            font-size: 16px !important;
            padding: 1rem !important;
            border-radius: 0.5rem !important;
            border: 1px solid #ccc !important;
        }
        </style>
    """, unsafe_allow_html=True)

    return st.text_area(
        "Enter the text you want summarized:",
        height=250,
        placeholder="Paste or type your text here...",
        key="custom_text_input",
        label_visibility="visible",
        help="This field is horizontally expanded and resizable.",
    )
