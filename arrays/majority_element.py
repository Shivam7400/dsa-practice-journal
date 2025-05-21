# Important | Eazy Level
"""
Problem: Majority Element
Topics: Array, Hash Map, Boyer-Moore Voting Algorithm, Linear Scan
"""
class Solution:
    # Time Complexity: O(n) where n is the number of elements in the list.
    # Space Complexity: O(1) as we are using constant space.
    def majorityElement(self, nums: list[int]) -> int:
        ans = None
        count = 0

        for i in nums:
            if count == 0:
                ans = i
            count += (1 if i == ans else -1)
        return ans

if __name__ == "__main__":
    majority_Element = Solution()
    nums = [3, 2, 3, 6, 3, 2, 1, 3]
    print(majority_Element.majorityElement(nums))
