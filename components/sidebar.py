import streamlit as st

def render_sidebar() -> str:
    st.markdown("""
        <style>
            
            /* Sidebar background */
            section[data-testid="stSidebar"] {
                background-color: #1f2a37;
                padding-top: 2rem;
            }


            /* Hide radio inputs */
            div[data-testid="stRadio"] input {
                display: none !important;
            }

            /* Layout radio labels like large buttons */
            div[data-testid="stRadio"] > div {
                display: flex;
                flex-direction: column;
                gap: 1rem;
                align-items: center;
            }

            div[data-testid="stRadio"] label {
                background-color: #e0e7ff;
                color: #1f2937;
                border-radius: 10px;
                padding: 0.8rem 1.5rem;
                width: 80%;
                text-align: center;
                font-weight: bold;
                font-size: 1.1rem;
                transition: 0.2s ease;
                cursor: pointer;
                border: none;
            }

            div[data-testid="stRadio"] label:hover {
                background-color: #c7d2fe;
            }

            /* Selected radio style */
            div[data-testid="stRadio"] input:checked + div > label {
                background-color: #93c5fd;
                color: #1e40af;
            }

            /* External links */
            .custom-link {
                display: block;
                background-color: #e0e7ff;
                color: #1f2937 !important;
                padding: 0.8rem 1.5rem;
                text-align: center;
                width: 80%;
                margin: 0.5rem auto;
                border-radius: 10px;
                font-weight: bold;
                text-decoration: none;
                transition: 0.2s ease;
            }

            .custom-link:hover {
                background-color: #c7d2fe;
                color: #1e40af !important;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

                .sidebar-title h1 {
                    font-family: 'Poppins', sans-serif;
                    font-size: 34px;
                    font-weight: 600;
                    color: #60a5fa;
                    margin-top: -15px;
                    margin-bottom: 15px;
                    text-align: center;
                    transition: all 0.2s ease-in-out;
                }

                .sidebar-title h1:hover {
                    color: #3b82f6;
                    transform: scale(1.03);
                }
            </style>

            <div class="sidebar-title">
                <h1>TL;DR Generator</h1>
            </div>
        """, unsafe_allow_html=True)

        selected = st.radio(
            "Choose a summarizer:",
            ["Text Summarizer", "Paper Summarizer", "Book Summarizer"],
            label_visibility="collapsed"
        )

        st.markdown("<hr style='border-color:#4b5563;'>", unsafe_allow_html=True)
        st.markdown('<a class="custom-link" href="https://github.com/a-deep97/pdf-summarizer" target="_blank">🔗 GitHub Repo</a>', unsafe_allow_html=True)
        st.markdown('<a class="custom-link" href="mailto:a.deep97@outlook.com">💬 Feedback</a>', unsafe_allow_html=True)

    return selected
