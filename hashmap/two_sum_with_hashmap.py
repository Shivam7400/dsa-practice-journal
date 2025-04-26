"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Topics: Hashmap
"""
from typing import List
class Solution:
    # Time Complexity: O(n) - because of the nested loop.
    # Space Complexity: O(n)
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in d:
                return [d[comp], i]
            d[num] = i

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.two_sum(nums, target))