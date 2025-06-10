# Midium level
"""
Problem: House Robber
Topics: Dynamic Programming(DP), Array, Robbery, Optimization
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0  # dp[i - 1]
        prev2 = 0  # dp[i - 2]

        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp

        return prev1

if __name__ == "__main__":
    robber = Solution()
    houses = [2, 7, 9, 3, 1]
    print(robber.rob(houses))
