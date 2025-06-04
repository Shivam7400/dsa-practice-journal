# Importent | Medium Level
"""
Problem: Find Pair With Difference
Topics: Array, Two Pointers, Sorting, Hashing (Hash Set), Searching
"""
class Solution:
    # Time Complexity: O(n²)
    # Space Complexity: O(1)
    def find_pair_with_difference(arr, diff):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) == diff:
                    return True
        return False

    
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def find_pair_with_difference(self, arr, diff):
        arr.sort()
        i, j = 0, 1
        while i < len(arr) and j < len(arr):
            if i != j and abs(arr[j] - arr[i]) == diff:
                return True
            elif abs(arr[j] - arr[i]) < diff:
                j += 1
            else:
                i += 1
        return False


if __name__ == "__main__":
    list = [5, 20, 3, 2, 5, 80]
    target = 3
    list = [7, 3, 2, 4, 9, 12, 56]
    
    pair_difference = Solution()
    print(pair_difference.find_pair_with_difference([7, 3, 2, 4, 9, 12, 56], 4))
    print(pair_difference.find_pair_with_difference([5, 20, 3, 2, 5, 80], 78))
    print(pair_difference.find_pair_with_difference([90, 70, 20, 80, 50], 45))
