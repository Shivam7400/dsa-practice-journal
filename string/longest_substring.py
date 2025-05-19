"""
Problem: Longest Substring
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Topics: String, Sliding Window, Hash Table, Two Pointers
"""
class Solution:
    # Approach: Sliding Window
    # Time Complexity: O(n) - Each character is visited at most twice.
    # Space Complexity: O(min(n, m)) - n is length of string, m is the character set (e.g., 26 for lowercase English).
    def length_of_longest_substring(self, s:str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()
s = "abcabcbb"
print(sol.length_of_longest_substring(s))