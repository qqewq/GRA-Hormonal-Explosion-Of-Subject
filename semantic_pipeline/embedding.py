from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Any

_model = None


def get_model(model_name='all-MiniLM-L6-v2'):
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model


def embed_items(items: List[Dict[str, Any]]) -> np.ndarray:
    model = get_model()
    texts = [item['text'] for item in items]
    embeddings = model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)
