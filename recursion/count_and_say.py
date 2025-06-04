# Important | Medium Level
"""
Problem: Count and Say
Topics: String, Recursion
"""
class Solution:
    # Time Complexity: O(2^n) in worst case (due to string operations)
    # Space Complexity: O(n) for recursion stack
    def countAndSay(self, n):
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1

        result += str(count) + prev[-1]
        return result

if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.countAndSay(n))
