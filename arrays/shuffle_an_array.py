# Important | Medium Level
"""
Problem: Shuffle an Array
Topics: Array, Random, Fisher–Yates Shuffle, Design
"""
import random

class Solution:
    # Time Complexity: O(n) for shuffle and O(1) for reset
    # Space Complexity: O(n) for storing the original array
    def __init__(self, nums: list[int]):
        self.original = nums[:]

    def reset(self) -> list[int]:
        return self.original[:]

    def shuffle(self) -> list[int]:
        arr = self.original[:]
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print("Shuffled:", obj.shuffle())
    print("Reset:", obj.reset())
    print("Shuffled again:", obj.shuffle())