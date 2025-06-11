# 📄 Too Long; Didn’t Read – PDF TL;DR Generator

A smart and fast Streamlit app that compresses large PDF files or raw text into bite-sized summaries using state-of-the-art NLP models. Whether you're working with research papers, contracts, or entire books, this tool helps you extract core information instantly.

---

## 🚀 Features

- 📎 **PDF Upload** – Works with research papers, books, and reports
- 📝 **Text Summarizer** – Summarize custom input text instantly
- 📚 **Book Chapter Summarizer** – Define chapters by page ranges and generate chapter-wise summaries
- 🧠 **Topic Generator** – Automatically creates a meaningful topic for each summary
- 📘 **Key Term Extractor** – Extracts core keywords from PDFs
- 💬 **Semantic Q&A** – Ask questions and get contextual answers from the document using embeddings
- 📥 **Download as PDF** – Export summaries with generated titles as professional PDFs
- ⚡ **Lightweight & Fast** – Powered by Hugging Face Transformers (`facebook/bart-large-cnn`) and SentenceTransformers
- 🧩 **Modular Codebase** – Organized into plugins and utilities for easy extensibility

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **NLP Models**:
  - Summarization: `facebook/bart-large-cnn`
  - Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- **PDF Parsing**: PyMuPDF
- **Packaging**: PDF export via `reportlab`

---

## 🧪 Use Cases

- 🎓 Students – Summarize long research papers or textbooks
- 💼 Professionals – Digest contracts, whitepapers, or business docs
- 📖 Readers – Generate notes from nonfiction books chapter-by-chapter

---

## 📦 Run 

Install all dependencies via:

```bash
git clone https://github.com/a-deep97/pdf-tldr-generator
cd pdf-tldr-generator
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure
```
pdf-tldr-generator/
│
├── app.py # Main entry point with tab-based navigation
│
├── summarizers/ # Streamlit views for different summarization modes
│ ├── text_summarizer.py # Summarize plain input text
│ ├── paper_summarizer.py # Summarize research papers + key terms + Q&A
│ └── book_summarizer.py # Chapter-wise summarization for books
│
├── utils/ # Core processing logic
│ ├── pdf_utils.py # Extracts text from selected PDF pages
│ ├── summarizer.py # Uses HuggingFace Transformers to summarize text
│ ├── topic_generator.py # Generates a clean title/topic for the summary
│ ├── key_terms.py # Extracts key terms from input text
│ ├── qa.py # Handles embedding, semantic search, and QA
│ └── pdf_exporter.py # Saves summaries as downloadable PDF files
│
├── assets/ # Optional: icons/images for UI (if any)
│
├── requirements.txt # Python dependencies
└── README.md # You're reading it
```