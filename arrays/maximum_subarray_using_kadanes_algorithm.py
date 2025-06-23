# Importent | Medium level
"""
Problem: Maximum Subarray (Kadane's Algorithm)
Topics: Array, Dynamic Programming, Greedy
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))
    nums = [1]
    print(solution.maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(solution.maxSubArray(nums))
