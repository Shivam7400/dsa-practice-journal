# Important | Medium Level
"""
Problem: Find First Repeated Word in String
Topics: String, Loop, Brute Force, Manual Parsing
"""

class Solution:
    # Time Complexity: O(n^2) in worst case (due to manual search)
    # Space Complexity: O(n) for storing unique words
    def firstRepeatedWord(self, s):
        words = []
        word = ""
        
        for char in s:
            if char != ' ':
                word += char
            else:
                if word != "":
                    words.append(word)
                    word = ""
        
        if word != "":
            words.append(word)

        seen = []
        for i in range(len(words)):
            found = False
            for j in range(len(seen)):
                if words[i] == seen[j]:
                    return words[i]
            seen.append(words[i])
        
        return None

if __name__ == "__main__":
    first_repeated_word_finder = Solution()
    string = "This is a test string with some test words"
    print(first_repeated_word_finder.firstRepeatedWord(string))
