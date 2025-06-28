# Medium Level
"""
Problem: Calculate Cosine Similarity Between Two Vectors
Topics: Vectors, Math, NLP, GenAI Embeddings
"""
from typing import List
import math

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        if len(vec1) != len(vec2):
            raise ValueError("Vectors must be of the same length.")

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude_vec1 = math.sqrt(sum(a * a for a in vec1))
        magnitude_vec2 = math.sqrt(sum(b * b for b in vec2))

        if magnitude_vec1 == 0 or magnitude_vec2 == 0:
            raise ValueError("One of the vectors has zero magnitude.")

        return dot_product / (magnitude_vec1 * magnitude_vec2)


if __name__ == "__main__":
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]

    similarity = Solution().cosine_similarity(vec1, vec2)
    print("Cosine Similarity:", similarity)
