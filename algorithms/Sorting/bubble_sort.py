"""
Problem: Sort an Array Using Bubble Sort

Topics: Array, Two Pointer, Sorting, Bubble Sort
"""
from typing import List

class Solution:
    # Approach: Bubble Sort
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swaped = False
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swaped = True
                    
            if not swaped:
                break
        return nums

if __name__ == "__main__":
    obj = Solution()
    print(obj.sortArray([32, 94, 13, 83, 4, 23, 53, 65]))