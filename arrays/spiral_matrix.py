# Importent | Midium level
"""
Problem: Spiral Matrix
Topics: Array, Matrix, Spiral, Traversal, Algorithm
"""
class Solution:
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n) (including output) / O(1) (excluding output)
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right+ 1): # Traverse from left to right
                result.append(matrix[top][i])
            top+=1

            for i in range(top, bottom +1): # Traverse downwards
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):  # Traverse from right to left
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):  # Traverse upwards
                    result.append(matrix[i][left])
                left += 1

        return result

if __name__ == "__main__":
    spiral_matrix = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_matrix.spiralOrder(matrix))