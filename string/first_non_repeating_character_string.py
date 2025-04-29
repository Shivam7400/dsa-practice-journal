"""
Problem: First Non-Repeating Character in a String  
Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Topics: Hash Table, String, Queue
"""

class Solution:
    # Time Complexity: O(n) where n is the length of the string
    # Space Complexity: O(1) since there are only 26 lowercase letters (constant space)
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1

sol = Solution()
s = "leetcode"
print(sol.firstUniqChar(s))
