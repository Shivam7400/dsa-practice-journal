# Importent | Medium level
"""
Problem: Spiral Matrix II
Topics: Matrix, Simulation, Spiral Traversal
"""
class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1) (excluding output matrix)
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # Left to right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # Top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1

            # Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix

if __name__ == "__main__":
    solution = Solution()

    n = 3
    result = solution.generateMatrix(n)
    for row in result:
        print(row)