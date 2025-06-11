import streamlit as st

def get_chapter_ranges():
    st.markdown("### ➕ Define Chapters")
    chapters = []
    num_chapters = st.number_input("Number of chapters", min_value=1, max_value=50, step=1)

    for i in range(num_chapters):
        with st.expander(f"📖 Chapter {i+1}"):
            title = st.text_input(f"Chapter {i+1} Title", key=f"title_{i}")
            start_page = st.number_input(f"Start Page", key=f"start_{i}", min_value=1)
            end_page = st.number_input(f"End Page", key=f"end_{i}", min_value=start_page)
            chapters.append((title, int(start_page), int(end_page)))
    return chapters
