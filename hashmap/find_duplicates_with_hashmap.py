"""
Problem: Find Duplicates In An Array
Topics: Hashmap
"""
from typing import List
class FindDuplicates:
    # Time Complexity: O(n) - because of the parllel loop.
    # Space Complexity: O(n)
    def find_duplicates(self, nums: List[int]) -> List[int]:
        freqMap = {}
        result = []
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for key, value in freqMap.items():
            if value > 1:
                result.append(key)
        if not result:
            result.append(-1)

        return result
    
sol = FindDuplicates()
duplicates = [1, 6, 5, 2, 3, 3, 2]
print(sol.find_duplicates(duplicates))