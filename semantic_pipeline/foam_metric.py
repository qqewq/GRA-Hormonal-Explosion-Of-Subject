import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_foam_matrix(embeddings: np.ndarray) -> np.ndarray:
    """
    Foam = 1 - cosine_similarity.
    High foam = low similarity = high contradiction.
    """
    sim = cosine_similarity(embeddings)
    foam = 1 - sim
    return foam


def global_foam(foam_matrix: np.ndarray) -> float:
    """
    Global foam measure: average of upper triangular (excluding diagonal).
    """
    n = foam_matrix.shape[0]
    if n < 2:
        return 0.0
    triu_indices = np.triu_indices_from(foam_matrix, k=1)
    return np.mean(foam_matrix[triu_indices])


def local_foam_for_element(foam_matrix: np.ndarray, idx: int) -> float:
    """Average foam of element idx with all others."""
    n = foam_matrix.shape[0]
    if n <= 1:
        return 0.0
    others = np.delete(foam_matrix[idx], idx)
    return np.mean(others)
