# Importent | Medium level
"""
Problem: Group Anagrams
Topics: String, Hash Map, Sorting
"""
class Solution:
    # Time Complexity: O(n * k log k), where n = len(strs), k = max length of a string
    # Space Complexity: O(n)
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)

        return list(anagram_map.values())

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))

    # Test Case 2
    strs = [""]
    print(solution.groupAnagrams(strs))

    # Test Case 3
    strs = ["a"]
    print(solution.groupAnagrams(strs))
