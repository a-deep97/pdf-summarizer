def extract_key_terms(text):
    common_terms = [
        "objective", "method", "conclusion", "algorithm", "accuracy", "precision",
        "dataset", "evaluation", "optimization", "performance"
    ]
    return [term for term in common_terms if term.lower() in text.lower()]
