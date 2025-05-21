# Important | Medium Level
"""
Problem: Group Anagrams 
Topics: Strings, Hashing, Sorting, HashMap, Two Pointers
"""
from collections import defaultdict

class Solution:
    # Time Complexity: O(n * k * log k) where n is the number of words and k is the average length of the word.
    # Space Complexity: O(n * k) where n is the number of words and k is the average length of the word.
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
        return list(anagram_groups.values())

if __name__ == "__main__":
    group_Anagrams = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_Anagrams.groupAnagrams(input_strs))
