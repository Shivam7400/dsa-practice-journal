"""
Problem: Sort an Array
Link: https://leetcode.com/problems/sort-an-array/description/

Topics: Array, Divide and Conquer, Sorting, Merge Sort
"""
from typing import List

class Solution:
    # Approach: Top-Down Recursive Merge Sort
    # Time Complexity: O(n log n) - Best, Average, and Worst Case.
    # Space Complexity: O(n) - extra space for temporary arrays.
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i, j, result = 0, 0, []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

def main():
    unsorted_array = eval(input("Enter a list of numbers (e.g., [11, 2, 7, 8, 4, 6, 1, 3, 10]) to sort the list: "))
    solution = Solution()
    sorted_list = solution.sortArray(unsorted_array)
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()