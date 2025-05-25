"""
Problem: Longest Recurring Subsequence
Topics: Strings, Dynamic Programming(DP), sMatrix/Table-based DP, Backtracking
"""
class Solution:
    # Time Complexity: O(n²)
    # Space Complexity: O(n²)
    def longest_recurring_subsequence(self, s: str) -> str:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        i, j = n, n
        lrs = []

        while i > 0 and j > 0:
            if s[i - 1] == s[j - 1] and i != j:
                lrs.append(s[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(reversed(lrs))

if __name__ == "__main__":
    lrs = Solution()
    s = "aabebcdd"
    print(lrs.longest_recurring_subsequence(s))