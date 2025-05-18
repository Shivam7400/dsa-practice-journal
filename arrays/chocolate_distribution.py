"""
Problem: Python program to solve chocolate distribution
Topics: Array, Sliding Window
"""
class Solution:
    # Time Complexity: n*log(n)
    # Space Complexity: O(1)
    def findMinDiff(self, arr, m) -> bool:
        n = len(arr)
        arr.sort()
        minDiff = float('inf')

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < minDiff:
                minDiff = diff
        return minDiff

if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    chocolate_distribution = Solution()
    print(chocolate_distribution.findMinDiff(arr, m))