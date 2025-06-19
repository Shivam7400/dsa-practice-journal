# Importent | Medium Level
"""
Problem: Fibonacci Series
Topics: Recursion, Iteration, Dynamic Programming
"""
from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n) for storing the sequence
    def __init__(self, n: int):
        self.n = n

    def fibonacci_series(self) -> List[int]:
        if self.n <= 0:
            return []
        if self.n == 1:
            return [0]
        if self.n == 2:
            return [0, 1]

        fib = [0, 1]
        for i in range(2, self.n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

if __name__ == "__main__":
    num_terms = 10
    obj = Solution(num_terms)
    print(f"First {num_terms} Fibonacci numbers: {obj.fibonacci_series()}")
