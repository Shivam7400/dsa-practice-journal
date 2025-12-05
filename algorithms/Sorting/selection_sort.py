"""
Problem: Sort an Array Using Selection Sort

Topics: Array, Sorting, Selection Sort
"""
from typing import List

class Solution:
    # Approach: Selection Sort
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

if __name__ == "__main__":
    obj = Solution()
    print(obj.sortArray([24, 65, 74, 44, 12, 21, 17, 13]))