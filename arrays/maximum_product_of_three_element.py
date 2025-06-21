# Importent | Medium level
"""
Problem: Maximum Product of Three Numbers
Topics: Array, Sorting, Greedy, Math
"""
class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        return max(nums[n-1] * nums[n-2] * nums[n-3],
                   nums[0] * nums[1] * nums[n-1])

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(solution.maximumProduct(nums))

    nums = [-10, -10, 1, 3, 2]
    print(solution.maximumProduct(nums))
