# Medium Level
"""
Problem: Longest Consecutive Sequence
Topics: Hashing, Set, Arrays
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums

    def longest_consecutive(self) -> int:
        if not self.nums:
            return 0

        num_set = set(self.nums)
        longest_string = 0

        for num in num_set:
            # Only start counting if it's the start of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest_string = max(longest_string, count)

        return longest_string

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    obj = Solution(nums)
    print(f"Longest consecutive sequence length: {obj.longest_consecutive()}")
