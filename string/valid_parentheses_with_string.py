"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/description/

Topics: String
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False        
        return not stack
    
sol = Solution()
s = "()[]{}"
print(sol.isValid(s))