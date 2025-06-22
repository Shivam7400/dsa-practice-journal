# Importent | Medium level
"""
Problem: Subarray Sum Equals K
Topics: Array, Hash Map, Prefix Sum
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def subarraySum(self, nums, k):
        p_sum = 0
        count = 0
        p_map = {0: 1}

        for num in nums:
            p_sum += num
            if p_sum - k in p_map:
                count += p_map[p_sum - k]
            p_map[p_sum] = p_map.get(p_sum, 0) + 1

        return count

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    print(solution.subarraySum(nums, k))
    nums = [1, 2, 3]
    k = 3
    print(solution.subarraySum(nums, k))
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    print(solution.subarraySum(nums, k))
