from sentence_transformers import SentenceTransformer, util
import torch

def load_embed_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def get_top_passages(text, query, embed_model, chunk_size=500, top_k=3):
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = embed_model.encode(text_chunks, convert_to_tensor=True)
    query_embedding = embed_model.encode(query, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    top_indices = torch.topk(similarities, k=top_k).indices
    return "\n".join([text_chunks[i] for i in top_indices])
