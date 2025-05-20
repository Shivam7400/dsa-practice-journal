# Importent | Meadium level
"""
Problem: Longest Palindromic Substring 
Topics: Strings, Two Pointers, Dynamic Programming(DP), 2D Array, Matrix
"""
class Solution:
    # Time Complexity: O(n²)
    # Space Complexity: O(n²)
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        n = len(s)
        max_len = 1
        max_str = s[0]

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(1, n):
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j:i + 1]
        return max_str
    
if __name__ == "__main__":
    longest_Palindrome = Solution()
    print(longest_Palindrome.longestPalindrome("adaadadbabadadadada"))
