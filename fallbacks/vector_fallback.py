import json
import os
from sentence_transformers import SentenceTransformer, util

with open("data/examples.json", "r") as f:
    examples = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

example_texts = [e["sentence"] for e in examples]
example_embeddings = model.encode(example_texts, convert_to_tensor=True)

def find_closest(text: str, threshold: float = 0.6):
    query_embedding = model.encode(text, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, example_embeddings)[0]

    best_score = float(scores.max())
    if best_score < threshold:
        return None

    best_idx = int(scores.argmax())
    return examples[best_idx]
