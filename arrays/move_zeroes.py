"""
Problem: Nove Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Topics: Array, Two Pointers
"""
from typing import List

class Solution:
    # Approach: Two Pointers
    # Time Complexity: O(n) - Each element is processed once.
    # Space Complexity: O(1) - No extra space used.
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_position = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_position] = nums[i]
                non_zero_position += 1

        for i in range(non_zero_position, len(nums)):
            nums[i] = 0
        return nums

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    print(sol.moveZeroes(nums))