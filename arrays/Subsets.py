# Medium level
"""
Problem: Subsets
Topics: Array, Backtracking, Bit Manipulation
"""
from typing import List
class Solution:
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result

if __name__ == "__main__":
    arr = [1,2,3]
    Subsets = Solution()
    print(Subsets.subsets(arr))