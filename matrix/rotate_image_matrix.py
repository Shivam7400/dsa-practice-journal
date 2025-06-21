# Importent | Medium level
"""
Problem: Rotate Image (90 Degrees Clockwise)
Topics: Matrix, Array, In-place, 2D Transformation
"""
class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution.rotate(matrix)
    for row in matrix:
        print(row)
