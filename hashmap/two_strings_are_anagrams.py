# Importent | Medium level
"""
Problem: Two Strings Are Anagrams
Topics: String, Hash Map, List
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        data = {}
        for i in s:
            data[i] = data.get(i, 0) + 1
        for char in t:
            if char in data:
                data[char] = data.get(char, 0) - 1
        if all(val == 0 for val in data.values()):
            return True
        return False

if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram("listen", "silent")) #  ➞ True  
    print(solution.isAnagram("triangle", "integral")) #  ➞ True  
    print(solution.isAnagram("apple", "papel")) #  ➞ True  
    print(solution.isAnagram("rat", "car")) #  ➞ False  
    print(solution.isAnagram("hello", "helloo")) #  ➞ False