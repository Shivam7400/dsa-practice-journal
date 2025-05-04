"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/description/

Topics: Array, Binary Search
"""
from typing import List

class Binary_Search:
    def binary_search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                return m
        return -1

search = Binary_Search()
print(search.binary_search([1, 2, 3, 4, 5], 3))