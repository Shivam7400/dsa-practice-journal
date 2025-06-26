# Medium Level
"""
Problem: Matrix Multiplication Without NumPy
Topics: Matrix, Nested Loops, Math, Deep Learning Basics
"""

from typing import List

class Solution:
    # Time Complexity: O(m * n * p)
    # Space Complexity: O(m * p), where
    #   A is m x n and B is n x p

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A[0]) != len(B):
            raise ValueError("Number of columns of A must equal number of rows of B.")

        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        return result


if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    B = [
        [7, 8, 9],
        [10, 11, 12]
    ]
    
    matrix_multiplier = Solution()
    result = matrix_multiplier.multiply(A, B)

    print("Result of Matrix Multiplication:")
    for row in result:
        print(row)
