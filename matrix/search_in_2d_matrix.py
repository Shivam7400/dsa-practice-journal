# Importent | Medium level
"""
Problem: Search a 2D Matrix
Topics: Matrix, Binary Search, 2D Array
"""
class Solution:
    # Time Complexity: O(log (m * n)) = O(log n) where n is total elements
    # Space Complexity: O(1)
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(solution.searchMatrix(matrix, target))
    target = 13
    print(solution.searchMatrix(matrix, target))
