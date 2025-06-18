# Importent | Eazy level
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

# Medium Level
"""
Problem: Palindrome String
Topics: String, Two-Pointer
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n) to store cleaned string
    def __init__(self, s: str):
        self.s = s

    def isPalindrome(self) -> str:
        cleaned = [c.lower() for c in self.s if c.isalpha()]
        l, r = 0, len(cleaned) - 1

        while l < r:
            if cleaned[l] != cleaned[r]:
                return "Not Palindrome"
            l += 1
            r -= 1

        return ''.join(cleaned)

if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    obj = Solution(test_string)
    print(f"Result for '{test_string}': {obj.isPalindrome()}")