from typing import List
"""
Problem: Contains Duplicate from Array
Topics: Array, Hash Table, Sorting
"""
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # Using Hash Table to solve the problem
    def containsDuplicatedict(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                return True
            count[num] = 1
        return False

    # Using set() function
    def containsDuplicateset(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    cd = Solution()
    # duplicate = [1,2,3,1]
    print(cd.containsDuplicatedict([1,2,3,1]))
    print(cd.containsDuplicateset([1,2,3,1]))
    # unique = [1,2,3,4]
    print(cd.containsDuplicatedict([1,2,3,4]))
    print(cd.containsDuplicateset([1,2,3,4]))