from transformers import pipeline

_topic_generator = pipeline("text-generation", model="gpt2")


def generate_topic(text: str) -> str:
    """
    Generate a short, relevant topic title from the input text.
    Keeps only 3-7 words, no author metadata or citation junk.
    """
    # Optionally truncate very long inputs
    clean_text = text.strip()[:1000]

    prompt = (
        "Generate a short, high-level topic title (3 to 7 words) that describes the main subject of this text:\n"
        f"{clean_text}\n\nTopic:"
    )

    result = _topic_generator(prompt, max_new_tokens=12, do_sample=False)[0]["generated_text"]
    
    # Extract only the portion after "Topic:"
    if "Topic:" in result:
        topic = result.split("Topic:")[-1].strip()
    else:
        topic = result.strip()
    
    # Keep it filename-safe
    topic_slug = topic.lower().replace(" ", "_").replace(",", "").replace(".", "")
    return topic_slug[:60]  # Optional: limit length
