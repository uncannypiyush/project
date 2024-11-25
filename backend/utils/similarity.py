import numpy as np
from typing import List, Tuple

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    """
    dot_product = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Handle edge case where vector magnitude is zero
    return dot_product / (magnitude1 * magnitude2)

def calculate_similarities(query_embedding: np.ndarray, embeddings: List[np.ndarray]) -> List[float]:
    """
    Compute cosine similarities between a query embedding and a list of embeddings.
    """
    return [cosine_similarity(query_embedding, embedding) for embedding in embeddings]

def get_top_k_similarities(
    query_embedding: np.ndarray, 
    embeddings: List[np.ndarray], 
    contents: List[str], 
    top_k: int = 5
) -> List[Tuple[str, float]]:
    """
    Retrieve the top-k most similar embeddings based on cosine similarity.
    
    Args:
        query_embedding: Embedding of the query.
        embeddings: List of document embeddings.
        contents: List of document chunks corresponding to the embeddings.
        top_k: Number of top results to return.
        
    Returns:
        A list of tuples containing the content and its similarity score.
    """
    similarities = calculate_similarities(query_embedding, embeddings)
    # Pair contents with their similarity scores
    results = list(zip(contents, similarities))
    # Sort by similarity score in descending order
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    # Return top-k results
    return sorted_results[:top_k]
