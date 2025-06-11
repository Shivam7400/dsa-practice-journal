# Important | Medium Level
"""
Problem: Find First and Last Position of Element in Sorted Array
Topics: Array, Binary Search
"""
class Solution:
    # Time Complexity: O(log n) - Binary Search
    # Space Complexity: O(1)

    def __init__(self, nums: list[int]):
        self.nums = nums

    def searchRange(self, target: int) -> list[int]:
        return [self._find_bound(target, True), self._find_bound(target, False)]

    def _find_bound(self, target: int, is_first: bool) -> int:
        left, right = 0, len(self.nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] < target:
                left = mid + 1
            elif self.nums[mid] > target:
                right = mid - 1
            else:
                result = mid
                if is_first:
                    right = mid - 1  # for move left to find first
                else:
                    left = mid + 1   # move right to find last element
        return result

if __name__ == "__main__":
    obj = Solution([5, 7, 7, 8, 8, 10])
    target = 8
    print(f"First and last position of {target}: {obj.searchRange(target)}")
