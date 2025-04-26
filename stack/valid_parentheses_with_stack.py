"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/description/

Topics: Stack
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if st:
                last = st[-1]
                if self.is_pair(last, s[i]):
                    st.pop()
                    continue
            st.append(s[i])        
        return not st
    
    def is_pair(self, last, cur):
        if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
            return True
        return False
    
sol = Solution()
s = "()[]{}"
print(sol.isValid(s))