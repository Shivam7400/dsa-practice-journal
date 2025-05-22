# Midium Level
'''
Find Peak Element
Type: Array, Binary Search
'''
from typing import List

class Solution:
    # Time Complexity: O(log n) where n is the number of elements in the list.
    # Space Complexity: O(1) as we are using constant space.
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l

if __name__ == "__main__":
    find_peak_element = Solution()
    nums = find_peak_element.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(nums)