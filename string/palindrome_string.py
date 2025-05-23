"""
Problem: Next Permutation
Topics: String, Slicing
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        if s == s[::-1]:
            return True
        else:
            return False
        
is_palindrome = Solution()
print(is_palindrome.isPalindrome("madam"))
print(is_palindrome.isPalindrome("shivam"))