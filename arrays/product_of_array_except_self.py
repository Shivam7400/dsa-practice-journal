# Importent | Medium level
"""
Problem: Product of Array Except Self
Topics: Array, Prefix Product, Suffix Product, Space Optimization
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) (output array not counted as extra space per problem statement)
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))
    nums = [2, 3, 4, 5]
    print(solution.productExceptSelf(nums))
    nums = [1, 0, 3, 0]
    print(solution.productExceptSelf(nums))
