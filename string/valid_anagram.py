"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/description/

Topics: String, Hash Table
"""
class CheckIsAnagram:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True

check_anagram = CheckIsAnagram()
print(check_anagram.isAnagram("leetcode", "tcodelee"))
print(check_anagram.isAnagram("shivam", "shiva"))