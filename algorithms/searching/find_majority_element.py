# Importent | Eazy Level
"""
Problem: Find Majority Element
Topics: Array, Searching, Hash Map
"""
class Solution:
    # Time Complexity: n*log(n)
    # Space Complexity: O(1)
    def majorityelement(self, nums):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
            
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    majority_element = Solution()
    print(majority_element.majorityelement(arr))
