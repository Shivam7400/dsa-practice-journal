# Important | Medium Level
"""
Problem: Find Pivot Element in Rotated Sorted Array
Topics: Binary Search, Array, Rotation, Algorithm
"""
class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findPivot(self, arr):
        low, high = 0, len(arr) - 1
        if arr[low] <= arr[high]:
            return arr[low]

        while low <= high:
            mid = (low + high) // 2
            if mid < high and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]
            if mid > low and arr[mid - 1] > arr[mid]:
                return arr[mid]
            if arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == "__main__":
    pivot_finder = Solution()
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(pivot_finder.findPivot(arr))
