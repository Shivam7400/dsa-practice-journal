# Importent | Easy level
"""
Problem: Find the Most Frequent Element (No Counter)
Topics: Array, List, Dictionary
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    def most_frequent(self, lst):
        freq = {}
        for num in lst:
            freq[num] = freq.get(num, 0) + 1

        max_freq_ele = 0
        most_common_ele = None
        for num, count in freq.items():
            if count > max_freq_ele:
                max_freq_ele = count
                most_common_ele = num
        return most_common_ele

if __name__ == "__main__":
    solution = Solution()
    lst = [1, 3, 2, 1, 4, 1, 3]
    print(solution.most_frequent(lst))
