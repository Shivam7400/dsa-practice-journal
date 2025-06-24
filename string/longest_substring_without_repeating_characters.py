# Importent | Medium level
"""
Problem: Longest Substring Without Repeating Characters
Topics: String, Sliding Window, Hash Map, Two Pointers
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(k), where k is the size of the charset (max 128 for ASCII)
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))
