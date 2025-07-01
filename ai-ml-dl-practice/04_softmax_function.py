# Medium Level
"""
Problem: Implement Softmax Activation Function
Topics: Arrays, Math, Deep Learning, Activation Functions
"""
from typing import List
import math

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def softmax(self, logits: List[float]) -> List[float]:
        """
        Calculates the softmax activation for a list of logits.

        Args:
            logits (List[float]): Raw scores (logits) from the output layer.

        Returns:
            List[float]: Softmax probabilities.
        """
        max_logit = max(logits)  # For numerical stability
        exp_values = [math.exp(x - max_logit) for x in logits]
        sum_exp = sum(exp_values)
        probabilities = [x / sum_exp for x in exp_values]
        return probabilities


if __name__ == "__main__":
    logits = [2.0, 1.0, 0.1]
    softmax_output = Solution().softmax(logits)
    print("Softmax Output:", softmax_output)
