# Importent | Medium level
"""
Problem: Set Matrix Zeroes
Topics: Matrix, Array, In-place, Space Optimization
"""
class Solution:
    # Time Complexity: O(m * n)
    # Space Complexity: O(1) — using matrix itself for markers
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    solution.setZeroes(matrix)
    for row in matrix:
        print(row)
