from typing import List
"""
Problem: Next Permutation
Topics: Array, Two Pointers
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

if __name__ == "__main__":
    next_permutation = Solution()
    print(next_permutation.nextPermutation([1,2,3]))
    print(next_permutation.nextPermutation([3,2,1]))
    print(next_permutation.nextPermutation([1,1,5]))