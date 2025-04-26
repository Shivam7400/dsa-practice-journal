"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Topics: Array
"""
from typing import List
class Solution:
    # Approach: Brute Force Approach
    # Time Complexity: O(n²) - because of the nested loop.
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))